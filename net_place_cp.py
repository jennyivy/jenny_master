#/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
#    File Name: net_place.py
#       Author: jenny
#        Email: lliu@herobt.com
# Created Time: 2017年08月10日 星期四 11时37分59秒
#########################################################################
import sys
sys.path.append('/home/lliu/model_package')
import json
import pickle
from multiprocessing import Pool
import operator
from collections import OrderedDict
from  util import percentcal as perc
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime as dt


def nets_place(nets, now_dt, city_prov_dic):
    

    init_dict=OrderedDict()
    for key in city_prov_dic.keys():
        init_dict[key]=0.0

    nets_place_prov_count=init_dict
    nets_place_prov_count_perc=init_dict.copy()
    nets_place_prov_min_tot=init_dict.copy()
    nets_place_prov_min_tot_perc=init_dict.copy()
    nets_place_prov_flow_tot=init_dict.copy()
    nets_place_prov_flow_tot_perc=init_dict.copy()
    nets_place_prov_count_6_mon=init_dict.copy()
    nets_place_prov_count_6_mon_perc=init_dict.copy()
    nets_place_prov_min_tot_6_mon=init_dict.copy()
    nets_place_prov_min_tot_6_mon_perc=init_dict.copy()
    nets_place_prov_flow_tot_6_mon=init_dict.copy()
    nets_place_prov_flow_tot_6_mon_perc=init_dict.copy()
    nets_place_prov_count_3_mon = init_dict.copy()
    nets_place_prov_count_3_mon_perc = init_dict.copy()
    nets_place_prov_min_tot_3_mon = init_dict.copy()
    nets_place_prov_min_tot_3_mon_perc = init_dict.copy()
    nets_place_prov_flow_tot_3_mon = init_dict.copy()
    nets_place_prov_flow_tot_3_mon_perc = init_dict.copy()
    nets_place_prov_count_2_mon = init_dict.copy()
    nets_place_prov_count_2_mon_perc = init_dict.copy()
    nets_place_prov_min_tot_2_mon = init_dict.copy()
    nets_place_prov_min_tot_2_mon_perc = init_dict.copy()
    nets_place_prov_flow_tot_2_mon = init_dict.copy()
    nets_place_prov_flow_tot_2_mon_perc = init_dict.copy()
    nets_place_prov_count_1_mon = init_dict.copy()
    nets_place_prov_count_1_mon_perc = init_dict.copy()
    nets_place_prov_min_tot_1_mon = init_dict.copy()
    nets_place_prov_min_tot_1_mon_perc = init_dict.copy()
    nets_place_prov_flow_tot_1_mon = init_dict.copy()
    nets_place_prov_flow_tot_1_mon_perc = init_dict.copy()
    nets_place_prov_count_2_wk = init_dict.copy()
    nets_place_prov_count_2_wk_perc = init_dict.copy()
    nets_place_prov_min_tot_2_wk = init_dict.copy()
    nets_place_prov_min_tot_2_wk_perc = init_dict.copy()
    nets_place_prov_flow_tot_2_wk = init_dict.copy()
    nets_place_prov_flow_tot_2_wk_perc = init_dict.copy()
    nets_place_prov_count_1_wk = init_dict.copy()
    nets_place_prov_count_1_wk_perc = init_dict.copy()
    nets_place_prov_min_tot_1_wk = init_dict.copy()
    nets_place_prov_min_tot_1_wk_perc = init_dict.copy()
    nets_place_prov_flow_tot_1_wk = init_dict.copy()
    nets_place_prov_flow_tot_1_wk_perc = init_dict.copy()

    nets_place_prov_count_6_mon_3_mon_diff = init_dict.copy()
    nets_place_prov_count_6_mon_3_mon_perc_diff = init_dict.copy()
    nets_place_prov_min_tot_6_mon_3_mon_diff = init_dict.copy()
    nets_place_prov_min_tot_6_mon_3_mon_perc_diff = init_dict.copy()
    nets_place_prov_flow_tot_6_mon_3_mon_diff = init_dict.copy()
    nets_place_prov_flow_tot_6_mon_3_mon_perc_diff = init_dict.copy()
    
    nets_place_prov_count_3_mon_2_mon_diff = init_dict.copy()
    nets_place_prov_count_3_mon_2_mon_perc_diff = init_dict.copy()
    nets_place_prov_min_tot_3_mon_2_mon_diff = init_dict.copy()
    nets_place_prov_min_tot_3_mon_2_mon_perc_diff = init_dict.copy()
    nets_place_prov_flow_tot_3_mon_2_mon_diff = init_dict.copy()
    nets_place_prov_flow_tot_3_mon_2_mon_perc_diff = init_dict.copy()
    
    nets_place_prov_count_2_mon_1_mon_diff = init_dict.copy()
    nets_place_prov_count_2_mon_1_mon_perc_diff = init_dict.copy()
    nets_place_prov_min_tot_2_mon_1_mon_diff = init_dict.copy()
    nets_place_prov_min_tot_2_mon_1_mon_perc_diff = init_dict.copy()
    nets_place_prov_flow_tot_2_mon_1_mon_diff = init_dict.copy()
    nets_place_prov_flow_tot_2_mon_1_mon_perc_diff = init_dict.copy()
    
    nets_place_prov_count_1_mon_2_wk_diff = init_dict.copy()
    nets_place_prov_count_1_mon_2_wk_perc_diff = init_dict.copy()
    nets_place_prov_min_tot_1_mon_2_wk_diff = init_dict.copy()
    nets_place_prov_min_tot_1_mon_2_wk_perc_diff = init_dict.copy()
    nets_place_prov_flow_tot_1_mon_2_wk_diff = init_dict.copy()
    nets_place_prov_flow_tot_1_mon_2_wk_perc_diff = init_dict.copy()
    
    nets_place_prov_count_2_wk_1_wk_diff = init_dict.copy()
    nets_place_prov_count_2_wk_1_wk_perc_diff = init_dict.copy()
    nets_place_prov_min_tot_2_wk_1_wk_diff = init_dict.copy()
    nets_place_prov_min_tot_2_wk_1_wk_perc_diff = init_dict.copy()
    nets_place_prov_flow_tot_2_wk_1_wk_diff = init_dict.copy()
    nets_place_prov_flow_tot_2_wk_1_wk_perc_diff = init_dict.copy()

    nets_place_prov_count_tot = 0.0
    nets_place_prov_min_tot_for_all = 0.0
    nets_place_prov_flow_tot_for_all = 0.0
    nets_place_prov_count_tot_6_mon = 0.0
    nets_place_prov_min_tot_for_all_6_mon = 0.0
    nets_place_prov_flow_tot_for_all_6_mon = 0.0
    nets_place_prov_count_tot_3_mon = 0.0
    nets_place_prov_min_tot_for_all_3_mon = 0.0
    nets_place_prov_flow_tot_for_all_3_mon = 0.0
    nets_place_prov_count_tot_2_mon = 0.0
    nets_place_prov_min_tot_for_all_2_mon = 0.0
    nets_place_prov_flow_tot_for_all_2_mon = 0.0
    nets_place_prov_count_tot_1_mon = 0.0
    nets_place_prov_min_tot_for_all_1_mon = 0.0
    nets_place_prov_flow_tot_for_all_1_mon = 0.0
    nets_place_prov_count_tot_2_wk = 0.0
    nets_place_prov_min_tot_for_all_2_wk = 0.0
    nets_place_prov_flow_tot_for_all_2_wk = 0.0
    nets_place_prov_count_tot_1_wk = 0.0
    nets_place_prov_min_tot_for_all_1_wk = 0.0
    nets_place_prov_flow_tot_for_all_1_wk = 0.0

    nets_place_prov_count_tot_6_mon_3_mon_diff = 0.0
    nets_place_prov_min_tot_for_all_6_mon_3_mon_diff = 0.0
    nets_place_prov_flow_tot_for_all_6_mon_3_mon_diff = 0.0
    nets_place_prov_count_tot_3_mon_2_mon_diff = 0.0
    nets_place_prov_min_tot_for_all_3_mon_2_mon_diff = 0.0
    nets_place_prov_flow_tot_for_all_3_mon_2_mon_diff = 0.0
    nets_place_prov_count_tot_2_mon_1_mon_diff = 0.0
    nets_place_prov_min_tot_for_all_2_mon_1_mon_diff = 0.0
    nets_place_prov_flow_tot_for_all_2_mon_1_mon_diff = 0.0
    nets_place_prov_count_tot_1_mon_2_wk_diff = 0.0
    nets_place_prov_min_tot_for_all_1_mon_2_wk_diff = 0.0
    nets_place_prov_flow_tot_for_all_1_mon_2_wk_diff = 0.0
    nets_place_prov_count_tot_2_wk_1_wk_diff = 0.0
    nets_place_prov_min_tot_for_all_2_wk_1_wk_diff = 0.0
    nets_place_prov_flow_tot_for_all_2_wk_1_wk_diff = 0.0


    if nets is not None and nets not in ('null','nul','Null','NULL',''):

        for i, item in enumerate(nets):
            nets_place = item['place']
            usetime=item['useTime']
            subflow=item['subflow']
            try:
                start_time = dt.strptime(item['startTime'], '%Y-%m-%d %H:%M:%S')
            except:
                start_time = now_dt

            spacing_interval = (now_dt - start_time).days
           # print spacing_interval

            if spacing_interval <= 7:
                for k in city_prov_dic.keys():
                    if nets_place in city_prov_dic[k]:
                        nets_place_prov_count_1_wk[k] += 1.0
                        nets_place_prov_count_tot_1_wk += 1.0
                        nets_place_prov_min_tot_1_wk[k] += usetime
                        nets_place_prov_flow_tot_1_wk[k] += subflow
                        nets_place_prov_min_tot_for_all_1_wk += usetime
                        nets_place_prov_flow_tot_for_all_1_wk += subflow
                        nets_place_prov_count_tot += 1.0
                        nets_place_prov_min_tot_for_all += usetime
                        nets_place_prov_flow_tot_for_all += subflow

            elif spacing_interval <= 14:
                for k in city_prov_dic.keys():
                    if nets_place in city_prov_dic[k]:
                        nets_place_prov_count_2_wk[k] += 1.0
                        nets_place_prov_count_tot_2_wk += 1.0
                        nets_place_prov_min_tot_2_wk[k] += usetime
                        nets_place_prov_flow_tot_2_wk[k] += subflow
                        nets_place_prov_min_tot_for_all_2_wk += usetime
                        nets_place_prov_flow_tot_for_all_2_wk += subflow
                        nets_place_prov_count_tot += 1.0
                        nets_place_prov_min_tot_for_all += usetime
                        nets_place_prov_flow_tot_for_all += subflow

            elif spacing_interval <= 30:
                for k in city_prov_dic.keys():
                    if nets_place in city_prov_dic[k]:
                        nets_place_prov_count_1_mon[k] += 1.0
                        nets_place_prov_count_tot_1_mon += 1.0
                        nets_place_prov_min_tot_1_mon[k] += usetime
                        nets_place_prov_flow_tot_1_mon[k] += subflow
                        nets_place_prov_min_tot_for_all_1_mon += usetime
                        nets_place_prov_flow_tot_for_all_1_mon += subflow
                        nets_place_prov_count_tot += 1.0
                        nets_place_prov_min_tot_for_all += usetime
                        nets_place_prov_flow_tot_for_all += subflow

            elif spacing_interval <=60:
                for k in city_prov_dic.keys():
                    if nets_place in city_prov_dic[k]:
                        nets_place_prov_count_2_mon[k]+=1.0
                        nets_place_prov_count_tot_2_mon+=1.0
                        nets_place_prov_min_tot_2_mon[k]+=usetime
                        nets_place_prov_flow_tot_2_mon[k]+=subflow
                        nets_place_prov_min_tot_for_all_2_mon+=usetime
                        nets_place_prov_flow_tot_for_all_2_mon+=subflow
                        nets_place_prov_count_tot+=1.0
                        nets_place_prov_min_tot_for_all+=usetime
                        nets_place_prov_flow_tot_for_all+=subflow

            elif spacing_interval <= 90:
                for k in city_prov_dic.keys():
                    if nets_place in city_prov_dic[k]:
                        nets_place_prov_count_3_mon[k]+=1.0
                        nets_place_prov_count_tot_3_mon+=1.0
                        nets_place_prov_min_tot_3_mon[k]+=usetime
                        nets_place_prov_flow_tot_3_mon[k]+=subflow
                        nets_place_prov_min_tot_for_all_3_mon+=usetime
                        nets_place_prov_flow_tot_for_all_3_mon+=subflow
                        nets_place_prov_count_tot+=1.0
                        nets_place_prov_min_tot_for_all+=usetime
                        nets_place_prov_flow_tot_for_all+=subflow

            elif spacing_interval <= 180:
                for k in city_prov_dic.keys():
                    if nets_place in city_prov_dic[k]:
                        nets_place_prov_count_6_mon[k]+=1.0
                        nets_place_prov_count_tot_6_mon+=1.0
                        nets_place_prov_min_tot_6_mon[k]+=usetime
                        nets_place_prov_flow_tot_6_mon[k]+=subflow
                        nets_place_prov_min_tot_for_all_6_mon+=usetime
                        nets_place_prov_flow_tot_for_all_6_mon+=subflow
                        nets_place_prov_count_tot+=1.0
                        nets_place_prov_min_tot_for_all+=usetime
                        nets_place_prov_flow_tot_for_all+=subflow

        for k in nets_place_prov_count_6_mon.keys():
            nets_place_prov_count_6_mon_3_mon_diff[k] = nets_place_prov_count_6_mon[k] - nets_place_prov_count_3_mon[k]
            nets_place_prov_count_3_mon_2_mon_diff[k] = nets_place_prov_count_3_mon[k] - nets_place_prov_count_2_mon[k]
            nets_place_prov_count_2_mon_1_mon_diff[k] = nets_place_prov_count_2_mon[k] - nets_place_prov_count_1_mon[k]
            nets_place_prov_count_1_mon_2_wk_diff[k] = nets_place_prov_count_1_mon[k] - nets_place_prov_count_2_wk[k]
            nets_place_prov_count_2_wk_1_wk_diff[k] = nets_place_prov_count_2_wk[k] - nets_place_prov_count_1_wk[k]

        for k in nets_place_prov_count_6_mon.keys():
            nets_place_prov_count_6_mon_perc[k]=perc(nets_place_prov_count_6_mon[k], nets_place_prov_count_tot_6_mon)
            nets_place_prov_flow_tot_6_mon_perc[k]=perc(nets_place_prov_flow_tot_6_mon[k], nets_place_prov_flow_tot_for_all_6_mon)
            nets_place_prov_min_tot_6_mon_perc[k]=perc(nets_place_prov_min_tot_6_mon[k], nets_place_prov_min_tot_for_all_6_mon)
        for k in nets_place_prov_count_3_mon.keys():
            nets_place_prov_count_3_mon_perc[k] = perc(nets_place_prov_count_3_mon[k], nets_place_prov_count_tot_3_mon)
            nets_place_prov_flow_tot_3_mon_perc[k] = perc(nets_place_prov_flow_tot_3_mon[k],nets_place_prov_flow_tot_for_all_3_mon)
            nets_place_prov_min_tot_3_mon_perc[k] = perc(nets_place_prov_min_tot_3_mon[k],nets_place_prov_min_tot_for_all_3_mon)
        for k in nets_place_prov_count_2_mon.keys():
            nets_place_prov_count_2_mon_perc[k] = perc(nets_place_prov_count_2_mon[k], nets_place_prov_count_tot_2_mon)
            nets_place_prov_flow_tot_2_mon_perc[k] = perc(nets_place_prov_flow_tot_2_mon[k],nets_place_prov_flow_tot_for_all_2_mon)
            nets_place_prov_min_tot_2_mon_perc[k] = perc(nets_place_prov_min_tot_2_mon[k],nets_place_prov_min_tot_for_all_2_mon)
        for k in nets_place_prov_count_1_mon.keys():
            nets_place_prov_count_1_mon_perc[k] = perc(nets_place_prov_count_1_mon[k], nets_place_prov_count_tot_1_mon)
            nets_place_prov_flow_tot_1_mon_perc[k] = perc(nets_place_prov_flow_tot_1_mon[k],nets_place_prov_flow_tot_for_all_1_mon)
            nets_place_prov_min_tot_1_mon_perc[k] = perc(nets_place_prov_min_tot_1_mon[k],nets_place_prov_min_tot_for_all_1_mon)
        for k in nets_place_prov_count_2_wk.keys():
            nets_place_prov_count_2_wk_perc[k] = perc(nets_place_prov_count_2_wk[k], nets_place_prov_count_tot_2_wk)
            nets_place_prov_flow_tot_2_wk_perc[k] = perc(nets_place_prov_flow_tot_2_wk[k],nets_place_prov_flow_tot_for_all_2_wk)
            nets_place_prov_min_tot_2_wk_perc[k] = perc(nets_place_prov_min_tot_2_wk[k],nets_place_prov_min_tot_for_all_2_wk)
        for k in nets_place_prov_count_1_wk.keys():
            nets_place_prov_count_1_wk_perc[k] = perc(nets_place_prov_count_1_wk[k], nets_place_prov_count_tot_1_wk)
            nets_place_prov_flow_tot_1_wk_perc[k] = perc(nets_place_prov_flow_tot_1_wk[k], nets_place_prov_flow_tot_for_all_1_wk)
            nets_place_prov_min_tot_1_wk_perc[k] = perc(nets_place_prov_min_tot_1_wk[k],nets_place_prov_min_tot_for_all_1_wk)

        for k in nets_place_prov_count_6_mon.keys():
            nets_place_prov_count_6_mon_3_mon_perc_diff[k] = nets_place_prov_count_6_mon_perc[k] - nets_place_prov_count_3_mon_perc[k]
            nets_place_prov_count_3_mon_2_mon_perc_diff[k] = nets_place_prov_count_3_mon_perc[k] - nets_place_prov_count_2_mon_perc[k]
            nets_place_prov_count_2_mon_1_mon_perc_diff[k] = nets_place_prov_count_2_mon_perc[k] - nets_place_prov_count_1_mon_perc[k]
            nets_place_prov_count_1_mon_2_wk_perc_diff[k] = nets_place_prov_count_1_mon_perc[k] - nets_place_prov_count_2_wk_perc[k]
            nets_place_prov_count_2_wk_1_wk_perc_diff[k] = nets_place_prov_count_2_wk_perc[k] - nets_place_prov_count_1_wk_perc[k]


        sorted_nets_place_prov_count_6_mon=sorted(nets_place_prov_count_6_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_6_mon=sorted(nets_place_prov_flow_tot_6_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_6_mon= sorted(nets_place_prov_min_tot_6_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_6_mon_perc= sorted(nets_place_prov_count_6_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_6_mon_perc= sorted(nets_place_prov_flow_tot_6_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_6_mon_perc= sorted(nets_place_prov_min_tot_6_mon_perc.items(), key=operator.itemgetter(0))

        sorted_nets_place_prov_count_3_mon = sorted(nets_place_prov_count_3_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_3_mon = sorted(nets_place_prov_flow_tot_3_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_3_mon = sorted(nets_place_prov_min_tot_3_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_3_mon_perc = sorted(nets_place_prov_count_3_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_3_mon_perc = sorted(nets_place_prov_flow_tot_3_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_3_mon_perc = sorted(nets_place_prov_min_tot_3_mon_perc.items(), key=operator.itemgetter(0))

        sorted_nets_place_prov_count_2_mon = sorted(nets_place_prov_count_2_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_mon = sorted(nets_place_prov_flow_tot_2_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_mon = sorted(nets_place_prov_min_tot_2_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_2_mon_perc = sorted(nets_place_prov_count_2_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_mon_perc = sorted(nets_place_prov_flow_tot_2_mon_perc.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_mon_perc = sorted(nets_place_prov_min_tot_2_mon_perc.items(),key=operator.itemgetter(0))

        sorted_nets_place_prov_count_1_mon = sorted(nets_place_prov_count_1_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_mon = sorted(nets_place_prov_flow_tot_1_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_mon = sorted(nets_place_prov_min_tot_1_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_1_mon_perc = sorted(nets_place_prov_count_1_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_mon_perc = sorted(nets_place_prov_flow_tot_1_mon_perc.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_mon_perc = sorted(nets_place_prov_min_tot_1_mon_perc.items(), key=operator.itemgetter(0))

        sorted_nets_place_prov_count_2_wk = sorted(nets_place_prov_count_2_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_wk = sorted(nets_place_prov_flow_tot_2_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_wk = sorted(nets_place_prov_min_tot_2_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_2_wk_perc = sorted(nets_place_prov_count_2_wk_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_wk_perc = sorted(nets_place_prov_flow_tot_2_wk_perc.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_wk_perc = sorted(nets_place_prov_min_tot_2_wk_perc.items(),key=operator.itemgetter(0))

        sorted_nets_place_prov_count_1_wk = sorted(nets_place_prov_count_1_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_wk = sorted(nets_place_prov_flow_tot_1_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_wk = sorted(nets_place_prov_min_tot_1_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_1_wk_perc = sorted(nets_place_prov_count_1_wk_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_wk_perc = sorted(nets_place_prov_flow_tot_1_wk_perc.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_wk_perc = sorted(nets_place_prov_min_tot_1_wk_perc.items(),key=operator.itemgetter(0))

        sorted_nets_place_prov_count_6_mon_3_mon_diff = sorted(nets_place_prov_count_6_mon_3_mon_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_6_mon_3_mon_diff = sorted(nets_place_prov_flow_tot_6_mon_3_mon_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_6_mon_3_mon_diff = sorted(nets_place_prov_min_tot_6_mon_3_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_count_6_mon_3_mon_perc_diff = sorted(nets_place_prov_count_6_mon_3_mon_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_6_mon_3_mon_perc_diff = sorted(nets_place_prov_flow_tot_6_mon_3_mon_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_6_mon_3_mon_perc_diff = sorted(nets_place_prov_min_tot_6_mon_3_mon_perc_diff.items(),key=operator.itemgetter(0))

        sorted_nets_place_prov_count_3_mon_2_mon_diff = sorted(nets_place_prov_count_3_mon_2_mon_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_3_mon_2_mon_diff = sorted(nets_place_prov_flow_tot_3_mon_2_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_3_mon_2_mon_diff = sorted(nets_place_prov_min_tot_3_mon_2_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_count_3_mon_2_mon_perc_diff = sorted(nets_place_prov_count_3_mon_2_mon_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_3_mon_2_mon_perc_diff = sorted(nets_place_prov_flow_tot_3_mon_2_mon_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_3_mon_2_mon_perc_diff = sorted(nets_place_prov_min_tot_3_mon_2_mon_perc_diff.items(),key=operator.itemgetter(0))

        sorted_nets_place_prov_count_2_mon_1_mon_diff = sorted(nets_place_prov_count_2_mon_1_mon_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_mon_1_mon_diff = sorted(nets_place_prov_flow_tot_2_mon_1_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_mon_1_mon_diff = sorted(nets_place_prov_min_tot_2_mon_1_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_count_2_mon_1_mon_perc_diff = sorted(nets_place_prov_count_2_mon_1_mon_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_mon_1_mon_perc_diff = sorted(nets_place_prov_flow_tot_2_mon_1_mon_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_mon_1_mon_perc_diff = sorted(nets_place_prov_min_tot_2_mon_1_mon_perc_diff.items(),key=operator.itemgetter(0))

        sorted_nets_place_prov_count_1_mon_2_wk_diff = sorted(nets_place_prov_count_1_mon_2_wk_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_mon_2_wk_diff = sorted(nets_place_prov_flow_tot_1_mon_2_wk_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_mon_2_wk_diff = sorted(nets_place_prov_min_tot_1_mon_2_wk_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_count_1_mon_2_wk_perc_diff = sorted(nets_place_prov_count_1_mon_2_wk_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_mon_2_wk_perc_diff = sorted(nets_place_prov_flow_tot_1_mon_2_wk_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_mon_2_wk_perc_diff = sorted(nets_place_prov_min_tot_1_mon_2_wk_perc_diff.items(),key=operator.itemgetter(0))

        sorted_nets_place_prov_count_2_wk_1_wk_diff = sorted(nets_place_prov_count_2_wk_1_wk_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_wk_1_wk_diff = sorted(nets_place_prov_flow_tot_2_wk_1_wk_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_wk_1_wk_diff = sorted(nets_place_prov_min_tot_2_wk_1_wk_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_count_2_wk_1_wk_perc_diff = sorted(nets_place_prov_count_2_wk_1_wk_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_wk_1_wk_perc_diff = sorted(nets_place_prov_flow_tot_2_wk_1_wk_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_wk_1_wk_perc_diff = sorted(nets_place_prov_min_tot_2_wk_1_wk_perc_diff.items(),key=operator.itemgetter(0))

        nets_place_prov_count_tot_6_mon_3_mon_diff = nets_place_prov_count_tot_6_mon - nets_place_prov_count_tot_3_mon
        nets_place_prov_min_tot_for_all_6_mon_3_mon_diff =  nets_place_prov_min_tot_for_all_6_mon-  nets_place_prov_min_tot_for_all_3_mon
        nets_place_prov_flow_tot_for_all_6_mon_3_mon_diff = nets_place_prov_flow_tot_for_all_6_mon- nets_place_prov_flow_tot_for_all_3_mon
        nets_place_prov_count_tot_3_mon_2_mon_diff = nets_place_prov_count_tot_3_mon - nets_place_prov_count_tot_2_mon
        nets_place_prov_min_tot_for_all_3_mon_2_mon_diff =  nets_place_prov_min_tot_for_all_3_mon- nets_place_prov_min_tot_for_all_2_mon
        nets_place_prov_flow_tot_for_all_3_mon_2_mon_diff = nets_place_prov_flow_tot_for_all_3_mon- nets_place_prov_flow_tot_for_all_2_mon
        nets_place_prov_count_tot_2_mon_1_mon_diff =  nets_place_prov_count_tot_2_mon-  nets_place_prov_count_tot_1_mon
        nets_place_prov_min_tot_for_all_2_mon_1_mon_diff = nets_place_prov_min_tot_for_all_2_mon- nets_place_prov_min_tot_for_all_1_mon
        nets_place_prov_flow_tot_for_all_2_mon_1_mon_diff =  nets_place_prov_flow_tot_for_all_2_mon-  nets_place_prov_flow_tot_for_all_1_mon
        nets_place_prov_count_tot_1_mon_2_wk_diff =  nets_place_prov_count_tot_1_mon-  nets_place_prov_count_tot_2_wk
        nets_place_prov_min_tot_for_all_1_mon_2_wk_diff = nets_place_prov_min_tot_for_all_1_mon- nets_place_prov_min_tot_for_all_2_wk
        nets_place_prov_flow_tot_for_all_1_mon_2_wk_diff = nets_place_prov_flow_tot_for_all_1_mon-nets_place_prov_flow_tot_for_all_2_wk
        nets_place_prov_count_tot_2_wk_1_wk_diff =  nets_place_prov_count_tot_2_wk-  nets_place_prov_count_tot_1_wk
        nets_place_prov_min_tot_for_all_2_wk_1_wk_diff = nets_place_prov_min_tot_for_all_2_wk- nets_place_prov_min_tot_for_all_1_wk
        nets_place_prov_flow_tot_for_all_2_wk_1_wk_diff = nets_place_prov_flow_tot_for_all_2_wk- nets_place_prov_flow_tot_for_all_1_wk

        result_list=[v for k, v in sorted_nets_place_prov_count_6_mon]
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_6_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_6_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_6_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_6_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_6_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_3_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_3_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_3_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_3_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_3_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_3_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_wk_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_wk_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_wk_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_wk_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_wk_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_wk_perc])

        result_list.extend([v for k, v in sorted_nets_place_prov_count_6_mon_3_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_6_mon_3_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_6_mon_3_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_6_mon_3_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_6_mon_3_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_6_mon_3_mon_perc_diff])

        result_list.extend([v for k, v in sorted_nets_place_prov_count_3_mon_2_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_3_mon_2_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_3_mon_2_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_3_mon_2_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_3_mon_2_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_3_mon_2_mon_perc_diff])

        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_mon_1_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_mon_1_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_mon_1_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_mon_1_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_mon_1_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_mon_1_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_mon_2_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_mon_2_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_mon_2_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_mon_2_wk_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_mon_2_wk_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_mon_2_wk_perc_diff])

        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_wk_1_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_wk_1_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_wk_1_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_wk_1_wk_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_wk_1_wk_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_wk_1_wk_perc_diff])

        result_list.extend([nets_place_prov_count_tot,
                            nets_place_prov_min_tot_for_all ,
                            nets_place_prov_flow_tot_for_all ,
                            nets_place_prov_count_tot_6_mon ,
                            nets_place_prov_min_tot_for_all_6_mon ,
                            nets_place_prov_flow_tot_for_all_6_mon,
                            nets_place_prov_count_tot_3_mon ,
                            nets_place_prov_min_tot_for_all_3_mon ,
                            nets_place_prov_flow_tot_for_all_3_mon ,
                            nets_place_prov_count_tot_2_mon ,
                            nets_place_prov_min_tot_for_all_2_mon ,
                            nets_place_prov_flow_tot_for_all_2_mon ,
                            nets_place_prov_count_tot_1_mon ,
                            nets_place_prov_min_tot_for_all_1_mon ,
                            nets_place_prov_flow_tot_for_all_1_mon ,
                            nets_place_prov_count_tot_2_wk ,
                            nets_place_prov_min_tot_for_all_2_wk ,
                            nets_place_prov_flow_tot_for_all_2_wk ,
                            nets_place_prov_count_tot_1_wk ,
                            nets_place_prov_min_tot_for_all_1_wk ,
                            nets_place_prov_flow_tot_for_all_1_wk])

        result_list.extend([nets_place_prov_count_tot_6_mon_3_mon_diff,
                            nets_place_prov_min_tot_for_all_6_mon_3_mon_diff,
                            nets_place_prov_flow_tot_for_all_6_mon_3_mon_diff,
                            nets_place_prov_count_tot_3_mon_2_mon_diff,
                            nets_place_prov_min_tot_for_all_3_mon_2_mon_diff,
                            nets_place_prov_flow_tot_for_all_3_mon_2_mon_diff,
                            nets_place_prov_count_tot_2_mon_1_mon_diff,
                            nets_place_prov_min_tot_for_all_2_mon_1_mon_diff,
                            nets_place_prov_flow_tot_for_all_2_mon_1_mon_diff,
                            nets_place_prov_count_tot_1_mon_2_wk_diff,
                            nets_place_prov_min_tot_for_all_1_mon_2_wk_diff,
                            nets_place_prov_flow_tot_for_all_1_mon_2_wk_diff,
                            nets_place_prov_count_tot_2_wk_1_wk_diff,
                            nets_place_prov_min_tot_for_all_2_wk_1_wk_diff ,
                            nets_place_prov_flow_tot_for_all_2_wk_1_wk_diff])



    else:
        sorted_nets_place_prov_count_6_mon=sorted(nets_place_prov_count_6_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_6_mon=sorted(nets_place_prov_flow_tot_6_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_6_mon= sorted(nets_place_prov_min_tot_6_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_6_mon_perc= sorted(nets_place_prov_count_6_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_6_mon_perc= sorted(nets_place_prov_flow_tot_6_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_6_mon_perc= sorted(nets_place_prov_min_tot_6_mon_perc.items(), key=operator.itemgetter(0))

        sorted_nets_place_prov_count_3_mon = sorted(nets_place_prov_count_3_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_3_mon = sorted(nets_place_prov_flow_tot_3_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_3_mon = sorted(nets_place_prov_min_tot_3_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_3_mon_perc = sorted(nets_place_prov_count_3_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_3_mon_perc = sorted(nets_place_prov_flow_tot_3_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_3_mon_perc = sorted(nets_place_prov_min_tot_3_mon_perc.items(), key=operator.itemgetter(0))

        sorted_nets_place_prov_count_2_mon = sorted(nets_place_prov_count_2_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_mon = sorted(nets_place_prov_flow_tot_2_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_mon = sorted(nets_place_prov_min_tot_2_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_2_mon_perc = sorted(nets_place_prov_count_2_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_mon_perc = sorted(nets_place_prov_flow_tot_2_mon_perc.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_mon_perc = sorted(nets_place_prov_min_tot_2_mon_perc.items(),key=operator.itemgetter(0))

        sorted_nets_place_prov_count_1_mon = sorted(nets_place_prov_count_1_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_mon = sorted(nets_place_prov_flow_tot_1_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_mon = sorted(nets_place_prov_min_tot_1_mon.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_1_mon_perc = sorted(nets_place_prov_count_1_mon_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_mon_perc = sorted(nets_place_prov_flow_tot_1_mon_perc.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_mon_perc = sorted(nets_place_prov_min_tot_1_mon_perc.items(), key=operator.itemgetter(0))

        sorted_nets_place_prov_count_2_wk = sorted(nets_place_prov_count_2_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_wk = sorted(nets_place_prov_flow_tot_2_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_wk = sorted(nets_place_prov_min_tot_2_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_2_wk_perc = sorted(nets_place_prov_count_2_wk_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_wk_perc = sorted(nets_place_prov_flow_tot_2_wk_perc.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_wk_perc = sorted(nets_place_prov_min_tot_2_wk_perc.items(),key=operator.itemgetter(0))

        sorted_nets_place_prov_count_1_wk = sorted(nets_place_prov_count_1_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_wk = sorted(nets_place_prov_flow_tot_1_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_wk = sorted(nets_place_prov_min_tot_1_wk.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_count_1_wk_perc = sorted(nets_place_prov_count_1_wk_perc.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_wk_perc = sorted(nets_place_prov_flow_tot_1_wk_perc.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_wk_perc = sorted(nets_place_prov_min_tot_1_wk_perc.items(),key=operator.itemgetter(0))

        sorted_nets_place_prov_count_6_mon_3_mon_diff = sorted(nets_place_prov_count_6_mon_3_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_6_mon_3_mon_diff = sorted(nets_place_prov_flow_tot_6_mon_3_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_6_mon_3_mon_diff = sorted(nets_place_prov_min_tot_6_mon_3_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_count_6_mon_3_mon_perc_diff = sorted(nets_place_prov_count_6_mon_3_mon_perc_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_6_mon_3_mon_perc_diff = sorted(nets_place_prov_flow_tot_6_mon_3_mon_perc_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_6_mon_3_mon_perc_diff = sorted(nets_place_prov_min_tot_6_mon_3_mon_perc_diff.items(), key=operator.itemgetter(0))

        sorted_nets_place_prov_count_3_mon_2_mon_diff = sorted(nets_place_prov_count_3_mon_2_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_3_mon_2_mon_diff = sorted(nets_place_prov_flow_tot_3_mon_2_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_3_mon_2_mon_diff = sorted(nets_place_prov_min_tot_3_mon_2_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_count_3_mon_2_mon_perc_diff = sorted(nets_place_prov_count_3_mon_2_mon_perc_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_3_mon_2_mon_perc_diff = sorted(nets_place_prov_flow_tot_3_mon_2_mon_perc_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_3_mon_2_mon_perc_diff = sorted(nets_place_prov_min_tot_3_mon_2_mon_perc_diff.items(), key=operator.itemgetter(0))

        sorted_nets_place_prov_count_2_mon_1_mon_diff = sorted(nets_place_prov_count_2_mon_1_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_mon_1_mon_diff = sorted(nets_place_prov_flow_tot_2_mon_1_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_mon_1_mon_diff = sorted(nets_place_prov_min_tot_2_mon_1_mon_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_count_2_mon_1_mon_perc_diff = sorted(nets_place_prov_count_2_mon_1_mon_perc_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_mon_1_mon_perc_diff = sorted(nets_place_prov_flow_tot_2_mon_1_mon_perc_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_mon_1_mon_perc_diff = sorted(nets_place_prov_min_tot_2_mon_1_mon_perc_diff.items(), key=operator.itemgetter(0))

        sorted_nets_place_prov_count_1_mon_2_wk_diff = sorted(nets_place_prov_count_1_mon_2_wk_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_mon_2_wk_diff = sorted(nets_place_prov_flow_tot_1_mon_2_wk_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_mon_2_wk_diff = sorted(nets_place_prov_min_tot_1_mon_2_wk_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_count_1_mon_2_wk_perc_diff = sorted(nets_place_prov_count_1_mon_2_wk_perc_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_1_mon_2_wk_perc_diff = sorted(nets_place_prov_flow_tot_1_mon_2_wk_perc_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_1_mon_2_wk_perc_diff = sorted(nets_place_prov_min_tot_1_mon_2_wk_perc_diff.items(), key=operator.itemgetter(0))

        sorted_nets_place_prov_count_2_wk_1_wk_diff = sorted(nets_place_prov_count_2_wk_1_wk_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_wk_1_wk_diff = sorted(nets_place_prov_flow_tot_2_wk_1_wk_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_wk_1_wk_diff = sorted(nets_place_prov_min_tot_2_wk_1_wk_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_count_2_wk_1_wk_perc_diff = sorted(nets_place_prov_count_2_wk_1_wk_perc_diff.items(),key=operator.itemgetter(0))
        sorted_nets_place_prov_flow_tot_2_wk_1_wk_perc_diff = sorted(nets_place_prov_flow_tot_2_wk_1_wk_perc_diff.items(), key=operator.itemgetter(0))
        sorted_nets_place_prov_min_tot_2_wk_1_wk_perc_diff = sorted(nets_place_prov_min_tot_2_wk_1_wk_perc_diff.items(), key=operator.itemgetter(0))

        result_list=[v for k, v in sorted_nets_place_prov_count_6_mon]
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_6_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_6_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_6_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_6_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_6_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_3_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_3_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_3_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_3_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_3_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_3_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_mon])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_mon_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_wk_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_wk_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_wk_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_wk])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_wk_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_wk_perc])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_wk_perc])

        result_list.extend([v for k, v in sorted_nets_place_prov_count_6_mon_3_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_6_mon_3_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_6_mon_3_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_6_mon_3_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_6_mon_3_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_6_mon_3_mon_perc_diff])

        result_list.extend([v for k, v in sorted_nets_place_prov_count_3_mon_2_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_3_mon_2_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_3_mon_2_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_3_mon_2_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_3_mon_2_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_3_mon_2_mon_perc_diff])

        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_mon_1_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_mon_1_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_mon_1_mon_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_mon_1_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_mon_1_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_mon_1_mon_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_mon_2_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_mon_2_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_mon_2_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_1_mon_2_wk_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_1_mon_2_wk_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_1_mon_2_wk_perc_diff])

        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_wk_1_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_wk_1_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_wk_1_wk_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_count_2_wk_1_wk_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_flow_tot_2_wk_1_wk_perc_diff])
        result_list.extend([v for k, v in sorted_nets_place_prov_min_tot_2_wk_1_wk_perc_diff])

        result_list.extend([nets_place_prov_count_tot,
                            nets_place_prov_min_tot_for_all ,
                            nets_place_prov_flow_tot_for_all ,
                            nets_place_prov_count_tot_6_mon ,
                            nets_place_prov_min_tot_for_all_6_mon ,
                            nets_place_prov_flow_tot_for_all_6_mon,
                            nets_place_prov_count_tot_3_mon ,
                            nets_place_prov_min_tot_for_all_3_mon ,
                            nets_place_prov_flow_tot_for_all_3_mon ,
                            nets_place_prov_count_tot_2_mon ,
                            nets_place_prov_min_tot_for_all_2_mon ,
                            nets_place_prov_flow_tot_for_all_2_mon ,
                            nets_place_prov_count_tot_1_mon ,
                            nets_place_prov_min_tot_for_all_1_mon ,
                            nets_place_prov_flow_tot_for_all_1_mon ,
                            nets_place_prov_count_tot_2_wk ,
                            nets_place_prov_min_tot_for_all_2_wk ,
                            nets_place_prov_flow_tot_for_all_2_wk ,
                            nets_place_prov_count_tot_1_wk ,
                            nets_place_prov_min_tot_for_all_1_wk ,
                            nets_place_prov_flow_tot_for_all_1_wk])

        result_list.extend([nets_place_prov_count_tot_6_mon_3_mon_diff,
                            nets_place_prov_min_tot_for_all_6_mon_3_mon_diff,
                            nets_place_prov_flow_tot_for_all_6_mon_3_mon_diff,
                            nets_place_prov_count_tot_3_mon_2_mon_diff,
                            nets_place_prov_min_tot_for_all_3_mon_2_mon_diff,
                            nets_place_prov_flow_tot_for_all_3_mon_2_mon_diff,
                            nets_place_prov_count_tot_2_mon_1_mon_diff,
                            nets_place_prov_min_tot_for_all_2_mon_1_mon_diff,
                            nets_place_prov_flow_tot_for_all_2_mon_1_mon_diff,
                            nets_place_prov_count_tot_1_mon_2_wk_diff,
                            nets_place_prov_min_tot_for_all_1_mon_2_wk_diff,
                            nets_place_prov_flow_tot_for_all_1_mon_2_wk_diff,
                            nets_place_prov_count_tot_2_wk_1_wk_diff,
                            nets_place_prov_min_tot_for_all_2_wk_1_wk_diff,
                            nets_place_prov_flow_tot_for_all_2_wk_1_wk_diff])


    return result_list



if __name__=='__main__':

   # input_file=['/data3/regular_model/2017_0630/modelling/2017_0630_model_21_n_new.txt', '/data3/regular_model/2017_0630/modelling/2017_0630_model_21_n_old.txtaa','/data3/regular_model/2017_0630/modelling/2017_0630_model_21_n_old.txtab','/data3/regular_model/2017_0630/modelling/2017_0630_model_21_n_old.txtac','/data3/regular_model/2017_0630/modelling/2017_0630_model_21_n_old.txtad','/data3/regular_model/2017_0630/modelling/2017_0630_model_21_y_new.txt', '/data3/regular_model/2017_0630/modelling/2017_0630_model_21_y_old.txt','/data3/regular_model/2017_0630/modelling/2017_0630_model_7_n_new.txt','/data3/regular_model/2017_0630/modelling/2017_0630_model_7_n_old.txt','/data3/regular_model/2017_0630/modelling/2017_0630_model_7_y_new.txt','/data3/regular_model/2017_0630/modelling/2017_0630_model_7_y_old.txt']
    input_file='/data3/regular_model/2017_0814/2017_0814_model_7_y.txt'
    with open(input_file) as f:
        for i, lines in enumerate(f):
            if i<=430:   
                json_data=json.loads(lines)
                jxl_call_records=json_data['jxl_call_records']
                updateTime_f = float(json_data['updateTime']) / 1000
                now_dt = dt.fromtimestamp(updateTime_f)
               # print now_dt
                nets_place_list = nets_place(jxl_call_records, now_dt)
                print len(nets_place_list)     
               # print nets_place_list
         

                
  #  out_put_dics=pool.map(nets_place, input_file)

  

