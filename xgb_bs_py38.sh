screen -Sdm Airl-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Airlines  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Airl-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Airl-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm Airl-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Airlines  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Airl-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Airl-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm Airl-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Airlines  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Airl-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Airl-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm chri-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d christine  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_chri-xgb_flaml_woinit-BS_D-0 2>./stdout/err_chri-xgb_flaml_woinit-BS_D-0"
sleep 10s
sleep 1980s
screen -Sdm chri-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d christine  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_chri-xgb_flaml_woinit-BS_D-1 2>./stdout/err_chri-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm chri-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d christine  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_chri-xgb_flaml_woinit-BS_D-2 2>./stdout/err_chri-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm shut-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d shuttle  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_shut-xgb_flaml_woinit-BS_D-0 2>./stdout/err_shut-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm shut-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d shuttle  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_shut-xgb_flaml_woinit-BS_D-1 2>./stdout/err_shut-xgb_flaml_woinit-BS_D-1"
sleep 10s
sleep 1980s
screen -Sdm shut-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d shuttle  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_shut-xgb_flaml_woinit-BS_D-2 2>./stdout/err_shut-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm car-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d car  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_car-xgb_flaml_woinit-BS_D-0 2>./stdout/err_car-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm car-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d car  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_car-xgb_flaml_woinit-BS_D-1 2>./stdout/err_car-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm car-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d car  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_car-xgb_flaml_woinit-BS_D-2 2>./stdout/err_car-xgb_flaml_woinit-BS_D-2"
sleep 10s
sleep 1980s
screen -Sdm cred-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d credit  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_cred-xgb_flaml_woinit-BS_D-0 2>./stdout/err_cred-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm cred-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d credit  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_cred-xgb_flaml_woinit-BS_D-1 2>./stdout/err_cred-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm cred-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d credit  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_cred-xgb_flaml_woinit-BS_D-2 2>./stdout/err_cred-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm conn-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d connect  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_conn-xgb_flaml_woinit-BS_D-0 2>./stdout/err_conn-xgb_flaml_woinit-BS_D-0"
sleep 10s
sleep 1980s
screen -Sdm conn-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d connect  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_conn-xgb_flaml_woinit-BS_D-1 2>./stdout/err_conn-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm conn-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d connect  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_conn-xgb_flaml_woinit-BS_D-2 2>./stdout/err_conn-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm sylv-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d sylvine  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_sylv-xgb_flaml_woinit-BS_D-0 2>./stdout/err_sylv-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm sylv-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d sylvine  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_sylv-xgb_flaml_woinit-BS_D-1 2>./stdout/err_sylv-xgb_flaml_woinit-BS_D-1"
sleep 10s
sleep 1980s
screen -Sdm volk-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d volkert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_volk-xgb_flaml_woinit-BS_D-0 2>./stdout/err_volk-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm volk-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d volkert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_volk-xgb_flaml_woinit-BS_D-1 2>./stdout/err_volk-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm volk-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d volkert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_volk-xgb_flaml_woinit-BS_D-2 2>./stdout/err_volk-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm Mini-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d MiniBooNE  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Mini-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Mini-xgb_flaml_woinit-BS_D-0"
sleep 10s
sleep 1980s
screen -Sdm Mini-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d MiniBooNE  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Mini-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Mini-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm Mini-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d MiniBooNE  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Mini-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Mini-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm Jann-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Jannis  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Jann-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Jann-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm Jann-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Jannis  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Jann-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Jann-xgb_flaml_woinit-BS_D-1"
sleep 10s
sleep 1980s
screen -Sdm Jann-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Jannis  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Jann-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Jann-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm mfea-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d mfeat  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_mfea-xgb_flaml_woinit-BS_D-0 2>./stdout/err_mfea-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm mfea-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d mfeat  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_mfea-xgb_flaml_woinit-BS_D-1 2>./stdout/err_mfea-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm mfea-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d mfeat  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_mfea-xgb_flaml_woinit-BS_D-2 2>./stdout/err_mfea-xgb_flaml_woinit-BS_D-2"
sleep 10s
sleep 1980s
screen -Sdm jung-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d jungle  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_jung-xgb_flaml_woinit-BS_D-0 2>./stdout/err_jung-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm jung-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d jungle  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_jung-xgb_flaml_woinit-BS_D-1 2>./stdout/err_jung-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm jung-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d jungle  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_jung-xgb_flaml_woinit-BS_D-2 2>./stdout/err_jung-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm jasm-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d jasmine  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_jasm-xgb_flaml_woinit-BS_D-0 2>./stdout/err_jasm-xgb_flaml_woinit-BS_D-0"
sleep 10s
sleep 1980s
screen -Sdm fabe-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d fabert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_fabe-xgb_flaml_woinit-BS_D-0 2>./stdout/err_fabe-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm fabe-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d fabert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_fabe-xgb_flaml_woinit-BS_D-1 2>./stdout/err_fabe-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm fabe-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d fabert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_fabe-xgb_flaml_woinit-BS_D-2 2>./stdout/err_fabe-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm segm-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d segment  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_segm-xgb_flaml_woinit-BS_D-0 2>./stdout/err_segm-xgb_flaml_woinit-BS_D-0"
sleep 10s
sleep 1980s
screen -Sdm segm-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d segment  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_segm-xgb_flaml_woinit-BS_D-1 2>./stdout/err_segm-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm segm-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d segment  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_segm-xgb_flaml_woinit-BS_D-2 2>./stdout/err_segm-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm cnae-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d cnae  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_cnae-xgb_flaml_woinit-BS_D-0 2>./stdout/err_cnae-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm cnae-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d cnae  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_cnae-xgb_flaml_woinit-BS_D-1 2>./stdout/err_cnae-xgb_flaml_woinit-BS_D-1"
sleep 10s
sleep 1980s
screen -Sdm cnae-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d cnae  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_cnae-xgb_flaml_woinit-BS_D-2 2>./stdout/err_cnae-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm kc1-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d kc1  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_kc1-xgb_flaml_woinit-BS_D-0 2>./stdout/err_kc1-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm kc1-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d kc1  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_kc1-xgb_flaml_woinit-BS_D-1 2>./stdout/err_kc1-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm kc1-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d kc1  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_kc1-xgb_flaml_woinit-BS_D-2 2>./stdout/err_kc1-xgb_flaml_woinit-BS_D-2"
sleep 10s
sleep 1980s
screen -Sdm kr-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d kr  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_kr-xgb_flaml_woinit-BS_D-0 2>./stdout/err_kr-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm kr-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d kr  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_kr-xgb_flaml_woinit-BS_D-1 2>./stdout/err_kr-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm kr-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d kr  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_kr-xgb_flaml_woinit-BS_D-2 2>./stdout/err_kr-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm Albe-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Albert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Albe-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Albe-xgb_flaml_woinit-BS_D-0"
sleep 10s
sleep 1980s
screen -Sdm Albe-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Albert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Albe-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Albe-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm Albe-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Albert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Albe-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Albe-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm APSF-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d APSFailure  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_APSF-xgb_flaml_woinit-BS_D-0 2>./stdout/err_APSF-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm APSF-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d APSFailure  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_APSF-xgb_flaml_woinit-BS_D-1 2>./stdout/err_APSF-xgb_flaml_woinit-BS_D-1"
sleep 10s
sleep 1980s
screen -Sdm APSF-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d APSFailure  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_APSF-xgb_flaml_woinit-BS_D-2 2>./stdout/err_APSF-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm bank-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d bank  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_bank-xgb_flaml_woinit-BS_D-0 2>./stdout/err_bank-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm bank-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d bank  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_bank-xgb_flaml_woinit-BS_D-1 2>./stdout/err_bank-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm bank-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d bank  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_bank-xgb_flaml_woinit-BS_D-2 2>./stdout/err_bank-xgb_flaml_woinit-BS_D-2"
sleep 10s
sleep 1980s
screen -Sdm noma-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d nomao  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_noma-xgb_flaml_woinit-BS_D-0 2>./stdout/err_noma-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm noma-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d nomao  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_noma-xgb_flaml_woinit-BS_D-1 2>./stdout/err_noma-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm noma-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d nomao  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_noma-xgb_flaml_woinit-BS_D-2 2>./stdout/err_noma-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm nume-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d numerai28  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_nume-xgb_flaml_woinit-BS_D-0 2>./stdout/err_nume-xgb_flaml_woinit-BS_D-0"
sleep 10s
sleep 1980s
screen -Sdm nume-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d numerai28  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_nume-xgb_flaml_woinit-BS_D-1 2>./stdout/err_nume-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm nume-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d numerai28  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_nume-xgb_flaml_woinit-BS_D-2 2>./stdout/err_nume-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm phon-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d phoneme  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_phon-xgb_flaml_woinit-BS_D-0 2>./stdout/err_phon-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm phon-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d phoneme  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_phon-xgb_flaml_woinit-BS_D-1 2>./stdout/err_phon-xgb_flaml_woinit-BS_D-1"
sleep 10s
sleep 1980s
screen -Sdm phon-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d phoneme  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_phon-xgb_flaml_woinit-BS_D-2 2>./stdout/err_phon-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm Hele-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Helena  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Hele-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Hele-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm Hele-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Helena  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Hele-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Hele-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm Hele-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Helena  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Hele-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Hele-xgb_flaml_woinit-BS_D-2"
sleep 10s
sleep 1980s
screen -Sdm KDDC-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d KDDCup09  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_KDDC-xgb_flaml_woinit-BS_D-0 2>./stdout/err_KDDC-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm KDDC-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d KDDCup09  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_KDDC-xgb_flaml_woinit-BS_D-1 2>./stdout/err_KDDC-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm KDDC-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d KDDCup09  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_KDDC-xgb_flaml_woinit-BS_D-2 2>./stdout/err_KDDC-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm adul-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d adult  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_adul-xgb_flaml_woinit-BS_D-0 2>./stdout/err_adul-xgb_flaml_woinit-BS_D-0"
sleep 10s
sleep 1980s
screen -Sdm adul-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d adult  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_adul-xgb_flaml_woinit-BS_D-1 2>./stdout/err_adul-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm adul-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d adult  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_adul-xgb_flaml_woinit-BS_D-2 2>./stdout/err_adul-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm Amaz-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Amazon  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Amaz-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Amaz-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm Amaz-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Amazon  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Amaz-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Amaz-xgb_flaml_woinit-BS_D-1"
sleep 10s
sleep 1980s
screen -Sdm Amaz-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Amazon  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Amaz-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Amaz-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm vehi-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d vehicle  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_vehi-xgb_flaml_woinit-BS_D-0 2>./stdout/err_vehi-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm vehi-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d vehicle  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_vehi-xgb_flaml_woinit-BS_D-1 2>./stdout/err_vehi-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm vehi-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d vehicle  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_vehi-xgb_flaml_woinit-BS_D-2 2>./stdout/err_vehi-xgb_flaml_woinit-BS_D-2"
sleep 10s
sleep 1980s
screen -Sdm bloo-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d blood  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_bloo-xgb_flaml_woinit-BS_D-0 2>./stdout/err_bloo-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm bloo-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d blood  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_bloo-xgb_flaml_woinit-BS_D-1 2>./stdout/err_bloo-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm bloo-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d blood  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_bloo-xgb_flaml_woinit-BS_D-2 2>./stdout/err_bloo-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm Aust-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Australian  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Aust-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Aust-xgb_flaml_woinit-BS_D-0"
sleep 10s
sleep 1980s
screen -Sdm jasm-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d jasmine  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_jasm-xgb_flaml_woinit-BS_D-1 2>./stdout/err_jasm-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm jasm-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d jasmine  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_jasm-xgb_flaml_woinit-BS_D-2 2>./stdout/err_jasm-xgb_flaml_woinit-BS_D-2"
sleep 10s
screen -Sdm higg-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d higgs  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_higg-xgb_flaml_woinit-BS_D-1 2>./stdout/err_higg-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm higg-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d higgs  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_higg-xgb_flaml_woinit-BS_D-2 2>./stdout/err_higg-xgb_flaml_woinit-BS_D-2"
sleep 10s
sleep 1980s
screen -Sdm higg-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d higgs  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_higg-xgb_flaml_woinit-BS_D-0 2>./stdout/err_higg-xgb_flaml_woinit-BS_D-0"
sleep 10s
screen -Sdm Aust-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Australian  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Aust-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Aust-xgb_flaml_woinit-BS_D-1"
sleep 10s
screen -Sdm Aust-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Australian  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Aust-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Aust-xgb_flaml_woinit-BS_D-2"
sleep 10s
# screen -Sdm Dion-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Dionis  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Dion-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Dion-xgb_flaml_woinit-BS_D-0"
# sleep 10s
# screen -Sdm Dion-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Dionis  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Dion-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Dion-xgb_flaml_woinit-BS_D-1"
# sleep 10s
# sleep 1980s
# screen -Sdm Dion-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Dionis  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Dion-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Dion-xgb_flaml_woinit-BS_D-2"
# sleep 10s
# screen -Sdm dilb-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d dilbert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_dilb-xgb_flaml_woinit-BS_D-0 2>./stdout/err_dilb-xgb_flaml_woinit-BS_D-0"
# sleep 10s
# screen -Sdm dilb-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d dilbert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_dilb-xgb_flaml_woinit-BS_D-1 2>./stdout/err_dilb-xgb_flaml_woinit-BS_D-1"
# sleep 10s
# screen -Sdm dilb-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d dilbert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_dilb-xgb_flaml_woinit-BS_D-2 2>./stdout/err_dilb-xgb_flaml_woinit-BS_D-2"
# sleep 10s
# sleep 1980s
# screen -Sdm ricc-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d riccardo  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_ricc-xgb_flaml_woinit-BS_D-2 2>./stdout/err_ricc-xgb_flaml_woinit-BS_D-2"
# sleep 10s
# screen -Sdm ricc-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d riccardo  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_ricc-xgb_flaml_woinit-BS_D-0 2>./stdout/err_ricc-xgb_flaml_woinit-BS_D-0"
# sleep 10s
# screen -Sdm ricc-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d riccardo  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_ricc-xgb_flaml_woinit-BS_D-1 2>./stdout/err_ricc-xgb_flaml_woinit-BS_D-1"
# sleep 10s
# sleep 1980s
# screen -Sdm Cove-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Covertype  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Cove-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Cove-xgb_flaml_woinit-BS_D-0"
# sleep 10s
# screen -Sdm Cove-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Covertype  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Cove-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Cove-xgb_flaml_woinit-BS_D-1"
# sleep 10s
# screen -Sdm Cove-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Covertype  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Cove-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Cove-xgb_flaml_woinit-BS_D-2"
# sleep 10s
# screen -Sdm Robe-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Robert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Robe-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Robe-xgb_flaml_woinit-BS_D-0"
# sleep 10s
# sleep 1980s
# screen -Sdm sylv-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d sylvine  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_sylv-xgb_flaml_woinit-BS_D-2 2>./stdout/err_sylv-xgb_flaml_woinit-BS_D-2"
# sleep 10s
# screen -Sdm guil-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d guillermo  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_guil-xgb_flaml_woinit-BS_D-0 2>./stdout/err_guil-xgb_flaml_woinit-BS_D-0"
# sleep 10s
# screen -Sdm guil-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d guillermo  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_guil-xgb_flaml_woinit-BS_D-1 2>./stdout/err_guil-xgb_flaml_woinit-BS_D-1"
# sleep 10s
# screen -Sdm guil-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d guillermo  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_guil-xgb_flaml_woinit-BS_D-2 2>./stdout/err_guil-xgb_flaml_woinit-BS_D-2"
# sleep 10s
# sleep 1980s
# screen -Sdm Robe-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Robert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Robe-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Robe-xgb_flaml_woinit-BS_D-1"
# sleep 10s
# screen -Sdm Robe-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Robert  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Robe-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Robe-xgb_flaml_woinit-BS_D-2"
# sleep 10s
# screen -Sdm Fash-xgb_flaml_woinit-BS_D-0 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Fashion  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 0 >./stdout/out_Fash-xgb_flaml_woinit-BS_D-0 2>./stdout/err_Fash-xgb_flaml_woinit-BS_D-0"
# sleep 10s
# screen -Sdm Fash-xgb_flaml_woinit-BS_D-1 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Fashion  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 1 >./stdout/out_Fash-xgb_flaml_woinit-BS_D-1 2>./stdout/err_Fash-xgb_flaml_woinit-BS_D-1"
# sleep 10s
# sleep 1980s
# screen -Sdm Fash-xgb_flaml_woinit-BS_D-2 bash -c "python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d Fashion  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 2 >./stdout/out_Fash-xgb_flaml_woinit-BS_D-2 2>./stdout/err_Fash-xgb_flaml_woinit-BS_D-2"
# sleep 10s