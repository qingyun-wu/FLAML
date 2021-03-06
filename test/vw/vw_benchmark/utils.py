
import numpy as np
import matplotlib.pyplot as plt
import itertools
import logging
from .config import WARMSTART_NUM
from .config import FONT_size_label, FONT_size_stick_label, CSFONT, LEGEND_properties
from .config import FINAL_METHOD_line, FINAL_METHOD_marker
from .config import FINAL_METHOD_alias, FINAL_METHOD_color, FINAL_METHOD_alias_key_list
from datetime import datetime
from csv import DictReader
import re
logger = logging.getLogger(__name__)


def convert_tuple_list(tuple_list):
    converted_tuple_list = []
    for element in tuple_list:
        tuple_ = ele_from_nested_tuple(element)
        converted_tuple_list.append(tuple_)
    return converted_tuple_list


def ele_from_nested_tuple(test_tuple):
    res = tuple()
    if type(test_tuple) is int:
        return (test_tuple,)
    else:
        for ele in test_tuple:
            if isinstance(ele, tuple):
                res += ele_from_nested_tuple(ele)
            else:
                res += (ele,)
        return res


def cob_list_of_tuple(list1, list2):
    # get combinatorial list of tuples
    new_list = []
    for i in list1:
        for j in list2:
            new_tuple = (i,) + (j,)
            # TODO: is there a more efficient way to do this?
            if new_tuple not in new_list and ((j,) + (i,)) not in new_list:
                new_list.append(new_tuple)
    return new_list


def plot_obj(obj_list, alg_name='ChaCha', vertical_list=None, demo=False):
    print(obj_list[:5])
    avg_list = [sum(obj_list[:i]) / i for i in range(1, len(obj_list))]
    total_obs = len(avg_list)
    warm_starting_point = 0  # WARMSTART_NUM#  int(total_obs*0.01) #100 #
    if alg_name in FINAL_METHOD_alias:
        alias = FINAL_METHOD_alias[alg_name]
        if demo:
            if 'Naive' in alias:
                alias = 'online learning'
            if 'ChaCha' in alias:
                alias = 'online learning with ChaCha'
            # if 'ExhaustInit' in alias: alias = 'online learning with ChaCha'
        plt.plot(range(warm_starting_point, len(avg_list)), avg_list[warm_starting_point:], color=FINAL_METHOD_color[alg_name], label = alias)
        plt.xlabel('# of data samples', fontsize=FONT_size_label, **CSFONT)
        plt.ylabel('Progressive validation loss', fontsize=FONT_size_label, **CSFONT)
        plt.rcParams['ytick.labelsize'] = FONT_size_stick_label
        plt.yscale('log')
        plt.legend(loc='upper right', prop=LEGEND_properties)


def get_methods_loss_mean_std(loss_dic, result_interval=1, demo_drift=False):
    progressive_loss_dic = {}
    prog_loss_mean_dic = {}
    prog_loss_std_dic = {}
    # converting loss to average loss
    print('converting loss to average loss')
    for k, v in loss_dic.items():
        if demo_drift:
            new_offline_key = k
            progressive_loss_dic[new_offline_key] = []
            for loss_list in v:
                # Do offline learning on 20% of the total data, and treat every 10% of total data as one testing phrase,
                # which means that there are 8 testing phrases
                avg_list = []
                offline_length = int(len(loss_list)*0.2)
                print('offline_length', offline_length)
                testing_phrase_length = round(len(loss_list)*0.1)
                offline_learning_avg_list = [sum(loss_list[:offline_length]) / offline_length for i in
                            range(offline_length)]
                avg_list += offline_learning_avg_list
                total_testing_phrases = 8
                for testing_phrase in range(total_testing_phrases):
                    testing_loss = [sum(loss_list[offline_length+testing_phrase*(testing_phrase_length):offline_length+(testing_phrase+1)*testing_phrase_length]) / testing_phrase_length for i in range(testing_phrase_length)]
                    # testing_loss = [sum(loss_list[:offline_length+testing_phrase*(testing_phrase_length+1)]) / (offline_length+(testing_phrase+1)*(testing_phrase_length+1)) for i in range(testing_phrase_length)]
                    avg_list += testing_loss
                # avg_list = [sum(loss_list[:i * result_interval]) / (i * result_interval) for i in
                #             range(1, int(len(loss_list) / result_interval) - 1)]
                progressive_loss_dic[new_offline_key].append(avg_list)
            progressive_loss_dic[new_offline_key] = np.array(progressive_loss_dic[new_offline_key])
            prog_loss_mean_dic[new_offline_key] = np.mean(progressive_loss_dic[new_offline_key], axis=0)
            prog_loss_std_dic[new_offline_key] = np.std(progressive_loss_dic[new_offline_key], axis=0)
        else:
            progressive_loss_dic[k] = []
            # if 'Offline' not in k:
            for loss_list in v:
                avg_list = [sum(loss_list[:i * result_interval]) / (i * result_interval) for i in
                            range(1, int(len(loss_list) / result_interval) - 1)]
                progressive_loss_dic[k].append(avg_list)
            progressive_loss_dic[k] = np.array(progressive_loss_dic[k])
            prog_loss_mean_dic[k] = np.mean(progressive_loss_dic[k], axis=0)
            prog_loss_std_dic[k] = np.std(progressive_loss_dic[k], axis=0)

    return progressive_loss_dic, prog_loss_mean_dic, prog_loss_std_dic


def plot_progressive_loss_icml(loss_dic, fig_name, result_interval=1, demo_drift=False):
    """Show real-time progressive validation loss

    Args:
        loss_dic [dict]: key: alg_name, value: list of loss list
        fig_name [str]: file name of the figure
    """
    print('--genearting loss figures---')

    # converting loss to average loss
    progressive_loss_dic, prog_loss_mean_dic, prog_loss_std_dic = get_methods_loss_mean_std(loss_dic, result_interval, demo_drift)
    
    # plt.figure()
    fig, ax = plt.subplots(figsize=(8, 6))
    methods_added = []
    method_alias_dic = {}
    for method in progressive_loss_dic.keys():
        method_alias = FINAL_METHOD_alias.get(method, None)
        if method_alias is None and 'ChaCha' in method:
            method_alias = 'ChaCha'
        method_alias_dic[method_alias] = method
        # method_alias_dic[method] = FINAL_METHOD_alias[method]
    for a in FINAL_METHOD_alias_key_list:
        if a in method_alias_dic:
            method = method_alias_dic[a]
        else:
            continue
        method_alias = a
        if method in prog_loss_mean_dic and method_alias not in methods_added:
            avg_list = prog_loss_mean_dic[method]
            std_list = prog_loss_std_dic[method]
            print('prog_loss_mean_dic', prog_loss_mean_dic)
            warm_starting_point = 0  # WARMSTART_NUM  # int(total_obs*0.01) #100 #
            avg_list = avg_list[warm_starting_point:]
            std_list = std_list[warm_starting_point:]
            markevery_number = int(len(avg_list)/10)
            if demo_drift:
                starting_point = int(0.2*len(avg_list))
                print('starting_point', starting_point)
                print('list', avg_list[starting_point:])
            else:
                starting_point = 0
            ax.plot(range(starting_point, len(avg_list)), avg_list[starting_point:], color=FINAL_METHOD_color[method_alias],
                label=method_alias, ls=FINAL_METHOD_line[method_alias], marker=FINAL_METHOD_marker[method_alias],
                markevery=markevery_number, linewidth=1.5)
            ax.fill_between(range(starting_point, len(avg_list)), avg_list[starting_point:] - std_list[starting_point:], avg_list[starting_point:] + std_list[starting_point:],
                            color=FINAL_METHOD_color[method_alias], alpha=0.3)
            methods_added.append(method_alias)
    if demo_drift:
        # ax.axvline(x=0.2*len(avg_list), ymin=0, ymax=1, color='r', ls=':')
        print('length', len(avg_list)*0.2)
        for j in range(9):
            ax.axvline(x=(0.1*j + 0.2)*len(avg_list), ymin=0, ymax=1, color='r', ls=':')
    ax.set_xlabel('# of data samples', fontsize=FONT_size_label)
    ax.set_ylabel('Progressive validation loss', fontsize=FONT_size_label)
    ax.set_xlim([0,len(avg_list)])
    ticks = ax.get_xticks() * int(result_interval)
    plt.ylabel('Progressive validation loss', fontsize=FONT_size_label)
    ax.set_xticklabels(ticks)
    ax.set_yscale('log')
    
    plt.legend(loc='upper right', ncol=2, prop=LEGEND_properties)
    if demo_drift:
        fig_name = fig_name.replace('.pdf', '_drift.pdf')
        ax.set_ylabel('Average loss over time intervals', fontsize=FONT_size_label)
        ax.set_xlim([0,len(avg_list)])
        ax.set_ylim([20, 80])
    print('fig_name', fig_name)
    plt.savefig(fig_name)


def plot_progressive_loss(loss_dic, fig_name, result_interval=1, demo_drift=False):
    """Show real-time progressive validation loss

    Args:
        loss_dic [dict]: key: alg_name, value: list of loss list
        fig_name [str]: file name of the figure
    """
    print('--genearting loss figures---')

    # converting loss to average loss
    progressive_loss_dic, prog_loss_mean_dic, prog_loss_std_dic = get_methods_loss_mean_std(loss_dic, result_interval, demo_drift)
    fig, ax = plt.subplots(figsize=(8, 6))
    methods_added = []
    for method in progressive_loss_dic.keys():
        method_alias = FINAL_METHOD_alias.get(method, method)
        if method in prog_loss_mean_dic and method_alias not in methods_added:
            avg_list = prog_loss_mean_dic[method]
            std_list = prog_loss_std_dic[method]
            print('prog_loss_mean_dic', prog_loss_mean_dic)
            warm_starting_point = 0  # WARMSTART_NUM  # int(total_obs*0.01) #100 #
            avg_list = avg_list[warm_starting_point:]
            std_list = std_list[warm_starting_point:]
            markevery_number = int(len(avg_list)/10)
            if demo_drift:
                starting_point = int(0.2*len(avg_list))
                print('starting_point', starting_point)
                print('list', avg_list[starting_point:])
            else:
                starting_point = 0
            ax.plot(range(starting_point, len(avg_list)), avg_list[starting_point:], 
                label=method_alias, markevery=markevery_number, linewidth=1.5)
            ax.fill_between(range(starting_point, len(avg_list)), avg_list[starting_point:] - std_list[starting_point:], avg_list[starting_point:] + std_list[starting_point:],
                             alpha=0.3)
            methods_added.append(method_alias)
    if demo_drift:
        # ax.axvline(x=0.2*len(avg_list), ymin=0, ymax=1, color='r', ls=':')
        print('length', len(avg_list)*0.2)
        for j in range(9):
            ax.axvline(x=(0.1*j + 0.2)*len(avg_list), ymin=0, ymax=1, color='r', ls=':')
    ax.set_xlabel('# of data samples', fontsize=FONT_size_label)
    ax.set_ylabel('Progressive validation loss', fontsize=FONT_size_label)
    ax.set_xlim([0,len(avg_list)])
    ticks = ax.get_xticks() * int(result_interval)
    plt.ylabel('Progressive validation loss', fontsize=FONT_size_label)
    ax.set_xticklabels(ticks)
    ax.set_yscale('log')
    
    plt.legend(loc='upper right', ncol=2, prop=LEGEND_properties)
    if demo_drift:
        fig_name = fig_name.replace('.pdf', '_drift.pdf')
        ax.set_ylabel('Average loss over time intervals', fontsize=FONT_size_label)
        ax.set_xlim([0,len(avg_list)])
        ax.set_ylim([20, 80])
    print('fig_name', fig_name)
    plt.savefig(fig_name)


def plot_progressive_loss_demo(loss_dic, fig_name, demo_m_list=['Vanilla', 'ChaCha'], fold=0, result_interval=1):
    """Show real-time progressive validation loss

    Args:
        loss_dic [dict]: key: alg_name, value: list of loss list
        fig_name [str]: file name of the figure
    """
    print('genearting loss figures')
    progressive_loss_dic, prog_loss_mean_dic, prog_loss_std_dic = get_methods_loss_mean_std(loss_dic, result_interval)
    plt.figure()
    # fig, ax = plt.subplots()
    methods_added = []
    method_alias_dic = {}
    for method in loss_dic.keys():
        method_alias = FINAL_METHOD_alias[method]
        method_alias_dic[method_alias] = method
        # method_alias_dic[method] = FINAL_METHOD_alias[method]
    for a in FINAL_METHOD_alias_key_list:
        if a in method_alias_dic:
            method = method_alias_dic[a]
        else:
            continue
    # for method in loss_dic.keys():
        method_alias = FINAL_METHOD_alias[method]
        if method in prog_loss_mean_dic and method_alias not in methods_added:
            loss_list = progressive_loss_dic[method][fold]
            warm_starting_point = 10  # WARMSTART_NUM  # int(total_obs*0.01) #100 #
            loss_list = loss_list[warm_starting_point:3000]
            markevery_number = int(len(loss_list)/10)
            if 'Vanilla' in method_alias or 'ChaCha' in method_alias:
                if 'Vanilla' in method_alias:
                    alias = 'online learning'
                if 'ChaCha' in method_alias:
                    alias = 'online learning with ChaCha'
                plt.plot(range(len(loss_list)), loss_list, color=FINAL_METHOD_color[method_alias],
                         label=alias, ls=FINAL_METHOD_line[method_alias], marker=FINAL_METHOD_marker[method_alias],
                         markevery=markevery_number, linewidth=1.5)
                methods_added.append(method_alias)

    plt.xlabel('# of data samples', fontsize=FONT_size_label, **CSFONT)
    plt.ylabel('Progressive validation loss', fontsize=FONT_size_label, **CSFONT)
    plt.rcParams['ytick.labelsize'] = FONT_size_stick_label
    plt.yscale('log')
    plt.legend(loc='upper right', prop=LEGEND_properties)
    plt.savefig(fig_name)
