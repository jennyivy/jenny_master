#/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
#    File Name: qhrisk.py
#       Author: lliu
#        Email: lliu@herobt.com
# Created Time: Sat 03 Dec 2016 04:37:40 PM CST
#########################################################################
import sys
sys.path.append('/home/lliu/model_package')

import string
from util import percentcal as perc
from datetime import datetime as dt

def qhrisk(qh_riskmark, now_dt):
    # qh_riskmark, 前海风险度
    qhrisk_record_cnt = 0
    qhrisk_source_id_A_cnt = 0
    qhrisk_source_id_B_cnt = 0
    qhrisk_source_id_C_cnt = 0
    qhrisk_source_id_oth_cnt = 0
    qhrisk_source_id_A_perc = 0
    qhrisk_source_id_B_perc = 0
    qhrisk_source_id_C_perc = 0
    qhrisk_source_id_oth_perc = 0
    qhrisk_risk_score_A_tot = 0
    qhrisk_risk_score_B_tot = 0
    qhrisk_risk_score_C_tot = 0
    qhrisk_risk_score_oth_tot = 0
    qhrisk_risk_score_A_avg = 0
    qhrisk_risk_score_B_avg = 0
    qhrisk_risk_score_C_avg = 0
    qhrisk_risk_score_oth_avg = 0
    qhrisk_source_id_A_cnt_1_mon = 0
    qhrisk_source_id_A_cnt_2_mon = 0
    qhrisk_source_id_A_cnt_3_mon = 0
    qhrisk_source_id_A_cnt_6_mon = 0
    qhrisk_source_id_A_cnt_12_mon = 0
    qhrisk_source_id_A_cnt_13_mon = 0
    qhrisk_source_id_B_cnt_1_mon = 0
    qhrisk_source_id_B_cnt_2_mon = 0
    qhrisk_source_id_B_cnt_3_mon = 0
    qhrisk_source_id_B_cnt_6_mon = 0
    qhrisk_source_id_B_cnt_12_mon = 0
    qhrisk_source_id_B_cnt_13_mon = 0
    qhrisk_source_id_C_cnt_1_mon = 0
    qhrisk_source_id_C_cnt_2_mon = 0
    qhrisk_source_id_C_cnt_3_mon = 0
    qhrisk_source_id_C_cnt_6_mon = 0
    qhrisk_source_id_C_cnt_12_mon = 0
    qhrisk_source_id_C_cnt_13_mon = 0
    qhrisk_source_id_oth_cnt_1_mon = 0
    qhrisk_source_id_oth_cnt_2_mon = 0
    qhrisk_source_id_oth_cnt_3_mon = 0
    qhrisk_source_id_oth_cnt_6_mon = 0
    qhrisk_source_id_oth_cnt_12_mon = 0
    qhrisk_source_id_oth_cnt_13_mon = 0
    qhrisk_risk_score_A_tot_1_mon = 0
    qhrisk_risk_score_A_tot_2_mon = 0
    qhrisk_risk_score_A_tot_3_mon = 0
    qhrisk_risk_score_A_tot_6_mon = 0
    qhrisk_risk_score_A_tot_12_mon = 0
    qhrisk_risk_score_A_tot_13_mon = 0
    qhrisk_risk_score_A_avg_1_mon = 0
    qhrisk_risk_score_A_avg_2_mon = 0
    qhrisk_risk_score_A_avg_3_mon = 0
    qhrisk_risk_score_A_avg_6_mon = 0
    qhrisk_risk_score_A_avg_12_mon = 0
    qhrisk_risk_score_A_avg_13_mon = 0
    qhrisk_risk_score_B_tot_1_mon = 0
    qhrisk_risk_score_B_tot_2_mon = 0
    qhrisk_risk_score_B_tot_3_mon = 0
    qhrisk_risk_score_B_tot_6_mon = 0
    qhrisk_risk_score_B_tot_12_mon = 0
    qhrisk_risk_score_B_tot_13_mon = 0
    qhrisk_risk_score_B_avg_1_mon = 0
    qhrisk_risk_score_B_avg_2_mon = 0
    qhrisk_risk_score_B_avg_3_mon = 0
    qhrisk_risk_score_B_avg_6_mon = 0
    qhrisk_risk_score_B_avg_12_mon = 0
    qhrisk_risk_score_B_avg_13_mon = 0
    qhrisk_risk_score_C_tot_1_mon = 0
    qhrisk_risk_score_C_tot_2_mon = 0
    qhrisk_risk_score_C_tot_3_mon = 0
    qhrisk_risk_score_C_tot_6_mon = 0
    qhrisk_risk_score_C_tot_12_mon = 0
    qhrisk_risk_score_C_tot_13_mon = 0
    qhrisk_risk_score_C_avg_1_mon = 0
    qhrisk_risk_score_C_avg_2_mon = 0
    qhrisk_risk_score_C_avg_3_mon = 0
    qhrisk_risk_score_C_avg_6_mon = 0
    qhrisk_risk_score_C_avg_12_mon = 0
    qhrisk_risk_score_C_avg_13_mon = 0
    qhrisk_risk_score_oth_tot_1_mon = 0
    qhrisk_risk_score_oth_tot_2_mon = 0
    qhrisk_risk_score_oth_tot_3_mon = 0
    qhrisk_risk_score_oth_tot_6_mon = 0
    qhrisk_risk_score_oth_tot_12_mon = 0
    qhrisk_risk_score_oth_tot_13_mon = 0
    qhrisk_risk_score_oth_avg_1_mon = 0
    qhrisk_risk_score_oth_avg_2_mon = 0
    qhrisk_risk_score_oth_avg_3_mon = 0
    qhrisk_risk_score_oth_avg_6_mon = 0
    qhrisk_risk_score_oth_avg_12_mon = 0
    qhrisk_risk_score_oth_avg_13_mon = 0
    qhrisk_risk_mark_B2_cnt = 0
    qhrisk_risk_mark_B1_cnt = 0
    qhrisk_risk_mark_B3_cnt = 0
    qhrisk_risk_mark_C1_cnt = 0
    qhrisk_risk_mark_C2_cnt = 0
    qhrisk_risk_mark_C3_cnt = 0
    qhrisk_risk_mark_C4_cnt = 0
    qhrisk_risk_mark_oth_cnt = 0
    qhrisk_risk_mark_B2_perc = 0
    qhrisk_risk_mark_B1_perc = 0
    qhrisk_risk_mark_B3_perc = 0
    qhrisk_risk_mark_C1_perc = 0
    qhrisk_risk_mark_C2_perc = 0
    qhrisk_risk_mark_C3_perc = 0
    qhrisk_risk_mark_C4_perc = 0
    qhrisk_risk_mark_oth_perc = 0
    qhrisk_risk_mark_B2_cnt_1_mon = 0
    qhrisk_risk_mark_B2_cnt_2_mon = 0
    qhrisk_risk_mark_B2_cnt_3_mon = 0
    qhrisk_risk_mark_B2_cnt_6_mon = 0
    qhrisk_risk_mark_B2_cnt_12_mon = 0
    qhrisk_risk_mark_B2_cnt_13_mon = 0
    qhrisk_risk_mark_B1_cnt_1_mon = 0
    qhrisk_risk_mark_B1_cnt_2_mon = 0
    qhrisk_risk_mark_B1_cnt_3_mon = 0
    qhrisk_risk_mark_B1_cnt_6_mon = 0
    qhrisk_risk_mark_B1_cnt_12_mon = 0
    qhrisk_risk_mark_B1_cnt_13_mon = 0
    qhrisk_risk_mark_B3_cnt_1_mon = 0
    qhrisk_risk_mark_B3_cnt_2_mon = 0
    qhrisk_risk_mark_B3_cnt_3_mon = 0
    qhrisk_risk_mark_B3_cnt_6_mon = 0
    qhrisk_risk_mark_B3_cnt_12_mon = 0
    qhrisk_risk_mark_B3_cnt_13_mon = 0
    qhrisk_risk_mark_C1_cnt_1_mon = 0
    qhrisk_risk_mark_C1_cnt_2_mon = 0
    qhrisk_risk_mark_C1_cnt_3_mon = 0
    qhrisk_risk_mark_C1_cnt_6_mon = 0
    qhrisk_risk_mark_C1_cnt_12_mon = 0
    qhrisk_risk_mark_C1_cnt_13_mon = 0
    qhrisk_risk_mark_C2_cnt_1_mon = 0
    qhrisk_risk_mark_C2_cnt_2_mon = 0
    qhrisk_risk_mark_C2_cnt_3_mon = 0
    qhrisk_risk_mark_C2_cnt_6_mon = 0
    qhrisk_risk_mark_C2_cnt_12_mon = 0
    qhrisk_risk_mark_C2_cnt_13_mon = 0
    qhrisk_risk_mark_C3_cnt_1_mon = 0
    qhrisk_risk_mark_C3_cnt_2_mon = 0
    qhrisk_risk_mark_C3_cnt_3_mon = 0
    qhrisk_risk_mark_C3_cnt_6_mon = 0
    qhrisk_risk_mark_C3_cnt_12_mon = 0
    qhrisk_risk_mark_C3_cnt_13_mon = 0
    qhrisk_risk_mark_C4_cnt_1_mon = 0
    qhrisk_risk_mark_C4_cnt_2_mon = 0
    qhrisk_risk_mark_C4_cnt_3_mon = 0
    qhrisk_risk_mark_C4_cnt_6_mon = 0
    qhrisk_risk_mark_C4_cnt_12_mon = 0
    qhrisk_risk_mark_C4_cnt_13_mon = 0
    qhrisk_risk_mark_oth_cnt_1_mon = 0
    qhrisk_risk_mark_oth_cnt_2_mon = 0
    qhrisk_risk_mark_oth_cnt_3_mon = 0
    qhrisk_risk_mark_oth_cnt_6_mon = 0
    qhrisk_risk_mark_oth_cnt_12_mon = 0
    qhrisk_risk_mark_oth_cnt_13_mon = 0

    qhrisk_source_id_A_B_cnt_diff= 0
    qhrisk_source_id_B_C_cnt_diff= 0
    qhrisk_source_id_C_oth_cnt_diff= 0
    qhrisk_risk_score_A_B_tot_diff= 0
    qhrisk_risk_score_B_C_tot_diff= 0
    qhrisk_risk_score_C_oth_tot_diff= 0
    qhrisk_risk_score_A_tot_1_mon_2mon_diff= 0
    qhrisk_risk_score_A_tot_2_mon_3mon_diff= 0
    qhrisk_risk_score_A_tot_3_mon_6mon_diff= 0
    qhrisk_risk_score_A_tot_6_mon_12mon_diff= 0
    qhrisk_risk_score_A_tot_12_mon_13mon_diff= 0
    qhrisk_risk_score_B_tot_1_mon_2mon_diff= 0
    qhrisk_risk_score_B_tot_2_mon_3mon_diff= 0
    qhrisk_risk_score_B_tot_3_mon_6mon_diff= 0
    qhrisk_risk_score_B_tot_6_mon_12mon_diff= 0
    qhrisk_risk_score_B_tot_12_mon_13mon_diff= 0
    qhrisk_risk_score_C_tot_1_mon_2mon_diff= 0
    qhrisk_risk_score_C_tot_2_mon_3mon_diff= 0
    qhrisk_risk_score_C_tot_3_mon_6mon_diff= 0
    qhrisk_risk_score_C_tot_6_mon_12mon_diff= 0
    qhrisk_risk_score_C_tot_12_mon_13mon_diff= 0
    qhrisk_risk_score_oth_tot_1_mon_2mon_diff= 0
    qhrisk_risk_score_oth_tot_2_mon_3mon_diff= 0
    qhrisk_risk_score_oth_tot_3_mon_6mon_diff= 0
    qhrisk_risk_score_oth_tot_6_mon_12mon_diff= 0
    qhrisk_risk_score_oth_tot_12_mon_13mon_diff= 0
    qhrisk_risk_mark_B1_B2_cnt_diff= 0
    qhrisk_risk_mark_B2_B3_cnt_diff= 0
    qhrisk_risk_mark_B3_C1_cnt_diff= 0
    qhrisk_risk_mark_C1_C2_cnt_diff= 0
    qhrisk_risk_mark_C2_C3_cnt_diff= 0
    qhrisk_risk_mark_C3_C4_cnt_diff= 0
    qhrisk_risk_mark_C4_oth_cnt_diff= 0
    qhrisk_risk_score_A_avg_1_mon_avg= 0
    qhrisk_risk_score_A_avg_2_mon_avg= 0
    qhrisk_risk_score_A_avg_3_mon_avg= 0
    qhrisk_risk_score_A_avg_6_mon_avg= 0
    qhrisk_risk_score_A_avg_12_mon_avg= 0
    qhrisk_risk_score_A_avg_13_mon_avg= 0
    qhrisk_risk_score_B_avg_1_mon_avg= 0
    qhrisk_risk_score_B_avg_2_mon_avg= 0
    qhrisk_risk_score_B_avg_3_mon_avg= 0
    qhrisk_risk_score_B_avg_6_mon_avg= 0
    qhrisk_risk_score_B_avg_12_mon_avg= 0
    qhrisk_risk_score_B_avg_13_mon_avg= 0
    qhrisk_risk_score_C_avg_1_mon_avg= 0
    qhrisk_risk_score_C_avg_2_mon_avg= 0
    qhrisk_risk_score_C_avg_3_mon_avg= 0
    qhrisk_risk_score_C_avg_6_mon_avg= 0
    qhrisk_risk_score_C_avg_12_mon_avg= 0
    qhrisk_risk_score_C_avg_13_mon_avg= 0
    qhrisk_risk_score_oth_avg_1_mon_avg= 0
    qhrisk_risk_score_oth_avg_2_mon_avg= 0
    qhrisk_risk_score_oth_avg_3_mon_avg= 0
    qhrisk_risk_score_oth_avg_6_mon_avg= 0
    qhrisk_risk_score_oth_avg_12_mon_avg= 0
    qhrisk_risk_score_oth_avg_13_mon_avg= 0


    if qh_riskmark is not None and qh_riskmark not in ('', 'Null', 'null', 'NULL'):
        for ele in qh_riskmark:
            if 'erMsg' not in ele:
                if ele['dataBuildTime'] in ('', '99'):
                    busiDate = dt.strptime('2014-01-01', '%Y-%m-%d')
                else:
                    if len(ele['dataBuildTime']) == 10:
                        busiDate = dt.strptime(ele['dataBuildTime'], '%Y-%m-%d')
                    else:
                        busiDate = dt.strptime(ele['dataBuildTime'].split('.')[0], '%Y-%m-%d %H:%M:%S')
                qhrisk_record_cnt += 1
                if 'rskScore' in ele:
                    rskScore = string.atoi(ele['rskScore'])
                else:
                    rskScore = 0
                if 'rskMark' in ele:
                    rskMark = ele['rskMark']
                else:
                    rskMark = 'oth'
                if ele['sourceId'] == "A":
                    qhrisk_source_id_A_cnt += 1
                    qhrisk_risk_score_A_tot += rskScore
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_source_id_A_cnt_1_mon += 1
                        qhrisk_risk_score_A_tot_1_mon += rskScore
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_source_id_A_cnt_2_mon += 1
                        qhrisk_risk_score_A_tot_2_mon += rskScore
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_source_id_A_cnt_3_mon += 1
                        qhrisk_risk_score_A_tot_3_mon += rskScore
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_source_id_A_cnt_6_mon += 1
                        qhrisk_risk_score_A_tot_6_mon += rskScore
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_source_id_A_cnt_12_mon += 1
                        qhrisk_risk_score_A_tot_12_mon += rskScore
                    else:
                        qhrisk_source_id_A_cnt_13_mon += 1
                        qhrisk_risk_score_A_tot_13_mon += rskScore
                elif ele['sourceId'] == 'B':
                    qhrisk_source_id_B_cnt += 1
                    qhrisk_risk_score_B_tot += rskScore
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_source_id_B_cnt_1_mon += 1
                        qhrisk_risk_score_B_tot_1_mon += rskScore
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_source_id_B_cnt_2_mon += 1
                        qhrisk_risk_score_B_tot_2_mon += rskScore
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_source_id_B_cnt_3_mon += 1
                        qhrisk_risk_score_B_tot_3_mon += rskScore
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_source_id_B_cnt_6_mon += 1
                        qhrisk_risk_score_B_tot_6_mon += rskScore
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_source_id_B_cnt_12_mon += 1
                        qhrisk_risk_score_B_tot_12_mon += rskScore
                    else:
                        qhrisk_source_id_B_cnt_13_mon += 1
                        qhrisk_risk_score_B_tot_13_mon += rskScore
                elif ele['sourceId'] == 'C':
                    qhrisk_source_id_C_cnt += 1
                    qhrisk_risk_score_C_tot += rskScore
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_source_id_C_cnt_1_mon += 1
                        qhrisk_risk_score_C_tot_1_mon += rskScore
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_source_id_C_cnt_2_mon += 1
                        qhrisk_risk_score_C_tot_2_mon += rskScore
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_source_id_C_cnt_3_mon += 1
                        qhrisk_risk_score_C_tot_3_mon += rskScore
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_source_id_C_cnt_6_mon += 1
                        qhrisk_risk_score_C_tot_6_mon += rskScore
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_source_id_C_cnt_12_mon += 1
                        qhrisk_risk_score_C_tot_12_mon += rskScore
                    else:
                        qhrisk_source_id_C_cnt_13_mon += 1
                        qhrisk_risk_score_C_tot_13_mon += rskScore
                else:
                    qhrisk_source_id_oth_cnt += 1
                    qhrisk_risk_score_oth_tot += rskScore
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_source_id_oth_cnt_1_mon += 1
                        qhrisk_risk_score_oth_tot_1_mon += rskScore
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_source_id_oth_cnt_2_mon += 1
                        qhrisk_risk_score_oth_tot_2_mon += rskScore
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_source_id_oth_cnt_3_mon += 1
                        qhrisk_risk_score_oth_tot_3_mon += rskScore
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_source_id_oth_cnt_6_mon += 1
                        qhrisk_risk_score_oth_tot_6_mon += rskScore
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_source_id_oth_cnt_12_mon += 1
                        qhrisk_risk_score_oth_tot_12_mon += rskScore
                    else:
                        qhrisk_source_id_oth_cnt_13_mon += 1
                        qhrisk_risk_score_oth_tot_13_mon += rskScore
                if rskMark == 'B2':
                    qhrisk_risk_mark_B2_cnt += 1
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_risk_mark_B2_cnt_1_mon += 1
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_risk_mark_B2_cnt_2_mon += 1
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_risk_mark_B2_cnt_3_mon += 1
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_risk_mark_B2_cnt_6_mon += 1
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_risk_mark_B2_cnt_12_mon += 1
                    else:
                        qhrisk_risk_mark_B2_cnt_13_mon += 1
                elif rskMark == 'B1':
                    qhrisk_risk_mark_B1_cnt += 1
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_risk_mark_B1_cnt_1_mon += 1
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_risk_mark_B1_cnt_2_mon += 1
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_risk_mark_B1_cnt_3_mon += 1
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_risk_mark_B1_cnt_6_mon += 1
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_risk_mark_B1_cnt_12_mon += 1
                    else:
                        qhrisk_risk_mark_B1_cnt_13_mon += 1
                elif rskMark == 'B3':
                    qhrisk_risk_mark_B3_cnt += 1
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_risk_mark_B3_cnt_1_mon += 1
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_risk_mark_B3_cnt_2_mon += 1
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_risk_mark_B3_cnt_3_mon += 1
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_risk_mark_B3_cnt_6_mon += 1
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_risk_mark_B3_cnt_12_mon += 1
                    else:
                        qhrisk_risk_mark_B3_cnt_13_mon += 1
                elif rskMark == 'C1':
                    qhrisk_risk_mark_C1_cnt += 1
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_risk_mark_C1_cnt_1_mon += 1
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_risk_mark_C1_cnt_2_mon += 1
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_risk_mark_C1_cnt_3_mon += 1
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_risk_mark_C1_cnt_6_mon += 1
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_risk_mark_C1_cnt_12_mon += 1
                    else:
                        qhrisk_risk_mark_C1_cnt_13_mon += 1
                elif rskMark == 'C2':
                    qhrisk_risk_mark_C2_cnt += 1
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_risk_mark_C2_cnt_1_mon += 1
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_risk_mark_C2_cnt_2_mon += 1
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_risk_mark_C2_cnt_3_mon += 1
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_risk_mark_C2_cnt_6_mon += 1
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_risk_mark_C2_cnt_12_mon += 1
                    else:
                        qhrisk_risk_mark_C2_cnt_13_mon += 1
                elif rskMark == 'C3':
                    qhrisk_risk_mark_C3_cnt += 1
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_risk_mark_C3_cnt_1_mon += 1
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_risk_mark_C3_cnt_2_mon += 1
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_risk_mark_C3_cnt_3_mon += 1
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_risk_mark_C3_cnt_6_mon += 1
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_risk_mark_C3_cnt_12_mon += 1
                    else:
                        qhrisk_risk_mark_C3_cnt_13_mon += 1
                elif rskMark == 'C4':
                    qhrisk_risk_mark_C4_cnt += 1
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_risk_mark_C4_cnt_1_mon += 1
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_risk_mark_C4_cnt_2_mon += 1
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_risk_mark_C4_cnt_3_mon += 1
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_risk_mark_C4_cnt_6_mon += 1
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_risk_mark_C4_cnt_12_mon += 1
                    else:
                        qhrisk_risk_mark_C4_cnt_13_mon += 1
                else:
                    qhrisk_risk_mark_oth_cnt += 1
                    if (now_dt - busiDate).days <= 30:
                        qhrisk_risk_mark_oth_cnt_1_mon += 1
                    if (now_dt - busiDate).days <= 60:
                        qhrisk_risk_mark_oth_cnt_2_mon += 1
                    if (now_dt - busiDate).days <= 90:
                        qhrisk_risk_mark_oth_cnt_3_mon += 1
                    if (now_dt - busiDate).days <= 180:
                        qhrisk_risk_mark_oth_cnt_6_mon += 1
                    if (now_dt - busiDate).days <= 360:
                        qhrisk_risk_mark_oth_cnt_12_mon += 1
                    else:
                        qhrisk_risk_mark_oth_cnt_13_mon += 1
        qhrisk_source_id_A_perc = perc(qhrisk_source_id_A_cnt, qhrisk_record_cnt)
        qhrisk_source_id_B_perc = perc(qhrisk_source_id_B_cnt, qhrisk_record_cnt)
        qhrisk_source_id_C_perc = perc(qhrisk_source_id_C_cnt, qhrisk_record_cnt)
        qhrisk_source_id_oth_perc = perc(qhrisk_source_id_oth_cnt, qhrisk_record_cnt)
        qhrisk_risk_score_A_avg = perc(qhrisk_risk_score_A_tot, qhrisk_source_id_A_cnt)
        qhrisk_risk_score_B_avg = perc(qhrisk_risk_score_B_tot, qhrisk_source_id_B_cnt)
        qhrisk_risk_score_C_avg = perc(qhrisk_risk_score_A_tot, qhrisk_source_id_C_cnt)
        qhrisk_risk_score_oth_avg = perc(qhrisk_risk_score_oth_tot, qhrisk_source_id_oth_cnt)
        qhrisk_risk_score_A_avg_1_mon = perc(qhrisk_risk_score_A_tot_1_mon, qhrisk_risk_score_A_tot)
        qhrisk_risk_score_A_avg_2_mon = perc(qhrisk_risk_score_A_tot_2_mon, qhrisk_risk_score_A_tot)
        qhrisk_risk_score_A_avg_3_mon = perc(qhrisk_risk_score_A_tot_3_mon, qhrisk_risk_score_A_tot)
        qhrisk_risk_score_A_avg_6_mon = perc(qhrisk_risk_score_A_tot_6_mon, qhrisk_risk_score_A_tot)
        qhrisk_risk_score_A_avg_12_mon = perc(qhrisk_risk_score_A_tot_12_mon, qhrisk_risk_score_A_tot)
        qhrisk_risk_score_A_avg_13_mon = perc(qhrisk_risk_score_A_tot_13_mon, qhrisk_risk_score_A_tot)
        qhrisk_risk_score_B_avg_1_mon = perc(qhrisk_risk_score_B_tot_1_mon, qhrisk_risk_score_B_tot)
        qhrisk_risk_score_B_avg_2_mon = perc(qhrisk_risk_score_B_tot_2_mon, qhrisk_risk_score_B_tot)
        qhrisk_risk_score_B_avg_3_mon = perc(qhrisk_risk_score_B_tot_3_mon, qhrisk_risk_score_B_tot)
        qhrisk_risk_score_B_avg_6_mon = perc(qhrisk_risk_score_B_tot_6_mon, qhrisk_risk_score_B_tot)
        qhrisk_risk_score_B_avg_12_mon = perc(qhrisk_risk_score_B_tot_12_mon, qhrisk_risk_score_B_tot)
        qhrisk_risk_score_B_avg_13_mon = perc(qhrisk_risk_score_B_tot_13_mon, qhrisk_risk_score_B_tot)
        qhrisk_risk_score_C_avg_1_mon = perc(qhrisk_risk_score_C_tot_1_mon, qhrisk_risk_score_C_tot)
        qhrisk_risk_score_C_avg_2_mon = perc(qhrisk_risk_score_C_tot_2_mon, qhrisk_risk_score_C_tot)
        qhrisk_risk_score_C_avg_3_mon = perc(qhrisk_risk_score_C_tot_3_mon, qhrisk_risk_score_C_tot)
        qhrisk_risk_score_C_avg_6_mon = perc(qhrisk_risk_score_C_tot_6_mon, qhrisk_risk_score_C_tot)
        qhrisk_risk_score_C_avg_12_mon = perc(qhrisk_risk_score_C_tot_12_mon, qhrisk_risk_score_C_tot)
        qhrisk_risk_score_C_avg_13_mon = perc(qhrisk_risk_score_C_tot_13_mon, qhrisk_risk_score_C_tot)
        qhrisk_risk_score_oth_avg_1_mon = perc(qhrisk_risk_score_oth_tot_1_mon, qhrisk_risk_score_oth_tot)
        qhrisk_risk_score_oth_avg_2_mon = perc(qhrisk_risk_score_oth_tot_2_mon, qhrisk_risk_score_oth_tot)
        qhrisk_risk_score_oth_avg_3_mon = perc(qhrisk_risk_score_oth_tot_3_mon, qhrisk_risk_score_oth_tot)
        qhrisk_risk_score_oth_avg_6_mon = perc(qhrisk_risk_score_oth_tot_6_mon, qhrisk_risk_score_oth_tot)
        qhrisk_risk_score_oth_avg_12_mon = perc(qhrisk_risk_score_oth_tot_12_mon, qhrisk_risk_score_oth_tot)
        qhrisk_risk_score_oth_avg_13_mon = perc(qhrisk_risk_score_oth_tot_13_mon, qhrisk_risk_score_oth_tot)
        qhrisk_risk_mark_B2_perc = perc(qhrisk_risk_mark_B2_cnt, qhrisk_record_cnt)
        qhrisk_risk_mark_B1_perc = perc(qhrisk_risk_mark_B1_cnt, qhrisk_record_cnt)
        qhrisk_risk_mark_B3_perc = perc(qhrisk_risk_mark_B3_cnt, qhrisk_record_cnt)
        qhrisk_risk_mark_C1_perc = perc(qhrisk_risk_mark_C1_cnt, qhrisk_record_cnt)
        qhrisk_risk_mark_C2_perc = perc(qhrisk_risk_mark_C2_cnt, qhrisk_record_cnt)
        qhrisk_risk_mark_C3_perc = perc(qhrisk_risk_mark_C3_cnt, qhrisk_record_cnt)
        qhrisk_risk_mark_C4_perc = perc(qhrisk_risk_mark_C4_cnt, qhrisk_record_cnt)
        qhrisk_risk_mark_oth_perc = perc(qhrisk_risk_mark_oth_cnt, qhrisk_record_cnt)

        qhrisk_source_id_A_B_cnt_diff = qhrisk_source_id_B_cnt - qhrisk_source_id_A_cnt
        qhrisk_source_id_B_C_cnt_diff = qhrisk_source_id_C_cnt - qhrisk_source_id_B_cnt
        qhrisk_source_id_C_oth_cnt_diff = qhrisk_source_id_oth_cnt - qhrisk_source_id_C_cnt

        qhrisk_risk_score_A_B_tot_diff = qhrisk_risk_score_B_tot- qhrisk_risk_score_A_tot
        qhrisk_risk_score_B_C_tot_diff = qhrisk_risk_score_C_tot- qhrisk_risk_score_B_tot
        qhrisk_risk_score_C_oth_tot_diff = qhrisk_risk_score_oth_tot- qhrisk_risk_score_C_tot

        qhrisk_risk_score_A_tot_1_mon_2mon_diff = qhrisk_risk_score_A_tot_2_mon - qhrisk_risk_score_A_tot_1_mon
        qhrisk_risk_score_A_tot_2_mon_3mon_diff = qhrisk_risk_score_A_tot_3_mon - qhrisk_risk_score_A_tot_2_mon
        qhrisk_risk_score_A_tot_3_mon_6mon_diff = qhrisk_risk_score_A_tot_6_mon - qhrisk_risk_score_A_tot_3_mon
        qhrisk_risk_score_A_tot_6_mon_12mon_diff = qhrisk_risk_score_A_tot_12_mon - qhrisk_risk_score_A_tot_6_mon
        qhrisk_risk_score_A_tot_12_mon_13mon_diff = qhrisk_risk_score_A_tot_13_mon - qhrisk_risk_score_A_tot_12_mon

        qhrisk_risk_score_B_tot_1_mon_2mon_diff = qhrisk_risk_score_B_tot_2_mon - qhrisk_risk_score_B_tot_1_mon
        qhrisk_risk_score_B_tot_2_mon_3mon_diff = qhrisk_risk_score_B_tot_3_mon - qhrisk_risk_score_B_tot_2_mon
        qhrisk_risk_score_B_tot_3_mon_6mon_diff = qhrisk_risk_score_B_tot_6_mon - qhrisk_risk_score_B_tot_3_mon
        qhrisk_risk_score_B_tot_6_mon_12mon_diff = qhrisk_risk_score_B_tot_12_mon - qhrisk_risk_score_B_tot_6_mon
        qhrisk_risk_score_B_tot_12_mon_13mon_diff = qhrisk_risk_score_B_tot_13_mon - qhrisk_risk_score_B_tot_12_mon


        qhrisk_risk_score_C_tot_1_mon_2mon_diff = qhrisk_risk_score_C_tot_2_mon - qhrisk_risk_score_C_tot_1_mon
        qhrisk_risk_score_C_tot_2_mon_3mon_diff = qhrisk_risk_score_C_tot_3_mon - qhrisk_risk_score_C_tot_2_mon
        qhrisk_risk_score_C_tot_3_mon_6mon_diff = qhrisk_risk_score_C_tot_6_mon - qhrisk_risk_score_C_tot_3_mon
        qhrisk_risk_score_C_tot_6_mon_12mon_diff = qhrisk_risk_score_C_tot_12_mon - qhrisk_risk_score_C_tot_6_mon
        qhrisk_risk_score_C_tot_12_mon_13mon_diff = qhrisk_risk_score_C_tot_13_mon - qhrisk_risk_score_C_tot_12_mon

        qhrisk_risk_score_oth_tot_1_mon_2mon_diff = qhrisk_risk_score_oth_tot_2_mon - qhrisk_risk_score_oth_tot_1_mon
        qhrisk_risk_score_oth_tot_2_mon_3mon_diff = qhrisk_risk_score_oth_tot_3_mon - qhrisk_risk_score_oth_tot_2_mon
        qhrisk_risk_score_oth_tot_3_mon_6mon_diff = qhrisk_risk_score_oth_tot_6_mon - qhrisk_risk_score_oth_tot_3_mon
        qhrisk_risk_score_oth_tot_6_mon_12mon_diff = qhrisk_risk_score_oth_tot_12_mon - qhrisk_risk_score_oth_tot_6_mon
        qhrisk_risk_score_oth_tot_12_mon_13mon_diff = qhrisk_risk_score_oth_tot_13_mon - qhrisk_risk_score_oth_tot_12_mon

        qhrisk_risk_mark_B1_B2_cnt_diff = qhrisk_risk_mark_B1_cnt - qhrisk_risk_mark_B2_cnt
        qhrisk_risk_mark_B2_B3_cnt_diff = qhrisk_risk_mark_B3_cnt - qhrisk_risk_mark_B2_cnt
        qhrisk_risk_mark_B3_C1_cnt_diff = qhrisk_risk_mark_C1_cnt - qhrisk_risk_mark_B3_cnt
        qhrisk_risk_mark_C1_C2_cnt_diff = qhrisk_risk_mark_C2_cnt - qhrisk_risk_mark_C1_cnt
        qhrisk_risk_mark_C2_C3_cnt_diff = qhrisk_risk_mark_C3_cnt - qhrisk_risk_mark_C2_cnt
        qhrisk_risk_mark_C3_C4_cnt_diff = qhrisk_risk_mark_C4_cnt - qhrisk_risk_mark_C3_cnt
        qhrisk_risk_mark_C4_oth_cnt_diff = qhrisk_risk_mark_oth_cnt - qhrisk_risk_mark_C4_cnt

        qhrisk_risk_score_A_avg_1_mon_avg = float(qhrisk_risk_score_A_avg_1_mon)/1
        qhrisk_risk_score_A_avg_2_mon_avg = float(qhrisk_risk_score_A_avg_2_mon)/2
        qhrisk_risk_score_A_avg_3_mon_avg = float(qhrisk_risk_score_A_avg_3_mon)/3
        qhrisk_risk_score_A_avg_6_mon_avg = float(qhrisk_risk_score_A_avg_6_mon)/6
        qhrisk_risk_score_A_avg_12_mon_avg = float(qhrisk_risk_score_A_avg_12_mon)/12
        qhrisk_risk_score_A_avg_13_mon_avg = float(qhrisk_risk_score_A_avg_13_mon)/13

        qhrisk_risk_score_B_avg_1_mon_avg = float(qhrisk_risk_score_B_avg_1_mon)/1
        qhrisk_risk_score_B_avg_2_mon_avg = float(qhrisk_risk_score_B_avg_2_mon)/2
        qhrisk_risk_score_B_avg_3_mon_avg = float(qhrisk_risk_score_B_avg_3_mon)/3
        qhrisk_risk_score_B_avg_6_mon_avg = float(qhrisk_risk_score_B_avg_6_mon)/6
        qhrisk_risk_score_B_avg_12_mon_avg = float(qhrisk_risk_score_B_avg_12_mon)/12
        qhrisk_risk_score_B_avg_13_mon_avg = float(qhrisk_risk_score_B_avg_13_mon)/13

        qhrisk_risk_score_C_avg_1_mon_avg = float(qhrisk_risk_score_C_avg_1_mon)/1
        qhrisk_risk_score_C_avg_2_mon_avg = float(qhrisk_risk_score_C_avg_2_mon)/2
        qhrisk_risk_score_C_avg_3_mon_avg = float(qhrisk_risk_score_C_avg_3_mon)/3
        qhrisk_risk_score_C_avg_6_mon_avg = float(qhrisk_risk_score_C_avg_6_mon)/6
        qhrisk_risk_score_C_avg_12_mon_avg = float(qhrisk_risk_score_C_avg_12_mon)/12
        qhrisk_risk_score_C_avg_13_mon_avg = float(qhrisk_risk_score_C_avg_13_mon)/13


        qhrisk_risk_score_oth_avg_1_mon_avg = float(qhrisk_risk_score_oth_avg_1_mon)/1
        qhrisk_risk_score_oth_avg_2_mon_avg = float(qhrisk_risk_score_oth_avg_2_mon)/2
        qhrisk_risk_score_oth_avg_3_mon_avg = float(qhrisk_risk_score_oth_avg_3_mon)/3
        qhrisk_risk_score_oth_avg_6_mon_avg = float(qhrisk_risk_score_oth_avg_6_mon)/6
        qhrisk_risk_score_oth_avg_12_mon_avg = float(qhrisk_risk_score_oth_avg_12_mon)/12
        qhrisk_risk_score_oth_avg_13_mon_avg = float(qhrisk_risk_score_oth_avg_13_mon)/13



    return [qhrisk_record_cnt,qhrisk_source_id_A_cnt,qhrisk_source_id_B_cnt,qhrisk_source_id_C_cnt,qhrisk_source_id_oth_cnt,qhrisk_source_id_A_perc,qhrisk_source_id_B_perc,qhrisk_source_id_C_perc,qhrisk_source_id_oth_perc,qhrisk_risk_score_A_tot,qhrisk_risk_score_B_tot,qhrisk_risk_score_C_tot,qhrisk_risk_score_oth_tot,qhrisk_risk_score_A_avg,qhrisk_risk_score_B_avg,qhrisk_risk_score_C_avg,qhrisk_risk_score_oth_avg,qhrisk_source_id_A_cnt_1_mon,qhrisk_source_id_A_cnt_2_mon,qhrisk_source_id_A_cnt_3_mon,qhrisk_source_id_A_cnt_6_mon,qhrisk_source_id_A_cnt_12_mon,qhrisk_source_id_A_cnt_13_mon,qhrisk_source_id_B_cnt_1_mon,qhrisk_source_id_B_cnt_2_mon,qhrisk_source_id_B_cnt_3_mon,qhrisk_source_id_B_cnt_6_mon,qhrisk_source_id_B_cnt_12_mon,qhrisk_source_id_B_cnt_13_mon,qhrisk_source_id_C_cnt_1_mon,qhrisk_source_id_C_cnt_2_mon,qhrisk_source_id_C_cnt_3_mon,qhrisk_source_id_C_cnt_6_mon,qhrisk_source_id_C_cnt_12_mon,qhrisk_source_id_C_cnt_13_mon,qhrisk_source_id_oth_cnt_1_mon,qhrisk_source_id_oth_cnt_2_mon,qhrisk_source_id_oth_cnt_3_mon,qhrisk_source_id_oth_cnt_6_mon,qhrisk_source_id_oth_cnt_12_mon,qhrisk_source_id_oth_cnt_13_mon,qhrisk_risk_score_A_tot_1_mon,qhrisk_risk_score_A_tot_2_mon,qhrisk_risk_score_A_tot_3_mon,qhrisk_risk_score_A_tot_6_mon,qhrisk_risk_score_A_tot_12_mon,qhrisk_risk_score_A_tot_13_mon,qhrisk_risk_score_A_avg_1_mon,qhrisk_risk_score_A_avg_2_mon,qhrisk_risk_score_A_avg_3_mon,qhrisk_risk_score_A_avg_6_mon,qhrisk_risk_score_A_avg_12_mon,qhrisk_risk_score_A_avg_13_mon,qhrisk_risk_score_B_tot_1_mon,qhrisk_risk_score_B_tot_2_mon,qhrisk_risk_score_B_tot_3_mon,qhrisk_risk_score_B_tot_6_mon,qhrisk_risk_score_B_tot_12_mon,qhrisk_risk_score_B_tot_13_mon,qhrisk_risk_score_B_avg_1_mon,qhrisk_risk_score_B_avg_2_mon,qhrisk_risk_score_B_avg_3_mon,qhrisk_risk_score_B_avg_6_mon,qhrisk_risk_score_B_avg_12_mon,qhrisk_risk_score_B_avg_13_mon,qhrisk_risk_score_C_tot_1_mon,qhrisk_risk_score_C_tot_2_mon,qhrisk_risk_score_C_tot_3_mon,qhrisk_risk_score_C_tot_6_mon,qhrisk_risk_score_C_tot_12_mon,qhrisk_risk_score_C_tot_13_mon,qhrisk_risk_score_C_avg_1_mon,qhrisk_risk_score_C_avg_2_mon,qhrisk_risk_score_C_avg_3_mon,qhrisk_risk_score_C_avg_6_mon,qhrisk_risk_score_C_avg_12_mon,qhrisk_risk_score_C_avg_13_mon,qhrisk_risk_score_oth_tot_1_mon,qhrisk_risk_score_oth_tot_2_mon,qhrisk_risk_score_oth_tot_3_mon,qhrisk_risk_score_oth_tot_6_mon,qhrisk_risk_score_oth_tot_12_mon,qhrisk_risk_score_oth_tot_13_mon,qhrisk_risk_score_oth_avg_1_mon,qhrisk_risk_score_oth_avg_2_mon,qhrisk_risk_score_oth_avg_3_mon,qhrisk_risk_score_oth_avg_6_mon,qhrisk_risk_score_oth_avg_12_mon,qhrisk_risk_score_oth_avg_13_mon,qhrisk_risk_mark_B2_cnt,qhrisk_risk_mark_B1_cnt,qhrisk_risk_mark_B3_cnt,qhrisk_risk_mark_C1_cnt,qhrisk_risk_mark_C2_cnt,qhrisk_risk_mark_C3_cnt,qhrisk_risk_mark_C4_cnt,qhrisk_risk_mark_oth_cnt,qhrisk_risk_mark_B2_perc,qhrisk_risk_mark_B1_perc,qhrisk_risk_mark_B3_perc,qhrisk_risk_mark_C1_perc,qhrisk_risk_mark_C2_perc,qhrisk_risk_mark_C3_perc,qhrisk_risk_mark_C4_perc,qhrisk_risk_mark_oth_perc,qhrisk_risk_mark_B2_cnt_1_mon,qhrisk_risk_mark_B2_cnt_2_mon,qhrisk_risk_mark_B2_cnt_3_mon,qhrisk_risk_mark_B2_cnt_6_mon,qhrisk_risk_mark_B2_cnt_12_mon,qhrisk_risk_mark_B2_cnt_13_mon,qhrisk_risk_mark_B1_cnt_1_mon,qhrisk_risk_mark_B1_cnt_2_mon,qhrisk_risk_mark_B1_cnt_3_mon,qhrisk_risk_mark_B1_cnt_6_mon,qhrisk_risk_mark_B1_cnt_12_mon,qhrisk_risk_mark_B1_cnt_13_mon,qhrisk_risk_mark_B3_cnt_1_mon,qhrisk_risk_mark_B3_cnt_2_mon,qhrisk_risk_mark_B3_cnt_3_mon,qhrisk_risk_mark_B3_cnt_6_mon,qhrisk_risk_mark_B3_cnt_12_mon,qhrisk_risk_mark_B3_cnt_13_mon,qhrisk_risk_mark_C1_cnt_1_mon,qhrisk_risk_mark_C1_cnt_2_mon,qhrisk_risk_mark_C1_cnt_3_mon,qhrisk_risk_mark_C1_cnt_6_mon,qhrisk_risk_mark_C1_cnt_12_mon,qhrisk_risk_mark_C1_cnt_13_mon,qhrisk_risk_mark_C2_cnt_1_mon,qhrisk_risk_mark_C2_cnt_2_mon,qhrisk_risk_mark_C2_cnt_3_mon,qhrisk_risk_mark_C2_cnt_6_mon,qhrisk_risk_mark_C2_cnt_12_mon,qhrisk_risk_mark_C2_cnt_13_mon,qhrisk_risk_mark_C3_cnt_1_mon,qhrisk_risk_mark_C3_cnt_2_mon,qhrisk_risk_mark_C3_cnt_3_mon,qhrisk_risk_mark_C3_cnt_6_mon,qhrisk_risk_mark_C3_cnt_12_mon,qhrisk_risk_mark_C3_cnt_13_mon,qhrisk_risk_mark_C4_cnt_1_mon,qhrisk_risk_mark_C4_cnt_2_mon,qhrisk_risk_mark_C4_cnt_3_mon,qhrisk_risk_mark_C4_cnt_6_mon,qhrisk_risk_mark_C4_cnt_12_mon,qhrisk_risk_mark_C4_cnt_13_mon,qhrisk_risk_mark_oth_cnt_1_mon,qhrisk_risk_mark_oth_cnt_2_mon,qhrisk_risk_mark_oth_cnt_3_mon,qhrisk_risk_mark_oth_cnt_6_mon,qhrisk_risk_mark_oth_cnt_12_mon,qhrisk_risk_mark_oth_cnt_13_mon, qhrisk_source_id_A_B_cnt_diff,qhrisk_source_id_B_C_cnt_diff, qhrisk_source_id_C_oth_cnt_diff, qhrisk_risk_score_A_B_tot_diff, qhrisk_risk_score_B_C_tot_diff, qhrisk_risk_score_C_oth_tot_diff, qhrisk_risk_score_A_tot_1_mon_2mon_diff, qhrisk_risk_score_A_tot_2_mon_3mon_diff, qhrisk_risk_score_A_tot_3_mon_6mon_diff, qhrisk_risk_score_A_tot_6_mon_12mon_diff,qhrisk_risk_score_A_tot_12_mon_13mon_diff, qhrisk_risk_score_B_tot_1_mon_2mon_diff, qhrisk_risk_score_B_tot_2_mon_3mon_diff, qhrisk_risk_score_B_tot_3_mon_6mon_diff,qhrisk_risk_score_B_tot_6_mon_12mon_diff, qhrisk_risk_score_B_tot_12_mon_13mon_diff, qhrisk_risk_score_C_tot_1_mon_2mon_diff, qhrisk_risk_score_C_tot_2_mon_3mon_diff, qhrisk_risk_score_C_tot_3_mon_6mon_diff, qhrisk_risk_score_C_tot_6_mon_12mon_diff, qhrisk_risk_score_C_tot_12_mon_13mon_diff, qhrisk_risk_score_oth_tot_1_mon_2mon_diff,   qhrisk_risk_score_oth_tot_2_mon_3mon_diff, qhrisk_risk_score_oth_tot_3_mon_6mon_diff, qhrisk_risk_score_oth_tot_6_mon_12mon_diff, qhrisk_risk_score_oth_tot_12_mon_13mon_diff,qhrisk_risk_mark_B1_B2_cnt_diff, qhrisk_risk_mark_B2_B3_cnt_diff, qhrisk_risk_mark_B3_C1_cnt_diff, qhrisk_risk_mark_C1_C2_cnt_diff, qhrisk_risk_mark_C2_C3_cnt_diff, qhrisk_risk_mark_C3_C4_cnt_diff, qhrisk_risk_mark_C4_oth_cnt_diff,qhrisk_risk_score_A_avg_1_mon_avg, qhrisk_risk_score_A_avg_2_mon_avg, qhrisk_risk_score_A_avg_3_mon_avg, qhrisk_risk_score_A_avg_6_mon_avg, qhrisk_risk_score_A_avg_12_mon_avg, qhrisk_risk_score_A_avg_13_mon_avg, qhrisk_risk_score_B_avg_1_mon_avg, qhrisk_risk_score_B_avg_2_mon_avg, qhrisk_risk_score_B_avg_3_mon_avg , qhrisk_risk_score_B_avg_6_mon_avg, qhrisk_risk_score_B_avg_12_mon_avg, qhrisk_risk_score_B_avg_13_mon_avg, qhrisk_risk_score_C_avg_1_mon_avg, qhrisk_risk_score_C_avg_2_mon_avg, qhrisk_risk_score_C_avg_3_mon_avg, qhrisk_risk_score_C_avg_6_mon_avg, qhrisk_risk_score_C_avg_12_mon_avg , qhrisk_risk_score_C_avg_13_mon_avg, qhrisk_risk_score_oth_avg_1_mon_avg,  qhrisk_risk_score_oth_avg_2_mon_avg, qhrisk_risk_score_oth_avg_3_mon_avg,  qhrisk_risk_score_oth_avg_6_mon_avg, qhrisk_risk_score_oth_avg_12_mon_avg, qhrisk_risk_score_oth_avg_13_mon_avg]
