# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: rick
    @contact: xurui@herobt.com
    @file: jxl_call_time.py
    @time: 2017/5/8 14:05
"""

from datetime import datetime as dt
from util import percentcal as perc


def jxl_time(jxl_call_records, now_dt):
    """

    :param jxl_call_records: 聚信立通话记录
        {
            "callType":"国内通话",
            "cellPhone":"18615618575",
            "initType":"被叫",
            "otherCellPhone":"18653330009",
            "place":"山东淄博",
            "startTime":"2016-11-08 17:47:07",
            "subtotal":0,
            "updateTime":"2016-11-09 06:08:50",
            "useTime":9
        }
    :param now_dt: 聚信立抓取的时间
    :param mainContact1Phone: 第一个紧急联系人
    :param mainContact2Phone: 第二个紧急联系人
    :param moreContact: 更多联系人
    :return:
    """

    contact_cnt_tot = 0
    contact_min_tot = 0

    contact_hour_0_cnt_6_mon = 0
    contact_hour_1_cnt_6_mon = 0
    contact_hour_2_cnt_6_mon = 0
    contact_hour_3_cnt_6_mon = 0
    contact_hour_4_cnt_6_mon = 0
    contact_hour_5_cnt_6_mon = 0
    contact_hour_6_cnt_6_mon = 0
    contact_hour_7_cnt_6_mon = 0
    contact_hour_8_cnt_6_mon = 0
    contact_hour_9_cnt_6_mon = 0
    contact_hour_10_cnt_6_mon = 0
    contact_hour_11_cnt_6_mon = 0
    contact_hour_12_cnt_6_mon = 0
    contact_hour_13_cnt_6_mon = 0
    contact_hour_14_cnt_6_mon = 0
    contact_hour_15_cnt_6_mon = 0
    contact_hour_16_cnt_6_mon = 0
    contact_hour_17_cnt_6_mon = 0
    contact_hour_18_cnt_6_mon = 0
    contact_hour_19_cnt_6_mon = 0
    contact_hour_20_cnt_6_mon = 0
    contact_hour_21_cnt_6_mon = 0
    contact_hour_22_cnt_6_mon = 0
    contact_hour_23_cnt_6_mon = 0

    contact_hour_0_min_tot_6_mon = 0
    contact_hour_1_min_tot_6_mon = 0
    contact_hour_2_min_tot_6_mon = 0
    contact_hour_3_min_tot_6_mon = 0
    contact_hour_4_min_tot_6_mon = 0
    contact_hour_5_min_tot_6_mon = 0
    contact_hour_6_min_tot_6_mon = 0
    contact_hour_7_min_tot_6_mon = 0
    contact_hour_8_min_tot_6_mon = 0
    contact_hour_9_min_tot_6_mon = 0
    contact_hour_10_min_tot_6_mon = 0
    contact_hour_11_min_tot_6_mon = 0
    contact_hour_12_min_tot_6_mon = 0
    contact_hour_13_min_tot_6_mon = 0
    contact_hour_14_min_tot_6_mon = 0
    contact_hour_15_min_tot_6_mon = 0
    contact_hour_16_min_tot_6_mon = 0
    contact_hour_17_min_tot_6_mon = 0
    contact_hour_18_min_tot_6_mon = 0
    contact_hour_19_min_tot_6_mon = 0
    contact_hour_20_min_tot_6_mon = 0
    contact_hour_21_min_tot_6_mon = 0
    contact_hour_22_min_tot_6_mon = 0
    contact_hour_23_min_tot_6_mon = 0

    contact_hour_0_call_cnt_6_mon = 0
    contact_hour_1_call_cnt_6_mon = 0
    contact_hour_2_call_cnt_6_mon = 0
    contact_hour_3_call_cnt_6_mon = 0
    contact_hour_4_call_cnt_6_mon = 0
    contact_hour_5_call_cnt_6_mon = 0
    contact_hour_6_call_cnt_6_mon = 0
    contact_hour_7_call_cnt_6_mon = 0
    contact_hour_8_call_cnt_6_mon = 0
    contact_hour_9_call_cnt_6_mon = 0
    contact_hour_10_call_cnt_6_mon = 0
    contact_hour_11_call_cnt_6_mon = 0
    contact_hour_12_call_cnt_6_mon = 0
    contact_hour_13_call_cnt_6_mon = 0
    contact_hour_14_call_cnt_6_mon = 0
    contact_hour_15_call_cnt_6_mon = 0
    contact_hour_16_call_cnt_6_mon = 0
    contact_hour_17_call_cnt_6_mon = 0
    contact_hour_18_call_cnt_6_mon = 0
    contact_hour_19_call_cnt_6_mon = 0
    contact_hour_20_call_cnt_6_mon = 0
    contact_hour_21_call_cnt_6_mon = 0
    contact_hour_22_call_cnt_6_mon = 0
    contact_hour_23_call_cnt_6_mon = 0

    contact_hour_0_call_min_tot_6_mon = 0
    contact_hour_1_call_min_tot_6_mon = 0
    contact_hour_2_call_min_tot_6_mon = 0
    contact_hour_3_call_min_tot_6_mon = 0
    contact_hour_4_call_min_tot_6_mon = 0
    contact_hour_5_call_min_tot_6_mon = 0
    contact_hour_6_call_min_tot_6_mon = 0
    contact_hour_7_call_min_tot_6_mon = 0
    contact_hour_8_call_min_tot_6_mon = 0
    contact_hour_9_call_min_tot_6_mon = 0
    contact_hour_10_call_min_tot_6_mon = 0
    contact_hour_11_call_min_tot_6_mon = 0
    contact_hour_12_call_min_tot_6_mon = 0
    contact_hour_13_call_min_tot_6_mon = 0
    contact_hour_14_call_min_tot_6_mon = 0
    contact_hour_15_call_min_tot_6_mon = 0
    contact_hour_16_call_min_tot_6_mon = 0
    contact_hour_17_call_min_tot_6_mon = 0
    contact_hour_18_call_min_tot_6_mon = 0
    contact_hour_19_call_min_tot_6_mon = 0
    contact_hour_20_call_min_tot_6_mon = 0
    contact_hour_21_call_min_tot_6_mon = 0
    contact_hour_22_call_min_tot_6_mon = 0
    contact_hour_23_call_min_tot_6_mon = 0

    contact_hour_0_rece_cnt_6_mon = 0
    contact_hour_1_rece_cnt_6_mon = 0
    contact_hour_2_rece_cnt_6_mon = 0
    contact_hour_3_rece_cnt_6_mon = 0
    contact_hour_4_rece_cnt_6_mon = 0
    contact_hour_5_rece_cnt_6_mon = 0
    contact_hour_6_rece_cnt_6_mon = 0
    contact_hour_7_rece_cnt_6_mon = 0
    contact_hour_8_rece_cnt_6_mon = 0
    contact_hour_9_rece_cnt_6_mon = 0
    contact_hour_10_rece_cnt_6_mon = 0
    contact_hour_11_rece_cnt_6_mon = 0
    contact_hour_12_rece_cnt_6_mon = 0
    contact_hour_13_rece_cnt_6_mon = 0
    contact_hour_14_rece_cnt_6_mon = 0
    contact_hour_15_rece_cnt_6_mon = 0
    contact_hour_16_rece_cnt_6_mon = 0
    contact_hour_17_rece_cnt_6_mon = 0
    contact_hour_18_rece_cnt_6_mon = 0
    contact_hour_19_rece_cnt_6_mon = 0
    contact_hour_20_rece_cnt_6_mon = 0
    contact_hour_21_rece_cnt_6_mon = 0
    contact_hour_22_rece_cnt_6_mon = 0
    contact_hour_23_rece_cnt_6_mon = 0

    contact_hour_0_rece_min_tot_6_mon = 0
    contact_hour_1_rece_min_tot_6_mon = 0
    contact_hour_2_rece_min_tot_6_mon = 0
    contact_hour_3_rece_min_tot_6_mon = 0
    contact_hour_4_rece_min_tot_6_mon = 0
    contact_hour_5_rece_min_tot_6_mon = 0
    contact_hour_6_rece_min_tot_6_mon = 0
    contact_hour_7_rece_min_tot_6_mon = 0
    contact_hour_8_rece_min_tot_6_mon = 0
    contact_hour_9_rece_min_tot_6_mon = 0
    contact_hour_10_rece_min_tot_6_mon = 0
    contact_hour_11_rece_min_tot_6_mon = 0
    contact_hour_12_rece_min_tot_6_mon = 0
    contact_hour_13_rece_min_tot_6_mon = 0
    contact_hour_14_rece_min_tot_6_mon = 0
    contact_hour_15_rece_min_tot_6_mon = 0
    contact_hour_16_rece_min_tot_6_mon = 0
    contact_hour_17_rece_min_tot_6_mon = 0
    contact_hour_18_rece_min_tot_6_mon = 0
    contact_hour_19_rece_min_tot_6_mon = 0
    contact_hour_20_rece_min_tot_6_mon = 0
    contact_hour_21_rece_min_tot_6_mon = 0
    contact_hour_22_rece_min_tot_6_mon = 0
    contact_hour_23_rece_min_tot_6_mon = 0

    contact_hour_0_cnt_3_mon = 0
    contact_hour_1_cnt_3_mon = 0
    contact_hour_2_cnt_3_mon = 0
    contact_hour_3_cnt_3_mon = 0
    contact_hour_4_cnt_3_mon = 0
    contact_hour_5_cnt_3_mon = 0
    contact_hour_6_cnt_3_mon = 0
    contact_hour_7_cnt_3_mon = 0
    contact_hour_8_cnt_3_mon = 0
    contact_hour_9_cnt_3_mon = 0
    contact_hour_10_cnt_3_mon = 0
    contact_hour_11_cnt_3_mon = 0
    contact_hour_12_cnt_3_mon = 0
    contact_hour_13_cnt_3_mon = 0
    contact_hour_14_cnt_3_mon = 0
    contact_hour_15_cnt_3_mon = 0
    contact_hour_16_cnt_3_mon = 0
    contact_hour_17_cnt_3_mon = 0
    contact_hour_18_cnt_3_mon = 0
    contact_hour_19_cnt_3_mon = 0
    contact_hour_20_cnt_3_mon = 0
    contact_hour_21_cnt_3_mon = 0
    contact_hour_22_cnt_3_mon = 0
    contact_hour_23_cnt_3_mon = 0

    contact_hour_0_min_tot_3_mon = 0
    contact_hour_1_min_tot_3_mon = 0
    contact_hour_2_min_tot_3_mon = 0
    contact_hour_3_min_tot_3_mon = 0
    contact_hour_4_min_tot_3_mon = 0
    contact_hour_5_min_tot_3_mon = 0
    contact_hour_6_min_tot_3_mon = 0
    contact_hour_7_min_tot_3_mon = 0
    contact_hour_8_min_tot_3_mon = 0
    contact_hour_9_min_tot_3_mon = 0
    contact_hour_10_min_tot_3_mon = 0
    contact_hour_11_min_tot_3_mon = 0
    contact_hour_12_min_tot_3_mon = 0
    contact_hour_13_min_tot_3_mon = 0
    contact_hour_14_min_tot_3_mon = 0
    contact_hour_15_min_tot_3_mon = 0
    contact_hour_16_min_tot_3_mon = 0
    contact_hour_17_min_tot_3_mon = 0
    contact_hour_18_min_tot_3_mon = 0
    contact_hour_19_min_tot_3_mon = 0
    contact_hour_20_min_tot_3_mon = 0
    contact_hour_21_min_tot_3_mon = 0
    contact_hour_22_min_tot_3_mon = 0
    contact_hour_23_min_tot_3_mon = 0

    contact_hour_0_call_cnt_3_mon = 0
    contact_hour_1_call_cnt_3_mon = 0
    contact_hour_2_call_cnt_3_mon = 0
    contact_hour_3_call_cnt_3_mon = 0
    contact_hour_4_call_cnt_3_mon = 0
    contact_hour_5_call_cnt_3_mon = 0
    contact_hour_6_call_cnt_3_mon = 0
    contact_hour_7_call_cnt_3_mon = 0
    contact_hour_8_call_cnt_3_mon = 0
    contact_hour_9_call_cnt_3_mon = 0
    contact_hour_10_call_cnt_3_mon = 0
    contact_hour_11_call_cnt_3_mon = 0
    contact_hour_12_call_cnt_3_mon = 0
    contact_hour_13_call_cnt_3_mon = 0
    contact_hour_14_call_cnt_3_mon = 0
    contact_hour_15_call_cnt_3_mon = 0
    contact_hour_16_call_cnt_3_mon = 0
    contact_hour_17_call_cnt_3_mon = 0
    contact_hour_18_call_cnt_3_mon = 0
    contact_hour_19_call_cnt_3_mon = 0
    contact_hour_20_call_cnt_3_mon = 0
    contact_hour_21_call_cnt_3_mon = 0
    contact_hour_22_call_cnt_3_mon = 0
    contact_hour_23_call_cnt_3_mon = 0

    contact_hour_0_call_min_tot_3_mon = 0
    contact_hour_1_call_min_tot_3_mon = 0
    contact_hour_2_call_min_tot_3_mon = 0
    contact_hour_3_call_min_tot_3_mon = 0
    contact_hour_4_call_min_tot_3_mon = 0
    contact_hour_5_call_min_tot_3_mon = 0
    contact_hour_6_call_min_tot_3_mon = 0
    contact_hour_7_call_min_tot_3_mon = 0
    contact_hour_8_call_min_tot_3_mon = 0
    contact_hour_9_call_min_tot_3_mon = 0
    contact_hour_10_call_min_tot_3_mon = 0
    contact_hour_11_call_min_tot_3_mon = 0
    contact_hour_12_call_min_tot_3_mon = 0
    contact_hour_13_call_min_tot_3_mon = 0
    contact_hour_14_call_min_tot_3_mon = 0
    contact_hour_15_call_min_tot_3_mon = 0
    contact_hour_16_call_min_tot_3_mon = 0
    contact_hour_17_call_min_tot_3_mon = 0
    contact_hour_18_call_min_tot_3_mon = 0
    contact_hour_19_call_min_tot_3_mon = 0
    contact_hour_20_call_min_tot_3_mon = 0
    contact_hour_21_call_min_tot_3_mon = 0
    contact_hour_22_call_min_tot_3_mon = 0
    contact_hour_23_call_min_tot_3_mon = 0

    contact_hour_0_rece_cnt_3_mon = 0
    contact_hour_1_rece_cnt_3_mon = 0
    contact_hour_2_rece_cnt_3_mon = 0
    contact_hour_3_rece_cnt_3_mon = 0
    contact_hour_4_rece_cnt_3_mon = 0
    contact_hour_5_rece_cnt_3_mon = 0
    contact_hour_6_rece_cnt_3_mon = 0
    contact_hour_7_rece_cnt_3_mon = 0
    contact_hour_8_rece_cnt_3_mon = 0
    contact_hour_9_rece_cnt_3_mon = 0
    contact_hour_10_rece_cnt_3_mon = 0
    contact_hour_11_rece_cnt_3_mon = 0
    contact_hour_12_rece_cnt_3_mon = 0
    contact_hour_13_rece_cnt_3_mon = 0
    contact_hour_14_rece_cnt_3_mon = 0
    contact_hour_15_rece_cnt_3_mon = 0
    contact_hour_16_rece_cnt_3_mon = 0
    contact_hour_17_rece_cnt_3_mon = 0
    contact_hour_18_rece_cnt_3_mon = 0
    contact_hour_19_rece_cnt_3_mon = 0
    contact_hour_20_rece_cnt_3_mon = 0
    contact_hour_21_rece_cnt_3_mon = 0
    contact_hour_22_rece_cnt_3_mon = 0
    contact_hour_23_rece_cnt_3_mon = 0

    contact_hour_0_rece_min_tot_3_mon = 0
    contact_hour_1_rece_min_tot_3_mon = 0
    contact_hour_2_rece_min_tot_3_mon = 0
    contact_hour_3_rece_min_tot_3_mon = 0
    contact_hour_4_rece_min_tot_3_mon = 0
    contact_hour_5_rece_min_tot_3_mon = 0
    contact_hour_6_rece_min_tot_3_mon = 0
    contact_hour_7_rece_min_tot_3_mon = 0
    contact_hour_8_rece_min_tot_3_mon = 0
    contact_hour_9_rece_min_tot_3_mon = 0
    contact_hour_10_rece_min_tot_3_mon = 0
    contact_hour_11_rece_min_tot_3_mon = 0
    contact_hour_12_rece_min_tot_3_mon = 0
    contact_hour_13_rece_min_tot_3_mon = 0
    contact_hour_14_rece_min_tot_3_mon = 0
    contact_hour_15_rece_min_tot_3_mon = 0
    contact_hour_16_rece_min_tot_3_mon = 0
    contact_hour_17_rece_min_tot_3_mon = 0
    contact_hour_18_rece_min_tot_3_mon = 0
    contact_hour_19_rece_min_tot_3_mon = 0
    contact_hour_20_rece_min_tot_3_mon = 0
    contact_hour_21_rece_min_tot_3_mon = 0
    contact_hour_22_rece_min_tot_3_mon = 0
    contact_hour_23_rece_min_tot_3_mon = 0

    contact_hour_0_cnt_2_mon = 0
    contact_hour_1_cnt_2_mon = 0
    contact_hour_2_cnt_2_mon = 0
    contact_hour_3_cnt_2_mon = 0
    contact_hour_4_cnt_2_mon = 0
    contact_hour_5_cnt_2_mon = 0
    contact_hour_6_cnt_2_mon = 0
    contact_hour_7_cnt_2_mon = 0
    contact_hour_8_cnt_2_mon = 0
    contact_hour_9_cnt_2_mon = 0
    contact_hour_10_cnt_2_mon = 0
    contact_hour_11_cnt_2_mon = 0
    contact_hour_12_cnt_2_mon = 0
    contact_hour_13_cnt_2_mon = 0
    contact_hour_14_cnt_2_mon = 0
    contact_hour_15_cnt_2_mon = 0
    contact_hour_16_cnt_2_mon = 0
    contact_hour_17_cnt_2_mon = 0
    contact_hour_18_cnt_2_mon = 0
    contact_hour_19_cnt_2_mon = 0
    contact_hour_20_cnt_2_mon = 0
    contact_hour_21_cnt_2_mon = 0
    contact_hour_22_cnt_2_mon = 0
    contact_hour_23_cnt_2_mon = 0

    contact_hour_0_min_tot_2_mon = 0
    contact_hour_1_min_tot_2_mon = 0
    contact_hour_2_min_tot_2_mon = 0
    contact_hour_3_min_tot_2_mon = 0
    contact_hour_4_min_tot_2_mon = 0
    contact_hour_5_min_tot_2_mon = 0
    contact_hour_6_min_tot_2_mon = 0
    contact_hour_7_min_tot_2_mon = 0
    contact_hour_8_min_tot_2_mon = 0
    contact_hour_9_min_tot_2_mon = 0
    contact_hour_10_min_tot_2_mon = 0
    contact_hour_11_min_tot_2_mon = 0
    contact_hour_12_min_tot_2_mon = 0
    contact_hour_13_min_tot_2_mon = 0
    contact_hour_14_min_tot_2_mon = 0
    contact_hour_15_min_tot_2_mon = 0
    contact_hour_16_min_tot_2_mon = 0
    contact_hour_17_min_tot_2_mon = 0
    contact_hour_18_min_tot_2_mon = 0
    contact_hour_19_min_tot_2_mon = 0
    contact_hour_20_min_tot_2_mon = 0
    contact_hour_21_min_tot_2_mon = 0
    contact_hour_22_min_tot_2_mon = 0
    contact_hour_23_min_tot_2_mon = 0

    contact_hour_0_call_cnt_2_mon = 0
    contact_hour_1_call_cnt_2_mon = 0
    contact_hour_2_call_cnt_2_mon = 0
    contact_hour_3_call_cnt_2_mon = 0
    contact_hour_4_call_cnt_2_mon = 0
    contact_hour_5_call_cnt_2_mon = 0
    contact_hour_6_call_cnt_2_mon = 0
    contact_hour_7_call_cnt_2_mon = 0
    contact_hour_8_call_cnt_2_mon = 0
    contact_hour_9_call_cnt_2_mon = 0
    contact_hour_10_call_cnt_2_mon = 0
    contact_hour_11_call_cnt_2_mon = 0
    contact_hour_12_call_cnt_2_mon = 0
    contact_hour_13_call_cnt_2_mon = 0
    contact_hour_14_call_cnt_2_mon = 0
    contact_hour_15_call_cnt_2_mon = 0
    contact_hour_16_call_cnt_2_mon = 0
    contact_hour_17_call_cnt_2_mon = 0
    contact_hour_18_call_cnt_2_mon = 0
    contact_hour_19_call_cnt_2_mon = 0
    contact_hour_20_call_cnt_2_mon = 0
    contact_hour_21_call_cnt_2_mon = 0
    contact_hour_22_call_cnt_2_mon = 0
    contact_hour_23_call_cnt_2_mon = 0

    contact_hour_0_call_min_tot_2_mon = 0
    contact_hour_1_call_min_tot_2_mon = 0
    contact_hour_2_call_min_tot_2_mon = 0
    contact_hour_3_call_min_tot_2_mon = 0
    contact_hour_4_call_min_tot_2_mon = 0
    contact_hour_5_call_min_tot_2_mon = 0
    contact_hour_6_call_min_tot_2_mon = 0
    contact_hour_7_call_min_tot_2_mon = 0
    contact_hour_8_call_min_tot_2_mon = 0
    contact_hour_9_call_min_tot_2_mon = 0
    contact_hour_10_call_min_tot_2_mon = 0
    contact_hour_11_call_min_tot_2_mon = 0
    contact_hour_12_call_min_tot_2_mon = 0
    contact_hour_13_call_min_tot_2_mon = 0
    contact_hour_14_call_min_tot_2_mon = 0
    contact_hour_15_call_min_tot_2_mon = 0
    contact_hour_16_call_min_tot_2_mon = 0
    contact_hour_17_call_min_tot_2_mon = 0
    contact_hour_18_call_min_tot_2_mon = 0
    contact_hour_19_call_min_tot_2_mon = 0
    contact_hour_20_call_min_tot_2_mon = 0
    contact_hour_21_call_min_tot_2_mon = 0
    contact_hour_22_call_min_tot_2_mon = 0
    contact_hour_23_call_min_tot_2_mon = 0

    contact_hour_0_rece_cnt_2_mon = 0
    contact_hour_1_rece_cnt_2_mon = 0
    contact_hour_2_rece_cnt_2_mon = 0
    contact_hour_3_rece_cnt_2_mon = 0
    contact_hour_4_rece_cnt_2_mon = 0
    contact_hour_5_rece_cnt_2_mon = 0
    contact_hour_6_rece_cnt_2_mon = 0
    contact_hour_7_rece_cnt_2_mon = 0
    contact_hour_8_rece_cnt_2_mon = 0
    contact_hour_9_rece_cnt_2_mon = 0
    contact_hour_10_rece_cnt_2_mon = 0
    contact_hour_11_rece_cnt_2_mon = 0
    contact_hour_12_rece_cnt_2_mon = 0
    contact_hour_13_rece_cnt_2_mon = 0
    contact_hour_14_rece_cnt_2_mon = 0
    contact_hour_15_rece_cnt_2_mon = 0
    contact_hour_16_rece_cnt_2_mon = 0
    contact_hour_17_rece_cnt_2_mon = 0
    contact_hour_18_rece_cnt_2_mon = 0
    contact_hour_19_rece_cnt_2_mon = 0
    contact_hour_20_rece_cnt_2_mon = 0
    contact_hour_21_rece_cnt_2_mon = 0
    contact_hour_22_rece_cnt_2_mon = 0
    contact_hour_23_rece_cnt_2_mon = 0

    contact_hour_0_rece_min_tot_2_mon = 0
    contact_hour_1_rece_min_tot_2_mon = 0
    contact_hour_2_rece_min_tot_2_mon = 0
    contact_hour_3_rece_min_tot_2_mon = 0
    contact_hour_4_rece_min_tot_2_mon = 0
    contact_hour_5_rece_min_tot_2_mon = 0
    contact_hour_6_rece_min_tot_2_mon = 0
    contact_hour_7_rece_min_tot_2_mon = 0
    contact_hour_8_rece_min_tot_2_mon = 0
    contact_hour_9_rece_min_tot_2_mon = 0
    contact_hour_10_rece_min_tot_2_mon = 0
    contact_hour_11_rece_min_tot_2_mon = 0
    contact_hour_12_rece_min_tot_2_mon = 0
    contact_hour_13_rece_min_tot_2_mon = 0
    contact_hour_14_rece_min_tot_2_mon = 0
    contact_hour_15_rece_min_tot_2_mon = 0
    contact_hour_16_rece_min_tot_2_mon = 0
    contact_hour_17_rece_min_tot_2_mon = 0
    contact_hour_18_rece_min_tot_2_mon = 0
    contact_hour_19_rece_min_tot_2_mon = 0
    contact_hour_20_rece_min_tot_2_mon = 0
    contact_hour_21_rece_min_tot_2_mon = 0
    contact_hour_22_rece_min_tot_2_mon = 0
    contact_hour_23_rece_min_tot_2_mon = 0

    contact_hour_0_cnt_1_mon = 0
    contact_hour_1_cnt_1_mon = 0
    contact_hour_2_cnt_1_mon = 0
    contact_hour_3_cnt_1_mon = 0
    contact_hour_4_cnt_1_mon = 0
    contact_hour_5_cnt_1_mon = 0
    contact_hour_6_cnt_1_mon = 0
    contact_hour_7_cnt_1_mon = 0
    contact_hour_8_cnt_1_mon = 0
    contact_hour_9_cnt_1_mon = 0
    contact_hour_10_cnt_1_mon = 0
    contact_hour_11_cnt_1_mon = 0
    contact_hour_12_cnt_1_mon = 0
    contact_hour_13_cnt_1_mon = 0
    contact_hour_14_cnt_1_mon = 0
    contact_hour_15_cnt_1_mon = 0
    contact_hour_16_cnt_1_mon = 0
    contact_hour_17_cnt_1_mon = 0
    contact_hour_18_cnt_1_mon = 0
    contact_hour_19_cnt_1_mon = 0
    contact_hour_20_cnt_1_mon = 0
    contact_hour_21_cnt_1_mon = 0
    contact_hour_22_cnt_1_mon = 0
    contact_hour_23_cnt_1_mon = 0

    contact_hour_0_min_tot_1_mon = 0
    contact_hour_1_min_tot_1_mon = 0
    contact_hour_2_min_tot_1_mon = 0
    contact_hour_3_min_tot_1_mon = 0
    contact_hour_4_min_tot_1_mon = 0
    contact_hour_5_min_tot_1_mon = 0
    contact_hour_6_min_tot_1_mon = 0
    contact_hour_7_min_tot_1_mon = 0
    contact_hour_8_min_tot_1_mon = 0
    contact_hour_9_min_tot_1_mon = 0
    contact_hour_10_min_tot_1_mon = 0
    contact_hour_11_min_tot_1_mon = 0
    contact_hour_12_min_tot_1_mon = 0
    contact_hour_13_min_tot_1_mon = 0
    contact_hour_14_min_tot_1_mon = 0
    contact_hour_15_min_tot_1_mon = 0
    contact_hour_16_min_tot_1_mon = 0
    contact_hour_17_min_tot_1_mon = 0
    contact_hour_18_min_tot_1_mon = 0
    contact_hour_19_min_tot_1_mon = 0
    contact_hour_20_min_tot_1_mon = 0
    contact_hour_21_min_tot_1_mon = 0
    contact_hour_22_min_tot_1_mon = 0
    contact_hour_23_min_tot_1_mon = 0

    contact_hour_0_call_cnt_1_mon = 0
    contact_hour_1_call_cnt_1_mon = 0
    contact_hour_2_call_cnt_1_mon = 0
    contact_hour_3_call_cnt_1_mon = 0
    contact_hour_4_call_cnt_1_mon = 0
    contact_hour_5_call_cnt_1_mon = 0
    contact_hour_6_call_cnt_1_mon = 0
    contact_hour_7_call_cnt_1_mon = 0
    contact_hour_8_call_cnt_1_mon = 0
    contact_hour_9_call_cnt_1_mon = 0
    contact_hour_10_call_cnt_1_mon = 0
    contact_hour_11_call_cnt_1_mon = 0
    contact_hour_12_call_cnt_1_mon = 0
    contact_hour_13_call_cnt_1_mon = 0
    contact_hour_14_call_cnt_1_mon = 0
    contact_hour_15_call_cnt_1_mon = 0
    contact_hour_16_call_cnt_1_mon = 0
    contact_hour_17_call_cnt_1_mon = 0
    contact_hour_18_call_cnt_1_mon = 0
    contact_hour_19_call_cnt_1_mon = 0
    contact_hour_20_call_cnt_1_mon = 0
    contact_hour_21_call_cnt_1_mon = 0
    contact_hour_22_call_cnt_1_mon = 0
    contact_hour_23_call_cnt_1_mon = 0

    contact_hour_0_call_min_tot_1_mon = 0
    contact_hour_1_call_min_tot_1_mon = 0
    contact_hour_2_call_min_tot_1_mon = 0
    contact_hour_3_call_min_tot_1_mon = 0
    contact_hour_4_call_min_tot_1_mon = 0
    contact_hour_5_call_min_tot_1_mon = 0
    contact_hour_6_call_min_tot_1_mon = 0
    contact_hour_7_call_min_tot_1_mon = 0
    contact_hour_8_call_min_tot_1_mon = 0
    contact_hour_9_call_min_tot_1_mon = 0
    contact_hour_10_call_min_tot_1_mon = 0
    contact_hour_11_call_min_tot_1_mon = 0
    contact_hour_12_call_min_tot_1_mon = 0
    contact_hour_13_call_min_tot_1_mon = 0
    contact_hour_14_call_min_tot_1_mon = 0
    contact_hour_15_call_min_tot_1_mon = 0
    contact_hour_16_call_min_tot_1_mon = 0
    contact_hour_17_call_min_tot_1_mon = 0
    contact_hour_18_call_min_tot_1_mon = 0
    contact_hour_19_call_min_tot_1_mon = 0
    contact_hour_20_call_min_tot_1_mon = 0
    contact_hour_21_call_min_tot_1_mon = 0
    contact_hour_22_call_min_tot_1_mon = 0
    contact_hour_23_call_min_tot_1_mon = 0

    contact_hour_0_rece_cnt_1_mon = 0
    contact_hour_1_rece_cnt_1_mon = 0
    contact_hour_2_rece_cnt_1_mon = 0
    contact_hour_3_rece_cnt_1_mon = 0
    contact_hour_4_rece_cnt_1_mon = 0
    contact_hour_5_rece_cnt_1_mon = 0
    contact_hour_6_rece_cnt_1_mon = 0
    contact_hour_7_rece_cnt_1_mon = 0
    contact_hour_8_rece_cnt_1_mon = 0
    contact_hour_9_rece_cnt_1_mon = 0
    contact_hour_10_rece_cnt_1_mon = 0
    contact_hour_11_rece_cnt_1_mon = 0
    contact_hour_12_rece_cnt_1_mon = 0
    contact_hour_13_rece_cnt_1_mon = 0
    contact_hour_14_rece_cnt_1_mon = 0
    contact_hour_15_rece_cnt_1_mon = 0
    contact_hour_16_rece_cnt_1_mon = 0
    contact_hour_17_rece_cnt_1_mon = 0
    contact_hour_18_rece_cnt_1_mon = 0
    contact_hour_19_rece_cnt_1_mon = 0
    contact_hour_20_rece_cnt_1_mon = 0
    contact_hour_21_rece_cnt_1_mon = 0
    contact_hour_22_rece_cnt_1_mon = 0
    contact_hour_23_rece_cnt_1_mon = 0

    contact_hour_0_rece_min_tot_1_mon = 0
    contact_hour_1_rece_min_tot_1_mon = 0
    contact_hour_2_rece_min_tot_1_mon = 0
    contact_hour_3_rece_min_tot_1_mon = 0
    contact_hour_4_rece_min_tot_1_mon = 0
    contact_hour_5_rece_min_tot_1_mon = 0
    contact_hour_6_rece_min_tot_1_mon = 0
    contact_hour_7_rece_min_tot_1_mon = 0
    contact_hour_8_rece_min_tot_1_mon = 0
    contact_hour_9_rece_min_tot_1_mon = 0
    contact_hour_10_rece_min_tot_1_mon = 0
    contact_hour_11_rece_min_tot_1_mon = 0
    contact_hour_12_rece_min_tot_1_mon = 0
    contact_hour_13_rece_min_tot_1_mon = 0
    contact_hour_14_rece_min_tot_1_mon = 0
    contact_hour_15_rece_min_tot_1_mon = 0
    contact_hour_16_rece_min_tot_1_mon = 0
    contact_hour_17_rece_min_tot_1_mon = 0
    contact_hour_18_rece_min_tot_1_mon = 0
    contact_hour_19_rece_min_tot_1_mon = 0
    contact_hour_20_rece_min_tot_1_mon = 0
    contact_hour_21_rece_min_tot_1_mon = 0
    contact_hour_22_rece_min_tot_1_mon = 0
    contact_hour_23_rece_min_tot_1_mon = 0

    contact_hour_0_cnt_2_wk = 0
    contact_hour_1_cnt_2_wk = 0
    contact_hour_2_cnt_2_wk = 0
    contact_hour_3_cnt_2_wk = 0
    contact_hour_4_cnt_2_wk = 0
    contact_hour_5_cnt_2_wk = 0
    contact_hour_6_cnt_2_wk = 0
    contact_hour_7_cnt_2_wk = 0
    contact_hour_8_cnt_2_wk = 0
    contact_hour_9_cnt_2_wk = 0
    contact_hour_10_cnt_2_wk = 0
    contact_hour_11_cnt_2_wk = 0
    contact_hour_12_cnt_2_wk = 0
    contact_hour_13_cnt_2_wk = 0
    contact_hour_14_cnt_2_wk = 0
    contact_hour_15_cnt_2_wk = 0
    contact_hour_16_cnt_2_wk = 0
    contact_hour_17_cnt_2_wk = 0
    contact_hour_18_cnt_2_wk = 0
    contact_hour_19_cnt_2_wk = 0
    contact_hour_20_cnt_2_wk = 0
    contact_hour_21_cnt_2_wk = 0
    contact_hour_22_cnt_2_wk = 0
    contact_hour_23_cnt_2_wk = 0

    contact_hour_0_min_tot_2_wk = 0
    contact_hour_1_min_tot_2_wk = 0
    contact_hour_2_min_tot_2_wk = 0
    contact_hour_3_min_tot_2_wk = 0
    contact_hour_4_min_tot_2_wk = 0
    contact_hour_5_min_tot_2_wk = 0
    contact_hour_6_min_tot_2_wk = 0
    contact_hour_7_min_tot_2_wk = 0
    contact_hour_8_min_tot_2_wk = 0
    contact_hour_9_min_tot_2_wk = 0
    contact_hour_10_min_tot_2_wk = 0
    contact_hour_11_min_tot_2_wk = 0
    contact_hour_12_min_tot_2_wk = 0
    contact_hour_13_min_tot_2_wk = 0
    contact_hour_14_min_tot_2_wk = 0
    contact_hour_15_min_tot_2_wk = 0
    contact_hour_16_min_tot_2_wk = 0
    contact_hour_17_min_tot_2_wk = 0
    contact_hour_18_min_tot_2_wk = 0
    contact_hour_19_min_tot_2_wk = 0
    contact_hour_20_min_tot_2_wk = 0
    contact_hour_21_min_tot_2_wk = 0
    contact_hour_22_min_tot_2_wk = 0
    contact_hour_23_min_tot_2_wk = 0

    contact_hour_0_call_cnt_2_wk = 0
    contact_hour_1_call_cnt_2_wk = 0
    contact_hour_2_call_cnt_2_wk = 0
    contact_hour_3_call_cnt_2_wk = 0
    contact_hour_4_call_cnt_2_wk = 0
    contact_hour_5_call_cnt_2_wk = 0
    contact_hour_6_call_cnt_2_wk = 0
    contact_hour_7_call_cnt_2_wk = 0
    contact_hour_8_call_cnt_2_wk = 0
    contact_hour_9_call_cnt_2_wk = 0
    contact_hour_10_call_cnt_2_wk = 0
    contact_hour_11_call_cnt_2_wk = 0
    contact_hour_12_call_cnt_2_wk = 0
    contact_hour_13_call_cnt_2_wk = 0
    contact_hour_14_call_cnt_2_wk = 0
    contact_hour_15_call_cnt_2_wk = 0
    contact_hour_16_call_cnt_2_wk = 0
    contact_hour_17_call_cnt_2_wk = 0
    contact_hour_18_call_cnt_2_wk = 0
    contact_hour_19_call_cnt_2_wk = 0
    contact_hour_20_call_cnt_2_wk = 0
    contact_hour_21_call_cnt_2_wk = 0
    contact_hour_22_call_cnt_2_wk = 0
    contact_hour_23_call_cnt_2_wk = 0

    contact_hour_0_call_min_tot_2_wk = 0
    contact_hour_1_call_min_tot_2_wk = 0
    contact_hour_2_call_min_tot_2_wk = 0
    contact_hour_3_call_min_tot_2_wk = 0
    contact_hour_4_call_min_tot_2_wk = 0
    contact_hour_5_call_min_tot_2_wk = 0
    contact_hour_6_call_min_tot_2_wk = 0
    contact_hour_7_call_min_tot_2_wk = 0
    contact_hour_8_call_min_tot_2_wk = 0
    contact_hour_9_call_min_tot_2_wk = 0
    contact_hour_10_call_min_tot_2_wk = 0
    contact_hour_11_call_min_tot_2_wk = 0
    contact_hour_12_call_min_tot_2_wk = 0
    contact_hour_13_call_min_tot_2_wk = 0
    contact_hour_14_call_min_tot_2_wk = 0
    contact_hour_15_call_min_tot_2_wk = 0
    contact_hour_16_call_min_tot_2_wk = 0
    contact_hour_17_call_min_tot_2_wk = 0
    contact_hour_18_call_min_tot_2_wk = 0
    contact_hour_19_call_min_tot_2_wk = 0
    contact_hour_20_call_min_tot_2_wk = 0
    contact_hour_21_call_min_tot_2_wk = 0
    contact_hour_22_call_min_tot_2_wk = 0
    contact_hour_23_call_min_tot_2_wk = 0

    contact_hour_0_rece_cnt_2_wk = 0
    contact_hour_1_rece_cnt_2_wk = 0
    contact_hour_2_rece_cnt_2_wk = 0
    contact_hour_3_rece_cnt_2_wk = 0
    contact_hour_4_rece_cnt_2_wk = 0
    contact_hour_5_rece_cnt_2_wk = 0
    contact_hour_6_rece_cnt_2_wk = 0
    contact_hour_7_rece_cnt_2_wk = 0
    contact_hour_8_rece_cnt_2_wk = 0
    contact_hour_9_rece_cnt_2_wk = 0
    contact_hour_10_rece_cnt_2_wk = 0
    contact_hour_11_rece_cnt_2_wk = 0
    contact_hour_12_rece_cnt_2_wk = 0
    contact_hour_13_rece_cnt_2_wk = 0
    contact_hour_14_rece_cnt_2_wk = 0
    contact_hour_15_rece_cnt_2_wk = 0
    contact_hour_16_rece_cnt_2_wk = 0
    contact_hour_17_rece_cnt_2_wk = 0
    contact_hour_18_rece_cnt_2_wk = 0
    contact_hour_19_rece_cnt_2_wk = 0
    contact_hour_20_rece_cnt_2_wk = 0
    contact_hour_21_rece_cnt_2_wk = 0
    contact_hour_22_rece_cnt_2_wk = 0
    contact_hour_23_rece_cnt_2_wk = 0

    contact_hour_0_rece_min_tot_2_wk = 0
    contact_hour_1_rece_min_tot_2_wk = 0
    contact_hour_2_rece_min_tot_2_wk = 0
    contact_hour_3_rece_min_tot_2_wk = 0
    contact_hour_4_rece_min_tot_2_wk = 0
    contact_hour_5_rece_min_tot_2_wk = 0
    contact_hour_6_rece_min_tot_2_wk = 0
    contact_hour_7_rece_min_tot_2_wk = 0
    contact_hour_8_rece_min_tot_2_wk = 0
    contact_hour_9_rece_min_tot_2_wk = 0
    contact_hour_10_rece_min_tot_2_wk = 0
    contact_hour_11_rece_min_tot_2_wk = 0
    contact_hour_12_rece_min_tot_2_wk = 0
    contact_hour_13_rece_min_tot_2_wk = 0
    contact_hour_14_rece_min_tot_2_wk = 0
    contact_hour_15_rece_min_tot_2_wk = 0
    contact_hour_16_rece_min_tot_2_wk = 0
    contact_hour_17_rece_min_tot_2_wk = 0
    contact_hour_18_rece_min_tot_2_wk = 0
    contact_hour_19_rece_min_tot_2_wk = 0
    contact_hour_20_rece_min_tot_2_wk = 0
    contact_hour_21_rece_min_tot_2_wk = 0
    contact_hour_22_rece_min_tot_2_wk = 0
    contact_hour_23_rece_min_tot_2_wk = 0

    contact_hour_0_cnt = 0
    contact_hour_1_cnt = 0
    contact_hour_2_cnt = 0
    contact_hour_3_cnt = 0
    contact_hour_4_cnt = 0
    contact_hour_5_cnt = 0
    contact_hour_6_cnt = 0
    contact_hour_7_cnt = 0
    contact_hour_8_cnt = 0
    contact_hour_9_cnt = 0
    contact_hour_10_cnt = 0
    contact_hour_11_cnt = 0
    contact_hour_12_cnt = 0
    contact_hour_13_cnt = 0
    contact_hour_14_cnt = 0
    contact_hour_15_cnt = 0
    contact_hour_16_cnt = 0
    contact_hour_17_cnt = 0
    contact_hour_18_cnt = 0
    contact_hour_19_cnt = 0
    contact_hour_20_cnt = 0
    contact_hour_21_cnt = 0
    contact_hour_22_cnt = 0
    contact_hour_23_cnt = 0

    contact_hour_0_min_tot = 0
    contact_hour_1_min_tot = 0
    contact_hour_2_min_tot = 0
    contact_hour_3_min_tot = 0
    contact_hour_4_min_tot = 0
    contact_hour_5_min_tot = 0
    contact_hour_6_min_tot = 0
    contact_hour_7_min_tot = 0
    contact_hour_8_min_tot = 0
    contact_hour_9_min_tot = 0
    contact_hour_10_min_tot = 0
    contact_hour_11_min_tot = 0
    contact_hour_12_min_tot = 0
    contact_hour_13_min_tot = 0
    contact_hour_14_min_tot = 0
    contact_hour_15_min_tot = 0
    contact_hour_16_min_tot = 0
    contact_hour_17_min_tot = 0
    contact_hour_18_min_tot = 0
    contact_hour_19_min_tot = 0
    contact_hour_20_min_tot = 0
    contact_hour_21_min_tot = 0
    contact_hour_22_min_tot = 0
    contact_hour_23_min_tot = 0

    contact_hour_0_call_cnt = 0
    contact_hour_1_call_cnt = 0
    contact_hour_2_call_cnt = 0
    contact_hour_3_call_cnt = 0
    contact_hour_4_call_cnt = 0
    contact_hour_5_call_cnt = 0
    contact_hour_6_call_cnt = 0
    contact_hour_7_call_cnt = 0
    contact_hour_8_call_cnt = 0
    contact_hour_9_call_cnt = 0
    contact_hour_10_call_cnt = 0
    contact_hour_11_call_cnt = 0
    contact_hour_12_call_cnt = 0
    contact_hour_13_call_cnt = 0
    contact_hour_14_call_cnt = 0
    contact_hour_15_call_cnt = 0
    contact_hour_16_call_cnt = 0
    contact_hour_17_call_cnt = 0
    contact_hour_18_call_cnt = 0
    contact_hour_19_call_cnt = 0
    contact_hour_20_call_cnt = 0
    contact_hour_21_call_cnt = 0
    contact_hour_22_call_cnt = 0
    contact_hour_23_call_cnt = 0

    contact_hour_0_call_min_tot = 0
    contact_hour_1_call_min_tot = 0
    contact_hour_2_call_min_tot = 0
    contact_hour_3_call_min_tot = 0
    contact_hour_4_call_min_tot = 0
    contact_hour_5_call_min_tot = 0
    contact_hour_6_call_min_tot = 0
    contact_hour_7_call_min_tot = 0
    contact_hour_8_call_min_tot = 0
    contact_hour_9_call_min_tot = 0
    contact_hour_10_call_min_tot = 0
    contact_hour_11_call_min_tot = 0
    contact_hour_12_call_min_tot = 0
    contact_hour_13_call_min_tot = 0
    contact_hour_14_call_min_tot = 0
    contact_hour_15_call_min_tot = 0
    contact_hour_16_call_min_tot = 0
    contact_hour_17_call_min_tot = 0
    contact_hour_18_call_min_tot = 0
    contact_hour_19_call_min_tot = 0
    contact_hour_20_call_min_tot = 0
    contact_hour_21_call_min_tot = 0
    contact_hour_22_call_min_tot = 0
    contact_hour_23_call_min_tot = 0

    contact_hour_0_rece_cnt = 0
    contact_hour_1_rece_cnt = 0
    contact_hour_2_rece_cnt = 0
    contact_hour_3_rece_cnt = 0
    contact_hour_4_rece_cnt = 0
    contact_hour_5_rece_cnt = 0
    contact_hour_6_rece_cnt = 0
    contact_hour_7_rece_cnt = 0
    contact_hour_8_rece_cnt = 0
    contact_hour_9_rece_cnt = 0
    contact_hour_10_rece_cnt = 0
    contact_hour_11_rece_cnt = 0
    contact_hour_12_rece_cnt = 0
    contact_hour_13_rece_cnt = 0
    contact_hour_14_rece_cnt = 0
    contact_hour_15_rece_cnt = 0
    contact_hour_16_rece_cnt = 0
    contact_hour_17_rece_cnt = 0
    contact_hour_18_rece_cnt = 0
    contact_hour_19_rece_cnt = 0
    contact_hour_20_rece_cnt = 0
    contact_hour_21_rece_cnt = 0
    contact_hour_22_rece_cnt = 0
    contact_hour_23_rece_cnt = 0

    contact_hour_0_rece_min_tot = 0
    contact_hour_1_rece_min_tot = 0
    contact_hour_2_rece_min_tot = 0
    contact_hour_3_rece_min_tot = 0
    contact_hour_4_rece_min_tot = 0
    contact_hour_5_rece_min_tot = 0
    contact_hour_6_rece_min_tot = 0
    contact_hour_7_rece_min_tot = 0
    contact_hour_8_rece_min_tot = 0
    contact_hour_9_rece_min_tot = 0
    contact_hour_10_rece_min_tot = 0
    contact_hour_11_rece_min_tot = 0
    contact_hour_12_rece_min_tot = 0
    contact_hour_13_rece_min_tot = 0
    contact_hour_14_rece_min_tot = 0
    contact_hour_15_rece_min_tot = 0
    contact_hour_16_rece_min_tot = 0
    contact_hour_17_rece_min_tot = 0
    contact_hour_18_rece_min_tot = 0
    contact_hour_19_rece_min_tot = 0
    contact_hour_20_rece_min_tot = 0
    contact_hour_21_rece_min_tot = 0
    contact_hour_22_rece_min_tot = 0
    contact_hour_23_rece_min_tot = 0

    # WEEKDAY AND WEEKENDS
    contact_weekday_cnt = 0
    contact_weekday_min_tot = 0
    contact_weekday_call_cnt = 0
    contact_weekday_call_min_tot = 0
    contact_weekday_rece_cnt = 0
    contact_weekday_rece_min_tot = 0

    contact_weekend_cnt = 0
    contact_weekend_min_tot = 0
    contact_weekend_call_cnt = 0
    contact_weekend_call_min_tot = 0
    contact_weekend_rece_cnt = 0
    contact_weekend_rece_min_tot = 0

    contact_weekday_cnt = 0
    contact_weekday_min_tot = 0
    contact_weekday_call_cnt = 0
    contact_weekday_call_min_tot = 0
    contact_weekday_rece_cnt = 0
    contact_weekday_rece_min_tot = 0
    contact_weekend_cnt = 0
    contact_weekend_min_tot = 0
    contact_weekend_call_cnt = 0
    contact_weekend_call_min_tot = 0
    contact_weekend_rece_cnt = 0
    contact_weekend_rece_min_tot = 0

    contact_weekday_cnt_6_mon = 0
    contact_weekday_min_tot_6_mon = 0
    contact_weekday_call_cnt_6_mon = 0
    contact_weekday_call_min_tot_6_mon = 0
    contact_weekday_rece_cnt_6_mon = 0
    contact_weekday_rece_min_tot_6_mon = 0
    contact_weekend_cnt_6_mon = 0
    contact_weekend_min_tot_6_mon = 0
    contact_weekend_call_cnt_6_mon = 0
    contact_weekend_call_min_tot_6_mon = 0
    contact_weekend_rece_cnt_6_mon = 0
    contact_weekend_rece_min_tot_6_mon = 0

    contact_weekday_cnt_3_mon = 0
    contact_weekday_min_tot_3_mon = 0
    contact_weekday_call_cnt_3_mon = 0
    contact_weekday_call_min_tot_3_mon = 0
    contact_weekday_rece_cnt_3_mon = 0
    contact_weekday_rece_min_tot_3_mon = 0
    contact_weekend_cnt_3_mon = 0
    contact_weekend_min_tot_3_mon = 0
    contact_weekend_call_cnt_3_mon = 0
    contact_weekend_call_min_tot_3_mon = 0
    contact_weekend_rece_cnt_3_mon = 0
    contact_weekend_rece_min_tot_3_mon = 0

    contact_weekday_cnt_2_mon = 0
    contact_weekday_min_tot_2_mon = 0
    contact_weekday_call_cnt_2_mon = 0
    contact_weekday_call_min_tot_2_mon = 0
    contact_weekday_rece_cnt_2_mon = 0
    contact_weekday_rece_min_tot_2_mon = 0
    contact_weekend_cnt_2_mon = 0
    contact_weekend_min_tot_2_mon = 0
    contact_weekend_call_cnt_2_mon = 0
    contact_weekend_call_min_tot_2_mon = 0
    contact_weekend_rece_cnt_2_mon = 0
    contact_weekend_rece_min_tot_2_mon = 0

    contact_weekday_cnt_1_mon = 0
    contact_weekday_min_tot_1_mon = 0
    contact_weekday_call_cnt_1_mon = 0
    contact_weekday_call_min_tot_1_mon = 0
    contact_weekday_rece_cnt_1_mon = 0
    contact_weekday_rece_min_tot_1_mon = 0
    contact_weekend_cnt_1_mon = 0
    contact_weekend_min_tot_1_mon = 0
    contact_weekend_call_cnt_1_mon = 0
    contact_weekend_call_min_tot_1_mon = 0
    contact_weekend_rece_cnt_1_mon = 0
    contact_weekend_rece_min_tot_1_mon = 0

    contact_weekday_cnt_2_wk = 0
    contact_weekday_min_tot_2_wk = 0
    contact_weekday_call_cnt_2_wk = 0
    contact_weekday_call_min_tot_2_wk = 0
    contact_weekday_rece_cnt_2_wk = 0
    contact_weekday_rece_min_tot_2_wk = 0
    contact_weekend_cnt_2_wk = 0
    contact_weekend_min_tot_2_wk = 0
    contact_weekend_call_cnt_2_wk = 0
    contact_weekend_call_min_tot_2_wk = 0
    contact_weekend_rece_cnt_2_wk = 0
    contact_weekend_rece_min_tot_2_wk = 0

    # contact duration over 15s, 30s, 60s
    contact_min_over_15s_cnt = 0
    contact_min_over_15s_min_tot = 0
    contact_min_over_15s_call_cnt = 0
    contact_min_over_15s_call_min_tot = 0
    contact_min_over_15s_rece_cnt = 0
    contact_min_over_15s_rece_min_tot = 0
    contact_min_over_30s_cnt = 0
    contact_min_over_30s_min_tot = 0
    contact_min_over_30s_call_cnt = 0
    contact_min_over_30s_call_min_tot = 0
    contact_min_over_30s_rece_cnt = 0
    contact_min_over_30s_rece_min_tot = 0
    contact_min_over_60s_cnt = 0
    contact_min_over_60s_min_tot = 0
    contact_min_over_60s_call_cnt = 0
    contact_min_over_60s_call_min_tot = 0
    contact_min_over_60s_rece_cnt = 0
    contact_min_over_60s_rece_min_tot = 0

    contact_min_over_15s_cnt_6_mon = 0
    contact_min_over_15s_min_tot_6_mon = 0
    contact_min_over_15s_call_cnt_6_mon = 0
    contact_min_over_15s_call_min_tot_6_mon = 0
    contact_min_over_15s_rece_cnt_6_mon = 0
    contact_min_over_15s_rece_min_tot_6_mon = 0
    contact_min_over_30s_cnt_6_mon = 0
    contact_min_over_30s_min_tot_6_mon = 0
    contact_min_over_30s_call_cnt_6_mon = 0
    contact_min_over_30s_call_min_tot_6_mon = 0
    contact_min_over_30s_rece_cnt_6_mon = 0
    contact_min_over_30s_rece_min_tot_6_mon = 0
    contact_min_over_60s_cnt_6_mon = 0
    contact_min_over_60s_min_tot_6_mon = 0
    contact_min_over_60s_call_cnt_6_mon = 0
    contact_min_over_60s_call_min_tot_6_mon = 0
    contact_min_over_60s_rece_cnt_6_mon = 0
    contact_min_over_60s_rece_min_tot_6_mon = 0

    contact_min_over_15s_cnt_3_mon = 0
    contact_min_over_15s_min_tot_3_mon = 0
    contact_min_over_15s_call_cnt_3_mon = 0
    contact_min_over_15s_call_min_tot_3_mon = 0
    contact_min_over_15s_rece_cnt_3_mon = 0
    contact_min_over_15s_rece_min_tot_3_mon = 0
    contact_min_over_30s_cnt_3_mon = 0
    contact_min_over_30s_min_tot_3_mon = 0
    contact_min_over_30s_call_cnt_3_mon = 0
    contact_min_over_30s_call_min_tot_3_mon = 0
    contact_min_over_30s_rece_cnt_3_mon = 0
    contact_min_over_30s_rece_min_tot_3_mon = 0
    contact_min_over_60s_cnt_3_mon = 0
    contact_min_over_60s_min_tot_3_mon = 0
    contact_min_over_60s_call_cnt_3_mon = 0
    contact_min_over_60s_call_min_tot_3_mon = 0
    contact_min_over_60s_rece_cnt_3_mon = 0
    contact_min_over_60s_rece_min_tot_3_mon = 0

    contact_min_over_15s_cnt_2_mon = 0
    contact_min_over_15s_min_tot_2_mon = 0
    contact_min_over_15s_call_cnt_2_mon = 0
    contact_min_over_15s_call_min_tot_2_mon = 0
    contact_min_over_15s_rece_cnt_2_mon = 0
    contact_min_over_15s_rece_min_tot_2_mon = 0
    contact_min_over_30s_cnt_2_mon = 0
    contact_min_over_30s_min_tot_2_mon = 0
    contact_min_over_30s_call_cnt_2_mon = 0
    contact_min_over_30s_call_min_tot_2_mon = 0
    contact_min_over_30s_rece_cnt_2_mon = 0
    contact_min_over_30s_rece_min_tot_2_mon = 0
    contact_min_over_60s_cnt_2_mon = 0
    contact_min_over_60s_min_tot_2_mon = 0
    contact_min_over_60s_call_cnt_2_mon = 0
    contact_min_over_60s_call_min_tot_2_mon = 0
    contact_min_over_60s_rece_cnt_2_mon = 0
    contact_min_over_60s_rece_min_tot_2_mon = 0

    contact_min_over_15s_cnt_1_mon = 0
    contact_min_over_15s_min_tot_1_mon = 0
    contact_min_over_15s_call_cnt_1_mon = 0
    contact_min_over_15s_call_min_tot_1_mon = 0
    contact_min_over_15s_rece_cnt_1_mon = 0
    contact_min_over_15s_rece_min_tot_1_mon = 0
    contact_min_over_30s_cnt_1_mon = 0
    contact_min_over_30s_min_tot_1_mon = 0
    contact_min_over_30s_call_cnt_1_mon = 0
    contact_min_over_30s_call_min_tot_1_mon = 0
    contact_min_over_30s_rece_cnt_1_mon = 0
    contact_min_over_30s_rece_min_tot_1_mon = 0
    contact_min_over_60s_cnt_1_mon = 0
    contact_min_over_60s_min_tot_1_mon = 0
    contact_min_over_60s_call_cnt_1_mon = 0
    contact_min_over_60s_call_min_tot_1_mon = 0
    contact_min_over_60s_rece_cnt_1_mon = 0
    contact_min_over_60s_rece_min_tot_1_mon = 0

    contact_min_over_15s_cnt_2_wk = 0
    contact_min_over_15s_min_tot_2_wk = 0
    contact_min_over_15s_call_cnt_2_wk = 0
    contact_min_over_15s_call_min_tot_2_wk = 0
    contact_min_over_15s_rece_cnt_2_wk = 0
    contact_min_over_15s_rece_min_tot_2_wk = 0
    contact_min_over_30s_cnt_2_wk = 0
    contact_min_over_30s_min_tot_2_wk = 0
    contact_min_over_30s_call_cnt_2_wk = 0
    contact_min_over_30s_call_min_tot_2_wk = 0
    contact_min_over_30s_rece_cnt_2_wk = 0
    contact_min_over_30s_rece_min_tot_2_wk = 0
    contact_min_over_60s_cnt_2_wk = 0
    contact_min_over_60s_min_tot_2_wk = 0
    contact_min_over_60s_call_cnt_2_wk = 0
    contact_min_over_60s_call_min_tot_2_wk = 0
    contact_min_over_60s_rece_cnt_2_wk = 0
    contact_min_over_60s_rece_min_tot_2_wk = 0

    # contact hour combine
    contact_hour_0to1_cnt = 0
    contact_hour_2to3_cnt = 0
    contact_hour_4to5_cnt = 0
    contact_hour_6to7_cnt = 0
    contact_hour_8to9_cnt = 0
    contact_hour_10to11_cnt = 0
    contact_hour_12to13_cnt = 0
    contact_hour_14to15_cnt = 0
    contact_hour_16to17_cnt = 0
    contact_hour_18to19_cnt = 0
    contact_hour_20to21_cnt = 0
    contact_hour_22to23_cnt = 0

    contact_hour_0to1_min_tot = 0
    contact_hour_2to3_min_tot = 0
    contact_hour_4to5_min_tot = 0
    contact_hour_6to7_min_tot = 0
    contact_hour_8to9_min_tot = 0
    contact_hour_10to11_min_tot = 0
    contact_hour_12to13_min_tot = 0
    contact_hour_14to15_min_tot = 0
    contact_hour_16to17_min_tot = 0
    contact_hour_18to19_min_tot = 0
    contact_hour_20to21_min_tot = 0
    contact_hour_22to23_min_tot = 0

    contact_hour_0to1_cnt = 0
    contact_hour_2to3_cnt = 0
    contact_hour_4to5_cnt = 0
    contact_hour_6to7_cnt = 0
    contact_hour_8to9_cnt = 0
    contact_hour_10to11_cnt = 0
    contact_hour_12to13_cnt = 0
    contact_hour_14to15_cnt = 0
    contact_hour_16to17_cnt = 0
    contact_hour_18to19_cnt = 0
    contact_hour_20to21_cnt = 0
    contact_hour_22to23_cnt = 0

    contact_hour_0to1_min_tot = 0
    contact_hour_2to3_min_tot = 0
    contact_hour_4to5_min_tot = 0
    contact_hour_6to7_min_tot = 0
    contact_hour_8to9_min_tot = 0
    contact_hour_10to11_min_tot = 0
    contact_hour_12to13_min_tot = 0
    contact_hour_14to15_min_tot = 0
    contact_hour_16to17_min_tot = 0
    contact_hour_18to19_min_tot = 0
    contact_hour_20to21_min_tot = 0
    contact_hour_22to23_min_tot = 0

    contact_hour_0to1_cnt_6_mon = 0
    contact_hour_2to3_cnt_6_mon = 0
    contact_hour_4to5_cnt_6_mon = 0
    contact_hour_6to7_cnt_6_mon = 0
    contact_hour_8to9_cnt_6_mon = 0
    contact_hour_10to11_cnt_6_mon = 0
    contact_hour_12to13_cnt_6_mon = 0
    contact_hour_14to15_cnt_6_mon = 0
    contact_hour_16to17_cnt_6_mon = 0
    contact_hour_18to19_cnt_6_mon = 0
    contact_hour_20to21_cnt_6_mon = 0
    contact_hour_22to23_cnt_6_mon = 0

    contact_hour_0to1_min_tot_6_mon = 0
    contact_hour_2to3_min_tot_6_mon = 0
    contact_hour_4to5_min_tot_6_mon = 0
    contact_hour_6to7_min_tot_6_mon = 0
    contact_hour_8to9_min_tot_6_mon = 0
    contact_hour_10to11_min_tot_6_mon = 0
    contact_hour_12to13_min_tot_6_mon = 0
    contact_hour_14to15_min_tot_6_mon = 0
    contact_hour_16to17_min_tot_6_mon = 0
    contact_hour_18to19_min_tot_6_mon = 0
    contact_hour_20to21_min_tot_6_mon = 0
    contact_hour_22to23_min_tot_6_mon = 0

    contact_hour_0to1_cnt_3_mon = 0
    contact_hour_2to3_cnt_3_mon = 0
    contact_hour_4to5_cnt_3_mon = 0
    contact_hour_6to7_cnt_3_mon = 0
    contact_hour_8to9_cnt_3_mon = 0
    contact_hour_10to11_cnt_3_mon = 0
    contact_hour_12to13_cnt_3_mon = 0
    contact_hour_14to15_cnt_3_mon = 0
    contact_hour_16to17_cnt_3_mon = 0
    contact_hour_18to19_cnt_3_mon = 0
    contact_hour_20to21_cnt_3_mon = 0
    contact_hour_22to23_cnt_3_mon = 0

    contact_hour_0to1_min_tot_3_mon = 0
    contact_hour_2to3_min_tot_3_mon = 0
    contact_hour_4to5_min_tot_3_mon = 0
    contact_hour_6to7_min_tot_3_mon = 0
    contact_hour_8to9_min_tot_3_mon = 0
    contact_hour_10to11_min_tot_3_mon = 0
    contact_hour_12to13_min_tot_3_mon = 0
    contact_hour_14to15_min_tot_3_mon = 0
    contact_hour_16to17_min_tot_3_mon = 0
    contact_hour_18to19_min_tot_3_mon = 0
    contact_hour_20to21_min_tot_3_mon = 0
    contact_hour_22to23_min_tot_3_mon = 0

    contact_hour_0to1_cnt_2_mon = 0
    contact_hour_2to3_cnt_2_mon = 0
    contact_hour_4to5_cnt_2_mon = 0
    contact_hour_6to7_cnt_2_mon = 0
    contact_hour_8to9_cnt_2_mon = 0
    contact_hour_10to11_cnt_2_mon = 0
    contact_hour_12to13_cnt_2_mon = 0
    contact_hour_14to15_cnt_2_mon = 0
    contact_hour_16to17_cnt_2_mon = 0
    contact_hour_18to19_cnt_2_mon = 0
    contact_hour_20to21_cnt_2_mon = 0
    contact_hour_22to23_cnt_2_mon = 0

    contact_hour_0to1_min_tot_2_mon = 0
    contact_hour_2to3_min_tot_2_mon = 0
    contact_hour_4to5_min_tot_2_mon = 0
    contact_hour_6to7_min_tot_2_mon = 0
    contact_hour_8to9_min_tot_2_mon = 0
    contact_hour_10to11_min_tot_2_mon = 0
    contact_hour_12to13_min_tot_2_mon = 0
    contact_hour_14to15_min_tot_2_mon = 0
    contact_hour_16to17_min_tot_2_mon = 0
    contact_hour_18to19_min_tot_2_mon = 0
    contact_hour_20to21_min_tot_2_mon = 0
    contact_hour_22to23_min_tot_2_mon = 0

    contact_hour_0to1_cnt_1_mon = 0
    contact_hour_2to3_cnt_1_mon = 0
    contact_hour_4to5_cnt_1_mon = 0
    contact_hour_6to7_cnt_1_mon = 0
    contact_hour_8to9_cnt_1_mon = 0
    contact_hour_10to11_cnt_1_mon = 0
    contact_hour_12to13_cnt_1_mon = 0
    contact_hour_14to15_cnt_1_mon = 0
    contact_hour_16to17_cnt_1_mon = 0
    contact_hour_18to19_cnt_1_mon = 0
    contact_hour_20to21_cnt_1_mon = 0
    contact_hour_22to23_cnt_1_mon = 0

    contact_hour_0to1_min_tot_1_mon = 0
    contact_hour_2to3_min_tot_1_mon = 0
    contact_hour_4to5_min_tot_1_mon = 0
    contact_hour_6to7_min_tot_1_mon = 0
    contact_hour_8to9_min_tot_1_mon = 0
    contact_hour_10to11_min_tot_1_mon = 0
    contact_hour_12to13_min_tot_1_mon = 0
    contact_hour_14to15_min_tot_1_mon = 0
    contact_hour_16to17_min_tot_1_mon = 0
    contact_hour_18to19_min_tot_1_mon = 0
    contact_hour_20to21_min_tot_1_mon = 0
    contact_hour_22to23_min_tot_1_mon = 0

    contact_hour_0to1_cnt_2_wk = 0
    contact_hour_2to3_cnt_2_wk = 0
    contact_hour_4to5_cnt_2_wk = 0
    contact_hour_6to7_cnt_2_wk = 0
    contact_hour_8to9_cnt_2_wk = 0
    contact_hour_10to11_cnt_2_wk = 0
    contact_hour_12to13_cnt_2_wk = 0
    contact_hour_14to15_cnt_2_wk = 0
    contact_hour_16to17_cnt_2_wk = 0
    contact_hour_18to19_cnt_2_wk = 0
    contact_hour_20to21_cnt_2_wk = 0
    contact_hour_22to23_cnt_2_wk = 0

    contact_hour_0to1_min_tot_2_wk = 0
    contact_hour_2to3_min_tot_2_wk = 0
    contact_hour_4to5_min_tot_2_wk = 0
    contact_hour_6to7_min_tot_2_wk = 0
    contact_hour_8to9_min_tot_2_wk = 0
    contact_hour_10to11_min_tot_2_wk = 0
    contact_hour_12to13_min_tot_2_wk = 0
    contact_hour_14to15_min_tot_2_wk = 0
    contact_hour_16to17_min_tot_2_wk = 0
    contact_hour_18to19_min_tot_2_wk = 0
    contact_hour_20to21_min_tot_2_wk = 0
    contact_hour_22to23_min_tot_2_wk = 0

    contact_hour_1to6_cnt = 0
    contact_hour_7to12_cnt = 0
    contact_hour_13to18_cnt = 0
    contact_hour_19to0_cnt = 0

    contact_hour_1to6_min_tot = 0
    contact_hour_7to12_min_tot = 0
    contact_hour_13to18_min_tot = 0
    contact_hour_19to0_min_tot = 0

    contact_hour_1to6_cnt_6_mon = 0
    contact_hour_7to12_cnt_6_mon = 0
    contact_hour_13to18_cnt_6_mon = 0
    contact_hour_19to0_cnt_6_mon = 0

    contact_hour_1to6_min_tot_6_mon = 0
    contact_hour_7to12_min_tot_6_mon = 0
    contact_hour_13to18_min_tot_6_mon = 0
    contact_hour_19to0_min_tot_6_mon = 0

    contact_hour_1to6_cnt_3_mon = 0
    contact_hour_7to12_cnt_3_mon = 0
    contact_hour_13to18_cnt_3_mon = 0
    contact_hour_19to0_cnt_3_mon = 0

    contact_hour_1to6_min_tot_3_mon = 0
    contact_hour_7to12_min_tot_3_mon = 0
    contact_hour_13to18_min_tot_3_mon = 0
    contact_hour_19to0_min_tot_3_mon = 0

    contact_hour_1to6_cnt_2_mon = 0
    contact_hour_7to12_cnt_2_mon = 0
    contact_hour_13to18_cnt_2_mon = 0
    contact_hour_19to0_cnt_2_mon = 0

    contact_hour_1to6_min_tot_2_mon = 0
    contact_hour_7to12_min_tot_2_mon = 0
    contact_hour_13to18_min_tot_2_mon = 0
    contact_hour_19to0_min_tot_2_mon = 0

    contact_hour_1to6_cnt_1_mon = 0
    contact_hour_7to12_cnt_1_mon = 0
    contact_hour_13to18_cnt_1_mon = 0
    contact_hour_19to0_cnt_1_mon = 0

    contact_hour_1to6_min_tot_1_mon = 0
    contact_hour_7to12_min_tot_1_mon = 0
    contact_hour_13to18_min_tot_1_mon = 0
    contact_hour_19to0_min_tot_1_mon = 0

    contact_hour_1to6_cnt_2_wk = 0
    contact_hour_7to12_cnt_2_wk = 0
    contact_hour_13to18_cnt_2_wk = 0
    contact_hour_19to0_cnt_2_wk = 0

    contact_hour_1to6_min_tot_2_wk = 0
    contact_hour_7to12_min_tot_2_wk = 0
    contact_hour_13to18_min_tot_2_wk = 0
    contact_hour_19to0_min_tot_2_wk = 0

    contact_hour_1to8_cnt = 0
    contact_hour_9to16_cnt = 0
    contact_hour_17to0_cnt = 0

    contact_hour_1to8_min_tot = 0
    contact_hour_9to16_min_tot = 0
    contact_hour_17to0_min_tot = 0

    contact_hour_1to8_cnt_6_mon = 0
    contact_hour_9to16_cnt_6_mon = 0
    contact_hour_17to0_cnt_6_mon = 0

    contact_hour_1to8_min_tot_6_mon = 0
    contact_hour_9to16_min_tot_6_mon = 0
    contact_hour_17to0_min_tot_6_mon = 0

    contact_hour_1to8_cnt_3_mon = 0
    contact_hour_9to16_cnt_3_mon = 0
    contact_hour_17to0_cnt_3_mon = 0

    contact_hour_1to8_min_tot_3_mon = 0
    contact_hour_9to16_min_tot_3_mon = 0
    contact_hour_17to0_min_tot_3_mon = 0

    contact_hour_1to8_cnt_2_mon = 0
    contact_hour_9to16_cnt_2_mon = 0
    contact_hour_17to0_cnt_2_mon = 0

    contact_hour_1to8_min_tot_2_mon = 0
    contact_hour_9to16_min_tot_2_mon = 0
    contact_hour_17to0_min_tot_2_mon = 0

    contact_hour_1to8_cnt_1_mon = 0
    contact_hour_9to16_cnt_1_mon = 0
    contact_hour_17to0_cnt_1_mon = 0

    contact_hour_1to8_min_tot_1_mon = 0
    contact_hour_9to16_min_tot_1_mon = 0
    contact_hour_17to0_min_tot_1_mon = 0

    contact_hour_1to8_cnt_2_wk = 0
    contact_hour_9to16_cnt_2_wk = 0
    contact_hour_17to0_cnt_2_wk = 0

    contact_hour_1to8_min_tot_2_wk = 0
    contact_hour_9to16_min_tot_2_wk = 0
    contact_hour_17to0_min_tot_2_wk = 0

    contact_hour_9to20_cnt = 0
    contact_hour_21to8_cnt = 0

    contact_hour_9to20_min_tot = 0
    contact_hour_21to8_min_tot = 0

    contact_hour_9to20_cnt_6_mon = 0
    contact_hour_21to8_cnt_6_mon = 0

    contact_hour_9to20_min_tot_6_mon = 0
    contact_hour_21to8_min_tot_6_mon = 0

    contact_hour_9to20_cnt_3_mon = 0
    contact_hour_21to8_cnt_3_mon = 0

    contact_hour_9to20_min_tot_3_mon = 0
    contact_hour_21to8_min_tot_3_mon = 0

    contact_hour_9to20_cnt_2_mon = 0
    contact_hour_21to8_cnt_2_mon = 0

    contact_hour_9to20_min_tot_2_mon = 0
    contact_hour_21to8_min_tot_2_mon = 0

    contact_hour_9to20_cnt_1_mon = 0
    contact_hour_21to8_cnt_1_mon = 0

    contact_hour_9to20_min_tot_1_mon = 0
    contact_hour_21to8_min_tot_1_mon = 0

    contact_hour_9to20_cnt_2_wk = 0
    contact_hour_21to8_cnt_2_wk = 0

    contact_hour_9to20_min_tot_2_wk = 0
    contact_hour_21to8_min_tot_2_wk = 0

    contact_hour_0to1_call_cnt = 0
    contact_hour_2to3_call_cnt = 0
    contact_hour_4to5_call_cnt = 0
    contact_hour_6to7_call_cnt = 0
    contact_hour_8to9_call_cnt = 0
    contact_hour_10to11_call_cnt = 0
    contact_hour_12to13_call_cnt = 0
    contact_hour_14to15_call_cnt = 0
    contact_hour_16to17_call_cnt = 0
    contact_hour_18to19_call_cnt = 0
    contact_hour_20to21_call_cnt = 0
    contact_hour_22to23_call_cnt = 0

    contact_hour_0to1_call_min_tot = 0
    contact_hour_2to3_call_min_tot = 0
    contact_hour_4to5_call_min_tot = 0
    contact_hour_6to7_call_min_tot = 0
    contact_hour_8to9_call_min_tot = 0
    contact_hour_10to11_call_min_tot = 0
    contact_hour_12to13_call_min_tot = 0
    contact_hour_14to15_call_min_tot = 0
    contact_hour_16to17_call_min_tot = 0
    contact_hour_18to19_call_min_tot = 0
    contact_hour_20to21_call_min_tot = 0
    contact_hour_22to23_call_min_tot = 0

    contact_hour_0to1_call_cnt_6_mon = 0
    contact_hour_2to3_call_cnt_6_mon = 0
    contact_hour_4to5_call_cnt_6_mon = 0
    contact_hour_6to7_call_cnt_6_mon = 0
    contact_hour_8to9_call_cnt_6_mon = 0
    contact_hour_10to11_call_cnt_6_mon = 0
    contact_hour_12to13_call_cnt_6_mon = 0
    contact_hour_14to15_call_cnt_6_mon = 0
    contact_hour_16to17_call_cnt_6_mon = 0
    contact_hour_18to19_call_cnt_6_mon = 0
    contact_hour_20to21_call_cnt_6_mon = 0
    contact_hour_22to23_call_cnt_6_mon = 0

    contact_hour_0to1_call_min_tot_6_mon = 0
    contact_hour_2to3_call_min_tot_6_mon = 0
    contact_hour_4to5_call_min_tot_6_mon = 0
    contact_hour_6to7_call_min_tot_6_mon = 0
    contact_hour_8to9_call_min_tot_6_mon = 0
    contact_hour_10to11_call_min_tot_6_mon = 0
    contact_hour_12to13_call_min_tot_6_mon = 0
    contact_hour_14to15_call_min_tot_6_mon = 0
    contact_hour_16to17_call_min_tot_6_mon = 0
    contact_hour_18to19_call_min_tot_6_mon = 0
    contact_hour_20to21_call_min_tot_6_mon = 0
    contact_hour_22to23_call_min_tot_6_mon = 0

    contact_hour_0to1_call_cnt_3_mon = 0
    contact_hour_2to3_call_cnt_3_mon = 0
    contact_hour_4to5_call_cnt_3_mon = 0
    contact_hour_6to7_call_cnt_3_mon = 0
    contact_hour_8to9_call_cnt_3_mon = 0
    contact_hour_10to11_call_cnt_3_mon = 0
    contact_hour_12to13_call_cnt_3_mon = 0
    contact_hour_14to15_call_cnt_3_mon = 0
    contact_hour_16to17_call_cnt_3_mon = 0
    contact_hour_18to19_call_cnt_3_mon = 0
    contact_hour_20to21_call_cnt_3_mon = 0
    contact_hour_22to23_call_cnt_3_mon = 0

    contact_hour_0to1_call_min_tot_3_mon = 0
    contact_hour_2to3_call_min_tot_3_mon = 0
    contact_hour_4to5_call_min_tot_3_mon = 0
    contact_hour_6to7_call_min_tot_3_mon = 0
    contact_hour_8to9_call_min_tot_3_mon = 0
    contact_hour_10to11_call_min_tot_3_mon = 0
    contact_hour_12to13_call_min_tot_3_mon = 0
    contact_hour_14to15_call_min_tot_3_mon = 0
    contact_hour_16to17_call_min_tot_3_mon = 0
    contact_hour_18to19_call_min_tot_3_mon = 0
    contact_hour_20to21_call_min_tot_3_mon = 0
    contact_hour_22to23_call_min_tot_3_mon = 0

    contact_hour_0to1_call_cnt_2_mon = 0
    contact_hour_2to3_call_cnt_2_mon = 0
    contact_hour_4to5_call_cnt_2_mon = 0
    contact_hour_6to7_call_cnt_2_mon = 0
    contact_hour_8to9_call_cnt_2_mon = 0
    contact_hour_10to11_call_cnt_2_mon = 0
    contact_hour_12to13_call_cnt_2_mon = 0
    contact_hour_14to15_call_cnt_2_mon = 0
    contact_hour_16to17_call_cnt_2_mon = 0
    contact_hour_18to19_call_cnt_2_mon = 0
    contact_hour_20to21_call_cnt_2_mon = 0
    contact_hour_22to23_call_cnt_2_mon = 0

    contact_hour_0to1_call_min_tot_2_mon = 0
    contact_hour_2to3_call_min_tot_2_mon = 0
    contact_hour_4to5_call_min_tot_2_mon = 0
    contact_hour_6to7_call_min_tot_2_mon = 0
    contact_hour_8to9_call_min_tot_2_mon = 0
    contact_hour_10to11_call_min_tot_2_mon = 0
    contact_hour_12to13_call_min_tot_2_mon = 0
    contact_hour_14to15_call_min_tot_2_mon = 0
    contact_hour_16to17_call_min_tot_2_mon = 0
    contact_hour_18to19_call_min_tot_2_mon = 0
    contact_hour_20to21_call_min_tot_2_mon = 0
    contact_hour_22to23_call_min_tot_2_mon = 0

    contact_hour_0to1_call_cnt_1_mon = 0
    contact_hour_2to3_call_cnt_1_mon = 0
    contact_hour_4to5_call_cnt_1_mon = 0
    contact_hour_6to7_call_cnt_1_mon = 0
    contact_hour_8to9_call_cnt_1_mon = 0
    contact_hour_10to11_call_cnt_1_mon = 0
    contact_hour_12to13_call_cnt_1_mon = 0
    contact_hour_14to15_call_cnt_1_mon = 0
    contact_hour_16to17_call_cnt_1_mon = 0
    contact_hour_18to19_call_cnt_1_mon = 0
    contact_hour_20to21_call_cnt_1_mon = 0
    contact_hour_22to23_call_cnt_1_mon = 0

    contact_hour_0to1_call_min_tot_1_mon = 0
    contact_hour_2to3_call_min_tot_1_mon = 0
    contact_hour_4to5_call_min_tot_1_mon = 0
    contact_hour_6to7_call_min_tot_1_mon = 0
    contact_hour_8to9_call_min_tot_1_mon = 0
    contact_hour_10to11_call_min_tot_1_mon = 0
    contact_hour_12to13_call_min_tot_1_mon = 0
    contact_hour_14to15_call_min_tot_1_mon = 0
    contact_hour_16to17_call_min_tot_1_mon = 0
    contact_hour_18to19_call_min_tot_1_mon = 0
    contact_hour_20to21_call_min_tot_1_mon = 0
    contact_hour_22to23_call_min_tot_1_mon = 0

    contact_hour_0to1_call_cnt_2_wk = 0
    contact_hour_2to3_call_cnt_2_wk = 0
    contact_hour_4to5_call_cnt_2_wk = 0
    contact_hour_6to7_call_cnt_2_wk = 0
    contact_hour_8to9_call_cnt_2_wk = 0
    contact_hour_10to11_call_cnt_2_wk = 0
    contact_hour_12to13_call_cnt_2_wk = 0
    contact_hour_14to15_call_cnt_2_wk = 0
    contact_hour_16to17_call_cnt_2_wk = 0
    contact_hour_18to19_call_cnt_2_wk = 0
    contact_hour_20to21_call_cnt_2_wk = 0
    contact_hour_22to23_call_cnt_2_wk = 0

    contact_hour_0to1_call_min_tot_2_wk = 0
    contact_hour_2to3_call_min_tot_2_wk = 0
    contact_hour_4to5_call_min_tot_2_wk = 0
    contact_hour_6to7_call_min_tot_2_wk = 0
    contact_hour_8to9_call_min_tot_2_wk = 0
    contact_hour_10to11_call_min_tot_2_wk = 0
    contact_hour_12to13_call_min_tot_2_wk = 0
    contact_hour_14to15_call_min_tot_2_wk = 0
    contact_hour_16to17_call_min_tot_2_wk = 0
    contact_hour_18to19_call_min_tot_2_wk = 0
    contact_hour_20to21_call_min_tot_2_wk = 0
    contact_hour_22to23_call_min_tot_2_wk = 0

    contact_hour_1to6_call_cnt = 0
    contact_hour_7to12_call_cnt = 0
    contact_hour_13to18_call_cnt = 0
    contact_hour_19to0_call_cnt = 0

    contact_hour_1to6_call_min_tot = 0
    contact_hour_7to12_call_min_tot = 0
    contact_hour_13to18_call_min_tot = 0
    contact_hour_19to0_call_min_tot = 0

    contact_hour_1to6_call_cnt_6_mon = 0
    contact_hour_7to12_call_cnt_6_mon = 0
    contact_hour_13to18_call_cnt_6_mon = 0
    contact_hour_19to0_call_cnt_6_mon = 0

    contact_hour_1to6_call_min_tot_6_mon = 0
    contact_hour_7to12_call_min_tot_6_mon = 0
    contact_hour_13to18_call_min_tot_6_mon = 0
    contact_hour_19to0_call_min_tot_6_mon = 0

    contact_hour_1to6_call_cnt_3_mon = 0
    contact_hour_7to12_call_cnt_3_mon = 0
    contact_hour_13to18_call_cnt_3_mon = 0
    contact_hour_19to0_call_cnt_3_mon = 0

    contact_hour_1to6_call_min_tot_3_mon = 0
    contact_hour_7to12_call_min_tot_3_mon = 0
    contact_hour_13to18_call_min_tot_3_mon = 0
    contact_hour_19to0_call_min_tot_3_mon = 0

    contact_hour_1to6_call_cnt_2_mon = 0
    contact_hour_7to12_call_cnt_2_mon = 0
    contact_hour_13to18_call_cnt_2_mon = 0
    contact_hour_19to0_call_cnt_2_mon = 0

    contact_hour_1to6_call_min_tot_2_mon = 0
    contact_hour_7to12_call_min_tot_2_mon = 0
    contact_hour_13to18_call_min_tot_2_mon = 0
    contact_hour_19to0_call_min_tot_2_mon = 0

    contact_hour_1to6_call_cnt_1_mon = 0
    contact_hour_7to12_call_cnt_1_mon = 0
    contact_hour_13to18_call_cnt_1_mon = 0
    contact_hour_19to0_call_cnt_1_mon = 0

    contact_hour_1to6_call_min_tot_1_mon = 0
    contact_hour_7to12_call_min_tot_1_mon = 0
    contact_hour_13to18_call_min_tot_1_mon = 0
    contact_hour_19to0_call_min_tot_1_mon = 0

    contact_hour_1to6_call_cnt_2_wk = 0
    contact_hour_7to12_call_cnt_2_wk = 0
    contact_hour_13to18_call_cnt_2_wk = 0
    contact_hour_19to0_call_cnt_2_wk = 0

    contact_hour_1to6_call_min_tot_2_wk = 0
    contact_hour_7to12_call_min_tot_2_wk = 0
    contact_hour_13to18_call_min_tot_2_wk = 0
    contact_hour_19to0_call_min_tot_2_wk = 0

    contact_hour_1to8_call_cnt = 0
    contact_hour_9to16_call_cnt = 0
    contact_hour_17to0_call_cnt = 0

    contact_hour_1to8_call_min_tot = 0
    contact_hour_9to16_call_min_tot = 0
    contact_hour_17to0_call_min_tot = 0

    contact_hour_1to8_call_cnt_6_mon = 0
    contact_hour_9to16_call_cnt_6_mon = 0
    contact_hour_17to0_call_cnt_6_mon = 0

    contact_hour_1to8_call_min_tot_6_mon = 0
    contact_hour_9to16_call_min_tot_6_mon = 0
    contact_hour_17to0_call_min_tot_6_mon = 0

    contact_hour_1to8_call_cnt_3_mon = 0
    contact_hour_9to16_call_cnt_3_mon = 0
    contact_hour_17to0_call_cnt_3_mon = 0

    contact_hour_1to8_call_min_tot_3_mon = 0
    contact_hour_9to16_call_min_tot_3_mon = 0
    contact_hour_17to0_call_min_tot_3_mon = 0

    contact_hour_1to8_call_cnt_2_mon = 0
    contact_hour_9to16_call_cnt_2_mon = 0
    contact_hour_17to0_call_cnt_2_mon = 0

    contact_hour_1to8_call_min_tot_2_mon = 0
    contact_hour_9to16_call_min_tot_2_mon = 0
    contact_hour_17to0_call_min_tot_2_mon = 0

    contact_hour_1to8_call_cnt_1_mon = 0
    contact_hour_9to16_call_cnt_1_mon = 0
    contact_hour_17to0_call_cnt_1_mon = 0

    contact_hour_1to8_call_min_tot_1_mon = 0
    contact_hour_9to16_call_min_tot_1_mon = 0
    contact_hour_17to0_call_min_tot_1_mon = 0

    contact_hour_1to8_call_cnt_2_wk = 0
    contact_hour_9to16_call_cnt_2_wk = 0
    contact_hour_17to0_call_cnt_2_wk = 0

    contact_hour_1to8_call_min_tot_2_wk = 0
    contact_hour_9to16_call_min_tot_2_wk = 0
    contact_hour_17to0_call_min_tot_2_wk = 0

    contact_hour_9to20_call_cnt = 0
    contact_hour_21to8_call_cnt = 0

    contact_hour_9to20_call_min_tot = 0
    contact_hour_21to8_call_min_tot = 0

    contact_hour_9to20_call_cnt_6_mon = 0
    contact_hour_21to8_call_cnt_6_mon = 0

    contact_hour_9to20_call_min_tot_6_mon = 0
    contact_hour_21to8_call_min_tot_6_mon = 0

    contact_hour_9to20_call_cnt_3_mon = 0
    contact_hour_21to8_call_cnt_3_mon = 0

    contact_hour_9to20_call_min_tot_3_mon = 0
    contact_hour_21to8_call_min_tot_3_mon = 0

    contact_hour_9to20_call_cnt_2_mon = 0
    contact_hour_21to8_call_cnt_2_mon = 0

    contact_hour_9to20_call_min_tot_2_mon = 0
    contact_hour_21to8_call_min_tot_2_mon = 0

    contact_hour_9to20_call_cnt_1_mon = 0
    contact_hour_21to8_call_cnt_1_mon = 0

    contact_hour_9to20_call_min_tot_1_mon = 0
    contact_hour_21to8_call_min_tot_1_mon = 0

    contact_hour_9to20_call_cnt_2_wk = 0
    contact_hour_21to8_call_cnt_2_wk = 0

    contact_hour_9to20_call_min_tot_2_wk = 0
    contact_hour_21to8_call_min_tot_2_wk = 0

    contact_hour_0to1_rece_cnt = 0
    contact_hour_2to3_rece_cnt = 0
    contact_hour_4to5_rece_cnt = 0
    contact_hour_6to7_rece_cnt = 0
    contact_hour_8to9_rece_cnt = 0
    contact_hour_10to11_rece_cnt = 0
    contact_hour_12to13_rece_cnt = 0
    contact_hour_14to15_rece_cnt = 0
    contact_hour_16to17_rece_cnt = 0
    contact_hour_18to19_rece_cnt = 0
    contact_hour_20to21_rece_cnt = 0
    contact_hour_22to23_rece_cnt = 0

    contact_hour_0to1_rece_min_tot = 0
    contact_hour_2to3_rece_min_tot = 0
    contact_hour_4to5_rece_min_tot = 0
    contact_hour_6to7_rece_min_tot = 0
    contact_hour_8to9_rece_min_tot = 0
    contact_hour_10to11_rece_min_tot = 0
    contact_hour_12to13_rece_min_tot = 0
    contact_hour_14to15_rece_min_tot = 0
    contact_hour_16to17_rece_min_tot = 0
    contact_hour_18to19_rece_min_tot = 0
    contact_hour_20to21_rece_min_tot = 0
    contact_hour_22to23_rece_min_tot = 0

    contact_hour_0to1_rece_cnt_6_mon = 0
    contact_hour_2to3_rece_cnt_6_mon = 0
    contact_hour_4to5_rece_cnt_6_mon = 0
    contact_hour_6to7_rece_cnt_6_mon = 0
    contact_hour_8to9_rece_cnt_6_mon = 0
    contact_hour_10to11_rece_cnt_6_mon = 0
    contact_hour_12to13_rece_cnt_6_mon = 0
    contact_hour_14to15_rece_cnt_6_mon = 0
    contact_hour_16to17_rece_cnt_6_mon = 0
    contact_hour_18to19_rece_cnt_6_mon = 0
    contact_hour_20to21_rece_cnt_6_mon = 0
    contact_hour_22to23_rece_cnt_6_mon = 0

    contact_hour_0to1_rece_min_tot_6_mon = 0
    contact_hour_2to3_rece_min_tot_6_mon = 0
    contact_hour_4to5_rece_min_tot_6_mon = 0
    contact_hour_6to7_rece_min_tot_6_mon = 0
    contact_hour_8to9_rece_min_tot_6_mon = 0
    contact_hour_10to11_rece_min_tot_6_mon = 0
    contact_hour_12to13_rece_min_tot_6_mon = 0
    contact_hour_14to15_rece_min_tot_6_mon = 0
    contact_hour_16to17_rece_min_tot_6_mon = 0
    contact_hour_18to19_rece_min_tot_6_mon = 0
    contact_hour_20to21_rece_min_tot_6_mon = 0
    contact_hour_22to23_rece_min_tot_6_mon = 0

    contact_hour_0to1_rece_cnt_3_mon = 0
    contact_hour_2to3_rece_cnt_3_mon = 0
    contact_hour_4to5_rece_cnt_3_mon = 0
    contact_hour_6to7_rece_cnt_3_mon = 0
    contact_hour_8to9_rece_cnt_3_mon = 0
    contact_hour_10to11_rece_cnt_3_mon = 0
    contact_hour_12to13_rece_cnt_3_mon = 0
    contact_hour_14to15_rece_cnt_3_mon = 0
    contact_hour_16to17_rece_cnt_3_mon = 0
    contact_hour_18to19_rece_cnt_3_mon = 0
    contact_hour_20to21_rece_cnt_3_mon = 0
    contact_hour_22to23_rece_cnt_3_mon = 0

    contact_hour_0to1_rece_min_tot_3_mon = 0
    contact_hour_2to3_rece_min_tot_3_mon = 0
    contact_hour_4to5_rece_min_tot_3_mon = 0
    contact_hour_6to7_rece_min_tot_3_mon = 0
    contact_hour_8to9_rece_min_tot_3_mon = 0
    contact_hour_10to11_rece_min_tot_3_mon = 0
    contact_hour_12to13_rece_min_tot_3_mon = 0
    contact_hour_14to15_rece_min_tot_3_mon = 0
    contact_hour_16to17_rece_min_tot_3_mon = 0
    contact_hour_18to19_rece_min_tot_3_mon = 0
    contact_hour_20to21_rece_min_tot_3_mon = 0
    contact_hour_22to23_rece_min_tot_3_mon = 0

    contact_hour_0to1_rece_cnt_2_mon = 0
    contact_hour_2to3_rece_cnt_2_mon = 0
    contact_hour_4to5_rece_cnt_2_mon = 0
    contact_hour_6to7_rece_cnt_2_mon = 0
    contact_hour_8to9_rece_cnt_2_mon = 0
    contact_hour_10to11_rece_cnt_2_mon = 0
    contact_hour_12to13_rece_cnt_2_mon = 0
    contact_hour_14to15_rece_cnt_2_mon = 0
    contact_hour_16to17_rece_cnt_2_mon = 0
    contact_hour_18to19_rece_cnt_2_mon = 0
    contact_hour_20to21_rece_cnt_2_mon = 0
    contact_hour_22to23_rece_cnt_2_mon = 0

    contact_hour_0to1_rece_min_tot_2_mon = 0
    contact_hour_2to3_rece_min_tot_2_mon = 0
    contact_hour_4to5_rece_min_tot_2_mon = 0
    contact_hour_6to7_rece_min_tot_2_mon = 0
    contact_hour_8to9_rece_min_tot_2_mon = 0
    contact_hour_10to11_rece_min_tot_2_mon = 0
    contact_hour_12to13_rece_min_tot_2_mon = 0
    contact_hour_14to15_rece_min_tot_2_mon = 0
    contact_hour_16to17_rece_min_tot_2_mon = 0
    contact_hour_18to19_rece_min_tot_2_mon = 0
    contact_hour_20to21_rece_min_tot_2_mon = 0
    contact_hour_22to23_rece_min_tot_2_mon = 0

    contact_hour_0to1_rece_cnt_1_mon = 0
    contact_hour_2to3_rece_cnt_1_mon = 0
    contact_hour_4to5_rece_cnt_1_mon = 0
    contact_hour_6to7_rece_cnt_1_mon = 0
    contact_hour_8to9_rece_cnt_1_mon = 0
    contact_hour_10to11_rece_cnt_1_mon = 0
    contact_hour_12to13_rece_cnt_1_mon = 0
    contact_hour_14to15_rece_cnt_1_mon = 0
    contact_hour_16to17_rece_cnt_1_mon = 0
    contact_hour_18to19_rece_cnt_1_mon = 0
    contact_hour_20to21_rece_cnt_1_mon = 0
    contact_hour_22to23_rece_cnt_1_mon = 0

    contact_hour_0to1_rece_min_tot_1_mon = 0
    contact_hour_2to3_rece_min_tot_1_mon = 0
    contact_hour_4to5_rece_min_tot_1_mon = 0
    contact_hour_6to7_rece_min_tot_1_mon = 0
    contact_hour_8to9_rece_min_tot_1_mon = 0
    contact_hour_10to11_rece_min_tot_1_mon = 0
    contact_hour_12to13_rece_min_tot_1_mon = 0
    contact_hour_14to15_rece_min_tot_1_mon = 0
    contact_hour_16to17_rece_min_tot_1_mon = 0
    contact_hour_18to19_rece_min_tot_1_mon = 0
    contact_hour_20to21_rece_min_tot_1_mon = 0
    contact_hour_22to23_rece_min_tot_1_mon = 0

    contact_hour_0to1_rece_cnt_2_wk = 0
    contact_hour_2to3_rece_cnt_2_wk = 0
    contact_hour_4to5_rece_cnt_2_wk = 0
    contact_hour_6to7_rece_cnt_2_wk = 0
    contact_hour_8to9_rece_cnt_2_wk = 0
    contact_hour_10to11_rece_cnt_2_wk = 0
    contact_hour_12to13_rece_cnt_2_wk = 0
    contact_hour_14to15_rece_cnt_2_wk = 0
    contact_hour_16to17_rece_cnt_2_wk = 0
    contact_hour_18to19_rece_cnt_2_wk = 0
    contact_hour_20to21_rece_cnt_2_wk = 0
    contact_hour_22to23_rece_cnt_2_wk = 0

    contact_hour_0to1_rece_min_tot_2_wk = 0
    contact_hour_2to3_rece_min_tot_2_wk = 0
    contact_hour_4to5_rece_min_tot_2_wk = 0
    contact_hour_6to7_rece_min_tot_2_wk = 0
    contact_hour_8to9_rece_min_tot_2_wk = 0
    contact_hour_10to11_rece_min_tot_2_wk = 0
    contact_hour_12to13_rece_min_tot_2_wk = 0
    contact_hour_14to15_rece_min_tot_2_wk = 0
    contact_hour_16to17_rece_min_tot_2_wk = 0
    contact_hour_18to19_rece_min_tot_2_wk = 0
    contact_hour_20to21_rece_min_tot_2_wk = 0
    contact_hour_22to23_rece_min_tot_2_wk = 0

    contact_hour_1to6_rece_cnt = 0
    contact_hour_7to12_rece_cnt = 0
    contact_hour_13to18_rece_cnt = 0
    contact_hour_19to0_rece_cnt = 0

    contact_hour_1to6_rece_min_tot = 0
    contact_hour_7to12_rece_min_tot = 0
    contact_hour_13to18_rece_min_tot = 0
    contact_hour_19to0_rece_min_tot = 0

    contact_hour_1to6_rece_cnt_6_mon = 0
    contact_hour_7to12_rece_cnt_6_mon = 0
    contact_hour_13to18_rece_cnt_6_mon = 0
    contact_hour_19to0_rece_cnt_6_mon = 0

    contact_hour_1to6_rece_min_tot_6_mon = 0
    contact_hour_7to12_rece_min_tot_6_mon = 0
    contact_hour_13to18_rece_min_tot_6_mon = 0
    contact_hour_19to0_rece_min_tot_6_mon = 0

    contact_hour_1to6_rece_cnt_3_mon = 0
    contact_hour_7to12_rece_cnt_3_mon = 0
    contact_hour_13to18_rece_cnt_3_mon = 0
    contact_hour_19to0_rece_cnt_3_mon = 0

    contact_hour_1to6_rece_min_tot_3_mon = 0
    contact_hour_7to12_rece_min_tot_3_mon = 0
    contact_hour_13to18_rece_min_tot_3_mon = 0
    contact_hour_19to0_rece_min_tot_3_mon = 0

    contact_hour_1to6_rece_cnt_2_mon = 0
    contact_hour_7to12_rece_cnt_2_mon = 0
    contact_hour_13to18_rece_cnt_2_mon = 0
    contact_hour_19to0_rece_cnt_2_mon = 0

    contact_hour_1to6_rece_min_tot_2_mon = 0
    contact_hour_7to12_rece_min_tot_2_mon = 0
    contact_hour_13to18_rece_min_tot_2_mon = 0
    contact_hour_19to0_rece_min_tot_2_mon = 0

    contact_hour_1to6_rece_cnt_1_mon = 0
    contact_hour_7to12_rece_cnt_1_mon = 0
    contact_hour_13to18_rece_cnt_1_mon = 0
    contact_hour_19to0_rece_cnt_1_mon = 0

    contact_hour_1to6_rece_min_tot_1_mon = 0
    contact_hour_7to12_rece_min_tot_1_mon = 0
    contact_hour_13to18_rece_min_tot_1_mon = 0
    contact_hour_19to0_rece_min_tot_1_mon = 0

    contact_hour_1to6_rece_cnt_2_wk = 0
    contact_hour_7to12_rece_cnt_2_wk = 0
    contact_hour_13to18_rece_cnt_2_wk = 0
    contact_hour_19to0_rece_cnt_2_wk = 0

    contact_hour_1to6_rece_min_tot_2_wk = 0
    contact_hour_7to12_rece_min_tot_2_wk = 0
    contact_hour_13to18_rece_min_tot_2_wk = 0
    contact_hour_19to0_rece_min_tot_2_wk = 0

    contact_hour_1to8_rece_cnt = 0
    contact_hour_9to16_rece_cnt = 0
    contact_hour_17to0_rece_cnt = 0

    contact_hour_1to8_rece_min_tot = 0
    contact_hour_9to16_rece_min_tot = 0
    contact_hour_17to0_rece_min_tot = 0

    contact_hour_1to8_rece_cnt_6_mon = 0
    contact_hour_9to16_rece_cnt_6_mon = 0
    contact_hour_17to0_rece_cnt_6_mon = 0

    contact_hour_1to8_rece_min_tot_6_mon = 0
    contact_hour_9to16_rece_min_tot_6_mon = 0
    contact_hour_17to0_rece_min_tot_6_mon = 0

    contact_hour_1to8_rece_cnt_3_mon = 0
    contact_hour_9to16_rece_cnt_3_mon = 0
    contact_hour_17to0_rece_cnt_3_mon = 0

    contact_hour_1to8_rece_min_tot_3_mon = 0
    contact_hour_9to16_rece_min_tot_3_mon = 0
    contact_hour_17to0_rece_min_tot_3_mon = 0

    contact_hour_1to8_rece_cnt_2_mon = 0
    contact_hour_9to16_rece_cnt_2_mon = 0
    contact_hour_17to0_rece_cnt_2_mon = 0

    contact_hour_1to8_rece_min_tot_2_mon = 0
    contact_hour_9to16_rece_min_tot_2_mon = 0
    contact_hour_17to0_rece_min_tot_2_mon = 0

    contact_hour_1to8_rece_cnt_1_mon = 0
    contact_hour_9to16_rece_cnt_1_mon = 0
    contact_hour_17to0_rece_cnt_1_mon = 0

    contact_hour_1to8_rece_min_tot_1_mon = 0
    contact_hour_9to16_rece_min_tot_1_mon = 0
    contact_hour_17to0_rece_min_tot_1_mon = 0

    contact_hour_1to8_rece_cnt_2_wk = 0
    contact_hour_9to16_rece_cnt_2_wk = 0
    contact_hour_17to0_rece_cnt_2_wk = 0

    contact_hour_1to8_rece_min_tot_2_wk = 0
    contact_hour_9to16_rece_min_tot_2_wk = 0
    contact_hour_17to0_rece_min_tot_2_wk = 0

    contact_hour_9to20_rece_cnt = 0
    contact_hour_21to8_rece_cnt = 0

    contact_hour_9to20_rece_min_tot = 0
    contact_hour_21to8_rece_min_tot = 0

    contact_hour_9to20_rece_cnt_6_mon = 0
    contact_hour_21to8_rece_cnt_6_mon = 0

    contact_hour_9to20_rece_min_tot_6_mon = 0
    contact_hour_21to8_rece_min_tot_6_mon = 0

    contact_hour_9to20_rece_cnt_3_mon = 0
    contact_hour_21to8_rece_cnt_3_mon = 0

    contact_hour_9to20_rece_min_tot_3_mon = 0
    contact_hour_21to8_rece_min_tot_3_mon = 0

    contact_hour_9to20_rece_cnt_2_mon = 0
    contact_hour_21to8_rece_cnt_2_mon = 0

    contact_hour_9to20_rece_min_tot_2_mon = 0
    contact_hour_21to8_rece_min_tot_2_mon = 0

    contact_hour_9to20_rece_cnt_1_mon = 0
    contact_hour_21to8_rece_cnt_1_mon = 0

    contact_hour_9to20_rece_min_tot_1_mon = 0
    contact_hour_21to8_rece_min_tot_1_mon = 0

    contact_hour_9to20_rece_cnt_2_wk = 0
    contact_hour_21to8_rece_cnt_2_wk = 0

    contact_hour_9to20_rece_min_tot_2_wk = 0
    contact_hour_21to8_rece_min_tot_2_wk = 0

    # avg
    contact_hour_0_min_avg = 0
    contact_hour_1_min_avg = 0
    contact_hour_2_min_avg = 0
    contact_hour_3_min_avg = 0
    contact_hour_4_min_avg = 0
    contact_hour_5_min_avg = 0
    contact_hour_6_min_avg = 0
    contact_hour_7_min_avg = 0
    contact_hour_8_min_avg = 0
    contact_hour_9_min_avg = 0
    contact_hour_10_min_avg = 0
    contact_hour_11_min_avg = 0
    contact_hour_12_min_avg = 0
    contact_hour_13_min_avg = 0
    contact_hour_14_min_avg = 0
    contact_hour_15_min_avg = 0
    contact_hour_16_min_avg = 0
    contact_hour_17_min_avg = 0
    contact_hour_18_min_avg = 0
    contact_hour_19_min_avg = 0
    contact_hour_20_min_avg = 0
    contact_hour_21_min_avg = 0
    contact_hour_22_min_avg = 0
    contact_hour_23_min_avg = 0

    contact_hour_0_min_avg_6_mon = 0
    contact_hour_1_min_avg_6_mon = 0
    contact_hour_2_min_avg_6_mon = 0
    contact_hour_3_min_avg_6_mon = 0
    contact_hour_4_min_avg_6_mon = 0
    contact_hour_5_min_avg_6_mon = 0
    contact_hour_6_min_avg_6_mon = 0
    contact_hour_7_min_avg_6_mon = 0
    contact_hour_8_min_avg_6_mon = 0
    contact_hour_9_min_avg_6_mon = 0
    contact_hour_10_min_avg_6_mon = 0
    contact_hour_11_min_avg_6_mon = 0
    contact_hour_12_min_avg_6_mon = 0
    contact_hour_13_min_avg_6_mon = 0
    contact_hour_14_min_avg_6_mon = 0
    contact_hour_15_min_avg_6_mon = 0
    contact_hour_16_min_avg_6_mon = 0
    contact_hour_17_min_avg_6_mon = 0
    contact_hour_18_min_avg_6_mon = 0
    contact_hour_19_min_avg_6_mon = 0
    contact_hour_20_min_avg_6_mon = 0
    contact_hour_21_min_avg_6_mon = 0
    contact_hour_22_min_avg_6_mon = 0
    contact_hour_23_min_avg_6_mon = 0

    contact_hour_0_min_avg_3_mon = 0
    contact_hour_1_min_avg_3_mon = 0
    contact_hour_2_min_avg_3_mon = 0
    contact_hour_3_min_avg_3_mon = 0
    contact_hour_4_min_avg_3_mon = 0
    contact_hour_5_min_avg_3_mon = 0
    contact_hour_6_min_avg_3_mon = 0
    contact_hour_7_min_avg_3_mon = 0
    contact_hour_8_min_avg_3_mon = 0
    contact_hour_9_min_avg_3_mon = 0
    contact_hour_10_min_avg_3_mon = 0
    contact_hour_11_min_avg_3_mon = 0
    contact_hour_12_min_avg_3_mon = 0
    contact_hour_13_min_avg_3_mon = 0
    contact_hour_14_min_avg_3_mon = 0
    contact_hour_15_min_avg_3_mon = 0
    contact_hour_16_min_avg_3_mon = 0
    contact_hour_17_min_avg_3_mon = 0
    contact_hour_18_min_avg_3_mon = 0
    contact_hour_19_min_avg_3_mon = 0
    contact_hour_20_min_avg_3_mon = 0
    contact_hour_21_min_avg_3_mon = 0
    contact_hour_22_min_avg_3_mon = 0
    contact_hour_23_min_avg_3_mon = 0

    contact_hour_0_min_avg_2_mon = 0
    contact_hour_1_min_avg_2_mon = 0
    contact_hour_2_min_avg_2_mon = 0
    contact_hour_3_min_avg_2_mon = 0
    contact_hour_4_min_avg_2_mon = 0
    contact_hour_5_min_avg_2_mon = 0
    contact_hour_6_min_avg_2_mon = 0
    contact_hour_7_min_avg_2_mon = 0
    contact_hour_8_min_avg_2_mon = 0
    contact_hour_9_min_avg_2_mon = 0
    contact_hour_10_min_avg_2_mon = 0
    contact_hour_11_min_avg_2_mon = 0
    contact_hour_12_min_avg_2_mon = 0
    contact_hour_13_min_avg_2_mon = 0
    contact_hour_14_min_avg_2_mon = 0
    contact_hour_15_min_avg_2_mon = 0
    contact_hour_16_min_avg_2_mon = 0
    contact_hour_17_min_avg_2_mon = 0
    contact_hour_18_min_avg_2_mon = 0
    contact_hour_19_min_avg_2_mon = 0
    contact_hour_20_min_avg_2_mon = 0
    contact_hour_21_min_avg_2_mon = 0
    contact_hour_22_min_avg_2_mon = 0
    contact_hour_23_min_avg_2_mon = 0

    contact_hour_0_min_avg_1_mon = 0
    contact_hour_1_min_avg_1_mon = 0
    contact_hour_2_min_avg_1_mon = 0
    contact_hour_3_min_avg_1_mon = 0
    contact_hour_4_min_avg_1_mon = 0
    contact_hour_5_min_avg_1_mon = 0
    contact_hour_6_min_avg_1_mon = 0
    contact_hour_7_min_avg_1_mon = 0
    contact_hour_8_min_avg_1_mon = 0
    contact_hour_9_min_avg_1_mon = 0
    contact_hour_10_min_avg_1_mon = 0
    contact_hour_11_min_avg_1_mon = 0
    contact_hour_12_min_avg_1_mon = 0
    contact_hour_13_min_avg_1_mon = 0
    contact_hour_14_min_avg_1_mon = 0
    contact_hour_15_min_avg_1_mon = 0
    contact_hour_16_min_avg_1_mon = 0
    contact_hour_17_min_avg_1_mon = 0
    contact_hour_18_min_avg_1_mon = 0
    contact_hour_19_min_avg_1_mon = 0
    contact_hour_20_min_avg_1_mon = 0
    contact_hour_21_min_avg_1_mon = 0
    contact_hour_22_min_avg_1_mon = 0
    contact_hour_23_min_avg_1_mon = 0

    contact_hour_0_min_avg_2_wk = 0
    contact_hour_1_min_avg_2_wk = 0
    contact_hour_2_min_avg_2_wk = 0
    contact_hour_3_min_avg_2_wk = 0
    contact_hour_4_min_avg_2_wk = 0
    contact_hour_5_min_avg_2_wk = 0
    contact_hour_6_min_avg_2_wk = 0
    contact_hour_7_min_avg_2_wk = 0
    contact_hour_8_min_avg_2_wk = 0
    contact_hour_9_min_avg_2_wk = 0
    contact_hour_10_min_avg_2_wk = 0
    contact_hour_11_min_avg_2_wk = 0
    contact_hour_12_min_avg_2_wk = 0
    contact_hour_13_min_avg_2_wk = 0
    contact_hour_14_min_avg_2_wk = 0
    contact_hour_15_min_avg_2_wk = 0
    contact_hour_16_min_avg_2_wk = 0
    contact_hour_17_min_avg_2_wk = 0
    contact_hour_18_min_avg_2_wk = 0
    contact_hour_19_min_avg_2_wk = 0
    contact_hour_20_min_avg_2_wk = 0
    contact_hour_21_min_avg_2_wk = 0
    contact_hour_22_min_avg_2_wk = 0
    contact_hour_23_min_avg_2_wk = 0

    contact_hour_0to1_min_avg = 0
    contact_hour_2to3_min_avg = 0
    contact_hour_4to5_min_avg = 0
    contact_hour_6to7_min_avg = 0
    contact_hour_8to9_min_avg = 0
    contact_hour_10to11_min_avg = 0
    contact_hour_12to13_min_avg = 0
    contact_hour_14to15_min_avg = 0
    contact_hour_16to17_min_avg = 0
    contact_hour_18to19_min_avg = 0
    contact_hour_20to21_min_avg = 0
    contact_hour_22to23_min_avg = 0

    contact_hour_0to1_min_avg_6_mon = 0
    contact_hour_2to3_min_avg_6_mon = 0
    contact_hour_4to5_min_avg_6_mon = 0
    contact_hour_6to7_min_avg_6_mon = 0
    contact_hour_8to9_min_avg_6_mon = 0
    contact_hour_10to11_min_avg_6_mon = 0
    contact_hour_12to13_min_avg_6_mon = 0
    contact_hour_14to15_min_avg_6_mon = 0
    contact_hour_16to17_min_avg_6_mon = 0
    contact_hour_18to19_min_avg_6_mon = 0
    contact_hour_20to21_min_avg_6_mon = 0
    contact_hour_22to23_min_avg_6_mon = 0

    contact_hour_0to1_min_avg_3_mon = 0
    contact_hour_2to3_min_avg_3_mon = 0
    contact_hour_4to5_min_avg_3_mon = 0
    contact_hour_6to7_min_avg_3_mon = 0
    contact_hour_8to9_min_avg_3_mon = 0
    contact_hour_10to11_min_avg_3_mon = 0
    contact_hour_12to13_min_avg_3_mon = 0
    contact_hour_14to15_min_avg_3_mon = 0
    contact_hour_16to17_min_avg_3_mon = 0
    contact_hour_18to19_min_avg_3_mon = 0
    contact_hour_20to21_min_avg_3_mon = 0
    contact_hour_22to23_min_avg_3_mon = 0

    contact_hour_0to1_min_avg_2_mon = 0
    contact_hour_2to3_min_avg_2_mon = 0
    contact_hour_4to5_min_avg_2_mon = 0
    contact_hour_6to7_min_avg_2_mon = 0
    contact_hour_8to9_min_avg_2_mon = 0
    contact_hour_10to11_min_avg_2_mon = 0
    contact_hour_12to13_min_avg_2_mon = 0
    contact_hour_14to15_min_avg_2_mon = 0
    contact_hour_16to17_min_avg_2_mon = 0
    contact_hour_18to19_min_avg_2_mon = 0
    contact_hour_20to21_min_avg_2_mon = 0
    contact_hour_22to23_min_avg_2_mon = 0

    contact_hour_0to1_min_avg_1_mon = 0
    contact_hour_2to3_min_avg_1_mon = 0
    contact_hour_4to5_min_avg_1_mon = 0
    contact_hour_6to7_min_avg_1_mon = 0
    contact_hour_8to9_min_avg_1_mon = 0
    contact_hour_10to11_min_avg_1_mon = 0
    contact_hour_12to13_min_avg_1_mon = 0
    contact_hour_14to15_min_avg_1_mon = 0
    contact_hour_16to17_min_avg_1_mon = 0
    contact_hour_18to19_min_avg_1_mon = 0
    contact_hour_20to21_min_avg_1_mon = 0
    contact_hour_22to23_min_avg_1_mon = 0

    contact_hour_0to1_min_avg_2_wk = 0
    contact_hour_2to3_min_avg_2_wk = 0
    contact_hour_4to5_min_avg_2_wk = 0
    contact_hour_6to7_min_avg_2_wk = 0
    contact_hour_8to9_min_avg_2_wk = 0
    contact_hour_10to11_min_avg_2_wk = 0
    contact_hour_12to13_min_avg_2_wk = 0
    contact_hour_14to15_min_avg_2_wk = 0
    contact_hour_16to17_min_avg_2_wk = 0
    contact_hour_18to19_min_avg_2_wk = 0
    contact_hour_20to21_min_avg_2_wk = 0
    contact_hour_22to23_min_avg_2_wk = 0

    contact_hour_1to8_min_avg = 0
    contact_hour_9to16_min_avg = 0
    contact_hour_17to0_min_avg = 0

    contact_hour_1to8_min_avg_6_mon = 0
    contact_hour_9to16_min_avg_6_mon = 0
    contact_hour_17to0_min_avg_6_mon = 0

    contact_hour_1to8_min_avg_3_mon = 0
    contact_hour_9to16_min_avg_3_mon = 0
    contact_hour_17to0_min_avg_3_mon = 0

    contact_hour_1to8_min_avg_2_mon = 0
    contact_hour_9to16_min_avg_2_mon = 0
    contact_hour_17to0_min_avg_2_mon = 0

    contact_hour_1to8_min_avg_1_mon = 0
    contact_hour_9to16_min_avg_1_mon = 0
    contact_hour_17to0_min_avg_1_mon = 0

    contact_hour_1to8_min_avg_2_wk = 0
    contact_hour_9to16_min_avg_2_wk = 0
    contact_hour_17to0_min_avg_2_wk = 0

    contact_hour_1to6_call_min_avg = 0
    contact_hour_7to12_call_min_avg = 0
    contact_hour_13to18_call_min_avg = 0
    contact_hour_19to0_call_min_avg = 0

    contact_hour_1to6_call_min_avg_6_mon = 0
    contact_hour_7to12_call_min_avg_6_mon = 0
    contact_hour_13to18_call_min_avg_6_mon = 0
    contact_hour_19to0_call_min_avg_6_mon = 0

    contact_hour_1to6_call_min_avg_3_mon = 0
    contact_hour_7to12_call_min_avg_3_mon = 0
    contact_hour_13to18_call_min_avg_3_mon = 0
    contact_hour_19to0_call_min_avg_3_mon = 0

    contact_hour_1to6_call_min_avg_2_mon = 0
    contact_hour_7to12_call_min_avg_2_mon = 0
    contact_hour_13to18_call_min_avg_2_mon = 0
    contact_hour_19to0_call_min_avg_2_mon = 0

    contact_hour_1to6_call_min_avg_1_mon = 0
    contact_hour_7to12_call_min_avg_1_mon = 0
    contact_hour_13to18_call_min_avg_1_mon = 0
    contact_hour_19to0_call_min_avg_1_mon = 0

    contact_hour_1to6_call_min_avg_2_wk = 0
    contact_hour_7to12_call_min_avg_2_wk = 0
    contact_hour_13to18_call_min_avg_2_wk = 0
    contact_hour_19to0_call_min_avg_2_wk = 0

    contact_hour_1to8_call_min_avg = 0
    contact_hour_9to16_call_min_avg = 0
    contact_hour_17to0_call_min_avg = 0

    contact_hour_1to8_call_min_avg_6_mon = 0
    contact_hour_9to16_call_min_avg_6_mon = 0
    contact_hour_17to0_call_min_avg_6_mon = 0

    contact_hour_1to8_call_min_avg_3_mon = 0
    contact_hour_9to16_call_min_avg_3_mon = 0
    contact_hour_17to0_call_min_avg_3_mon = 0

    contact_hour_1to8_call_min_avg_2_mon = 0
    contact_hour_9to16_call_min_avg_2_mon = 0
    contact_hour_17to0_call_min_avg_2_mon = 0

    contact_hour_1to8_call_min_avg_1_mon = 0
    contact_hour_9to16_call_min_avg_1_mon = 0
    contact_hour_17to0_call_min_avg_1_mon = 0

    contact_hour_1to8_call_min_avg_2_wk = 0
    contact_hour_9to16_call_min_avg_2_wk = 0
    contact_hour_17to0_call_min_avg_2_wk = 0

    contact_hour_9to20_call_min_avg = 0
    contact_hour_21to8_call_min_avg = 0

    contact_hour_9to20_call_min_avg_6_mon = 0
    contact_hour_21to8_call_min_avg_6_mon = 0

    contact_hour_9to20_call_min_avg_3_mon = 0
    contact_hour_21to8_call_min_avg_3_mon = 0

    contact_hour_9to20_call_min_avg_2_mon = 0
    contact_hour_21to8_call_min_avg_2_mon = 0

    contact_hour_9to20_call_min_avg_1_mon = 0
    contact_hour_21to8_call_min_avg_1_mon = 0

    contact_hour_9to20_call_min_avg_2_wk = 0
    contact_hour_21to8_call_min_avg_2_wk = 0

    contact_hour_1to6_rece_min_avg = 0
    contact_hour_7to12_rece_min_avg = 0
    contact_hour_13to18_rece_min_avg = 0
    contact_hour_19to0_rece_min_avg = 0

    contact_hour_1to6_rece_min_avg_6_mon = 0
    contact_hour_7to12_rece_min_avg_6_mon = 0
    contact_hour_13to18_rece_min_avg_6_mon = 0
    contact_hour_19to0_rece_min_avg_6_mon = 0

    contact_hour_1to6_rece_min_avg_3_mon = 0
    contact_hour_7to12_rece_min_avg_3_mon = 0
    contact_hour_13to18_rece_min_avg_3_mon = 0
    contact_hour_19to0_rece_min_avg_3_mon = 0

    contact_hour_1to6_rece_min_avg_2_mon = 0
    contact_hour_7to12_rece_min_avg_2_mon = 0
    contact_hour_13to18_rece_min_avg_2_mon = 0
    contact_hour_19to0_rece_min_avg_2_mon = 0

    contact_hour_1to6_rece_min_avg_1_mon = 0
    contact_hour_7to12_rece_min_avg_1_mon = 0
    contact_hour_13to18_rece_min_avg_1_mon = 0
    contact_hour_19to0_rece_min_avg_1_mon = 0

    contact_hour_1to6_rece_min_avg_2_wk = 0
    contact_hour_7to12_rece_min_avg_2_wk = 0
    contact_hour_13to18_rece_min_avg_2_wk = 0
    contact_hour_19to0_rece_min_avg_2_wk = 0

    contact_hour_1to8_rece_min_avg = 0
    contact_hour_9to16_rece_min_avg = 0
    contact_hour_17to0_rece_min_avg = 0

    contact_hour_1to8_rece_min_avg_6_mon = 0
    contact_hour_9to16_rece_min_avg_6_mon = 0
    contact_hour_17to0_rece_min_avg_6_mon = 0

    contact_hour_1to8_rece_min_avg_3_mon = 0
    contact_hour_9to16_rece_min_avg_3_mon = 0
    contact_hour_17to0_rece_min_avg_3_mon = 0

    contact_hour_1to8_rece_min_avg_2_mon = 0
    contact_hour_9to16_rece_min_avg_2_mon = 0
    contact_hour_17to0_rece_min_avg_2_mon = 0

    contact_hour_1to8_rece_min_avg_1_mon = 0
    contact_hour_9to16_rece_min_avg_1_mon = 0
    contact_hour_17to0_rece_min_avg_1_mon = 0

    contact_hour_1to8_rece_min_avg_2_wk = 0
    contact_hour_9to16_rece_min_avg_2_wk = 0
    contact_hour_17to0_rece_min_avg_2_wk = 0

    contact_hour_9to20_rece_min_avg = 0
    contact_hour_21to8_rece_min_avg = 0

    contact_hour_9to20_rece_min_avg_6_mon = 0
    contact_hour_21to8_rece_min_avg_6_mon = 0

    contact_hour_9to20_rece_min_avg_3_mon = 0
    contact_hour_21to8_rece_min_avg_3_mon = 0

    contact_hour_9to20_rece_min_avg_2_mon = 0
    contact_hour_21to8_rece_min_avg_2_mon = 0

    contact_hour_9to20_rece_min_avg_1_mon = 0
    contact_hour_21to8_rece_min_avg_1_mon = 0

    contact_hour_9to20_rece_min_avg_2_wk = 0
    contact_hour_21to8_rece_min_avg_2_wk = 0

    # 24 hour perc
    contact_hour_1to6_cnt_24h_perc = 0
    contact_hour_7to12_cnt_24h_perc = 0
    contact_hour_13to18_cnt_24h_perc = 0
    contact_hour_19to0_cnt_24h_perc = 0

    contact_hour_1to6_min_tot_24h_perc = 0
    contact_hour_7to12_min_tot_24h_perc = 0
    contact_hour_13to18_min_tot_24h_perc = 0
    contact_hour_19to0_min_tot_24h_perc = 0

    contact_hour_1to6_cnt_6_mon_24h_perc = 0
    contact_hour_7to12_cnt_6_mon_24h_perc = 0
    contact_hour_13to18_cnt_6_mon_24h_perc = 0
    contact_hour_19to0_cnt_6_mon_24h_perc = 0

    contact_hour_1to6_min_tot_6_mon_24h_perc = 0
    contact_hour_7to12_min_tot_6_mon_24h_perc = 0
    contact_hour_13to18_min_tot_6_mon_24h_perc = 0
    contact_hour_19to0_min_tot_6_mon_24h_perc = 0

    contact_hour_1to6_cnt_3_mon_24h_perc = 0
    contact_hour_7to12_cnt_3_mon_24h_perc = 0
    contact_hour_13to18_cnt_3_mon_24h_perc = 0
    contact_hour_19to0_cnt_3_mon_24h_perc = 0

    contact_hour_1to6_min_tot_3_mon_24h_perc = 0
    contact_hour_7to12_min_tot_3_mon_24h_perc = 0
    contact_hour_13to18_min_tot_3_mon_24h_perc = 0
    contact_hour_19to0_min_tot_3_mon_24h_perc = 0

    contact_hour_1to6_cnt_2_mon_24h_perc = 0
    contact_hour_7to12_cnt_2_mon_24h_perc = 0
    contact_hour_13to18_cnt_2_mon_24h_perc = 0
    contact_hour_19to0_cnt_2_mon_24h_perc = 0

    contact_hour_1to6_min_tot_2_mon_24h_perc = 0
    contact_hour_7to12_min_tot_2_mon_24h_perc = 0
    contact_hour_13to18_min_tot_2_mon_24h_perc = 0
    contact_hour_19to0_min_tot_2_mon_24h_perc = 0

    contact_hour_1to6_cnt_1_mon_24h_perc = 0
    contact_hour_7to12_cnt_1_mon_24h_perc = 0
    contact_hour_13to18_cnt_1_mon_24h_perc = 0
    contact_hour_19to0_cnt_1_mon_24h_perc = 0

    contact_hour_1to6_min_tot_1_mon_24h_perc = 0
    contact_hour_7to12_min_tot_1_mon_24h_perc = 0
    contact_hour_13to18_min_tot_1_mon_24h_perc = 0
    contact_hour_19to0_min_tot_1_mon_24h_perc = 0

    contact_hour_1to6_cnt_2_wk_24h_perc = 0
    contact_hour_7to12_cnt_2_wk_24h_perc = 0
    contact_hour_13to18_cnt_2_wk_24h_perc = 0
    contact_hour_19to0_cnt_2_wk_24h_perc = 0

    contact_hour_1to6_min_tot_2_wk_24h_perc = 0
    contact_hour_7to12_min_tot_2_wk_24h_perc = 0
    contact_hour_13to18_min_tot_2_wk_24h_perc = 0
    contact_hour_19to0_min_tot_2_wk_24h_perc = 0

    contact_hour_1to8_cnt_24h_perc = 0
    contact_hour_9to16_cnt_24h_perc = 0
    contact_hour_17to0_cnt_24h_perc = 0

    contact_hour_1to8_min_tot_24h_perc = 0
    contact_hour_9to16_min_tot_24h_perc = 0
    contact_hour_17to0_min_tot_24h_perc = 0

    contact_hour_1to8_cnt_6_mon_24h_perc = 0
    contact_hour_9to16_cnt_6_mon_24h_perc = 0
    contact_hour_17to0_cnt_6_mon_24h_perc = 0

    contact_hour_1to8_min_tot_6_mon_24h_perc = 0
    contact_hour_9to16_min_tot_6_mon_24h_perc = 0
    contact_hour_17to0_min_tot_6_mon_24h_perc = 0

    contact_hour_1to8_cnt_3_mon_24h_perc = 0
    contact_hour_9to16_cnt_3_mon_24h_perc = 0
    contact_hour_17to0_cnt_3_mon_24h_perc = 0

    contact_hour_1to8_min_tot_3_mon_24h_perc = 0
    contact_hour_9to16_min_tot_3_mon_24h_perc = 0
    contact_hour_17to0_min_tot_3_mon_24h_perc = 0

    contact_hour_1to8_cnt_2_mon_24h_perc = 0
    contact_hour_9to16_cnt_2_mon_24h_perc = 0
    contact_hour_17to0_cnt_2_mon_24h_perc = 0

    contact_hour_1to8_min_tot_2_mon_24h_perc = 0
    contact_hour_9to16_min_tot_2_mon_24h_perc = 0
    contact_hour_17to0_min_tot_2_mon_24h_perc = 0

    contact_hour_1to8_cnt_1_mon_24h_perc = 0
    contact_hour_9to16_cnt_1_mon_24h_perc = 0
    contact_hour_17to0_cnt_1_mon_24h_perc = 0

    contact_hour_1to8_min_tot_1_mon_24h_perc = 0
    contact_hour_9to16_min_tot_1_mon_24h_perc = 0
    contact_hour_17to0_min_tot_1_mon_24h_perc = 0

    contact_hour_1to8_cnt_2_wk_24h_perc = 0
    contact_hour_9to16_cnt_2_wk_24h_perc = 0
    contact_hour_17to0_cnt_2_wk_24h_perc = 0

    contact_hour_1to8_min_tot_2_wk_24h_perc = 0
    contact_hour_9to16_min_tot_2_wk_24h_perc = 0
    contact_hour_17to0_min_tot_2_wk_24h_perc = 0

    contact_hour_9to20_cnt_24_hour_perc = 0
    contact_hour_21to8_cnt_24_hour_perc = 0

    contact_hour_9to20_min_tot_24_hour_perc = 0
    contact_hour_21to8_min_tot_24_hour_perc = 0

    contact_hour_9to20_cnt_6_mon_24_hour_perc = 0
    contact_hour_21to8_cnt_6_mon_24_hour_perc = 0

    contact_hour_9to20_min_tot_6_mon_24_hour_perc = 0
    contact_hour_21to8_min_tot_6_mon_24_hour_perc = 0

    contact_hour_9to20_cnt_3_mon_24_hour_perc = 0
    contact_hour_21to8_cnt_3_mon_24_hour_perc = 0

    contact_hour_9to20_min_tot_3_mon_24_hour_perc = 0
    contact_hour_21to8_min_tot_3_mon_24_hour_perc = 0

    contact_hour_9to20_cnt_2_mon_24_hour_perc = 0
    contact_hour_21to8_cnt_2_mon_24_hour_perc = 0

    contact_hour_9to20_min_tot_2_mon_24_hour_perc = 0
    contact_hour_21to8_min_tot_2_mon_24_hour_perc = 0

    contact_hour_9to20_cnt_2_wk_24_hour_perc = 0
    contact_hour_21to8_cnt_2_wk_24_hour_perc = 0

    contact_hour_9to20_min_tot_2_wk_24_hour_perc = 0
    contact_hour_21to8_min_tot_2_wk_24_hour_perc = 0

    contact_hour_1to6_call_cnt_24h_perc = 0
    contact_hour_7to12_call_cnt_24h_perc = 0
    contact_hour_13to18_call_cnt_24h_perc = 0
    contact_hour_19to0_call_cnt_24h_perc = 0

    contact_hour_1to6_call_min_tot_24h_perc = 0
    contact_hour_7to12_call_min_tot_24h_perc = 0
    contact_hour_13to18_call_min_tot_24h_perc = 0
    contact_hour_19to0_call_min_tot_24h_perc = 0

    contact_hour_1to6_call_cnt_6_mon_24h_perc = 0
    contact_hour_7to12_call_cnt_6_mon_24h_perc = 0
    contact_hour_13to18_call_cnt_6_mon_24h_perc = 0
    contact_hour_19to0_call_cnt_6_mon_24h_perc = 0

    contact_hour_1to6_call_min_tot_6_mon_24h_perc = 0
    contact_hour_7to12_call_min_tot_6_mon_24h_perc = 0
    contact_hour_13to18_call_min_tot_6_mon_24h_perc = 0
    contact_hour_19to0_call_min_tot_6_mon_24h_perc = 0

    contact_hour_1to6_call_cnt_3_mon_24h_perc = 0
    contact_hour_7to12_call_cnt_3_mon_24h_perc = 0
    contact_hour_13to18_call_cnt_3_mon_24h_perc = 0
    contact_hour_19to0_call_cnt_3_mon_24h_perc = 0

    contact_hour_1to6_call_min_tot_3_mon_24h_perc = 0
    contact_hour_7to12_call_min_tot_3_mon_24h_perc = 0
    contact_hour_13to18_call_min_tot_3_mon_24h_perc = 0
    contact_hour_19to0_call_min_tot_3_mon_24h_perc = 0

    contact_hour_1to6_call_cnt_2_mon_24h_perc = 0
    contact_hour_7to12_call_cnt_2_mon_24h_perc = 0
    contact_hour_13to18_call_cnt_2_mon_24h_perc = 0
    contact_hour_19to0_call_cnt_2_mon_24h_perc = 0

    contact_hour_1to6_call_min_tot_2_mon_24h_perc = 0
    contact_hour_7to12_call_min_tot_2_mon_24h_perc = 0
    contact_hour_13to18_call_min_tot_2_mon_24h_perc = 0
    contact_hour_19to0_call_min_tot_2_mon_24h_perc = 0

    contact_hour_1to6_call_cnt_1_mon_24h_perc = 0
    contact_hour_7to12_call_cnt_1_mon_24h_perc = 0
    contact_hour_13to18_call_cnt_1_mon_24h_perc = 0
    contact_hour_19to0_call_cnt_1_mon_24h_perc = 0

    contact_hour_1to6_call_min_tot_1_mon_24h_perc = 0
    contact_hour_7to12_call_min_tot_1_mon_24h_perc = 0
    contact_hour_13to18_call_min_tot_1_mon_24h_perc = 0
    contact_hour_19to0_call_min_tot_1_mon_24h_perc = 0

    contact_hour_1to6_call_cnt_2_wk_24h_perc = 0
    contact_hour_7to12_call_cnt_2_wk_24h_perc = 0
    contact_hour_13to18_call_cnt_2_wk_24h_perc = 0
    contact_hour_19to0_call_cnt_2_wk_24h_perc = 0

    contact_hour_1to6_call_min_tot_2_wk_24h_perc = 0
    contact_hour_7to12_call_min_tot_2_wk_24h_perc = 0
    contact_hour_13to18_call_min_tot_2_wk_24h_perc = 0
    contact_hour_19to0_call_min_tot_2_wk_24h_perc = 0

    contact_hour_1to8_call_cnt_24h_perc = 0
    contact_hour_9to16_call_cnt_24h_perc = 0
    contact_hour_17to0_call_cnt_24h_perc = 0

    contact_hour_1to8_call_min_tot_24h_perc = 0
    contact_hour_9to16_call_min_tot_24h_perc = 0
    contact_hour_17to0_call_min_tot_24h_perc = 0

    contact_hour_1to8_call_cnt_6_mon_24h_perc = 0
    contact_hour_9to16_call_cnt_6_mon_24h_perc = 0
    contact_hour_17to0_call_cnt_6_mon_24h_perc = 0

    contact_hour_1to8_call_min_tot_6_mon_24h_perc = 0
    contact_hour_9to16_call_min_tot_6_mon_24h_perc = 0
    contact_hour_17to0_call_min_tot_6_mon_24h_perc = 0

    contact_hour_1to8_call_cnt_3_mon_24h_perc = 0
    contact_hour_9to16_call_cnt_3_mon_24h_perc = 0
    contact_hour_17to0_call_cnt_3_mon_24h_perc = 0

    contact_hour_1to8_call_min_tot_3_mon_24h_perc = 0
    contact_hour_9to16_call_min_tot_3_mon_24h_perc = 0
    contact_hour_17to0_call_min_tot_3_mon_24h_perc = 0

    contact_hour_1to8_call_cnt_2_mon_24h_perc = 0
    contact_hour_9to16_call_cnt_2_mon_24h_perc = 0
    contact_hour_17to0_call_cnt_2_mon_24h_perc = 0

    contact_hour_1to8_call_min_tot_2_mon_24h_perc = 0
    contact_hour_9to16_call_min_tot_2_mon_24h_perc = 0
    contact_hour_17to0_call_min_tot_2_mon_24h_perc = 0

    contact_hour_1to8_call_cnt_1_mon_24h_perc = 0
    contact_hour_9to16_call_cnt_1_mon_24h_perc = 0
    contact_hour_17to0_call_cnt_1_mon_24h_perc = 0

    contact_hour_1to8_call_min_tot_1_mon_24h_perc = 0
    contact_hour_9to16_call_min_tot_1_mon_24h_perc = 0
    contact_hour_17to0_call_min_tot_1_mon_24h_perc = 0

    contact_hour_1to8_call_cnt_2_wk_24h_perc = 0
    contact_hour_9to16_call_cnt_2_wk_24h_perc = 0
    contact_hour_17to0_call_cnt_2_wk_24h_perc = 0

    contact_hour_1to8_call_min_tot_2_wk_24h_perc = 0
    contact_hour_9to16_call_min_tot_2_wk_24h_perc = 0
    contact_hour_17to0_call_min_tot_2_wk_24h_perc = 0

    contact_hour_9to20_call_cnt_24_hour_perc = 0
    contact_hour_21to8_call_cnt_24_hour_perc = 0

    contact_hour_9to20_call_min_tot_24_hour_perc = 0
    contact_hour_21to8_call_min_tot_24_hour_perc = 0

    contact_hour_9to20_call_cnt_6_mon_24_hour_perc = 0
    contact_hour_21to8_call_cnt_6_mon_24_hour_perc = 0

    contact_hour_9to20_call_min_tot_6_mon_24_hour_perc = 0
    contact_hour_21to8_call_min_tot_6_mon_24_hour_perc = 0

    contact_hour_9to20_call_cnt_3_mon_24_hour_perc = 0
    contact_hour_21to8_call_cnt_3_mon_24_hour_perc = 0

    contact_hour_9to20_call_min_tot_3_mon_24_hour_perc = 0
    contact_hour_21to8_call_min_tot_3_mon_24_hour_perc = 0

    contact_hour_9to20_call_cnt_2_mon_24_hour_perc = 0
    contact_hour_21to8_call_cnt_2_mon_24_hour_perc = 0

    contact_hour_9to20_call_min_tot_2_mon_24_hour_perc = 0
    contact_hour_21to8_call_min_tot_2_mon_24_hour_perc = 0

    contact_hour_9to20_call_cnt_2_wk_24_hour_perc = 0
    contact_hour_21to8_call_cnt_2_wk_24_hour_perc = 0

    contact_hour_9to20_call_min_tot_2_wk_24_hour_perc = 0
    contact_hour_21to8_call_min_tot_2_wk_24_hour_perc = 0

    contact_hour_1to6_rece_cnt_24h_perc = 0
    contact_hour_7to12_rece_cnt_24h_perc = 0
    contact_hour_13to18_rece_cnt_24h_perc = 0
    contact_hour_19to0_rece_cnt_24h_perc = 0

    contact_hour_1to6_rece_min_tot_24h_perc = 0
    contact_hour_7to12_rece_min_tot_24h_perc = 0
    contact_hour_13to18_rece_min_tot_24h_perc = 0
    contact_hour_19to0_rece_min_tot_24h_perc = 0

    contact_hour_1to6_rece_cnt_6_mon_24h_perc = 0
    contact_hour_7to12_rece_cnt_6_mon_24h_perc = 0
    contact_hour_13to18_rece_cnt_6_mon_24h_perc = 0
    contact_hour_19to0_rece_cnt_6_mon_24h_perc = 0

    contact_hour_1to6_rece_min_tot_6_mon_24h_perc = 0
    contact_hour_7to12_rece_min_tot_6_mon_24h_perc = 0
    contact_hour_13to18_rece_min_tot_6_mon_24h_perc = 0
    contact_hour_19to0_rece_min_tot_6_mon_24h_perc = 0

    contact_hour_1to6_rece_cnt_3_mon_24h_perc = 0
    contact_hour_7to12_rece_cnt_3_mon_24h_perc = 0
    contact_hour_13to18_rece_cnt_3_mon_24h_perc = 0
    contact_hour_19to0_rece_cnt_3_mon_24h_perc = 0

    contact_hour_1to6_rece_min_tot_3_mon_24h_perc = 0
    contact_hour_7to12_rece_min_tot_3_mon_24h_perc = 0
    contact_hour_13to18_rece_min_tot_3_mon_24h_perc = 0
    contact_hour_19to0_rece_min_tot_3_mon_24h_perc = 0

    contact_hour_1to6_rece_cnt_2_mon_24h_perc = 0
    contact_hour_7to12_rece_cnt_2_mon_24h_perc = 0
    contact_hour_13to18_rece_cnt_2_mon_24h_perc = 0
    contact_hour_19to0_rece_cnt_2_mon_24h_perc = 0

    contact_hour_1to6_rece_min_tot_2_mon_24h_perc = 0
    contact_hour_7to12_rece_min_tot_2_mon_24h_perc = 0
    contact_hour_13to18_rece_min_tot_2_mon_24h_perc = 0
    contact_hour_19to0_rece_min_tot_2_mon_24h_perc = 0

    contact_hour_1to6_rece_cnt_1_mon_24h_perc = 0
    contact_hour_7to12_rece_cnt_1_mon_24h_perc = 0
    contact_hour_13to18_rece_cnt_1_mon_24h_perc = 0
    contact_hour_19to0_rece_cnt_1_mon_24h_perc = 0

    contact_hour_1to6_rece_min_tot_1_mon_24h_perc = 0
    contact_hour_7to12_rece_min_tot_1_mon_24h_perc = 0
    contact_hour_13to18_rece_min_tot_1_mon_24h_perc = 0
    contact_hour_19to0_rece_min_tot_1_mon_24h_perc = 0

    contact_hour_1to6_rece_cnt_2_wk_24h_perc = 0
    contact_hour_7to12_rece_cnt_2_wk_24h_perc = 0
    contact_hour_13to18_rece_cnt_2_wk_24h_perc = 0
    contact_hour_19to0_rece_cnt_2_wk_24h_perc = 0

    contact_hour_1to6_rece_min_tot_2_wk_24h_perc = 0
    contact_hour_7to12_rece_min_tot_2_wk_24h_perc = 0
    contact_hour_13to18_rece_min_tot_2_wk_24h_perc = 0
    contact_hour_19to0_rece_min_tot_2_wk_24h_perc = 0

    contact_hour_1to8_rece_cnt_24h_perc = 0
    contact_hour_9to16_rece_cnt_24h_perc = 0
    contact_hour_17to0_rece_cnt_24h_perc = 0

    contact_hour_1to8_rece_min_tot_24h_perc = 0
    contact_hour_9to16_rece_min_tot_24h_perc = 0
    contact_hour_17to0_rece_min_tot_24h_perc = 0

    contact_hour_1to8_rece_cnt_6_mon_24h_perc = 0
    contact_hour_9to16_rece_cnt_6_mon_24h_perc = 0
    contact_hour_17to0_rece_cnt_6_mon_24h_perc = 0

    contact_hour_1to8_rece_min_tot_6_mon_24h_perc = 0
    contact_hour_9to16_rece_min_tot_6_mon_24h_perc = 0
    contact_hour_17to0_rece_min_tot_6_mon_24h_perc = 0

    contact_hour_1to8_rece_cnt_3_mon_24h_perc = 0
    contact_hour_9to16_rece_cnt_3_mon_24h_perc = 0
    contact_hour_17to0_rece_cnt_3_mon_24h_perc = 0

    contact_hour_1to8_rece_min_tot_3_mon_24h_perc = 0
    contact_hour_9to16_rece_min_tot_3_mon_24h_perc = 0
    contact_hour_17to0_rece_min_tot_3_mon_24h_perc = 0

    contact_hour_1to8_rece_cnt_2_mon_24h_perc = 0
    contact_hour_9to16_rece_cnt_2_mon_24h_perc = 0
    contact_hour_17to0_rece_cnt_2_mon_24h_perc = 0

    contact_hour_1to8_rece_min_tot_2_mon_24h_perc = 0
    contact_hour_9to16_rece_min_tot_2_mon_24h_perc = 0
    contact_hour_17to0_rece_min_tot_2_mon_24h_perc = 0

    contact_hour_1to8_rece_cnt_1_mon_24h_perc = 0
    contact_hour_9to16_rece_cnt_1_mon_24h_perc = 0
    contact_hour_17to0_rece_cnt_1_mon_24h_perc = 0

    contact_hour_1to8_rece_min_tot_1_mon_24h_perc = 0
    contact_hour_9to16_rece_min_tot_1_mon_24h_perc = 0
    contact_hour_17to0_rece_min_tot_1_mon_24h_perc = 0

    contact_hour_1to8_rece_cnt_2_wk_24h_perc = 0
    contact_hour_9to16_rece_cnt_2_wk_24h_perc = 0
    contact_hour_17to0_rece_cnt_2_wk_24h_perc = 0

    contact_hour_1to8_rece_min_tot_2_wk_24h_perc = 0
    contact_hour_9to16_rece_min_tot_2_wk_24h_perc = 0
    contact_hour_17to0_rece_min_tot_2_wk_24h_perc = 0

    contact_hour_9to20_rece_cnt_24_hour_perc = 0
    contact_hour_21to8_rece_cnt_24_hour_perc = 0

    contact_hour_9to20_rece_min_tot_24_hour_perc = 0
    contact_hour_21to8_rece_min_tot_24_hour_perc = 0

    contact_hour_9to20_rece_cnt_6_mon_24_hour_perc = 0
    contact_hour_21to8_rece_cnt_6_mon_24_hour_perc = 0

    contact_hour_9to20_rece_min_tot_6_mon_24_hour_perc = 0
    contact_hour_21to8_rece_min_tot_6_mon_24_hour_perc = 0

    contact_hour_9to20_rece_cnt_3_mon_24_hour_perc = 0
    contact_hour_21to8_rece_cnt_3_mon_24_hour_perc = 0

    contact_hour_9to20_rece_min_tot_3_mon_24_hour_perc = 0
    contact_hour_21to8_rece_min_tot_3_mon_24_hour_perc = 0

    contact_hour_9to20_rece_cnt_2_mon_24_hour_perc = 0
    contact_hour_21to8_rece_cnt_2_mon_24_hour_perc = 0

    contact_hour_9to20_rece_min_tot_2_mon_24_hour_perc = 0
    contact_hour_21to8_rece_min_tot_2_mon_24_hour_perc = 0

    contact_hour_9to20_rece_cnt_2_wk_24_hour_perc = 0
    contact_hour_21to8_rece_cnt_2_wk_24_hour_perc = 0

    contact_hour_9to20_rece_min_tot_2_wk_24_hour_perc = 0
    contact_hour_21to8_rece_min_tot_2_wk_24_hour_perc = 0

    # 6 mon perc
    contact_hour_1to6_cnt_3_mon_perc = 0
    contact_hour_7to12_cnt_3_mon_perc = 0
    contact_hour_13to18_cnt_3_mon_perc = 0
    contact_hour_19to0_cnt_3_mon_perc = 0

    contact_hour_1to6_min_tot_3_mon_perc = 0
    contact_hour_7to12_min_tot_3_mon_perc = 0
    contact_hour_13to18_min_tot_3_mon_perc = 0
    contact_hour_19to0_min_tot_3_mon_perc = 0

    contact_hour_1to6_cnt_2_mon_perc = 0
    contact_hour_7to12_cnt_2_mon_perc = 0
    contact_hour_13to18_cnt_2_mon_perc = 0
    contact_hour_19to0_cnt_2_mon_perc = 0

    contact_hour_1to6_min_tot_2_mon_perc = 0
    contact_hour_7to12_min_tot_2_mon_perc = 0
    contact_hour_13to18_min_tot_2_mon_perc = 0
    contact_hour_19to0_min_tot_2_mon_perc = 0

    contact_hour_1to6_cnt_1_mon_perc = 0
    contact_hour_7to12_cnt_1_mon_perc = 0
    contact_hour_13to18_cnt_1_mon_perc = 0
    contact_hour_19to0_cnt_1_mon_perc = 0

    contact_hour_1to6_min_tot_1_mon_perc = 0
    contact_hour_7to12_min_tot_1_mon_perc = 0
    contact_hour_13to18_min_tot_1_mon_perc = 0
    contact_hour_19to0_min_tot_1_mon_perc = 0

    contact_hour_1to6_cnt_2_wk_perc = 0
    contact_hour_7to12_cnt_2_wk_perc = 0
    contact_hour_13to18_cnt_2_wk_perc = 0
    contact_hour_19to0_cnt_2_wk_perc = 0

    contact_hour_1to6_min_tot_2_wk_perc = 0
    contact_hour_7to12_min_tot_2_wk_perc = 0
    contact_hour_13to18_min_tot_2_wk_perc = 0
    contact_hour_19to0_min_tot_2_wk_perc = 0

    contact_hour_1to8_cnt_3_mon_perc = 0
    contact_hour_9to16_cnt_3_mon_perc = 0
    contact_hour_17to0_cnt_3_mon_perc = 0

    contact_hour_1to8_min_tot_3_mon_perc = 0
    contact_hour_9to16_min_tot_3_mon_perc = 0
    contact_hour_17to0_min_tot_3_mon_perc = 0

    contact_hour_1to8_cnt_2_mon_perc = 0
    contact_hour_9to16_cnt_2_mon_perc = 0
    contact_hour_17to0_cnt_2_mon_perc = 0

    contact_hour_1to8_min_tot_2_mon_perc = 0
    contact_hour_9to16_min_tot_2_mon_perc = 0
    contact_hour_17to0_min_tot_2_mon_perc = 0

    contact_hour_1to8_cnt_1_mon_perc = 0
    contact_hour_9to16_cnt_1_mon_perc = 0
    contact_hour_17to0_cnt_1_mon_perc = 0

    contact_hour_1to8_min_tot_1_mon_perc = 0
    contact_hour_9to16_min_tot_1_mon_perc = 0
    contact_hour_17to0_min_tot_1_mon_perc = 0

    contact_hour_1to8_cnt_2_wk_perc = 0
    contact_hour_9to16_cnt_2_wk_perc = 0
    contact_hour_17to0_cnt_2_wk_perc = 0

    contact_hour_1to8_min_tot_2_wk_perc = 0
    contact_hour_9to16_min_tot_2_wk_perc = 0
    contact_hour_17to0_min_tot_2_wk_perc = 0

    contact_hour_9to20_cnt_3_mon_perc = 0
    contact_hour_21to8_cnt_3_mon_perc = 0

    contact_hour_9to20_min_tot_3_mon_perc = 0
    contact_hour_21to8_min_tot_3_mon_perc = 0

    contact_hour_9to20_cnt_2_mon_perc = 0
    contact_hour_21to8_cnt_2_mon_perc = 0

    contact_hour_9to20_min_tot_2_mon_perc = 0
    contact_hour_21to8_min_tot_2_mon_perc = 0

    contact_hour_9to20_cnt_1_mon_perc = 0
    contact_hour_21to8_cnt_1_mon_perc = 0

    contact_hour_9to20_min_tot_1_mon_perc = 0
    contact_hour_21to8_min_tot_1_mon_perc = 0

    contact_hour_9to20_cnt_2_wk_perc = 0
    contact_hour_21to8_cnt_2_wk_perc = 0

    contact_hour_9to20_min_tot_2_wk_perc = 0
    contact_hour_21to8_min_tot_2_wk_perc = 0

    contact_hour_1to6_call_cnt_3_mon_perc = 0
    contact_hour_7to12_call_cnt_3_mon_perc = 0
    contact_hour_13to18_call_cnt_3_mon_perc = 0
    contact_hour_19to0_call_cnt_3_mon_perc = 0

    contact_hour_1to6_call_min_tot_3_mon_perc = 0
    contact_hour_7to12_call_min_tot_3_mon_perc = 0
    contact_hour_13to18_call_min_tot_3_mon_perc = 0
    contact_hour_19to0_call_min_tot_3_mon_perc = 0

    contact_hour_1to6_call_cnt_2_mon_perc = 0
    contact_hour_7to12_call_cnt_2_mon_perc = 0
    contact_hour_13to18_call_cnt_2_mon_perc = 0
    contact_hour_19to0_call_cnt_2_mon_perc = 0

    contact_hour_1to6_call_min_tot_2_mon_perc = 0
    contact_hour_7to12_call_min_tot_2_mon_perc = 0
    contact_hour_13to18_call_min_tot_2_mon_perc = 0
    contact_hour_19to0_call_min_tot_2_mon_perc = 0

    contact_hour_1to6_call_cnt_1_mon_perc = 0
    contact_hour_7to12_call_cnt_1_mon_perc = 0
    contact_hour_13to18_call_cnt_1_mon_perc = 0
    contact_hour_19to0_call_cnt_1_mon_perc = 0

    contact_hour_1to6_call_min_tot_1_mon_perc = 0
    contact_hour_7to12_call_min_tot_1_mon_perc = 0
    contact_hour_13to18_call_min_tot_1_mon_perc = 0
    contact_hour_19to0_call_min_tot_1_mon_perc = 0

    contact_hour_1to6_call_cnt_2_wk_perc = 0
    contact_hour_7to12_call_cnt_2_wk_perc = 0
    contact_hour_13to18_call_cnt_2_wk_perc = 0
    contact_hour_19to0_call_cnt_2_wk_perc = 0

    contact_hour_1to6_call_min_tot_2_wk_perc = 0
    contact_hour_7to12_call_min_tot_2_wk_perc = 0
    contact_hour_13to18_call_min_tot_2_wk_perc = 0
    contact_hour_19to0_call_min_tot_2_wk_perc = 0

    contact_hour_1to8_call_cnt_3_mon_perc = 0
    contact_hour_9to16_call_cnt_3_mon_perc = 0
    contact_hour_17to0_call_cnt_3_mon_perc = 0

    contact_hour_1to8_call_min_tot_3_mon_perc = 0
    contact_hour_9to16_call_min_tot_3_mon_perc = 0
    contact_hour_17to0_call_min_tot_3_mon_perc = 0

    contact_hour_1to8_call_cnt_2_mon_perc = 0
    contact_hour_9to16_call_cnt_2_mon_perc = 0
    contact_hour_17to0_call_cnt_2_mon_perc = 0

    contact_hour_1to8_call_min_tot_2_mon_perc = 0
    contact_hour_9to16_call_min_tot_2_mon_perc = 0
    contact_hour_17to0_call_min_tot_2_mon_perc = 0

    contact_hour_1to8_call_cnt_1_mon_perc = 0
    contact_hour_9to16_call_cnt_1_mon_perc = 0
    contact_hour_17to0_call_cnt_1_mon_perc = 0

    contact_hour_1to8_call_min_tot_1_mon_perc = 0
    contact_hour_9to16_call_min_tot_1_mon_perc = 0
    contact_hour_17to0_call_min_tot_1_mon_perc = 0

    contact_hour_1to8_call_cnt_2_wk_perc = 0
    contact_hour_9to16_call_cnt_2_wk_perc = 0
    contact_hour_17to0_call_cnt_2_wk_perc = 0

    contact_hour_1to8_call_min_tot_2_wk_perc = 0
    contact_hour_9to16_call_min_tot_2_wk_perc = 0
    contact_hour_17to0_call_min_tot_2_wk_perc = 0

    contact_hour_9to20_call_cnt_3_mon_perc = 0
    contact_hour_21to8_call_cnt_3_mon_perc = 0

    contact_hour_9to20_call_min_tot_3_mon_perc = 0
    contact_hour_21to8_call_min_tot_3_mon_perc = 0

    contact_hour_9to20_call_cnt_2_mon_perc = 0
    contact_hour_21to8_call_cnt_2_mon_perc = 0

    contact_hour_9to20_call_min_tot_2_mon_perc = 0
    contact_hour_21to8_call_min_tot_2_mon_perc = 0

    contact_hour_9to20_call_cnt_1_mon_perc = 0
    contact_hour_21to8_call_cnt_1_mon_perc = 0

    contact_hour_9to20_call_min_tot_1_mon_perc = 0
    contact_hour_21to8_call_min_tot_1_mon_perc = 0

    contact_hour_9to20_call_cnt_2_wk_perc = 0
    contact_hour_21to8_call_cnt_2_wk_perc = 0

    contact_hour_9to20_call_min_tot_2_wk_perc = 0
    contact_hour_21to8_call_min_tot_2_wk_perc = 0

    contact_hour_1to6_rece_cnt_3_mon_perc = 0
    contact_hour_7to12_rece_cnt_3_mon_perc = 0
    contact_hour_13to18_rece_cnt_3_mon_perc = 0
    contact_hour_19to0_rece_cnt_3_mon_perc = 0

    contact_hour_1to6_rece_min_tot_3_mon_perc = 0
    contact_hour_7to12_rece_min_tot_3_mon_perc = 0
    contact_hour_13to18_rece_min_tot_3_mon_perc = 0
    contact_hour_19to0_rece_min_tot_3_mon_perc = 0

    contact_hour_1to6_rece_cnt_2_mon_perc = 0
    contact_hour_7to12_rece_cnt_2_mon_perc = 0
    contact_hour_13to18_rece_cnt_2_mon_perc = 0
    contact_hour_19to0_rece_cnt_2_mon_perc = 0

    contact_hour_1to6_rece_min_tot_2_mon_perc = 0
    contact_hour_7to12_rece_min_tot_2_mon_perc = 0
    contact_hour_13to18_rece_min_tot_2_mon_perc = 0
    contact_hour_19to0_rece_min_tot_2_mon_perc = 0

    contact_hour_1to6_rece_cnt_1_mon_perc = 0
    contact_hour_7to12_rece_cnt_1_mon_perc = 0
    contact_hour_13to18_rece_cnt_1_mon_perc = 0
    contact_hour_19to0_rece_cnt_1_mon_perc = 0

    contact_hour_1to6_rece_min_tot_1_mon_perc = 0
    contact_hour_7to12_rece_min_tot_1_mon_perc = 0
    contact_hour_13to18_rece_min_tot_1_mon_perc = 0
    contact_hour_19to0_rece_min_tot_1_mon_perc = 0

    contact_hour_1to6_rece_cnt_2_wk_perc = 0
    contact_hour_7to12_rece_cnt_2_wk_perc = 0
    contact_hour_13to18_rece_cnt_2_wk_perc = 0
    contact_hour_19to0_rece_cnt_2_wk_perc = 0

    contact_hour_1to6_rece_min_tot_2_wk_perc = 0
    contact_hour_7to12_rece_min_tot_2_wk_perc = 0
    contact_hour_13to18_rece_min_tot_2_wk_perc = 0
    contact_hour_19to0_rece_min_tot_2_wk_perc = 0

    contact_hour_1to8_rece_cnt_3_mon_perc = 0
    contact_hour_9to16_rece_cnt_3_mon_perc = 0
    contact_hour_17to0_rece_cnt_3_mon_perc = 0

    contact_hour_1to8_rece_min_tot_3_mon_perc = 0
    contact_hour_9to16_rece_min_tot_3_mon_perc = 0
    contact_hour_17to0_rece_min_tot_3_mon_perc = 0

    contact_hour_1to8_rece_cnt_2_mon_perc = 0
    contact_hour_9to16_rece_cnt_2_mon_perc = 0
    contact_hour_17to0_rece_cnt_2_mon_perc = 0

    contact_hour_1to8_rece_min_tot_2_mon_perc = 0
    contact_hour_9to16_rece_min_tot_2_mon_perc = 0
    contact_hour_17to0_rece_min_tot_2_mon_perc = 0

    contact_hour_1to8_rece_cnt_1_mon_perc = 0
    contact_hour_9to16_rece_cnt_1_mon_perc = 0
    contact_hour_17to0_rece_cnt_1_mon_perc = 0

    contact_hour_1to8_rece_min_tot_1_mon_perc = 0
    contact_hour_9to16_rece_min_tot_1_mon_perc = 0
    contact_hour_17to0_rece_min_tot_1_mon_perc = 0

    contact_hour_1to8_rece_cnt_2_wk_perc = 0
    contact_hour_9to16_rece_cnt_2_wk_perc = 0
    contact_hour_17to0_rece_cnt_2_wk_perc = 0

    contact_hour_1to8_rece_min_tot_2_wk_perc = 0
    contact_hour_9to16_rece_min_tot_2_wk_perc = 0
    contact_hour_17to0_rece_min_tot_2_wk_perc = 0

    contact_hour_9to20_rece_cnt_3_mon_perc = 0
    contact_hour_21to8_rece_cnt_3_mon_perc = 0

    contact_hour_9to20_rece_min_tot_3_mon_perc = 0
    contact_hour_21to8_rece_min_tot_3_mon_perc = 0

    contact_hour_9to20_rece_cnt_2_mon_perc = 0
    contact_hour_21to8_rece_cnt_2_mon_perc = 0

    contact_hour_9to20_rece_min_tot_2_mon_perc = 0
    contact_hour_21to8_rece_min_tot_2_mon_perc = 0

    contact_hour_9to20_rece_cnt_1_mon_perc = 0
    contact_hour_21to8_rece_cnt_1_mon_perc = 0

    contact_hour_9to20_rece_min_tot_1_mon_perc = 0
    contact_hour_21to8_rece_min_tot_1_mon_perc = 0

    contact_hour_9to20_rece_cnt_2_wk_perc = 0
    contact_hour_21to8_rece_cnt_2_wk_perc = 0

    contact_hour_9to20_rece_min_tot_2_wk_perc = 0
    contact_hour_21to8_rece_min_tot_2_wk_perc = 0

    # call inout perc
    contact_hour_1to6_call_cnt_inout_perc = 0
    contact_hour_7to12_call_cnt_inout_perc = 0
    contact_hour_13to18_call_cnt_inout_perc = 0
    contact_hour_19to0_call_cnt_inout_perc = 0

    contact_hour_1to6_call_min_tot_inout_perc = 0
    contact_hour_7to12_call_min_tot_inout_perc = 0
    contact_hour_13to18_call_min_tot_inout_perc = 0
    contact_hour_19to0_call_min_tot_inout_perc = 0

    contact_hour_1to6_call_cnt_6_mon_inout_perc = 0
    contact_hour_7to12_call_cnt_6_mon_inout_perc = 0
    contact_hour_13to18_call_cnt_6_mon_inout_perc = 0
    contact_hour_19to0_call_cnt_6_mon_inout_perc = 0

    contact_hour_1to6_call_min_tot_6_mon_inout_perc = 0
    contact_hour_7to12_call_min_tot_6_mon_inout_perc = 0
    contact_hour_13to18_call_min_tot_6_mon_inout_perc = 0
    contact_hour_19to0_call_min_tot_6_mon_inout_perc = 0

    contact_hour_1to6_call_cnt_3_mon_inout_perc = 0
    contact_hour_7to12_call_cnt_3_mon_inout_perc = 0
    contact_hour_13to18_call_cnt_3_mon_inout_perc = 0
    contact_hour_19to0_call_cnt_3_mon_inout_perc = 0

    contact_hour_1to6_call_min_tot_3_mon_inout_perc = 0
    contact_hour_7to12_call_min_tot_3_mon_inout_perc = 0
    contact_hour_13to18_call_min_tot_3_mon_inout_perc = 0
    contact_hour_19to0_call_min_tot_3_mon_inout_perc = 0

    contact_hour_1to6_call_cnt_2_mon_inout_perc = 0
    contact_hour_7to12_call_cnt_2_mon_inout_perc = 0
    contact_hour_13to18_call_cnt_2_mon_inout_perc = 0
    contact_hour_19to0_call_cnt_2_mon_inout_perc = 0

    contact_hour_1to6_call_min_tot_2_mon_inout_perc = 0
    contact_hour_7to12_call_min_tot_2_mon_inout_perc = 0
    contact_hour_13to18_call_min_tot_2_mon_inout_perc = 0
    contact_hour_19to0_call_min_tot_2_mon_inout_perc = 0

    contact_hour_1to6_call_cnt_1_mon_inout_perc = 0
    contact_hour_7to12_call_cnt_1_mon_inout_perc = 0
    contact_hour_13to18_call_cnt_1_mon_inout_perc = 0
    contact_hour_19to0_call_cnt_1_mon_inout_perc = 0

    contact_hour_1to6_call_min_tot_1_mon_inout_perc = 0
    contact_hour_7to12_call_min_tot_1_mon_inout_perc = 0
    contact_hour_13to18_call_min_tot_1_mon_inout_perc = 0
    contact_hour_19to0_call_min_tot_1_mon_inout_perc = 0

    contact_hour_1to6_call_cnt_2_wk_inout_perc = 0
    contact_hour_7to12_call_cnt_2_wk_inout_perc = 0
    contact_hour_13to18_call_cnt_2_wk_inout_perc = 0
    contact_hour_19to0_call_cnt_2_wk_inout_perc = 0

    contact_hour_1to6_call_min_tot_2_wk_inout_perc = 0
    contact_hour_7to12_call_min_tot_2_wk_inout_perc = 0
    contact_hour_13to18_call_min_tot_2_wk_inout_perc = 0
    contact_hour_19to0_call_min_tot_2_wk_inout_perc = 0

    contact_hour_1to8_call_cnt_inout_perc = 0
    contact_hour_9to16_call_cnt_inout_perc = 0
    contact_hour_17to0_call_cnt_inout_perc = 0

    contact_hour_1to8_call_min_tot_inout_perc = 0
    contact_hour_9to16_call_min_tot_inout_perc = 0
    contact_hour_17to0_call_min_tot_inout_perc = 0

    contact_hour_1to8_call_cnt_6_mon_inout_perc = 0
    contact_hour_9to16_call_cnt_6_mon_inout_perc = 0
    contact_hour_17to0_call_cnt_6_mon_inout_perc = 0

    contact_hour_1to8_call_min_tot_6_mon_inout_perc = 0
    contact_hour_9to16_call_min_tot_6_mon_inout_perc = 0
    contact_hour_17to0_call_min_tot_6_mon_inout_perc = 0

    contact_hour_1to8_call_cnt_3_mon_inout_perc = 0
    contact_hour_9to16_call_cnt_3_mon_inout_perc = 0
    contact_hour_17to0_call_cnt_3_mon_inout_perc = 0

    contact_hour_1to8_call_min_tot_3_mon_inout_perc = 0
    contact_hour_9to16_call_min_tot_3_mon_inout_perc = 0
    contact_hour_17to0_call_min_tot_3_mon_inout_perc = 0

    contact_hour_1to8_call_cnt_2_mon_inout_perc = 0
    contact_hour_9to16_call_cnt_2_mon_inout_perc = 0
    contact_hour_17to0_call_cnt_2_mon_inout_perc = 0

    contact_hour_1to8_call_min_tot_2_mon_inout_perc = 0
    contact_hour_9to16_call_min_tot_2_mon_inout_perc = 0
    contact_hour_17to0_call_min_tot_2_mon_inout_perc = 0

    contact_hour_1to8_call_cnt_1_mon_inout_perc = 0
    contact_hour_9to16_call_cnt_1_mon_inout_perc = 0
    contact_hour_17to0_call_cnt_1_mon_inout_perc = 0

    contact_hour_1to8_call_min_tot_1_mon_inout_perc = 0
    contact_hour_9to16_call_min_tot_1_mon_inout_perc = 0
    contact_hour_17to0_call_min_tot_1_mon_inout_perc = 0

    contact_hour_1to8_call_cnt_2_wk_inout_perc = 0
    contact_hour_9to16_call_cnt_2_wk_inout_perc = 0
    contact_hour_17to0_call_cnt_2_wk_inout_perc = 0

    contact_hour_1to8_call_min_tot_2_wk_inout_perc = 0
    contact_hour_9to16_call_min_tot_2_wk_inout_perc = 0
    contact_hour_17to0_call_min_tot_2_wk_inout_perc = 0

    contact_hour_9to20_call_cnt_inout_perc = 0
    contact_hour_21to8_call_cnt_inout_perc = 0

    contact_hour_9to20_call_min_tot_inout_perc = 0
    contact_hour_21to8_call_min_tot_inout_perc = 0

    contact_hour_9to20_call_cnt_6_mon_inout_perc = 0
    contact_hour_21to8_call_cnt_6_mon_inout_perc = 0

    contact_hour_9to20_call_min_tot_6_mon_inout_perc = 0
    contact_hour_21to8_call_min_tot_6_mon_inout_perc = 0

    contact_hour_9to20_call_cnt_3_mon_inout_perc = 0
    contact_hour_21to8_call_cnt_3_mon_inout_perc = 0

    contact_hour_9to20_call_min_tot_3_mon_inout_perc = 0
    contact_hour_21to8_call_min_tot_3_mon_inout_perc = 0

    contact_hour_9to20_call_cnt_2_mon_inout_perc = 0
    contact_hour_21to8_call_cnt_2_mon_inout_perc = 0

    contact_hour_9to20_call_min_tot_2_mon_inout_perc = 0
    contact_hour_21to8_call_min_tot_2_mon_inout_perc = 0

    contact_hour_9to20_call_cnt_1_mon_inout_perc = 0
    contact_hour_21to8_call_cnt_1_mon_inout_perc = 0

    contact_hour_9to20_call_min_tot_1_mon_inout_perc = 0
    contact_hour_21to8_call_min_tot_1_mon_inout_perc = 0

    contact_hour_9to20_call_cnt_2_wk_inout_perc = 0
    contact_hour_21to8_call_cnt_2_wk_inout_perc = 0

    contact_hour_9to20_call_min_tot_2_wk_inout_perc = 0
    contact_hour_21to8_call_min_tot_2_wk_inout_perc = 0

    # contact weekday and weekend avg
    contact_weekday_min_avg = 0
    contact_weekday_min_avg_6_mon = 0
    contact_weekday_min_avg_3_mon = 0
    contact_weekday_min_avg_2_mon = 0
    contact_weekday_min_avg_1_mon = 0
    contact_weekday_min_avg_2_wk = 0

    contact_weekend_min_avg = 0
    contact_weekend_min_avg_6_mon = 0
    contact_weekend_min_avg_3_mon = 0
    contact_weekend_min_avg_2_mon = 0
    contact_weekend_min_avg_1_mon = 0
    contact_weekend_min_avg_2_wk = 0

    contact_weekday_call_min_avg = 0
    contact_weekday_call_min_avg_6_mon = 0
    contact_weekday_call_min_avg_3_mon = 0
    contact_weekday_call_min_avg_2_mon = 0
    contact_weekday_call_min_avg_1_mon = 0
    contact_weekday_call_min_avg_2_wk = 0

    contact_weekend_call_min_avg = 0
    contact_weekend_call_min_avg_6_mon = 0
    contact_weekend_call_min_avg_3_mon = 0
    contact_weekend_call_min_avg_2_mon = 0
    contact_weekend_call_min_avg_1_mon = 0
    contact_weekend_call_min_avg_2_wk = 0

    contact_weekday_rece_min_avg = 0
    contact_weekday_rece_min_avg_6_mon = 0
    contact_weekday_rece_min_avg_3_mon = 0
    contact_weekday_rece_min_avg_2_mon = 0
    contact_weekday_rece_min_avg_1_mon = 0
    contact_weekday_rece_min_avg_2_wk = 0

    contact_weekend_rece_min_avg = 0
    contact_weekend_rece_min_avg_6_mon = 0
    contact_weekend_rece_min_avg_3_mon = 0
    contact_weekend_rece_min_avg_2_mon = 0
    contact_weekend_rece_min_avg_1_mon = 0
    contact_weekend_rece_min_avg_2_wk = 0

    # contact weekday and weekend 6 mon perc
    contact_weekday_cnt_3_mon_perc = 0
    contact_weekday_min_tot_3_mon_perc = 0
    contact_weekday_call_cnt_3_mon_perc = 0
    contact_weekday_rece_cnt_3_mon_perc = 0
    contact_weekday_call_min_tot_3_mon_perc = 0
    contact_weekday_rece_min_tot_3_mon_perc = 0

    contact_weekday_cnt_2_mon_perc = 0
    contact_weekday_min_tot_2_mon_perc = 0
    contact_weekday_call_cnt_2_mon_perc = 0
    contact_weekday_rece_cnt_2_mon_perc = 0
    contact_weekday_call_min_tot_2_mon_perc = 0
    contact_weekday_rece_min_tot_2_mon_perc = 0

    contact_weekday_cnt_1_mon_perc = 0
    contact_weekday_min_tot_1_mon_perc = 0
    contact_weekday_call_cnt_1_mon_perc = 0
    contact_weekday_rece_cnt_1_mon_perc = 0
    contact_weekday_call_min_tot_1_mon_perc = 0
    contact_weekday_rece_min_tot_1_mon_perc = 0

    contact_weekday_cnt_2_wk_perc = 0
    contact_weekday_min_tot_2_wk_perc = 0
    contact_weekday_call_cnt_2_wk_perc = 0
    contact_weekday_rece_cnt_2_wk_perc = 0
    contact_weekday_call_min_tot_2_wk_perc = 0
    contact_weekday_rece_min_tot_2_wk_perc = 0

    contact_weekend_cnt_3_mon_perc = 0
    contact_weekend_min_tot_3_mon_perc = 0
    contact_weekend_call_cnt_3_mon_perc = 0
    contact_weekend_rece_cnt_3_mon_perc = 0
    contact_weekend_call_min_tot_3_mon_perc = 0
    contact_weekend_rece_min_tot_3_mon_perc = 0

    contact_weekend_cnt_2_mon_perc = 0
    contact_weekend_min_tot_2_mon_perc = 0
    contact_weekend_call_cnt_2_mon_perc = 0
    contact_weekend_rece_cnt_2_mon_perc = 0
    contact_weekend_call_min_tot_2_mon_perc = 0
    contact_weekend_rece_min_tot_2_mon_perc = 0

    contact_weekend_cnt_1_mon_perc = 0
    contact_weekend_min_tot_1_mon_perc = 0
    contact_weekend_call_cnt_1_mon_perc = 0
    contact_weekend_rece_cnt_1_mon_perc = 0
    contact_weekend_call_min_tot_1_mon_perc = 0
    contact_weekend_rece_min_tot_1_mon_perc = 0

    contact_weekend_cnt_2_wk_perc = 0
    contact_weekend_min_tot_2_wk_perc = 0
    contact_weekend_call_cnt_2_wk_perc = 0
    contact_weekend_rece_cnt_2_wk_perc = 0
    contact_weekend_call_min_tot_2_wk_perc = 0
    contact_weekend_rece_min_tot_2_wk_perc = 0

    # weekday week perc
    contact_weekday_cnt_week_perc = 0
    contact_weekday_min_tot_week_perc = 0
    contact_weekday_call_cnt_week_perc = 0
    contact_weekday_rece_cnt_week_perc = 0
    contact_weekday_call_min_tot_week_perc = 0
    contact_weekday_rece_min_tot_week_perc = 0

    contact_weekday_cnt_6_mon_week_perc = 0
    contact_weekday_min_tot_6_mon_week_perc = 0
    contact_weekday_call_cnt_6_mon_week_perc = 0
    contact_weekday_rece_cnt_6_mon_week_perc = 0
    contact_weekday_call_min_tot_6_mon_week_perc = 0
    contact_weekday_rece_min_tot_6_mon_week_perc = 0

    contact_weekday_cnt_3_mon_week_perc = 0
    contact_weekday_min_tot_3_mon_week_perc = 0
    contact_weekday_call_cnt_3_mon_week_perc = 0
    contact_weekday_rece_cnt_3_mon_week_perc = 0
    contact_weekday_call_min_tot_3_mon_week_perc = 0
    contact_weekday_rece_min_tot_3_mon_week_perc = 0

    contact_weekday_cnt_2_mon_week_perc = 0
    contact_weekday_min_tot_2_mon_week_perc = 0
    contact_weekday_call_cnt_2_mon_week_perc = 0
    contact_weekday_rece_cnt_2_mon_week_perc = 0
    contact_weekday_call_min_tot_2_mon_week_perc = 0
    contact_weekday_rece_min_tot_2_mon_week_perc = 0

    contact_weekday_cnt_1_mon_week_perc = 0
    contact_weekday_min_tot_1_mon_week_perc = 0
    contact_weekday_call_cnt_1_mon_week_perc = 0
    contact_weekday_rece_cnt_1_mon_week_perc = 0
    contact_weekday_call_min_tot_1_mon_week_perc = 0
    contact_weekday_rece_min_tot_1_mon_week_perc = 0

    contact_weekday_cnt_2_wk_week_perc = 0
    contact_weekday_min_tot_2_wk_week_perc = 0
    contact_weekday_call_cnt_2_wk_week_perc = 0
    contact_weekday_rece_cnt_2_wk_week_perc = 0
    contact_weekday_call_min_tot_2_wk_week_perc = 0
    contact_weekday_rece_min_tot_2_wk_week_perc = 0

    # duration avg over 15s, 30s, 60s,
    contact_min_over_15s_min_avg = 0
    contact_min_over_15s_call_min_avg = 0
    contact_min_over_15s_rece_min_avg = 0
    contact_min_over_30s_min_avg = 0
    contact_min_over_30s_call_min_avg = 0
    contact_min_over_30s_rece_min_avg = 0
    contact_min_over_60s_min_avg = 0
    contact_min_over_60s_call_min_avg = 0
    contact_min_over_60s_rece_min_avg = 0
    contact_min_over_15s_min_avg_6_mon = 0
    contact_min_over_15s_call_min_avg_6_mon = 0
    contact_min_over_15s_rece_min_avg_6_mon = 0
    contact_min_over_30s_min_avg_6_mon = 0
    contact_min_over_30s_call_min_avg_6_mon = 0
    contact_min_over_30s_rece_min_avg_6_mon = 0
    contact_min_over_60s_min_avg_6_mon = 0
    contact_min_over_60s_call_min_avg_6_mon = 0
    contact_min_over_60s_rece_min_avg_6_mon = 0
    contact_min_over_15s_min_avg_3_mon = 0
    contact_min_over_15s_call_min_avg_3_mon = 0
    contact_min_over_15s_rece_min_avg_3_mon = 0
    contact_min_over_30s_min_avg_3_mon = 0
    contact_min_over_30s_call_min_avg_3_mon = 0
    contact_min_over_30s_rece_min_avg_3_mon = 0
    contact_min_over_60s_min_avg_3_mon = 0
    contact_min_over_60s_call_min_avg_3_mon = 0
    contact_min_over_60s_rece_min_avg_3_mon = 0
    contact_min_over_15s_min_avg_2_mon = 0
    contact_min_over_15s_call_min_avg_2_mon = 0
    contact_min_over_15s_rece_min_avg_2_mon = 0
    contact_min_over_30s_min_avg_2_mon = 0
    contact_min_over_30s_call_min_avg_2_mon = 0
    contact_min_over_30s_rece_min_avg_2_mon = 0
    contact_min_over_60s_min_avg_2_mon = 0
    contact_min_over_60s_call_min_avg_2_mon = 0
    contact_min_over_60s_rece_min_avg_2_mon = 0
    contact_min_over_15s_min_avg_1_mon = 0
    contact_min_over_15s_call_min_avg_1_mon = 0
    contact_min_over_15s_rece_min_avg_1_mon = 0
    contact_min_over_30s_min_avg_1_mon = 0
    contact_min_over_30s_call_min_avg_1_mon = 0
    contact_min_over_30s_rece_min_avg_1_mon = 0
    contact_min_over_60s_min_avg_1_mon = 0
    contact_min_over_60s_call_min_avg_1_mon = 0
    contact_min_over_60s_rece_min_avg_1_mon = 0
    contact_min_over_15s_min_avg_2_wk = 0
    contact_min_over_15s_call_min_avg_2_wk = 0
    contact_min_over_15s_rece_min_avg_2_wk = 0
    contact_min_over_30s_min_avg_2_wk = 0
    contact_min_over_30s_call_min_avg_2_wk = 0
    contact_min_over_30s_rece_min_avg_2_wk = 0
    contact_min_over_60s_min_avg_2_wk = 0
    contact_min_over_60s_call_min_avg_2_wk = 0
    contact_min_over_60s_rece_min_avg_2_wk = 0

    # duration over 15s, 30s, 60s inout perc
    contact_min_over_15s_call_cnt_inout_perc = 0
    contact_min_over_15s_rece_cnt_inout_perc = 0
    contact_min_over_30s_call_cnt_inout_perc = 0
    contact_min_over_30s_rece_cnt_inout_perc = 0
    contact_min_over_60s_call_cnt_inout_perc = 0
    contact_min_over_60s_rece_cnt_inout_perc = 0
    contact_min_over_15s_call_cnt_6_mon_inout_perc = 0
    contact_min_over_15s_rece_cnt_6_mon_inout_perc = 0
    contact_min_over_30s_call_cnt_6_mon_inout_perc = 0
    contact_min_over_30s_rece_cnt_6_mon_inout_perc = 0
    contact_min_over_60s_call_cnt_6_mon_inout_perc = 0
    contact_min_over_60s_rece_cnt_6_mon_inout_perc = 0
    contact_min_over_15s_call_cnt_3_mon_inout_perc = 0
    contact_min_over_15s_rece_cnt_3_mon_inout_perc = 0
    contact_min_over_30s_call_cnt_3_mon_inout_perc = 0
    contact_min_over_30s_rece_cnt_3_mon_inout_perc = 0
    contact_min_over_60s_call_cnt_3_mon_inout_perc = 0
    contact_min_over_60s_rece_cnt_3_mon_inout_perc = 0
    contact_min_over_15s_call_cnt_2_mon_inout_perc = 0
    contact_min_over_15s_rece_cnt_2_mon_inout_perc = 0
    contact_min_over_30s_call_cnt_2_mon_inout_perc = 0
    contact_min_over_30s_rece_cnt_2_mon_inout_perc = 0
    contact_min_over_60s_call_cnt_2_mon_inout_perc = 0
    contact_min_over_60s_rece_cnt_2_mon_inout_perc = 0
    contact_min_over_15s_call_cnt_1_mon_inout_perc = 0
    contact_min_over_15s_rece_cnt_1_mon_inout_perc = 0
    contact_min_over_30s_call_cnt_1_mon_inout_perc = 0
    contact_min_over_30s_rece_cnt_1_mon_inout_perc = 0
    contact_min_over_60s_call_cnt_1_mon_inout_perc = 0
    contact_min_over_60s_rece_cnt_1_mon_inout_perc = 0
    contact_min_over_15s_call_cnt_2_wk_inout_perc = 0
    contact_min_over_15s_rece_cnt_2_wk_inout_perc = 0
    contact_min_over_30s_call_cnt_2_wk_inout_perc = 0
    contact_min_over_30s_rece_cnt_2_wk_inout_perc = 0
    contact_min_over_60s_call_cnt_2_wk_inout_perc = 0
    contact_min_over_60s_rece_cnt_2_wk_inout_perc = 0

    # duration over 15s, 30s, 60s 6 mon perc
    contact_min_over_15s_cnt_3_mon_perc = 0
    contact_min_over_15s_min_tot_3_mon_perc = 0
    contact_min_over_15s_call_cnt_3_mon_perc = 0
    contact_min_over_15s_call_min_tot_3_mon_perc = 0
    contact_min_over_15s_rece_cnt_3_mon_perc = 0
    contact_min_over_15s_rece_min_tot_3_mon_perc = 0

    contact_min_over_30s_cnt_3_mon_perc = 0
    contact_min_over_30s_min_tot_3_mon_perc = 0
    contact_min_over_30s_call_cnt_3_mon_perc = 0
    contact_min_over_30s_call_min_tot_3_mon_perc = 0
    contact_min_over_30s_rece_cnt_3_mon_perc = 0
    contact_min_over_30s_rece_min_tot_3_mon_perc = 0

    contact_min_over_60s_cnt_3_mon_perc = 0
    contact_min_over_60s_min_tot_3_mon_perc = 0
    contact_min_over_60s_call_cnt_3_mon_perc = 0
    contact_min_over_60s_call_min_tot_3_mon_perc = 0
    contact_min_over_60s_rece_cnt_3_mon_perc = 0
    contact_min_over_60s_rece_min_tot_3_mon_perc = 0

    contact_min_over_15s_cnt_2_mon_perc = 0
    contact_min_over_15s_min_tot_2_mon_perc = 0
    contact_min_over_15s_call_cnt_2_mon_perc = 0
    contact_min_over_15s_call_min_tot_2_mon_perc = 0
    contact_min_over_15s_rece_cnt_2_mon_perc = 0
    contact_min_over_15s_rece_min_tot_2_mon_perc = 0

    contact_min_over_30s_cnt_2_mon_perc = 0
    contact_min_over_30s_min_tot_2_mon_perc = 0
    contact_min_over_30s_call_cnt_2_mon_perc = 0
    contact_min_over_30s_call_min_tot_2_mon_perc = 0
    contact_min_over_30s_rece_cnt_2_mon_perc = 0
    contact_min_over_30s_rece_min_tot_2_mon_perc = 0

    contact_min_over_60s_cnt_2_mon_perc = 0
    contact_min_over_60s_min_tot_2_mon_perc = 0
    contact_min_over_60s_call_cnt_2_mon_perc = 0
    contact_min_over_60s_call_min_tot_2_mon_perc = 0
    contact_min_over_60s_rece_cnt_2_mon_perc = 0
    contact_min_over_60s_rece_min_tot_2_mon_perc = 0

    contact_min_over_15s_cnt_1_mon_perc = 0
    contact_min_over_15s_min_tot_1_mon_perc = 0
    contact_min_over_15s_call_cnt_1_mon_perc = 0
    contact_min_over_15s_call_min_tot_1_mon_perc = 0
    contact_min_over_15s_rece_cnt_1_mon_perc = 0
    contact_min_over_15s_rece_min_tot_1_mon_perc = 0

    contact_min_over_30s_cnt_1_mon_perc = 0
    contact_min_over_30s_min_tot_1_mon_perc = 0
    contact_min_over_30s_call_cnt_1_mon_perc = 0
    contact_min_over_30s_call_min_tot_1_mon_perc = 0
    contact_min_over_30s_rece_cnt_1_mon_perc = 0
    contact_min_over_30s_rece_min_tot_1_mon_perc = 0

    contact_min_over_60s_cnt_1_mon_perc = 0
    contact_min_over_60s_min_tot_1_mon_perc = 0
    contact_min_over_60s_call_cnt_1_mon_perc = 0
    contact_min_over_60s_call_min_tot_1_mon_perc = 0
    contact_min_over_60s_rece_cnt_1_mon_perc = 0
    contact_min_over_60s_rece_min_tot_1_mon_perc = 0

    contact_min_over_15s_cnt_2_wk_perc = 0
    contact_min_over_15s_min_tot_2_wk_perc = 0
    contact_min_over_15s_call_cnt_2_wk_perc = 0
    contact_min_over_15s_call_min_tot_2_wk_perc = 0
    contact_min_over_15s_rece_cnt_2_wk_perc = 0
    contact_min_over_15s_rece_min_tot_2_wk_perc = 0

    contact_min_over_30s_cnt_2_wk_perc = 0
    contact_min_over_30s_min_tot_2_wk_perc = 0
    contact_min_over_30s_call_cnt_2_wk_perc = 0
    contact_min_over_30s_call_min_tot_2_wk_perc = 0
    contact_min_over_30s_rece_cnt_2_wk_perc = 0
    contact_min_over_30s_rece_min_tot_2_wk_perc = 0

    contact_min_over_60s_cnt_2_wk_perc = 0
    contact_min_over_60s_min_tot_2_wk_perc = 0
    contact_min_over_60s_call_cnt_2_wk_perc = 0
    contact_min_over_60s_call_min_tot_2_wk_perc = 0
    contact_min_over_60s_rece_cnt_2_wk_perc = 0
    contact_min_over_60s_rece_min_tot_2_wk_perc = 0

    # duration over 15, 30, 60s min perc
    contact_min_over_15s_cnt_min_perc = 0
    contact_min_over_15s_min_tot_min_perc = 0
    contact_min_over_15s_call_cnt_min_perc = 0
    contact_min_over_15s_call_min_tot_min_perc = 0
    contact_min_over_15s_rece_cnt_min_perc = 0
    contact_min_over_15s_rece_min_tot_min_perc = 0

    contact_min_over_30s_cnt_min_perc = 0
    contact_min_over_30s_min_tot_min_perc = 0
    contact_min_over_30s_call_cnt_min_perc = 0
    contact_min_over_30s_call_min_tot_min_perc = 0
    contact_min_over_30s_rece_cnt_min_perc = 0
    contact_min_over_30s_rece_min_tot_min_perc = 0

    contact_min_over_60s_cnt_min_perc = 0
    contact_min_over_60s_min_tot_min_perc = 0
    contact_min_over_60s_call_cnt_min_perc = 0
    contact_min_over_60s_call_min_tot_min_perc = 0
    contact_min_over_60s_rece_cnt_min_perc = 0
    contact_min_over_60s_rece_min_tot_min_perc = 0

    contact_min_over_15s_cnt_6_mon_min_perc = 0
    contact_min_over_15s_min_tot_6_mon_min_perc = 0
    contact_min_over_15s_call_cnt_6_mon_min_perc = 0
    contact_min_over_15s_call_min_tot_6_mon_min_perc = 0
    contact_min_over_15s_rece_cnt_6_mon_min_perc = 0
    contact_min_over_15s_rece_min_tot_6_mon_min_perc = 0

    contact_min_over_30s_cnt_6_mon_min_perc = 0
    contact_min_over_30s_min_tot_6_mon_min_perc = 0
    contact_min_over_30s_call_cnt_6_mon_min_perc = 0
    contact_min_over_30s_call_min_tot_6_mon_min_perc = 0
    contact_min_over_30s_rece_cnt_6_mon_min_perc = 0
    contact_min_over_30s_rece_min_tot_6_mon_min_perc = 0

    contact_min_over_60s_cnt_6_mon_min_perc = 0
    contact_min_over_60s_min_tot_6_mon_min_perc = 0
    contact_min_over_60s_call_cnt_6_mon_min_perc = 0
    contact_min_over_60s_call_min_tot_6_mon_min_perc = 0
    contact_min_over_60s_rece_cnt_6_mon_min_perc = 0
    contact_min_over_60s_rece_min_tot_6_mon_min_perc = 0

    contact_min_over_15s_cnt_3_mon_min_perc = 0
    contact_min_over_15s_min_tot_3_mon_min_perc = 0
    contact_min_over_15s_call_cnt_3_mon_min_perc = 0
    contact_min_over_15s_call_min_tot_3_mon_min_perc = 0
    contact_min_over_15s_rece_cnt_3_mon_min_perc = 0
    contact_min_over_15s_rece_min_tot_3_mon_min_perc = 0

    contact_min_over_30s_cnt_3_mon_min_perc = 0
    contact_min_over_30s_min_tot_3_mon_min_perc = 0
    contact_min_over_30s_call_cnt_3_mon_min_perc = 0
    contact_min_over_30s_call_min_tot_3_mon_min_perc = 0
    contact_min_over_30s_rece_cnt_3_mon_min_perc = 0
    contact_min_over_30s_rece_min_tot_3_mon_min_perc = 0

    contact_min_over_60s_cnt_3_mon_min_perc = 0
    contact_min_over_60s_min_tot_3_mon_min_perc = 0
    contact_min_over_60s_call_cnt_3_mon_min_perc = 0
    contact_min_over_60s_call_min_tot_3_mon_min_perc = 0
    contact_min_over_60s_rece_cnt_3_mon_min_perc = 0
    contact_min_over_60s_rece_min_tot_3_mon_min_perc = 0

    contact_min_over_15s_cnt_2_mon_min_perc = 0
    contact_min_over_15s_min_tot_2_mon_min_perc = 0
    contact_min_over_15s_call_cnt_2_mon_min_perc = 0
    contact_min_over_15s_call_min_tot_2_mon_min_perc = 0
    contact_min_over_15s_rece_cnt_2_mon_min_perc = 0
    contact_min_over_15s_rece_min_tot_2_mon_min_perc = 0

    contact_min_over_30s_cnt_2_mon_min_perc = 0
    contact_min_over_30s_min_tot_2_mon_min_perc = 0
    contact_min_over_30s_call_cnt_2_mon_min_perc = 0
    contact_min_over_30s_call_min_tot_2_mon_min_perc = 0
    contact_min_over_30s_rece_cnt_2_mon_min_perc = 0
    contact_min_over_30s_rece_min_tot_2_mon_min_perc = 0

    contact_min_over_60s_cnt_2_mon_min_perc = 0
    contact_min_over_60s_min_tot_2_mon_min_perc = 0
    contact_min_over_60s_call_cnt_2_mon_min_perc = 0
    contact_min_over_60s_call_min_tot_2_mon_min_perc = 0
    contact_min_over_60s_rece_cnt_2_mon_min_perc = 0
    contact_min_over_60s_rece_min_tot_2_mon_min_perc = 0

    contact_min_over_15s_cnt_1_mon_min_perc = 0
    contact_min_over_15s_min_tot_1_mon_min_perc = 0
    contact_min_over_15s_call_cnt_1_mon_min_perc = 0
    contact_min_over_15s_call_min_tot_1_mon_min_perc = 0
    contact_min_over_15s_rece_cnt_1_mon_min_perc = 0
    contact_min_over_15s_rece_min_tot_1_mon_min_perc = 0

    contact_min_over_30s_cnt_1_mon_min_perc = 0
    contact_min_over_30s_min_tot_1_mon_min_perc = 0
    contact_min_over_30s_call_cnt_1_mon_min_perc = 0
    contact_min_over_30s_call_min_tot_1_mon_min_perc = 0
    contact_min_over_30s_rece_cnt_1_mon_min_perc = 0
    contact_min_over_30s_rece_min_tot_1_mon_min_perc = 0

    contact_min_over_60s_cnt_1_mon_min_perc = 0
    contact_min_over_60s_min_tot_1_mon_min_perc = 0
    contact_min_over_60s_call_cnt_1_mon_min_perc = 0
    contact_min_over_60s_call_min_tot_1_mon_min_perc = 0
    contact_min_over_60s_rece_cnt_1_mon_min_perc = 0
    contact_min_over_60s_rece_min_tot_1_mon_min_perc = 0

    contact_min_over_15s_cnt_2_wk_min_perc = 0
    contact_min_over_15s_min_tot_2_wk_min_perc = 0
    contact_min_over_15s_call_cnt_2_wk_min_perc = 0
    contact_min_over_15s_call_min_tot_2_wk_min_perc = 0
    contact_min_over_15s_rece_cnt_2_wk_min_perc = 0
    contact_min_over_15s_rece_min_tot_2_wk_min_perc = 0

    contact_min_over_30s_cnt_2_wk_min_perc = 0
    contact_min_over_30s_min_tot_2_wk_min_perc = 0
    contact_min_over_30s_call_cnt_2_wk_min_perc = 0
    contact_min_over_30s_call_min_tot_2_wk_min_perc = 0
    contact_min_over_30s_rece_cnt_2_wk_min_perc = 0
    contact_min_over_30s_rece_min_tot_2_wk_min_perc = 0

    contact_min_over_60s_cnt_2_wk_min_perc = 0
    contact_min_over_60s_min_tot_2_wk_min_perc = 0
    contact_min_over_60s_call_cnt_2_wk_min_perc = 0
    contact_min_over_60s_call_min_tot_2_wk_min_perc = 0
    contact_min_over_60s_rece_cnt_2_wk_min_perc = 0
    contact_min_over_60s_rece_min_tot_2_wk_min_perc = 0

    # jxl call record
    # init variables

    if jxl_call_records is not None and jxl_call_records not in ('', 'Null', 'null', 'Null'):
        # 第一次循环开始
        for items in jxl_call_records:
            call_type = items['call_type']
            other_cell_phone = str(items['other_cell_phone'])
            use_time = items['use_time']
            init_type = items['init_type']
            contact_cnt_tot += 1
            contact_min_tot += use_time

            if now_dt == '':
                now_dt = dt.strptime(items['update_time'][:19], '%Y-%m-%d %H:%M:%S')

            try:
                start_time = dt.strptime(items['start_time'], '%Y-%m-%d %H:%M:%S')
            except:
                start_time = now_dt

            spacing_interval = (now_dt - start_time).days

            if start_time.hour == 0:
                contact_hour_0_cnt += 1
                contact_hour_0_min_tot += use_time
            elif start_time.hour == 1:
                contact_hour_1_cnt += 1
                contact_hour_1_min_tot += use_time
            elif start_time.hour == 2:
                contact_hour_2_cnt += 1
                contact_hour_2_min_tot += use_time
            elif start_time.hour == 3:
                contact_hour_3_cnt += 1
                contact_hour_3_min_tot += use_time
            elif start_time.hour == 4:
                contact_hour_4_cnt += 1
                contact_hour_4_min_tot += use_time
            elif start_time.hour == 5:
                contact_hour_5_cnt += 1
                contact_hour_5_min_tot += use_time
            elif start_time.hour == 6:
                contact_hour_6_cnt += 1
                contact_hour_6_min_tot += use_time
            elif start_time.hour == 7:
                contact_hour_7_cnt += 1
                contact_hour_7_min_tot += use_time
            elif start_time.hour == 8:
                contact_hour_8_cnt += 1
                contact_hour_8_min_tot += use_time
            elif start_time.hour == 9:
                contact_hour_9_cnt += 1
                contact_hour_9_min_tot += use_time
            elif start_time.hour == 10:
                contact_hour_10_cnt += 1
                contact_hour_10_min_tot += use_time
            elif start_time.hour == 11:
                contact_hour_11_cnt += 1
                contact_hour_11_min_tot += use_time
            elif start_time.hour == 12:
                contact_hour_12_cnt += 1
                contact_hour_12_min_tot += use_time
            elif start_time.hour == 13:
                contact_hour_13_cnt += 1
                contact_hour_13_min_tot += use_time
            elif start_time.hour == 14:
                contact_hour_14_cnt += 1
                contact_hour_14_min_tot += use_time
            elif start_time.hour == 15:
                contact_hour_15_cnt += 1
                contact_hour_15_min_tot += use_time
            elif start_time.hour == 16:
                contact_hour_16_cnt += 1
                contact_hour_16_min_tot += use_time
            elif start_time.hour == 17:
                contact_hour_17_cnt += 1
                contact_hour_17_min_tot += use_time
            elif start_time.hour == 18:
                contact_hour_18_cnt += 1
                contact_hour_18_min_tot += use_time
            elif start_time.hour == 19:
                contact_hour_19_cnt += 1
                contact_hour_19_min_tot += use_time
            elif start_time.hour == 20:
                contact_hour_20_cnt += 1
                contact_hour_20_min_tot += use_time
            elif start_time.hour == 21:
                contact_hour_21_cnt += 1
                contact_hour_21_min_tot += use_time
            elif start_time.hour == 22:
                contact_hour_22_cnt += 1
                contact_hour_22_min_tot += use_time
            elif start_time.hour == 23:
                contact_hour_23_cnt += 1
                contact_hour_23_min_tot += use_time

            if u'主' in init_type or '主' in init_type:
                if start_time.hour == 0:
                    contact_hour_0_call_cnt += 1
                    contact_hour_0_call_min_tot += use_time
                elif start_time.hour == 1:
                    contact_hour_1_call_cnt += 1
                    contact_hour_1_call_min_tot += use_time
                elif start_time.hour == 2:
                    contact_hour_2_call_cnt += 1
                    contact_hour_2_call_min_tot += use_time
                elif start_time.hour == 3:
                    contact_hour_3_call_cnt += 1
                    contact_hour_3_call_min_tot += use_time
                elif start_time.hour == 4:
                    contact_hour_4_call_cnt += 1
                    contact_hour_4_call_min_tot += use_time
                elif start_time.hour == 5:
                    contact_hour_5_call_cnt += 1
                    contact_hour_5_call_min_tot += use_time
                elif start_time.hour == 6:
                    contact_hour_6_call_cnt += 1
                    contact_hour_6_call_min_tot += use_time
                elif start_time.hour == 7:
                    contact_hour_7_call_cnt += 1
                    contact_hour_7_call_min_tot += use_time
                elif start_time.hour == 8:
                    contact_hour_8_call_cnt += 1
                    contact_hour_8_call_min_tot += use_time
                elif start_time.hour == 9:
                    contact_hour_9_call_cnt += 1
                    contact_hour_9_call_min_tot += use_time
                elif start_time.hour == 10:
                    contact_hour_10_call_cnt += 1
                    contact_hour_10_call_min_tot += use_time
                elif start_time.hour == 11:
                    contact_hour_11_call_cnt += 1
                    contact_hour_11_call_min_tot += use_time
                elif start_time.hour == 12:
                    contact_hour_12_call_cnt += 1
                    contact_hour_12_call_min_tot += use_time
                elif start_time.hour == 13:
                    contact_hour_13_call_cnt += 1
                    contact_hour_13_call_min_tot += use_time
                elif start_time.hour == 14:
                    contact_hour_14_call_cnt += 1
                    contact_hour_14_call_min_tot += use_time
                elif start_time.hour == 15:
                    contact_hour_15_call_cnt += 1
                    contact_hour_15_call_min_tot += use_time
                elif start_time.hour == 16:
                    contact_hour_16_call_cnt += 1
                    contact_hour_16_call_min_tot += use_time
                elif start_time.hour == 17:
                    contact_hour_17_call_cnt += 1
                    contact_hour_17_call_min_tot += use_time
                elif start_time.hour == 18:
                    contact_hour_18_call_cnt += 1
                    contact_hour_18_call_min_tot += use_time
                elif start_time.hour == 19:
                    contact_hour_19_call_cnt += 1
                    contact_hour_19_call_min_tot += use_time
                elif start_time.hour == 20:
                    contact_hour_20_call_cnt += 1
                    contact_hour_20_call_min_tot += use_time
                elif start_time.hour == 21:
                    contact_hour_21_call_cnt += 1
                    contact_hour_21_call_min_tot += use_time
                elif start_time.hour == 22:
                    contact_hour_22_call_cnt += 1
                    contact_hour_22_call_min_tot += use_time
                elif start_time.hour == 23:
                    contact_hour_23_call_cnt += 1
                    contact_hour_23_call_min_tot += use_time
            elif u'被' in init_type or '被' in init_type:
                if start_time.hour == 0:
                    contact_hour_0_rece_cnt += 1
                    contact_hour_0_rece_min_tot += use_time
                elif start_time.hour == 1:
                    contact_hour_1_rece_cnt += 1
                    contact_hour_1_rece_min_tot += use_time
                elif start_time.hour == 2:
                    contact_hour_2_rece_cnt += 1
                    contact_hour_2_rece_min_tot += use_time
                elif start_time.hour == 3:
                    contact_hour_3_rece_cnt += 1
                    contact_hour_3_rece_min_tot += use_time
                elif start_time.hour == 4:
                    contact_hour_4_rece_cnt += 1
                    contact_hour_4_rece_min_tot += use_time
                elif start_time.hour == 5:
                    contact_hour_5_rece_cnt += 1
                    contact_hour_5_rece_min_tot += use_time
                elif start_time.hour == 6:
                    contact_hour_6_rece_cnt += 1
                    contact_hour_6_rece_min_tot += use_time
                elif start_time.hour == 7:
                    contact_hour_7_rece_cnt += 1
                    contact_hour_7_rece_min_tot += use_time
                elif start_time.hour == 8:
                    contact_hour_8_rece_cnt += 1
                    contact_hour_8_rece_min_tot += use_time
                elif start_time.hour == 9:
                    contact_hour_9_rece_cnt += 1
                    contact_hour_9_rece_min_tot += use_time
                elif start_time.hour == 10:
                    contact_hour_10_rece_cnt += 1
                    contact_hour_10_rece_min_tot += use_time
                elif start_time.hour == 11:
                    contact_hour_11_rece_cnt += 1
                    contact_hour_11_rece_min_tot += use_time
                elif start_time.hour == 12:
                    contact_hour_12_rece_cnt += 1
                    contact_hour_12_rece_min_tot += use_time
                elif start_time.hour == 13:
                    contact_hour_13_rece_cnt += 1
                    contact_hour_13_rece_min_tot += use_time
                elif start_time.hour == 14:
                    contact_hour_14_rece_cnt += 1
                    contact_hour_14_rece_min_tot += use_time
                elif start_time.hour == 15:
                    contact_hour_15_rece_cnt += 1
                    contact_hour_15_rece_min_tot += use_time
                elif start_time.hour == 16:
                    contact_hour_16_rece_cnt += 1
                    contact_hour_16_rece_min_tot += use_time
                elif start_time.hour == 17:
                    contact_hour_17_rece_cnt += 1
                    contact_hour_17_rece_min_tot += use_time
                elif start_time.hour == 18:
                    contact_hour_18_rece_cnt += 1
                    contact_hour_18_rece_min_tot += use_time
                elif start_time.hour == 19:
                    contact_hour_19_rece_cnt += 1
                    contact_hour_19_rece_min_tot += use_time
                elif start_time.hour == 20:
                    contact_hour_20_rece_cnt += 1
                    contact_hour_20_rece_min_tot += use_time
                elif start_time.hour == 21:
                    contact_hour_21_rece_cnt += 1
                    contact_hour_21_rece_min_tot += use_time
                elif start_time.hour == 22:
                    contact_hour_22_rece_cnt += 1
                    contact_hour_22_rece_min_tot += use_time
                elif start_time.hour == 23:
                    contact_hour_23_rece_cnt += 1
                    contact_hour_23_rece_min_tot += use_time

            if start_time.weekday() in (0, 1, 2, 3, 4):
                # 0,1,2,3,4 对应星期一、二、三、四、五
                contact_weekday_cnt += 1
                contact_weekday_min_tot += use_time
                if u'主' in init_type or '主' in init_type:
                    contact_weekday_call_cnt += 1
                    contact_weekday_call_min_tot += use_time
                elif u'被' in init_type or '被' in init_type:
                    contact_weekday_rece_cnt += 1
                    contact_weekday_rece_min_tot += use_time
            elif start_time.weekday() in (5, 6):
                # 5,6 对应星期六、星期天
                contact_weekend_cnt += 1
                contact_weekend_min_tot += use_time
                if u'主' in init_type or '主' in init_type:
                    contact_weekend_call_cnt += 1
                    contact_weekend_call_min_tot += use_time
                elif u'被' in init_type or '被' in init_type:
                    contact_weekend_rece_cnt += 1
                    contact_weekend_rece_min_tot += use_time

            if use_time >= 15:
                contact_min_over_15s_cnt += 1
                contact_min_over_15s_min_tot += use_time
                if u'主' in init_type or '主' in init_type:
                    contact_min_over_15s_call_cnt += 1
                    contact_min_over_15s_call_min_tot += use_time
                elif u'被' in init_type or '被' in init_type:
                    contact_min_over_15s_rece_cnt += 1
                    contact_min_over_15s_rece_min_tot += use_time

            if use_time >= 30:
                contact_min_over_30s_cnt += 1
                contact_min_over_30s_min_tot += use_time
                if u'主' in init_type or '主' in init_type:
                    contact_min_over_30s_call_cnt += 1
                    contact_min_over_30s_call_min_tot += use_time
                elif u'被' in init_type or '被' in init_type:
                    contact_min_over_30s_rece_cnt += 1
                    contact_min_over_30s_rece_min_tot += use_time

            if use_time >= 60:
                contact_min_over_60s_cnt += 1
                contact_min_over_60s_min_tot += use_time
                if u'主' in init_type or '主' in init_type:
                    contact_min_over_60s_call_cnt += 1
                    contact_min_over_60s_call_min_tot += use_time
                elif u'被' in init_type or '被' in init_type:
                    contact_min_over_60s_rece_cnt += 1
                    contact_min_over_60s_rece_min_tot += use_time

            if spacing_interval <= 180:  # 6个月之内
                if start_time.hour == 0:
                    contact_hour_0_cnt_6_mon += 1
                    contact_hour_0_min_tot_6_mon += use_time
                elif start_time.hour == 1:
                    contact_hour_1_cnt_6_mon += 1
                    contact_hour_1_min_tot_6_mon += use_time
                elif start_time.hour == 2:
                    contact_hour_2_cnt_6_mon += 1
                    contact_hour_2_min_tot_6_mon += use_time
                elif start_time.hour == 3:
                    contact_hour_3_cnt_6_mon += 1
                    contact_hour_3_min_tot_6_mon += use_time
                elif start_time.hour == 4:
                    contact_hour_4_cnt_6_mon += 1
                    contact_hour_4_min_tot_6_mon += use_time
                elif start_time.hour == 5:
                    contact_hour_5_cnt_6_mon += 1
                    contact_hour_5_min_tot_6_mon += use_time
                elif start_time.hour == 6:
                    contact_hour_6_cnt_6_mon += 1
                    contact_hour_6_min_tot_6_mon += use_time
                elif start_time.hour == 7:
                    contact_hour_7_cnt_6_mon += 1
                    contact_hour_7_min_tot_6_mon += use_time
                elif start_time.hour == 8:
                    contact_hour_8_cnt_6_mon += 1
                    contact_hour_8_min_tot_6_mon += use_time
                elif start_time.hour == 9:
                    contact_hour_9_cnt_6_mon += 1
                    contact_hour_9_min_tot_6_mon += use_time
                elif start_time.hour == 10:
                    contact_hour_10_cnt_6_mon += 1
                    contact_hour_10_min_tot_6_mon += use_time
                elif start_time.hour == 11:
                    contact_hour_11_cnt_6_mon += 1
                    contact_hour_11_min_tot_6_mon += use_time
                elif start_time.hour == 12:
                    contact_hour_12_cnt_6_mon += 1
                    contact_hour_12_min_tot_6_mon += use_time
                elif start_time.hour == 13:
                    contact_hour_13_cnt_6_mon += 1
                    contact_hour_13_min_tot_6_mon += use_time
                elif start_time.hour == 14:
                    contact_hour_14_cnt_6_mon += 1
                    contact_hour_14_min_tot_6_mon += use_time
                elif start_time.hour == 15:
                    contact_hour_15_cnt_6_mon += 1
                    contact_hour_15_min_tot_6_mon += use_time
                elif start_time.hour == 16:
                    contact_hour_16_cnt_6_mon += 1
                    contact_hour_16_min_tot_6_mon += use_time
                elif start_time.hour == 17:
                    contact_hour_17_cnt_6_mon += 1
                    contact_hour_17_min_tot_6_mon += use_time
                elif start_time.hour == 18:
                    contact_hour_18_cnt_6_mon += 1
                    contact_hour_18_min_tot_6_mon += use_time
                elif start_time.hour == 19:
                    contact_hour_19_cnt_6_mon += 1
                    contact_hour_19_min_tot_6_mon += use_time
                elif start_time.hour == 20:
                    contact_hour_20_cnt_6_mon += 1
                    contact_hour_20_min_tot_6_mon += use_time
                elif start_time.hour == 21:
                    contact_hour_21_cnt_6_mon += 1
                    contact_hour_21_min_tot_6_mon += use_time
                elif start_time.hour == 22:
                    contact_hour_22_cnt_6_mon += 1
                    contact_hour_22_min_tot_6_mon += use_time
                elif start_time.hour == 23:
                    contact_hour_23_cnt_6_mon += 1
                    contact_hour_23_min_tot_6_mon += use_time

                if u'主' in init_type or '主' in init_type:
                    if start_time.hour == 0:
                        contact_hour_0_call_cnt_6_mon += 1
                        contact_hour_0_call_min_tot_6_mon += use_time
                    elif start_time.hour == 1:
                        contact_hour_1_call_cnt_6_mon += 1
                        contact_hour_1_call_min_tot_6_mon += use_time
                    elif start_time.hour == 2:
                        contact_hour_2_call_cnt_6_mon += 1
                        contact_hour_2_call_min_tot_6_mon += use_time
                    elif start_time.hour == 3:
                        contact_hour_3_call_cnt_6_mon += 1
                        contact_hour_3_call_min_tot_6_mon += use_time
                    elif start_time.hour == 4:
                        contact_hour_4_call_cnt_6_mon += 1
                        contact_hour_4_call_min_tot_6_mon += use_time
                    elif start_time.hour == 5:
                        contact_hour_5_call_cnt_6_mon += 1
                        contact_hour_5_call_min_tot_6_mon += use_time
                    elif start_time.hour == 6:
                        contact_hour_6_call_cnt_6_mon += 1
                        contact_hour_6_call_min_tot_6_mon += use_time
                    elif start_time.hour == 7:
                        contact_hour_7_call_cnt_6_mon += 1
                        contact_hour_7_call_min_tot_6_mon += use_time
                    elif start_time.hour == 8:
                        contact_hour_8_call_cnt_6_mon += 1
                        contact_hour_8_call_min_tot_6_mon += use_time
                    elif start_time.hour == 9:
                        contact_hour_9_call_cnt_6_mon += 1
                        contact_hour_9_call_min_tot_6_mon += use_time
                    elif start_time.hour == 10:
                        contact_hour_10_call_cnt_6_mon += 1
                        contact_hour_10_call_min_tot_6_mon += use_time
                    elif start_time.hour == 11:
                        contact_hour_11_call_cnt_6_mon += 1
                        contact_hour_11_call_min_tot_6_mon += use_time
                    elif start_time.hour == 12:
                        contact_hour_12_call_cnt_6_mon += 1
                        contact_hour_12_call_min_tot_6_mon += use_time
                    elif start_time.hour == 13:
                        contact_hour_13_call_cnt_6_mon += 1
                        contact_hour_13_call_min_tot_6_mon += use_time
                    elif start_time.hour == 14:
                        contact_hour_14_call_cnt_6_mon += 1
                        contact_hour_14_call_min_tot_6_mon += use_time
                    elif start_time.hour == 15:
                        contact_hour_15_call_cnt_6_mon += 1
                        contact_hour_15_call_min_tot_6_mon += use_time
                    elif start_time.hour == 16:
                        contact_hour_16_call_cnt_6_mon += 1
                        contact_hour_16_call_min_tot_6_mon += use_time
                    elif start_time.hour == 17:
                        contact_hour_17_call_cnt_6_mon += 1
                        contact_hour_17_call_min_tot_6_mon += use_time
                    elif start_time.hour == 18:
                        contact_hour_18_call_cnt_6_mon += 1
                        contact_hour_18_call_min_tot_6_mon += use_time
                    elif start_time.hour == 19:
                        contact_hour_19_call_cnt_6_mon += 1
                        contact_hour_19_call_min_tot_6_mon += use_time
                    elif start_time.hour == 20:
                        contact_hour_20_call_cnt_6_mon += 1
                        contact_hour_20_call_min_tot_6_mon += use_time
                    elif start_time.hour == 21:
                        contact_hour_21_call_cnt_6_mon += 1
                        contact_hour_21_call_min_tot_6_mon += use_time
                    elif start_time.hour == 22:
                        contact_hour_22_call_cnt_6_mon += 1
                        contact_hour_22_call_min_tot_6_mon += use_time
                    elif start_time.hour == 23:
                        contact_hour_23_call_cnt_6_mon += 1
                        contact_hour_23_call_min_tot_6_mon += use_time
                elif u'被' in init_type or '被' in init_type:
                    if start_time.hour == 0:
                        contact_hour_0_rece_cnt_6_mon += 1
                        contact_hour_0_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 1:
                        contact_hour_1_rece_cnt_6_mon += 1
                        contact_hour_1_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 2:
                        contact_hour_2_rece_cnt_6_mon += 1
                        contact_hour_2_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 3:
                        contact_hour_3_rece_cnt_6_mon += 1
                        contact_hour_3_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 4:
                        contact_hour_4_rece_cnt_6_mon += 1
                        contact_hour_4_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 5:
                        contact_hour_5_rece_cnt_6_mon += 1
                        contact_hour_5_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 6:
                        contact_hour_6_rece_cnt_6_mon += 1
                        contact_hour_6_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 7:
                        contact_hour_7_rece_cnt_6_mon += 1
                        contact_hour_7_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 8:
                        contact_hour_8_rece_cnt_6_mon += 1
                        contact_hour_8_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 9:
                        contact_hour_9_rece_cnt_6_mon += 1
                        contact_hour_9_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 10:
                        contact_hour_10_rece_cnt_6_mon += 1
                        contact_hour_10_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 11:
                        contact_hour_11_rece_cnt_6_mon += 1
                        contact_hour_11_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 12:
                        contact_hour_12_rece_cnt_6_mon += 1
                        contact_hour_12_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 13:
                        contact_hour_13_rece_cnt_6_mon += 1
                        contact_hour_13_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 14:
                        contact_hour_14_rece_cnt_6_mon += 1
                        contact_hour_14_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 15:
                        contact_hour_15_rece_cnt_6_mon += 1
                        contact_hour_15_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 16:
                        contact_hour_16_rece_cnt_6_mon += 1
                        contact_hour_16_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 17:
                        contact_hour_17_rece_cnt_6_mon += 1
                        contact_hour_17_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 18:
                        contact_hour_18_rece_cnt_6_mon += 1
                        contact_hour_18_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 19:
                        contact_hour_19_rece_cnt_6_mon += 1
                        contact_hour_19_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 20:
                        contact_hour_20_rece_cnt_6_mon += 1
                        contact_hour_20_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 21:
                        contact_hour_21_rece_cnt_6_mon += 1
                        contact_hour_21_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 22:
                        contact_hour_22_rece_cnt_6_mon += 1
                        contact_hour_22_rece_min_tot_6_mon += use_time
                    elif start_time.hour == 23:
                        contact_hour_23_rece_cnt_6_mon += 1
                        contact_hour_23_rece_min_tot_6_mon += use_time

                if start_time.weekday() in (0, 1, 2, 3, 4):
                    # 0,1,2,3,4 对应星期一、二、三、四、五
                    contact_weekday_cnt_6_mon += 1
                    contact_weekday_min_tot_6_mon += use_time
                    if u'主' in init_type or '主' in init_type:
                        contact_weekday_call_cnt_6_mon += 1
                        contact_weekday_call_min_tot_6_mon += use_time
                    elif u'被' in init_type or '被' in init_type:
                        contact_weekday_rece_cnt_6_mon += 1
                        contact_weekday_rece_min_tot_6_mon += use_time
                elif start_time.weekday() in (5, 6):
                    # 5,6 对应星期六、星期天
                    contact_weekend_cnt_6_mon += 1
                    contact_weekend_min_tot_6_mon += use_time
                    if u'主' in init_type or '主' in init_type:
                        contact_weekend_call_cnt_6_mon += 1
                        contact_weekend_call_min_tot_6_mon += use_time
                    elif u'被' in init_type or '被' in init_type:
                        contact_weekend_rece_cnt_6_mon += 1
                        contact_weekend_rece_min_tot_6_mon += use_time

                if use_time >= 15:
                    contact_min_over_15s_cnt_6_mon += 1
                    contact_min_over_15s_min_tot_6_mon += use_time
                    if u'主' in init_type or '主' in init_type:
                        contact_min_over_15s_call_cnt_6_mon += 1
                        contact_min_over_15s_call_min_tot_6_mon += use_time
                    elif u'被' in init_type or '被' in init_type:
                        contact_min_over_15s_rece_cnt_6_mon += 1
                        contact_min_over_15s_rece_min_tot_6_mon += use_time

                if use_time >= 30:
                    contact_min_over_30s_cnt_6_mon += 1
                    contact_min_over_30s_min_tot_6_mon += use_time
                    if u'主' in init_type or '主' in init_type:
                        contact_min_over_30s_call_cnt_6_mon += 1
                        contact_min_over_30s_call_min_tot_6_mon += use_time
                    elif u'被' in init_type or '被' in init_type:
                        contact_min_over_30s_rece_cnt_6_mon += 1
                        contact_min_over_30s_rece_min_tot_6_mon += use_time

                if use_time >= 60:
                    contact_min_over_60s_cnt_6_mon += 1
                    contact_min_over_60s_min_tot_6_mon += use_time
                    if u'主' in init_type or '主' in init_type:
                        contact_min_over_60s_call_cnt_6_mon += 1
                        contact_min_over_60s_call_min_tot_6_mon += use_time
                    elif u'被' in init_type or '被' in init_type:
                        contact_min_over_60s_rece_cnt_6_mon += 1
                        contact_min_over_60s_rece_min_tot_6_mon += use_time

                if spacing_interval <= 90:  # 3个月之内
                    if start_time.hour == 0:
                        contact_hour_0_cnt_3_mon += 1
                        contact_hour_0_min_tot_3_mon += use_time
                    elif start_time.hour == 1:
                        contact_hour_1_cnt_3_mon += 1
                        contact_hour_1_min_tot_3_mon += use_time
                    elif start_time.hour == 2:
                        contact_hour_2_cnt_3_mon += 1
                        contact_hour_2_min_tot_3_mon += use_time
                    elif start_time.hour == 3:
                        contact_hour_3_cnt_3_mon += 1
                        contact_hour_3_min_tot_3_mon += use_time
                    elif start_time.hour == 4:
                        contact_hour_4_cnt_3_mon += 1
                        contact_hour_4_min_tot_3_mon += use_time
                    elif start_time.hour == 5:
                        contact_hour_5_cnt_3_mon += 1
                        contact_hour_5_min_tot_3_mon += use_time
                    elif start_time.hour == 6:
                        contact_hour_6_cnt_3_mon += 1
                        contact_hour_6_min_tot_3_mon += use_time
                    elif start_time.hour == 7:
                        contact_hour_7_cnt_3_mon += 1
                        contact_hour_7_min_tot_3_mon += use_time
                    elif start_time.hour == 8:
                        contact_hour_8_cnt_3_mon += 1
                        contact_hour_8_min_tot_3_mon += use_time
                    elif start_time.hour == 9:
                        contact_hour_9_cnt_3_mon += 1
                        contact_hour_9_min_tot_3_mon += use_time
                    elif start_time.hour == 10:
                        contact_hour_10_cnt_3_mon += 1
                        contact_hour_10_min_tot_3_mon += use_time
                    elif start_time.hour == 11:
                        contact_hour_11_cnt_3_mon += 1
                        contact_hour_11_min_tot_3_mon += use_time
                    elif start_time.hour == 12:
                        contact_hour_12_cnt_3_mon += 1
                        contact_hour_12_min_tot_3_mon += use_time
                    elif start_time.hour == 13:
                        contact_hour_13_cnt_3_mon += 1
                        contact_hour_13_min_tot_3_mon += use_time
                    elif start_time.hour == 14:
                        contact_hour_14_cnt_3_mon += 1
                        contact_hour_14_min_tot_3_mon += use_time
                    elif start_time.hour == 15:
                        contact_hour_15_cnt_3_mon += 1
                        contact_hour_15_min_tot_3_mon += use_time
                    elif start_time.hour == 16:
                        contact_hour_16_cnt_3_mon += 1
                        contact_hour_16_min_tot_3_mon += use_time
                    elif start_time.hour == 17:
                        contact_hour_17_cnt_3_mon += 1
                        contact_hour_17_min_tot_3_mon += use_time
                    elif start_time.hour == 18:
                        contact_hour_18_cnt_3_mon += 1
                        contact_hour_18_min_tot_3_mon += use_time
                    elif start_time.hour == 19:
                        contact_hour_19_cnt_3_mon += 1
                        contact_hour_19_min_tot_3_mon += use_time
                    elif start_time.hour == 20:
                        contact_hour_20_cnt_3_mon += 1
                        contact_hour_20_min_tot_3_mon += use_time
                    elif start_time.hour == 21:
                        contact_hour_21_cnt_3_mon += 1
                        contact_hour_21_min_tot_3_mon += use_time
                    elif start_time.hour == 22:
                        contact_hour_22_cnt_3_mon += 1
                        contact_hour_22_min_tot_3_mon += use_time
                    elif start_time.hour == 23:
                        contact_hour_23_cnt_3_mon += 1
                        contact_hour_23_min_tot_3_mon += use_time

                    if u'主' in init_type or '主' in init_type:
                        if start_time.hour == 0:
                            contact_hour_0_call_cnt_3_mon += 1
                            contact_hour_0_call_min_tot_3_mon += use_time
                        elif start_time.hour == 1:
                            contact_hour_1_call_cnt_3_mon += 1
                            contact_hour_1_call_min_tot_3_mon += use_time
                        elif start_time.hour == 2:
                            contact_hour_2_call_cnt_3_mon += 1
                            contact_hour_2_call_min_tot_3_mon += use_time
                        elif start_time.hour == 3:
                            contact_hour_3_call_cnt_3_mon += 1
                            contact_hour_3_call_min_tot_3_mon += use_time
                        elif start_time.hour == 4:
                            contact_hour_4_call_cnt_3_mon += 1
                            contact_hour_4_call_min_tot_3_mon += use_time
                        elif start_time.hour == 5:
                            contact_hour_5_call_cnt_3_mon += 1
                            contact_hour_5_call_min_tot_3_mon += use_time
                        elif start_time.hour == 6:
                            contact_hour_6_call_cnt_3_mon += 1
                            contact_hour_6_call_min_tot_3_mon += use_time
                        elif start_time.hour == 7:
                            contact_hour_7_call_cnt_3_mon += 1
                            contact_hour_7_call_min_tot_3_mon += use_time
                        elif start_time.hour == 8:
                            contact_hour_8_call_cnt_3_mon += 1
                            contact_hour_8_call_min_tot_3_mon += use_time
                        elif start_time.hour == 9:
                            contact_hour_9_call_cnt_3_mon += 1
                            contact_hour_9_call_min_tot_3_mon += use_time
                        elif start_time.hour == 10:
                            contact_hour_10_call_cnt_3_mon += 1
                            contact_hour_10_call_min_tot_3_mon += use_time
                        elif start_time.hour == 11:
                            contact_hour_11_call_cnt_3_mon += 1
                            contact_hour_11_call_min_tot_3_mon += use_time
                        elif start_time.hour == 12:
                            contact_hour_12_call_cnt_3_mon += 1
                            contact_hour_12_call_min_tot_3_mon += use_time
                        elif start_time.hour == 13:
                            contact_hour_13_call_cnt_3_mon += 1
                            contact_hour_13_call_min_tot_3_mon += use_time
                        elif start_time.hour == 14:
                            contact_hour_14_call_cnt_3_mon += 1
                            contact_hour_14_call_min_tot_3_mon += use_time
                        elif start_time.hour == 15:
                            contact_hour_15_call_cnt_3_mon += 1
                            contact_hour_15_call_min_tot_3_mon += use_time
                        elif start_time.hour == 16:
                            contact_hour_16_call_cnt_3_mon += 1
                            contact_hour_16_call_min_tot_3_mon += use_time
                        elif start_time.hour == 17:
                            contact_hour_17_call_cnt_3_mon += 1
                            contact_hour_17_call_min_tot_3_mon += use_time
                        elif start_time.hour == 18:
                            contact_hour_18_call_cnt_3_mon += 1
                            contact_hour_18_call_min_tot_3_mon += use_time
                        elif start_time.hour == 19:
                            contact_hour_19_call_cnt_3_mon += 1
                            contact_hour_19_call_min_tot_3_mon += use_time
                        elif start_time.hour == 20:
                            contact_hour_20_call_cnt_3_mon += 1
                            contact_hour_20_call_min_tot_3_mon += use_time
                        elif start_time.hour == 21:
                            contact_hour_21_call_cnt_3_mon += 1
                            contact_hour_21_call_min_tot_3_mon += use_time
                        elif start_time.hour == 22:
                            contact_hour_22_call_cnt_3_mon += 1
                            contact_hour_22_call_min_tot_3_mon += use_time
                        elif start_time.hour == 23:
                            contact_hour_23_call_cnt_3_mon += 1
                            contact_hour_23_call_min_tot_3_mon += use_time
                    elif u'被' in init_type or '被' in init_type:
                        if start_time.hour == 0:
                            contact_hour_0_rece_cnt_3_mon += 1
                            contact_hour_0_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 1:
                            contact_hour_1_rece_cnt_3_mon += 1
                            contact_hour_1_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 2:
                            contact_hour_2_rece_cnt_3_mon += 1
                            contact_hour_2_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 3:
                            contact_hour_3_rece_cnt_3_mon += 1
                            contact_hour_3_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 4:
                            contact_hour_4_rece_cnt_3_mon += 1
                            contact_hour_4_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 5:
                            contact_hour_5_rece_cnt_3_mon += 1
                            contact_hour_5_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 6:
                            contact_hour_6_rece_cnt_3_mon += 1
                            contact_hour_6_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 7:
                            contact_hour_7_rece_cnt_3_mon += 1
                            contact_hour_7_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 8:
                            contact_hour_8_rece_cnt_3_mon += 1
                            contact_hour_8_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 9:
                            contact_hour_9_rece_cnt_3_mon += 1
                            contact_hour_9_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 10:
                            contact_hour_10_rece_cnt_3_mon += 1
                            contact_hour_10_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 11:
                            contact_hour_11_rece_cnt_3_mon += 1
                            contact_hour_11_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 12:
                            contact_hour_12_rece_cnt_3_mon += 1
                            contact_hour_12_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 13:
                            contact_hour_13_rece_cnt_3_mon += 1
                            contact_hour_13_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 14:
                            contact_hour_14_rece_cnt_3_mon += 1
                            contact_hour_14_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 15:
                            contact_hour_15_rece_cnt_3_mon += 1
                            contact_hour_15_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 16:
                            contact_hour_16_rece_cnt_3_mon += 1
                            contact_hour_16_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 17:
                            contact_hour_17_rece_cnt_3_mon += 1
                            contact_hour_17_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 18:
                            contact_hour_18_rece_cnt_3_mon += 1
                            contact_hour_18_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 19:
                            contact_hour_19_rece_cnt_3_mon += 1
                            contact_hour_19_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 20:
                            contact_hour_20_rece_cnt_3_mon += 1
                            contact_hour_20_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 21:
                            contact_hour_21_rece_cnt_3_mon += 1
                            contact_hour_21_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 22:
                            contact_hour_22_rece_cnt_3_mon += 1
                            contact_hour_22_rece_min_tot_3_mon += use_time
                        elif start_time.hour == 23:
                            contact_hour_23_rece_cnt_3_mon += 1
                            contact_hour_23_rece_min_tot_3_mon += use_time

                    if start_time.weekday() in (0, 1, 2, 3, 4):
                        # 0,1,2,3,4 对应星期一、二、三、四、五
                        contact_weekday_cnt_3_mon += 1
                        contact_weekday_min_tot_3_mon += use_time
                        if u'主' in init_type or '主' in init_type:
                            contact_weekday_call_cnt_3_mon += 1
                            contact_weekday_call_min_tot_3_mon += use_time
                        elif u'被' in init_type or '被' in init_type:
                            contact_weekday_rece_cnt_3_mon += 1
                            contact_weekday_rece_min_tot_3_mon += use_time
                    elif start_time.weekday() in (5, 6):
                        # 5,6 对应星期六、星期天
                        contact_weekend_cnt_3_mon += 1
                        contact_weekend_min_tot_3_mon += use_time
                        if u'主' in init_type or '主' in init_type:
                            contact_weekend_call_cnt_3_mon += 1
                            contact_weekend_call_min_tot_3_mon += use_time
                        elif u'被' in init_type or '被' in init_type:
                            contact_weekend_rece_cnt_3_mon += 1
                            contact_weekend_rece_min_tot_3_mon += use_time

                    if use_time >= 15:
                        contact_min_over_15s_cnt_3_mon += 1
                        contact_min_over_15s_min_tot_3_mon += use_time
                        if u'主' in init_type or '主' in init_type:
                            contact_min_over_15s_call_cnt_3_mon += 1
                            contact_min_over_15s_call_min_tot_3_mon += use_time
                        elif u'被' in init_type or '被' in init_type:
                            contact_min_over_15s_rece_cnt_3_mon += 1
                            contact_min_over_15s_rece_min_tot_3_mon += use_time

                    if use_time >= 30:
                        contact_min_over_30s_cnt_3_mon += 1
                        contact_min_over_30s_min_tot_3_mon += use_time
                        if u'主' in init_type or '主' in init_type:
                            contact_min_over_30s_call_cnt_3_mon += 1
                            contact_min_over_30s_call_min_tot_3_mon += use_time
                        elif u'被' in init_type or '被' in init_type:
                            contact_min_over_30s_rece_cnt_3_mon += 1
                            contact_min_over_30s_rece_min_tot_3_mon += use_time

                    if use_time >= 60:
                        contact_min_over_60s_cnt_3_mon += 1
                        contact_min_over_60s_min_tot_3_mon += use_time
                        if u'主' in init_type or '主' in init_type:
                            contact_min_over_60s_call_cnt_3_mon += 1
                            contact_min_over_60s_call_min_tot_3_mon += use_time
                        elif u'被' in init_type or '被' in init_type:
                            contact_min_over_60s_rece_cnt_3_mon += 1
                            contact_min_over_60s_rece_min_tot_3_mon += use_time

                    if spacing_interval <= 60:  # 2个月之内
                        if start_time.hour == 0:
                            contact_hour_0_cnt_2_mon += 1
                            contact_hour_0_min_tot_2_mon += use_time
                        elif start_time.hour == 1:
                            contact_hour_1_cnt_2_mon += 1
                            contact_hour_1_min_tot_2_mon += use_time
                        elif start_time.hour == 2:
                            contact_hour_2_cnt_2_mon += 1
                            contact_hour_2_min_tot_2_mon += use_time
                        elif start_time.hour == 3:
                            contact_hour_3_cnt_2_mon += 1
                            contact_hour_3_min_tot_2_mon += use_time
                        elif start_time.hour == 4:
                            contact_hour_4_cnt_2_mon += 1
                            contact_hour_4_min_tot_2_mon += use_time
                        elif start_time.hour == 5:
                            contact_hour_5_cnt_2_mon += 1
                            contact_hour_5_min_tot_2_mon += use_time
                        elif start_time.hour == 6:
                            contact_hour_6_cnt_2_mon += 1
                            contact_hour_6_min_tot_2_mon += use_time
                        elif start_time.hour == 7:
                            contact_hour_7_cnt_2_mon += 1
                            contact_hour_7_min_tot_2_mon += use_time
                        elif start_time.hour == 8:
                            contact_hour_8_cnt_2_mon += 1
                            contact_hour_8_min_tot_2_mon += use_time
                        elif start_time.hour == 9:
                            contact_hour_9_cnt_2_mon += 1
                            contact_hour_9_min_tot_2_mon += use_time
                        elif start_time.hour == 10:
                            contact_hour_10_cnt_2_mon += 1
                            contact_hour_10_min_tot_2_mon += use_time
                        elif start_time.hour == 11:
                            contact_hour_11_cnt_2_mon += 1
                            contact_hour_11_min_tot_2_mon += use_time
                        elif start_time.hour == 12:
                            contact_hour_12_cnt_2_mon += 1
                            contact_hour_12_min_tot_2_mon += use_time
                        elif start_time.hour == 13:
                            contact_hour_13_cnt_2_mon += 1
                            contact_hour_13_min_tot_2_mon += use_time
                        elif start_time.hour == 14:
                            contact_hour_14_cnt_2_mon += 1
                            contact_hour_14_min_tot_2_mon += use_time
                        elif start_time.hour == 15:
                            contact_hour_15_cnt_2_mon += 1
                            contact_hour_15_min_tot_2_mon += use_time
                        elif start_time.hour == 16:
                            contact_hour_16_cnt_2_mon += 1
                            contact_hour_16_min_tot_2_mon += use_time
                        elif start_time.hour == 17:
                            contact_hour_17_cnt_2_mon += 1
                            contact_hour_17_min_tot_2_mon += use_time
                        elif start_time.hour == 18:
                            contact_hour_18_cnt_2_mon += 1
                            contact_hour_18_min_tot_2_mon += use_time
                        elif start_time.hour == 19:
                            contact_hour_19_cnt_2_mon += 1
                            contact_hour_19_min_tot_2_mon += use_time
                        elif start_time.hour == 20:
                            contact_hour_20_cnt_2_mon += 1
                            contact_hour_20_min_tot_2_mon += use_time
                        elif start_time.hour == 21:
                            contact_hour_21_cnt_2_mon += 1
                            contact_hour_21_min_tot_2_mon += use_time
                        elif start_time.hour == 22:
                            contact_hour_22_cnt_2_mon += 1
                            contact_hour_22_min_tot_2_mon += use_time
                        elif start_time.hour == 23:
                            contact_hour_23_cnt_2_mon += 1
                            contact_hour_23_min_tot_2_mon += use_time

                        if u'主' in init_type or '主' in init_type:
                            if start_time.hour == 0:
                                contact_hour_0_call_cnt_2_mon += 1
                                contact_hour_0_call_min_tot_2_mon += use_time
                            elif start_time.hour == 1:
                                contact_hour_1_call_cnt_2_mon += 1
                                contact_hour_1_call_min_tot_2_mon += use_time
                            elif start_time.hour == 2:
                                contact_hour_2_call_cnt_2_mon += 1
                                contact_hour_2_call_min_tot_2_mon += use_time
                            elif start_time.hour == 3:
                                contact_hour_3_call_cnt_2_mon += 1
                                contact_hour_3_call_min_tot_2_mon += use_time
                            elif start_time.hour == 4:
                                contact_hour_4_call_cnt_2_mon += 1
                                contact_hour_4_call_min_tot_2_mon += use_time
                            elif start_time.hour == 5:
                                contact_hour_5_call_cnt_2_mon += 1
                                contact_hour_5_call_min_tot_2_mon += use_time
                            elif start_time.hour == 6:
                                contact_hour_6_call_cnt_2_mon += 1
                                contact_hour_6_call_min_tot_2_mon += use_time
                            elif start_time.hour == 7:
                                contact_hour_7_call_cnt_2_mon += 1
                                contact_hour_7_call_min_tot_2_mon += use_time
                            elif start_time.hour == 8:
                                contact_hour_8_call_cnt_2_mon += 1
                                contact_hour_8_call_min_tot_2_mon += use_time
                            elif start_time.hour == 9:
                                contact_hour_9_call_cnt_2_mon += 1
                                contact_hour_9_call_min_tot_2_mon += use_time
                            elif start_time.hour == 10:
                                contact_hour_10_call_cnt_2_mon += 1
                                contact_hour_10_call_min_tot_2_mon += use_time
                            elif start_time.hour == 11:
                                contact_hour_11_call_cnt_2_mon += 1
                                contact_hour_11_call_min_tot_2_mon += use_time
                            elif start_time.hour == 12:
                                contact_hour_12_call_cnt_2_mon += 1
                                contact_hour_12_call_min_tot_2_mon += use_time
                            elif start_time.hour == 13:
                                contact_hour_13_call_cnt_2_mon += 1
                                contact_hour_13_call_min_tot_2_mon += use_time
                            elif start_time.hour == 14:
                                contact_hour_14_call_cnt_2_mon += 1
                                contact_hour_14_call_min_tot_2_mon += use_time
                            elif start_time.hour == 15:
                                contact_hour_15_call_cnt_2_mon += 1
                                contact_hour_15_call_min_tot_2_mon += use_time
                            elif start_time.hour == 16:
                                contact_hour_16_call_cnt_2_mon += 1
                                contact_hour_16_call_min_tot_2_mon += use_time
                            elif start_time.hour == 17:
                                contact_hour_17_call_cnt_2_mon += 1
                                contact_hour_17_call_min_tot_2_mon += use_time
                            elif start_time.hour == 18:
                                contact_hour_18_call_cnt_2_mon += 1
                                contact_hour_18_call_min_tot_2_mon += use_time
                            elif start_time.hour == 19:
                                contact_hour_19_call_cnt_2_mon += 1
                                contact_hour_19_call_min_tot_2_mon += use_time
                            elif start_time.hour == 20:
                                contact_hour_20_call_cnt_2_mon += 1
                                contact_hour_20_call_min_tot_2_mon += use_time
                            elif start_time.hour == 21:
                                contact_hour_21_call_cnt_2_mon += 1
                                contact_hour_21_call_min_tot_2_mon += use_time
                            elif start_time.hour == 22:
                                contact_hour_22_call_cnt_2_mon += 1
                                contact_hour_22_call_min_tot_2_mon += use_time
                            elif start_time.hour == 23:
                                contact_hour_23_call_cnt_2_mon += 1
                                contact_hour_23_call_min_tot_2_mon += use_time
                        elif u'被' in init_type or '被' in init_type:
                            if start_time.hour == 0:
                                contact_hour_0_rece_cnt_2_mon += 1
                                contact_hour_0_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 1:
                                contact_hour_1_rece_cnt_2_mon += 1
                                contact_hour_1_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 2:
                                contact_hour_2_rece_cnt_2_mon += 1
                                contact_hour_2_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 3:
                                contact_hour_3_rece_cnt_2_mon += 1
                                contact_hour_3_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 4:
                                contact_hour_4_rece_cnt_2_mon += 1
                                contact_hour_4_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 5:
                                contact_hour_5_rece_cnt_2_mon += 1
                                contact_hour_5_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 6:
                                contact_hour_6_rece_cnt_2_mon += 1
                                contact_hour_6_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 7:
                                contact_hour_7_rece_cnt_2_mon += 1
                                contact_hour_7_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 8:
                                contact_hour_8_rece_cnt_2_mon += 1
                                contact_hour_8_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 9:
                                contact_hour_9_rece_cnt_2_mon += 1
                                contact_hour_9_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 10:
                                contact_hour_10_rece_cnt_2_mon += 1
                                contact_hour_10_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 11:
                                contact_hour_11_rece_cnt_2_mon += 1
                                contact_hour_11_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 12:
                                contact_hour_12_rece_cnt_2_mon += 1
                                contact_hour_12_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 13:
                                contact_hour_13_rece_cnt_2_mon += 1
                                contact_hour_13_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 14:
                                contact_hour_14_rece_cnt_2_mon += 1
                                contact_hour_14_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 15:
                                contact_hour_15_rece_cnt_2_mon += 1
                                contact_hour_15_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 16:
                                contact_hour_16_rece_cnt_2_mon += 1
                                contact_hour_16_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 17:
                                contact_hour_17_rece_cnt_2_mon += 1
                                contact_hour_17_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 18:
                                contact_hour_18_rece_cnt_2_mon += 1
                                contact_hour_18_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 19:
                                contact_hour_19_rece_cnt_2_mon += 1
                                contact_hour_19_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 20:
                                contact_hour_20_rece_cnt_2_mon += 1
                                contact_hour_20_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 21:
                                contact_hour_21_rece_cnt_2_mon += 1
                                contact_hour_21_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 22:
                                contact_hour_22_rece_cnt_2_mon += 1
                                contact_hour_22_rece_min_tot_2_mon += use_time
                            elif start_time.hour == 23:
                                contact_hour_23_rece_cnt_2_mon += 1
                                contact_hour_23_rece_min_tot_2_mon += use_time

                        if start_time.weekday() in (0, 1, 2, 3, 4):
                            # 0,1,2,3,4 对应星期一、二、三、四、五
                            contact_weekday_cnt_2_mon += 1
                            contact_weekday_min_tot_2_mon += use_time
                            if u'主' in init_type or '主' in init_type:
                                contact_weekday_call_cnt_2_mon += 1
                                contact_weekday_call_min_tot_2_mon += use_time
                            elif u'被' in init_type or '被' in init_type:
                                contact_weekday_rece_cnt_2_mon += 1
                                contact_weekday_rece_min_tot_2_mon += use_time
                        elif start_time.weekday() in (5, 6):
                            # 5,6 对应星期六、星期天
                            contact_weekend_cnt_2_mon += 1
                            contact_weekend_min_tot_2_mon += use_time
                            if u'主' in init_type or '主' in init_type:
                                contact_weekend_call_cnt_2_mon += 1
                                contact_weekend_call_min_tot_2_mon += use_time
                            elif u'被' in init_type or '被' in init_type:
                                contact_weekend_rece_cnt_2_mon += 1
                                contact_weekend_rece_min_tot_2_mon += use_time

                        if use_time >= 15:
                            contact_min_over_15s_cnt_2_mon += 1
                            contact_min_over_15s_min_tot_2_mon += use_time
                            if u'主' in init_type or '主' in init_type:
                                contact_min_over_15s_call_cnt_2_mon += 1
                                contact_min_over_15s_call_min_tot_2_mon += use_time
                            elif u'被' in init_type or '被' in init_type:
                                contact_min_over_15s_rece_cnt_2_mon += 1
                                contact_min_over_15s_rece_min_tot_2_mon += use_time

                        if use_time >= 30:
                            contact_min_over_30s_cnt_2_mon += 1
                            contact_min_over_30s_min_tot_2_mon += use_time
                            if u'主' in init_type or '主' in init_type:
                                contact_min_over_30s_call_cnt_2_mon += 1
                                contact_min_over_30s_call_min_tot_2_mon += use_time
                            elif u'被' in init_type or '被' in init_type:
                                contact_min_over_30s_rece_cnt_2_mon += 1
                                contact_min_over_30s_rece_min_tot_2_mon += use_time

                        if use_time >= 60:
                            contact_min_over_60s_cnt_2_mon += 1
                            contact_min_over_60s_min_tot_2_mon += use_time
                            if u'主' in init_type or '主' in init_type:
                                contact_min_over_60s_call_cnt_2_mon += 1
                                contact_min_over_60s_call_min_tot_2_mon += use_time
                            elif u'被' in init_type or '被' in init_type:
                                contact_min_over_60s_rece_cnt_2_mon += 1
                                contact_min_over_60s_rece_min_tot_2_mon += use_time

                        if spacing_interval <= 30:  # 1个月之内
                            if start_time.hour == 0:
                                contact_hour_0_cnt_1_mon += 1
                                contact_hour_0_min_tot_1_mon += use_time
                            elif start_time.hour == 1:
                                contact_hour_1_cnt_1_mon += 1
                                contact_hour_1_min_tot_1_mon += use_time
                            elif start_time.hour == 2:
                                contact_hour_2_cnt_1_mon += 1
                                contact_hour_2_min_tot_1_mon += use_time
                            elif start_time.hour == 3:
                                contact_hour_3_cnt_1_mon += 1
                                contact_hour_3_min_tot_1_mon += use_time
                            elif start_time.hour == 4:
                                contact_hour_4_cnt_1_mon += 1
                                contact_hour_4_min_tot_1_mon += use_time
                            elif start_time.hour == 5:
                                contact_hour_5_cnt_1_mon += 1
                                contact_hour_5_min_tot_1_mon += use_time
                            elif start_time.hour == 6:
                                contact_hour_6_cnt_1_mon += 1
                                contact_hour_6_min_tot_1_mon += use_time
                            elif start_time.hour == 7:
                                contact_hour_7_cnt_1_mon += 1
                                contact_hour_7_min_tot_1_mon += use_time
                            elif start_time.hour == 8:
                                contact_hour_8_cnt_1_mon += 1
                                contact_hour_8_min_tot_1_mon += use_time
                            elif start_time.hour == 9:
                                contact_hour_9_cnt_1_mon += 1
                                contact_hour_9_min_tot_1_mon += use_time
                            elif start_time.hour == 10:
                                contact_hour_10_cnt_1_mon += 1
                                contact_hour_10_min_tot_1_mon += use_time
                            elif start_time.hour == 11:
                                contact_hour_11_cnt_1_mon += 1
                                contact_hour_11_min_tot_1_mon += use_time
                            elif start_time.hour == 12:
                                contact_hour_12_cnt_1_mon += 1
                                contact_hour_12_min_tot_1_mon += use_time
                            elif start_time.hour == 13:
                                contact_hour_13_cnt_1_mon += 1
                                contact_hour_13_min_tot_1_mon += use_time
                            elif start_time.hour == 14:
                                contact_hour_14_cnt_1_mon += 1
                                contact_hour_14_min_tot_1_mon += use_time
                            elif start_time.hour == 15:
                                contact_hour_15_cnt_1_mon += 1
                                contact_hour_15_min_tot_1_mon += use_time
                            elif start_time.hour == 16:
                                contact_hour_16_cnt_1_mon += 1
                                contact_hour_16_min_tot_1_mon += use_time
                            elif start_time.hour == 17:
                                contact_hour_17_cnt_1_mon += 1
                                contact_hour_17_min_tot_1_mon += use_time
                            elif start_time.hour == 18:
                                contact_hour_18_cnt_1_mon += 1
                                contact_hour_18_min_tot_1_mon += use_time
                            elif start_time.hour == 19:
                                contact_hour_19_cnt_1_mon += 1
                                contact_hour_19_min_tot_1_mon += use_time
                            elif start_time.hour == 20:
                                contact_hour_20_cnt_1_mon += 1
                                contact_hour_20_min_tot_1_mon += use_time
                            elif start_time.hour == 21:
                                contact_hour_21_cnt_1_mon += 1
                                contact_hour_21_min_tot_1_mon += use_time
                            elif start_time.hour == 22:
                                contact_hour_22_cnt_1_mon += 1
                                contact_hour_22_min_tot_1_mon += use_time
                            elif start_time.hour == 23:
                                contact_hour_23_cnt_1_mon += 1
                                contact_hour_23_min_tot_1_mon += use_time

                            if u'主' in init_type or '主' in init_type:
                                if start_time.hour == 0:
                                    contact_hour_0_call_cnt_1_mon += 1
                                    contact_hour_0_call_min_tot_1_mon += use_time
                                elif start_time.hour == 1:
                                    contact_hour_1_call_cnt_1_mon += 1
                                    contact_hour_1_call_min_tot_1_mon += use_time
                                elif start_time.hour == 2:
                                    contact_hour_2_call_cnt_1_mon += 1
                                    contact_hour_2_call_min_tot_1_mon += use_time
                                elif start_time.hour == 3:
                                    contact_hour_3_call_cnt_1_mon += 1
                                    contact_hour_3_call_min_tot_1_mon += use_time
                                elif start_time.hour == 4:
                                    contact_hour_4_call_cnt_1_mon += 1
                                    contact_hour_4_call_min_tot_1_mon += use_time
                                elif start_time.hour == 5:
                                    contact_hour_5_call_cnt_1_mon += 1
                                    contact_hour_5_call_min_tot_1_mon += use_time
                                elif start_time.hour == 6:
                                    contact_hour_6_call_cnt_1_mon += 1
                                    contact_hour_6_call_min_tot_1_mon += use_time
                                elif start_time.hour == 7:
                                    contact_hour_7_call_cnt_1_mon += 1
                                    contact_hour_7_call_min_tot_1_mon += use_time
                                elif start_time.hour == 8:
                                    contact_hour_8_call_cnt_1_mon += 1
                                    contact_hour_8_call_min_tot_1_mon += use_time
                                elif start_time.hour == 9:
                                    contact_hour_9_call_cnt_1_mon += 1
                                    contact_hour_9_call_min_tot_1_mon += use_time
                                elif start_time.hour == 10:
                                    contact_hour_10_call_cnt_1_mon += 1
                                    contact_hour_10_call_min_tot_1_mon += use_time
                                elif start_time.hour == 11:
                                    contact_hour_11_call_cnt_1_mon += 1
                                    contact_hour_11_call_min_tot_1_mon += use_time
                                elif start_time.hour == 12:
                                    contact_hour_12_call_cnt_1_mon += 1
                                    contact_hour_12_call_min_tot_1_mon += use_time
                                elif start_time.hour == 13:
                                    contact_hour_13_call_cnt_1_mon += 1
                                    contact_hour_13_call_min_tot_1_mon += use_time
                                elif start_time.hour == 14:
                                    contact_hour_14_call_cnt_1_mon += 1
                                    contact_hour_14_call_min_tot_1_mon += use_time
                                elif start_time.hour == 15:
                                    contact_hour_15_call_cnt_1_mon += 1
                                    contact_hour_15_call_min_tot_1_mon += use_time
                                elif start_time.hour == 16:
                                    contact_hour_16_call_cnt_1_mon += 1
                                    contact_hour_16_call_min_tot_1_mon += use_time
                                elif start_time.hour == 17:
                                    contact_hour_17_call_cnt_1_mon += 1
                                    contact_hour_17_call_min_tot_1_mon += use_time
                                elif start_time.hour == 18:
                                    contact_hour_18_call_cnt_1_mon += 1
                                    contact_hour_18_call_min_tot_1_mon += use_time
                                elif start_time.hour == 19:
                                    contact_hour_19_call_cnt_1_mon += 1
                                    contact_hour_19_call_min_tot_1_mon += use_time
                                elif start_time.hour == 20:
                                    contact_hour_20_call_cnt_1_mon += 1
                                    contact_hour_20_call_min_tot_1_mon += use_time
                                elif start_time.hour == 21:
                                    contact_hour_21_call_cnt_1_mon += 1
                                    contact_hour_21_call_min_tot_1_mon += use_time
                                elif start_time.hour == 22:
                                    contact_hour_22_call_cnt_1_mon += 1
                                    contact_hour_22_call_min_tot_1_mon += use_time
                                elif start_time.hour == 23:
                                    contact_hour_23_call_cnt_1_mon += 1
                                    contact_hour_23_call_min_tot_1_mon += use_time
                            elif u'被' in init_type or '被' in init_type:
                                if start_time.hour == 0:
                                    contact_hour_0_rece_cnt_1_mon += 1
                                    contact_hour_0_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 1:
                                    contact_hour_1_rece_cnt_1_mon += 1
                                    contact_hour_1_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 2:
                                    contact_hour_2_rece_cnt_1_mon += 1
                                    contact_hour_2_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 3:
                                    contact_hour_3_rece_cnt_1_mon += 1
                                    contact_hour_3_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 4:
                                    contact_hour_4_rece_cnt_1_mon += 1
                                    contact_hour_4_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 5:
                                    contact_hour_5_rece_cnt_1_mon += 1
                                    contact_hour_5_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 6:
                                    contact_hour_6_rece_cnt_1_mon += 1
                                    contact_hour_6_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 7:
                                    contact_hour_7_rece_cnt_1_mon += 1
                                    contact_hour_7_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 8:
                                    contact_hour_8_rece_cnt_1_mon += 1
                                    contact_hour_8_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 9:
                                    contact_hour_9_rece_cnt_1_mon += 1
                                    contact_hour_9_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 10:
                                    contact_hour_10_rece_cnt_1_mon += 1
                                    contact_hour_10_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 11:
                                    contact_hour_11_rece_cnt_1_mon += 1
                                    contact_hour_11_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 12:
                                    contact_hour_12_rece_cnt_1_mon += 1
                                    contact_hour_12_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 13:
                                    contact_hour_13_rece_cnt_1_mon += 1
                                    contact_hour_13_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 14:
                                    contact_hour_14_rece_cnt_1_mon += 1
                                    contact_hour_14_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 15:
                                    contact_hour_15_rece_cnt_1_mon += 1
                                    contact_hour_15_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 16:
                                    contact_hour_16_rece_cnt_1_mon += 1
                                    contact_hour_16_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 17:
                                    contact_hour_17_rece_cnt_1_mon += 1
                                    contact_hour_17_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 18:
                                    contact_hour_18_rece_cnt_1_mon += 1
                                    contact_hour_18_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 19:
                                    contact_hour_19_rece_cnt_1_mon += 1
                                    contact_hour_19_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 20:
                                    contact_hour_20_rece_cnt_1_mon += 1
                                    contact_hour_20_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 21:
                                    contact_hour_21_rece_cnt_1_mon += 1
                                    contact_hour_21_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 22:
                                    contact_hour_22_rece_cnt_1_mon += 1
                                    contact_hour_22_rece_min_tot_1_mon += use_time
                                elif start_time.hour == 23:
                                    contact_hour_23_rece_cnt_1_mon += 1
                                    contact_hour_23_rece_min_tot_1_mon += use_time

                            if start_time.weekday() in (0, 1, 2, 3, 4):
                                # 0,1,2,3,4 对应星期一、二、三、四、五
                                contact_weekday_cnt_1_mon += 1
                                contact_weekday_min_tot_1_mon += use_time
                                if u'主' in init_type or '主' in init_type:
                                    contact_weekday_call_cnt_1_mon += 1
                                    contact_weekday_call_min_tot_1_mon += use_time
                                elif u'被' in init_type or '被' in init_type:
                                    contact_weekday_rece_cnt_1_mon += 1
                                    contact_weekday_rece_min_tot_1_mon += use_time
                            elif start_time.weekday() in (5, 6):
                                # 5,6 对应星期六、星期天
                                contact_weekend_cnt_1_mon += 1
                                contact_weekend_min_tot_1_mon += use_time
                                if u'主' in init_type or '主' in init_type:
                                    contact_weekend_call_cnt_1_mon += 1
                                    contact_weekend_call_min_tot_1_mon += use_time
                                elif u'被' in init_type or '被' in init_type:
                                    contact_weekend_rece_cnt_1_mon += 1
                                    contact_weekend_rece_min_tot_1_mon += use_time

                            if use_time >= 15:
                                contact_min_over_15s_cnt_1_mon += 1
                                contact_min_over_15s_min_tot_1_mon += use_time
                                if u'主' in init_type or '主' in init_type:
                                    contact_min_over_15s_call_cnt_1_mon += 1
                                    contact_min_over_15s_call_min_tot_1_mon += use_time
                                elif u'被' in init_type or '被' in init_type:
                                    contact_min_over_15s_rece_cnt_1_mon += 1
                                    contact_min_over_15s_rece_min_tot_1_mon += use_time

                            if use_time >= 30:
                                contact_min_over_30s_cnt_1_mon += 1
                                contact_min_over_30s_min_tot_1_mon += use_time
                                if u'主' in init_type or '主' in init_type:
                                    contact_min_over_30s_call_cnt_1_mon += 1
                                    contact_min_over_30s_call_min_tot_1_mon += use_time
                                elif u'被' in init_type or '被' in init_type:
                                    contact_min_over_30s_rece_cnt_1_mon += 1
                                    contact_min_over_30s_rece_min_tot_1_mon += use_time

                            if use_time >= 60:
                                contact_min_over_60s_cnt_1_mon += 1
                                contact_min_over_60s_min_tot_1_mon += use_time
                                if u'主' in init_type or '主' in init_type:
                                    contact_min_over_60s_call_cnt_1_mon += 1
                                    contact_min_over_60s_call_min_tot_1_mon += use_time
                                elif u'被' in init_type or '被' in init_type:
                                    contact_min_over_60s_rece_cnt_1_mon += 1
                                    contact_min_over_60s_rece_min_tot_1_mon += use_time

                            if spacing_interval <= 14:  # 2周之内
                                if start_time.hour == 0:
                                    contact_hour_0_cnt_2_wk += 1
                                    contact_hour_0_min_tot_2_wk += use_time
                                elif start_time.hour == 1:
                                    contact_hour_1_cnt_2_wk += 1
                                    contact_hour_1_min_tot_2_wk += use_time
                                elif start_time.hour == 2:
                                    contact_hour_2_cnt_2_wk += 1
                                    contact_hour_2_min_tot_2_wk += use_time
                                elif start_time.hour == 3:
                                    contact_hour_3_cnt_2_wk += 1
                                    contact_hour_3_min_tot_2_wk += use_time
                                elif start_time.hour == 4:
                                    contact_hour_4_cnt_2_wk += 1
                                    contact_hour_4_min_tot_2_wk += use_time
                                elif start_time.hour == 5:
                                    contact_hour_5_cnt_2_wk += 1
                                    contact_hour_5_min_tot_2_wk += use_time
                                elif start_time.hour == 6:
                                    contact_hour_6_cnt_2_wk += 1
                                    contact_hour_6_min_tot_2_wk += use_time
                                elif start_time.hour == 7:
                                    contact_hour_7_cnt_2_wk += 1
                                    contact_hour_7_min_tot_2_wk += use_time
                                elif start_time.hour == 8:
                                    contact_hour_8_cnt_2_wk += 1
                                    contact_hour_8_min_tot_2_wk += use_time
                                elif start_time.hour == 9:
                                    contact_hour_9_cnt_2_wk += 1
                                    contact_hour_9_min_tot_2_wk += use_time
                                elif start_time.hour == 10:
                                    contact_hour_10_cnt_2_wk += 1
                                    contact_hour_10_min_tot_2_wk += use_time
                                elif start_time.hour == 11:
                                    contact_hour_11_cnt_2_wk += 1
                                    contact_hour_11_min_tot_2_wk += use_time
                                elif start_time.hour == 12:
                                    contact_hour_12_cnt_2_wk += 1
                                    contact_hour_12_min_tot_2_wk += use_time
                                elif start_time.hour == 13:
                                    contact_hour_13_cnt_2_wk += 1
                                    contact_hour_13_min_tot_2_wk += use_time
                                elif start_time.hour == 14:
                                    contact_hour_14_cnt_2_wk += 1
                                    contact_hour_14_min_tot_2_wk += use_time
                                elif start_time.hour == 15:
                                    contact_hour_15_cnt_2_wk += 1
                                    contact_hour_15_min_tot_2_wk += use_time
                                elif start_time.hour == 16:
                                    contact_hour_16_cnt_2_wk += 1
                                    contact_hour_16_min_tot_2_wk += use_time
                                elif start_time.hour == 17:
                                    contact_hour_17_cnt_2_wk += 1
                                    contact_hour_17_min_tot_2_wk += use_time
                                elif start_time.hour == 18:
                                    contact_hour_18_cnt_2_wk += 1
                                    contact_hour_18_min_tot_2_wk += use_time
                                elif start_time.hour == 19:
                                    contact_hour_19_cnt_2_wk += 1
                                    contact_hour_19_min_tot_2_wk += use_time
                                elif start_time.hour == 20:
                                    contact_hour_20_cnt_2_wk += 1
                                    contact_hour_20_min_tot_2_wk += use_time
                                elif start_time.hour == 21:
                                    contact_hour_21_cnt_2_wk += 1
                                    contact_hour_21_min_tot_2_wk += use_time
                                elif start_time.hour == 22:
                                    contact_hour_22_cnt_2_wk += 1
                                    contact_hour_22_min_tot_2_wk += use_time
                                elif start_time.hour == 23:
                                    contact_hour_23_cnt_2_wk += 1
                                    contact_hour_23_min_tot_2_wk += use_time

                                if u'主' in init_type or '主' in init_type:
                                    if start_time.hour == 0:
                                        contact_hour_0_call_cnt_2_wk += 1
                                        contact_hour_0_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 1:
                                        contact_hour_1_call_cnt_2_wk += 1
                                        contact_hour_1_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 2:
                                        contact_hour_2_call_cnt_2_wk += 1
                                        contact_hour_2_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 3:
                                        contact_hour_3_call_cnt_2_wk += 1
                                        contact_hour_3_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 4:
                                        contact_hour_4_call_cnt_2_wk += 1
                                        contact_hour_4_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 5:
                                        contact_hour_5_call_cnt_2_wk += 1
                                        contact_hour_5_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 6:
                                        contact_hour_6_call_cnt_2_wk += 1
                                        contact_hour_6_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 7:
                                        contact_hour_7_call_cnt_2_wk += 1
                                        contact_hour_7_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 8:
                                        contact_hour_8_call_cnt_2_wk += 1
                                        contact_hour_8_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 9:
                                        contact_hour_9_call_cnt_2_wk += 1
                                        contact_hour_9_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 10:
                                        contact_hour_10_call_cnt_2_wk += 1
                                        contact_hour_10_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 11:
                                        contact_hour_11_call_cnt_2_wk += 1
                                        contact_hour_11_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 12:
                                        contact_hour_12_call_cnt_2_wk += 1
                                        contact_hour_12_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 13:
                                        contact_hour_13_call_cnt_2_wk += 1
                                        contact_hour_13_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 14:
                                        contact_hour_14_call_cnt_2_wk += 1
                                        contact_hour_14_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 15:
                                        contact_hour_15_call_cnt_2_wk += 1
                                        contact_hour_15_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 16:
                                        contact_hour_16_call_cnt_2_wk += 1
                                        contact_hour_16_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 17:
                                        contact_hour_17_call_cnt_2_wk += 1
                                        contact_hour_17_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 18:
                                        contact_hour_18_call_cnt_2_wk += 1
                                        contact_hour_18_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 19:
                                        contact_hour_19_call_cnt_2_wk += 1
                                        contact_hour_19_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 20:
                                        contact_hour_20_call_cnt_2_wk += 1
                                        contact_hour_20_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 21:
                                        contact_hour_21_call_cnt_2_wk += 1
                                        contact_hour_21_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 22:
                                        contact_hour_22_call_cnt_2_wk += 1
                                        contact_hour_22_call_min_tot_2_wk += use_time
                                    elif start_time.hour == 23:
                                        contact_hour_23_call_cnt_2_wk += 1
                                        contact_hour_23_call_min_tot_2_wk += use_time
                                elif u'被' in init_type or '被' in init_type:
                                    if start_time.hour == 0:
                                        contact_hour_0_rece_cnt_2_wk += 1
                                        contact_hour_0_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 1:
                                        contact_hour_1_rece_cnt_2_wk += 1
                                        contact_hour_1_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 2:
                                        contact_hour_2_rece_cnt_2_wk += 1
                                        contact_hour_2_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 3:
                                        contact_hour_3_rece_cnt_2_wk += 1
                                        contact_hour_3_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 4:
                                        contact_hour_4_rece_cnt_2_wk += 1
                                        contact_hour_4_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 5:
                                        contact_hour_5_rece_cnt_2_wk += 1
                                        contact_hour_5_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 6:
                                        contact_hour_6_rece_cnt_2_wk += 1
                                        contact_hour_6_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 7:
                                        contact_hour_7_rece_cnt_2_wk += 1
                                        contact_hour_7_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 8:
                                        contact_hour_8_rece_cnt_2_wk += 1
                                        contact_hour_8_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 9:
                                        contact_hour_9_rece_cnt_2_wk += 1
                                        contact_hour_9_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 10:
                                        contact_hour_10_rece_cnt_2_wk += 1
                                        contact_hour_10_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 11:
                                        contact_hour_11_rece_cnt_2_wk += 1
                                        contact_hour_11_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 12:
                                        contact_hour_12_rece_cnt_2_wk += 1
                                        contact_hour_12_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 13:
                                        contact_hour_13_rece_cnt_2_wk += 1
                                        contact_hour_13_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 14:
                                        contact_hour_14_rece_cnt_2_wk += 1
                                        contact_hour_14_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 15:
                                        contact_hour_15_rece_cnt_2_wk += 1
                                        contact_hour_15_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 16:
                                        contact_hour_16_rece_cnt_2_wk += 1
                                        contact_hour_16_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 17:
                                        contact_hour_17_rece_cnt_2_wk += 1
                                        contact_hour_17_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 18:
                                        contact_hour_18_rece_cnt_2_wk += 1
                                        contact_hour_18_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 19:
                                        contact_hour_19_rece_cnt_2_wk += 1
                                        contact_hour_19_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 20:
                                        contact_hour_20_rece_cnt_2_wk += 1
                                        contact_hour_20_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 21:
                                        contact_hour_21_rece_cnt_2_wk += 1
                                        contact_hour_21_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 22:
                                        contact_hour_22_rece_cnt_2_wk += 1
                                        contact_hour_22_rece_min_tot_2_wk += use_time
                                    elif start_time.hour == 23:
                                        contact_hour_23_rece_cnt_2_wk += 1
                                        contact_hour_23_rece_min_tot_2_wk += use_time

                                if start_time.weekday() in (0, 1, 2, 3, 4):
                                    # 0,1,2,3,4 对应星期一、二、三、四、五
                                    contact_weekday_cnt_2_wk += 1
                                    contact_weekday_min_tot_2_wk += use_time
                                    if u'主' in init_type or '主' in init_type:
                                        contact_weekday_call_cnt_2_wk += 1
                                        contact_weekday_call_min_tot_2_wk += use_time
                                    elif u'被' in init_type or '被' in init_type:
                                        contact_weekday_rece_cnt_2_wk += 1
                                        contact_weekday_rece_min_tot_2_wk += use_time
                                elif start_time.weekday() in (5, 6):
                                    # 5,6 对应星期六、星期天
                                    contact_weekend_cnt_2_wk += 1
                                    contact_weekend_min_tot_2_wk += use_time
                                    if u'主' in init_type or '主' in init_type:
                                        contact_weekend_call_cnt_2_wk += 1
                                        contact_weekend_call_min_tot_2_wk += use_time
                                    elif u'被' in init_type or '被' in init_type:
                                        contact_weekend_rece_cnt_2_wk += 1
                                        contact_weekend_rece_min_tot_2_wk += use_time

                                if use_time >= 15:
                                    contact_min_over_15s_cnt_2_wk += 1
                                    contact_min_over_15s_min_tot_2_wk += use_time
                                    if u'主' in init_type or '主' in init_type:
                                        contact_min_over_15s_call_cnt_2_wk += 1
                                        contact_min_over_15s_call_min_tot_2_wk += use_time
                                    elif u'被' in init_type or '被' in init_type:
                                        contact_min_over_15s_rece_cnt_2_wk += 1
                                        contact_min_over_15s_rece_min_tot_2_wk += use_time

                                if use_time >= 30:
                                    contact_min_over_30s_cnt_2_wk += 1
                                    contact_min_over_30s_min_tot_2_wk += use_time
                                    if u'主' in init_type or '主' in init_type:
                                        contact_min_over_30s_call_cnt_2_wk += 1
                                        contact_min_over_30s_call_min_tot_2_wk += use_time
                                    elif u'被' in init_type or '被' in init_type:
                                        contact_min_over_30s_rece_cnt_2_wk += 1
                                        contact_min_over_30s_rece_min_tot_2_wk += use_time

                                if use_time >= 60:
                                    contact_min_over_60s_cnt_2_wk += 1
                                    contact_min_over_60s_min_tot_2_wk += use_time
                                    if u'主' in init_type or '主' in init_type:
                                        contact_min_over_60s_call_cnt_2_wk += 1
                                        contact_min_over_60s_call_min_tot_2_wk += use_time
                                    elif u'被' in init_type or '被' in init_type:
                                        contact_min_over_60s_rece_cnt_2_wk += 1
                                        contact_min_over_60s_rece_min_tot_2_wk += use_time

        contact_hour_0to1_cnt = contact_hour_0_cnt + contact_hour_1_cnt
        contact_hour_2to3_cnt = contact_hour_2_cnt + contact_hour_3_cnt
        contact_hour_4to5_cnt = contact_hour_4_cnt + contact_hour_5_cnt
        contact_hour_6to7_cnt = contact_hour_6_cnt + contact_hour_7_cnt
        contact_hour_8to9_cnt = contact_hour_8_cnt + contact_hour_9_cnt
        contact_hour_10to11_cnt = contact_hour_10_cnt + contact_hour_11_cnt
        contact_hour_12to13_cnt = contact_hour_12_cnt + contact_hour_13_cnt
        contact_hour_14to15_cnt = contact_hour_14_cnt + contact_hour_15_cnt
        contact_hour_16to17_cnt = contact_hour_16_cnt + contact_hour_17_cnt
        contact_hour_18to19_cnt = contact_hour_18_cnt + contact_hour_19_cnt
        contact_hour_20to21_cnt = contact_hour_20_cnt + contact_hour_21_cnt
        contact_hour_22to23_cnt = contact_hour_22_cnt + contact_hour_23_cnt

        contact_hour_0to1_min_tot = contact_hour_0_min_tot + contact_hour_1_min_tot
        contact_hour_2to3_min_tot = contact_hour_2_min_tot + contact_hour_3_min_tot
        contact_hour_4to5_min_tot = contact_hour_4_min_tot + contact_hour_5_min_tot
        contact_hour_6to7_min_tot = contact_hour_6_min_tot + contact_hour_7_min_tot
        contact_hour_8to9_min_tot = contact_hour_8_min_tot + contact_hour_9_min_tot
        contact_hour_10to11_min_tot = contact_hour_10_min_tot + contact_hour_11_min_tot
        contact_hour_12to13_min_tot = contact_hour_12_min_tot + contact_hour_13_min_tot
        contact_hour_14to15_min_tot = contact_hour_14_min_tot + contact_hour_15_min_tot
        contact_hour_16to17_min_tot = contact_hour_16_min_tot + contact_hour_17_min_tot
        contact_hour_18to19_min_tot = contact_hour_18_min_tot + contact_hour_19_min_tot
        contact_hour_20to21_min_tot = contact_hour_20_min_tot + contact_hour_21_min_tot
        contact_hour_22to23_min_tot = contact_hour_22_min_tot + contact_hour_23_min_tot

        contact_hour_0to1_cnt_6_mon = contact_hour_0_cnt_6_mon + contact_hour_1_cnt_6_mon
        contact_hour_2to3_cnt_6_mon = contact_hour_2_cnt_6_mon + contact_hour_3_cnt_6_mon
        contact_hour_4to5_cnt_6_mon = contact_hour_4_cnt_6_mon + contact_hour_5_cnt_6_mon
        contact_hour_6to7_cnt_6_mon = contact_hour_6_cnt_6_mon + contact_hour_7_cnt_6_mon
        contact_hour_8to9_cnt_6_mon = contact_hour_8_cnt_6_mon + contact_hour_9_cnt_6_mon
        contact_hour_10to11_cnt_6_mon = contact_hour_10_cnt_6_mon + contact_hour_11_cnt_6_mon
        contact_hour_12to13_cnt_6_mon = contact_hour_12_cnt_6_mon + contact_hour_13_cnt_6_mon
        contact_hour_14to15_cnt_6_mon = contact_hour_14_cnt_6_mon + contact_hour_15_cnt_6_mon
        contact_hour_16to17_cnt_6_mon = contact_hour_16_cnt_6_mon + contact_hour_17_cnt_6_mon
        contact_hour_18to19_cnt_6_mon = contact_hour_18_cnt_6_mon + contact_hour_19_cnt_6_mon
        contact_hour_20to21_cnt_6_mon = contact_hour_20_cnt_6_mon + contact_hour_21_cnt_6_mon
        contact_hour_22to23_cnt_6_mon = contact_hour_22_cnt_6_mon + contact_hour_23_cnt_6_mon

        contact_hour_0to1_min_tot_6_mon = contact_hour_0_min_tot_6_mon + contact_hour_1_min_tot_6_mon
        contact_hour_2to3_min_tot_6_mon = contact_hour_2_min_tot_6_mon + contact_hour_3_min_tot_6_mon
        contact_hour_4to5_min_tot_6_mon = contact_hour_4_min_tot_6_mon + contact_hour_5_min_tot_6_mon
        contact_hour_6to7_min_tot_6_mon = contact_hour_6_min_tot_6_mon + contact_hour_7_min_tot_6_mon
        contact_hour_8to9_min_tot_6_mon = contact_hour_8_min_tot_6_mon + contact_hour_9_min_tot_6_mon
        contact_hour_10to11_min_tot_6_mon = contact_hour_10_min_tot_6_mon + contact_hour_11_min_tot_6_mon
        contact_hour_12to13_min_tot_6_mon = contact_hour_12_min_tot_6_mon + contact_hour_13_min_tot_6_mon
        contact_hour_14to15_min_tot_6_mon = contact_hour_14_min_tot_6_mon + contact_hour_15_min_tot_6_mon
        contact_hour_16to17_min_tot_6_mon = contact_hour_16_min_tot_6_mon + contact_hour_17_min_tot_6_mon
        contact_hour_18to19_min_tot_6_mon = contact_hour_18_min_tot_6_mon + contact_hour_19_min_tot_6_mon
        contact_hour_20to21_min_tot_6_mon = contact_hour_20_min_tot_6_mon + contact_hour_21_min_tot_6_mon
        contact_hour_22to23_min_tot_6_mon = contact_hour_22_min_tot_6_mon + contact_hour_23_min_tot_6_mon

        contact_hour_0to1_cnt_3_mon = contact_hour_0_cnt_3_mon + contact_hour_1_cnt_3_mon
        contact_hour_2to3_cnt_3_mon = contact_hour_2_cnt_3_mon + contact_hour_3_cnt_3_mon
        contact_hour_4to5_cnt_3_mon = contact_hour_4_cnt_3_mon + contact_hour_5_cnt_3_mon
        contact_hour_6to7_cnt_3_mon = contact_hour_6_cnt_3_mon + contact_hour_7_cnt_3_mon
        contact_hour_8to9_cnt_3_mon = contact_hour_8_cnt_3_mon + contact_hour_9_cnt_3_mon
        contact_hour_10to11_cnt_3_mon = contact_hour_10_cnt_3_mon + contact_hour_11_cnt_3_mon
        contact_hour_12to13_cnt_3_mon = contact_hour_12_cnt_3_mon + contact_hour_13_cnt_3_mon
        contact_hour_14to15_cnt_3_mon = contact_hour_14_cnt_3_mon + contact_hour_15_cnt_3_mon
        contact_hour_16to17_cnt_3_mon = contact_hour_16_cnt_3_mon + contact_hour_17_cnt_3_mon
        contact_hour_18to19_cnt_3_mon = contact_hour_18_cnt_3_mon + contact_hour_19_cnt_3_mon
        contact_hour_20to21_cnt_3_mon = contact_hour_20_cnt_3_mon + contact_hour_21_cnt_3_mon
        contact_hour_22to23_cnt_3_mon = contact_hour_22_cnt_3_mon + contact_hour_23_cnt_3_mon

        contact_hour_0to1_min_tot_3_mon = contact_hour_0_min_tot_3_mon + contact_hour_1_min_tot_3_mon
        contact_hour_2to3_min_tot_3_mon = contact_hour_2_min_tot_3_mon + contact_hour_3_min_tot_3_mon
        contact_hour_4to5_min_tot_3_mon = contact_hour_4_min_tot_3_mon + contact_hour_5_min_tot_3_mon
        contact_hour_6to7_min_tot_3_mon = contact_hour_6_min_tot_3_mon + contact_hour_7_min_tot_3_mon
        contact_hour_8to9_min_tot_3_mon = contact_hour_8_min_tot_3_mon + contact_hour_9_min_tot_3_mon
        contact_hour_10to11_min_tot_3_mon = contact_hour_10_min_tot_3_mon + contact_hour_11_min_tot_3_mon
        contact_hour_12to13_min_tot_3_mon = contact_hour_12_min_tot_3_mon + contact_hour_13_min_tot_3_mon
        contact_hour_14to15_min_tot_3_mon = contact_hour_14_min_tot_3_mon + contact_hour_15_min_tot_3_mon
        contact_hour_16to17_min_tot_3_mon = contact_hour_16_min_tot_3_mon + contact_hour_17_min_tot_3_mon
        contact_hour_18to19_min_tot_3_mon = contact_hour_18_min_tot_3_mon + contact_hour_19_min_tot_3_mon
        contact_hour_20to21_min_tot_3_mon = contact_hour_20_min_tot_3_mon + contact_hour_21_min_tot_3_mon
        contact_hour_22to23_min_tot_3_mon = contact_hour_22_min_tot_3_mon + contact_hour_23_min_tot_3_mon

        contact_hour_0to1_cnt_2_mon = contact_hour_0_cnt_2_mon + contact_hour_1_cnt_2_mon
        contact_hour_2to3_cnt_2_mon = contact_hour_2_cnt_2_mon + contact_hour_3_cnt_2_mon
        contact_hour_4to5_cnt_2_mon = contact_hour_4_cnt_2_mon + contact_hour_5_cnt_2_mon
        contact_hour_6to7_cnt_2_mon = contact_hour_6_cnt_2_mon + contact_hour_7_cnt_2_mon
        contact_hour_8to9_cnt_2_mon = contact_hour_8_cnt_2_mon + contact_hour_9_cnt_2_mon
        contact_hour_10to11_cnt_2_mon = contact_hour_10_cnt_2_mon + contact_hour_11_cnt_2_mon
        contact_hour_12to13_cnt_2_mon = contact_hour_12_cnt_2_mon + contact_hour_13_cnt_2_mon
        contact_hour_14to15_cnt_2_mon = contact_hour_14_cnt_2_mon + contact_hour_15_cnt_2_mon
        contact_hour_16to17_cnt_2_mon = contact_hour_16_cnt_2_mon + contact_hour_17_cnt_2_mon
        contact_hour_18to19_cnt_2_mon = contact_hour_18_cnt_2_mon + contact_hour_19_cnt_2_mon
        contact_hour_20to21_cnt_2_mon = contact_hour_20_cnt_2_mon + contact_hour_21_cnt_2_mon
        contact_hour_22to23_cnt_2_mon = contact_hour_22_cnt_2_mon + contact_hour_23_cnt_2_mon

        contact_hour_0to1_min_tot_2_mon = contact_hour_0_min_tot_2_mon + contact_hour_1_min_tot_2_mon
        contact_hour_2to3_min_tot_2_mon = contact_hour_2_min_tot_2_mon + contact_hour_3_min_tot_2_mon
        contact_hour_4to5_min_tot_2_mon = contact_hour_4_min_tot_2_mon + contact_hour_5_min_tot_2_mon
        contact_hour_6to7_min_tot_2_mon = contact_hour_6_min_tot_2_mon + contact_hour_7_min_tot_2_mon
        contact_hour_8to9_min_tot_2_mon = contact_hour_8_min_tot_2_mon + contact_hour_9_min_tot_2_mon
        contact_hour_10to11_min_tot_2_mon = contact_hour_10_min_tot_2_mon + contact_hour_11_min_tot_2_mon
        contact_hour_12to13_min_tot_2_mon = contact_hour_12_min_tot_2_mon + contact_hour_13_min_tot_2_mon
        contact_hour_14to15_min_tot_2_mon = contact_hour_14_min_tot_2_mon + contact_hour_15_min_tot_2_mon
        contact_hour_16to17_min_tot_2_mon = contact_hour_16_min_tot_2_mon + contact_hour_17_min_tot_2_mon
        contact_hour_18to19_min_tot_2_mon = contact_hour_18_min_tot_2_mon + contact_hour_19_min_tot_2_mon
        contact_hour_20to21_min_tot_2_mon = contact_hour_20_min_tot_2_mon + contact_hour_21_min_tot_2_mon
        contact_hour_22to23_min_tot_2_mon = contact_hour_22_min_tot_2_mon + contact_hour_23_min_tot_2_mon

        contact_hour_0to1_cnt_1_mon = contact_hour_0_cnt_1_mon + contact_hour_1_cnt_1_mon
        contact_hour_2to3_cnt_1_mon = contact_hour_2_cnt_1_mon + contact_hour_3_cnt_1_mon
        contact_hour_4to5_cnt_1_mon = contact_hour_4_cnt_1_mon + contact_hour_5_cnt_1_mon
        contact_hour_6to7_cnt_1_mon = contact_hour_6_cnt_1_mon + contact_hour_7_cnt_1_mon
        contact_hour_8to9_cnt_1_mon = contact_hour_8_cnt_1_mon + contact_hour_9_cnt_1_mon
        contact_hour_10to11_cnt_1_mon = contact_hour_10_cnt_1_mon + contact_hour_11_cnt_1_mon
        contact_hour_12to13_cnt_1_mon = contact_hour_12_cnt_1_mon + contact_hour_13_cnt_1_mon
        contact_hour_14to15_cnt_1_mon = contact_hour_14_cnt_1_mon + contact_hour_15_cnt_1_mon
        contact_hour_16to17_cnt_1_mon = contact_hour_16_cnt_1_mon + contact_hour_17_cnt_1_mon
        contact_hour_18to19_cnt_1_mon = contact_hour_18_cnt_1_mon + contact_hour_19_cnt_1_mon
        contact_hour_20to21_cnt_1_mon = contact_hour_20_cnt_1_mon + contact_hour_21_cnt_1_mon
        contact_hour_22to23_cnt_1_mon = contact_hour_22_cnt_1_mon + contact_hour_23_cnt_1_mon

        contact_hour_0to1_min_tot_1_mon = contact_hour_0_min_tot_1_mon + contact_hour_1_min_tot_1_mon
        contact_hour_2to3_min_tot_1_mon = contact_hour_2_min_tot_1_mon + contact_hour_3_min_tot_1_mon
        contact_hour_4to5_min_tot_1_mon = contact_hour_4_min_tot_1_mon + contact_hour_5_min_tot_1_mon
        contact_hour_6to7_min_tot_1_mon = contact_hour_6_min_tot_1_mon + contact_hour_7_min_tot_1_mon
        contact_hour_8to9_min_tot_1_mon = contact_hour_8_min_tot_1_mon + contact_hour_9_min_tot_1_mon
        contact_hour_10to11_min_tot_1_mon = contact_hour_10_min_tot_1_mon + contact_hour_11_min_tot_1_mon
        contact_hour_12to13_min_tot_1_mon = contact_hour_12_min_tot_1_mon + contact_hour_13_min_tot_1_mon
        contact_hour_14to15_min_tot_1_mon = contact_hour_14_min_tot_1_mon + contact_hour_15_min_tot_1_mon
        contact_hour_16to17_min_tot_1_mon = contact_hour_16_min_tot_1_mon + contact_hour_17_min_tot_1_mon
        contact_hour_18to19_min_tot_1_mon = contact_hour_18_min_tot_1_mon + contact_hour_19_min_tot_1_mon
        contact_hour_20to21_min_tot_1_mon = contact_hour_20_min_tot_1_mon + contact_hour_21_min_tot_1_mon
        contact_hour_22to23_min_tot_1_mon = contact_hour_22_min_tot_1_mon + contact_hour_23_min_tot_1_mon

        contact_hour_0to1_cnt_2_wk = contact_hour_0_cnt_2_wk + contact_hour_1_cnt_2_wk
        contact_hour_2to3_cnt_2_wk = contact_hour_2_cnt_2_wk + contact_hour_3_cnt_2_wk
        contact_hour_4to5_cnt_2_wk = contact_hour_4_cnt_2_wk + contact_hour_5_cnt_2_wk
        contact_hour_6to7_cnt_2_wk = contact_hour_6_cnt_2_wk + contact_hour_7_cnt_2_wk
        contact_hour_8to9_cnt_2_wk = contact_hour_8_cnt_2_wk + contact_hour_9_cnt_2_wk
        contact_hour_10to11_cnt_2_wk = contact_hour_10_cnt_2_wk + contact_hour_11_cnt_2_wk
        contact_hour_12to13_cnt_2_wk = contact_hour_12_cnt_2_wk + contact_hour_13_cnt_2_wk
        contact_hour_14to15_cnt_2_wk = contact_hour_14_cnt_2_wk + contact_hour_15_cnt_2_wk
        contact_hour_16to17_cnt_2_wk = contact_hour_16_cnt_2_wk + contact_hour_17_cnt_2_wk
        contact_hour_18to19_cnt_2_wk = contact_hour_18_cnt_2_wk + contact_hour_19_cnt_2_wk
        contact_hour_20to21_cnt_2_wk = contact_hour_20_cnt_2_wk + contact_hour_21_cnt_2_wk
        contact_hour_22to23_cnt_2_wk = contact_hour_22_cnt_2_wk + contact_hour_23_cnt_2_wk

        contact_hour_0to1_min_tot_2_wk = contact_hour_0_min_tot_2_wk + contact_hour_1_min_tot_2_wk
        contact_hour_2to3_min_tot_2_wk = contact_hour_2_min_tot_2_wk + contact_hour_3_min_tot_2_wk
        contact_hour_4to5_min_tot_2_wk = contact_hour_4_min_tot_2_wk + contact_hour_5_min_tot_2_wk
        contact_hour_6to7_min_tot_2_wk = contact_hour_6_min_tot_2_wk + contact_hour_7_min_tot_2_wk
        contact_hour_8to9_min_tot_2_wk = contact_hour_8_min_tot_2_wk + contact_hour_9_min_tot_2_wk
        contact_hour_10to11_min_tot_2_wk = contact_hour_10_min_tot_2_wk + contact_hour_11_min_tot_2_wk
        contact_hour_12to13_min_tot_2_wk = contact_hour_12_min_tot_2_wk + contact_hour_13_min_tot_2_wk
        contact_hour_14to15_min_tot_2_wk = contact_hour_14_min_tot_2_wk + contact_hour_15_min_tot_2_wk
        contact_hour_16to17_min_tot_2_wk = contact_hour_16_min_tot_2_wk + contact_hour_17_min_tot_2_wk
        contact_hour_18to19_min_tot_2_wk = contact_hour_18_min_tot_2_wk + contact_hour_19_min_tot_2_wk
        contact_hour_20to21_min_tot_2_wk = contact_hour_20_min_tot_2_wk + contact_hour_21_min_tot_2_wk
        contact_hour_22to23_min_tot_2_wk = contact_hour_22_min_tot_2_wk + contact_hour_23_min_tot_2_wk

        contact_hour_1to6_cnt = contact_hour_1_cnt + contact_hour_2_cnt + contact_hour_3_cnt + contact_hour_4_cnt + contact_hour_5_cnt + contact_hour_6_cnt
        contact_hour_7to12_cnt = contact_hour_7_cnt + contact_hour_8_cnt + contact_hour_9_cnt + contact_hour_10_cnt + contact_hour_11_cnt + contact_hour_12_cnt
        contact_hour_13to18_cnt = contact_hour_13_cnt + contact_hour_14_cnt + contact_hour_15_cnt + contact_hour_16_cnt + contact_hour_17_cnt + contact_hour_18_cnt
        contact_hour_19to0_cnt = contact_hour_19_cnt + contact_hour_20_cnt + contact_hour_21_cnt + contact_hour_22_cnt + contact_hour_23_cnt + contact_hour_0_cnt

        contact_hour_1to6_min_tot = contact_hour_1_min_tot + contact_hour_2_min_tot + contact_hour_3_min_tot + contact_hour_4_min_tot + contact_hour_5_min_tot + contact_hour_6_min_tot
        contact_hour_7to12_min_tot = contact_hour_7_min_tot + contact_hour_8_min_tot + contact_hour_9_min_tot + contact_hour_10_min_tot + contact_hour_11_min_tot + contact_hour_12_min_tot
        contact_hour_13to18_min_tot = contact_hour_13_min_tot + contact_hour_14_min_tot + contact_hour_15_min_tot + contact_hour_16_min_tot + contact_hour_17_min_tot + contact_hour_18_min_tot
        contact_hour_19to0_min_tot = contact_hour_19_min_tot + contact_hour_20_min_tot + contact_hour_21_min_tot + contact_hour_22_min_tot + contact_hour_23_min_tot + contact_hour_0_min_tot

        contact_hour_1to6_cnt_6_mon = contact_hour_1_cnt_6_mon + contact_hour_2_cnt_6_mon + contact_hour_3_cnt_6_mon + contact_hour_4_cnt_6_mon + contact_hour_5_cnt_6_mon + contact_hour_6_cnt_6_mon
        contact_hour_7to12_cnt_6_mon = contact_hour_7_cnt_6_mon + contact_hour_8_cnt_6_mon + contact_hour_9_cnt_6_mon + contact_hour_10_cnt_6_mon + contact_hour_11_cnt_6_mon + contact_hour_12_cnt_6_mon
        contact_hour_13to18_cnt_6_mon = contact_hour_13_cnt_6_mon + contact_hour_14_cnt_6_mon + contact_hour_15_cnt_6_mon + contact_hour_16_cnt_6_mon + contact_hour_17_cnt_6_mon + contact_hour_18_cnt_6_mon
        contact_hour_19to0_cnt_6_mon = contact_hour_19_cnt_6_mon + contact_hour_20_cnt_6_mon + contact_hour_21_cnt_6_mon + contact_hour_22_cnt_6_mon + contact_hour_23_cnt_6_mon + contact_hour_0_cnt_6_mon

        contact_hour_1to6_min_tot_6_mon = contact_hour_1_min_tot_6_mon + contact_hour_2_min_tot_6_mon + contact_hour_3_min_tot_6_mon + contact_hour_4_min_tot_6_mon + contact_hour_5_min_tot_6_mon + contact_hour_6_min_tot_6_mon
        contact_hour_7to12_min_tot_6_mon = contact_hour_7_min_tot_6_mon + contact_hour_8_min_tot_6_mon + contact_hour_9_min_tot_6_mon + contact_hour_10_min_tot_6_mon + contact_hour_11_min_tot_6_mon + contact_hour_12_min_tot_6_mon
        contact_hour_13to18_min_tot_6_mon = contact_hour_13_min_tot_6_mon + contact_hour_14_min_tot_6_mon + contact_hour_15_min_tot_6_mon + contact_hour_16_min_tot_6_mon + contact_hour_17_min_tot_6_mon + contact_hour_18_min_tot_6_mon
        contact_hour_19to0_min_tot_6_mon = contact_hour_19_min_tot_6_mon + contact_hour_20_min_tot_6_mon + contact_hour_21_min_tot_6_mon + contact_hour_22_min_tot_6_mon + contact_hour_23_min_tot_6_mon + contact_hour_0_min_tot_6_mon

        contact_hour_1to6_cnt_3_mon = contact_hour_1_cnt_3_mon + contact_hour_2_cnt_3_mon + contact_hour_3_cnt_3_mon + contact_hour_4_cnt_3_mon + contact_hour_5_cnt_3_mon + contact_hour_6_cnt_3_mon
        contact_hour_7to12_cnt_3_mon = contact_hour_7_cnt_3_mon + contact_hour_8_cnt_3_mon + contact_hour_9_cnt_3_mon + contact_hour_10_cnt_3_mon + contact_hour_11_cnt_3_mon + contact_hour_12_cnt_3_mon
        contact_hour_13to18_cnt_3_mon = contact_hour_13_cnt_3_mon + contact_hour_14_cnt_3_mon + contact_hour_15_cnt_3_mon + contact_hour_16_cnt_3_mon + contact_hour_17_cnt_3_mon + contact_hour_18_cnt_3_mon
        contact_hour_19to0_cnt_3_mon = contact_hour_19_cnt_3_mon + contact_hour_20_cnt_3_mon + contact_hour_21_cnt_3_mon + contact_hour_22_cnt_3_mon + contact_hour_23_cnt_3_mon + contact_hour_0_cnt_3_mon

        contact_hour_1to6_min_tot_3_mon = contact_hour_1_min_tot_3_mon + contact_hour_2_min_tot_3_mon + contact_hour_3_min_tot_3_mon + contact_hour_4_min_tot_3_mon + contact_hour_5_min_tot_3_mon + contact_hour_6_min_tot_3_mon
        contact_hour_7to12_min_tot_3_mon = contact_hour_7_min_tot_3_mon + contact_hour_8_min_tot_3_mon + contact_hour_9_min_tot_3_mon + contact_hour_10_min_tot_3_mon + contact_hour_11_min_tot_3_mon + contact_hour_12_min_tot_3_mon
        contact_hour_13to18_min_tot_3_mon = contact_hour_13_min_tot_3_mon + contact_hour_14_min_tot_3_mon + contact_hour_15_min_tot_3_mon + contact_hour_16_min_tot_3_mon + contact_hour_17_min_tot_3_mon + contact_hour_18_min_tot_3_mon
        contact_hour_19to0_min_tot_3_mon = contact_hour_19_min_tot_3_mon + contact_hour_20_min_tot_3_mon + contact_hour_21_min_tot_3_mon + contact_hour_22_min_tot_3_mon + contact_hour_23_min_tot_3_mon + contact_hour_0_min_tot_3_mon

        contact_hour_1to6_cnt_2_mon = contact_hour_1_cnt_2_mon + contact_hour_2_cnt_2_mon + contact_hour_3_cnt_2_mon + contact_hour_4_cnt_2_mon + contact_hour_5_cnt_2_mon + contact_hour_6_cnt_2_mon
        contact_hour_7to12_cnt_2_mon = contact_hour_7_cnt_2_mon + contact_hour_8_cnt_2_mon + contact_hour_9_cnt_2_mon + contact_hour_10_cnt_2_mon + contact_hour_11_cnt_2_mon + contact_hour_12_cnt_2_mon
        contact_hour_13to18_cnt_2_mon = contact_hour_13_cnt_2_mon + contact_hour_14_cnt_2_mon + contact_hour_15_cnt_2_mon + contact_hour_16_cnt_2_mon + contact_hour_17_cnt_2_mon + contact_hour_18_cnt_2_mon
        contact_hour_19to0_cnt_2_mon = contact_hour_19_cnt_2_mon + contact_hour_20_cnt_2_mon + contact_hour_21_cnt_2_mon + contact_hour_22_cnt_2_mon + contact_hour_23_cnt_2_mon + contact_hour_0_cnt_2_mon

        contact_hour_1to6_min_tot_2_mon = contact_hour_1_min_tot_2_mon + contact_hour_2_min_tot_2_mon + contact_hour_3_min_tot_2_mon + contact_hour_4_min_tot_2_mon + contact_hour_5_min_tot_2_mon + contact_hour_6_min_tot_2_mon
        contact_hour_7to12_min_tot_2_mon = contact_hour_7_min_tot_2_mon + contact_hour_8_min_tot_2_mon + contact_hour_9_min_tot_2_mon + contact_hour_10_min_tot_2_mon + contact_hour_11_min_tot_2_mon + contact_hour_12_min_tot_2_mon
        contact_hour_13to18_min_tot_2_mon = contact_hour_13_min_tot_2_mon + contact_hour_14_min_tot_2_mon + contact_hour_15_min_tot_2_mon + contact_hour_16_min_tot_2_mon + contact_hour_17_min_tot_2_mon + contact_hour_18_min_tot_2_mon
        contact_hour_19to0_min_tot_2_mon = contact_hour_19_min_tot_2_mon + contact_hour_20_min_tot_2_mon + contact_hour_21_min_tot_2_mon + contact_hour_22_min_tot_2_mon + contact_hour_23_min_tot_2_mon + contact_hour_0_min_tot_2_mon

        contact_hour_1to6_cnt_1_mon = contact_hour_1_cnt_1_mon + contact_hour_2_cnt_1_mon + contact_hour_3_cnt_1_mon + contact_hour_4_cnt_1_mon + contact_hour_5_cnt_1_mon + contact_hour_6_cnt_1_mon
        contact_hour_7to12_cnt_1_mon = contact_hour_7_cnt_1_mon + contact_hour_8_cnt_1_mon + contact_hour_9_cnt_1_mon + contact_hour_10_cnt_1_mon + contact_hour_11_cnt_1_mon + contact_hour_12_cnt_1_mon
        contact_hour_13to18_cnt_1_mon = contact_hour_13_cnt_1_mon + contact_hour_14_cnt_1_mon + contact_hour_15_cnt_1_mon + contact_hour_16_cnt_1_mon + contact_hour_17_cnt_1_mon + contact_hour_18_cnt_1_mon
        contact_hour_19to0_cnt_1_mon = contact_hour_19_cnt_1_mon + contact_hour_20_cnt_1_mon + contact_hour_21_cnt_1_mon + contact_hour_22_cnt_1_mon + contact_hour_23_cnt_1_mon + contact_hour_0_cnt_1_mon

        contact_hour_1to6_min_tot_1_mon = contact_hour_1_min_tot_1_mon + contact_hour_2_min_tot_1_mon + contact_hour_3_min_tot_1_mon + contact_hour_4_min_tot_1_mon + contact_hour_5_min_tot_1_mon + contact_hour_6_min_tot_1_mon
        contact_hour_7to12_min_tot_1_mon = contact_hour_7_min_tot_1_mon + contact_hour_8_min_tot_1_mon + contact_hour_9_min_tot_1_mon + contact_hour_10_min_tot_1_mon + contact_hour_11_min_tot_1_mon + contact_hour_12_min_tot_1_mon
        contact_hour_13to18_min_tot_1_mon = contact_hour_13_min_tot_1_mon + contact_hour_14_min_tot_1_mon + contact_hour_15_min_tot_1_mon + contact_hour_16_min_tot_1_mon + contact_hour_17_min_tot_1_mon + contact_hour_18_min_tot_1_mon
        contact_hour_19to0_min_tot_1_mon = contact_hour_19_min_tot_1_mon + contact_hour_20_min_tot_1_mon + contact_hour_21_min_tot_1_mon + contact_hour_22_min_tot_1_mon + contact_hour_23_min_tot_1_mon + contact_hour_0_min_tot_1_mon

        contact_hour_1to6_cnt_2_wk = contact_hour_1_cnt_2_wk + contact_hour_2_cnt_2_wk + contact_hour_3_cnt_2_wk + contact_hour_4_cnt_2_wk + contact_hour_5_cnt_2_wk + contact_hour_6_cnt_2_wk
        contact_hour_7to12_cnt_2_wk = contact_hour_7_cnt_2_wk + contact_hour_8_cnt_2_wk + contact_hour_9_cnt_2_wk + contact_hour_10_cnt_2_wk + contact_hour_11_cnt_2_wk + contact_hour_12_cnt_2_wk
        contact_hour_13to18_cnt_2_wk = contact_hour_13_cnt_2_wk + contact_hour_14_cnt_2_wk + contact_hour_15_cnt_2_wk + contact_hour_16_cnt_2_wk + contact_hour_17_cnt_2_wk + contact_hour_18_cnt_2_wk
        contact_hour_19to0_cnt_2_wk = contact_hour_19_cnt_2_wk + contact_hour_20_cnt_2_wk + contact_hour_21_cnt_2_wk + contact_hour_22_cnt_2_wk + contact_hour_23_cnt_2_wk + contact_hour_0_cnt_2_wk

        contact_hour_1to6_min_tot_2_wk = contact_hour_1_min_tot_2_wk + contact_hour_2_min_tot_2_wk + contact_hour_3_min_tot_2_wk + contact_hour_4_min_tot_2_wk + contact_hour_5_min_tot_2_wk + contact_hour_6_min_tot_2_wk
        contact_hour_7to12_min_tot_2_wk = contact_hour_7_min_tot_2_wk + contact_hour_8_min_tot_2_wk + contact_hour_9_min_tot_2_wk + contact_hour_10_min_tot_2_wk + contact_hour_11_min_tot_2_wk + contact_hour_12_min_tot_2_wk
        contact_hour_13to18_min_tot_2_wk = contact_hour_13_min_tot_2_wk + contact_hour_14_min_tot_2_wk + contact_hour_15_min_tot_2_wk + contact_hour_16_min_tot_2_wk + contact_hour_17_min_tot_2_wk + contact_hour_18_min_tot_2_wk
        contact_hour_19to0_min_tot_2_wk = contact_hour_19_min_tot_2_wk + contact_hour_20_min_tot_2_wk + contact_hour_21_min_tot_2_wk + contact_hour_22_min_tot_2_wk + contact_hour_23_min_tot_2_wk + contact_hour_0_min_tot_2_wk

        contact_hour_1to8_cnt = contact_hour_1_cnt + contact_hour_2_cnt + contact_hour_3_cnt + contact_hour_4_cnt + contact_hour_5_cnt + contact_hour_6_cnt + contact_hour_7_cnt + contact_hour_8_cnt
        contact_hour_9to16_cnt = contact_hour_9_cnt + contact_hour_10_cnt + contact_hour_11_cnt + contact_hour_12_cnt + contact_hour_13_cnt + contact_hour_14_cnt + contact_hour_15_cnt + contact_hour_16_cnt
        contact_hour_17to0_cnt = contact_hour_17_cnt + contact_hour_18_cnt + contact_hour_19_cnt + contact_hour_20_cnt + contact_hour_21_cnt + contact_hour_22_cnt + contact_hour_23_cnt + contact_hour_0_cnt

        contact_hour_1to8_min_tot = contact_hour_1_min_tot + contact_hour_2_min_tot + contact_hour_3_min_tot + contact_hour_4_min_tot + contact_hour_5_min_tot + contact_hour_6_min_tot + contact_hour_7_min_tot + contact_hour_8_min_tot
        contact_hour_9to16_min_tot = contact_hour_9_min_tot + contact_hour_10_min_tot + contact_hour_11_min_tot + contact_hour_12_min_tot + contact_hour_13_min_tot + contact_hour_14_min_tot + contact_hour_15_min_tot + contact_hour_16_min_tot
        contact_hour_17to0_min_tot = contact_hour_17_min_tot + contact_hour_18_min_tot + contact_hour_19_min_tot + contact_hour_20_min_tot + contact_hour_21_min_tot + contact_hour_22_min_tot + contact_hour_23_min_tot + contact_hour_0_min_tot

        contact_hour_1to8_cnt_6_mon = contact_hour_1_cnt_6_mon + contact_hour_2_cnt_6_mon + contact_hour_3_cnt_6_mon + contact_hour_4_cnt_6_mon + contact_hour_5_cnt_6_mon + contact_hour_6_cnt_6_mon + contact_hour_7_cnt_6_mon + contact_hour_8_cnt_6_mon
        contact_hour_9to16_cnt_6_mon = contact_hour_9_cnt_6_mon + contact_hour_10_cnt_6_mon + contact_hour_11_cnt_6_mon + contact_hour_12_cnt_6_mon + contact_hour_13_cnt_6_mon + contact_hour_14_cnt_6_mon + contact_hour_15_cnt_6_mon + contact_hour_16_cnt_6_mon
        contact_hour_17to0_cnt_6_mon = contact_hour_17_cnt_6_mon + contact_hour_18_cnt_6_mon + contact_hour_19_cnt_6_mon + contact_hour_20_cnt_6_mon + contact_hour_21_cnt_6_mon + contact_hour_22_cnt_6_mon + contact_hour_23_cnt_6_mon + contact_hour_0_cnt_6_mon

        contact_hour_1to8_min_tot_6_mon = contact_hour_1_min_tot_6_mon + contact_hour_2_min_tot_6_mon + contact_hour_3_min_tot_6_mon + contact_hour_4_min_tot_6_mon + contact_hour_5_min_tot_6_mon + contact_hour_6_min_tot_6_mon + contact_hour_7_min_tot_6_mon + contact_hour_8_min_tot_6_mon
        contact_hour_9to16_min_tot_6_mon = contact_hour_9_min_tot_6_mon + contact_hour_10_min_tot_6_mon + contact_hour_11_min_tot_6_mon + contact_hour_12_min_tot_6_mon + contact_hour_13_min_tot_6_mon + contact_hour_14_min_tot_6_mon + contact_hour_15_min_tot_6_mon + contact_hour_16_min_tot_6_mon
        contact_hour_17to0_min_tot_6_mon = contact_hour_17_min_tot_6_mon + contact_hour_18_min_tot_6_mon + contact_hour_19_min_tot_6_mon + contact_hour_20_min_tot_6_mon + contact_hour_21_min_tot_6_mon + contact_hour_22_min_tot_6_mon + contact_hour_23_min_tot_6_mon + contact_hour_0_min_tot_6_mon

        contact_hour_1to8_cnt_3_mon = contact_hour_1_cnt_3_mon + contact_hour_2_cnt_3_mon + contact_hour_3_cnt_3_mon + contact_hour_4_cnt_3_mon + contact_hour_5_cnt_3_mon + contact_hour_6_cnt_3_mon + contact_hour_7_cnt_3_mon + contact_hour_8_cnt_3_mon
        contact_hour_9to16_cnt_3_mon = contact_hour_9_cnt_3_mon + contact_hour_10_cnt_3_mon + contact_hour_11_cnt_3_mon + contact_hour_12_cnt_3_mon + contact_hour_13_cnt_3_mon + contact_hour_14_cnt_3_mon + contact_hour_15_cnt_3_mon + contact_hour_16_cnt_3_mon
        contact_hour_17to0_cnt_3_mon = contact_hour_17_cnt_3_mon + contact_hour_18_cnt_3_mon + contact_hour_19_cnt_3_mon + contact_hour_20_cnt_3_mon + contact_hour_21_cnt_3_mon + contact_hour_22_cnt_3_mon + contact_hour_23_cnt_3_mon + contact_hour_0_cnt_3_mon

        contact_hour_1to8_min_tot_3_mon = contact_hour_1_min_tot_3_mon + contact_hour_2_min_tot_3_mon + contact_hour_3_min_tot_3_mon + contact_hour_4_min_tot_3_mon + contact_hour_5_min_tot_3_mon + contact_hour_6_min_tot_3_mon + contact_hour_7_min_tot_3_mon + contact_hour_8_min_tot_3_mon
        contact_hour_9to16_min_tot_3_mon = contact_hour_9_min_tot_3_mon + contact_hour_10_min_tot_3_mon + contact_hour_11_min_tot_3_mon + contact_hour_12_min_tot_3_mon + contact_hour_13_min_tot_3_mon + contact_hour_14_min_tot_3_mon + contact_hour_15_min_tot_3_mon + contact_hour_16_min_tot_3_mon
        contact_hour_17to0_min_tot_3_mon = contact_hour_17_min_tot_3_mon + contact_hour_18_min_tot_3_mon + contact_hour_19_min_tot_3_mon + contact_hour_20_min_tot_3_mon + contact_hour_21_min_tot_3_mon + contact_hour_22_min_tot_3_mon + contact_hour_23_min_tot_3_mon + contact_hour_0_min_tot_3_mon

        contact_hour_1to8_cnt_2_mon = contact_hour_1_cnt_2_mon + contact_hour_2_cnt_2_mon + contact_hour_3_cnt_2_mon + contact_hour_4_cnt_2_mon + contact_hour_5_cnt_2_mon + contact_hour_6_cnt_2_mon + contact_hour_7_cnt_2_mon + contact_hour_8_cnt_2_mon
        contact_hour_9to16_cnt_2_mon = contact_hour_9_cnt_2_mon + contact_hour_10_cnt_2_mon + contact_hour_11_cnt_2_mon + contact_hour_12_cnt_2_mon + contact_hour_13_cnt_2_mon + contact_hour_14_cnt_2_mon + contact_hour_15_cnt_2_mon + contact_hour_16_cnt_2_mon
        contact_hour_17to0_cnt_2_mon = contact_hour_17_cnt_2_mon + contact_hour_18_cnt_2_mon + contact_hour_19_cnt_2_mon + contact_hour_20_cnt_2_mon + contact_hour_21_cnt_2_mon + contact_hour_22_cnt_2_mon + contact_hour_23_cnt_2_mon + contact_hour_0_cnt_2_mon

        contact_hour_1to8_min_tot_2_mon = contact_hour_1_min_tot_2_mon + contact_hour_2_min_tot_2_mon + contact_hour_3_min_tot_2_mon + contact_hour_4_min_tot_2_mon + contact_hour_5_min_tot_2_mon + contact_hour_6_min_tot_2_mon + contact_hour_7_min_tot_2_mon + contact_hour_8_min_tot_2_mon
        contact_hour_9to16_min_tot_2_mon = contact_hour_9_min_tot_2_mon + contact_hour_10_min_tot_2_mon + contact_hour_11_min_tot_2_mon + contact_hour_12_min_tot_2_mon + contact_hour_13_min_tot_2_mon + contact_hour_14_min_tot_2_mon + contact_hour_15_min_tot_2_mon + contact_hour_16_min_tot_2_mon
        contact_hour_17to0_min_tot_2_mon = contact_hour_17_min_tot_2_mon + contact_hour_18_min_tot_2_mon + contact_hour_19_min_tot_2_mon + contact_hour_20_min_tot_2_mon + contact_hour_21_min_tot_2_mon + contact_hour_22_min_tot_2_mon + contact_hour_23_min_tot_2_mon + contact_hour_0_min_tot_2_mon

        contact_hour_1to8_cnt_1_mon = contact_hour_1_cnt_1_mon + contact_hour_2_cnt_1_mon + contact_hour_3_cnt_1_mon + contact_hour_4_cnt_1_mon + contact_hour_5_cnt_1_mon + contact_hour_6_cnt_1_mon + contact_hour_7_cnt_1_mon + contact_hour_8_cnt_1_mon
        contact_hour_9to16_cnt_1_mon = contact_hour_9_cnt_1_mon + contact_hour_10_cnt_1_mon + contact_hour_11_cnt_1_mon + contact_hour_12_cnt_1_mon + contact_hour_13_cnt_1_mon + contact_hour_14_cnt_1_mon + contact_hour_15_cnt_1_mon + contact_hour_16_cnt_1_mon
        contact_hour_17to0_cnt_1_mon = contact_hour_17_cnt_1_mon + contact_hour_18_cnt_1_mon + contact_hour_19_cnt_1_mon + contact_hour_20_cnt_1_mon + contact_hour_21_cnt_1_mon + contact_hour_22_cnt_1_mon + contact_hour_23_cnt_1_mon + contact_hour_0_cnt_1_mon

        contact_hour_1to8_min_tot_1_mon = contact_hour_1_min_tot_1_mon + contact_hour_2_min_tot_1_mon + contact_hour_3_min_tot_1_mon + contact_hour_4_min_tot_1_mon + contact_hour_5_min_tot_1_mon + contact_hour_6_min_tot_1_mon + contact_hour_7_min_tot_1_mon + contact_hour_8_min_tot_1_mon
        contact_hour_9to16_min_tot_1_mon = contact_hour_9_min_tot_1_mon + contact_hour_10_min_tot_1_mon + contact_hour_11_min_tot_1_mon + contact_hour_12_min_tot_1_mon + contact_hour_13_min_tot_1_mon + contact_hour_14_min_tot_1_mon + contact_hour_15_min_tot_1_mon + contact_hour_16_min_tot_1_mon
        contact_hour_17to0_min_tot_1_mon = contact_hour_17_min_tot_1_mon + contact_hour_18_min_tot_1_mon + contact_hour_19_min_tot_1_mon + contact_hour_20_min_tot_1_mon + contact_hour_21_min_tot_1_mon + contact_hour_22_min_tot_1_mon + contact_hour_23_min_tot_1_mon + contact_hour_0_min_tot_1_mon

        contact_hour_1to8_cnt_2_wk = contact_hour_1_cnt_2_wk + contact_hour_2_cnt_2_wk + contact_hour_3_cnt_2_wk + contact_hour_4_cnt_2_wk + contact_hour_5_cnt_2_wk + contact_hour_6_cnt_2_wk + contact_hour_7_cnt_2_wk + contact_hour_8_cnt_2_wk
        contact_hour_9to16_cnt_2_wk = contact_hour_9_cnt_2_wk + contact_hour_10_cnt_2_wk + contact_hour_11_cnt_2_wk + contact_hour_12_cnt_2_wk + contact_hour_13_cnt_2_wk + contact_hour_14_cnt_2_wk + contact_hour_15_cnt_2_wk + contact_hour_16_cnt_2_wk
        contact_hour_17to0_cnt_2_wk = contact_hour_17_cnt_2_wk + contact_hour_18_cnt_2_wk + contact_hour_19_cnt_2_wk + contact_hour_20_cnt_2_wk + contact_hour_21_cnt_2_wk + contact_hour_22_cnt_2_wk + contact_hour_23_cnt_2_wk + contact_hour_0_cnt_2_wk

        contact_hour_1to8_min_tot_2_wk = contact_hour_1_min_tot_2_wk + contact_hour_2_min_tot_2_wk + contact_hour_3_min_tot_2_wk + contact_hour_4_min_tot_2_wk + contact_hour_5_min_tot_2_wk + contact_hour_6_min_tot_2_wk + contact_hour_7_min_tot_2_wk + contact_hour_8_min_tot_2_wk
        contact_hour_9to16_min_tot_2_wk = contact_hour_9_min_tot_2_wk + contact_hour_10_min_tot_2_wk + contact_hour_11_min_tot_2_wk + contact_hour_12_min_tot_2_wk + contact_hour_13_min_tot_2_wk + contact_hour_14_min_tot_2_wk + contact_hour_15_min_tot_2_wk + contact_hour_16_min_tot_2_wk
        contact_hour_17to0_min_tot_2_wk = contact_hour_17_min_tot_2_wk + contact_hour_18_min_tot_2_wk + contact_hour_19_min_tot_2_wk + contact_hour_20_min_tot_2_wk + contact_hour_21_min_tot_2_wk + contact_hour_22_min_tot_2_wk + contact_hour_23_min_tot_2_wk + contact_hour_0_min_tot_2_wk

        contact_hour_9to20_cnt = contact_hour_9_cnt + contact_hour_10_cnt + contact_hour_11_cnt + contact_hour_12_cnt + contact_hour_13_cnt + contact_hour_14_cnt + contact_hour_15_cnt + contact_hour_16_cnt + contact_hour_17_cnt + contact_hour_18_cnt + contact_hour_19_cnt + contact_hour_20_cnt
        contact_hour_21to8_cnt = contact_hour_21_cnt + contact_hour_22_cnt + contact_hour_23_cnt + contact_hour_0_cnt + contact_hour_1_cnt + contact_hour_2_cnt + contact_hour_3_cnt + contact_hour_4_cnt + contact_hour_5_cnt + contact_hour_6_cnt + contact_hour_7_cnt + contact_hour_8_cnt

        contact_hour_9to20_min_tot = contact_hour_9_min_tot + contact_hour_10_min_tot + contact_hour_11_min_tot + contact_hour_12_min_tot + contact_hour_13_min_tot + contact_hour_14_min_tot + contact_hour_15_min_tot + contact_hour_16_min_tot + contact_hour_17_min_tot + contact_hour_18_min_tot + contact_hour_19_min_tot + contact_hour_20_min_tot
        contact_hour_21to8_min_tot = contact_hour_21_min_tot + contact_hour_22_min_tot + contact_hour_23_min_tot + contact_hour_0_min_tot + contact_hour_1_min_tot + contact_hour_2_min_tot + contact_hour_3_min_tot + contact_hour_4_min_tot + contact_hour_5_min_tot + contact_hour_6_min_tot + contact_hour_7_min_tot + contact_hour_8_min_tot

        contact_hour_9to20_cnt_6_mon = contact_hour_9_cnt_6_mon + contact_hour_10_cnt_6_mon + contact_hour_11_cnt_6_mon + contact_hour_12_cnt_6_mon + contact_hour_13_cnt_6_mon + contact_hour_14_cnt_6_mon + contact_hour_15_cnt_6_mon + contact_hour_16_cnt_6_mon + contact_hour_17_cnt_6_mon + contact_hour_18_cnt_6_mon + contact_hour_19_cnt_6_mon + contact_hour_20_cnt_6_mon
        contact_hour_21to8_cnt_6_mon = contact_hour_21_cnt_6_mon + contact_hour_22_cnt_6_mon + contact_hour_23_cnt_6_mon + contact_hour_0_cnt_6_mon + contact_hour_1_cnt_6_mon + contact_hour_2_cnt_6_mon + contact_hour_3_cnt_6_mon + contact_hour_4_cnt_6_mon + contact_hour_5_cnt_6_mon + contact_hour_6_cnt_6_mon + contact_hour_7_cnt_6_mon + contact_hour_8_cnt_6_mon

        contact_hour_9to20_min_tot_6_mon = contact_hour_9_min_tot_6_mon + contact_hour_10_min_tot_6_mon + contact_hour_11_min_tot_6_mon + contact_hour_12_min_tot_6_mon + contact_hour_13_min_tot_6_mon + contact_hour_14_min_tot_6_mon + contact_hour_15_min_tot_6_mon + contact_hour_16_min_tot_6_mon + contact_hour_17_min_tot_6_mon + contact_hour_18_min_tot_6_mon + contact_hour_19_min_tot_6_mon + contact_hour_20_min_tot_6_mon
        contact_hour_21to8_min_tot_6_mon = contact_hour_21_min_tot_6_mon + contact_hour_22_min_tot_6_mon + contact_hour_23_min_tot_6_mon + contact_hour_0_min_tot_6_mon + contact_hour_1_min_tot_6_mon + contact_hour_2_min_tot_6_mon + contact_hour_3_min_tot_6_mon + contact_hour_4_min_tot_6_mon + contact_hour_5_min_tot_6_mon + contact_hour_6_min_tot_6_mon + contact_hour_7_min_tot_6_mon + contact_hour_8_min_tot_6_mon

        contact_hour_9to20_cnt_3_mon = contact_hour_9_cnt_3_mon + contact_hour_10_cnt_3_mon + contact_hour_11_cnt_3_mon + contact_hour_12_cnt_3_mon + contact_hour_13_cnt_3_mon + contact_hour_14_cnt_3_mon + contact_hour_15_cnt_3_mon + contact_hour_16_cnt_3_mon + contact_hour_17_cnt_3_mon + contact_hour_18_cnt_3_mon + contact_hour_19_cnt_3_mon + contact_hour_20_cnt_3_mon
        contact_hour_21to8_cnt_3_mon = contact_hour_21_cnt_3_mon + contact_hour_22_cnt_3_mon + contact_hour_23_cnt_3_mon + contact_hour_0_cnt_3_mon + contact_hour_1_cnt_3_mon + contact_hour_2_cnt_3_mon + contact_hour_3_cnt_3_mon + contact_hour_4_cnt_3_mon + contact_hour_5_cnt_3_mon + contact_hour_6_cnt_3_mon + contact_hour_7_cnt_3_mon + contact_hour_8_cnt_3_mon

        contact_hour_9to20_min_tot_3_mon = contact_hour_9_min_tot_3_mon + contact_hour_10_min_tot_3_mon + contact_hour_11_min_tot_3_mon + contact_hour_12_min_tot_3_mon + contact_hour_13_min_tot_3_mon + contact_hour_14_min_tot_3_mon + contact_hour_15_min_tot_3_mon + contact_hour_16_min_tot_3_mon + contact_hour_17_min_tot_3_mon + contact_hour_18_min_tot_3_mon + contact_hour_19_min_tot_3_mon + contact_hour_20_min_tot_3_mon
        contact_hour_21to8_min_tot_3_mon = contact_hour_21_min_tot_3_mon + contact_hour_22_min_tot_3_mon + contact_hour_23_min_tot_3_mon + contact_hour_0_min_tot_3_mon + contact_hour_1_min_tot_3_mon + contact_hour_2_min_tot_3_mon + contact_hour_3_min_tot_3_mon + contact_hour_4_min_tot_3_mon + contact_hour_5_min_tot_3_mon + contact_hour_6_min_tot_3_mon + contact_hour_7_min_tot_3_mon + contact_hour_8_min_tot_3_mon

        contact_hour_9to20_cnt_2_mon = contact_hour_9_cnt_2_mon + contact_hour_10_cnt_2_mon + contact_hour_11_cnt_2_mon + contact_hour_12_cnt_2_mon + contact_hour_13_cnt_2_mon + contact_hour_14_cnt_2_mon + contact_hour_15_cnt_2_mon + contact_hour_16_cnt_2_mon + contact_hour_17_cnt_2_mon + contact_hour_18_cnt_2_mon + contact_hour_19_cnt_2_mon + contact_hour_20_cnt_2_mon
        contact_hour_21to8_cnt_2_mon = contact_hour_21_cnt_2_mon + contact_hour_22_cnt_2_mon + contact_hour_23_cnt_2_mon + contact_hour_0_cnt_2_mon + contact_hour_1_cnt_2_mon + contact_hour_2_cnt_2_mon + contact_hour_3_cnt_2_mon + contact_hour_4_cnt_2_mon + contact_hour_5_cnt_2_mon + contact_hour_6_cnt_2_mon + contact_hour_7_cnt_2_mon + contact_hour_8_cnt_2_mon

        contact_hour_9to20_min_tot_2_mon = contact_hour_9_min_tot_2_mon + contact_hour_10_min_tot_2_mon + contact_hour_11_min_tot_2_mon + contact_hour_12_min_tot_2_mon + contact_hour_13_min_tot_2_mon + contact_hour_14_min_tot_2_mon + contact_hour_15_min_tot_2_mon + contact_hour_16_min_tot_2_mon + contact_hour_17_min_tot_2_mon + contact_hour_18_min_tot_2_mon + contact_hour_19_min_tot_2_mon + contact_hour_20_min_tot_2_mon
        contact_hour_21to8_min_tot_2_mon = contact_hour_21_min_tot_2_mon + contact_hour_22_min_tot_2_mon + contact_hour_23_min_tot_2_mon + contact_hour_0_min_tot_2_mon + contact_hour_1_min_tot_2_mon + contact_hour_2_min_tot_2_mon + contact_hour_3_min_tot_2_mon + contact_hour_4_min_tot_2_mon + contact_hour_5_min_tot_2_mon + contact_hour_6_min_tot_2_mon + contact_hour_7_min_tot_2_mon + contact_hour_8_min_tot_2_mon

        contact_hour_9to20_cnt_1_mon = contact_hour_9_cnt_1_mon + contact_hour_10_cnt_1_mon + contact_hour_11_cnt_1_mon + contact_hour_12_cnt_1_mon + contact_hour_13_cnt_1_mon + contact_hour_14_cnt_1_mon + contact_hour_15_cnt_1_mon + contact_hour_16_cnt_1_mon + contact_hour_17_cnt_1_mon + contact_hour_18_cnt_1_mon + contact_hour_19_cnt_1_mon + contact_hour_20_cnt_1_mon
        contact_hour_21to8_cnt_1_mon = contact_hour_21_cnt_1_mon + contact_hour_22_cnt_1_mon + contact_hour_23_cnt_1_mon + contact_hour_0_cnt_1_mon + contact_hour_1_cnt_1_mon + contact_hour_2_cnt_1_mon + contact_hour_3_cnt_1_mon + contact_hour_4_cnt_1_mon + contact_hour_5_cnt_1_mon + contact_hour_6_cnt_1_mon + contact_hour_7_cnt_1_mon + contact_hour_8_cnt_1_mon

        contact_hour_9to20_min_tot_1_mon = contact_hour_9_min_tot_1_mon + contact_hour_10_min_tot_1_mon + contact_hour_11_min_tot_1_mon + contact_hour_12_min_tot_1_mon + contact_hour_13_min_tot_1_mon + contact_hour_14_min_tot_1_mon + contact_hour_15_min_tot_1_mon + contact_hour_16_min_tot_1_mon + contact_hour_17_min_tot_1_mon + contact_hour_18_min_tot_1_mon + contact_hour_19_min_tot_1_mon + contact_hour_20_min_tot_1_mon
        contact_hour_21to8_min_tot_1_mon = contact_hour_21_min_tot_1_mon + contact_hour_22_min_tot_1_mon + contact_hour_23_min_tot_1_mon + contact_hour_0_min_tot_1_mon + contact_hour_1_min_tot_1_mon + contact_hour_2_min_tot_1_mon + contact_hour_3_min_tot_1_mon + contact_hour_4_min_tot_1_mon + contact_hour_5_min_tot_1_mon + contact_hour_6_min_tot_1_mon + contact_hour_7_min_tot_1_mon + contact_hour_8_min_tot_1_mon

        contact_hour_9to20_cnt_2_wk = contact_hour_9_cnt_2_wk + contact_hour_10_cnt_2_wk + contact_hour_11_cnt_2_wk + contact_hour_12_cnt_2_wk + contact_hour_13_cnt_2_wk + contact_hour_14_cnt_2_wk + contact_hour_15_cnt_2_wk + contact_hour_16_cnt_2_wk + contact_hour_17_cnt_2_wk + contact_hour_18_cnt_2_wk + contact_hour_19_cnt_2_wk + contact_hour_20_cnt_2_wk
        contact_hour_21to8_cnt_2_wk = contact_hour_21_cnt_2_wk + contact_hour_22_cnt_2_wk + contact_hour_23_cnt_2_wk + contact_hour_0_cnt_2_wk + contact_hour_1_cnt_2_wk + contact_hour_2_cnt_2_wk + contact_hour_3_cnt_2_wk + contact_hour_4_cnt_2_wk + contact_hour_5_cnt_2_wk + contact_hour_6_cnt_2_wk + contact_hour_7_cnt_2_wk + contact_hour_8_cnt_2_wk

        contact_hour_9to20_min_tot_2_wk = contact_hour_9_min_tot_2_wk + contact_hour_10_min_tot_2_wk + contact_hour_11_min_tot_2_wk + contact_hour_12_min_tot_2_wk + contact_hour_13_min_tot_2_wk + contact_hour_14_min_tot_2_wk + contact_hour_15_min_tot_2_wk + contact_hour_16_min_tot_2_wk + contact_hour_17_min_tot_2_wk + contact_hour_18_min_tot_2_wk + contact_hour_19_min_tot_2_wk + contact_hour_20_min_tot_2_wk
        contact_hour_21to8_min_tot_2_wk = contact_hour_21_min_tot_2_wk + contact_hour_22_min_tot_2_wk + contact_hour_23_min_tot_2_wk + contact_hour_0_min_tot_2_wk + contact_hour_1_min_tot_2_wk + contact_hour_2_min_tot_2_wk + contact_hour_3_min_tot_2_wk + contact_hour_4_min_tot_2_wk + contact_hour_5_min_tot_2_wk + contact_hour_6_min_tot_2_wk + contact_hour_7_min_tot_2_wk + contact_hour_8_min_tot_2_wk

        contact_hour_0to1_call_cnt = contact_hour_0_call_cnt + contact_hour_1_call_cnt
        contact_hour_2to3_call_cnt = contact_hour_2_call_cnt + contact_hour_3_call_cnt
        contact_hour_4to5_call_cnt = contact_hour_4_call_cnt + contact_hour_5_call_cnt
        contact_hour_6to7_call_cnt = contact_hour_6_call_cnt + contact_hour_7_call_cnt
        contact_hour_8to9_call_cnt = contact_hour_8_call_cnt + contact_hour_9_call_cnt
        contact_hour_10to11_call_cnt = contact_hour_10_call_cnt + contact_hour_11_call_cnt
        contact_hour_12to13_call_cnt = contact_hour_12_call_cnt + contact_hour_13_call_cnt
        contact_hour_14to15_call_cnt = contact_hour_14_call_cnt + contact_hour_15_call_cnt
        contact_hour_16to17_call_cnt = contact_hour_16_call_cnt + contact_hour_17_call_cnt
        contact_hour_18to19_call_cnt = contact_hour_18_call_cnt + contact_hour_19_call_cnt
        contact_hour_20to21_call_cnt = contact_hour_20_call_cnt + contact_hour_21_call_cnt
        contact_hour_22to23_call_cnt = contact_hour_22_call_cnt + contact_hour_23_call_cnt

        contact_hour_0to1_call_min_tot = contact_hour_0_call_min_tot + contact_hour_1_call_min_tot
        contact_hour_2to3_call_min_tot = contact_hour_2_call_min_tot + contact_hour_3_call_min_tot
        contact_hour_4to5_call_min_tot = contact_hour_4_call_min_tot + contact_hour_5_call_min_tot
        contact_hour_6to7_call_min_tot = contact_hour_6_call_min_tot + contact_hour_7_call_min_tot
        contact_hour_8to9_call_min_tot = contact_hour_8_call_min_tot + contact_hour_9_call_min_tot
        contact_hour_10to11_call_min_tot = contact_hour_10_call_min_tot + contact_hour_11_call_min_tot
        contact_hour_12to13_call_min_tot = contact_hour_12_call_min_tot + contact_hour_13_call_min_tot
        contact_hour_14to15_call_min_tot = contact_hour_14_call_min_tot + contact_hour_15_call_min_tot
        contact_hour_16to17_call_min_tot = contact_hour_16_call_min_tot + contact_hour_17_call_min_tot
        contact_hour_18to19_call_min_tot = contact_hour_18_call_min_tot + contact_hour_19_call_min_tot
        contact_hour_20to21_call_min_tot = contact_hour_20_call_min_tot + contact_hour_21_call_min_tot
        contact_hour_22to23_call_min_tot = contact_hour_22_call_min_tot + contact_hour_23_call_min_tot

        contact_hour_0to1_call_cnt_6_mon = contact_hour_0_call_cnt_6_mon + contact_hour_1_call_cnt_6_mon
        contact_hour_2to3_call_cnt_6_mon = contact_hour_2_call_cnt_6_mon + contact_hour_3_call_cnt_6_mon
        contact_hour_4to5_call_cnt_6_mon = contact_hour_4_call_cnt_6_mon + contact_hour_5_call_cnt_6_mon
        contact_hour_6to7_call_cnt_6_mon = contact_hour_6_call_cnt_6_mon + contact_hour_7_call_cnt_6_mon
        contact_hour_8to9_call_cnt_6_mon = contact_hour_8_call_cnt_6_mon + contact_hour_9_call_cnt_6_mon
        contact_hour_10to11_call_cnt_6_mon = contact_hour_10_call_cnt_6_mon + contact_hour_11_call_cnt_6_mon
        contact_hour_12to13_call_cnt_6_mon = contact_hour_12_call_cnt_6_mon + contact_hour_13_call_cnt_6_mon
        contact_hour_14to15_call_cnt_6_mon = contact_hour_14_call_cnt_6_mon + contact_hour_15_call_cnt_6_mon
        contact_hour_16to17_call_cnt_6_mon = contact_hour_16_call_cnt_6_mon + contact_hour_17_call_cnt_6_mon
        contact_hour_18to19_call_cnt_6_mon = contact_hour_18_call_cnt_6_mon + contact_hour_19_call_cnt_6_mon
        contact_hour_20to21_call_cnt_6_mon = contact_hour_20_call_cnt_6_mon + contact_hour_21_call_cnt_6_mon
        contact_hour_22to23_call_cnt_6_mon = contact_hour_22_call_cnt_6_mon + contact_hour_23_call_cnt_6_mon

        contact_hour_0to1_call_min_tot_6_mon = contact_hour_0_call_min_tot_6_mon + contact_hour_1_call_min_tot_6_mon
        contact_hour_2to3_call_min_tot_6_mon = contact_hour_2_call_min_tot_6_mon + contact_hour_3_call_min_tot_6_mon
        contact_hour_4to5_call_min_tot_6_mon = contact_hour_4_call_min_tot_6_mon + contact_hour_5_call_min_tot_6_mon
        contact_hour_6to7_call_min_tot_6_mon = contact_hour_6_call_min_tot_6_mon + contact_hour_7_call_min_tot_6_mon
        contact_hour_8to9_call_min_tot_6_mon = contact_hour_8_call_min_tot_6_mon + contact_hour_9_call_min_tot_6_mon
        contact_hour_10to11_call_min_tot_6_mon = contact_hour_10_call_min_tot_6_mon + contact_hour_11_call_min_tot_6_mon
        contact_hour_12to13_call_min_tot_6_mon = contact_hour_12_call_min_tot_6_mon + contact_hour_13_call_min_tot_6_mon
        contact_hour_14to15_call_min_tot_6_mon = contact_hour_14_call_min_tot_6_mon + contact_hour_15_call_min_tot_6_mon
        contact_hour_16to17_call_min_tot_6_mon = contact_hour_16_call_min_tot_6_mon + contact_hour_17_call_min_tot_6_mon
        contact_hour_18to19_call_min_tot_6_mon = contact_hour_18_call_min_tot_6_mon + contact_hour_19_call_min_tot_6_mon
        contact_hour_20to21_call_min_tot_6_mon = contact_hour_20_call_min_tot_6_mon + contact_hour_21_call_min_tot_6_mon
        contact_hour_22to23_call_min_tot_6_mon = contact_hour_22_call_min_tot_6_mon + contact_hour_23_call_min_tot_6_mon

        contact_hour_0to1_call_cnt_3_mon = contact_hour_0_call_cnt_3_mon + contact_hour_1_call_cnt_3_mon
        contact_hour_2to3_call_cnt_3_mon = contact_hour_2_call_cnt_3_mon + contact_hour_3_call_cnt_3_mon
        contact_hour_4to5_call_cnt_3_mon = contact_hour_4_call_cnt_3_mon + contact_hour_5_call_cnt_3_mon
        contact_hour_6to7_call_cnt_3_mon = contact_hour_6_call_cnt_3_mon + contact_hour_7_call_cnt_3_mon
        contact_hour_8to9_call_cnt_3_mon = contact_hour_8_call_cnt_3_mon + contact_hour_9_call_cnt_3_mon
        contact_hour_10to11_call_cnt_3_mon = contact_hour_10_call_cnt_3_mon + contact_hour_11_call_cnt_3_mon
        contact_hour_12to13_call_cnt_3_mon = contact_hour_12_call_cnt_3_mon + contact_hour_13_call_cnt_3_mon
        contact_hour_14to15_call_cnt_3_mon = contact_hour_14_call_cnt_3_mon + contact_hour_15_call_cnt_3_mon
        contact_hour_16to17_call_cnt_3_mon = contact_hour_16_call_cnt_3_mon + contact_hour_17_call_cnt_3_mon
        contact_hour_18to19_call_cnt_3_mon = contact_hour_18_call_cnt_3_mon + contact_hour_19_call_cnt_3_mon
        contact_hour_20to21_call_cnt_3_mon = contact_hour_20_call_cnt_3_mon + contact_hour_21_call_cnt_3_mon
        contact_hour_22to23_call_cnt_3_mon = contact_hour_22_call_cnt_3_mon + contact_hour_23_call_cnt_3_mon

        contact_hour_0to1_call_min_tot_3_mon = contact_hour_0_call_min_tot_3_mon + contact_hour_1_call_min_tot_3_mon
        contact_hour_2to3_call_min_tot_3_mon = contact_hour_2_call_min_tot_3_mon + contact_hour_3_call_min_tot_3_mon
        contact_hour_4to5_call_min_tot_3_mon = contact_hour_4_call_min_tot_3_mon + contact_hour_5_call_min_tot_3_mon
        contact_hour_6to7_call_min_tot_3_mon = contact_hour_6_call_min_tot_3_mon + contact_hour_7_call_min_tot_3_mon
        contact_hour_8to9_call_min_tot_3_mon = contact_hour_8_call_min_tot_3_mon + contact_hour_9_call_min_tot_3_mon
        contact_hour_10to11_call_min_tot_3_mon = contact_hour_10_call_min_tot_3_mon + contact_hour_11_call_min_tot_3_mon
        contact_hour_12to13_call_min_tot_3_mon = contact_hour_12_call_min_tot_3_mon + contact_hour_13_call_min_tot_3_mon
        contact_hour_14to15_call_min_tot_3_mon = contact_hour_14_call_min_tot_3_mon + contact_hour_15_call_min_tot_3_mon
        contact_hour_16to17_call_min_tot_3_mon = contact_hour_16_call_min_tot_3_mon + contact_hour_17_call_min_tot_3_mon
        contact_hour_18to19_call_min_tot_3_mon = contact_hour_18_call_min_tot_3_mon + contact_hour_19_call_min_tot_3_mon
        contact_hour_20to21_call_min_tot_3_mon = contact_hour_20_call_min_tot_3_mon + contact_hour_21_call_min_tot_3_mon
        contact_hour_22to23_call_min_tot_3_mon = contact_hour_22_call_min_tot_3_mon + contact_hour_23_call_min_tot_3_mon

        contact_hour_0to1_call_cnt_2_mon = contact_hour_0_call_cnt_2_mon + contact_hour_1_call_cnt_2_mon
        contact_hour_2to3_call_cnt_2_mon = contact_hour_2_call_cnt_2_mon + contact_hour_3_call_cnt_2_mon
        contact_hour_4to5_call_cnt_2_mon = contact_hour_4_call_cnt_2_mon + contact_hour_5_call_cnt_2_mon
        contact_hour_6to7_call_cnt_2_mon = contact_hour_6_call_cnt_2_mon + contact_hour_7_call_cnt_2_mon
        contact_hour_8to9_call_cnt_2_mon = contact_hour_8_call_cnt_2_mon + contact_hour_9_call_cnt_2_mon
        contact_hour_10to11_call_cnt_2_mon = contact_hour_10_call_cnt_2_mon + contact_hour_11_call_cnt_2_mon
        contact_hour_12to13_call_cnt_2_mon = contact_hour_12_call_cnt_2_mon + contact_hour_13_call_cnt_2_mon
        contact_hour_14to15_call_cnt_2_mon = contact_hour_14_call_cnt_2_mon + contact_hour_15_call_cnt_2_mon
        contact_hour_16to17_call_cnt_2_mon = contact_hour_16_call_cnt_2_mon + contact_hour_17_call_cnt_2_mon
        contact_hour_18to19_call_cnt_2_mon = contact_hour_18_call_cnt_2_mon + contact_hour_19_call_cnt_2_mon
        contact_hour_20to21_call_cnt_2_mon = contact_hour_20_call_cnt_2_mon + contact_hour_21_call_cnt_2_mon
        contact_hour_22to23_call_cnt_2_mon = contact_hour_22_call_cnt_2_mon + contact_hour_23_call_cnt_2_mon

        contact_hour_0to1_call_min_tot_2_mon = contact_hour_0_call_min_tot_2_mon + contact_hour_1_call_min_tot_2_mon
        contact_hour_2to3_call_min_tot_2_mon = contact_hour_2_call_min_tot_2_mon + contact_hour_3_call_min_tot_2_mon
        contact_hour_4to5_call_min_tot_2_mon = contact_hour_4_call_min_tot_2_mon + contact_hour_5_call_min_tot_2_mon
        contact_hour_6to7_call_min_tot_2_mon = contact_hour_6_call_min_tot_2_mon + contact_hour_7_call_min_tot_2_mon
        contact_hour_8to9_call_min_tot_2_mon = contact_hour_8_call_min_tot_2_mon + contact_hour_9_call_min_tot_2_mon
        contact_hour_10to11_call_min_tot_2_mon = contact_hour_10_call_min_tot_2_mon + contact_hour_11_call_min_tot_2_mon
        contact_hour_12to13_call_min_tot_2_mon = contact_hour_12_call_min_tot_2_mon + contact_hour_13_call_min_tot_2_mon
        contact_hour_14to15_call_min_tot_2_mon = contact_hour_14_call_min_tot_2_mon + contact_hour_15_call_min_tot_2_mon
        contact_hour_16to17_call_min_tot_2_mon = contact_hour_16_call_min_tot_2_mon + contact_hour_17_call_min_tot_2_mon
        contact_hour_18to19_call_min_tot_2_mon = contact_hour_18_call_min_tot_2_mon + contact_hour_19_call_min_tot_2_mon
        contact_hour_20to21_call_min_tot_2_mon = contact_hour_20_call_min_tot_2_mon + contact_hour_21_call_min_tot_2_mon
        contact_hour_22to23_call_min_tot_2_mon = contact_hour_22_call_min_tot_2_mon + contact_hour_23_call_min_tot_2_mon

        contact_hour_0to1_call_cnt_1_mon = contact_hour_0_call_cnt_1_mon + contact_hour_1_call_cnt_1_mon
        contact_hour_2to3_call_cnt_1_mon = contact_hour_2_call_cnt_1_mon + contact_hour_3_call_cnt_1_mon
        contact_hour_4to5_call_cnt_1_mon = contact_hour_4_call_cnt_1_mon + contact_hour_5_call_cnt_1_mon
        contact_hour_6to7_call_cnt_1_mon = contact_hour_6_call_cnt_1_mon + contact_hour_7_call_cnt_1_mon
        contact_hour_8to9_call_cnt_1_mon = contact_hour_8_call_cnt_1_mon + contact_hour_9_call_cnt_1_mon
        contact_hour_10to11_call_cnt_1_mon = contact_hour_10_call_cnt_1_mon + contact_hour_11_call_cnt_1_mon
        contact_hour_12to13_call_cnt_1_mon = contact_hour_12_call_cnt_1_mon + contact_hour_13_call_cnt_1_mon
        contact_hour_14to15_call_cnt_1_mon = contact_hour_14_call_cnt_1_mon + contact_hour_15_call_cnt_1_mon
        contact_hour_16to17_call_cnt_1_mon = contact_hour_16_call_cnt_1_mon + contact_hour_17_call_cnt_1_mon
        contact_hour_18to19_call_cnt_1_mon = contact_hour_18_call_cnt_1_mon + contact_hour_19_call_cnt_1_mon
        contact_hour_20to21_call_cnt_1_mon = contact_hour_20_call_cnt_1_mon + contact_hour_21_call_cnt_1_mon
        contact_hour_22to23_call_cnt_1_mon = contact_hour_22_call_cnt_1_mon + contact_hour_23_call_cnt_1_mon

        contact_hour_0to1_call_min_tot_1_mon = contact_hour_0_call_min_tot_1_mon + contact_hour_1_call_min_tot_1_mon
        contact_hour_2to3_call_min_tot_1_mon = contact_hour_2_call_min_tot_1_mon + contact_hour_3_call_min_tot_1_mon
        contact_hour_4to5_call_min_tot_1_mon = contact_hour_4_call_min_tot_1_mon + contact_hour_5_call_min_tot_1_mon
        contact_hour_6to7_call_min_tot_1_mon = contact_hour_6_call_min_tot_1_mon + contact_hour_7_call_min_tot_1_mon
        contact_hour_8to9_call_min_tot_1_mon = contact_hour_8_call_min_tot_1_mon + contact_hour_9_call_min_tot_1_mon
        contact_hour_10to11_call_min_tot_1_mon = contact_hour_10_call_min_tot_1_mon + contact_hour_11_call_min_tot_1_mon
        contact_hour_12to13_call_min_tot_1_mon = contact_hour_12_call_min_tot_1_mon + contact_hour_13_call_min_tot_1_mon
        contact_hour_14to15_call_min_tot_1_mon = contact_hour_14_call_min_tot_1_mon + contact_hour_15_call_min_tot_1_mon
        contact_hour_16to17_call_min_tot_1_mon = contact_hour_16_call_min_tot_1_mon + contact_hour_17_call_min_tot_1_mon
        contact_hour_18to19_call_min_tot_1_mon = contact_hour_18_call_min_tot_1_mon + contact_hour_19_call_min_tot_1_mon
        contact_hour_20to21_call_min_tot_1_mon = contact_hour_20_call_min_tot_1_mon + contact_hour_21_call_min_tot_1_mon
        contact_hour_22to23_call_min_tot_1_mon = contact_hour_22_call_min_tot_1_mon + contact_hour_23_call_min_tot_1_mon

        contact_hour_0to1_call_cnt_2_wk = contact_hour_0_call_cnt_2_wk + contact_hour_1_call_cnt_2_wk
        contact_hour_2to3_call_cnt_2_wk = contact_hour_2_call_cnt_2_wk + contact_hour_3_call_cnt_2_wk
        contact_hour_4to5_call_cnt_2_wk = contact_hour_4_call_cnt_2_wk + contact_hour_5_call_cnt_2_wk
        contact_hour_6to7_call_cnt_2_wk = contact_hour_6_call_cnt_2_wk + contact_hour_7_call_cnt_2_wk
        contact_hour_8to9_call_cnt_2_wk = contact_hour_8_call_cnt_2_wk + contact_hour_9_call_cnt_2_wk
        contact_hour_10to11_call_cnt_2_wk = contact_hour_10_call_cnt_2_wk + contact_hour_11_call_cnt_2_wk
        contact_hour_12to13_call_cnt_2_wk = contact_hour_12_call_cnt_2_wk + contact_hour_13_call_cnt_2_wk
        contact_hour_14to15_call_cnt_2_wk = contact_hour_14_call_cnt_2_wk + contact_hour_15_call_cnt_2_wk
        contact_hour_16to17_call_cnt_2_wk = contact_hour_16_call_cnt_2_wk + contact_hour_17_call_cnt_2_wk
        contact_hour_18to19_call_cnt_2_wk = contact_hour_18_call_cnt_2_wk + contact_hour_19_call_cnt_2_wk
        contact_hour_20to21_call_cnt_2_wk = contact_hour_20_call_cnt_2_wk + contact_hour_21_call_cnt_2_wk
        contact_hour_22to23_call_cnt_2_wk = contact_hour_22_call_cnt_2_wk + contact_hour_23_call_cnt_2_wk

        contact_hour_0to1_call_min_tot_2_wk = contact_hour_0_call_min_tot_2_wk + contact_hour_1_call_min_tot_2_wk
        contact_hour_2to3_call_min_tot_2_wk = contact_hour_2_call_min_tot_2_wk + contact_hour_3_call_min_tot_2_wk
        contact_hour_4to5_call_min_tot_2_wk = contact_hour_4_call_min_tot_2_wk + contact_hour_5_call_min_tot_2_wk
        contact_hour_6to7_call_min_tot_2_wk = contact_hour_6_call_min_tot_2_wk + contact_hour_7_call_min_tot_2_wk
        contact_hour_8to9_call_min_tot_2_wk = contact_hour_8_call_min_tot_2_wk + contact_hour_9_call_min_tot_2_wk
        contact_hour_10to11_call_min_tot_2_wk = contact_hour_10_call_min_tot_2_wk + contact_hour_11_call_min_tot_2_wk
        contact_hour_12to13_call_min_tot_2_wk = contact_hour_12_call_min_tot_2_wk + contact_hour_13_call_min_tot_2_wk
        contact_hour_14to15_call_min_tot_2_wk = contact_hour_14_call_min_tot_2_wk + contact_hour_15_call_min_tot_2_wk
        contact_hour_16to17_call_min_tot_2_wk = contact_hour_16_call_min_tot_2_wk + contact_hour_17_call_min_tot_2_wk
        contact_hour_18to19_call_min_tot_2_wk = contact_hour_18_call_min_tot_2_wk + contact_hour_19_call_min_tot_2_wk
        contact_hour_20to21_call_min_tot_2_wk = contact_hour_20_call_min_tot_2_wk + contact_hour_21_call_min_tot_2_wk
        contact_hour_22to23_call_min_tot_2_wk = contact_hour_22_call_min_tot_2_wk + contact_hour_23_call_min_tot_2_wk

        contact_hour_1to6_call_cnt = contact_hour_1_call_cnt + contact_hour_2_call_cnt + contact_hour_3_call_cnt + contact_hour_4_call_cnt + contact_hour_5_call_cnt + contact_hour_6_call_cnt
        contact_hour_7to12_call_cnt = contact_hour_7_call_cnt + contact_hour_8_call_cnt + contact_hour_9_call_cnt + contact_hour_10_call_cnt + contact_hour_11_call_cnt + contact_hour_12_call_cnt
        contact_hour_13to18_call_cnt = contact_hour_13_call_cnt + contact_hour_14_call_cnt + contact_hour_15_call_cnt + contact_hour_16_call_cnt + contact_hour_17_call_cnt + contact_hour_18_call_cnt
        contact_hour_19to0_call_cnt = contact_hour_19_call_cnt + contact_hour_20_call_cnt + contact_hour_21_call_cnt + contact_hour_22_call_cnt + contact_hour_23_call_cnt + contact_hour_0_call_cnt

        contact_hour_1to6_call_min_tot = contact_hour_1_call_min_tot + contact_hour_2_call_min_tot + contact_hour_3_call_min_tot + contact_hour_4_call_min_tot + contact_hour_5_call_min_tot + contact_hour_6_call_min_tot
        contact_hour_7to12_call_min_tot = contact_hour_7_call_min_tot + contact_hour_8_call_min_tot + contact_hour_9_call_min_tot + contact_hour_10_call_min_tot + contact_hour_11_call_min_tot + contact_hour_12_call_min_tot
        contact_hour_13to18_call_min_tot = contact_hour_13_call_min_tot + contact_hour_14_call_min_tot + contact_hour_15_call_min_tot + contact_hour_16_call_min_tot + contact_hour_17_call_min_tot + contact_hour_18_call_min_tot
        contact_hour_19to0_call_min_tot = contact_hour_19_call_min_tot + contact_hour_20_call_min_tot + contact_hour_21_call_min_tot + contact_hour_22_call_min_tot + contact_hour_23_call_min_tot + contact_hour_0_call_min_tot

        contact_hour_1to6_call_cnt_6_mon = contact_hour_1_call_cnt_6_mon + contact_hour_2_call_cnt_6_mon + contact_hour_3_call_cnt_6_mon + contact_hour_4_call_cnt_6_mon + contact_hour_5_call_cnt_6_mon + contact_hour_6_call_cnt_6_mon
        contact_hour_7to12_call_cnt_6_mon = contact_hour_7_call_cnt_6_mon + contact_hour_8_call_cnt_6_mon + contact_hour_9_call_cnt_6_mon + contact_hour_10_call_cnt_6_mon + contact_hour_11_call_cnt_6_mon + contact_hour_12_call_cnt_6_mon
        contact_hour_13to18_call_cnt_6_mon = contact_hour_13_call_cnt_6_mon + contact_hour_14_call_cnt_6_mon + contact_hour_15_call_cnt_6_mon + contact_hour_16_call_cnt_6_mon + contact_hour_17_call_cnt_6_mon + contact_hour_18_call_cnt_6_mon
        contact_hour_19to0_call_cnt_6_mon = contact_hour_19_call_cnt_6_mon + contact_hour_20_call_cnt_6_mon + contact_hour_21_call_cnt_6_mon + contact_hour_22_call_cnt_6_mon + contact_hour_23_call_cnt_6_mon + contact_hour_0_call_cnt_6_mon

        contact_hour_1to6_call_min_tot_6_mon = contact_hour_1_call_min_tot_6_mon + contact_hour_2_call_min_tot_6_mon + contact_hour_3_call_min_tot_6_mon + contact_hour_4_call_min_tot_6_mon + contact_hour_5_call_min_tot_6_mon + contact_hour_6_call_min_tot_6_mon
        contact_hour_7to12_call_min_tot_6_mon = contact_hour_7_call_min_tot_6_mon + contact_hour_8_call_min_tot_6_mon + contact_hour_9_call_min_tot_6_mon + contact_hour_10_call_min_tot_6_mon + contact_hour_11_call_min_tot_6_mon + contact_hour_12_call_min_tot_6_mon
        contact_hour_13to18_call_min_tot_6_mon = contact_hour_13_call_min_tot_6_mon + contact_hour_14_call_min_tot_6_mon + contact_hour_15_call_min_tot_6_mon + contact_hour_16_call_min_tot_6_mon + contact_hour_17_call_min_tot_6_mon + contact_hour_18_call_min_tot_6_mon
        contact_hour_19to0_call_min_tot_6_mon = contact_hour_19_call_min_tot_6_mon + contact_hour_20_call_min_tot_6_mon + contact_hour_21_call_min_tot_6_mon + contact_hour_22_call_min_tot_6_mon + contact_hour_23_call_min_tot_6_mon + contact_hour_0_call_min_tot_6_mon

        contact_hour_1to6_call_cnt_3_mon = contact_hour_1_call_cnt_3_mon + contact_hour_2_call_cnt_3_mon + contact_hour_3_call_cnt_3_mon + contact_hour_4_call_cnt_3_mon + contact_hour_5_call_cnt_3_mon + contact_hour_6_call_cnt_3_mon
        contact_hour_7to12_call_cnt_3_mon = contact_hour_7_call_cnt_3_mon + contact_hour_8_call_cnt_3_mon + contact_hour_9_call_cnt_3_mon + contact_hour_10_call_cnt_3_mon + contact_hour_11_call_cnt_3_mon + contact_hour_12_call_cnt_3_mon
        contact_hour_13to18_call_cnt_3_mon = contact_hour_13_call_cnt_3_mon + contact_hour_14_call_cnt_3_mon + contact_hour_15_call_cnt_3_mon + contact_hour_16_call_cnt_3_mon + contact_hour_17_call_cnt_3_mon + contact_hour_18_call_cnt_3_mon
        contact_hour_19to0_call_cnt_3_mon = contact_hour_19_call_cnt_3_mon + contact_hour_20_call_cnt_3_mon + contact_hour_21_call_cnt_3_mon + contact_hour_22_call_cnt_3_mon + contact_hour_23_call_cnt_3_mon + contact_hour_0_call_cnt_3_mon

        contact_hour_1to6_call_min_tot_3_mon = contact_hour_1_call_min_tot_3_mon + contact_hour_2_call_min_tot_3_mon + contact_hour_3_call_min_tot_3_mon + contact_hour_4_call_min_tot_3_mon + contact_hour_5_call_min_tot_3_mon + contact_hour_6_call_min_tot_3_mon
        contact_hour_7to12_call_min_tot_3_mon = contact_hour_7_call_min_tot_3_mon + contact_hour_8_call_min_tot_3_mon + contact_hour_9_call_min_tot_3_mon + contact_hour_10_call_min_tot_3_mon + contact_hour_11_call_min_tot_3_mon + contact_hour_12_call_min_tot_3_mon
        contact_hour_13to18_call_min_tot_3_mon = contact_hour_13_call_min_tot_3_mon + contact_hour_14_call_min_tot_3_mon + contact_hour_15_call_min_tot_3_mon + contact_hour_16_call_min_tot_3_mon + contact_hour_17_call_min_tot_3_mon + contact_hour_18_call_min_tot_3_mon
        contact_hour_19to0_call_min_tot_3_mon = contact_hour_19_call_min_tot_3_mon + contact_hour_20_call_min_tot_3_mon + contact_hour_21_call_min_tot_3_mon + contact_hour_22_call_min_tot_3_mon + contact_hour_23_call_min_tot_3_mon + contact_hour_0_call_min_tot_3_mon

        contact_hour_1to6_call_cnt_2_mon = contact_hour_1_call_cnt_2_mon + contact_hour_2_call_cnt_2_mon + contact_hour_3_call_cnt_2_mon + contact_hour_4_call_cnt_2_mon + contact_hour_5_call_cnt_2_mon + contact_hour_6_call_cnt_2_mon
        contact_hour_7to12_call_cnt_2_mon = contact_hour_7_call_cnt_2_mon + contact_hour_8_call_cnt_2_mon + contact_hour_9_call_cnt_2_mon + contact_hour_10_call_cnt_2_mon + contact_hour_11_call_cnt_2_mon + contact_hour_12_call_cnt_2_mon
        contact_hour_13to18_call_cnt_2_mon = contact_hour_13_call_cnt_2_mon + contact_hour_14_call_cnt_2_mon + contact_hour_15_call_cnt_2_mon + contact_hour_16_call_cnt_2_mon + contact_hour_17_call_cnt_2_mon + contact_hour_18_call_cnt_2_mon
        contact_hour_19to0_call_cnt_2_mon = contact_hour_19_call_cnt_2_mon + contact_hour_20_call_cnt_2_mon + contact_hour_21_call_cnt_2_mon + contact_hour_22_call_cnt_2_mon + contact_hour_23_call_cnt_2_mon + contact_hour_0_call_cnt_2_mon

        contact_hour_1to6_call_min_tot_2_mon = contact_hour_1_call_min_tot_2_mon + contact_hour_2_call_min_tot_2_mon + contact_hour_3_call_min_tot_2_mon + contact_hour_4_call_min_tot_2_mon + contact_hour_5_call_min_tot_2_mon + contact_hour_6_call_min_tot_2_mon
        contact_hour_7to12_call_min_tot_2_mon = contact_hour_7_call_min_tot_2_mon + contact_hour_8_call_min_tot_2_mon + contact_hour_9_call_min_tot_2_mon + contact_hour_10_call_min_tot_2_mon + contact_hour_11_call_min_tot_2_mon + contact_hour_12_call_min_tot_2_mon
        contact_hour_13to18_call_min_tot_2_mon = contact_hour_13_call_min_tot_2_mon + contact_hour_14_call_min_tot_2_mon + contact_hour_15_call_min_tot_2_mon + contact_hour_16_call_min_tot_2_mon + contact_hour_17_call_min_tot_2_mon + contact_hour_18_call_min_tot_2_mon
        contact_hour_19to0_call_min_tot_2_mon = contact_hour_19_call_min_tot_2_mon + contact_hour_20_call_min_tot_2_mon + contact_hour_21_call_min_tot_2_mon + contact_hour_22_call_min_tot_2_mon + contact_hour_23_call_min_tot_2_mon + contact_hour_0_call_min_tot_2_mon

        contact_hour_1to6_call_cnt_1_mon = contact_hour_1_call_cnt_1_mon + contact_hour_2_call_cnt_1_mon + contact_hour_3_call_cnt_1_mon + contact_hour_4_call_cnt_1_mon + contact_hour_5_call_cnt_1_mon + contact_hour_6_call_cnt_1_mon
        contact_hour_7to12_call_cnt_1_mon = contact_hour_7_call_cnt_1_mon + contact_hour_8_call_cnt_1_mon + contact_hour_9_call_cnt_1_mon + contact_hour_10_call_cnt_1_mon + contact_hour_11_call_cnt_1_mon + contact_hour_12_call_cnt_1_mon
        contact_hour_13to18_call_cnt_1_mon = contact_hour_13_call_cnt_1_mon + contact_hour_14_call_cnt_1_mon + contact_hour_15_call_cnt_1_mon + contact_hour_16_call_cnt_1_mon + contact_hour_17_call_cnt_1_mon + contact_hour_18_call_cnt_1_mon
        contact_hour_19to0_call_cnt_1_mon = contact_hour_19_call_cnt_1_mon + contact_hour_20_call_cnt_1_mon + contact_hour_21_call_cnt_1_mon + contact_hour_22_call_cnt_1_mon + contact_hour_23_call_cnt_1_mon + contact_hour_0_call_cnt_1_mon

        contact_hour_1to6_call_min_tot_1_mon = contact_hour_1_call_min_tot_1_mon + contact_hour_2_call_min_tot_1_mon + contact_hour_3_call_min_tot_1_mon + contact_hour_4_call_min_tot_1_mon + contact_hour_5_call_min_tot_1_mon + contact_hour_6_call_min_tot_1_mon
        contact_hour_7to12_call_min_tot_1_mon = contact_hour_7_call_min_tot_1_mon + contact_hour_8_call_min_tot_1_mon + contact_hour_9_call_min_tot_1_mon + contact_hour_10_call_min_tot_1_mon + contact_hour_11_call_min_tot_1_mon + contact_hour_12_call_min_tot_1_mon
        contact_hour_13to18_call_min_tot_1_mon = contact_hour_13_call_min_tot_1_mon + contact_hour_14_call_min_tot_1_mon + contact_hour_15_call_min_tot_1_mon + contact_hour_16_call_min_tot_1_mon + contact_hour_17_call_min_tot_1_mon + contact_hour_18_call_min_tot_1_mon
        contact_hour_19to0_call_min_tot_1_mon = contact_hour_19_call_min_tot_1_mon + contact_hour_20_call_min_tot_1_mon + contact_hour_21_call_min_tot_1_mon + contact_hour_22_call_min_tot_1_mon + contact_hour_23_call_min_tot_1_mon + contact_hour_0_call_min_tot_1_mon

        contact_hour_1to6_call_cnt_2_wk = contact_hour_1_call_cnt_2_wk + contact_hour_2_call_cnt_2_wk + contact_hour_3_call_cnt_2_wk + contact_hour_4_call_cnt_2_wk + contact_hour_5_call_cnt_2_wk + contact_hour_6_call_cnt_2_wk
        contact_hour_7to12_call_cnt_2_wk = contact_hour_7_call_cnt_2_wk + contact_hour_8_call_cnt_2_wk + contact_hour_9_call_cnt_2_wk + contact_hour_10_call_cnt_2_wk + contact_hour_11_call_cnt_2_wk + contact_hour_12_call_cnt_2_wk
        contact_hour_13to18_call_cnt_2_wk = contact_hour_13_call_cnt_2_wk + contact_hour_14_call_cnt_2_wk + contact_hour_15_call_cnt_2_wk + contact_hour_16_call_cnt_2_wk + contact_hour_17_call_cnt_2_wk + contact_hour_18_call_cnt_2_wk
        contact_hour_19to0_call_cnt_2_wk = contact_hour_19_call_cnt_2_wk + contact_hour_20_call_cnt_2_wk + contact_hour_21_call_cnt_2_wk + contact_hour_22_call_cnt_2_wk + contact_hour_23_call_cnt_2_wk + contact_hour_0_call_cnt_2_wk

        contact_hour_1to6_call_min_tot_2_wk = contact_hour_1_call_min_tot_2_wk + contact_hour_2_call_min_tot_2_wk + contact_hour_3_call_min_tot_2_wk + contact_hour_4_call_min_tot_2_wk + contact_hour_5_call_min_tot_2_wk + contact_hour_6_call_min_tot_2_wk
        contact_hour_7to12_call_min_tot_2_wk = contact_hour_7_call_min_tot_2_wk + contact_hour_8_call_min_tot_2_wk + contact_hour_9_call_min_tot_2_wk + contact_hour_10_call_min_tot_2_wk + contact_hour_11_call_min_tot_2_wk + contact_hour_12_call_min_tot_2_wk
        contact_hour_13to18_call_min_tot_2_wk = contact_hour_13_call_min_tot_2_wk + contact_hour_14_call_min_tot_2_wk + contact_hour_15_call_min_tot_2_wk + contact_hour_16_call_min_tot_2_wk + contact_hour_17_call_min_tot_2_wk + contact_hour_18_call_min_tot_2_wk
        contact_hour_19to0_call_min_tot_2_wk = contact_hour_19_call_min_tot_2_wk + contact_hour_20_call_min_tot_2_wk + contact_hour_21_call_min_tot_2_wk + contact_hour_22_call_min_tot_2_wk + contact_hour_23_call_min_tot_2_wk + contact_hour_0_call_min_tot_2_wk

        contact_hour_1to8_call_cnt = contact_hour_1_call_cnt + contact_hour_2_call_cnt + contact_hour_3_call_cnt + contact_hour_4_call_cnt + contact_hour_5_call_cnt + contact_hour_6_call_cnt + contact_hour_7_call_cnt + contact_hour_8_call_cnt
        contact_hour_9to16_call_cnt = contact_hour_9_call_cnt + contact_hour_10_call_cnt + contact_hour_11_call_cnt + contact_hour_12_call_cnt + contact_hour_13_call_cnt + contact_hour_14_call_cnt + contact_hour_15_call_cnt + contact_hour_16_call_cnt
        contact_hour_17to0_call_cnt = contact_hour_17_call_cnt + contact_hour_18_call_cnt + contact_hour_19_call_cnt + contact_hour_20_call_cnt + contact_hour_21_call_cnt + contact_hour_22_call_cnt + contact_hour_23_call_cnt + contact_hour_0_call_cnt

        contact_hour_1to8_call_min_tot = contact_hour_1_call_min_tot + contact_hour_2_call_min_tot + contact_hour_3_call_min_tot + contact_hour_4_call_min_tot + contact_hour_5_call_min_tot + contact_hour_6_call_min_tot + contact_hour_7_call_min_tot + contact_hour_8_call_min_tot
        contact_hour_9to16_call_min_tot = contact_hour_9_call_min_tot + contact_hour_10_call_min_tot + contact_hour_11_call_min_tot + contact_hour_12_call_min_tot + contact_hour_13_call_min_tot + contact_hour_14_call_min_tot + contact_hour_15_call_min_tot + contact_hour_16_call_min_tot
        contact_hour_17to0_call_min_tot = contact_hour_17_call_min_tot + contact_hour_18_call_min_tot + contact_hour_19_call_min_tot + contact_hour_20_call_min_tot + contact_hour_21_call_min_tot + contact_hour_22_call_min_tot + contact_hour_23_call_min_tot + contact_hour_0_call_min_tot

        contact_hour_1to8_call_cnt_6_mon = contact_hour_1_call_cnt_6_mon + contact_hour_2_call_cnt_6_mon + contact_hour_3_call_cnt_6_mon + contact_hour_4_call_cnt_6_mon + contact_hour_5_call_cnt_6_mon + contact_hour_6_call_cnt_6_mon + contact_hour_7_call_cnt_6_mon + contact_hour_8_call_cnt_6_mon
        contact_hour_9to16_call_cnt_6_mon = contact_hour_9_call_cnt_6_mon + contact_hour_10_call_cnt_6_mon + contact_hour_11_call_cnt_6_mon + contact_hour_12_call_cnt_6_mon + contact_hour_13_call_cnt_6_mon + contact_hour_14_call_cnt_6_mon + contact_hour_15_call_cnt_6_mon + contact_hour_16_call_cnt_6_mon
        contact_hour_17to0_call_cnt_6_mon = contact_hour_17_call_cnt_6_mon + contact_hour_18_call_cnt_6_mon + contact_hour_19_call_cnt_6_mon + contact_hour_20_call_cnt_6_mon + contact_hour_21_call_cnt_6_mon + contact_hour_22_call_cnt_6_mon + contact_hour_23_call_cnt_6_mon + contact_hour_0_call_cnt_6_mon

        contact_hour_1to8_call_min_tot_6_mon = contact_hour_1_call_min_tot_6_mon + contact_hour_2_call_min_tot_6_mon + contact_hour_3_call_min_tot_6_mon + contact_hour_4_call_min_tot_6_mon + contact_hour_5_call_min_tot_6_mon + contact_hour_6_call_min_tot_6_mon + contact_hour_7_call_min_tot_6_mon + contact_hour_8_call_min_tot_6_mon
        contact_hour_9to16_call_min_tot_6_mon = contact_hour_9_call_min_tot_6_mon + contact_hour_10_call_min_tot_6_mon + contact_hour_11_call_min_tot_6_mon + contact_hour_12_call_min_tot_6_mon + contact_hour_13_call_min_tot_6_mon + contact_hour_14_call_min_tot_6_mon + contact_hour_15_call_min_tot_6_mon + contact_hour_16_call_min_tot_6_mon
        contact_hour_17to0_call_min_tot_6_mon = contact_hour_17_call_min_tot_6_mon + contact_hour_18_call_min_tot_6_mon + contact_hour_19_call_min_tot_6_mon + contact_hour_20_call_min_tot_6_mon + contact_hour_21_call_min_tot_6_mon + contact_hour_22_call_min_tot_6_mon + contact_hour_23_call_min_tot_6_mon + contact_hour_0_call_min_tot_6_mon

        contact_hour_1to8_call_cnt_3_mon = contact_hour_1_call_cnt_3_mon + contact_hour_2_call_cnt_3_mon + contact_hour_3_call_cnt_3_mon + contact_hour_4_call_cnt_3_mon + contact_hour_5_call_cnt_3_mon + contact_hour_6_call_cnt_3_mon + contact_hour_7_call_cnt_3_mon + contact_hour_8_call_cnt_3_mon
        contact_hour_9to16_call_cnt_3_mon = contact_hour_9_call_cnt_3_mon + contact_hour_10_call_cnt_3_mon + contact_hour_11_call_cnt_3_mon + contact_hour_12_call_cnt_3_mon + contact_hour_13_call_cnt_3_mon + contact_hour_14_call_cnt_3_mon + contact_hour_15_call_cnt_3_mon + contact_hour_16_call_cnt_3_mon
        contact_hour_17to0_call_cnt_3_mon = contact_hour_17_call_cnt_3_mon + contact_hour_18_call_cnt_3_mon + contact_hour_19_call_cnt_3_mon + contact_hour_20_call_cnt_3_mon + contact_hour_21_call_cnt_3_mon + contact_hour_22_call_cnt_3_mon + contact_hour_23_call_cnt_3_mon + contact_hour_0_call_cnt_3_mon

        contact_hour_1to8_call_min_tot_3_mon = contact_hour_1_call_min_tot_3_mon + contact_hour_2_call_min_tot_3_mon + contact_hour_3_call_min_tot_3_mon + contact_hour_4_call_min_tot_3_mon + contact_hour_5_call_min_tot_3_mon + contact_hour_6_call_min_tot_3_mon + contact_hour_7_call_min_tot_3_mon + contact_hour_8_call_min_tot_3_mon
        contact_hour_9to16_call_min_tot_3_mon = contact_hour_9_call_min_tot_3_mon + contact_hour_10_call_min_tot_3_mon + contact_hour_11_call_min_tot_3_mon + contact_hour_12_call_min_tot_3_mon + contact_hour_13_call_min_tot_3_mon + contact_hour_14_call_min_tot_3_mon + contact_hour_15_call_min_tot_3_mon + contact_hour_16_call_min_tot_3_mon
        contact_hour_17to0_call_min_tot_3_mon = contact_hour_17_call_min_tot_3_mon + contact_hour_18_call_min_tot_3_mon + contact_hour_19_call_min_tot_3_mon + contact_hour_20_call_min_tot_3_mon + contact_hour_21_call_min_tot_3_mon + contact_hour_22_call_min_tot_3_mon + contact_hour_23_call_min_tot_3_mon + contact_hour_0_call_min_tot_3_mon

        contact_hour_1to8_call_cnt_2_mon = contact_hour_1_call_cnt_2_mon + contact_hour_2_call_cnt_2_mon + contact_hour_3_call_cnt_2_mon + contact_hour_4_call_cnt_2_mon + contact_hour_5_call_cnt_2_mon + contact_hour_6_call_cnt_2_mon + contact_hour_7_call_cnt_2_mon + contact_hour_8_call_cnt_2_mon
        contact_hour_9to16_call_cnt_2_mon = contact_hour_9_call_cnt_2_mon + contact_hour_10_call_cnt_2_mon + contact_hour_11_call_cnt_2_mon + contact_hour_12_call_cnt_2_mon + contact_hour_13_call_cnt_2_mon + contact_hour_14_call_cnt_2_mon + contact_hour_15_call_cnt_2_mon + contact_hour_16_call_cnt_2_mon
        contact_hour_17to0_call_cnt_2_mon = contact_hour_17_call_cnt_2_mon + contact_hour_18_call_cnt_2_mon + contact_hour_19_call_cnt_2_mon + contact_hour_20_call_cnt_2_mon + contact_hour_21_call_cnt_2_mon + contact_hour_22_call_cnt_2_mon + contact_hour_23_call_cnt_2_mon + contact_hour_0_call_cnt_2_mon

        contact_hour_1to8_call_min_tot_2_mon = contact_hour_1_call_min_tot_2_mon + contact_hour_2_call_min_tot_2_mon + contact_hour_3_call_min_tot_2_mon + contact_hour_4_call_min_tot_2_mon + contact_hour_5_call_min_tot_2_mon + contact_hour_6_call_min_tot_2_mon + contact_hour_7_call_min_tot_2_mon + contact_hour_8_call_min_tot_2_mon
        contact_hour_9to16_call_min_tot_2_mon = contact_hour_9_call_min_tot_2_mon + contact_hour_10_call_min_tot_2_mon + contact_hour_11_call_min_tot_2_mon + contact_hour_12_call_min_tot_2_mon + contact_hour_13_call_min_tot_2_mon + contact_hour_14_call_min_tot_2_mon + contact_hour_15_call_min_tot_2_mon + contact_hour_16_call_min_tot_2_mon
        contact_hour_17to0_call_min_tot_2_mon = contact_hour_17_call_min_tot_2_mon + contact_hour_18_call_min_tot_2_mon + contact_hour_19_call_min_tot_2_mon + contact_hour_20_call_min_tot_2_mon + contact_hour_21_call_min_tot_2_mon + contact_hour_22_call_min_tot_2_mon + contact_hour_23_call_min_tot_2_mon + contact_hour_0_call_min_tot_2_mon

        contact_hour_1to8_call_cnt_1_mon = contact_hour_1_call_cnt_1_mon + contact_hour_2_call_cnt_1_mon + contact_hour_3_call_cnt_1_mon + contact_hour_4_call_cnt_1_mon + contact_hour_5_call_cnt_1_mon + contact_hour_6_call_cnt_1_mon + contact_hour_7_call_cnt_1_mon + contact_hour_8_call_cnt_1_mon
        contact_hour_9to16_call_cnt_1_mon = contact_hour_9_call_cnt_1_mon + contact_hour_10_call_cnt_1_mon + contact_hour_11_call_cnt_1_mon + contact_hour_12_call_cnt_1_mon + contact_hour_13_call_cnt_1_mon + contact_hour_14_call_cnt_1_mon + contact_hour_15_call_cnt_1_mon + contact_hour_16_call_cnt_1_mon
        contact_hour_17to0_call_cnt_1_mon = contact_hour_17_call_cnt_1_mon + contact_hour_18_call_cnt_1_mon + contact_hour_19_call_cnt_1_mon + contact_hour_20_call_cnt_1_mon + contact_hour_21_call_cnt_1_mon + contact_hour_22_call_cnt_1_mon + contact_hour_23_call_cnt_1_mon + contact_hour_0_call_cnt_1_mon

        contact_hour_1to8_call_min_tot_1_mon = contact_hour_1_call_min_tot_1_mon + contact_hour_2_call_min_tot_1_mon + contact_hour_3_call_min_tot_1_mon + contact_hour_4_call_min_tot_1_mon + contact_hour_5_call_min_tot_1_mon + contact_hour_6_call_min_tot_1_mon + contact_hour_7_call_min_tot_1_mon + contact_hour_8_call_min_tot_1_mon
        contact_hour_9to16_call_min_tot_1_mon = contact_hour_9_call_min_tot_1_mon + contact_hour_10_call_min_tot_1_mon + contact_hour_11_call_min_tot_1_mon + contact_hour_12_call_min_tot_1_mon + contact_hour_13_call_min_tot_1_mon + contact_hour_14_call_min_tot_1_mon + contact_hour_15_call_min_tot_1_mon + contact_hour_16_call_min_tot_1_mon
        contact_hour_17to0_call_min_tot_1_mon = contact_hour_17_call_min_tot_1_mon + contact_hour_18_call_min_tot_1_mon + contact_hour_19_call_min_tot_1_mon + contact_hour_20_call_min_tot_1_mon + contact_hour_21_call_min_tot_1_mon + contact_hour_22_call_min_tot_1_mon + contact_hour_23_call_min_tot_1_mon + contact_hour_0_call_min_tot_1_mon

        contact_hour_1to8_call_cnt_2_wk = contact_hour_1_call_cnt_2_wk + contact_hour_2_call_cnt_2_wk + contact_hour_3_call_cnt_2_wk + contact_hour_4_call_cnt_2_wk + contact_hour_5_call_cnt_2_wk + contact_hour_6_call_cnt_2_wk + contact_hour_7_call_cnt_2_wk + contact_hour_8_call_cnt_2_wk
        contact_hour_9to16_call_cnt_2_wk = contact_hour_9_call_cnt_2_wk + contact_hour_10_call_cnt_2_wk + contact_hour_11_call_cnt_2_wk + contact_hour_12_call_cnt_2_wk + contact_hour_13_call_cnt_2_wk + contact_hour_14_call_cnt_2_wk + contact_hour_15_call_cnt_2_wk + contact_hour_16_call_cnt_2_wk
        contact_hour_17to0_call_cnt_2_wk = contact_hour_17_call_cnt_2_wk + contact_hour_18_call_cnt_2_wk + contact_hour_19_call_cnt_2_wk + contact_hour_20_call_cnt_2_wk + contact_hour_21_call_cnt_2_wk + contact_hour_22_call_cnt_2_wk + contact_hour_23_call_cnt_2_wk + contact_hour_0_call_cnt_2_wk

        contact_hour_1to8_call_min_tot_2_wk = contact_hour_1_call_min_tot_2_wk + contact_hour_2_call_min_tot_2_wk + contact_hour_3_call_min_tot_2_wk + contact_hour_4_call_min_tot_2_wk + contact_hour_5_call_min_tot_2_wk + contact_hour_6_call_min_tot_2_wk + contact_hour_7_call_min_tot_2_wk + contact_hour_8_call_min_tot_2_wk
        contact_hour_9to16_call_min_tot_2_wk = contact_hour_9_call_min_tot_2_wk + contact_hour_10_call_min_tot_2_wk + contact_hour_11_call_min_tot_2_wk + contact_hour_12_call_min_tot_2_wk + contact_hour_13_call_min_tot_2_wk + contact_hour_14_call_min_tot_2_wk + contact_hour_15_call_min_tot_2_wk + contact_hour_16_call_min_tot_2_wk
        contact_hour_17to0_call_min_tot_2_wk = contact_hour_17_call_min_tot_2_wk + contact_hour_18_call_min_tot_2_wk + contact_hour_19_call_min_tot_2_wk + contact_hour_20_call_min_tot_2_wk + contact_hour_21_call_min_tot_2_wk + contact_hour_22_call_min_tot_2_wk + contact_hour_23_call_min_tot_2_wk + contact_hour_0_call_min_tot_2_wk

        contact_hour_9to20_call_cnt = contact_hour_9_call_cnt + contact_hour_10_call_cnt + contact_hour_11_call_cnt + contact_hour_12_call_cnt + contact_hour_13_call_cnt + contact_hour_14_call_cnt + contact_hour_15_call_cnt + contact_hour_16_call_cnt + contact_hour_17_call_cnt + contact_hour_18_call_cnt + contact_hour_19_call_cnt + contact_hour_20_call_cnt
        contact_hour_21to8_call_cnt = contact_hour_21_call_cnt + contact_hour_22_call_cnt + contact_hour_23_call_cnt + contact_hour_0_call_cnt + contact_hour_1_call_cnt + contact_hour_2_call_cnt + contact_hour_3_call_cnt + contact_hour_4_call_cnt + contact_hour_5_call_cnt + contact_hour_6_call_cnt + contact_hour_7_call_cnt + contact_hour_8_call_cnt

        contact_hour_9to20_call_min_tot = contact_hour_9_call_min_tot + contact_hour_10_call_min_tot + contact_hour_11_call_min_tot + contact_hour_12_call_min_tot + contact_hour_13_call_min_tot + contact_hour_14_call_min_tot + contact_hour_15_call_min_tot + contact_hour_16_call_min_tot + contact_hour_17_call_min_tot + contact_hour_18_call_min_tot + contact_hour_19_call_min_tot + contact_hour_20_call_min_tot
        contact_hour_21to8_call_min_tot = contact_hour_21_call_min_tot + contact_hour_22_call_min_tot + contact_hour_23_call_min_tot + contact_hour_0_call_min_tot + contact_hour_1_call_min_tot + contact_hour_2_call_min_tot + contact_hour_3_call_min_tot + contact_hour_4_call_min_tot + contact_hour_5_call_min_tot + contact_hour_6_call_min_tot + contact_hour_7_call_min_tot + contact_hour_8_call_min_tot

        contact_hour_9to20_call_cnt_6_mon = contact_hour_9_call_cnt_6_mon + contact_hour_10_call_cnt_6_mon + contact_hour_11_call_cnt_6_mon + contact_hour_12_call_cnt_6_mon + contact_hour_13_call_cnt_6_mon + contact_hour_14_call_cnt_6_mon + contact_hour_15_call_cnt_6_mon + contact_hour_16_call_cnt_6_mon + contact_hour_17_call_cnt_6_mon + contact_hour_18_call_cnt_6_mon + contact_hour_19_call_cnt_6_mon + contact_hour_20_call_cnt_6_mon
        contact_hour_21to8_call_cnt_6_mon = contact_hour_21_call_cnt_6_mon + contact_hour_22_call_cnt_6_mon + contact_hour_23_call_cnt_6_mon + contact_hour_0_call_cnt_6_mon + contact_hour_1_call_cnt_6_mon + contact_hour_2_call_cnt_6_mon + contact_hour_3_call_cnt_6_mon + contact_hour_4_call_cnt_6_mon + contact_hour_5_call_cnt_6_mon + contact_hour_6_call_cnt_6_mon + contact_hour_7_call_cnt_6_mon + contact_hour_8_call_cnt_6_mon

        contact_hour_9to20_call_min_tot_6_mon = contact_hour_9_call_min_tot_6_mon + contact_hour_10_call_min_tot_6_mon + contact_hour_11_call_min_tot_6_mon + contact_hour_12_call_min_tot_6_mon + contact_hour_13_call_min_tot_6_mon + contact_hour_14_call_min_tot_6_mon + contact_hour_15_call_min_tot_6_mon + contact_hour_16_call_min_tot_6_mon + contact_hour_17_call_min_tot_6_mon + contact_hour_18_call_min_tot_6_mon + contact_hour_19_call_min_tot_6_mon + contact_hour_20_call_min_tot_6_mon
        contact_hour_21to8_call_min_tot_6_mon = contact_hour_21_call_min_tot_6_mon + contact_hour_22_call_min_tot_6_mon + contact_hour_23_call_min_tot_6_mon + contact_hour_0_call_min_tot_6_mon + contact_hour_1_call_min_tot_6_mon + contact_hour_2_call_min_tot_6_mon + contact_hour_3_call_min_tot_6_mon + contact_hour_4_call_min_tot_6_mon + contact_hour_5_call_min_tot_6_mon + contact_hour_6_call_min_tot_6_mon + contact_hour_7_call_min_tot_6_mon + contact_hour_8_call_min_tot_6_mon

        contact_hour_9to20_call_cnt_3_mon = contact_hour_9_call_cnt_3_mon + contact_hour_10_call_cnt_3_mon + contact_hour_11_call_cnt_3_mon + contact_hour_12_call_cnt_3_mon + contact_hour_13_call_cnt_3_mon + contact_hour_14_call_cnt_3_mon + contact_hour_15_call_cnt_3_mon + contact_hour_16_call_cnt_3_mon + contact_hour_17_call_cnt_3_mon + contact_hour_18_call_cnt_3_mon + contact_hour_19_call_cnt_3_mon + contact_hour_20_call_cnt_3_mon
        contact_hour_21to8_call_cnt_3_mon = contact_hour_21_call_cnt_3_mon + contact_hour_22_call_cnt_3_mon + contact_hour_23_call_cnt_3_mon + contact_hour_0_call_cnt_3_mon + contact_hour_1_call_cnt_3_mon + contact_hour_2_call_cnt_3_mon + contact_hour_3_call_cnt_3_mon + contact_hour_4_call_cnt_3_mon + contact_hour_5_call_cnt_3_mon + contact_hour_6_call_cnt_3_mon + contact_hour_7_call_cnt_3_mon + contact_hour_8_call_cnt_3_mon

        contact_hour_9to20_call_min_tot_3_mon = contact_hour_9_call_min_tot_3_mon + contact_hour_10_call_min_tot_3_mon + contact_hour_11_call_min_tot_3_mon + contact_hour_12_call_min_tot_3_mon + contact_hour_13_call_min_tot_3_mon + contact_hour_14_call_min_tot_3_mon + contact_hour_15_call_min_tot_3_mon + contact_hour_16_call_min_tot_3_mon + contact_hour_17_call_min_tot_3_mon + contact_hour_18_call_min_tot_3_mon + contact_hour_19_call_min_tot_3_mon + contact_hour_20_call_min_tot_3_mon
        contact_hour_21to8_call_min_tot_3_mon = contact_hour_21_call_min_tot_3_mon + contact_hour_22_call_min_tot_3_mon + contact_hour_23_call_min_tot_3_mon + contact_hour_0_call_min_tot_3_mon + contact_hour_1_call_min_tot_3_mon + contact_hour_2_call_min_tot_3_mon + contact_hour_3_call_min_tot_3_mon + contact_hour_4_call_min_tot_3_mon + contact_hour_5_call_min_tot_3_mon + contact_hour_6_call_min_tot_3_mon + contact_hour_7_call_min_tot_3_mon + contact_hour_8_call_min_tot_3_mon

        contact_hour_9to20_call_cnt_2_mon = contact_hour_9_call_cnt_2_mon + contact_hour_10_call_cnt_2_mon + contact_hour_11_call_cnt_2_mon + contact_hour_12_call_cnt_2_mon + contact_hour_13_call_cnt_2_mon + contact_hour_14_call_cnt_2_mon + contact_hour_15_call_cnt_2_mon + contact_hour_16_call_cnt_2_mon + contact_hour_17_call_cnt_2_mon + contact_hour_18_call_cnt_2_mon + contact_hour_19_call_cnt_2_mon + contact_hour_20_call_cnt_2_mon
        contact_hour_21to8_call_cnt_2_mon = contact_hour_21_call_cnt_2_mon + contact_hour_22_call_cnt_2_mon + contact_hour_23_call_cnt_2_mon + contact_hour_0_call_cnt_2_mon + contact_hour_1_call_cnt_2_mon + contact_hour_2_call_cnt_2_mon + contact_hour_3_call_cnt_2_mon + contact_hour_4_call_cnt_2_mon + contact_hour_5_call_cnt_2_mon + contact_hour_6_call_cnt_2_mon + contact_hour_7_call_cnt_2_mon + contact_hour_8_call_cnt_2_mon

        contact_hour_9to20_call_min_tot_2_mon = contact_hour_9_call_min_tot_2_mon + contact_hour_10_call_min_tot_2_mon + contact_hour_11_call_min_tot_2_mon + contact_hour_12_call_min_tot_2_mon + contact_hour_13_call_min_tot_2_mon + contact_hour_14_call_min_tot_2_mon + contact_hour_15_call_min_tot_2_mon + contact_hour_16_call_min_tot_2_mon + contact_hour_17_call_min_tot_2_mon + contact_hour_18_call_min_tot_2_mon + contact_hour_19_call_min_tot_2_mon + contact_hour_20_call_min_tot_2_mon
        contact_hour_21to8_call_min_tot_2_mon = contact_hour_21_call_min_tot_2_mon + contact_hour_22_call_min_tot_2_mon + contact_hour_23_call_min_tot_2_mon + contact_hour_0_call_min_tot_2_mon + contact_hour_1_call_min_tot_2_mon + contact_hour_2_call_min_tot_2_mon + contact_hour_3_call_min_tot_2_mon + contact_hour_4_call_min_tot_2_mon + contact_hour_5_call_min_tot_2_mon + contact_hour_6_call_min_tot_2_mon + contact_hour_7_call_min_tot_2_mon + contact_hour_8_call_min_tot_2_mon

        contact_hour_9to20_call_cnt_1_mon = contact_hour_9_call_cnt_1_mon + contact_hour_10_call_cnt_1_mon + contact_hour_11_call_cnt_1_mon + contact_hour_12_call_cnt_1_mon + contact_hour_13_call_cnt_1_mon + contact_hour_14_call_cnt_1_mon + contact_hour_15_call_cnt_1_mon + contact_hour_16_call_cnt_1_mon + contact_hour_17_call_cnt_1_mon + contact_hour_18_call_cnt_1_mon + contact_hour_19_call_cnt_1_mon + contact_hour_20_call_cnt_1_mon
        contact_hour_21to8_call_cnt_1_mon = contact_hour_21_call_cnt_1_mon + contact_hour_22_call_cnt_1_mon + contact_hour_23_call_cnt_1_mon + contact_hour_0_call_cnt_1_mon + contact_hour_1_call_cnt_1_mon + contact_hour_2_call_cnt_1_mon + contact_hour_3_call_cnt_1_mon + contact_hour_4_call_cnt_1_mon + contact_hour_5_call_cnt_1_mon + contact_hour_6_call_cnt_1_mon + contact_hour_7_call_cnt_1_mon + contact_hour_8_call_cnt_1_mon

        contact_hour_9to20_call_min_tot_1_mon = contact_hour_9_call_min_tot_1_mon + contact_hour_10_call_min_tot_1_mon + contact_hour_11_call_min_tot_1_mon + contact_hour_12_call_min_tot_1_mon + contact_hour_13_call_min_tot_1_mon + contact_hour_14_call_min_tot_1_mon + contact_hour_15_call_min_tot_1_mon + contact_hour_16_call_min_tot_1_mon + contact_hour_17_call_min_tot_1_mon + contact_hour_18_call_min_tot_1_mon + contact_hour_19_call_min_tot_1_mon + contact_hour_20_call_min_tot_1_mon
        contact_hour_21to8_call_min_tot_1_mon = contact_hour_21_call_min_tot_1_mon + contact_hour_22_call_min_tot_1_mon + contact_hour_23_call_min_tot_1_mon + contact_hour_0_call_min_tot_1_mon + contact_hour_1_call_min_tot_1_mon + contact_hour_2_call_min_tot_1_mon + contact_hour_3_call_min_tot_1_mon + contact_hour_4_call_min_tot_1_mon + contact_hour_5_call_min_tot_1_mon + contact_hour_6_call_min_tot_1_mon + contact_hour_7_call_min_tot_1_mon + contact_hour_8_call_min_tot_1_mon

        contact_hour_9to20_call_cnt_2_wk = contact_hour_9_call_cnt_2_wk + contact_hour_10_call_cnt_2_wk + contact_hour_11_call_cnt_2_wk + contact_hour_12_call_cnt_2_wk + contact_hour_13_call_cnt_2_wk + contact_hour_14_call_cnt_2_wk + contact_hour_15_call_cnt_2_wk + contact_hour_16_call_cnt_2_wk + contact_hour_17_call_cnt_2_wk + contact_hour_18_call_cnt_2_wk + contact_hour_19_call_cnt_2_wk + contact_hour_20_call_cnt_2_wk
        contact_hour_21to8_call_cnt_2_wk = contact_hour_21_call_cnt_2_wk + contact_hour_22_call_cnt_2_wk + contact_hour_23_call_cnt_2_wk + contact_hour_0_call_cnt_2_wk + contact_hour_1_call_cnt_2_wk + contact_hour_2_call_cnt_2_wk + contact_hour_3_call_cnt_2_wk + contact_hour_4_call_cnt_2_wk + contact_hour_5_call_cnt_2_wk + contact_hour_6_call_cnt_2_wk + contact_hour_7_call_cnt_2_wk + contact_hour_8_call_cnt_2_wk

        contact_hour_9to20_call_min_tot_2_wk = contact_hour_9_call_min_tot_2_wk + contact_hour_10_call_min_tot_2_wk + contact_hour_11_call_min_tot_2_wk + contact_hour_12_call_min_tot_2_wk + contact_hour_13_call_min_tot_2_wk + contact_hour_14_call_min_tot_2_wk + contact_hour_15_call_min_tot_2_wk + contact_hour_16_call_min_tot_2_wk + contact_hour_17_call_min_tot_2_wk + contact_hour_18_call_min_tot_2_wk + contact_hour_19_call_min_tot_2_wk + contact_hour_20_call_min_tot_2_wk
        contact_hour_21to8_call_min_tot_2_wk = contact_hour_21_call_min_tot_2_wk + contact_hour_22_call_min_tot_2_wk + contact_hour_23_call_min_tot_2_wk + contact_hour_0_call_min_tot_2_wk + contact_hour_1_call_min_tot_2_wk + contact_hour_2_call_min_tot_2_wk + contact_hour_3_call_min_tot_2_wk + contact_hour_4_call_min_tot_2_wk + contact_hour_5_call_min_tot_2_wk + contact_hour_6_call_min_tot_2_wk + contact_hour_7_call_min_tot_2_wk + contact_hour_8_call_min_tot_2_wk

        contact_hour_0to1_rece_cnt = contact_hour_0_rece_cnt + contact_hour_1_rece_cnt
        contact_hour_2to3_rece_cnt = contact_hour_2_rece_cnt + contact_hour_3_rece_cnt
        contact_hour_4to5_rece_cnt = contact_hour_4_rece_cnt + contact_hour_5_rece_cnt
        contact_hour_6to7_rece_cnt = contact_hour_6_rece_cnt + contact_hour_7_rece_cnt
        contact_hour_8to9_rece_cnt = contact_hour_8_rece_cnt + contact_hour_9_rece_cnt
        contact_hour_10to11_rece_cnt = contact_hour_10_rece_cnt + contact_hour_11_rece_cnt
        contact_hour_12to13_rece_cnt = contact_hour_12_rece_cnt + contact_hour_13_rece_cnt
        contact_hour_14to15_rece_cnt = contact_hour_14_rece_cnt + contact_hour_15_rece_cnt
        contact_hour_16to17_rece_cnt = contact_hour_16_rece_cnt + contact_hour_17_rece_cnt
        contact_hour_18to19_rece_cnt = contact_hour_18_rece_cnt + contact_hour_19_rece_cnt
        contact_hour_20to21_rece_cnt = contact_hour_20_rece_cnt + contact_hour_21_rece_cnt
        contact_hour_22to23_rece_cnt = contact_hour_22_rece_cnt + contact_hour_23_rece_cnt

        contact_hour_0to1_rece_min_tot = contact_hour_0_rece_min_tot + contact_hour_1_rece_min_tot
        contact_hour_2to3_rece_min_tot = contact_hour_2_rece_min_tot + contact_hour_3_rece_min_tot
        contact_hour_4to5_rece_min_tot = contact_hour_4_rece_min_tot + contact_hour_5_rece_min_tot
        contact_hour_6to7_rece_min_tot = contact_hour_6_rece_min_tot + contact_hour_7_rece_min_tot
        contact_hour_8to9_rece_min_tot = contact_hour_8_rece_min_tot + contact_hour_9_rece_min_tot
        contact_hour_10to11_rece_min_tot = contact_hour_10_rece_min_tot + contact_hour_11_rece_min_tot
        contact_hour_12to13_rece_min_tot = contact_hour_12_rece_min_tot + contact_hour_13_rece_min_tot
        contact_hour_14to15_rece_min_tot = contact_hour_14_rece_min_tot + contact_hour_15_rece_min_tot
        contact_hour_16to17_rece_min_tot = contact_hour_16_rece_min_tot + contact_hour_17_rece_min_tot
        contact_hour_18to19_rece_min_tot = contact_hour_18_rece_min_tot + contact_hour_19_rece_min_tot
        contact_hour_20to21_rece_min_tot = contact_hour_20_rece_min_tot + contact_hour_21_rece_min_tot
        contact_hour_22to23_rece_min_tot = contact_hour_22_rece_min_tot + contact_hour_23_rece_min_tot

        contact_hour_0to1_rece_cnt_6_mon = contact_hour_0_rece_cnt_6_mon + contact_hour_1_rece_cnt_6_mon
        contact_hour_2to3_rece_cnt_6_mon = contact_hour_2_rece_cnt_6_mon + contact_hour_3_rece_cnt_6_mon
        contact_hour_4to5_rece_cnt_6_mon = contact_hour_4_rece_cnt_6_mon + contact_hour_5_rece_cnt_6_mon
        contact_hour_6to7_rece_cnt_6_mon = contact_hour_6_rece_cnt_6_mon + contact_hour_7_rece_cnt_6_mon
        contact_hour_8to9_rece_cnt_6_mon = contact_hour_8_rece_cnt_6_mon + contact_hour_9_rece_cnt_6_mon
        contact_hour_10to11_rece_cnt_6_mon = contact_hour_10_rece_cnt_6_mon + contact_hour_11_rece_cnt_6_mon
        contact_hour_12to13_rece_cnt_6_mon = contact_hour_12_rece_cnt_6_mon + contact_hour_13_rece_cnt_6_mon
        contact_hour_14to15_rece_cnt_6_mon = contact_hour_14_rece_cnt_6_mon + contact_hour_15_rece_cnt_6_mon
        contact_hour_16to17_rece_cnt_6_mon = contact_hour_16_rece_cnt_6_mon + contact_hour_17_rece_cnt_6_mon
        contact_hour_18to19_rece_cnt_6_mon = contact_hour_18_rece_cnt_6_mon + contact_hour_19_rece_cnt_6_mon
        contact_hour_20to21_rece_cnt_6_mon = contact_hour_20_rece_cnt_6_mon + contact_hour_21_rece_cnt_6_mon
        contact_hour_22to23_rece_cnt_6_mon = contact_hour_22_rece_cnt_6_mon + contact_hour_23_rece_cnt_6_mon

        contact_hour_0to1_rece_min_tot_6_mon = contact_hour_0_rece_min_tot_6_mon + contact_hour_1_rece_min_tot_6_mon
        contact_hour_2to3_rece_min_tot_6_mon = contact_hour_2_rece_min_tot_6_mon + contact_hour_3_rece_min_tot_6_mon
        contact_hour_4to5_rece_min_tot_6_mon = contact_hour_4_rece_min_tot_6_mon + contact_hour_5_rece_min_tot_6_mon
        contact_hour_6to7_rece_min_tot_6_mon = contact_hour_6_rece_min_tot_6_mon + contact_hour_7_rece_min_tot_6_mon
        contact_hour_8to9_rece_min_tot_6_mon = contact_hour_8_rece_min_tot_6_mon + contact_hour_9_rece_min_tot_6_mon
        contact_hour_10to11_rece_min_tot_6_mon = contact_hour_10_rece_min_tot_6_mon + contact_hour_11_rece_min_tot_6_mon
        contact_hour_12to13_rece_min_tot_6_mon = contact_hour_12_rece_min_tot_6_mon + contact_hour_13_rece_min_tot_6_mon
        contact_hour_14to15_rece_min_tot_6_mon = contact_hour_14_rece_min_tot_6_mon + contact_hour_15_rece_min_tot_6_mon
        contact_hour_16to17_rece_min_tot_6_mon = contact_hour_16_rece_min_tot_6_mon + contact_hour_17_rece_min_tot_6_mon
        contact_hour_18to19_rece_min_tot_6_mon = contact_hour_18_rece_min_tot_6_mon + contact_hour_19_rece_min_tot_6_mon
        contact_hour_20to21_rece_min_tot_6_mon = contact_hour_20_rece_min_tot_6_mon + contact_hour_21_rece_min_tot_6_mon
        contact_hour_22to23_rece_min_tot_6_mon = contact_hour_22_rece_min_tot_6_mon + contact_hour_23_rece_min_tot_6_mon

        contact_hour_0to1_rece_cnt_3_mon = contact_hour_0_rece_cnt_3_mon + contact_hour_1_rece_cnt_3_mon
        contact_hour_2to3_rece_cnt_3_mon = contact_hour_2_rece_cnt_3_mon + contact_hour_3_rece_cnt_3_mon
        contact_hour_4to5_rece_cnt_3_mon = contact_hour_4_rece_cnt_3_mon + contact_hour_5_rece_cnt_3_mon
        contact_hour_6to7_rece_cnt_3_mon = contact_hour_6_rece_cnt_3_mon + contact_hour_7_rece_cnt_3_mon
        contact_hour_8to9_rece_cnt_3_mon = contact_hour_8_rece_cnt_3_mon + contact_hour_9_rece_cnt_3_mon
        contact_hour_10to11_rece_cnt_3_mon = contact_hour_10_rece_cnt_3_mon + contact_hour_11_rece_cnt_3_mon
        contact_hour_12to13_rece_cnt_3_mon = contact_hour_12_rece_cnt_3_mon + contact_hour_13_rece_cnt_3_mon
        contact_hour_14to15_rece_cnt_3_mon = contact_hour_14_rece_cnt_3_mon + contact_hour_15_rece_cnt_3_mon
        contact_hour_16to17_rece_cnt_3_mon = contact_hour_16_rece_cnt_3_mon + contact_hour_17_rece_cnt_3_mon
        contact_hour_18to19_rece_cnt_3_mon = contact_hour_18_rece_cnt_3_mon + contact_hour_19_rece_cnt_3_mon
        contact_hour_20to21_rece_cnt_3_mon = contact_hour_20_rece_cnt_3_mon + contact_hour_21_rece_cnt_3_mon
        contact_hour_22to23_rece_cnt_3_mon = contact_hour_22_rece_cnt_3_mon + contact_hour_23_rece_cnt_3_mon

        contact_hour_0to1_rece_min_tot_3_mon = contact_hour_0_rece_min_tot_3_mon + contact_hour_1_rece_min_tot_3_mon
        contact_hour_2to3_rece_min_tot_3_mon = contact_hour_2_rece_min_tot_3_mon + contact_hour_3_rece_min_tot_3_mon
        contact_hour_4to5_rece_min_tot_3_mon = contact_hour_4_rece_min_tot_3_mon + contact_hour_5_rece_min_tot_3_mon
        contact_hour_6to7_rece_min_tot_3_mon = contact_hour_6_rece_min_tot_3_mon + contact_hour_7_rece_min_tot_3_mon
        contact_hour_8to9_rece_min_tot_3_mon = contact_hour_8_rece_min_tot_3_mon + contact_hour_9_rece_min_tot_3_mon
        contact_hour_10to11_rece_min_tot_3_mon = contact_hour_10_rece_min_tot_3_mon + contact_hour_11_rece_min_tot_3_mon
        contact_hour_12to13_rece_min_tot_3_mon = contact_hour_12_rece_min_tot_3_mon + contact_hour_13_rece_min_tot_3_mon
        contact_hour_14to15_rece_min_tot_3_mon = contact_hour_14_rece_min_tot_3_mon + contact_hour_15_rece_min_tot_3_mon
        contact_hour_16to17_rece_min_tot_3_mon = contact_hour_16_rece_min_tot_3_mon + contact_hour_17_rece_min_tot_3_mon
        contact_hour_18to19_rece_min_tot_3_mon = contact_hour_18_rece_min_tot_3_mon + contact_hour_19_rece_min_tot_3_mon
        contact_hour_20to21_rece_min_tot_3_mon = contact_hour_20_rece_min_tot_3_mon + contact_hour_21_rece_min_tot_3_mon
        contact_hour_22to23_rece_min_tot_3_mon = contact_hour_22_rece_min_tot_3_mon + contact_hour_23_rece_min_tot_3_mon

        contact_hour_0to1_rece_cnt_2_mon = contact_hour_0_rece_cnt_2_mon + contact_hour_1_rece_cnt_2_mon
        contact_hour_2to3_rece_cnt_2_mon = contact_hour_2_rece_cnt_2_mon + contact_hour_3_rece_cnt_2_mon
        contact_hour_4to5_rece_cnt_2_mon = contact_hour_4_rece_cnt_2_mon + contact_hour_5_rece_cnt_2_mon
        contact_hour_6to7_rece_cnt_2_mon = contact_hour_6_rece_cnt_2_mon + contact_hour_7_rece_cnt_2_mon
        contact_hour_8to9_rece_cnt_2_mon = contact_hour_8_rece_cnt_2_mon + contact_hour_9_rece_cnt_2_mon
        contact_hour_10to11_rece_cnt_2_mon = contact_hour_10_rece_cnt_2_mon + contact_hour_11_rece_cnt_2_mon
        contact_hour_12to13_rece_cnt_2_mon = contact_hour_12_rece_cnt_2_mon + contact_hour_13_rece_cnt_2_mon
        contact_hour_14to15_rece_cnt_2_mon = contact_hour_14_rece_cnt_2_mon + contact_hour_15_rece_cnt_2_mon
        contact_hour_16to17_rece_cnt_2_mon = contact_hour_16_rece_cnt_2_mon + contact_hour_17_rece_cnt_2_mon
        contact_hour_18to19_rece_cnt_2_mon = contact_hour_18_rece_cnt_2_mon + contact_hour_19_rece_cnt_2_mon
        contact_hour_20to21_rece_cnt_2_mon = contact_hour_20_rece_cnt_2_mon + contact_hour_21_rece_cnt_2_mon
        contact_hour_22to23_rece_cnt_2_mon = contact_hour_22_rece_cnt_2_mon + contact_hour_23_rece_cnt_2_mon

        contact_hour_0to1_rece_min_tot_2_mon = contact_hour_0_rece_min_tot_2_mon + contact_hour_1_rece_min_tot_2_mon
        contact_hour_2to3_rece_min_tot_2_mon = contact_hour_2_rece_min_tot_2_mon + contact_hour_3_rece_min_tot_2_mon
        contact_hour_4to5_rece_min_tot_2_mon = contact_hour_4_rece_min_tot_2_mon + contact_hour_5_rece_min_tot_2_mon
        contact_hour_6to7_rece_min_tot_2_mon = contact_hour_6_rece_min_tot_2_mon + contact_hour_7_rece_min_tot_2_mon
        contact_hour_8to9_rece_min_tot_2_mon = contact_hour_8_rece_min_tot_2_mon + contact_hour_9_rece_min_tot_2_mon
        contact_hour_10to11_rece_min_tot_2_mon = contact_hour_10_rece_min_tot_2_mon + contact_hour_11_rece_min_tot_2_mon
        contact_hour_12to13_rece_min_tot_2_mon = contact_hour_12_rece_min_tot_2_mon + contact_hour_13_rece_min_tot_2_mon
        contact_hour_14to15_rece_min_tot_2_mon = contact_hour_14_rece_min_tot_2_mon + contact_hour_15_rece_min_tot_2_mon
        contact_hour_16to17_rece_min_tot_2_mon = contact_hour_16_rece_min_tot_2_mon + contact_hour_17_rece_min_tot_2_mon
        contact_hour_18to19_rece_min_tot_2_mon = contact_hour_18_rece_min_tot_2_mon + contact_hour_19_rece_min_tot_2_mon
        contact_hour_20to21_rece_min_tot_2_mon = contact_hour_20_rece_min_tot_2_mon + contact_hour_21_rece_min_tot_2_mon
        contact_hour_22to23_rece_min_tot_2_mon = contact_hour_22_rece_min_tot_2_mon + contact_hour_23_rece_min_tot_2_mon

        contact_hour_0to1_rece_cnt_1_mon = contact_hour_0_rece_cnt_1_mon + contact_hour_1_rece_cnt_1_mon
        contact_hour_2to3_rece_cnt_1_mon = contact_hour_2_rece_cnt_1_mon + contact_hour_3_rece_cnt_1_mon
        contact_hour_4to5_rece_cnt_1_mon = contact_hour_4_rece_cnt_1_mon + contact_hour_5_rece_cnt_1_mon
        contact_hour_6to7_rece_cnt_1_mon = contact_hour_6_rece_cnt_1_mon + contact_hour_7_rece_cnt_1_mon
        contact_hour_8to9_rece_cnt_1_mon = contact_hour_8_rece_cnt_1_mon + contact_hour_9_rece_cnt_1_mon
        contact_hour_10to11_rece_cnt_1_mon = contact_hour_10_rece_cnt_1_mon + contact_hour_11_rece_cnt_1_mon
        contact_hour_12to13_rece_cnt_1_mon = contact_hour_12_rece_cnt_1_mon + contact_hour_13_rece_cnt_1_mon
        contact_hour_14to15_rece_cnt_1_mon = contact_hour_14_rece_cnt_1_mon + contact_hour_15_rece_cnt_1_mon
        contact_hour_16to17_rece_cnt_1_mon = contact_hour_16_rece_cnt_1_mon + contact_hour_17_rece_cnt_1_mon
        contact_hour_18to19_rece_cnt_1_mon = contact_hour_18_rece_cnt_1_mon + contact_hour_19_rece_cnt_1_mon
        contact_hour_20to21_rece_cnt_1_mon = contact_hour_20_rece_cnt_1_mon + contact_hour_21_rece_cnt_1_mon
        contact_hour_22to23_rece_cnt_1_mon = contact_hour_22_rece_cnt_1_mon + contact_hour_23_rece_cnt_1_mon

        contact_hour_0to1_rece_min_tot_1_mon = contact_hour_0_rece_min_tot_1_mon + contact_hour_1_rece_min_tot_1_mon
        contact_hour_2to3_rece_min_tot_1_mon = contact_hour_2_rece_min_tot_1_mon + contact_hour_3_rece_min_tot_1_mon
        contact_hour_4to5_rece_min_tot_1_mon = contact_hour_4_rece_min_tot_1_mon + contact_hour_5_rece_min_tot_1_mon
        contact_hour_6to7_rece_min_tot_1_mon = contact_hour_6_rece_min_tot_1_mon + contact_hour_7_rece_min_tot_1_mon
        contact_hour_8to9_rece_min_tot_1_mon = contact_hour_8_rece_min_tot_1_mon + contact_hour_9_rece_min_tot_1_mon
        contact_hour_10to11_rece_min_tot_1_mon = contact_hour_10_rece_min_tot_1_mon + contact_hour_11_rece_min_tot_1_mon
        contact_hour_12to13_rece_min_tot_1_mon = contact_hour_12_rece_min_tot_1_mon + contact_hour_13_rece_min_tot_1_mon
        contact_hour_14to15_rece_min_tot_1_mon = contact_hour_14_rece_min_tot_1_mon + contact_hour_15_rece_min_tot_1_mon
        contact_hour_16to17_rece_min_tot_1_mon = contact_hour_16_rece_min_tot_1_mon + contact_hour_17_rece_min_tot_1_mon
        contact_hour_18to19_rece_min_tot_1_mon = contact_hour_18_rece_min_tot_1_mon + contact_hour_19_rece_min_tot_1_mon
        contact_hour_20to21_rece_min_tot_1_mon = contact_hour_20_rece_min_tot_1_mon + contact_hour_21_rece_min_tot_1_mon
        contact_hour_22to23_rece_min_tot_1_mon = contact_hour_22_rece_min_tot_1_mon + contact_hour_23_rece_min_tot_1_mon

        contact_hour_0to1_rece_cnt_2_wk = contact_hour_0_rece_cnt_2_wk + contact_hour_1_rece_cnt_2_wk
        contact_hour_2to3_rece_cnt_2_wk = contact_hour_2_rece_cnt_2_wk + contact_hour_3_rece_cnt_2_wk
        contact_hour_4to5_rece_cnt_2_wk = contact_hour_4_rece_cnt_2_wk + contact_hour_5_rece_cnt_2_wk
        contact_hour_6to7_rece_cnt_2_wk = contact_hour_6_rece_cnt_2_wk + contact_hour_7_rece_cnt_2_wk
        contact_hour_8to9_rece_cnt_2_wk = contact_hour_8_rece_cnt_2_wk + contact_hour_9_rece_cnt_2_wk
        contact_hour_10to11_rece_cnt_2_wk = contact_hour_10_rece_cnt_2_wk + contact_hour_11_rece_cnt_2_wk
        contact_hour_12to13_rece_cnt_2_wk = contact_hour_12_rece_cnt_2_wk + contact_hour_13_rece_cnt_2_wk
        contact_hour_14to15_rece_cnt_2_wk = contact_hour_14_rece_cnt_2_wk + contact_hour_15_rece_cnt_2_wk
        contact_hour_16to17_rece_cnt_2_wk = contact_hour_16_rece_cnt_2_wk + contact_hour_17_rece_cnt_2_wk
        contact_hour_18to19_rece_cnt_2_wk = contact_hour_18_rece_cnt_2_wk + contact_hour_19_rece_cnt_2_wk
        contact_hour_20to21_rece_cnt_2_wk = contact_hour_20_rece_cnt_2_wk + contact_hour_21_rece_cnt_2_wk
        contact_hour_22to23_rece_cnt_2_wk = contact_hour_22_rece_cnt_2_wk + contact_hour_23_rece_cnt_2_wk

        contact_hour_0to1_rece_min_tot_2_wk = contact_hour_0_rece_min_tot_2_wk + contact_hour_1_rece_min_tot_2_wk
        contact_hour_2to3_rece_min_tot_2_wk = contact_hour_2_rece_min_tot_2_wk + contact_hour_3_rece_min_tot_2_wk
        contact_hour_4to5_rece_min_tot_2_wk = contact_hour_4_rece_min_tot_2_wk + contact_hour_5_rece_min_tot_2_wk
        contact_hour_6to7_rece_min_tot_2_wk = contact_hour_6_rece_min_tot_2_wk + contact_hour_7_rece_min_tot_2_wk
        contact_hour_8to9_rece_min_tot_2_wk = contact_hour_8_rece_min_tot_2_wk + contact_hour_9_rece_min_tot_2_wk
        contact_hour_10to11_rece_min_tot_2_wk = contact_hour_10_rece_min_tot_2_wk + contact_hour_11_rece_min_tot_2_wk
        contact_hour_12to13_rece_min_tot_2_wk = contact_hour_12_rece_min_tot_2_wk + contact_hour_13_rece_min_tot_2_wk
        contact_hour_14to15_rece_min_tot_2_wk = contact_hour_14_rece_min_tot_2_wk + contact_hour_15_rece_min_tot_2_wk
        contact_hour_16to17_rece_min_tot_2_wk = contact_hour_16_rece_min_tot_2_wk + contact_hour_17_rece_min_tot_2_wk
        contact_hour_18to19_rece_min_tot_2_wk = contact_hour_18_rece_min_tot_2_wk + contact_hour_19_rece_min_tot_2_wk
        contact_hour_20to21_rece_min_tot_2_wk = contact_hour_20_rece_min_tot_2_wk + contact_hour_21_rece_min_tot_2_wk
        contact_hour_22to23_rece_min_tot_2_wk = contact_hour_22_rece_min_tot_2_wk + contact_hour_23_rece_min_tot_2_wk

        contact_hour_1to6_rece_cnt = contact_hour_1_rece_cnt + contact_hour_2_rece_cnt + contact_hour_3_rece_cnt + contact_hour_4_rece_cnt + contact_hour_5_rece_cnt + contact_hour_6_rece_cnt
        contact_hour_7to12_rece_cnt = contact_hour_7_rece_cnt + contact_hour_8_rece_cnt + contact_hour_9_rece_cnt + contact_hour_10_rece_cnt + contact_hour_11_rece_cnt + contact_hour_12_rece_cnt
        contact_hour_13to18_rece_cnt = contact_hour_13_rece_cnt + contact_hour_14_rece_cnt + contact_hour_15_rece_cnt + contact_hour_16_rece_cnt + contact_hour_17_rece_cnt + contact_hour_18_rece_cnt
        contact_hour_19to0_rece_cnt = contact_hour_19_rece_cnt + contact_hour_20_rece_cnt + contact_hour_21_rece_cnt + contact_hour_22_rece_cnt + contact_hour_23_rece_cnt + contact_hour_0_rece_cnt

        contact_hour_1to6_rece_min_tot = contact_hour_1_rece_min_tot + contact_hour_2_rece_min_tot + contact_hour_3_rece_min_tot + contact_hour_4_rece_min_tot + contact_hour_5_rece_min_tot + contact_hour_6_rece_min_tot
        contact_hour_7to12_rece_min_tot = contact_hour_7_rece_min_tot + contact_hour_8_rece_min_tot + contact_hour_9_rece_min_tot + contact_hour_10_rece_min_tot + contact_hour_11_rece_min_tot + contact_hour_12_rece_min_tot
        contact_hour_13to18_rece_min_tot = contact_hour_13_rece_min_tot + contact_hour_14_rece_min_tot + contact_hour_15_rece_min_tot + contact_hour_16_rece_min_tot + contact_hour_17_rece_min_tot + contact_hour_18_rece_min_tot
        contact_hour_19to0_rece_min_tot = contact_hour_19_rece_min_tot + contact_hour_20_rece_min_tot + contact_hour_21_rece_min_tot + contact_hour_22_rece_min_tot + contact_hour_23_rece_min_tot + contact_hour_0_rece_min_tot

        contact_hour_1to6_rece_cnt_6_mon = contact_hour_1_rece_cnt_6_mon + contact_hour_2_rece_cnt_6_mon + contact_hour_3_rece_cnt_6_mon + contact_hour_4_rece_cnt_6_mon + contact_hour_5_rece_cnt_6_mon + contact_hour_6_rece_cnt_6_mon
        contact_hour_7to12_rece_cnt_6_mon = contact_hour_7_rece_cnt_6_mon + contact_hour_8_rece_cnt_6_mon + contact_hour_9_rece_cnt_6_mon + contact_hour_10_rece_cnt_6_mon + contact_hour_11_rece_cnt_6_mon + contact_hour_12_rece_cnt_6_mon
        contact_hour_13to18_rece_cnt_6_mon = contact_hour_13_rece_cnt_6_mon + contact_hour_14_rece_cnt_6_mon + contact_hour_15_rece_cnt_6_mon + contact_hour_16_rece_cnt_6_mon + contact_hour_17_rece_cnt_6_mon + contact_hour_18_rece_cnt_6_mon
        contact_hour_19to0_rece_cnt_6_mon = contact_hour_19_rece_cnt_6_mon + contact_hour_20_rece_cnt_6_mon + contact_hour_21_rece_cnt_6_mon + contact_hour_22_rece_cnt_6_mon + contact_hour_23_rece_cnt_6_mon + contact_hour_0_rece_cnt_6_mon

        contact_hour_1to6_rece_min_tot_6_mon = contact_hour_1_rece_min_tot_6_mon + contact_hour_2_rece_min_tot_6_mon + contact_hour_3_rece_min_tot_6_mon + contact_hour_4_rece_min_tot_6_mon + contact_hour_5_rece_min_tot_6_mon + contact_hour_6_rece_min_tot_6_mon
        contact_hour_7to12_rece_min_tot_6_mon = contact_hour_7_rece_min_tot_6_mon + contact_hour_8_rece_min_tot_6_mon + contact_hour_9_rece_min_tot_6_mon + contact_hour_10_rece_min_tot_6_mon + contact_hour_11_rece_min_tot_6_mon + contact_hour_12_rece_min_tot_6_mon
        contact_hour_13to18_rece_min_tot_6_mon = contact_hour_13_rece_min_tot_6_mon + contact_hour_14_rece_min_tot_6_mon + contact_hour_15_rece_min_tot_6_mon + contact_hour_16_rece_min_tot_6_mon + contact_hour_17_rece_min_tot_6_mon + contact_hour_18_rece_min_tot_6_mon
        contact_hour_19to0_rece_min_tot_6_mon = contact_hour_19_rece_min_tot_6_mon + contact_hour_20_rece_min_tot_6_mon + contact_hour_21_rece_min_tot_6_mon + contact_hour_22_rece_min_tot_6_mon + contact_hour_23_rece_min_tot_6_mon + contact_hour_0_rece_min_tot_6_mon

        contact_hour_1to6_rece_cnt_3_mon = contact_hour_1_rece_cnt_3_mon + contact_hour_2_rece_cnt_3_mon + contact_hour_3_rece_cnt_3_mon + contact_hour_4_rece_cnt_3_mon + contact_hour_5_rece_cnt_3_mon + contact_hour_6_rece_cnt_3_mon
        contact_hour_7to12_rece_cnt_3_mon = contact_hour_7_rece_cnt_3_mon + contact_hour_8_rece_cnt_3_mon + contact_hour_9_rece_cnt_3_mon + contact_hour_10_rece_cnt_3_mon + contact_hour_11_rece_cnt_3_mon + contact_hour_12_rece_cnt_3_mon
        contact_hour_13to18_rece_cnt_3_mon = contact_hour_13_rece_cnt_3_mon + contact_hour_14_rece_cnt_3_mon + contact_hour_15_rece_cnt_3_mon + contact_hour_16_rece_cnt_3_mon + contact_hour_17_rece_cnt_3_mon + contact_hour_18_rece_cnt_3_mon
        contact_hour_19to0_rece_cnt_3_mon = contact_hour_19_rece_cnt_3_mon + contact_hour_20_rece_cnt_3_mon + contact_hour_21_rece_cnt_3_mon + contact_hour_22_rece_cnt_3_mon + contact_hour_23_rece_cnt_3_mon + contact_hour_0_rece_cnt_3_mon

        contact_hour_1to6_rece_min_tot_3_mon = contact_hour_1_rece_min_tot_3_mon + contact_hour_2_rece_min_tot_3_mon + contact_hour_3_rece_min_tot_3_mon + contact_hour_4_rece_min_tot_3_mon + contact_hour_5_rece_min_tot_3_mon + contact_hour_6_rece_min_tot_3_mon
        contact_hour_7to12_rece_min_tot_3_mon = contact_hour_7_rece_min_tot_3_mon + contact_hour_8_rece_min_tot_3_mon + contact_hour_9_rece_min_tot_3_mon + contact_hour_10_rece_min_tot_3_mon + contact_hour_11_rece_min_tot_3_mon + contact_hour_12_rece_min_tot_3_mon
        contact_hour_13to18_rece_min_tot_3_mon = contact_hour_13_rece_min_tot_3_mon + contact_hour_14_rece_min_tot_3_mon + contact_hour_15_rece_min_tot_3_mon + contact_hour_16_rece_min_tot_3_mon + contact_hour_17_rece_min_tot_3_mon + contact_hour_18_rece_min_tot_3_mon
        contact_hour_19to0_rece_min_tot_3_mon = contact_hour_19_rece_min_tot_3_mon + contact_hour_20_rece_min_tot_3_mon + contact_hour_21_rece_min_tot_3_mon + contact_hour_22_rece_min_tot_3_mon + contact_hour_23_rece_min_tot_3_mon + contact_hour_0_rece_min_tot_3_mon

        contact_hour_1to6_rece_cnt_2_mon = contact_hour_1_rece_cnt_2_mon + contact_hour_2_rece_cnt_2_mon + contact_hour_3_rece_cnt_2_mon + contact_hour_4_rece_cnt_2_mon + contact_hour_5_rece_cnt_2_mon + contact_hour_6_rece_cnt_2_mon
        contact_hour_7to12_rece_cnt_2_mon = contact_hour_7_rece_cnt_2_mon + contact_hour_8_rece_cnt_2_mon + contact_hour_9_rece_cnt_2_mon + contact_hour_10_rece_cnt_2_mon + contact_hour_11_rece_cnt_2_mon + contact_hour_12_rece_cnt_2_mon
        contact_hour_13to18_rece_cnt_2_mon = contact_hour_13_rece_cnt_2_mon + contact_hour_14_rece_cnt_2_mon + contact_hour_15_rece_cnt_2_mon + contact_hour_16_rece_cnt_2_mon + contact_hour_17_rece_cnt_2_mon + contact_hour_18_rece_cnt_2_mon
        contact_hour_19to0_rece_cnt_2_mon = contact_hour_19_rece_cnt_2_mon + contact_hour_20_rece_cnt_2_mon + contact_hour_21_rece_cnt_2_mon + contact_hour_22_rece_cnt_2_mon + contact_hour_23_rece_cnt_2_mon + contact_hour_0_rece_cnt_2_mon

        contact_hour_1to6_rece_min_tot_2_mon = contact_hour_1_rece_min_tot_2_mon + contact_hour_2_rece_min_tot_2_mon + contact_hour_3_rece_min_tot_2_mon + contact_hour_4_rece_min_tot_2_mon + contact_hour_5_rece_min_tot_2_mon + contact_hour_6_rece_min_tot_2_mon
        contact_hour_7to12_rece_min_tot_2_mon = contact_hour_7_rece_min_tot_2_mon + contact_hour_8_rece_min_tot_2_mon + contact_hour_9_rece_min_tot_2_mon + contact_hour_10_rece_min_tot_2_mon + contact_hour_11_rece_min_tot_2_mon + contact_hour_12_rece_min_tot_2_mon
        contact_hour_13to18_rece_min_tot_2_mon = contact_hour_13_rece_min_tot_2_mon + contact_hour_14_rece_min_tot_2_mon + contact_hour_15_rece_min_tot_2_mon + contact_hour_16_rece_min_tot_2_mon + contact_hour_17_rece_min_tot_2_mon + contact_hour_18_rece_min_tot_2_mon
        contact_hour_19to0_rece_min_tot_2_mon = contact_hour_19_rece_min_tot_2_mon + contact_hour_20_rece_min_tot_2_mon + contact_hour_21_rece_min_tot_2_mon + contact_hour_22_rece_min_tot_2_mon + contact_hour_23_rece_min_tot_2_mon + contact_hour_0_rece_min_tot_2_mon

        contact_hour_1to6_rece_cnt_1_mon = contact_hour_1_rece_cnt_1_mon + contact_hour_2_rece_cnt_1_mon + contact_hour_3_rece_cnt_1_mon + contact_hour_4_rece_cnt_1_mon + contact_hour_5_rece_cnt_1_mon + contact_hour_6_rece_cnt_1_mon
        contact_hour_7to12_rece_cnt_1_mon = contact_hour_7_rece_cnt_1_mon + contact_hour_8_rece_cnt_1_mon + contact_hour_9_rece_cnt_1_mon + contact_hour_10_rece_cnt_1_mon + contact_hour_11_rece_cnt_1_mon + contact_hour_12_rece_cnt_1_mon
        contact_hour_13to18_rece_cnt_1_mon = contact_hour_13_rece_cnt_1_mon + contact_hour_14_rece_cnt_1_mon + contact_hour_15_rece_cnt_1_mon + contact_hour_16_rece_cnt_1_mon + contact_hour_17_rece_cnt_1_mon + contact_hour_18_rece_cnt_1_mon
        contact_hour_19to0_rece_cnt_1_mon = contact_hour_19_rece_cnt_1_mon + contact_hour_20_rece_cnt_1_mon + contact_hour_21_rece_cnt_1_mon + contact_hour_22_rece_cnt_1_mon + contact_hour_23_rece_cnt_1_mon + contact_hour_0_rece_cnt_1_mon

        contact_hour_1to6_rece_min_tot_1_mon = contact_hour_1_rece_min_tot_1_mon + contact_hour_2_rece_min_tot_1_mon + contact_hour_3_rece_min_tot_1_mon + contact_hour_4_rece_min_tot_1_mon + contact_hour_5_rece_min_tot_1_mon + contact_hour_6_rece_min_tot_1_mon
        contact_hour_7to12_rece_min_tot_1_mon = contact_hour_7_rece_min_tot_1_mon + contact_hour_8_rece_min_tot_1_mon + contact_hour_9_rece_min_tot_1_mon + contact_hour_10_rece_min_tot_1_mon + contact_hour_11_rece_min_tot_1_mon + contact_hour_12_rece_min_tot_1_mon
        contact_hour_13to18_rece_min_tot_1_mon = contact_hour_13_rece_min_tot_1_mon + contact_hour_14_rece_min_tot_1_mon + contact_hour_15_rece_min_tot_1_mon + contact_hour_16_rece_min_tot_1_mon + contact_hour_17_rece_min_tot_1_mon + contact_hour_18_rece_min_tot_1_mon
        contact_hour_19to0_rece_min_tot_1_mon = contact_hour_19_rece_min_tot_1_mon + contact_hour_20_rece_min_tot_1_mon + contact_hour_21_rece_min_tot_1_mon + contact_hour_22_rece_min_tot_1_mon + contact_hour_23_rece_min_tot_1_mon + contact_hour_0_rece_min_tot_1_mon

        contact_hour_1to6_rece_cnt_2_wk = contact_hour_1_rece_cnt_2_wk + contact_hour_2_rece_cnt_2_wk + contact_hour_3_rece_cnt_2_wk + contact_hour_4_rece_cnt_2_wk + contact_hour_5_rece_cnt_2_wk + contact_hour_6_rece_cnt_2_wk
        contact_hour_7to12_rece_cnt_2_wk = contact_hour_7_rece_cnt_2_wk + contact_hour_8_rece_cnt_2_wk + contact_hour_9_rece_cnt_2_wk + contact_hour_10_rece_cnt_2_wk + contact_hour_11_rece_cnt_2_wk + contact_hour_12_rece_cnt_2_wk
        contact_hour_13to18_rece_cnt_2_wk = contact_hour_13_rece_cnt_2_wk + contact_hour_14_rece_cnt_2_wk + contact_hour_15_rece_cnt_2_wk + contact_hour_16_rece_cnt_2_wk + contact_hour_17_rece_cnt_2_wk + contact_hour_18_rece_cnt_2_wk
        contact_hour_19to0_rece_cnt_2_wk = contact_hour_19_rece_cnt_2_wk + contact_hour_20_rece_cnt_2_wk + contact_hour_21_rece_cnt_2_wk + contact_hour_22_rece_cnt_2_wk + contact_hour_23_rece_cnt_2_wk + contact_hour_0_rece_cnt_2_wk

        contact_hour_1to6_rece_min_tot_2_wk = contact_hour_1_rece_min_tot_2_wk + contact_hour_2_rece_min_tot_2_wk + contact_hour_3_rece_min_tot_2_wk + contact_hour_4_rece_min_tot_2_wk + contact_hour_5_rece_min_tot_2_wk + contact_hour_6_rece_min_tot_2_wk
        contact_hour_7to12_rece_min_tot_2_wk = contact_hour_7_rece_min_tot_2_wk + contact_hour_8_rece_min_tot_2_wk + contact_hour_9_rece_min_tot_2_wk + contact_hour_10_rece_min_tot_2_wk + contact_hour_11_rece_min_tot_2_wk + contact_hour_12_rece_min_tot_2_wk
        contact_hour_13to18_rece_min_tot_2_wk = contact_hour_13_rece_min_tot_2_wk + contact_hour_14_rece_min_tot_2_wk + contact_hour_15_rece_min_tot_2_wk + contact_hour_16_rece_min_tot_2_wk + contact_hour_17_rece_min_tot_2_wk + contact_hour_18_rece_min_tot_2_wk
        contact_hour_19to0_rece_min_tot_2_wk = contact_hour_19_rece_min_tot_2_wk + contact_hour_20_rece_min_tot_2_wk + contact_hour_21_rece_min_tot_2_wk + contact_hour_22_rece_min_tot_2_wk + contact_hour_23_rece_min_tot_2_wk + contact_hour_0_rece_min_tot_2_wk

        contact_hour_1to8_rece_cnt = contact_hour_1_rece_cnt + contact_hour_2_rece_cnt + contact_hour_3_rece_cnt + contact_hour_4_rece_cnt + contact_hour_5_rece_cnt + contact_hour_6_rece_cnt + contact_hour_7_rece_cnt + contact_hour_8_rece_cnt
        contact_hour_9to16_rece_cnt = contact_hour_9_rece_cnt + contact_hour_10_rece_cnt + contact_hour_11_rece_cnt + contact_hour_12_rece_cnt + contact_hour_13_rece_cnt + contact_hour_14_rece_cnt + contact_hour_15_rece_cnt + contact_hour_16_rece_cnt
        contact_hour_17to0_rece_cnt = contact_hour_17_rece_cnt + contact_hour_18_rece_cnt + contact_hour_19_rece_cnt + contact_hour_20_rece_cnt + contact_hour_21_rece_cnt + contact_hour_22_rece_cnt + contact_hour_23_rece_cnt + contact_hour_0_rece_cnt

        contact_hour_1to8_rece_min_tot = contact_hour_1_rece_min_tot + contact_hour_2_rece_min_tot + contact_hour_3_rece_min_tot + contact_hour_4_rece_min_tot + contact_hour_5_rece_min_tot + contact_hour_6_rece_min_tot + contact_hour_7_rece_min_tot + contact_hour_8_rece_min_tot
        contact_hour_9to16_rece_min_tot = contact_hour_9_rece_min_tot + contact_hour_10_rece_min_tot + contact_hour_11_rece_min_tot + contact_hour_12_rece_min_tot + contact_hour_13_rece_min_tot + contact_hour_14_rece_min_tot + contact_hour_15_rece_min_tot + contact_hour_16_rece_min_tot
        contact_hour_17to0_rece_min_tot = contact_hour_17_rece_min_tot + contact_hour_18_rece_min_tot + contact_hour_19_rece_min_tot + contact_hour_20_rece_min_tot + contact_hour_21_rece_min_tot + contact_hour_22_rece_min_tot + contact_hour_23_rece_min_tot + contact_hour_0_rece_min_tot

        contact_hour_1to8_rece_cnt_6_mon = contact_hour_1_rece_cnt_6_mon + contact_hour_2_rece_cnt_6_mon + contact_hour_3_rece_cnt_6_mon + contact_hour_4_rece_cnt_6_mon + contact_hour_5_rece_cnt_6_mon + contact_hour_6_rece_cnt_6_mon + contact_hour_7_rece_cnt_6_mon + contact_hour_8_rece_cnt_6_mon
        contact_hour_9to16_rece_cnt_6_mon = contact_hour_9_rece_cnt_6_mon + contact_hour_10_rece_cnt_6_mon + contact_hour_11_rece_cnt_6_mon + contact_hour_12_rece_cnt_6_mon + contact_hour_13_rece_cnt_6_mon + contact_hour_14_rece_cnt_6_mon + contact_hour_15_rece_cnt_6_mon + contact_hour_16_rece_cnt_6_mon
        contact_hour_17to0_rece_cnt_6_mon = contact_hour_17_rece_cnt_6_mon + contact_hour_18_rece_cnt_6_mon + contact_hour_19_rece_cnt_6_mon + contact_hour_20_rece_cnt_6_mon + contact_hour_21_rece_cnt_6_mon + contact_hour_22_rece_cnt_6_mon + contact_hour_23_rece_cnt_6_mon + contact_hour_0_rece_cnt_6_mon

        contact_hour_1to8_rece_min_tot_6_mon = contact_hour_1_rece_min_tot_6_mon + contact_hour_2_rece_min_tot_6_mon + contact_hour_3_rece_min_tot_6_mon + contact_hour_4_rece_min_tot_6_mon + contact_hour_5_rece_min_tot_6_mon + contact_hour_6_rece_min_tot_6_mon + contact_hour_7_rece_min_tot_6_mon + contact_hour_8_rece_min_tot_6_mon
        contact_hour_9to16_rece_min_tot_6_mon = contact_hour_9_rece_min_tot_6_mon + contact_hour_10_rece_min_tot_6_mon + contact_hour_11_rece_min_tot_6_mon + contact_hour_12_rece_min_tot_6_mon + contact_hour_13_rece_min_tot_6_mon + contact_hour_14_rece_min_tot_6_mon + contact_hour_15_rece_min_tot_6_mon + contact_hour_16_rece_min_tot_6_mon
        contact_hour_17to0_rece_min_tot_6_mon = contact_hour_17_rece_min_tot_6_mon + contact_hour_18_rece_min_tot_6_mon + contact_hour_19_rece_min_tot_6_mon + contact_hour_20_rece_min_tot_6_mon + contact_hour_21_rece_min_tot_6_mon + contact_hour_22_rece_min_tot_6_mon + contact_hour_23_rece_min_tot_6_mon + contact_hour_0_rece_min_tot_6_mon

        contact_hour_1to8_rece_cnt_3_mon = contact_hour_1_rece_cnt_3_mon + contact_hour_2_rece_cnt_3_mon + contact_hour_3_rece_cnt_3_mon + contact_hour_4_rece_cnt_3_mon + contact_hour_5_rece_cnt_3_mon + contact_hour_6_rece_cnt_3_mon + contact_hour_7_rece_cnt_3_mon + contact_hour_8_rece_cnt_3_mon
        contact_hour_9to16_rece_cnt_3_mon = contact_hour_9_rece_cnt_3_mon + contact_hour_10_rece_cnt_3_mon + contact_hour_11_rece_cnt_3_mon + contact_hour_12_rece_cnt_3_mon + contact_hour_13_rece_cnt_3_mon + contact_hour_14_rece_cnt_3_mon + contact_hour_15_rece_cnt_3_mon + contact_hour_16_rece_cnt_3_mon
        contact_hour_17to0_rece_cnt_3_mon = contact_hour_17_rece_cnt_3_mon + contact_hour_18_rece_cnt_3_mon + contact_hour_19_rece_cnt_3_mon + contact_hour_20_rece_cnt_3_mon + contact_hour_21_rece_cnt_3_mon + contact_hour_22_rece_cnt_3_mon + contact_hour_23_rece_cnt_3_mon + contact_hour_0_rece_cnt_3_mon

        contact_hour_1to8_rece_min_tot_3_mon = contact_hour_1_rece_min_tot_3_mon + contact_hour_2_rece_min_tot_3_mon + contact_hour_3_rece_min_tot_3_mon + contact_hour_4_rece_min_tot_3_mon + contact_hour_5_rece_min_tot_3_mon + contact_hour_6_rece_min_tot_3_mon + contact_hour_7_rece_min_tot_3_mon + contact_hour_8_rece_min_tot_3_mon
        contact_hour_9to16_rece_min_tot_3_mon = contact_hour_9_rece_min_tot_3_mon + contact_hour_10_rece_min_tot_3_mon + contact_hour_11_rece_min_tot_3_mon + contact_hour_12_rece_min_tot_3_mon + contact_hour_13_rece_min_tot_3_mon + contact_hour_14_rece_min_tot_3_mon + contact_hour_15_rece_min_tot_3_mon + contact_hour_16_rece_min_tot_3_mon
        contact_hour_17to0_rece_min_tot_3_mon = contact_hour_17_rece_min_tot_3_mon + contact_hour_18_rece_min_tot_3_mon + contact_hour_19_rece_min_tot_3_mon + contact_hour_20_rece_min_tot_3_mon + contact_hour_21_rece_min_tot_3_mon + contact_hour_22_rece_min_tot_3_mon + contact_hour_23_rece_min_tot_3_mon + contact_hour_0_rece_min_tot_3_mon

        contact_hour_1to8_rece_cnt_2_mon = contact_hour_1_rece_cnt_2_mon + contact_hour_2_rece_cnt_2_mon + contact_hour_3_rece_cnt_2_mon + contact_hour_4_rece_cnt_2_mon + contact_hour_5_rece_cnt_2_mon + contact_hour_6_rece_cnt_2_mon + contact_hour_7_rece_cnt_2_mon + contact_hour_8_rece_cnt_2_mon
        contact_hour_9to16_rece_cnt_2_mon = contact_hour_9_rece_cnt_2_mon + contact_hour_10_rece_cnt_2_mon + contact_hour_11_rece_cnt_2_mon + contact_hour_12_rece_cnt_2_mon + contact_hour_13_rece_cnt_2_mon + contact_hour_14_rece_cnt_2_mon + contact_hour_15_rece_cnt_2_mon + contact_hour_16_rece_cnt_2_mon
        contact_hour_17to0_rece_cnt_2_mon = contact_hour_17_rece_cnt_2_mon + contact_hour_18_rece_cnt_2_mon + contact_hour_19_rece_cnt_2_mon + contact_hour_20_rece_cnt_2_mon + contact_hour_21_rece_cnt_2_mon + contact_hour_22_rece_cnt_2_mon + contact_hour_23_rece_cnt_2_mon + contact_hour_0_rece_cnt_2_mon

        contact_hour_1to8_rece_min_tot_2_mon = contact_hour_1_rece_min_tot_2_mon + contact_hour_2_rece_min_tot_2_mon + contact_hour_3_rece_min_tot_2_mon + contact_hour_4_rece_min_tot_2_mon + contact_hour_5_rece_min_tot_2_mon + contact_hour_6_rece_min_tot_2_mon + contact_hour_7_rece_min_tot_2_mon + contact_hour_8_rece_min_tot_2_mon
        contact_hour_9to16_rece_min_tot_2_mon = contact_hour_9_rece_min_tot_2_mon + contact_hour_10_rece_min_tot_2_mon + contact_hour_11_rece_min_tot_2_mon + contact_hour_12_rece_min_tot_2_mon + contact_hour_13_rece_min_tot_2_mon + contact_hour_14_rece_min_tot_2_mon + contact_hour_15_rece_min_tot_2_mon + contact_hour_16_rece_min_tot_2_mon
        contact_hour_17to0_rece_min_tot_2_mon = contact_hour_17_rece_min_tot_2_mon + contact_hour_18_rece_min_tot_2_mon + contact_hour_19_rece_min_tot_2_mon + contact_hour_20_rece_min_tot_2_mon + contact_hour_21_rece_min_tot_2_mon + contact_hour_22_rece_min_tot_2_mon + contact_hour_23_rece_min_tot_2_mon + contact_hour_0_rece_min_tot_2_mon

        contact_hour_1to8_rece_cnt_1_mon = contact_hour_1_rece_cnt_1_mon + contact_hour_2_rece_cnt_1_mon + contact_hour_3_rece_cnt_1_mon + contact_hour_4_rece_cnt_1_mon + contact_hour_5_rece_cnt_1_mon + contact_hour_6_rece_cnt_1_mon + contact_hour_7_rece_cnt_1_mon + contact_hour_8_rece_cnt_1_mon
        contact_hour_9to16_rece_cnt_1_mon = contact_hour_9_rece_cnt_1_mon + contact_hour_10_rece_cnt_1_mon + contact_hour_11_rece_cnt_1_mon + contact_hour_12_rece_cnt_1_mon + contact_hour_13_rece_cnt_1_mon + contact_hour_14_rece_cnt_1_mon + contact_hour_15_rece_cnt_1_mon + contact_hour_16_rece_cnt_1_mon
        contact_hour_17to0_rece_cnt_1_mon = contact_hour_17_rece_cnt_1_mon + contact_hour_18_rece_cnt_1_mon + contact_hour_19_rece_cnt_1_mon + contact_hour_20_rece_cnt_1_mon + contact_hour_21_rece_cnt_1_mon + contact_hour_22_rece_cnt_1_mon + contact_hour_23_rece_cnt_1_mon + contact_hour_0_rece_cnt_1_mon

        contact_hour_1to8_rece_min_tot_1_mon = contact_hour_1_rece_min_tot_1_mon + contact_hour_2_rece_min_tot_1_mon + contact_hour_3_rece_min_tot_1_mon + contact_hour_4_rece_min_tot_1_mon + contact_hour_5_rece_min_tot_1_mon + contact_hour_6_rece_min_tot_1_mon + contact_hour_7_rece_min_tot_1_mon + contact_hour_8_rece_min_tot_1_mon
        contact_hour_9to16_rece_min_tot_1_mon = contact_hour_9_rece_min_tot_1_mon + contact_hour_10_rece_min_tot_1_mon + contact_hour_11_rece_min_tot_1_mon + contact_hour_12_rece_min_tot_1_mon + contact_hour_13_rece_min_tot_1_mon + contact_hour_14_rece_min_tot_1_mon + contact_hour_15_rece_min_tot_1_mon + contact_hour_16_rece_min_tot_1_mon
        contact_hour_17to0_rece_min_tot_1_mon = contact_hour_17_rece_min_tot_1_mon + contact_hour_18_rece_min_tot_1_mon + contact_hour_19_rece_min_tot_1_mon + contact_hour_20_rece_min_tot_1_mon + contact_hour_21_rece_min_tot_1_mon + contact_hour_22_rece_min_tot_1_mon + contact_hour_23_rece_min_tot_1_mon + contact_hour_0_rece_min_tot_1_mon

        contact_hour_1to8_rece_cnt_2_wk = contact_hour_1_rece_cnt_2_wk + contact_hour_2_rece_cnt_2_wk + contact_hour_3_rece_cnt_2_wk + contact_hour_4_rece_cnt_2_wk + contact_hour_5_rece_cnt_2_wk + contact_hour_6_rece_cnt_2_wk + contact_hour_7_rece_cnt_2_wk + contact_hour_8_rece_cnt_2_wk
        contact_hour_9to16_rece_cnt_2_wk = contact_hour_9_rece_cnt_2_wk + contact_hour_10_rece_cnt_2_wk + contact_hour_11_rece_cnt_2_wk + contact_hour_12_rece_cnt_2_wk + contact_hour_13_rece_cnt_2_wk + contact_hour_14_rece_cnt_2_wk + contact_hour_15_rece_cnt_2_wk + contact_hour_16_rece_cnt_2_wk
        contact_hour_17to0_rece_cnt_2_wk = contact_hour_17_rece_cnt_2_wk + contact_hour_18_rece_cnt_2_wk + contact_hour_19_rece_cnt_2_wk + contact_hour_20_rece_cnt_2_wk + contact_hour_21_rece_cnt_2_wk + contact_hour_22_rece_cnt_2_wk + contact_hour_23_rece_cnt_2_wk + contact_hour_0_rece_cnt_2_wk

        contact_hour_1to8_rece_min_tot_2_wk = contact_hour_1_rece_min_tot_2_wk + contact_hour_2_rece_min_tot_2_wk + contact_hour_3_rece_min_tot_2_wk + contact_hour_4_rece_min_tot_2_wk + contact_hour_5_rece_min_tot_2_wk + contact_hour_6_rece_min_tot_2_wk + contact_hour_7_rece_min_tot_2_wk + contact_hour_8_rece_min_tot_2_wk
        contact_hour_9to16_rece_min_tot_2_wk = contact_hour_9_rece_min_tot_2_wk + contact_hour_10_rece_min_tot_2_wk + contact_hour_11_rece_min_tot_2_wk + contact_hour_12_rece_min_tot_2_wk + contact_hour_13_rece_min_tot_2_wk + contact_hour_14_rece_min_tot_2_wk + contact_hour_15_rece_min_tot_2_wk + contact_hour_16_rece_min_tot_2_wk
        contact_hour_17to0_rece_min_tot_2_wk = contact_hour_17_rece_min_tot_2_wk + contact_hour_18_rece_min_tot_2_wk + contact_hour_19_rece_min_tot_2_wk + contact_hour_20_rece_min_tot_2_wk + contact_hour_21_rece_min_tot_2_wk + contact_hour_22_rece_min_tot_2_wk + contact_hour_23_rece_min_tot_2_wk + contact_hour_0_rece_min_tot_2_wk

        contact_hour_9to20_rece_cnt = contact_hour_9_rece_cnt + contact_hour_10_rece_cnt + contact_hour_11_rece_cnt + contact_hour_12_rece_cnt + contact_hour_13_rece_cnt + contact_hour_14_rece_cnt + contact_hour_15_rece_cnt + contact_hour_16_rece_cnt + contact_hour_17_rece_cnt + contact_hour_18_rece_cnt + contact_hour_19_rece_cnt + contact_hour_20_rece_cnt
        contact_hour_21to8_rece_cnt = contact_hour_21_rece_cnt + contact_hour_22_rece_cnt + contact_hour_23_rece_cnt + contact_hour_0_rece_cnt + contact_hour_1_rece_cnt + contact_hour_2_rece_cnt + contact_hour_3_rece_cnt + contact_hour_4_rece_cnt + contact_hour_5_rece_cnt + contact_hour_6_rece_cnt + contact_hour_7_rece_cnt + contact_hour_8_rece_cnt

        contact_hour_9to20_rece_min_tot = contact_hour_9_rece_min_tot + contact_hour_10_rece_min_tot + contact_hour_11_rece_min_tot + contact_hour_12_rece_min_tot + contact_hour_13_rece_min_tot + contact_hour_14_rece_min_tot + contact_hour_15_rece_min_tot + contact_hour_16_rece_min_tot + contact_hour_17_rece_min_tot + contact_hour_18_rece_min_tot + contact_hour_19_rece_min_tot + contact_hour_20_rece_min_tot
        contact_hour_21to8_rece_min_tot = contact_hour_21_rece_min_tot + contact_hour_22_rece_min_tot + contact_hour_23_rece_min_tot + contact_hour_0_rece_min_tot + contact_hour_1_rece_min_tot + contact_hour_2_rece_min_tot + contact_hour_3_rece_min_tot + contact_hour_4_rece_min_tot + contact_hour_5_rece_min_tot + contact_hour_6_rece_min_tot + contact_hour_7_rece_min_tot + contact_hour_8_rece_min_tot

        contact_hour_9to20_rece_cnt_6_mon = contact_hour_9_rece_cnt_6_mon + contact_hour_10_rece_cnt_6_mon + contact_hour_11_rece_cnt_6_mon + contact_hour_12_rece_cnt_6_mon + contact_hour_13_rece_cnt_6_mon + contact_hour_14_rece_cnt_6_mon + contact_hour_15_rece_cnt_6_mon + contact_hour_16_rece_cnt_6_mon + contact_hour_17_rece_cnt_6_mon + contact_hour_18_rece_cnt_6_mon + contact_hour_19_rece_cnt_6_mon + contact_hour_20_rece_cnt_6_mon
        contact_hour_21to8_rece_cnt_6_mon = contact_hour_21_rece_cnt_6_mon + contact_hour_22_rece_cnt_6_mon + contact_hour_23_rece_cnt_6_mon + contact_hour_0_rece_cnt_6_mon + contact_hour_1_rece_cnt_6_mon + contact_hour_2_rece_cnt_6_mon + contact_hour_3_rece_cnt_6_mon + contact_hour_4_rece_cnt_6_mon + contact_hour_5_rece_cnt_6_mon + contact_hour_6_rece_cnt_6_mon + contact_hour_7_rece_cnt_6_mon + contact_hour_8_rece_cnt_6_mon

        contact_hour_9to20_rece_min_tot_6_mon = contact_hour_9_rece_min_tot_6_mon + contact_hour_10_rece_min_tot_6_mon + contact_hour_11_rece_min_tot_6_mon + contact_hour_12_rece_min_tot_6_mon + contact_hour_13_rece_min_tot_6_mon + contact_hour_14_rece_min_tot_6_mon + contact_hour_15_rece_min_tot_6_mon + contact_hour_16_rece_min_tot_6_mon + contact_hour_17_rece_min_tot_6_mon + contact_hour_18_rece_min_tot_6_mon + contact_hour_19_rece_min_tot_6_mon + contact_hour_20_rece_min_tot_6_mon
        contact_hour_21to8_rece_min_tot_6_mon = contact_hour_21_rece_min_tot_6_mon + contact_hour_22_rece_min_tot_6_mon + contact_hour_23_rece_min_tot_6_mon + contact_hour_0_rece_min_tot_6_mon + contact_hour_1_rece_min_tot_6_mon + contact_hour_2_rece_min_tot_6_mon + contact_hour_3_rece_min_tot_6_mon + contact_hour_4_rece_min_tot_6_mon + contact_hour_5_rece_min_tot_6_mon + contact_hour_6_rece_min_tot_6_mon + contact_hour_7_rece_min_tot_6_mon + contact_hour_8_rece_min_tot_6_mon

        contact_hour_9to20_rece_cnt_3_mon = contact_hour_9_rece_cnt_3_mon + contact_hour_10_rece_cnt_3_mon + contact_hour_11_rece_cnt_3_mon + contact_hour_12_rece_cnt_3_mon + contact_hour_13_rece_cnt_3_mon + contact_hour_14_rece_cnt_3_mon + contact_hour_15_rece_cnt_3_mon + contact_hour_16_rece_cnt_3_mon + contact_hour_17_rece_cnt_3_mon + contact_hour_18_rece_cnt_3_mon + contact_hour_19_rece_cnt_3_mon + contact_hour_20_rece_cnt_3_mon
        contact_hour_21to8_rece_cnt_3_mon = contact_hour_21_rece_cnt_3_mon + contact_hour_22_rece_cnt_3_mon + contact_hour_23_rece_cnt_3_mon + contact_hour_0_rece_cnt_3_mon + contact_hour_1_rece_cnt_3_mon + contact_hour_2_rece_cnt_3_mon + contact_hour_3_rece_cnt_3_mon + contact_hour_4_rece_cnt_3_mon + contact_hour_5_rece_cnt_3_mon + contact_hour_6_rece_cnt_3_mon + contact_hour_7_rece_cnt_3_mon + contact_hour_8_rece_cnt_3_mon

        contact_hour_9to20_rece_min_tot_3_mon = contact_hour_9_rece_min_tot_3_mon + contact_hour_10_rece_min_tot_3_mon + contact_hour_11_rece_min_tot_3_mon + contact_hour_12_rece_min_tot_3_mon + contact_hour_13_rece_min_tot_3_mon + contact_hour_14_rece_min_tot_3_mon + contact_hour_15_rece_min_tot_3_mon + contact_hour_16_rece_min_tot_3_mon + contact_hour_17_rece_min_tot_3_mon + contact_hour_18_rece_min_tot_3_mon + contact_hour_19_rece_min_tot_3_mon + contact_hour_20_rece_min_tot_3_mon
        contact_hour_21to8_rece_min_tot_3_mon = contact_hour_21_rece_min_tot_3_mon + contact_hour_22_rece_min_tot_3_mon + contact_hour_23_rece_min_tot_3_mon + contact_hour_0_rece_min_tot_3_mon + contact_hour_1_rece_min_tot_3_mon + contact_hour_2_rece_min_tot_3_mon + contact_hour_3_rece_min_tot_3_mon + contact_hour_4_rece_min_tot_3_mon + contact_hour_5_rece_min_tot_3_mon + contact_hour_6_rece_min_tot_3_mon + contact_hour_7_rece_min_tot_3_mon + contact_hour_8_rece_min_tot_3_mon

        contact_hour_9to20_rece_cnt_2_mon = contact_hour_9_rece_cnt_2_mon + contact_hour_10_rece_cnt_2_mon + contact_hour_11_rece_cnt_2_mon + contact_hour_12_rece_cnt_2_mon + contact_hour_13_rece_cnt_2_mon + contact_hour_14_rece_cnt_2_mon + contact_hour_15_rece_cnt_2_mon + contact_hour_16_rece_cnt_2_mon + contact_hour_17_rece_cnt_2_mon + contact_hour_18_rece_cnt_2_mon + contact_hour_19_rece_cnt_2_mon + contact_hour_20_rece_cnt_2_mon
        contact_hour_21to8_rece_cnt_2_mon = contact_hour_21_rece_cnt_2_mon + contact_hour_22_rece_cnt_2_mon + contact_hour_23_rece_cnt_2_mon + contact_hour_0_rece_cnt_2_mon + contact_hour_1_rece_cnt_2_mon + contact_hour_2_rece_cnt_2_mon + contact_hour_3_rece_cnt_2_mon + contact_hour_4_rece_cnt_2_mon + contact_hour_5_rece_cnt_2_mon + contact_hour_6_rece_cnt_2_mon + contact_hour_7_rece_cnt_2_mon + contact_hour_8_rece_cnt_2_mon

        contact_hour_9to20_rece_min_tot_2_mon = contact_hour_9_rece_min_tot_2_mon + contact_hour_10_rece_min_tot_2_mon + contact_hour_11_rece_min_tot_2_mon + contact_hour_12_rece_min_tot_2_mon + contact_hour_13_rece_min_tot_2_mon + contact_hour_14_rece_min_tot_2_mon + contact_hour_15_rece_min_tot_2_mon + contact_hour_16_rece_min_tot_2_mon + contact_hour_17_rece_min_tot_2_mon + contact_hour_18_rece_min_tot_2_mon + contact_hour_19_rece_min_tot_2_mon + contact_hour_20_rece_min_tot_2_mon
        contact_hour_21to8_rece_min_tot_2_mon = contact_hour_21_rece_min_tot_2_mon + contact_hour_22_rece_min_tot_2_mon + contact_hour_23_rece_min_tot_2_mon + contact_hour_0_rece_min_tot_2_mon + contact_hour_1_rece_min_tot_2_mon + contact_hour_2_rece_min_tot_2_mon + contact_hour_3_rece_min_tot_2_mon + contact_hour_4_rece_min_tot_2_mon + contact_hour_5_rece_min_tot_2_mon + contact_hour_6_rece_min_tot_2_mon + contact_hour_7_rece_min_tot_2_mon + contact_hour_8_rece_min_tot_2_mon

        contact_hour_9to20_rece_cnt_1_mon = contact_hour_9_rece_cnt_1_mon + contact_hour_10_rece_cnt_1_mon + contact_hour_11_rece_cnt_1_mon + contact_hour_12_rece_cnt_1_mon + contact_hour_13_rece_cnt_1_mon + contact_hour_14_rece_cnt_1_mon + contact_hour_15_rece_cnt_1_mon + contact_hour_16_rece_cnt_1_mon + contact_hour_17_rece_cnt_1_mon + contact_hour_18_rece_cnt_1_mon + contact_hour_19_rece_cnt_1_mon + contact_hour_20_rece_cnt_1_mon
        contact_hour_21to8_rece_cnt_1_mon = contact_hour_21_rece_cnt_1_mon + contact_hour_22_rece_cnt_1_mon + contact_hour_23_rece_cnt_1_mon + contact_hour_0_rece_cnt_1_mon + contact_hour_1_rece_cnt_1_mon + contact_hour_2_rece_cnt_1_mon + contact_hour_3_rece_cnt_1_mon + contact_hour_4_rece_cnt_1_mon + contact_hour_5_rece_cnt_1_mon + contact_hour_6_rece_cnt_1_mon + contact_hour_7_rece_cnt_1_mon + contact_hour_8_rece_cnt_1_mon

        contact_hour_9to20_rece_min_tot_1_mon = contact_hour_9_rece_min_tot_1_mon + contact_hour_10_rece_min_tot_1_mon + contact_hour_11_rece_min_tot_1_mon + contact_hour_12_rece_min_tot_1_mon + contact_hour_13_rece_min_tot_1_mon + contact_hour_14_rece_min_tot_1_mon + contact_hour_15_rece_min_tot_1_mon + contact_hour_16_rece_min_tot_1_mon + contact_hour_17_rece_min_tot_1_mon + contact_hour_18_rece_min_tot_1_mon + contact_hour_19_rece_min_tot_1_mon + contact_hour_20_rece_min_tot_1_mon
        contact_hour_21to8_rece_min_tot_1_mon = contact_hour_21_rece_min_tot_1_mon + contact_hour_22_rece_min_tot_1_mon + contact_hour_23_rece_min_tot_1_mon + contact_hour_0_rece_min_tot_1_mon + contact_hour_1_rece_min_tot_1_mon + contact_hour_2_rece_min_tot_1_mon + contact_hour_3_rece_min_tot_1_mon + contact_hour_4_rece_min_tot_1_mon + contact_hour_5_rece_min_tot_1_mon + contact_hour_6_rece_min_tot_1_mon + contact_hour_7_rece_min_tot_1_mon + contact_hour_8_rece_min_tot_1_mon

        contact_hour_9to20_rece_cnt_2_wk = contact_hour_9_rece_cnt_2_wk + contact_hour_10_rece_cnt_2_wk + contact_hour_11_rece_cnt_2_wk + contact_hour_12_rece_cnt_2_wk + contact_hour_13_rece_cnt_2_wk + contact_hour_14_rece_cnt_2_wk + contact_hour_15_rece_cnt_2_wk + contact_hour_16_rece_cnt_2_wk + contact_hour_17_rece_cnt_2_wk + contact_hour_18_rece_cnt_2_wk + contact_hour_19_rece_cnt_2_wk + contact_hour_20_rece_cnt_2_wk
        contact_hour_21to8_rece_cnt_2_wk = contact_hour_21_rece_cnt_2_wk + contact_hour_22_rece_cnt_2_wk + contact_hour_23_rece_cnt_2_wk + contact_hour_0_rece_cnt_2_wk + contact_hour_1_rece_cnt_2_wk + contact_hour_2_rece_cnt_2_wk + contact_hour_3_rece_cnt_2_wk + contact_hour_4_rece_cnt_2_wk + contact_hour_5_rece_cnt_2_wk + contact_hour_6_rece_cnt_2_wk + contact_hour_7_rece_cnt_2_wk + contact_hour_8_rece_cnt_2_wk

        contact_hour_9to20_rece_min_tot_2_wk = contact_hour_9_rece_min_tot_2_wk + contact_hour_10_rece_min_tot_2_wk + contact_hour_11_rece_min_tot_2_wk + contact_hour_12_rece_min_tot_2_wk + contact_hour_13_rece_min_tot_2_wk + contact_hour_14_rece_min_tot_2_wk + contact_hour_15_rece_min_tot_2_wk + contact_hour_16_rece_min_tot_2_wk + contact_hour_17_rece_min_tot_2_wk + contact_hour_18_rece_min_tot_2_wk + contact_hour_19_rece_min_tot_2_wk + contact_hour_20_rece_min_tot_2_wk
        contact_hour_21to8_rece_min_tot_2_wk = contact_hour_21_rece_min_tot_2_wk + contact_hour_22_rece_min_tot_2_wk + contact_hour_23_rece_min_tot_2_wk + contact_hour_0_rece_min_tot_2_wk + contact_hour_1_rece_min_tot_2_wk + contact_hour_2_rece_min_tot_2_wk + contact_hour_3_rece_min_tot_2_wk + contact_hour_4_rece_min_tot_2_wk + contact_hour_5_rece_min_tot_2_wk + contact_hour_6_rece_min_tot_2_wk + contact_hour_7_rece_min_tot_2_wk + contact_hour_8_rece_min_tot_2_wk

        # 24 hours 通话
        contact_hour_0to23_cnt = contact_hour_9to20_cnt + contact_hour_21to8_cnt
        contact_hour_0to23_min_tot = contact_hour_9to20_min_tot + contact_hour_21to8_min_tot

        contact_hour_0to23_cnt_6_mon = contact_hour_9to20_cnt_6_mon + contact_hour_21to8_cnt_6_mon
        contact_hour_0to23_min_tot_6_mon = contact_hour_9to20_min_tot_6_mon + contact_hour_21to8_min_tot_6_mon

        contact_hour_0to23_cnt_3_mon = contact_hour_9to20_cnt_3_mon + contact_hour_21to8_cnt_3_mon
        contact_hour_0to23_min_tot_3_mon = contact_hour_9to20_min_tot_3_mon + contact_hour_21to8_min_tot_3_mon

        contact_hour_0to23_cnt_2_mon = contact_hour_9to20_cnt_2_mon + contact_hour_21to8_cnt_2_mon
        contact_hour_0to23_min_tot_2_mon = contact_hour_9to20_min_tot_2_mon + contact_hour_21to8_min_tot_2_mon

        contact_hour_0to23_cnt_1_mon = contact_hour_9to20_cnt_1_mon + contact_hour_21to8_cnt_1_mon
        contact_hour_0to23_min_tot_1_mon = contact_hour_9to20_min_tot_1_mon + contact_hour_21to8_min_tot_1_mon

        contact_hour_0to23_cnt_2_wk = contact_hour_9to20_cnt_2_wk + contact_hour_21to8_cnt_2_wk
        contact_hour_0to23_min_tot_2_wk = contact_hour_9to20_min_tot_2_wk + contact_hour_21to8_min_tot_2_wk

        contact_hour_0to23_call_cnt = contact_hour_9to20_cnt + contact_hour_21to8_cnt
        contact_hour_0to23_call_min_tot = contact_hour_9to20_call_min_tot + contact_hour_21to8_call_min_tot

        contact_hour_0to23_call_cnt_6_mon = contact_hour_9to20_call_cnt_6_mon + contact_hour_21to8_call_cnt_6_mon
        contact_hour_0to23_call_min_tot_6_mon = contact_hour_9to20_call_min_tot_6_mon + contact_hour_21to8_call_min_tot_6_mon

        contact_hour_0to23_call_cnt_3_mon = contact_hour_9to20_call_cnt_3_mon + contact_hour_21to8_call_cnt_3_mon
        contact_hour_0to23_call_min_tot_3_mon = contact_hour_9to20_call_min_tot_3_mon + contact_hour_21to8_call_min_tot_3_mon

        contact_hour_0to23_call_cnt_2_mon = contact_hour_9to20_call_cnt_2_mon + contact_hour_21to8_call_cnt_2_mon
        contact_hour_0to23_call_min_tot_2_mon = contact_hour_9to20_call_min_tot_2_mon + contact_hour_21to8_call_min_tot_2_mon

        contact_hour_0to23_call_cnt_1_mon = contact_hour_9to20_call_cnt_1_mon + contact_hour_21to8_call_cnt_1_mon
        contact_hour_0to23_call_min_tot_1_mon = contact_hour_9to20_call_min_tot_1_mon + contact_hour_21to8_call_min_tot_1_mon

        contact_hour_0to23_call_cnt_2_wk = contact_hour_9to20_call_cnt_2_wk + contact_hour_21to8_call_cnt_2_wk
        contact_hour_0to23_call_min_tot_2_wk = contact_hour_9to20_call_min_tot_2_wk + contact_hour_21to8_call_min_tot_2_wk

        contact_hour_0to23_rece_cnt = contact_hour_9to20_cnt + contact_hour_21to8_cnt
        contact_hour_0to23_rece_min_tot = contact_hour_9to20_rece_min_tot + contact_hour_21to8_rece_min_tot

        contact_hour_0to23_rece_cnt_6_mon = contact_hour_9to20_rece_cnt_6_mon + contact_hour_21to8_rece_cnt_6_mon
        contact_hour_0to23_rece_min_tot_6_mon = contact_hour_9to20_rece_min_tot_6_mon + contact_hour_21to8_rece_min_tot_6_mon

        contact_hour_0to23_rece_cnt_3_mon = contact_hour_9to20_rece_cnt_3_mon + contact_hour_21to8_rece_cnt_3_mon
        contact_hour_0to23_rece_min_tot_3_mon = contact_hour_9to20_rece_min_tot_3_mon + contact_hour_21to8_rece_min_tot_3_mon

        contact_hour_0to23_rece_cnt_2_mon = contact_hour_9to20_rece_cnt_2_mon + contact_hour_21to8_rece_cnt_2_mon
        contact_hour_0to23_rece_min_tot_2_mon = contact_hour_9to20_rece_min_tot_2_mon + contact_hour_21to8_rece_min_tot_2_mon

        contact_hour_0to23_rece_cnt_1_mon = contact_hour_9to20_rece_cnt_1_mon + contact_hour_21to8_rece_cnt_1_mon
        contact_hour_0to23_rece_min_tot_1_mon = contact_hour_9to20_rece_min_tot_1_mon + contact_hour_21to8_rece_min_tot_1_mon

        contact_hour_0to23_rece_cnt_2_wk = contact_hour_9to20_rece_cnt_2_wk + contact_hour_21to8_rece_cnt_2_wk
        contact_hour_0to23_rece_min_tot_2_wk = contact_hour_9to20_rece_min_tot_2_wk + contact_hour_21to8_rece_min_tot_2_wk

        # avg
        contact_hour_0_min_avg = perc(contact_hour_0_min_tot, contact_hour_0_cnt)
        contact_hour_1_min_avg = perc(contact_hour_1_min_tot, contact_hour_1_cnt)
        contact_hour_2_min_avg = perc(contact_hour_2_min_tot, contact_hour_2_cnt)
        contact_hour_3_min_avg = perc(contact_hour_3_min_tot, contact_hour_3_cnt)
        contact_hour_4_min_avg = perc(contact_hour_4_min_tot, contact_hour_4_cnt)
        contact_hour_5_min_avg = perc(contact_hour_5_min_tot, contact_hour_5_cnt)
        contact_hour_6_min_avg = perc(contact_hour_6_min_tot, contact_hour_6_cnt)
        contact_hour_7_min_avg = perc(contact_hour_7_min_tot, contact_hour_7_cnt)
        contact_hour_8_min_avg = perc(contact_hour_8_min_tot, contact_hour_8_cnt)
        contact_hour_9_min_avg = perc(contact_hour_9_min_tot, contact_hour_9_cnt)
        contact_hour_10_min_avg = perc(contact_hour_10_min_tot, contact_hour_10_cnt)
        contact_hour_11_min_avg = perc(contact_hour_11_min_tot, contact_hour_11_cnt)
        contact_hour_12_min_avg = perc(contact_hour_12_min_tot, contact_hour_12_cnt)
        contact_hour_13_min_avg = perc(contact_hour_13_min_tot, contact_hour_13_cnt)
        contact_hour_14_min_avg = perc(contact_hour_14_min_tot, contact_hour_14_cnt)
        contact_hour_15_min_avg = perc(contact_hour_15_min_tot, contact_hour_15_cnt)
        contact_hour_16_min_avg = perc(contact_hour_16_min_tot, contact_hour_16_cnt)
        contact_hour_17_min_avg = perc(contact_hour_17_min_tot, contact_hour_17_cnt)
        contact_hour_18_min_avg = perc(contact_hour_18_min_tot, contact_hour_18_cnt)
        contact_hour_19_min_avg = perc(contact_hour_19_min_tot, contact_hour_19_cnt)
        contact_hour_20_min_avg = perc(contact_hour_20_min_tot, contact_hour_20_cnt)
        contact_hour_21_min_avg = perc(contact_hour_21_min_tot, contact_hour_21_cnt)
        contact_hour_22_min_avg = perc(contact_hour_22_min_tot, contact_hour_22_cnt)
        contact_hour_23_min_avg = perc(contact_hour_23_min_tot, contact_hour_23_cnt)

        contact_hour_0_min_avg_6_mon = perc(contact_hour_0_min_tot_6_mon, contact_hour_0_cnt_6_mon)
        contact_hour_1_min_avg_6_mon = perc(contact_hour_1_min_tot_6_mon, contact_hour_1_cnt_6_mon)
        contact_hour_2_min_avg_6_mon = perc(contact_hour_2_min_tot_6_mon, contact_hour_2_cnt_6_mon)
        contact_hour_3_min_avg_6_mon = perc(contact_hour_3_min_tot_6_mon, contact_hour_3_cnt_6_mon)
        contact_hour_4_min_avg_6_mon = perc(contact_hour_4_min_tot_6_mon, contact_hour_4_cnt_6_mon)
        contact_hour_5_min_avg_6_mon = perc(contact_hour_5_min_tot_6_mon, contact_hour_5_cnt_6_mon)
        contact_hour_6_min_avg_6_mon = perc(contact_hour_6_min_tot_6_mon, contact_hour_6_cnt_6_mon)
        contact_hour_7_min_avg_6_mon = perc(contact_hour_7_min_tot_6_mon, contact_hour_7_cnt_6_mon)
        contact_hour_8_min_avg_6_mon = perc(contact_hour_8_min_tot_6_mon, contact_hour_8_cnt_6_mon)
        contact_hour_9_min_avg_6_mon = perc(contact_hour_9_min_tot_6_mon, contact_hour_9_cnt_6_mon)
        contact_hour_10_min_avg_6_mon = perc(contact_hour_10_min_tot_6_mon, contact_hour_10_cnt_6_mon)
        contact_hour_11_min_avg_6_mon = perc(contact_hour_11_min_tot_6_mon, contact_hour_11_cnt_6_mon)
        contact_hour_12_min_avg_6_mon = perc(contact_hour_12_min_tot_6_mon, contact_hour_12_cnt_6_mon)
        contact_hour_13_min_avg_6_mon = perc(contact_hour_13_min_tot_6_mon, contact_hour_13_cnt_6_mon)
        contact_hour_14_min_avg_6_mon = perc(contact_hour_14_min_tot_6_mon, contact_hour_14_cnt_6_mon)
        contact_hour_15_min_avg_6_mon = perc(contact_hour_15_min_tot_6_mon, contact_hour_15_cnt_6_mon)
        contact_hour_16_min_avg_6_mon = perc(contact_hour_16_min_tot_6_mon, contact_hour_16_cnt_6_mon)
        contact_hour_17_min_avg_6_mon = perc(contact_hour_17_min_tot_6_mon, contact_hour_17_cnt_6_mon)
        contact_hour_18_min_avg_6_mon = perc(contact_hour_18_min_tot_6_mon, contact_hour_18_cnt_6_mon)
        contact_hour_19_min_avg_6_mon = perc(contact_hour_19_min_tot_6_mon, contact_hour_19_cnt_6_mon)
        contact_hour_20_min_avg_6_mon = perc(contact_hour_20_min_tot_6_mon, contact_hour_20_cnt_6_mon)
        contact_hour_21_min_avg_6_mon = perc(contact_hour_21_min_tot_6_mon, contact_hour_21_cnt_6_mon)
        contact_hour_22_min_avg_6_mon = perc(contact_hour_22_min_tot_6_mon, contact_hour_22_cnt_6_mon)
        contact_hour_23_min_avg_6_mon = perc(contact_hour_23_min_tot_6_mon, contact_hour_23_cnt_6_mon)

        contact_hour_0_min_avg_3_mon = perc(contact_hour_0_min_tot_3_mon, contact_hour_0_cnt_3_mon)
        contact_hour_1_min_avg_3_mon = perc(contact_hour_1_min_tot_3_mon, contact_hour_1_cnt_3_mon)
        contact_hour_2_min_avg_3_mon = perc(contact_hour_2_min_tot_3_mon, contact_hour_2_cnt_3_mon)
        contact_hour_3_min_avg_3_mon = perc(contact_hour_3_min_tot_3_mon, contact_hour_3_cnt_3_mon)
        contact_hour_4_min_avg_3_mon = perc(contact_hour_4_min_tot_3_mon, contact_hour_4_cnt_3_mon)
        contact_hour_5_min_avg_3_mon = perc(contact_hour_5_min_tot_3_mon, contact_hour_5_cnt_3_mon)
        contact_hour_6_min_avg_3_mon = perc(contact_hour_6_min_tot_3_mon, contact_hour_6_cnt_3_mon)
        contact_hour_7_min_avg_3_mon = perc(contact_hour_7_min_tot_3_mon, contact_hour_7_cnt_3_mon)
        contact_hour_8_min_avg_3_mon = perc(contact_hour_8_min_tot_3_mon, contact_hour_8_cnt_3_mon)
        contact_hour_9_min_avg_3_mon = perc(contact_hour_9_min_tot_3_mon, contact_hour_9_cnt_3_mon)
        contact_hour_10_min_avg_3_mon = perc(contact_hour_10_min_tot_3_mon, contact_hour_10_cnt_3_mon)
        contact_hour_11_min_avg_3_mon = perc(contact_hour_11_min_tot_3_mon, contact_hour_11_cnt_3_mon)
        contact_hour_12_min_avg_3_mon = perc(contact_hour_12_min_tot_3_mon, contact_hour_12_cnt_3_mon)
        contact_hour_13_min_avg_3_mon = perc(contact_hour_13_min_tot_3_mon, contact_hour_13_cnt_3_mon)
        contact_hour_14_min_avg_3_mon = perc(contact_hour_14_min_tot_3_mon, contact_hour_14_cnt_3_mon)
        contact_hour_15_min_avg_3_mon = perc(contact_hour_15_min_tot_3_mon, contact_hour_15_cnt_3_mon)
        contact_hour_16_min_avg_3_mon = perc(contact_hour_16_min_tot_3_mon, contact_hour_16_cnt_3_mon)
        contact_hour_17_min_avg_3_mon = perc(contact_hour_17_min_tot_3_mon, contact_hour_17_cnt_3_mon)
        contact_hour_18_min_avg_3_mon = perc(contact_hour_18_min_tot_3_mon, contact_hour_18_cnt_3_mon)
        contact_hour_19_min_avg_3_mon = perc(contact_hour_19_min_tot_3_mon, contact_hour_19_cnt_3_mon)
        contact_hour_20_min_avg_3_mon = perc(contact_hour_20_min_tot_3_mon, contact_hour_20_cnt_3_mon)
        contact_hour_21_min_avg_3_mon = perc(contact_hour_21_min_tot_3_mon, contact_hour_21_cnt_3_mon)
        contact_hour_22_min_avg_3_mon = perc(contact_hour_22_min_tot_3_mon, contact_hour_22_cnt_3_mon)
        contact_hour_23_min_avg_3_mon = perc(contact_hour_23_min_tot_3_mon, contact_hour_23_cnt_3_mon)

        contact_hour_0_min_avg_2_mon = perc(contact_hour_0_min_tot_2_mon, contact_hour_0_cnt_2_mon)
        contact_hour_1_min_avg_2_mon = perc(contact_hour_1_min_tot_2_mon, contact_hour_1_cnt_2_mon)
        contact_hour_2_min_avg_2_mon = perc(contact_hour_2_min_tot_2_mon, contact_hour_2_cnt_2_mon)
        contact_hour_3_min_avg_2_mon = perc(contact_hour_3_min_tot_2_mon, contact_hour_3_cnt_2_mon)
        contact_hour_4_min_avg_2_mon = perc(contact_hour_4_min_tot_2_mon, contact_hour_4_cnt_2_mon)
        contact_hour_5_min_avg_2_mon = perc(contact_hour_5_min_tot_2_mon, contact_hour_5_cnt_2_mon)
        contact_hour_6_min_avg_2_mon = perc(contact_hour_6_min_tot_2_mon, contact_hour_6_cnt_2_mon)
        contact_hour_7_min_avg_2_mon = perc(contact_hour_7_min_tot_2_mon, contact_hour_7_cnt_2_mon)
        contact_hour_8_min_avg_2_mon = perc(contact_hour_8_min_tot_2_mon, contact_hour_8_cnt_2_mon)
        contact_hour_9_min_avg_2_mon = perc(contact_hour_9_min_tot_2_mon, contact_hour_9_cnt_2_mon)
        contact_hour_10_min_avg_2_mon = perc(contact_hour_10_min_tot_2_mon, contact_hour_10_cnt_2_mon)
        contact_hour_11_min_avg_2_mon = perc(contact_hour_11_min_tot_2_mon, contact_hour_11_cnt_2_mon)
        contact_hour_12_min_avg_2_mon = perc(contact_hour_12_min_tot_2_mon, contact_hour_12_cnt_2_mon)
        contact_hour_13_min_avg_2_mon = perc(contact_hour_13_min_tot_2_mon, contact_hour_13_cnt_2_mon)
        contact_hour_14_min_avg_2_mon = perc(contact_hour_14_min_tot_2_mon, contact_hour_14_cnt_2_mon)
        contact_hour_15_min_avg_2_mon = perc(contact_hour_15_min_tot_2_mon, contact_hour_15_cnt_2_mon)
        contact_hour_16_min_avg_2_mon = perc(contact_hour_16_min_tot_2_mon, contact_hour_16_cnt_2_mon)
        contact_hour_17_min_avg_2_mon = perc(contact_hour_17_min_tot_2_mon, contact_hour_17_cnt_2_mon)
        contact_hour_18_min_avg_2_mon = perc(contact_hour_18_min_tot_2_mon, contact_hour_18_cnt_2_mon)
        contact_hour_19_min_avg_2_mon = perc(contact_hour_19_min_tot_2_mon, contact_hour_19_cnt_2_mon)
        contact_hour_20_min_avg_2_mon = perc(contact_hour_20_min_tot_2_mon, contact_hour_20_cnt_2_mon)
        contact_hour_21_min_avg_2_mon = perc(contact_hour_21_min_tot_2_mon, contact_hour_21_cnt_2_mon)
        contact_hour_22_min_avg_2_mon = perc(contact_hour_22_min_tot_2_mon, contact_hour_22_cnt_2_mon)
        contact_hour_23_min_avg_2_mon = perc(contact_hour_23_min_tot_2_mon, contact_hour_23_cnt_2_mon)

        contact_hour_0_min_avg_1_mon = perc(contact_hour_0_min_tot_1_mon, contact_hour_0_cnt_1_mon)
        contact_hour_1_min_avg_1_mon = perc(contact_hour_1_min_tot_1_mon, contact_hour_1_cnt_1_mon)
        contact_hour_2_min_avg_1_mon = perc(contact_hour_2_min_tot_1_mon, contact_hour_2_cnt_1_mon)
        contact_hour_3_min_avg_1_mon = perc(contact_hour_3_min_tot_1_mon, contact_hour_3_cnt_1_mon)
        contact_hour_4_min_avg_1_mon = perc(contact_hour_4_min_tot_1_mon, contact_hour_4_cnt_1_mon)
        contact_hour_5_min_avg_1_mon = perc(contact_hour_5_min_tot_1_mon, contact_hour_5_cnt_1_mon)
        contact_hour_6_min_avg_1_mon = perc(contact_hour_6_min_tot_1_mon, contact_hour_6_cnt_1_mon)
        contact_hour_7_min_avg_1_mon = perc(contact_hour_7_min_tot_1_mon, contact_hour_7_cnt_1_mon)
        contact_hour_8_min_avg_1_mon = perc(contact_hour_8_min_tot_1_mon, contact_hour_8_cnt_1_mon)
        contact_hour_9_min_avg_1_mon = perc(contact_hour_9_min_tot_1_mon, contact_hour_9_cnt_1_mon)
        contact_hour_10_min_avg_1_mon = perc(contact_hour_10_min_tot_1_mon, contact_hour_10_cnt_1_mon)
        contact_hour_11_min_avg_1_mon = perc(contact_hour_11_min_tot_1_mon, contact_hour_11_cnt_1_mon)
        contact_hour_12_min_avg_1_mon = perc(contact_hour_12_min_tot_1_mon, contact_hour_12_cnt_1_mon)
        contact_hour_13_min_avg_1_mon = perc(contact_hour_13_min_tot_1_mon, contact_hour_13_cnt_1_mon)
        contact_hour_14_min_avg_1_mon = perc(contact_hour_14_min_tot_1_mon, contact_hour_14_cnt_1_mon)
        contact_hour_15_min_avg_1_mon = perc(contact_hour_15_min_tot_1_mon, contact_hour_15_cnt_1_mon)
        contact_hour_16_min_avg_1_mon = perc(contact_hour_16_min_tot_1_mon, contact_hour_16_cnt_1_mon)
        contact_hour_17_min_avg_1_mon = perc(contact_hour_17_min_tot_1_mon, contact_hour_17_cnt_1_mon)
        contact_hour_18_min_avg_1_mon = perc(contact_hour_18_min_tot_1_mon, contact_hour_18_cnt_1_mon)
        contact_hour_19_min_avg_1_mon = perc(contact_hour_19_min_tot_1_mon, contact_hour_19_cnt_1_mon)
        contact_hour_20_min_avg_1_mon = perc(contact_hour_20_min_tot_1_mon, contact_hour_20_cnt_1_mon)
        contact_hour_21_min_avg_1_mon = perc(contact_hour_21_min_tot_1_mon, contact_hour_21_cnt_1_mon)
        contact_hour_22_min_avg_1_mon = perc(contact_hour_22_min_tot_1_mon, contact_hour_22_cnt_1_mon)
        contact_hour_23_min_avg_1_mon = perc(contact_hour_23_min_tot_1_mon, contact_hour_23_cnt_1_mon)

        contact_hour_0_min_avg_2_wk = perc(contact_hour_0_min_tot_2_wk, contact_hour_0_cnt_2_wk)
        contact_hour_1_min_avg_2_wk = perc(contact_hour_1_min_tot_2_wk, contact_hour_1_cnt_2_wk)
        contact_hour_2_min_avg_2_wk = perc(contact_hour_2_min_tot_2_wk, contact_hour_2_cnt_2_wk)
        contact_hour_3_min_avg_2_wk = perc(contact_hour_3_min_tot_2_wk, contact_hour_3_cnt_2_wk)
        contact_hour_4_min_avg_2_wk = perc(contact_hour_4_min_tot_2_wk, contact_hour_4_cnt_2_wk)
        contact_hour_5_min_avg_2_wk = perc(contact_hour_5_min_tot_2_wk, contact_hour_5_cnt_2_wk)
        contact_hour_6_min_avg_2_wk = perc(contact_hour_6_min_tot_2_wk, contact_hour_6_cnt_2_wk)
        contact_hour_7_min_avg_2_wk = perc(contact_hour_7_min_tot_2_wk, contact_hour_7_cnt_2_wk)
        contact_hour_8_min_avg_2_wk = perc(contact_hour_8_min_tot_2_wk, contact_hour_8_cnt_2_wk)
        contact_hour_9_min_avg_2_wk = perc(contact_hour_9_min_tot_2_wk, contact_hour_9_cnt_2_wk)
        contact_hour_10_min_avg_2_wk = perc(contact_hour_10_min_tot_2_wk, contact_hour_10_cnt_2_wk)
        contact_hour_11_min_avg_2_wk = perc(contact_hour_11_min_tot_2_wk, contact_hour_11_cnt_2_wk)
        contact_hour_12_min_avg_2_wk = perc(contact_hour_12_min_tot_2_wk, contact_hour_12_cnt_2_wk)
        contact_hour_13_min_avg_2_wk = perc(contact_hour_13_min_tot_2_wk, contact_hour_13_cnt_2_wk)
        contact_hour_14_min_avg_2_wk = perc(contact_hour_14_min_tot_2_wk, contact_hour_14_cnt_2_wk)
        contact_hour_15_min_avg_2_wk = perc(contact_hour_15_min_tot_2_wk, contact_hour_15_cnt_2_wk)
        contact_hour_16_min_avg_2_wk = perc(contact_hour_16_min_tot_2_wk, contact_hour_16_cnt_2_wk)
        contact_hour_17_min_avg_2_wk = perc(contact_hour_17_min_tot_2_wk, contact_hour_17_cnt_2_wk)
        contact_hour_18_min_avg_2_wk = perc(contact_hour_18_min_tot_2_wk, contact_hour_18_cnt_2_wk)
        contact_hour_19_min_avg_2_wk = perc(contact_hour_19_min_tot_2_wk, contact_hour_19_cnt_2_wk)
        contact_hour_20_min_avg_2_wk = perc(contact_hour_20_min_tot_2_wk, contact_hour_20_cnt_2_wk)
        contact_hour_21_min_avg_2_wk = perc(contact_hour_21_min_tot_2_wk, contact_hour_21_cnt_2_wk)
        contact_hour_22_min_avg_2_wk = perc(contact_hour_22_min_tot_2_wk, contact_hour_22_cnt_2_wk)
        contact_hour_23_min_avg_2_wk = perc(contact_hour_23_min_tot_2_wk, contact_hour_23_cnt_2_wk)

        contact_hour_0to1_min_avg = perc(contact_hour_0to1_min_tot, contact_hour_0to1_cnt)
        contact_hour_2to3_min_avg = perc(contact_hour_2to3_min_tot, contact_hour_2to3_cnt)
        contact_hour_4to5_min_avg = perc(contact_hour_4to5_min_tot, contact_hour_4to5_cnt)
        contact_hour_6to7_min_avg = perc(contact_hour_6to7_min_tot, contact_hour_6to7_cnt)
        contact_hour_8to9_min_avg = perc(contact_hour_8to9_min_tot, contact_hour_8to9_cnt)
        contact_hour_10to11_min_avg = perc(contact_hour_10to11_min_tot, contact_hour_10to11_cnt)
        contact_hour_12to13_min_avg = perc(contact_hour_12to13_min_tot, contact_hour_12to13_cnt)
        contact_hour_14to15_min_avg = perc(contact_hour_14to15_min_tot, contact_hour_14to15_cnt)
        contact_hour_16to17_min_avg = perc(contact_hour_16to17_min_tot, contact_hour_16to17_cnt)
        contact_hour_18to19_min_avg = perc(contact_hour_18to19_min_tot, contact_hour_18to19_cnt)
        contact_hour_20to21_min_avg = perc(contact_hour_20to21_min_tot, contact_hour_20to21_cnt)
        contact_hour_22to23_min_avg = perc(contact_hour_22to23_min_tot, contact_hour_22to23_cnt)

        contact_hour_0to1_min_avg_6_mon = perc(contact_hour_0to1_min_tot_6_mon, contact_hour_0to1_cnt_6_mon)
        contact_hour_2to3_min_avg_6_mon = perc(contact_hour_2to3_min_tot_6_mon, contact_hour_2to3_cnt_6_mon)
        contact_hour_4to5_min_avg_6_mon = perc(contact_hour_4to5_min_tot_6_mon, contact_hour_4to5_cnt_6_mon)
        contact_hour_6to7_min_avg_6_mon = perc(contact_hour_6to7_min_tot_6_mon, contact_hour_6to7_cnt_6_mon)
        contact_hour_8to9_min_avg_6_mon = perc(contact_hour_8to9_min_tot_6_mon, contact_hour_8to9_cnt_6_mon)
        contact_hour_10to11_min_avg_6_mon = perc(contact_hour_10to11_min_tot_6_mon, contact_hour_10to11_cnt_6_mon)
        contact_hour_12to13_min_avg_6_mon = perc(contact_hour_12to13_min_tot_6_mon, contact_hour_12to13_cnt_6_mon)
        contact_hour_14to15_min_avg_6_mon = perc(contact_hour_14to15_min_tot_6_mon, contact_hour_14to15_cnt_6_mon)
        contact_hour_16to17_min_avg_6_mon = perc(contact_hour_16to17_min_tot_6_mon, contact_hour_16to17_cnt_6_mon)
        contact_hour_18to19_min_avg_6_mon = perc(contact_hour_18to19_min_tot_6_mon, contact_hour_18to19_cnt_6_mon)
        contact_hour_20to21_min_avg_6_mon = perc(contact_hour_20to21_min_tot_6_mon, contact_hour_20to21_cnt_6_mon)
        contact_hour_22to23_min_avg_6_mon = perc(contact_hour_22to23_min_tot_6_mon, contact_hour_22to23_cnt_6_mon)

        contact_hour_0to1_min_avg_3_mon = perc(contact_hour_0to1_min_tot_3_mon, contact_hour_0to1_cnt_3_mon)
        contact_hour_2to3_min_avg_3_mon = perc(contact_hour_2to3_min_tot_3_mon, contact_hour_2to3_cnt_3_mon)
        contact_hour_4to5_min_avg_3_mon = perc(contact_hour_4to5_min_tot_3_mon, contact_hour_4to5_cnt_3_mon)
        contact_hour_6to7_min_avg_3_mon = perc(contact_hour_6to7_min_tot_3_mon, contact_hour_6to7_cnt_3_mon)
        contact_hour_8to9_min_avg_3_mon = perc(contact_hour_8to9_min_tot_3_mon, contact_hour_8to9_cnt_3_mon)
        contact_hour_10to11_min_avg_3_mon = perc(contact_hour_10to11_min_tot_3_mon, contact_hour_10to11_cnt_3_mon)
        contact_hour_12to13_min_avg_3_mon = perc(contact_hour_12to13_min_tot_3_mon, contact_hour_12to13_cnt_3_mon)
        contact_hour_14to15_min_avg_3_mon = perc(contact_hour_14to15_min_tot_3_mon, contact_hour_14to15_cnt_3_mon)
        contact_hour_16to17_min_avg_3_mon = perc(contact_hour_16to17_min_tot_3_mon, contact_hour_16to17_cnt_3_mon)
        contact_hour_18to19_min_avg_3_mon = perc(contact_hour_18to19_min_tot_3_mon, contact_hour_18to19_cnt_3_mon)
        contact_hour_20to21_min_avg_3_mon = perc(contact_hour_20to21_min_tot_3_mon, contact_hour_20to21_cnt_3_mon)
        contact_hour_22to23_min_avg_3_mon = perc(contact_hour_22to23_min_tot_3_mon, contact_hour_22to23_cnt_3_mon)

        contact_hour_0to1_min_avg_2_mon = perc(contact_hour_0to1_min_tot_2_mon, contact_hour_0to1_cnt_2_mon)
        contact_hour_2to3_min_avg_2_mon = perc(contact_hour_2to3_min_tot_2_mon, contact_hour_2to3_cnt_2_mon)
        contact_hour_4to5_min_avg_2_mon = perc(contact_hour_4to5_min_tot_2_mon, contact_hour_4to5_cnt_2_mon)
        contact_hour_6to7_min_avg_2_mon = perc(contact_hour_6to7_min_tot_2_mon, contact_hour_6to7_cnt_2_mon)
        contact_hour_8to9_min_avg_2_mon = perc(contact_hour_8to9_min_tot_2_mon, contact_hour_8to9_cnt_2_mon)
        contact_hour_10to11_min_avg_2_mon = perc(contact_hour_10to11_min_tot_2_mon, contact_hour_10to11_cnt_2_mon)
        contact_hour_12to13_min_avg_2_mon = perc(contact_hour_12to13_min_tot_2_mon, contact_hour_12to13_cnt_2_mon)
        contact_hour_14to15_min_avg_2_mon = perc(contact_hour_14to15_min_tot_2_mon, contact_hour_14to15_cnt_2_mon)
        contact_hour_16to17_min_avg_2_mon = perc(contact_hour_16to17_min_tot_2_mon, contact_hour_16to17_cnt_2_mon)
        contact_hour_18to19_min_avg_2_mon = perc(contact_hour_18to19_min_tot_2_mon, contact_hour_18to19_cnt_2_mon)
        contact_hour_20to21_min_avg_2_mon = perc(contact_hour_20to21_min_tot_2_mon, contact_hour_20to21_cnt_2_mon)
        contact_hour_22to23_min_avg_2_mon = perc(contact_hour_22to23_min_tot_2_mon, contact_hour_22to23_cnt_2_mon)

        contact_hour_0to1_min_avg_1_mon = perc(contact_hour_0to1_min_tot_1_mon, contact_hour_0to1_cnt_1_mon)
        contact_hour_2to3_min_avg_1_mon = perc(contact_hour_2to3_min_tot_1_mon, contact_hour_2to3_cnt_1_mon)
        contact_hour_4to5_min_avg_1_mon = perc(contact_hour_4to5_min_tot_1_mon, contact_hour_4to5_cnt_1_mon)
        contact_hour_6to7_min_avg_1_mon = perc(contact_hour_6to7_min_tot_1_mon, contact_hour_6to7_cnt_1_mon)
        contact_hour_8to9_min_avg_1_mon = perc(contact_hour_8to9_min_tot_1_mon, contact_hour_8to9_cnt_1_mon)
        contact_hour_10to11_min_avg_1_mon = perc(contact_hour_10to11_min_tot_1_mon, contact_hour_10to11_cnt_1_mon)
        contact_hour_12to13_min_avg_1_mon = perc(contact_hour_12to13_min_tot_1_mon, contact_hour_12to13_cnt_1_mon)
        contact_hour_14to15_min_avg_1_mon = perc(contact_hour_14to15_min_tot_1_mon, contact_hour_14to15_cnt_1_mon)
        contact_hour_16to17_min_avg_1_mon = perc(contact_hour_16to17_min_tot_1_mon, contact_hour_16to17_cnt_1_mon)
        contact_hour_18to19_min_avg_1_mon = perc(contact_hour_18to19_min_tot_1_mon, contact_hour_18to19_cnt_1_mon)
        contact_hour_20to21_min_avg_1_mon = perc(contact_hour_20to21_min_tot_1_mon, contact_hour_20to21_cnt_1_mon)
        contact_hour_22to23_min_avg_1_mon = perc(contact_hour_22to23_min_tot_1_mon, contact_hour_22to23_cnt_1_mon)

        contact_hour_0to1_min_avg_2_wk = perc(contact_hour_0to1_min_tot_2_wk, contact_hour_0to1_cnt_2_wk)
        contact_hour_2to3_min_avg_2_wk = perc(contact_hour_2to3_min_tot_2_wk, contact_hour_2to3_cnt_2_wk)
        contact_hour_4to5_min_avg_2_wk = perc(contact_hour_4to5_min_tot_2_wk, contact_hour_4to5_cnt_2_wk)
        contact_hour_6to7_min_avg_2_wk = perc(contact_hour_6to7_min_tot_2_wk, contact_hour_6to7_cnt_2_wk)
        contact_hour_8to9_min_avg_2_wk = perc(contact_hour_8to9_min_tot_2_wk, contact_hour_8to9_cnt_2_wk)
        contact_hour_10to11_min_avg_2_wk = perc(contact_hour_10to11_min_tot_2_wk, contact_hour_10to11_cnt_2_wk)
        contact_hour_12to13_min_avg_2_wk = perc(contact_hour_12to13_min_tot_2_wk, contact_hour_12to13_cnt_2_wk)
        contact_hour_14to15_min_avg_2_wk = perc(contact_hour_14to15_min_tot_2_wk, contact_hour_14to15_cnt_2_wk)
        contact_hour_16to17_min_avg_2_wk = perc(contact_hour_16to17_min_tot_2_wk, contact_hour_16to17_cnt_2_wk)
        contact_hour_18to19_min_avg_2_wk = perc(contact_hour_18to19_min_tot_2_wk, contact_hour_18to19_cnt_2_wk)
        contact_hour_20to21_min_avg_2_wk = perc(contact_hour_20to21_min_tot_2_wk, contact_hour_20to21_cnt_2_wk)
        contact_hour_22to23_min_avg_2_wk = perc(contact_hour_22to23_min_tot_2_wk, contact_hour_22to23_cnt_2_wk)

        contact_hour_1to6_min_avg = perc(contact_hour_1to6_min_tot, contact_hour_1to6_cnt)
        contact_hour_7to12_min_avg = perc(contact_hour_7to12_min_tot, contact_hour_7to12_cnt)
        contact_hour_13to18_min_avg = perc(contact_hour_13to18_min_tot, contact_hour_13to18_cnt)
        contact_hour_19to0_min_avg = perc(contact_hour_19to0_min_tot, contact_hour_19to0_cnt)

        contact_hour_1to6_min_avg_6_mon = perc(contact_hour_1to6_min_tot_6_mon, contact_hour_1to6_cnt_6_mon)
        contact_hour_7to12_min_avg_6_mon = perc(contact_hour_7to12_min_tot_6_mon, contact_hour_7to12_cnt_6_mon)
        contact_hour_13to18_min_avg_6_mon = perc(contact_hour_13to18_min_tot_6_mon, contact_hour_13to18_cnt_6_mon)
        contact_hour_19to0_min_avg_6_mon = perc(contact_hour_19to0_min_tot_6_mon, contact_hour_19to0_cnt_6_mon)

        contact_hour_1to6_min_avg_3_mon = perc(contact_hour_1to6_min_tot_3_mon, contact_hour_1to6_cnt_3_mon)
        contact_hour_7to12_min_avg_3_mon = perc(contact_hour_7to12_min_tot_3_mon, contact_hour_7to12_cnt_3_mon)
        contact_hour_13to18_min_avg_3_mon = perc(contact_hour_13to18_min_tot_3_mon, contact_hour_13to18_cnt_3_mon)
        contact_hour_19to0_min_avg_3_mon = perc(contact_hour_19to0_min_tot_3_mon, contact_hour_19to0_cnt_3_mon)

        contact_hour_1to6_min_avg_2_mon = perc(contact_hour_1to6_min_tot_2_mon, contact_hour_1to6_cnt_2_mon)
        contact_hour_7to12_min_avg_2_mon = perc(contact_hour_7to12_min_tot_2_mon, contact_hour_7to12_cnt_2_mon)
        contact_hour_13to18_min_avg_2_mon = perc(contact_hour_13to18_min_tot_2_mon, contact_hour_13to18_cnt_2_mon)
        contact_hour_19to0_min_avg_2_mon = perc(contact_hour_19to0_min_tot_2_mon, contact_hour_19to0_cnt_2_mon)

        contact_hour_1to6_min_avg_1_mon = perc(contact_hour_1to6_min_tot_1_mon, contact_hour_1to6_cnt_1_mon)
        contact_hour_7to12_min_avg_1_mon = perc(contact_hour_7to12_min_tot_1_mon, contact_hour_7to12_cnt_1_mon)
        contact_hour_13to18_min_avg_1_mon = perc(contact_hour_13to18_min_tot_1_mon, contact_hour_13to18_cnt_1_mon)
        contact_hour_19to0_min_avg_1_mon = perc(contact_hour_19to0_min_tot_1_mon, contact_hour_19to0_cnt_1_mon)

        contact_hour_1to6_min_avg_2_wk = perc(contact_hour_1to6_min_tot_2_wk, contact_hour_1to6_cnt_2_wk)
        contact_hour_7to12_min_avg_2_wk = perc(contact_hour_7to12_min_tot_2_wk, contact_hour_7to12_cnt_2_wk)
        contact_hour_13to18_min_avg_2_wk = perc(contact_hour_13to18_min_tot_2_wk, contact_hour_13to18_cnt_2_wk)
        contact_hour_19to0_min_avg_2_wk = perc(contact_hour_19to0_min_tot_2_wk, contact_hour_19to0_cnt_2_wk)

        contact_hour_1to8_min_avg = perc(contact_hour_1to8_min_tot, contact_hour_1to8_cnt)
        contact_hour_9to16_min_avg = perc(contact_hour_9to16_min_tot, contact_hour_9to16_cnt)
        contact_hour_17to0_min_avg = perc(contact_hour_17to0_min_tot, contact_hour_17to0_cnt)

        contact_hour_1to8_min_avg_6_mon = perc(contact_hour_1to8_min_tot_6_mon, contact_hour_1to8_cnt_6_mon)
        contact_hour_9to16_min_avg_6_mon = perc(contact_hour_9to16_min_tot_6_mon, contact_hour_9to16_cnt_6_mon)
        contact_hour_17to0_min_avg_6_mon = perc(contact_hour_17to0_min_tot_6_mon, contact_hour_17to0_cnt_6_mon)

        contact_hour_1to8_min_avg_3_mon = perc(contact_hour_1to8_min_tot_3_mon, contact_hour_1to8_cnt_3_mon)
        contact_hour_9to16_min_avg_3_mon = perc(contact_hour_9to16_min_tot_3_mon, contact_hour_9to16_cnt_3_mon)
        contact_hour_17to0_min_avg_3_mon = perc(contact_hour_17to0_min_tot_3_mon, contact_hour_17to0_cnt_3_mon)

        contact_hour_1to8_min_avg_2_mon = perc(contact_hour_1to8_min_tot_2_mon, contact_hour_1to8_cnt_2_mon)
        contact_hour_9to16_min_avg_2_mon = perc(contact_hour_9to16_min_tot_2_mon, contact_hour_9to16_cnt_2_mon)
        contact_hour_17to0_min_avg_2_mon = perc(contact_hour_17to0_min_tot_2_mon, contact_hour_17to0_cnt_2_mon)

        contact_hour_1to8_min_avg_1_mon = perc(contact_hour_1to8_min_tot_1_mon, contact_hour_1to8_cnt_1_mon)
        contact_hour_9to16_min_avg_1_mon = perc(contact_hour_9to16_min_tot_1_mon, contact_hour_9to16_cnt_1_mon)
        contact_hour_17to0_min_avg_1_mon = perc(contact_hour_17to0_min_tot_1_mon, contact_hour_17to0_cnt_1_mon)

        contact_hour_1to8_min_avg_2_wk = perc(contact_hour_1to8_min_tot_2_wk, contact_hour_1to8_cnt_2_wk)
        contact_hour_9to16_min_avg_2_wk = perc(contact_hour_9to16_min_tot_2_wk, contact_hour_9to16_cnt_2_wk)
        contact_hour_17to0_min_avg_2_wk = perc(contact_hour_17to0_min_tot_2_wk, contact_hour_17to0_cnt_2_wk)

        contact_hour_9to20_min_avg = perc(contact_hour_9to20_min_tot, contact_hour_9to20_cnt)
        contact_hour_21to8_min_avg = perc(contact_hour_21to8_min_tot, contact_hour_21to8_cnt)

        contact_hour_9to20_min_avg_6_mon = perc(contact_hour_9to20_min_tot_6_mon, contact_hour_9to20_cnt_6_mon)
        contact_hour_21to8_min_avg_6_mon = perc(contact_hour_21to8_min_tot_6_mon, contact_hour_21to8_cnt_6_mon)

        contact_hour_9to20_min_avg_3_mon = perc(contact_hour_9to20_min_tot_3_mon, contact_hour_9to20_cnt_3_mon)
        contact_hour_21to8_min_avg_3_mon = perc(contact_hour_21to8_min_tot_3_mon, contact_hour_21to8_cnt_3_mon)

        contact_hour_9to20_min_avg_2_mon = perc(contact_hour_9to20_min_tot_2_mon, contact_hour_9to20_cnt_2_mon)
        contact_hour_21to8_min_avg_2_mon = perc(contact_hour_21to8_min_tot_2_mon, contact_hour_21to8_cnt_2_mon)

        contact_hour_9to20_min_avg_1_mon = perc(contact_hour_9to20_min_tot_1_mon, contact_hour_9to20_cnt_1_mon)
        contact_hour_21to8_min_avg_1_mon = perc(contact_hour_21to8_min_tot_1_mon, contact_hour_21to8_cnt_1_mon)

        contact_hour_9to20_min_avg_2_wk = perc(contact_hour_9to20_min_tot_2_wk, contact_hour_9to20_cnt_2_wk)
        contact_hour_21to8_min_avg_2_wk = perc(contact_hour_21to8_min_tot_2_wk, contact_hour_21to8_cnt_2_wk)

        contact_hour_1to6_call_min_avg = perc(contact_hour_1to6_call_min_tot, contact_hour_1to6_call_cnt)
        contact_hour_7to12_call_min_avg = perc(contact_hour_7to12_call_min_tot, contact_hour_7to12_call_cnt)
        contact_hour_13to18_call_min_avg = perc(contact_hour_13to18_call_min_tot, contact_hour_13to18_call_cnt)
        contact_hour_19to0_call_min_avg = perc(contact_hour_19to0_call_min_tot, contact_hour_19to0_call_cnt)

        contact_hour_1to6_call_min_avg_6_mon = perc(contact_hour_1to6_call_min_tot_6_mon, contact_hour_1to6_call_cnt_6_mon)
        contact_hour_7to12_call_min_avg_6_mon = perc(contact_hour_7to12_call_min_tot_6_mon, contact_hour_7to12_call_cnt_6_mon)
        contact_hour_13to18_call_min_avg_6_mon = perc(contact_hour_13to18_call_min_tot_6_mon, contact_hour_13to18_call_cnt_6_mon)
        contact_hour_19to0_call_min_avg_6_mon = perc(contact_hour_19to0_call_min_tot_6_mon, contact_hour_19to0_call_cnt_6_mon)

        contact_hour_1to6_call_min_avg_3_mon = perc(contact_hour_1to6_call_min_tot_3_mon, contact_hour_1to6_call_cnt_3_mon)
        contact_hour_7to12_call_min_avg_3_mon = perc(contact_hour_7to12_call_min_tot_3_mon, contact_hour_7to12_call_cnt_3_mon)
        contact_hour_13to18_call_min_avg_3_mon = perc(contact_hour_13to18_call_min_tot_3_mon, contact_hour_13to18_call_cnt_3_mon)
        contact_hour_19to0_call_min_avg_3_mon = perc(contact_hour_19to0_call_min_tot_3_mon, contact_hour_19to0_call_cnt_3_mon)

        contact_hour_1to6_call_min_avg_2_mon = perc(contact_hour_1to6_call_min_tot_2_mon, contact_hour_1to6_call_cnt_2_mon)
        contact_hour_7to12_call_min_avg_2_mon = perc(contact_hour_7to12_call_min_tot_2_mon, contact_hour_7to12_call_cnt_2_mon)
        contact_hour_13to18_call_min_avg_2_mon = perc(contact_hour_13to18_call_min_tot_2_mon, contact_hour_13to18_call_cnt_2_mon)
        contact_hour_19to0_call_min_avg_2_mon = perc(contact_hour_19to0_call_min_tot_2_mon, contact_hour_19to0_call_cnt_2_mon)

        contact_hour_1to6_call_min_avg_1_mon = perc(contact_hour_1to6_call_min_tot_1_mon, contact_hour_1to6_call_cnt_1_mon)
        contact_hour_7to12_call_min_avg_1_mon = perc(contact_hour_7to12_call_min_tot_1_mon, contact_hour_7to12_call_cnt_1_mon)
        contact_hour_13to18_call_min_avg_1_mon = perc(contact_hour_13to18_call_min_tot_1_mon, contact_hour_13to18_call_cnt_1_mon)
        contact_hour_19to0_call_min_avg_1_mon = perc(contact_hour_19to0_call_min_tot_1_mon, contact_hour_19to0_call_cnt_1_mon)

        contact_hour_1to6_call_min_avg_2_wk = perc(contact_hour_1to6_call_min_tot_2_wk, contact_hour_1to6_call_cnt_2_wk)
        contact_hour_7to12_call_min_avg_2_wk = perc(contact_hour_7to12_call_min_tot_2_wk, contact_hour_7to12_call_cnt_2_wk)
        contact_hour_13to18_call_min_avg_2_wk = perc(contact_hour_13to18_call_min_tot_2_wk, contact_hour_13to18_call_cnt_2_wk)
        contact_hour_19to0_call_min_avg_2_wk = perc(contact_hour_19to0_call_min_tot_2_wk, contact_hour_19to0_call_cnt_2_wk)

        contact_hour_1to8_call_min_avg = perc(contact_hour_1to8_call_min_tot, contact_hour_1to8_call_cnt)
        contact_hour_9to16_call_min_avg = perc(contact_hour_9to16_call_min_tot, contact_hour_9to16_call_cnt)
        contact_hour_17to0_call_min_avg = perc(contact_hour_17to0_call_min_tot, contact_hour_17to0_call_cnt)

        contact_hour_1to8_call_min_avg_6_mon = perc(contact_hour_1to8_call_min_tot_6_mon, contact_hour_1to8_call_cnt_6_mon)
        contact_hour_9to16_call_min_avg_6_mon = perc(contact_hour_9to16_call_min_tot_6_mon, contact_hour_9to16_call_cnt_6_mon)
        contact_hour_17to0_call_min_avg_6_mon = perc(contact_hour_17to0_call_min_tot_6_mon, contact_hour_17to0_call_cnt_6_mon)

        contact_hour_1to8_call_min_avg_3_mon = perc(contact_hour_1to8_call_min_tot_3_mon, contact_hour_1to8_call_cnt_3_mon)
        contact_hour_9to16_call_min_avg_3_mon = perc(contact_hour_9to16_call_min_tot_3_mon, contact_hour_9to16_call_cnt_3_mon)
        contact_hour_17to0_call_min_avg_3_mon = perc(contact_hour_17to0_call_min_tot_3_mon, contact_hour_17to0_call_cnt_3_mon)

        contact_hour_1to8_call_min_avg_2_mon = perc(contact_hour_1to8_call_min_tot_2_mon, contact_hour_1to8_call_cnt_2_mon)
        contact_hour_9to16_call_min_avg_2_mon = perc(contact_hour_9to16_call_min_tot_2_mon, contact_hour_9to16_call_cnt_2_mon)
        contact_hour_17to0_call_min_avg_2_mon = perc(contact_hour_17to0_call_min_tot_2_mon, contact_hour_17to0_call_cnt_2_mon)

        contact_hour_1to8_call_min_avg_1_mon = perc(contact_hour_1to8_call_min_tot_1_mon, contact_hour_1to8_call_cnt_1_mon)
        contact_hour_9to16_call_min_avg_1_mon = perc(contact_hour_9to16_call_min_tot_1_mon, contact_hour_9to16_call_cnt_1_mon)
        contact_hour_17to0_call_min_avg_1_mon = perc(contact_hour_17to0_call_min_tot_1_mon, contact_hour_17to0_call_cnt_1_mon)

        contact_hour_1to8_call_min_avg_2_wk = perc(contact_hour_1to8_call_min_tot_2_wk, contact_hour_1to8_call_cnt_2_wk)
        contact_hour_9to16_call_min_avg_2_wk = perc(contact_hour_9to16_call_min_tot_2_wk, contact_hour_9to16_call_cnt_2_wk)
        contact_hour_17to0_call_min_avg_2_wk = perc(contact_hour_17to0_call_min_tot_2_wk, contact_hour_17to0_call_cnt_2_wk)

        contact_hour_9to20_call_min_avg = perc(contact_hour_9to20_call_min_tot, contact_hour_9to20_call_cnt)
        contact_hour_21to8_call_min_avg = perc(contact_hour_21to8_call_min_tot, contact_hour_21to8_call_cnt)

        contact_hour_9to20_call_min_avg_6_mon = perc(contact_hour_9to20_call_min_tot_6_mon, contact_hour_9to20_call_cnt_6_mon)
        contact_hour_21to8_call_min_avg_6_mon = perc(contact_hour_21to8_call_min_tot_6_mon, contact_hour_21to8_call_cnt_6_mon)

        contact_hour_9to20_call_min_avg_3_mon = perc(contact_hour_9to20_call_min_tot_3_mon, contact_hour_9to20_call_cnt_3_mon)
        contact_hour_21to8_call_min_avg_3_mon = perc(contact_hour_21to8_call_min_tot_3_mon, contact_hour_21to8_call_cnt_3_mon)

        contact_hour_9to20_call_min_avg_2_mon = perc(contact_hour_9to20_call_min_tot_2_mon, contact_hour_9to20_call_cnt_2_mon)
        contact_hour_21to8_call_min_avg_2_mon = perc(contact_hour_21to8_call_min_tot_2_mon, contact_hour_21to8_call_cnt_2_mon)

        contact_hour_9to20_call_min_avg_1_mon = perc(contact_hour_9to20_call_min_tot_1_mon, contact_hour_9to20_call_cnt_1_mon)
        contact_hour_21to8_call_min_avg_1_mon = perc(contact_hour_21to8_call_min_tot_1_mon, contact_hour_21to8_call_cnt_1_mon)

        contact_hour_9to20_call_min_avg_2_wk = perc(contact_hour_9to20_call_min_tot_2_wk, contact_hour_9to20_call_cnt_2_wk)
        contact_hour_21to8_call_min_avg_2_wk = perc(contact_hour_21to8_call_min_tot_2_wk, contact_hour_21to8_call_cnt_2_wk)

        contact_hour_1to6_rece_min_avg = perc(contact_hour_1to6_rece_min_tot, contact_hour_1to6_rece_cnt)
        contact_hour_7to12_rece_min_avg = perc(contact_hour_7to12_rece_min_tot, contact_hour_7to12_rece_cnt)
        contact_hour_13to18_rece_min_avg = perc(contact_hour_13to18_rece_min_tot, contact_hour_13to18_rece_cnt)
        contact_hour_19to0_rece_min_avg = perc(contact_hour_19to0_rece_min_tot, contact_hour_19to0_rece_cnt)

        contact_hour_1to6_rece_min_avg_6_mon = perc(contact_hour_1to6_rece_min_tot_6_mon, contact_hour_1to6_rece_cnt_6_mon)
        contact_hour_7to12_rece_min_avg_6_mon = perc(contact_hour_7to12_rece_min_tot_6_mon, contact_hour_7to12_rece_cnt_6_mon)
        contact_hour_13to18_rece_min_avg_6_mon = perc(contact_hour_13to18_rece_min_tot_6_mon, contact_hour_13to18_rece_cnt_6_mon)
        contact_hour_19to0_rece_min_avg_6_mon = perc(contact_hour_19to0_rece_min_tot_6_mon, contact_hour_19to0_rece_cnt_6_mon)

        contact_hour_1to6_rece_min_avg_3_mon = perc(contact_hour_1to6_rece_min_tot_3_mon, contact_hour_1to6_rece_cnt_3_mon)
        contact_hour_7to12_rece_min_avg_3_mon = perc(contact_hour_7to12_rece_min_tot_3_mon, contact_hour_7to12_rece_cnt_3_mon)
        contact_hour_13to18_rece_min_avg_3_mon = perc(contact_hour_13to18_rece_min_tot_3_mon, contact_hour_13to18_rece_cnt_3_mon)
        contact_hour_19to0_rece_min_avg_3_mon = perc(contact_hour_19to0_rece_min_tot_3_mon, contact_hour_19to0_rece_cnt_3_mon)

        contact_hour_1to6_rece_min_avg_2_mon = perc(contact_hour_1to6_rece_min_tot_2_mon, contact_hour_1to6_rece_cnt_2_mon)
        contact_hour_7to12_rece_min_avg_2_mon = perc(contact_hour_7to12_rece_min_tot_2_mon, contact_hour_7to12_rece_cnt_2_mon)
        contact_hour_13to18_rece_min_avg_2_mon = perc(contact_hour_13to18_rece_min_tot_2_mon, contact_hour_13to18_rece_cnt_2_mon)
        contact_hour_19to0_rece_min_avg_2_mon = perc(contact_hour_19to0_rece_min_tot_2_mon, contact_hour_19to0_rece_cnt_2_mon)

        contact_hour_1to6_rece_min_avg_1_mon = perc(contact_hour_1to6_rece_min_tot_1_mon, contact_hour_1to6_rece_cnt_1_mon)
        contact_hour_7to12_rece_min_avg_1_mon = perc(contact_hour_7to12_rece_min_tot_1_mon, contact_hour_7to12_rece_cnt_1_mon)
        contact_hour_13to18_rece_min_avg_1_mon = perc(contact_hour_13to18_rece_min_tot_1_mon, contact_hour_13to18_rece_cnt_1_mon)
        contact_hour_19to0_rece_min_avg_1_mon = perc(contact_hour_19to0_rece_min_tot_1_mon, contact_hour_19to0_rece_cnt_1_mon)

        contact_hour_1to6_rece_min_avg_2_wk = perc(contact_hour_1to6_rece_min_tot_2_wk, contact_hour_1to6_rece_cnt_2_wk)
        contact_hour_7to12_rece_min_avg_2_wk = perc(contact_hour_7to12_rece_min_tot_2_wk, contact_hour_7to12_rece_cnt_2_wk)
        contact_hour_13to18_rece_min_avg_2_wk = perc(contact_hour_13to18_rece_min_tot_2_wk, contact_hour_13to18_rece_cnt_2_wk)
        contact_hour_19to0_rece_min_avg_2_wk = perc(contact_hour_19to0_rece_min_tot_2_wk, contact_hour_19to0_rece_cnt_2_wk)

        contact_hour_1to8_rece_min_avg = perc(contact_hour_1to8_rece_min_tot, contact_hour_1to8_rece_cnt)
        contact_hour_9to16_rece_min_avg = perc(contact_hour_9to16_rece_min_tot, contact_hour_9to16_rece_cnt)
        contact_hour_17to0_rece_min_avg = perc(contact_hour_17to0_rece_min_tot, contact_hour_17to0_rece_cnt)

        contact_hour_1to8_rece_min_avg_6_mon = perc(contact_hour_1to8_rece_min_tot_6_mon, contact_hour_1to8_rece_cnt_6_mon)
        contact_hour_9to16_rece_min_avg_6_mon = perc(contact_hour_9to16_rece_min_tot_6_mon, contact_hour_9to16_rece_cnt_6_mon)
        contact_hour_17to0_rece_min_avg_6_mon = perc(contact_hour_17to0_rece_min_tot_6_mon, contact_hour_17to0_rece_cnt_6_mon)

        contact_hour_1to8_rece_min_avg_3_mon = perc(contact_hour_1to8_rece_min_tot_3_mon, contact_hour_1to8_rece_cnt_3_mon)
        contact_hour_9to16_rece_min_avg_3_mon = perc(contact_hour_9to16_rece_min_tot_3_mon, contact_hour_9to16_rece_cnt_3_mon)
        contact_hour_17to0_rece_min_avg_3_mon = perc(contact_hour_17to0_rece_min_tot_3_mon, contact_hour_17to0_rece_cnt_3_mon)

        contact_hour_1to8_rece_min_avg_2_mon = perc(contact_hour_1to8_rece_min_tot_2_mon, contact_hour_1to8_rece_cnt_2_mon)
        contact_hour_9to16_rece_min_avg_2_mon = perc(contact_hour_9to16_rece_min_tot_2_mon, contact_hour_9to16_rece_cnt_2_mon)
        contact_hour_17to0_rece_min_avg_2_mon = perc(contact_hour_17to0_rece_min_tot_2_mon, contact_hour_17to0_rece_cnt_2_mon)

        contact_hour_1to8_rece_min_avg_1_mon = perc(contact_hour_1to8_rece_min_tot_1_mon, contact_hour_1to8_rece_cnt_1_mon)
        contact_hour_9to16_rece_min_avg_1_mon = perc(contact_hour_9to16_rece_min_tot_1_mon, contact_hour_9to16_rece_cnt_1_mon)
        contact_hour_17to0_rece_min_avg_1_mon = perc(contact_hour_17to0_rece_min_tot_1_mon, contact_hour_17to0_rece_cnt_1_mon)

        contact_hour_1to8_rece_min_avg_2_wk = perc(contact_hour_1to8_rece_min_tot_2_wk, contact_hour_1to8_rece_cnt_2_wk)
        contact_hour_9to16_rece_min_avg_2_wk = perc(contact_hour_9to16_rece_min_tot_2_wk, contact_hour_9to16_rece_cnt_2_wk)
        contact_hour_17to0_rece_min_avg_2_wk = perc(contact_hour_17to0_rece_min_tot_2_wk, contact_hour_17to0_rece_cnt_2_wk)

        contact_hour_9to20_rece_min_avg = perc(contact_hour_9to20_rece_min_tot, contact_hour_9to20_rece_cnt)
        contact_hour_21to8_rece_min_avg = perc(contact_hour_21to8_rece_min_tot, contact_hour_21to8_rece_cnt)

        contact_hour_9to20_rece_min_avg_6_mon = perc(contact_hour_9to20_rece_min_tot_6_mon, contact_hour_9to20_rece_cnt_6_mon)
        contact_hour_21to8_rece_min_avg_6_mon = perc(contact_hour_21to8_rece_min_tot_6_mon, contact_hour_21to8_rece_cnt_6_mon)

        contact_hour_9to20_rece_min_avg_3_mon = perc(contact_hour_9to20_rece_min_tot_3_mon, contact_hour_9to20_rece_cnt_3_mon)
        contact_hour_21to8_rece_min_avg_3_mon = perc(contact_hour_21to8_rece_min_tot_3_mon, contact_hour_21to8_rece_cnt_3_mon)

        contact_hour_9to20_rece_min_avg_2_mon = perc(contact_hour_9to20_rece_min_tot_2_mon, contact_hour_9to20_rece_cnt_2_mon)
        contact_hour_21to8_rece_min_avg_2_mon = perc(contact_hour_21to8_rece_min_tot_2_mon, contact_hour_21to8_rece_cnt_2_mon)

        contact_hour_9to20_rece_min_avg_1_mon = perc(contact_hour_9to20_rece_min_tot_1_mon, contact_hour_9to20_rece_cnt_1_mon)
        contact_hour_21to8_rece_min_avg_1_mon = perc(contact_hour_21to8_rece_min_tot_1_mon, contact_hour_21to8_rece_cnt_1_mon)

        contact_hour_9to20_rece_min_avg_2_wk = perc(contact_hour_9to20_rece_min_tot_2_wk, contact_hour_9to20_rece_cnt_2_wk)
        contact_hour_21to8_rece_min_avg_2_wk = perc(contact_hour_21to8_rece_min_tot_2_wk, contact_hour_21to8_rece_cnt_2_wk)

        # perc divided by 24 hours stats
        contact_hour_1to6_cnt_24h_perc = perc(contact_hour_1to6_cnt, contact_hour_0to23_cnt)
        contact_hour_7to12_cnt_24h_perc = perc(contact_hour_7to12_cnt, contact_hour_0to23_cnt)
        contact_hour_13to18_cnt_24h_perc = perc(contact_hour_13to18_cnt, contact_hour_0to23_cnt)
        contact_hour_19to0_cnt_24h_perc = perc(contact_hour_19to0_cnt, contact_hour_0to23_cnt)

        contact_hour_1to6_min_tot_24h_perc = perc(contact_hour_1to6_min_tot, contact_hour_0to23_min_tot)
        contact_hour_7to12_min_tot_24h_perc = perc(contact_hour_7to12_min_tot, contact_hour_0to23_min_tot)
        contact_hour_13to18_min_tot_24h_perc = perc(contact_hour_13to18_min_tot, contact_hour_0to23_min_tot)
        contact_hour_19to0_min_tot_24h_perc = perc(contact_hour_19to0_min_tot, contact_hour_0to23_min_tot)

        contact_hour_1to6_cnt_6_mon_24h_perc = perc(contact_hour_1to6_cnt_6_mon, contact_hour_0to23_cnt_6_mon)
        contact_hour_7to12_cnt_6_mon_24h_perc = perc(contact_hour_7to12_cnt_6_mon, contact_hour_0to23_cnt_6_mon)
        contact_hour_13to18_cnt_6_mon_24h_perc = perc(contact_hour_13to18_cnt_6_mon, contact_hour_0to23_cnt_6_mon)
        contact_hour_19to0_cnt_6_mon_24h_perc = perc(contact_hour_19to0_cnt_6_mon, contact_hour_0to23_cnt_6_mon)

        contact_hour_1to6_min_tot_6_mon_24h_perc = perc(contact_hour_1to6_min_tot_6_mon, contact_hour_0to23_min_tot_6_mon)
        contact_hour_7to12_min_tot_6_mon_24h_perc = perc(contact_hour_7to12_min_tot_6_mon, contact_hour_0to23_min_tot_6_mon)
        contact_hour_13to18_min_tot_6_mon_24h_perc = perc(contact_hour_13to18_min_tot_6_mon, contact_hour_0to23_min_tot_6_mon)
        contact_hour_19to0_min_tot_6_mon_24h_perc = perc(contact_hour_19to0_min_tot_6_mon, contact_hour_0to23_min_tot_6_mon)

        contact_hour_1to6_cnt_3_mon_24h_perc = perc(contact_hour_1to6_cnt_3_mon, contact_hour_0to23_cnt_3_mon)
        contact_hour_7to12_cnt_3_mon_24h_perc = perc(contact_hour_7to12_cnt_3_mon, contact_hour_0to23_cnt_3_mon)
        contact_hour_13to18_cnt_3_mon_24h_perc = perc(contact_hour_13to18_cnt_3_mon, contact_hour_0to23_cnt_3_mon)
        contact_hour_19to0_cnt_3_mon_24h_perc = perc(contact_hour_19to0_cnt_3_mon, contact_hour_0to23_cnt_3_mon)

        contact_hour_1to6_min_tot_3_mon_24h_perc = perc(contact_hour_1to6_min_tot_3_mon, contact_hour_0to23_min_tot_3_mon)
        contact_hour_7to12_min_tot_3_mon_24h_perc = perc(contact_hour_7to12_min_tot_3_mon, contact_hour_0to23_min_tot_3_mon)
        contact_hour_13to18_min_tot_3_mon_24h_perc = perc(contact_hour_13to18_min_tot_3_mon, contact_hour_0to23_min_tot_3_mon)
        contact_hour_19to0_min_tot_3_mon_24h_perc = perc(contact_hour_19to0_min_tot_3_mon, contact_hour_0to23_min_tot_3_mon)

        contact_hour_1to6_cnt_2_mon_24h_perc = perc(contact_hour_1to6_cnt_2_mon, contact_hour_0to23_cnt_2_mon)
        contact_hour_7to12_cnt_2_mon_24h_perc = perc(contact_hour_7to12_cnt_2_mon, contact_hour_0to23_cnt_2_mon)
        contact_hour_13to18_cnt_2_mon_24h_perc = perc(contact_hour_13to18_cnt_2_mon, contact_hour_0to23_cnt_2_mon)
        contact_hour_19to0_cnt_2_mon_24h_perc = perc(contact_hour_19to0_cnt_2_mon, contact_hour_0to23_cnt_2_mon)

        contact_hour_1to6_min_tot_2_mon_24h_perc = perc(contact_hour_1to6_min_tot_2_mon, contact_hour_0to23_min_tot_2_mon)
        contact_hour_7to12_min_tot_2_mon_24h_perc = perc(contact_hour_7to12_min_tot_2_mon, contact_hour_0to23_min_tot_2_mon)
        contact_hour_13to18_min_tot_2_mon_24h_perc = perc(contact_hour_13to18_min_tot_2_mon, contact_hour_0to23_min_tot_2_mon)
        contact_hour_19to0_min_tot_2_mon_24h_perc = perc(contact_hour_19to0_min_tot_2_mon, contact_hour_0to23_min_tot_2_mon)

        contact_hour_1to6_cnt_1_mon_24h_perc = perc(contact_hour_1to6_cnt_1_mon, contact_hour_0to23_cnt_1_mon)
        contact_hour_7to12_cnt_1_mon_24h_perc = perc(contact_hour_7to12_cnt_1_mon, contact_hour_0to23_cnt_1_mon)
        contact_hour_13to18_cnt_1_mon_24h_perc = perc(contact_hour_13to18_cnt_1_mon, contact_hour_0to23_cnt_1_mon)
        contact_hour_19to0_cnt_1_mon_24h_perc = perc(contact_hour_19to0_cnt_1_mon, contact_hour_0to23_cnt_1_mon)

        contact_hour_1to6_min_tot_1_mon_24h_perc = perc(contact_hour_1to6_min_tot_1_mon, contact_hour_0to23_min_tot_1_mon)
        contact_hour_7to12_min_tot_1_mon_24h_perc = perc(contact_hour_7to12_min_tot_1_mon, contact_hour_0to23_min_tot_1_mon)
        contact_hour_13to18_min_tot_1_mon_24h_perc = perc(contact_hour_13to18_min_tot_1_mon, contact_hour_0to23_min_tot_1_mon)
        contact_hour_19to0_min_tot_1_mon_24h_perc = perc(contact_hour_19to0_min_tot_1_mon, contact_hour_0to23_min_tot_1_mon)

        contact_hour_1to6_cnt_2_wk_24h_perc = perc(contact_hour_1to6_cnt_2_wk, contact_hour_0to23_cnt_2_wk)
        contact_hour_7to12_cnt_2_wk_24h_perc = perc(contact_hour_7to12_cnt_2_wk, contact_hour_0to23_cnt_2_wk)
        contact_hour_13to18_cnt_2_wk_24h_perc = perc(contact_hour_13to18_cnt_2_wk, contact_hour_0to23_cnt_2_wk)
        contact_hour_19to0_cnt_2_wk_24h_perc = perc(contact_hour_19to0_cnt_2_wk, contact_hour_0to23_cnt_2_wk)

        contact_hour_1to6_min_tot_2_wk_24h_perc = perc(contact_hour_1to6_min_tot_2_wk, contact_hour_0to23_min_tot_2_wk)
        contact_hour_7to12_min_tot_2_wk_24h_perc = perc(contact_hour_7to12_min_tot_2_wk, contact_hour_0to23_min_tot_2_wk)
        contact_hour_13to18_min_tot_2_wk_24h_perc = perc(contact_hour_13to18_min_tot_2_wk, contact_hour_0to23_min_tot_2_wk)
        contact_hour_19to0_min_tot_2_wk_24h_perc = perc(contact_hour_19to0_min_tot_2_wk, contact_hour_0to23_min_tot_2_wk)

        contact_hour_1to8_cnt_24h_perc = perc(contact_hour_1to8_cnt, contact_hour_0to23_cnt)
        contact_hour_9to16_cnt_24h_perc = perc(contact_hour_9to16_cnt, contact_hour_0to23_cnt)
        contact_hour_17to0_cnt_24h_perc = perc(contact_hour_17to0_cnt, contact_hour_0to23_cnt)

        contact_hour_1to8_min_tot_24h_perc = perc(contact_hour_1to8_min_tot, contact_hour_0to23_min_tot)
        contact_hour_9to16_min_tot_24h_perc = perc(contact_hour_9to16_min_tot, contact_hour_0to23_min_tot)
        contact_hour_17to0_min_tot_24h_perc = perc(contact_hour_17to0_min_tot, contact_hour_0to23_min_tot)

        contact_hour_1to8_cnt_6_mon_24h_perc = perc(contact_hour_1to8_cnt_6_mon, contact_hour_0to23_cnt_6_mon)
        contact_hour_9to16_cnt_6_mon_24h_perc = perc(contact_hour_9to16_cnt_6_mon, contact_hour_0to23_cnt_6_mon)
        contact_hour_17to0_cnt_6_mon_24h_perc = perc(contact_hour_17to0_cnt_6_mon, contact_hour_0to23_cnt_6_mon)

        contact_hour_1to8_min_tot_6_mon_24h_perc = perc(contact_hour_1to8_min_tot_6_mon, contact_hour_0to23_min_tot_6_mon)
        contact_hour_9to16_min_tot_6_mon_24h_perc = perc(contact_hour_9to16_min_tot_6_mon, contact_hour_0to23_min_tot_6_mon)
        contact_hour_17to0_min_tot_6_mon_24h_perc = perc(contact_hour_17to0_min_tot_6_mon, contact_hour_0to23_min_tot_6_mon)

        contact_hour_1to8_cnt_3_mon_24h_perc = perc(contact_hour_1to8_cnt_3_mon, contact_hour_0to23_cnt_3_mon)
        contact_hour_9to16_cnt_3_mon_24h_perc = perc(contact_hour_9to16_cnt_3_mon, contact_hour_0to23_cnt_3_mon)
        contact_hour_17to0_cnt_3_mon_24h_perc = perc(contact_hour_17to0_cnt_3_mon, contact_hour_0to23_cnt_3_mon)

        contact_hour_1to8_min_tot_3_mon_24h_perc = perc(contact_hour_1to8_min_tot_3_mon, contact_hour_0to23_min_tot_3_mon)
        contact_hour_9to16_min_tot_3_mon_24h_perc = perc(contact_hour_9to16_min_tot_3_mon, contact_hour_0to23_min_tot_3_mon)
        contact_hour_17to0_min_tot_3_mon_24h_perc = perc(contact_hour_17to0_min_tot_3_mon, contact_hour_0to23_min_tot_3_mon)

        contact_hour_1to8_cnt_2_mon_24h_perc = perc(contact_hour_1to8_cnt_2_mon, contact_hour_0to23_cnt_2_mon)
        contact_hour_9to16_cnt_2_mon_24h_perc = perc(contact_hour_9to16_cnt_2_mon, contact_hour_0to23_cnt_2_mon)
        contact_hour_17to0_cnt_2_mon_24h_perc = perc(contact_hour_17to0_cnt_2_mon, contact_hour_0to23_cnt_2_mon)

        contact_hour_1to8_min_tot_2_mon_24h_perc = perc(contact_hour_1to8_min_tot_2_mon, contact_hour_0to23_min_tot_2_mon)
        contact_hour_9to16_min_tot_2_mon_24h_perc = perc(contact_hour_9to16_min_tot_2_mon, contact_hour_0to23_min_tot_2_mon)
        contact_hour_17to0_min_tot_2_mon_24h_perc = perc(contact_hour_17to0_min_tot_2_mon, contact_hour_0to23_min_tot_2_mon)

        contact_hour_1to8_cnt_1_mon_24h_perc = perc(contact_hour_1to8_cnt_1_mon, contact_hour_0to23_cnt_1_mon)
        contact_hour_9to16_cnt_1_mon_24h_perc = perc(contact_hour_9to16_cnt_1_mon, contact_hour_0to23_cnt_1_mon)
        contact_hour_17to0_cnt_1_mon_24h_perc = perc(contact_hour_17to0_cnt_1_mon, contact_hour_0to23_cnt_1_mon)

        contact_hour_1to8_min_tot_1_mon_24h_perc = perc(contact_hour_1to8_min_tot_1_mon, contact_hour_0to23_min_tot_1_mon)
        contact_hour_9to16_min_tot_1_mon_24h_perc = perc(contact_hour_9to16_min_tot_1_mon, contact_hour_0to23_min_tot_1_mon)
        contact_hour_17to0_min_tot_1_mon_24h_perc = perc(contact_hour_17to0_min_tot_1_mon, contact_hour_0to23_min_tot_1_mon)

        contact_hour_1to8_cnt_2_wk_24h_perc = perc(contact_hour_1to8_cnt_2_wk, contact_hour_0to23_cnt_2_wk)
        contact_hour_9to16_cnt_2_wk_24h_perc = perc(contact_hour_9to16_cnt_2_wk, contact_hour_0to23_cnt_2_wk)
        contact_hour_17to0_cnt_2_wk_24h_perc = perc(contact_hour_17to0_cnt_2_wk, contact_hour_0to23_cnt_2_wk)

        contact_hour_1to8_min_tot_2_wk_24h_perc = perc(contact_hour_1to8_min_tot_2_wk, contact_hour_0to23_min_tot_2_wk)
        contact_hour_9to16_min_tot_2_wk_24h_perc = perc(contact_hour_9to16_min_tot_2_wk, contact_hour_0to23_min_tot_2_wk)
        contact_hour_17to0_min_tot_2_wk_24h_perc = perc(contact_hour_17to0_min_tot_2_wk, contact_hour_0to23_min_tot_2_wk)

        contact_hour_9to20_cnt_24_hour_perc = perc(contact_hour_9to20_cnt, contact_hour_0to23_cnt)
        contact_hour_21to8_cnt_24_hour_perc = perc(contact_hour_21to8_cnt, contact_hour_0to23_cnt)

        contact_hour_9to20_min_tot_24_hour_perc = perc(contact_hour_9to20_min_tot, contact_hour_0to23_min_tot)
        contact_hour_21to8_min_tot_24_hour_perc = perc(contact_hour_21to8_min_tot, contact_hour_0to23_min_tot)

        contact_hour_9to20_cnt_6_mon_24_hour_perc = perc(contact_hour_9to20_cnt_6_mon, contact_hour_0to23_cnt_6_mon)
        contact_hour_21to8_cnt_6_mon_24_hour_perc = perc(contact_hour_21to8_cnt_6_mon, contact_hour_0to23_cnt_6_mon)

        contact_hour_9to20_min_tot_6_mon_24_hour_perc = perc(contact_hour_9to20_min_tot_6_mon, contact_hour_0to23_min_tot_6_mon)
        contact_hour_21to8_min_tot_6_mon_24_hour_perc = perc(contact_hour_21to8_min_tot_6_mon, contact_hour_0to23_min_tot_6_mon)

        contact_hour_9to20_cnt_3_mon_24_hour_perc = perc(contact_hour_9to20_cnt_3_mon, contact_hour_0to23_cnt_3_mon)
        contact_hour_21to8_cnt_3_mon_24_hour_perc = perc(contact_hour_21to8_cnt_3_mon, contact_hour_0to23_cnt_3_mon)

        contact_hour_9to20_min_tot_3_mon_24_hour_perc = perc(contact_hour_9to20_min_tot_3_mon, contact_hour_0to23_min_tot_3_mon)
        contact_hour_21to8_min_tot_3_mon_24_hour_perc = perc(contact_hour_21to8_min_tot_3_mon, contact_hour_0to23_min_tot_3_mon)

        contact_hour_9to20_cnt_2_mon_24_hour_perc = perc(contact_hour_9to20_cnt_2_mon, contact_hour_0to23_cnt_2_mon)
        contact_hour_21to8_cnt_2_mon_24_hour_perc = perc(contact_hour_21to8_cnt_2_mon, contact_hour_0to23_cnt_2_mon)

        contact_hour_9to20_min_tot_2_mon_24_hour_perc = perc(contact_hour_9to20_min_tot_2_mon, contact_hour_0to23_min_tot_2_mon)
        contact_hour_21to8_min_tot_2_mon_24_hour_perc = perc(contact_hour_21to8_min_tot_2_mon, contact_hour_0to23_min_tot_2_mon)

        contact_hour_9to20_cnt_2_wk_24_hour_perc = perc(contact_hour_9to20_cnt_2_wk, contact_hour_0to23_cnt_2_wk)
        contact_hour_21to8_cnt_2_wk_24_hour_perc = perc(contact_hour_21to8_cnt_2_wk, contact_hour_0to23_cnt_2_wk)

        contact_hour_9to20_min_tot_2_wk_24_hour_perc = perc(contact_hour_9to20_min_tot_2_wk, contact_hour_0to23_min_tot_2_wk)
        contact_hour_21to8_min_tot_2_wk_24_hour_perc = perc(contact_hour_21to8_min_tot_2_wk, contact_hour_0to23_min_tot_2_wk)

        contact_hour_1to6_call_cnt_24h_perc = perc(contact_hour_1to6_call_cnt, contact_hour_0to23_call_cnt)
        contact_hour_7to12_call_cnt_24h_perc = perc(contact_hour_7to12_call_cnt, contact_hour_0to23_call_cnt)
        contact_hour_13to18_call_cnt_24h_perc = perc(contact_hour_13to18_call_cnt, contact_hour_0to23_call_cnt)
        contact_hour_19to0_call_cnt_24h_perc = perc(contact_hour_19to0_call_cnt, contact_hour_0to23_call_cnt)

        contact_hour_1to6_call_min_tot_24h_perc = perc(contact_hour_1to6_call_min_tot, contact_hour_0to23_call_min_tot)
        contact_hour_7to12_call_min_tot_24h_perc = perc(contact_hour_7to12_call_min_tot, contact_hour_0to23_call_min_tot)
        contact_hour_13to18_call_min_tot_24h_perc = perc(contact_hour_13to18_call_min_tot, contact_hour_0to23_call_min_tot)
        contact_hour_19to0_call_min_tot_24h_perc = perc(contact_hour_19to0_call_min_tot, contact_hour_0to23_call_min_tot)

        contact_hour_1to6_call_cnt_6_mon_24h_perc = perc(contact_hour_1to6_call_cnt_6_mon, contact_hour_0to23_call_cnt_6_mon)
        contact_hour_7to12_call_cnt_6_mon_24h_perc = perc(contact_hour_7to12_call_cnt_6_mon, contact_hour_0to23_call_cnt_6_mon)
        contact_hour_13to18_call_cnt_6_mon_24h_perc = perc(contact_hour_13to18_call_cnt_6_mon, contact_hour_0to23_call_cnt_6_mon)
        contact_hour_19to0_call_cnt_6_mon_24h_perc = perc(contact_hour_19to0_call_cnt_6_mon, contact_hour_0to23_call_cnt_6_mon)

        contact_hour_1to6_call_min_tot_6_mon_24h_perc = perc(contact_hour_1to6_call_min_tot_6_mon, contact_hour_0to23_call_min_tot_6_mon)
        contact_hour_7to12_call_min_tot_6_mon_24h_perc = perc(contact_hour_7to12_call_min_tot_6_mon, contact_hour_0to23_call_min_tot_6_mon)
        contact_hour_13to18_call_min_tot_6_mon_24h_perc = perc(contact_hour_13to18_call_min_tot_6_mon, contact_hour_0to23_call_min_tot_6_mon)
        contact_hour_19to0_call_min_tot_6_mon_24h_perc = perc(contact_hour_19to0_call_min_tot_6_mon, contact_hour_0to23_call_min_tot_6_mon)

        contact_hour_1to6_call_cnt_3_mon_24h_perc = perc(contact_hour_1to6_call_cnt_3_mon, contact_hour_0to23_call_cnt_3_mon)
        contact_hour_7to12_call_cnt_3_mon_24h_perc = perc(contact_hour_7to12_call_cnt_3_mon, contact_hour_0to23_call_cnt_3_mon)
        contact_hour_13to18_call_cnt_3_mon_24h_perc = perc(contact_hour_13to18_call_cnt_3_mon, contact_hour_0to23_call_cnt_3_mon)
        contact_hour_19to0_call_cnt_3_mon_24h_perc = perc(contact_hour_19to0_call_cnt_3_mon, contact_hour_0to23_call_cnt_3_mon)

        contact_hour_1to6_call_min_tot_3_mon_24h_perc = perc(contact_hour_1to6_call_min_tot_3_mon, contact_hour_0to23_call_min_tot_3_mon)
        contact_hour_7to12_call_min_tot_3_mon_24h_perc = perc(contact_hour_7to12_call_min_tot_3_mon, contact_hour_0to23_call_min_tot_3_mon)
        contact_hour_13to18_call_min_tot_3_mon_24h_perc = perc(contact_hour_13to18_call_min_tot_3_mon, contact_hour_0to23_call_min_tot_3_mon)
        contact_hour_19to0_call_min_tot_3_mon_24h_perc = perc(contact_hour_19to0_call_min_tot_3_mon, contact_hour_0to23_call_min_tot_3_mon)

        contact_hour_1to6_call_cnt_2_mon_24h_perc = perc(contact_hour_1to6_call_cnt_2_mon, contact_hour_0to23_call_cnt_2_mon)
        contact_hour_7to12_call_cnt_2_mon_24h_perc = perc(contact_hour_7to12_call_cnt_2_mon, contact_hour_0to23_call_cnt_2_mon)
        contact_hour_13to18_call_cnt_2_mon_24h_perc = perc(contact_hour_13to18_call_cnt_2_mon, contact_hour_0to23_call_cnt_2_mon)
        contact_hour_19to0_call_cnt_2_mon_24h_perc = perc(contact_hour_19to0_call_cnt_2_mon, contact_hour_0to23_call_cnt_2_mon)

        contact_hour_1to6_call_min_tot_2_mon_24h_perc = perc(contact_hour_1to6_call_min_tot_2_mon, contact_hour_0to23_call_min_tot_2_mon)
        contact_hour_7to12_call_min_tot_2_mon_24h_perc = perc(contact_hour_7to12_call_min_tot_2_mon, contact_hour_0to23_call_min_tot_2_mon)
        contact_hour_13to18_call_min_tot_2_mon_24h_perc = perc(contact_hour_13to18_call_min_tot_2_mon, contact_hour_0to23_call_min_tot_2_mon)
        contact_hour_19to0_call_min_tot_2_mon_24h_perc = perc(contact_hour_19to0_call_min_tot_2_mon, contact_hour_0to23_call_min_tot_2_mon)

        contact_hour_1to6_call_cnt_1_mon_24h_perc = perc(contact_hour_1to6_call_cnt_1_mon, contact_hour_0to23_call_cnt_1_mon)
        contact_hour_7to12_call_cnt_1_mon_24h_perc = perc(contact_hour_7to12_call_cnt_1_mon, contact_hour_0to23_call_cnt_1_mon)
        contact_hour_13to18_call_cnt_1_mon_24h_perc = perc(contact_hour_13to18_call_cnt_1_mon, contact_hour_0to23_call_cnt_1_mon)
        contact_hour_19to0_call_cnt_1_mon_24h_perc = perc(contact_hour_19to0_call_cnt_1_mon, contact_hour_0to23_call_cnt_1_mon)

        contact_hour_1to6_call_min_tot_1_mon_24h_perc = perc(contact_hour_1to6_call_min_tot_1_mon, contact_hour_0to23_call_min_tot_1_mon)
        contact_hour_7to12_call_min_tot_1_mon_24h_perc = perc(contact_hour_7to12_call_min_tot_1_mon, contact_hour_0to23_call_min_tot_1_mon)
        contact_hour_13to18_call_min_tot_1_mon_24h_perc = perc(contact_hour_13to18_call_min_tot_1_mon, contact_hour_0to23_call_min_tot_1_mon)
        contact_hour_19to0_call_min_tot_1_mon_24h_perc = perc(contact_hour_19to0_call_min_tot_1_mon, contact_hour_0to23_call_min_tot_1_mon)

        contact_hour_1to6_call_cnt_2_wk_24h_perc = perc(contact_hour_1to6_call_cnt_2_wk, contact_hour_0to23_call_cnt_2_wk)
        contact_hour_7to12_call_cnt_2_wk_24h_perc = perc(contact_hour_7to12_call_cnt_2_wk, contact_hour_0to23_call_cnt_2_wk)
        contact_hour_13to18_call_cnt_2_wk_24h_perc = perc(contact_hour_13to18_call_cnt_2_wk, contact_hour_0to23_call_cnt_2_wk)
        contact_hour_19to0_call_cnt_2_wk_24h_perc = perc(contact_hour_19to0_call_cnt_2_wk, contact_hour_0to23_call_cnt_2_wk)

        contact_hour_1to6_call_min_tot_2_wk_24h_perc = perc(contact_hour_1to6_call_min_tot_2_wk, contact_hour_0to23_call_min_tot_2_wk)
        contact_hour_7to12_call_min_tot_2_wk_24h_perc = perc(contact_hour_7to12_call_min_tot_2_wk, contact_hour_0to23_call_min_tot_2_wk)
        contact_hour_13to18_call_min_tot_2_wk_24h_perc = perc(contact_hour_13to18_call_min_tot_2_wk, contact_hour_0to23_call_min_tot_2_wk)
        contact_hour_19to0_call_min_tot_2_wk_24h_perc = perc(contact_hour_19to0_call_min_tot_2_wk, contact_hour_0to23_call_min_tot_2_wk)

        contact_hour_1to8_call_cnt_24h_perc = perc(contact_hour_1to8_call_cnt, contact_hour_0to23_call_cnt)
        contact_hour_9to16_call_cnt_24h_perc = perc(contact_hour_9to16_call_cnt, contact_hour_0to23_call_cnt)
        contact_hour_17to0_call_cnt_24h_perc = perc(contact_hour_17to0_call_cnt, contact_hour_0to23_call_cnt)

        contact_hour_1to8_call_min_tot_24h_perc = perc(contact_hour_1to8_call_min_tot, contact_hour_0to23_call_min_tot)
        contact_hour_9to16_call_min_tot_24h_perc = perc(contact_hour_9to16_call_min_tot, contact_hour_0to23_call_min_tot)
        contact_hour_17to0_call_min_tot_24h_perc = perc(contact_hour_17to0_call_min_tot, contact_hour_0to23_call_min_tot)

        contact_hour_1to8_call_cnt_6_mon_24h_perc = perc(contact_hour_1to8_call_cnt_6_mon, contact_hour_0to23_call_cnt_6_mon)
        contact_hour_9to16_call_cnt_6_mon_24h_perc = perc(contact_hour_9to16_call_cnt_6_mon, contact_hour_0to23_call_cnt_6_mon)
        contact_hour_17to0_call_cnt_6_mon_24h_perc = perc(contact_hour_17to0_call_cnt_6_mon, contact_hour_0to23_call_cnt_6_mon)

        contact_hour_1to8_call_min_tot_6_mon_24h_perc = perc(contact_hour_1to8_call_min_tot_6_mon, contact_hour_0to23_call_min_tot_6_mon)
        contact_hour_9to16_call_min_tot_6_mon_24h_perc = perc(contact_hour_9to16_call_min_tot_6_mon, contact_hour_0to23_call_min_tot_6_mon)
        contact_hour_17to0_call_min_tot_6_mon_24h_perc = perc(contact_hour_17to0_call_min_tot_6_mon, contact_hour_0to23_call_min_tot_6_mon)

        contact_hour_1to8_call_cnt_3_mon_24h_perc = perc(contact_hour_1to8_call_cnt_3_mon, contact_hour_0to23_call_cnt_3_mon)
        contact_hour_9to16_call_cnt_3_mon_24h_perc = perc(contact_hour_9to16_call_cnt_3_mon, contact_hour_0to23_call_cnt_3_mon)
        contact_hour_17to0_call_cnt_3_mon_24h_perc = perc(contact_hour_17to0_call_cnt_3_mon, contact_hour_0to23_call_cnt_3_mon)

        contact_hour_1to8_call_min_tot_3_mon_24h_perc = perc(contact_hour_1to8_call_min_tot_3_mon, contact_hour_0to23_call_min_tot_3_mon)
        contact_hour_9to16_call_min_tot_3_mon_24h_perc = perc(contact_hour_9to16_call_min_tot_3_mon, contact_hour_0to23_call_min_tot_3_mon)
        contact_hour_17to0_call_min_tot_3_mon_24h_perc = perc(contact_hour_17to0_call_min_tot_3_mon, contact_hour_0to23_call_min_tot_3_mon)

        contact_hour_1to8_call_cnt_2_mon_24h_perc = perc(contact_hour_1to8_call_cnt_2_mon, contact_hour_0to23_call_cnt_2_mon)
        contact_hour_9to16_call_cnt_2_mon_24h_perc = perc(contact_hour_9to16_call_cnt_2_mon, contact_hour_0to23_call_cnt_2_mon)
        contact_hour_17to0_call_cnt_2_mon_24h_perc = perc(contact_hour_17to0_call_cnt_2_mon, contact_hour_0to23_call_cnt_2_mon)

        contact_hour_1to8_call_min_tot_2_mon_24h_perc = perc(contact_hour_1to8_call_min_tot_2_mon, contact_hour_0to23_call_min_tot_2_mon)
        contact_hour_9to16_call_min_tot_2_mon_24h_perc = perc(contact_hour_9to16_call_min_tot_2_mon, contact_hour_0to23_call_min_tot_2_mon)
        contact_hour_17to0_call_min_tot_2_mon_24h_perc = perc(contact_hour_17to0_call_min_tot_2_mon, contact_hour_0to23_call_min_tot_2_mon)

        contact_hour_1to8_call_cnt_1_mon_24h_perc = perc(contact_hour_1to8_call_cnt_1_mon, contact_hour_0to23_call_cnt_1_mon)
        contact_hour_9to16_call_cnt_1_mon_24h_perc = perc(contact_hour_9to16_call_cnt_1_mon, contact_hour_0to23_call_cnt_1_mon)
        contact_hour_17to0_call_cnt_1_mon_24h_perc = perc(contact_hour_17to0_call_cnt_1_mon, contact_hour_0to23_call_cnt_1_mon)

        contact_hour_1to8_call_min_tot_1_mon_24h_perc = perc(contact_hour_1to8_call_min_tot_1_mon, contact_hour_0to23_call_min_tot_1_mon)
        contact_hour_9to16_call_min_tot_1_mon_24h_perc = perc(contact_hour_9to16_call_min_tot_1_mon, contact_hour_0to23_call_min_tot_1_mon)
        contact_hour_17to0_call_min_tot_1_mon_24h_perc = perc(contact_hour_17to0_call_min_tot_1_mon, contact_hour_0to23_call_min_tot_1_mon)

        contact_hour_1to8_call_cnt_2_wk_24h_perc = perc(contact_hour_1to8_call_cnt_2_wk, contact_hour_0to23_call_cnt_2_wk)
        contact_hour_9to16_call_cnt_2_wk_24h_perc = perc(contact_hour_9to16_call_cnt_2_wk, contact_hour_0to23_call_cnt_2_wk)
        contact_hour_17to0_call_cnt_2_wk_24h_perc = perc(contact_hour_17to0_call_cnt_2_wk, contact_hour_0to23_call_cnt_2_wk)

        contact_hour_1to8_call_min_tot_2_wk_24h_perc = perc(contact_hour_1to8_call_min_tot_2_wk, contact_hour_0to23_call_min_tot_2_wk)
        contact_hour_9to16_call_min_tot_2_wk_24h_perc = perc(contact_hour_9to16_call_min_tot_2_wk, contact_hour_0to23_call_min_tot_2_wk)
        contact_hour_17to0_call_min_tot_2_wk_24h_perc = perc(contact_hour_17to0_call_min_tot_2_wk, contact_hour_0to23_call_min_tot_2_wk)

        contact_hour_9to20_call_cnt_24_hour_perc = perc(contact_hour_9to20_call_cnt, contact_hour_0to23_call_cnt)
        contact_hour_21to8_call_cnt_24_hour_perc = perc(contact_hour_21to8_call_cnt, contact_hour_0to23_call_cnt)

        contact_hour_9to20_call_min_tot_24_hour_perc = perc(contact_hour_9to20_call_min_tot, contact_hour_0to23_call_min_tot)
        contact_hour_21to8_call_min_tot_24_hour_perc = perc(contact_hour_21to8_call_min_tot, contact_hour_0to23_call_min_tot)

        contact_hour_9to20_call_cnt_6_mon_24_hour_perc = perc(contact_hour_9to20_call_cnt_6_mon, contact_hour_0to23_call_cnt_6_mon)
        contact_hour_21to8_call_cnt_6_mon_24_hour_perc = perc(contact_hour_21to8_call_cnt_6_mon, contact_hour_0to23_call_cnt_6_mon)

        contact_hour_9to20_call_min_tot_6_mon_24_hour_perc = perc(contact_hour_9to20_call_min_tot_6_mon, contact_hour_0to23_call_min_tot_6_mon)
        contact_hour_21to8_call_min_tot_6_mon_24_hour_perc = perc(contact_hour_21to8_call_min_tot_6_mon, contact_hour_0to23_call_min_tot_6_mon)

        contact_hour_9to20_call_cnt_3_mon_24_hour_perc = perc(contact_hour_9to20_call_cnt_3_mon, contact_hour_0to23_call_cnt_3_mon)
        contact_hour_21to8_call_cnt_3_mon_24_hour_perc = perc(contact_hour_21to8_call_cnt_3_mon, contact_hour_0to23_call_cnt_3_mon)

        contact_hour_9to20_call_min_tot_3_mon_24_hour_perc = perc(contact_hour_9to20_call_min_tot_3_mon, contact_hour_0to23_call_min_tot_3_mon)
        contact_hour_21to8_call_min_tot_3_mon_24_hour_perc = perc(contact_hour_21to8_call_min_tot_3_mon, contact_hour_0to23_call_min_tot_3_mon)

        contact_hour_9to20_call_cnt_2_mon_24_hour_perc = perc(contact_hour_9to20_call_cnt_2_mon, contact_hour_0to23_call_cnt_2_mon)
        contact_hour_21to8_call_cnt_2_mon_24_hour_perc = perc(contact_hour_21to8_call_cnt_2_mon, contact_hour_0to23_call_cnt_2_mon)

        contact_hour_9to20_call_min_tot_2_mon_24_hour_perc = perc(contact_hour_9to20_call_min_tot_2_mon, contact_hour_0to23_call_min_tot_2_mon)
        contact_hour_21to8_call_min_tot_2_mon_24_hour_perc = perc(contact_hour_21to8_call_min_tot_2_mon, contact_hour_0to23_call_min_tot_2_mon)

        contact_hour_9to20_call_cnt_2_wk_24_hour_perc = perc(contact_hour_9to20_call_cnt_2_wk, contact_hour_0to23_call_cnt_2_wk)
        contact_hour_21to8_call_cnt_2_wk_24_hour_perc = perc(contact_hour_21to8_call_cnt_2_wk, contact_hour_0to23_call_cnt_2_wk)

        contact_hour_9to20_call_min_tot_2_wk_24_hour_perc = perc(contact_hour_9to20_call_min_tot_2_wk, contact_hour_0to23_call_min_tot_2_wk)
        contact_hour_21to8_call_min_tot_2_wk_24_hour_perc = perc(contact_hour_21to8_call_min_tot_2_wk, contact_hour_0to23_call_min_tot_2_wk)

        contact_hour_1to6_rece_cnt_24h_perc = perc(contact_hour_1to6_rece_cnt, contact_hour_0to23_rece_cnt)
        contact_hour_7to12_rece_cnt_24h_perc = perc(contact_hour_7to12_rece_cnt, contact_hour_0to23_rece_cnt)
        contact_hour_13to18_rece_cnt_24h_perc = perc(contact_hour_13to18_rece_cnt, contact_hour_0to23_rece_cnt)
        contact_hour_19to0_rece_cnt_24h_perc = perc(contact_hour_19to0_rece_cnt, contact_hour_0to23_rece_cnt)

        contact_hour_1to6_rece_min_tot_24h_perc = perc(contact_hour_1to6_rece_min_tot, contact_hour_0to23_rece_min_tot)
        contact_hour_7to12_rece_min_tot_24h_perc = perc(contact_hour_7to12_rece_min_tot, contact_hour_0to23_rece_min_tot)
        contact_hour_13to18_rece_min_tot_24h_perc = perc(contact_hour_13to18_rece_min_tot, contact_hour_0to23_rece_min_tot)
        contact_hour_19to0_rece_min_tot_24h_perc = perc(contact_hour_19to0_rece_min_tot, contact_hour_0to23_rece_min_tot)

        contact_hour_1to6_rece_cnt_6_mon_24h_perc = perc(contact_hour_1to6_rece_cnt_6_mon, contact_hour_0to23_rece_cnt_6_mon)
        contact_hour_7to12_rece_cnt_6_mon_24h_perc = perc(contact_hour_7to12_rece_cnt_6_mon, contact_hour_0to23_rece_cnt_6_mon)
        contact_hour_13to18_rece_cnt_6_mon_24h_perc = perc(contact_hour_13to18_rece_cnt_6_mon, contact_hour_0to23_rece_cnt_6_mon)
        contact_hour_19to0_rece_cnt_6_mon_24h_perc = perc(contact_hour_19to0_rece_cnt_6_mon, contact_hour_0to23_rece_cnt_6_mon)

        contact_hour_1to6_rece_min_tot_6_mon_24h_perc = perc(contact_hour_1to6_rece_min_tot_6_mon, contact_hour_0to23_rece_min_tot_6_mon)
        contact_hour_7to12_rece_min_tot_6_mon_24h_perc = perc(contact_hour_7to12_rece_min_tot_6_mon, contact_hour_0to23_rece_min_tot_6_mon)
        contact_hour_13to18_rece_min_tot_6_mon_24h_perc = perc(contact_hour_13to18_rece_min_tot_6_mon, contact_hour_0to23_rece_min_tot_6_mon)
        contact_hour_19to0_rece_min_tot_6_mon_24h_perc = perc(contact_hour_19to0_rece_min_tot_6_mon, contact_hour_0to23_rece_min_tot_6_mon)

        contact_hour_1to6_rece_cnt_3_mon_24h_perc = perc(contact_hour_1to6_rece_cnt_3_mon, contact_hour_0to23_rece_cnt_3_mon)
        contact_hour_7to12_rece_cnt_3_mon_24h_perc = perc(contact_hour_7to12_rece_cnt_3_mon, contact_hour_0to23_rece_cnt_3_mon)
        contact_hour_13to18_rece_cnt_3_mon_24h_perc = perc(contact_hour_13to18_rece_cnt_3_mon, contact_hour_0to23_rece_cnt_3_mon)
        contact_hour_19to0_rece_cnt_3_mon_24h_perc = perc(contact_hour_19to0_rece_cnt_3_mon, contact_hour_0to23_rece_cnt_3_mon)

        contact_hour_1to6_rece_min_tot_3_mon_24h_perc = perc(contact_hour_1to6_rece_min_tot_3_mon, contact_hour_0to23_rece_min_tot_3_mon)
        contact_hour_7to12_rece_min_tot_3_mon_24h_perc = perc(contact_hour_7to12_rece_min_tot_3_mon, contact_hour_0to23_rece_min_tot_3_mon)
        contact_hour_13to18_rece_min_tot_3_mon_24h_perc = perc(contact_hour_13to18_rece_min_tot_3_mon, contact_hour_0to23_rece_min_tot_3_mon)
        contact_hour_19to0_rece_min_tot_3_mon_24h_perc = perc(contact_hour_19to0_rece_min_tot_3_mon, contact_hour_0to23_rece_min_tot_3_mon)

        contact_hour_1to6_rece_cnt_2_mon_24h_perc = perc(contact_hour_1to6_rece_cnt_2_mon, contact_hour_0to23_rece_cnt_2_mon)
        contact_hour_7to12_rece_cnt_2_mon_24h_perc = perc(contact_hour_7to12_rece_cnt_2_mon, contact_hour_0to23_rece_cnt_2_mon)
        contact_hour_13to18_rece_cnt_2_mon_24h_perc = perc(contact_hour_13to18_rece_cnt_2_mon, contact_hour_0to23_rece_cnt_2_mon)
        contact_hour_19to0_rece_cnt_2_mon_24h_perc = perc(contact_hour_19to0_rece_cnt_2_mon, contact_hour_0to23_rece_cnt_2_mon)

        contact_hour_1to6_rece_min_tot_2_mon_24h_perc = perc(contact_hour_1to6_rece_min_tot_2_mon, contact_hour_0to23_rece_min_tot_2_mon)
        contact_hour_7to12_rece_min_tot_2_mon_24h_perc = perc(contact_hour_7to12_rece_min_tot_2_mon, contact_hour_0to23_rece_min_tot_2_mon)
        contact_hour_13to18_rece_min_tot_2_mon_24h_perc = perc(contact_hour_13to18_rece_min_tot_2_mon, contact_hour_0to23_rece_min_tot_2_mon)
        contact_hour_19to0_rece_min_tot_2_mon_24h_perc = perc(contact_hour_19to0_rece_min_tot_2_mon, contact_hour_0to23_rece_min_tot_2_mon)

        contact_hour_1to6_rece_cnt_1_mon_24h_perc = perc(contact_hour_1to6_rece_cnt_1_mon, contact_hour_0to23_rece_cnt_1_mon)
        contact_hour_7to12_rece_cnt_1_mon_24h_perc = perc(contact_hour_7to12_rece_cnt_1_mon, contact_hour_0to23_rece_cnt_1_mon)
        contact_hour_13to18_rece_cnt_1_mon_24h_perc = perc(contact_hour_13to18_rece_cnt_1_mon, contact_hour_0to23_rece_cnt_1_mon)
        contact_hour_19to0_rece_cnt_1_mon_24h_perc = perc(contact_hour_19to0_rece_cnt_1_mon, contact_hour_0to23_rece_cnt_1_mon)

        contact_hour_1to6_rece_min_tot_1_mon_24h_perc = perc(contact_hour_1to6_rece_min_tot_1_mon, contact_hour_0to23_rece_min_tot_1_mon)
        contact_hour_7to12_rece_min_tot_1_mon_24h_perc = perc(contact_hour_7to12_rece_min_tot_1_mon, contact_hour_0to23_rece_min_tot_1_mon)
        contact_hour_13to18_rece_min_tot_1_mon_24h_perc = perc(contact_hour_13to18_rece_min_tot_1_mon, contact_hour_0to23_rece_min_tot_1_mon)
        contact_hour_19to0_rece_min_tot_1_mon_24h_perc = perc(contact_hour_19to0_rece_min_tot_1_mon, contact_hour_0to23_rece_min_tot_1_mon)

        contact_hour_1to6_rece_cnt_2_wk_24h_perc = perc(contact_hour_1to6_rece_cnt_2_wk, contact_hour_0to23_rece_cnt_2_wk)
        contact_hour_7to12_rece_cnt_2_wk_24h_perc = perc(contact_hour_7to12_rece_cnt_2_wk, contact_hour_0to23_rece_cnt_2_wk)
        contact_hour_13to18_rece_cnt_2_wk_24h_perc = perc(contact_hour_13to18_rece_cnt_2_wk, contact_hour_0to23_rece_cnt_2_wk)
        contact_hour_19to0_rece_cnt_2_wk_24h_perc = perc(contact_hour_19to0_rece_cnt_2_wk, contact_hour_0to23_rece_cnt_2_wk)

        contact_hour_1to6_rece_min_tot_2_wk_24h_perc = perc(contact_hour_1to6_rece_min_tot_2_wk, contact_hour_0to23_rece_min_tot_2_wk)
        contact_hour_7to12_rece_min_tot_2_wk_24h_perc = perc(contact_hour_7to12_rece_min_tot_2_wk, contact_hour_0to23_rece_min_tot_2_wk)
        contact_hour_13to18_rece_min_tot_2_wk_24h_perc = perc(contact_hour_13to18_rece_min_tot_2_wk, contact_hour_0to23_rece_min_tot_2_wk)
        contact_hour_19to0_rece_min_tot_2_wk_24h_perc = perc(contact_hour_19to0_rece_min_tot_2_wk, contact_hour_0to23_rece_min_tot_2_wk)

        contact_hour_1to8_rece_cnt_24h_perc = perc(contact_hour_1to8_rece_cnt, contact_hour_0to23_rece_cnt)
        contact_hour_9to16_rece_cnt_24h_perc = perc(contact_hour_9to16_rece_cnt, contact_hour_0to23_rece_cnt)
        contact_hour_17to0_rece_cnt_24h_perc = perc(contact_hour_17to0_rece_cnt, contact_hour_0to23_rece_cnt)

        contact_hour_1to8_rece_min_tot_24h_perc = perc(contact_hour_1to8_rece_min_tot, contact_hour_0to23_rece_min_tot)
        contact_hour_9to16_rece_min_tot_24h_perc = perc(contact_hour_9to16_rece_min_tot, contact_hour_0to23_rece_min_tot)
        contact_hour_17to0_rece_min_tot_24h_perc = perc(contact_hour_17to0_rece_min_tot, contact_hour_0to23_rece_min_tot)

        contact_hour_1to8_rece_cnt_6_mon_24h_perc = perc(contact_hour_1to8_rece_cnt_6_mon, contact_hour_0to23_rece_cnt_6_mon)
        contact_hour_9to16_rece_cnt_6_mon_24h_perc = perc(contact_hour_9to16_rece_cnt_6_mon, contact_hour_0to23_rece_cnt_6_mon)
        contact_hour_17to0_rece_cnt_6_mon_24h_perc = perc(contact_hour_17to0_rece_cnt_6_mon, contact_hour_0to23_rece_cnt_6_mon)

        contact_hour_1to8_rece_min_tot_6_mon_24h_perc = perc(contact_hour_1to8_rece_min_tot_6_mon, contact_hour_0to23_rece_min_tot_6_mon)
        contact_hour_9to16_rece_min_tot_6_mon_24h_perc = perc(contact_hour_9to16_rece_min_tot_6_mon, contact_hour_0to23_rece_min_tot_6_mon)
        contact_hour_17to0_rece_min_tot_6_mon_24h_perc = perc(contact_hour_17to0_rece_min_tot_6_mon, contact_hour_0to23_rece_min_tot_6_mon)

        contact_hour_1to8_rece_cnt_3_mon_24h_perc = perc(contact_hour_1to8_rece_cnt_3_mon, contact_hour_0to23_rece_cnt_3_mon)
        contact_hour_9to16_rece_cnt_3_mon_24h_perc = perc(contact_hour_9to16_rece_cnt_3_mon, contact_hour_0to23_rece_cnt_3_mon)
        contact_hour_17to0_rece_cnt_3_mon_24h_perc = perc(contact_hour_17to0_rece_cnt_3_mon, contact_hour_0to23_rece_cnt_3_mon)

        contact_hour_1to8_rece_min_tot_3_mon_24h_perc = perc(contact_hour_1to8_rece_min_tot_3_mon, contact_hour_0to23_rece_min_tot_3_mon)
        contact_hour_9to16_rece_min_tot_3_mon_24h_perc = perc(contact_hour_9to16_rece_min_tot_3_mon, contact_hour_0to23_rece_min_tot_3_mon)
        contact_hour_17to0_rece_min_tot_3_mon_24h_perc = perc(contact_hour_17to0_rece_min_tot_3_mon, contact_hour_0to23_rece_min_tot_3_mon)

        contact_hour_1to8_rece_cnt_2_mon_24h_perc = perc(contact_hour_1to8_rece_cnt_2_mon, contact_hour_0to23_rece_cnt_2_mon)
        contact_hour_9to16_rece_cnt_2_mon_24h_perc = perc(contact_hour_9to16_rece_cnt_2_mon, contact_hour_0to23_rece_cnt_2_mon)
        contact_hour_17to0_rece_cnt_2_mon_24h_perc = perc(contact_hour_17to0_rece_cnt_2_mon, contact_hour_0to23_rece_cnt_2_mon)

        contact_hour_1to8_rece_min_tot_2_mon_24h_perc = perc(contact_hour_1to8_rece_min_tot_2_mon, contact_hour_0to23_rece_min_tot_2_mon)
        contact_hour_9to16_rece_min_tot_2_mon_24h_perc = perc(contact_hour_9to16_rece_min_tot_2_mon, contact_hour_0to23_rece_min_tot_2_mon)
        contact_hour_17to0_rece_min_tot_2_mon_24h_perc = perc(contact_hour_17to0_rece_min_tot_2_mon, contact_hour_0to23_rece_min_tot_2_mon)

        contact_hour_1to8_rece_cnt_1_mon_24h_perc = perc(contact_hour_1to8_rece_cnt_1_mon, contact_hour_0to23_rece_cnt_1_mon)
        contact_hour_9to16_rece_cnt_1_mon_24h_perc = perc(contact_hour_9to16_rece_cnt_1_mon, contact_hour_0to23_rece_cnt_1_mon)
        contact_hour_17to0_rece_cnt_1_mon_24h_perc = perc(contact_hour_17to0_rece_cnt_1_mon, contact_hour_0to23_rece_cnt_1_mon)

        contact_hour_1to8_rece_min_tot_1_mon_24h_perc = perc(contact_hour_1to8_rece_min_tot_1_mon, contact_hour_0to23_rece_min_tot_1_mon)
        contact_hour_9to16_rece_min_tot_1_mon_24h_perc = perc(contact_hour_9to16_rece_min_tot_1_mon, contact_hour_0to23_rece_min_tot_1_mon)
        contact_hour_17to0_rece_min_tot_1_mon_24h_perc = perc(contact_hour_17to0_rece_min_tot_1_mon, contact_hour_0to23_rece_min_tot_1_mon)

        contact_hour_1to8_rece_cnt_2_wk_24h_perc = perc(contact_hour_1to8_rece_cnt_2_wk, contact_hour_0to23_rece_cnt_2_wk)
        contact_hour_9to16_rece_cnt_2_wk_24h_perc = perc(contact_hour_9to16_rece_cnt_2_wk, contact_hour_0to23_rece_cnt_2_wk)
        contact_hour_17to0_rece_cnt_2_wk_24h_perc = perc(contact_hour_17to0_rece_cnt_2_wk, contact_hour_0to23_rece_cnt_2_wk)

        contact_hour_1to8_rece_min_tot_2_wk_24h_perc = perc(contact_hour_1to8_rece_min_tot_2_wk, contact_hour_0to23_rece_min_tot_2_wk)
        contact_hour_9to16_rece_min_tot_2_wk_24h_perc = perc(contact_hour_9to16_rece_min_tot_2_wk, contact_hour_0to23_rece_min_tot_2_wk)
        contact_hour_17to0_rece_min_tot_2_wk_24h_perc = perc(contact_hour_17to0_rece_min_tot_2_wk, contact_hour_0to23_rece_min_tot_2_wk)

        contact_hour_9to20_rece_cnt_24_hour_perc = perc(contact_hour_9to20_rece_cnt, contact_hour_0to23_rece_cnt)
        contact_hour_21to8_rece_cnt_24_hour_perc = perc(contact_hour_21to8_rece_cnt, contact_hour_0to23_rece_cnt)

        contact_hour_9to20_rece_min_tot_24_hour_perc = perc(contact_hour_9to20_rece_min_tot, contact_hour_0to23_rece_min_tot)
        contact_hour_21to8_rece_min_tot_24_hour_perc = perc(contact_hour_21to8_rece_min_tot, contact_hour_0to23_rece_min_tot)

        contact_hour_9to20_rece_cnt_6_mon_24_hour_perc = perc(contact_hour_9to20_rece_cnt_6_mon, contact_hour_0to23_rece_cnt_6_mon)
        contact_hour_21to8_rece_cnt_6_mon_24_hour_perc = perc(contact_hour_21to8_rece_cnt_6_mon, contact_hour_0to23_rece_cnt_6_mon)

        contact_hour_9to20_rece_min_tot_6_mon_24_hour_perc = perc(contact_hour_9to20_rece_min_tot_6_mon, contact_hour_0to23_rece_min_tot_6_mon)
        contact_hour_21to8_rece_min_tot_6_mon_24_hour_perc = perc(contact_hour_21to8_rece_min_tot_6_mon, contact_hour_0to23_rece_min_tot_6_mon)

        contact_hour_9to20_rece_cnt_3_mon_24_hour_perc = perc(contact_hour_9to20_rece_cnt_3_mon, contact_hour_0to23_rece_cnt_3_mon)
        contact_hour_21to8_rece_cnt_3_mon_24_hour_perc = perc(contact_hour_21to8_rece_cnt_3_mon, contact_hour_0to23_rece_cnt_3_mon)

        contact_hour_9to20_rece_min_tot_3_mon_24_hour_perc = perc(contact_hour_9to20_rece_min_tot_3_mon, contact_hour_0to23_rece_min_tot_3_mon)
        contact_hour_21to8_rece_min_tot_3_mon_24_hour_perc = perc(contact_hour_21to8_rece_min_tot_3_mon, contact_hour_0to23_rece_min_tot_3_mon)

        contact_hour_9to20_rece_cnt_2_mon_24_hour_perc = perc(contact_hour_9to20_rece_cnt_2_mon, contact_hour_0to23_rece_cnt_2_mon)
        contact_hour_21to8_rece_cnt_2_mon_24_hour_perc = perc(contact_hour_21to8_rece_cnt_2_mon, contact_hour_0to23_rece_cnt_2_mon)

        contact_hour_9to20_rece_min_tot_2_mon_24_hour_perc = perc(contact_hour_9to20_rece_min_tot_2_mon, contact_hour_0to23_rece_min_tot_2_mon)
        contact_hour_21to8_rece_min_tot_2_mon_24_hour_perc = perc(contact_hour_21to8_rece_min_tot_2_mon, contact_hour_0to23_rece_min_tot_2_mon)

        contact_hour_9to20_rece_cnt_2_wk_24_hour_perc = perc(contact_hour_9to20_rece_cnt_2_wk, contact_hour_0to23_rece_cnt_2_wk)
        contact_hour_21to8_rece_cnt_2_wk_24_hour_perc = perc(contact_hour_21to8_rece_cnt_2_wk, contact_hour_0to23_rece_cnt_2_wk)

        contact_hour_9to20_rece_min_tot_2_wk_24_hour_perc = perc(contact_hour_9to20_rece_min_tot_2_wk, contact_hour_0to23_rece_min_tot_2_wk)
        contact_hour_21to8_rece_min_tot_2_wk_24_hour_perc = perc(contact_hour_21to8_rece_min_tot_2_wk, contact_hour_0to23_rece_min_tot_2_wk)

        # perc divided by 6 mon record
        contact_hour_1to6_cnt_3_mon_perc = perc(contact_hour_1to6_cnt_3_mon, contact_hour_1to6_cnt_6_mon)
        contact_hour_7to12_cnt_3_mon_perc = perc(contact_hour_7to12_cnt_3_mon, contact_hour_7to12_cnt_6_mon)
        contact_hour_13to18_cnt_3_mon_perc = perc(contact_hour_13to18_cnt_3_mon, contact_hour_13to18_cnt_6_mon)
        contact_hour_19to0_cnt_3_mon_perc = perc(contact_hour_19to0_cnt_3_mon, contact_hour_19to0_cnt_6_mon)

        contact_hour_1to6_min_tot_3_mon_perc = perc(contact_hour_1to6_min_tot_3_mon, contact_hour_1to6_min_tot_6_mon)
        contact_hour_7to12_min_tot_3_mon_perc = perc(contact_hour_7to12_min_tot_3_mon, contact_hour_7to12_min_tot_6_mon)
        contact_hour_13to18_min_tot_3_mon_perc = perc(contact_hour_13to18_min_tot_3_mon, contact_hour_13to18_min_tot_6_mon)
        contact_hour_19to0_min_tot_3_mon_perc = perc(contact_hour_19to0_min_tot_3_mon, contact_hour_19to0_min_tot_6_mon)

        contact_hour_1to6_cnt_2_mon_perc = perc(contact_hour_1to6_cnt_2_mon, contact_hour_1to6_cnt_6_mon)
        contact_hour_7to12_cnt_2_mon_perc = perc(contact_hour_7to12_cnt_2_mon, contact_hour_7to12_cnt_6_mon)
        contact_hour_13to18_cnt_2_mon_perc = perc(contact_hour_13to18_cnt_2_mon, contact_hour_13to18_cnt_6_mon)
        contact_hour_19to0_cnt_2_mon_perc = perc(contact_hour_19to0_cnt_2_mon, contact_hour_19to0_cnt_6_mon)

        contact_hour_1to6_min_tot_2_mon_perc = perc(contact_hour_1to6_min_tot_2_mon, contact_hour_1to6_min_tot_6_mon)
        contact_hour_7to12_min_tot_2_mon_perc = perc(contact_hour_7to12_min_tot_2_mon, contact_hour_7to12_min_tot_6_mon)
        contact_hour_13to18_min_tot_2_mon_perc = perc(contact_hour_13to18_min_tot_2_mon, contact_hour_13to18_min_tot_6_mon)
        contact_hour_19to0_min_tot_2_mon_perc = perc(contact_hour_19to0_min_tot_2_mon, contact_hour_19to0_min_tot_6_mon)

        contact_hour_1to6_cnt_1_mon_perc = perc(contact_hour_1to6_cnt_1_mon, contact_hour_1to6_cnt_6_mon)
        contact_hour_7to12_cnt_1_mon_perc = perc(contact_hour_7to12_cnt_1_mon, contact_hour_7to12_cnt_6_mon)
        contact_hour_13to18_cnt_1_mon_perc = perc(contact_hour_13to18_cnt_1_mon, contact_hour_13to18_cnt_6_mon)
        contact_hour_19to0_cnt_1_mon_perc = perc(contact_hour_19to0_cnt_1_mon, contact_hour_19to0_cnt_6_mon)

        contact_hour_1to6_min_tot_1_mon_perc = perc(contact_hour_1to6_min_tot_1_mon, contact_hour_1to6_min_tot_6_mon)
        contact_hour_7to12_min_tot_1_mon_perc = perc(contact_hour_7to12_min_tot_1_mon, contact_hour_7to12_min_tot_6_mon)
        contact_hour_13to18_min_tot_1_mon_perc = perc(contact_hour_13to18_min_tot_1_mon, contact_hour_13to18_min_tot_6_mon)
        contact_hour_19to0_min_tot_1_mon_perc = perc(contact_hour_19to0_min_tot_1_mon, contact_hour_19to0_min_tot_6_mon)

        contact_hour_1to6_cnt_2_wk_perc = perc(contact_hour_1to6_cnt_2_wk, contact_hour_1to6_cnt_6_mon)
        contact_hour_7to12_cnt_2_wk_perc = perc(contact_hour_7to12_cnt_2_wk, contact_hour_7to12_cnt_6_mon)
        contact_hour_13to18_cnt_2_wk_perc = perc(contact_hour_13to18_cnt_2_wk, contact_hour_13to18_cnt_6_mon)
        contact_hour_19to0_cnt_2_wk_perc = perc(contact_hour_19to0_cnt_2_wk, contact_hour_19to0_cnt_6_mon)

        contact_hour_1to6_min_tot_2_wk_perc = perc(contact_hour_1to6_min_tot_2_wk, contact_hour_1to6_min_tot_6_mon)
        contact_hour_7to12_min_tot_2_wk_perc = perc(contact_hour_7to12_min_tot_2_wk, contact_hour_7to12_min_tot_6_mon)
        contact_hour_13to18_min_tot_2_wk_perc = perc(contact_hour_13to18_min_tot_2_wk, contact_hour_13to18_min_tot_6_mon)
        contact_hour_19to0_min_tot_2_wk_perc = perc(contact_hour_19to0_min_tot_2_wk, contact_hour_19to0_min_tot_6_mon)

        contact_hour_1to8_cnt_3_mon_perc = perc(contact_hour_1to8_cnt_3_mon, contact_hour_1to8_cnt_6_mon)
        contact_hour_9to16_cnt_3_mon_perc = perc(contact_hour_9to16_cnt_3_mon, contact_hour_9to16_cnt_6_mon)
        contact_hour_17to0_cnt_3_mon_perc = perc(contact_hour_17to0_cnt_3_mon, contact_hour_17to0_cnt_6_mon)

        contact_hour_1to8_min_tot_3_mon_perc = perc(contact_hour_1to8_min_tot_3_mon, contact_hour_1to8_min_tot_6_mon)
        contact_hour_9to16_min_tot_3_mon_perc = perc(contact_hour_9to16_min_tot_3_mon, contact_hour_9to16_min_tot_6_mon)
        contact_hour_17to0_min_tot_3_mon_perc = perc(contact_hour_17to0_min_tot_3_mon, contact_hour_17to0_min_tot_6_mon)

        contact_hour_1to8_cnt_2_mon_perc = perc(contact_hour_1to8_cnt_2_mon, contact_hour_1to8_cnt_6_mon)
        contact_hour_9to16_cnt_2_mon_perc = perc(contact_hour_9to16_cnt_2_mon, contact_hour_9to16_cnt_6_mon)
        contact_hour_17to0_cnt_2_mon_perc = perc(contact_hour_17to0_cnt_2_mon, contact_hour_17to0_cnt_6_mon)

        contact_hour_1to8_min_tot_2_mon_perc = perc(contact_hour_1to8_min_tot_2_mon, contact_hour_1to8_min_tot_6_mon)
        contact_hour_9to16_min_tot_2_mon_perc = perc(contact_hour_9to16_min_tot_2_mon, contact_hour_9to16_min_tot_6_mon)
        contact_hour_17to0_min_tot_2_mon_perc = perc(contact_hour_17to0_min_tot_2_mon, contact_hour_17to0_min_tot_6_mon)

        contact_hour_1to8_cnt_1_mon_perc = perc(contact_hour_1to8_cnt_1_mon, contact_hour_1to8_cnt_6_mon)
        contact_hour_9to16_cnt_1_mon_perc = perc(contact_hour_9to16_cnt_1_mon, contact_hour_9to16_cnt_6_mon)
        contact_hour_17to0_cnt_1_mon_perc = perc(contact_hour_17to0_cnt_1_mon, contact_hour_17to0_cnt_6_mon)

        contact_hour_1to8_min_tot_1_mon_perc = perc(contact_hour_1to8_min_tot_1_mon, contact_hour_1to8_min_tot_6_mon)
        contact_hour_9to16_min_tot_1_mon_perc = perc(contact_hour_9to16_min_tot_1_mon, contact_hour_9to16_min_tot_6_mon)
        contact_hour_17to0_min_tot_1_mon_perc = perc(contact_hour_17to0_min_tot_1_mon, contact_hour_17to0_min_tot_6_mon)

        contact_hour_1to8_cnt_2_wk_perc = perc(contact_hour_1to8_cnt_2_wk, contact_hour_1to8_cnt_6_mon)
        contact_hour_9to16_cnt_2_wk_perc = perc(contact_hour_9to16_cnt_2_wk, contact_hour_9to16_cnt_6_mon)
        contact_hour_17to0_cnt_2_wk_perc = perc(contact_hour_17to0_cnt_2_wk, contact_hour_17to0_cnt_6_mon)

        contact_hour_1to8_min_tot_2_wk_perc = perc(contact_hour_1to8_min_tot_2_wk, contact_hour_1to8_min_tot_6_mon)
        contact_hour_9to16_min_tot_2_wk_perc = perc(contact_hour_9to16_min_tot_2_wk, contact_hour_9to16_min_tot_6_mon)
        contact_hour_17to0_min_tot_2_wk_perc = perc(contact_hour_17to0_min_tot_2_wk, contact_hour_17to0_min_tot_6_mon)

        contact_hour_9to20_cnt_3_mon_perc = perc(contact_hour_9to20_cnt_3_mon, contact_hour_9to20_cnt_6_mon)
        contact_hour_21to8_cnt_3_mon_perc = perc(contact_hour_21to8_cnt_3_mon, contact_hour_21to8_cnt_6_mon)

        contact_hour_9to20_min_tot_3_mon_perc = perc(contact_hour_9to20_min_tot_3_mon, contact_hour_9to20_min_tot_6_mon)
        contact_hour_21to8_min_tot_3_mon_perc = perc(contact_hour_21to8_min_tot_3_mon, contact_hour_21to8_min_tot_6_mon)

        contact_hour_9to20_cnt_2_mon_perc = perc(contact_hour_9to20_cnt_2_mon, contact_hour_9to20_cnt_6_mon)
        contact_hour_21to8_cnt_2_mon_perc = perc(contact_hour_21to8_cnt_2_mon, contact_hour_21to8_cnt_6_mon)

        contact_hour_9to20_min_tot_2_mon_perc = perc(contact_hour_9to20_min_tot_2_mon, contact_hour_9to20_min_tot_6_mon)
        contact_hour_21to8_min_tot_2_mon_perc = perc(contact_hour_21to8_min_tot_2_mon, contact_hour_21to8_min_tot_6_mon)

        contact_hour_9to20_cnt_1_mon_perc = perc(contact_hour_9to20_cnt_1_mon, contact_hour_9to20_cnt_6_mon)
        contact_hour_21to8_cnt_1_mon_perc = perc(contact_hour_21to8_cnt_1_mon, contact_hour_21to8_cnt_6_mon)

        contact_hour_9to20_min_tot_1_mon_perc = perc(contact_hour_9to20_min_tot_1_mon, contact_hour_9to20_min_tot_6_mon)
        contact_hour_21to8_min_tot_1_mon_perc = perc(contact_hour_21to8_min_tot_1_mon, contact_hour_21to8_min_tot_6_mon)

        contact_hour_9to20_cnt_2_wk_perc = perc(contact_hour_9to20_cnt_2_wk, contact_hour_9to20_cnt_6_mon)
        contact_hour_21to8_cnt_2_wk_perc = perc(contact_hour_21to8_cnt_2_wk, contact_hour_21to8_cnt_6_mon)

        contact_hour_9to20_min_tot_2_wk_perc = perc(contact_hour_9to20_min_tot_2_wk, contact_hour_9to20_min_tot_6_mon)
        contact_hour_21to8_min_tot_2_wk_perc = perc(contact_hour_21to8_min_tot_2_wk, contact_hour_21to8_min_tot_6_mon)

        contact_hour_1to6_call_cnt_3_mon_perc = perc(contact_hour_1to6_call_cnt_3_mon, contact_hour_1to6_call_cnt_6_mon)
        contact_hour_7to12_call_cnt_3_mon_perc = perc(contact_hour_7to12_call_cnt_3_mon, contact_hour_7to12_call_cnt_6_mon)
        contact_hour_13to18_call_cnt_3_mon_perc = perc(contact_hour_13to18_call_cnt_3_mon, contact_hour_13to18_call_cnt_6_mon)
        contact_hour_19to0_call_cnt_3_mon_perc = perc(contact_hour_19to0_call_cnt_3_mon, contact_hour_19to0_call_cnt_6_mon)

        contact_hour_1to6_call_min_tot_3_mon_perc = perc(contact_hour_1to6_call_min_tot_3_mon, contact_hour_1to6_call_min_tot_6_mon)
        contact_hour_7to12_call_min_tot_3_mon_perc = perc(contact_hour_7to12_call_min_tot_3_mon, contact_hour_7to12_call_min_tot_6_mon)
        contact_hour_13to18_call_min_tot_3_mon_perc = perc(contact_hour_13to18_call_min_tot_3_mon, contact_hour_13to18_call_min_tot_6_mon)
        contact_hour_19to0_call_min_tot_3_mon_perc = perc(contact_hour_19to0_call_min_tot_3_mon, contact_hour_19to0_call_min_tot_6_mon)

        contact_hour_1to6_call_cnt_2_mon_perc = perc(contact_hour_1to6_call_cnt_2_mon, contact_hour_1to6_call_cnt_6_mon)
        contact_hour_7to12_call_cnt_2_mon_perc = perc(contact_hour_7to12_call_cnt_2_mon, contact_hour_7to12_call_cnt_6_mon)
        contact_hour_13to18_call_cnt_2_mon_perc = perc(contact_hour_13to18_call_cnt_2_mon, contact_hour_13to18_call_cnt_6_mon)
        contact_hour_19to0_call_cnt_2_mon_perc = perc(contact_hour_19to0_call_cnt_2_mon, contact_hour_19to0_call_cnt_6_mon)

        contact_hour_1to6_call_min_tot_2_mon_perc = perc(contact_hour_1to6_call_min_tot_2_mon, contact_hour_1to6_call_min_tot_6_mon)
        contact_hour_7to12_call_min_tot_2_mon_perc = perc(contact_hour_7to12_call_min_tot_2_mon, contact_hour_7to12_call_min_tot_6_mon)
        contact_hour_13to18_call_min_tot_2_mon_perc = perc(contact_hour_13to18_call_min_tot_2_mon, contact_hour_13to18_call_min_tot_6_mon)
        contact_hour_19to0_call_min_tot_2_mon_perc = perc(contact_hour_19to0_call_min_tot_2_mon, contact_hour_19to0_call_min_tot_6_mon)

        contact_hour_1to6_call_cnt_1_mon_perc = perc(contact_hour_1to6_call_cnt_1_mon, contact_hour_1to6_call_cnt_6_mon)
        contact_hour_7to12_call_cnt_1_mon_perc = perc(contact_hour_7to12_call_cnt_1_mon, contact_hour_7to12_call_cnt_6_mon)
        contact_hour_13to18_call_cnt_1_mon_perc = perc(contact_hour_13to18_call_cnt_1_mon, contact_hour_13to18_call_cnt_6_mon)
        contact_hour_19to0_call_cnt_1_mon_perc = perc(contact_hour_19to0_call_cnt_1_mon, contact_hour_19to0_call_cnt_6_mon)

        contact_hour_1to6_call_min_tot_1_mon_perc = perc(contact_hour_1to6_call_min_tot_1_mon, contact_hour_1to6_call_min_tot_6_mon)
        contact_hour_7to12_call_min_tot_1_mon_perc = perc(contact_hour_7to12_call_min_tot_1_mon, contact_hour_7to12_call_min_tot_6_mon)
        contact_hour_13to18_call_min_tot_1_mon_perc = perc(contact_hour_13to18_call_min_tot_1_mon, contact_hour_13to18_call_min_tot_6_mon)
        contact_hour_19to0_call_min_tot_1_mon_perc = perc(contact_hour_19to0_call_min_tot_1_mon, contact_hour_19to0_call_min_tot_6_mon)

        contact_hour_1to6_call_cnt_2_wk_perc = perc(contact_hour_1to6_call_cnt_2_wk, contact_hour_1to6_call_cnt_6_mon)
        contact_hour_7to12_call_cnt_2_wk_perc = perc(contact_hour_7to12_call_cnt_2_wk, contact_hour_7to12_call_cnt_6_mon)
        contact_hour_13to18_call_cnt_2_wk_perc = perc(contact_hour_13to18_call_cnt_2_wk, contact_hour_13to18_call_cnt_6_mon)
        contact_hour_19to0_call_cnt_2_wk_perc = perc(contact_hour_19to0_call_cnt_2_wk, contact_hour_19to0_call_cnt_6_mon)

        contact_hour_1to6_call_min_tot_2_wk_perc = perc(contact_hour_1to6_call_min_tot_2_wk, contact_hour_1to6_call_min_tot_6_mon)
        contact_hour_7to12_call_min_tot_2_wk_perc = perc(contact_hour_7to12_call_min_tot_2_wk, contact_hour_7to12_call_min_tot_6_mon)
        contact_hour_13to18_call_min_tot_2_wk_perc = perc(contact_hour_13to18_call_min_tot_2_wk, contact_hour_13to18_call_min_tot_6_mon)
        contact_hour_19to0_call_min_tot_2_wk_perc = perc(contact_hour_19to0_call_min_tot_2_wk, contact_hour_19to0_call_min_tot_6_mon)

        contact_hour_1to8_call_cnt_3_mon_perc = perc(contact_hour_1to8_call_cnt_3_mon, contact_hour_1to8_call_cnt_6_mon)
        contact_hour_9to16_call_cnt_3_mon_perc = perc(contact_hour_9to16_call_cnt_3_mon, contact_hour_9to16_call_cnt_6_mon)
        contact_hour_17to0_call_cnt_3_mon_perc = perc(contact_hour_17to0_call_cnt_3_mon, contact_hour_17to0_call_cnt_6_mon)

        contact_hour_1to8_call_min_tot_3_mon_perc = perc(contact_hour_1to8_call_min_tot_3_mon, contact_hour_1to8_call_min_tot_6_mon)
        contact_hour_9to16_call_min_tot_3_mon_perc = perc(contact_hour_9to16_call_min_tot_3_mon, contact_hour_9to16_call_min_tot_6_mon)
        contact_hour_17to0_call_min_tot_3_mon_perc = perc(contact_hour_17to0_call_min_tot_3_mon, contact_hour_17to0_call_min_tot_6_mon)

        contact_hour_1to8_call_cnt_2_mon_perc = perc(contact_hour_1to8_call_cnt_2_mon, contact_hour_1to8_call_cnt_6_mon)
        contact_hour_9to16_call_cnt_2_mon_perc = perc(contact_hour_9to16_call_cnt_2_mon, contact_hour_9to16_call_cnt_6_mon)
        contact_hour_17to0_call_cnt_2_mon_perc = perc(contact_hour_17to0_call_cnt_2_mon, contact_hour_17to0_call_cnt_6_mon)

        contact_hour_1to8_call_min_tot_2_mon_perc = perc(contact_hour_1to8_call_min_tot_2_mon, contact_hour_1to8_call_min_tot_6_mon)
        contact_hour_9to16_call_min_tot_2_mon_perc = perc(contact_hour_9to16_call_min_tot_2_mon, contact_hour_9to16_call_min_tot_6_mon)
        contact_hour_17to0_call_min_tot_2_mon_perc = perc(contact_hour_17to0_call_min_tot_2_mon, contact_hour_17to0_call_min_tot_6_mon)

        contact_hour_1to8_call_cnt_1_mon_perc = perc(contact_hour_1to8_call_cnt_1_mon, contact_hour_1to8_call_cnt_6_mon)
        contact_hour_9to16_call_cnt_1_mon_perc = perc(contact_hour_9to16_call_cnt_1_mon, contact_hour_9to16_call_cnt_6_mon)
        contact_hour_17to0_call_cnt_1_mon_perc = perc(contact_hour_17to0_call_cnt_1_mon, contact_hour_17to0_call_cnt_6_mon)

        contact_hour_1to8_call_min_tot_1_mon_perc = perc(contact_hour_1to8_call_min_tot_1_mon, contact_hour_1to8_call_min_tot_6_mon)
        contact_hour_9to16_call_min_tot_1_mon_perc = perc(contact_hour_9to16_call_min_tot_1_mon, contact_hour_9to16_call_min_tot_6_mon)
        contact_hour_17to0_call_min_tot_1_mon_perc = perc(contact_hour_17to0_call_min_tot_1_mon, contact_hour_17to0_call_min_tot_6_mon)

        contact_hour_1to8_call_cnt_2_wk_perc = perc(contact_hour_1to8_call_cnt_2_wk, contact_hour_1to8_call_cnt_6_mon)
        contact_hour_9to16_call_cnt_2_wk_perc = perc(contact_hour_9to16_call_cnt_2_wk, contact_hour_9to16_call_cnt_6_mon)
        contact_hour_17to0_call_cnt_2_wk_perc = perc(contact_hour_17to0_call_cnt_2_wk, contact_hour_17to0_call_cnt_6_mon)

        contact_hour_1to8_call_min_tot_2_wk_perc = perc(contact_hour_1to8_call_min_tot_2_wk, contact_hour_1to8_call_min_tot_6_mon)
        contact_hour_9to16_call_min_tot_2_wk_perc = perc(contact_hour_9to16_call_min_tot_2_wk, contact_hour_9to16_call_min_tot_6_mon)
        contact_hour_17to0_call_min_tot_2_wk_perc = perc(contact_hour_17to0_call_min_tot_2_wk, contact_hour_17to0_call_min_tot_6_mon)

        contact_hour_9to20_call_cnt_3_mon_perc = perc(contact_hour_9to20_call_cnt_3_mon, contact_hour_9to20_call_cnt_6_mon)
        contact_hour_21to8_call_cnt_3_mon_perc = perc(contact_hour_21to8_call_cnt_3_mon, contact_hour_21to8_call_cnt_6_mon)

        contact_hour_9to20_call_min_tot_3_mon_perc = perc(contact_hour_9to20_call_min_tot_3_mon, contact_hour_9to20_call_min_tot_6_mon)
        contact_hour_21to8_call_min_tot_3_mon_perc = perc(contact_hour_21to8_call_min_tot_3_mon, contact_hour_21to8_call_min_tot_6_mon)

        contact_hour_9to20_call_cnt_2_mon_perc = perc(contact_hour_9to20_call_cnt_2_mon, contact_hour_9to20_call_cnt_6_mon)
        contact_hour_21to8_call_cnt_2_mon_perc = perc(contact_hour_21to8_call_cnt_2_mon, contact_hour_21to8_call_cnt_6_mon)

        contact_hour_9to20_call_min_tot_2_mon_perc = perc(contact_hour_9to20_call_min_tot_2_mon, contact_hour_9to20_call_min_tot_6_mon)
        contact_hour_21to8_call_min_tot_2_mon_perc = perc(contact_hour_21to8_call_min_tot_2_mon, contact_hour_21to8_call_min_tot_6_mon)

        contact_hour_9to20_call_cnt_1_mon_perc = perc(contact_hour_9to20_call_cnt_1_mon, contact_hour_9to20_call_cnt_6_mon)
        contact_hour_21to8_call_cnt_1_mon_perc = perc(contact_hour_21to8_call_cnt_1_mon, contact_hour_21to8_call_cnt_6_mon)

        contact_hour_9to20_call_min_tot_1_mon_perc = perc(contact_hour_9to20_call_min_tot_1_mon, contact_hour_9to20_call_min_tot_6_mon)
        contact_hour_21to8_call_min_tot_1_mon_perc = perc(contact_hour_21to8_call_min_tot_1_mon, contact_hour_21to8_call_min_tot_6_mon)

        contact_hour_9to20_call_cnt_2_wk_perc = perc(contact_hour_9to20_call_cnt_2_wk, contact_hour_9to20_call_cnt_6_mon)
        contact_hour_21to8_call_cnt_2_wk_perc = perc(contact_hour_21to8_call_cnt_2_wk, contact_hour_21to8_call_cnt_6_mon)

        contact_hour_9to20_call_min_tot_2_wk_perc = perc(contact_hour_9to20_call_min_tot_2_wk, contact_hour_9to20_call_min_tot_6_mon)
        contact_hour_21to8_call_min_tot_2_wk_perc = perc(contact_hour_21to8_call_min_tot_2_wk, contact_hour_21to8_call_min_tot_6_mon)

        contact_hour_1to6_rece_cnt_3_mon_perc = perc(contact_hour_1to6_rece_cnt_3_mon, contact_hour_1to6_rece_cnt_6_mon)
        contact_hour_7to12_rece_cnt_3_mon_perc = perc(contact_hour_7to12_rece_cnt_3_mon, contact_hour_7to12_rece_cnt_6_mon)
        contact_hour_13to18_rece_cnt_3_mon_perc = perc(contact_hour_13to18_rece_cnt_3_mon, contact_hour_13to18_rece_cnt_6_mon)
        contact_hour_19to0_rece_cnt_3_mon_perc = perc(contact_hour_19to0_rece_cnt_3_mon, contact_hour_19to0_rece_cnt_6_mon)

        contact_hour_1to6_rece_min_tot_3_mon_perc = perc(contact_hour_1to6_rece_min_tot_3_mon, contact_hour_1to6_rece_min_tot_6_mon)
        contact_hour_7to12_rece_min_tot_3_mon_perc = perc(contact_hour_7to12_rece_min_tot_3_mon, contact_hour_7to12_rece_min_tot_6_mon)
        contact_hour_13to18_rece_min_tot_3_mon_perc = perc(contact_hour_13to18_rece_min_tot_3_mon, contact_hour_13to18_rece_min_tot_6_mon)
        contact_hour_19to0_rece_min_tot_3_mon_perc = perc(contact_hour_19to0_rece_min_tot_3_mon, contact_hour_19to0_rece_min_tot_6_mon)

        contact_hour_1to6_rece_cnt_2_mon_perc = perc(contact_hour_1to6_rece_cnt_2_mon, contact_hour_1to6_rece_cnt_6_mon)
        contact_hour_7to12_rece_cnt_2_mon_perc = perc(contact_hour_7to12_rece_cnt_2_mon, contact_hour_7to12_rece_cnt_6_mon)
        contact_hour_13to18_rece_cnt_2_mon_perc = perc(contact_hour_13to18_rece_cnt_2_mon, contact_hour_13to18_rece_cnt_6_mon)
        contact_hour_19to0_rece_cnt_2_mon_perc = perc(contact_hour_19to0_rece_cnt_2_mon, contact_hour_19to0_rece_cnt_6_mon)

        contact_hour_1to6_rece_min_tot_2_mon_perc = perc(contact_hour_1to6_rece_min_tot_2_mon, contact_hour_1to6_rece_min_tot_6_mon)
        contact_hour_7to12_rece_min_tot_2_mon_perc = perc(contact_hour_7to12_rece_min_tot_2_mon, contact_hour_7to12_rece_min_tot_6_mon)
        contact_hour_13to18_rece_min_tot_2_mon_perc = perc(contact_hour_13to18_rece_min_tot_2_mon, contact_hour_13to18_rece_min_tot_6_mon)
        contact_hour_19to0_rece_min_tot_2_mon_perc = perc(contact_hour_19to0_rece_min_tot_2_mon, contact_hour_19to0_rece_min_tot_6_mon)

        contact_hour_1to6_rece_cnt_1_mon_perc = perc(contact_hour_1to6_rece_cnt_1_mon, contact_hour_1to6_rece_cnt_6_mon)
        contact_hour_7to12_rece_cnt_1_mon_perc = perc(contact_hour_7to12_rece_cnt_1_mon, contact_hour_7to12_rece_cnt_6_mon)
        contact_hour_13to18_rece_cnt_1_mon_perc = perc(contact_hour_13to18_rece_cnt_1_mon, contact_hour_13to18_rece_cnt_6_mon)
        contact_hour_19to0_rece_cnt_1_mon_perc = perc(contact_hour_19to0_rece_cnt_1_mon, contact_hour_19to0_rece_cnt_6_mon)

        contact_hour_1to6_rece_min_tot_1_mon_perc = perc(contact_hour_1to6_rece_min_tot_1_mon, contact_hour_1to6_rece_min_tot_6_mon)
        contact_hour_7to12_rece_min_tot_1_mon_perc = perc(contact_hour_7to12_rece_min_tot_1_mon, contact_hour_7to12_rece_min_tot_6_mon)
        contact_hour_13to18_rece_min_tot_1_mon_perc = perc(contact_hour_13to18_rece_min_tot_1_mon, contact_hour_13to18_rece_min_tot_6_mon)
        contact_hour_19to0_rece_min_tot_1_mon_perc = perc(contact_hour_19to0_rece_min_tot_1_mon, contact_hour_19to0_rece_min_tot_6_mon)

        contact_hour_1to6_rece_cnt_2_wk_perc = perc(contact_hour_1to6_rece_cnt_2_wk, contact_hour_1to6_rece_cnt_6_mon)
        contact_hour_7to12_rece_cnt_2_wk_perc = perc(contact_hour_7to12_rece_cnt_2_wk, contact_hour_7to12_rece_cnt_6_mon)
        contact_hour_13to18_rece_cnt_2_wk_perc = perc(contact_hour_13to18_rece_cnt_2_wk, contact_hour_13to18_rece_cnt_6_mon)
        contact_hour_19to0_rece_cnt_2_wk_perc = perc(contact_hour_19to0_rece_cnt_2_wk, contact_hour_19to0_rece_cnt_6_mon)

        contact_hour_1to6_rece_min_tot_2_wk_perc = perc(contact_hour_1to6_rece_min_tot_2_wk, contact_hour_1to6_rece_min_tot_6_mon)
        contact_hour_7to12_rece_min_tot_2_wk_perc = perc(contact_hour_7to12_rece_min_tot_2_wk, contact_hour_7to12_rece_min_tot_6_mon)
        contact_hour_13to18_rece_min_tot_2_wk_perc = perc(contact_hour_13to18_rece_min_tot_2_wk, contact_hour_13to18_rece_min_tot_6_mon)
        contact_hour_19to0_rece_min_tot_2_wk_perc = perc(contact_hour_19to0_rece_min_tot_2_wk, contact_hour_19to0_rece_min_tot_6_mon)

        contact_hour_1to8_rece_cnt_3_mon_perc = perc(contact_hour_1to8_rece_cnt_3_mon, contact_hour_1to8_rece_cnt_6_mon)
        contact_hour_9to16_rece_cnt_3_mon_perc = perc(contact_hour_9to16_rece_cnt_3_mon, contact_hour_9to16_rece_cnt_6_mon)
        contact_hour_17to0_rece_cnt_3_mon_perc = perc(contact_hour_17to0_rece_cnt_3_mon, contact_hour_17to0_rece_cnt_6_mon)

        contact_hour_1to8_rece_min_tot_3_mon_perc = perc(contact_hour_1to8_rece_min_tot_3_mon, contact_hour_1to8_rece_min_tot_6_mon)
        contact_hour_9to16_rece_min_tot_3_mon_perc = perc(contact_hour_9to16_rece_min_tot_3_mon, contact_hour_9to16_rece_min_tot_6_mon)
        contact_hour_17to0_rece_min_tot_3_mon_perc = perc(contact_hour_17to0_rece_min_tot_3_mon, contact_hour_17to0_rece_min_tot_6_mon)

        contact_hour_1to8_rece_cnt_2_mon_perc = perc(contact_hour_1to8_rece_cnt_2_mon, contact_hour_1to8_rece_cnt_6_mon)
        contact_hour_9to16_rece_cnt_2_mon_perc = perc(contact_hour_9to16_rece_cnt_2_mon, contact_hour_9to16_rece_cnt_6_mon)
        contact_hour_17to0_rece_cnt_2_mon_perc = perc(contact_hour_17to0_rece_cnt_2_mon, contact_hour_17to0_rece_cnt_6_mon)

        contact_hour_1to8_rece_min_tot_2_mon_perc = perc(contact_hour_1to8_rece_min_tot_2_mon, contact_hour_1to8_rece_min_tot_6_mon)
        contact_hour_9to16_rece_min_tot_2_mon_perc = perc(contact_hour_9to16_rece_min_tot_2_mon, contact_hour_9to16_rece_min_tot_6_mon)
        contact_hour_17to0_rece_min_tot_2_mon_perc = perc(contact_hour_17to0_rece_min_tot_2_mon, contact_hour_17to0_rece_min_tot_6_mon)

        contact_hour_1to8_rece_cnt_1_mon_perc = perc(contact_hour_1to8_rece_cnt_1_mon, contact_hour_1to8_rece_cnt_6_mon)
        contact_hour_9to16_rece_cnt_1_mon_perc = perc(contact_hour_9to16_rece_cnt_1_mon, contact_hour_9to16_rece_cnt_6_mon)
        contact_hour_17to0_rece_cnt_1_mon_perc = perc(contact_hour_17to0_rece_cnt_1_mon, contact_hour_17to0_rece_cnt_6_mon)

        contact_hour_1to8_rece_min_tot_1_mon_perc = perc(contact_hour_1to8_rece_min_tot_1_mon, contact_hour_1to8_rece_min_tot_6_mon)
        contact_hour_9to16_rece_min_tot_1_mon_perc = perc(contact_hour_9to16_rece_min_tot_1_mon, contact_hour_9to16_rece_min_tot_6_mon)
        contact_hour_17to0_rece_min_tot_1_mon_perc = perc(contact_hour_17to0_rece_min_tot_1_mon, contact_hour_17to0_rece_min_tot_6_mon)

        contact_hour_1to8_rece_cnt_2_wk_perc = perc(contact_hour_1to8_rece_cnt_2_wk, contact_hour_1to8_rece_cnt_6_mon)
        contact_hour_9to16_rece_cnt_2_wk_perc = perc(contact_hour_9to16_rece_cnt_2_wk, contact_hour_9to16_rece_cnt_6_mon)
        contact_hour_17to0_rece_cnt_2_wk_perc = perc(contact_hour_17to0_rece_cnt_2_wk, contact_hour_17to0_rece_cnt_6_mon)

        contact_hour_1to8_rece_min_tot_2_wk_perc = perc(contact_hour_1to8_rece_min_tot_2_wk, contact_hour_1to8_rece_min_tot_6_mon)
        contact_hour_9to16_rece_min_tot_2_wk_perc = perc(contact_hour_9to16_rece_min_tot_2_wk, contact_hour_9to16_rece_min_tot_6_mon)
        contact_hour_17to0_rece_min_tot_2_wk_perc = perc(contact_hour_17to0_rece_min_tot_2_wk, contact_hour_17to0_rece_min_tot_6_mon)

        contact_hour_9to20_rece_cnt_3_mon_perc = perc(contact_hour_9to20_rece_cnt_3_mon, contact_hour_9to20_rece_cnt_6_mon)
        contact_hour_21to8_rece_cnt_3_mon_perc = perc(contact_hour_21to8_rece_cnt_3_mon, contact_hour_21to8_rece_cnt_6_mon)

        contact_hour_9to20_rece_min_tot_3_mon_perc = perc(contact_hour_9to20_rece_min_tot_3_mon, contact_hour_9to20_rece_min_tot_6_mon)
        contact_hour_21to8_rece_min_tot_3_mon_perc = perc(contact_hour_21to8_rece_min_tot_3_mon, contact_hour_21to8_rece_min_tot_6_mon)

        contact_hour_9to20_rece_cnt_2_mon_perc = perc(contact_hour_9to20_rece_cnt_2_mon, contact_hour_9to20_rece_cnt_6_mon)
        contact_hour_21to8_rece_cnt_2_mon_perc = perc(contact_hour_21to8_rece_cnt_2_mon, contact_hour_21to8_rece_cnt_6_mon)

        contact_hour_9to20_rece_min_tot_2_mon_perc = perc(contact_hour_9to20_rece_min_tot_2_mon, contact_hour_9to20_rece_min_tot_6_mon)
        contact_hour_21to8_rece_min_tot_2_mon_perc = perc(contact_hour_21to8_rece_min_tot_2_mon, contact_hour_21to8_rece_min_tot_6_mon)

        contact_hour_9to20_rece_cnt_1_mon_perc = perc(contact_hour_9to20_rece_cnt_1_mon, contact_hour_9to20_rece_cnt_6_mon)
        contact_hour_21to8_rece_cnt_1_mon_perc = perc(contact_hour_21to8_rece_cnt_1_mon, contact_hour_21to8_rece_cnt_6_mon)

        contact_hour_9to20_rece_min_tot_1_mon_perc = perc(contact_hour_9to20_rece_min_tot_1_mon, contact_hour_9to20_rece_min_tot_6_mon)
        contact_hour_21to8_rece_min_tot_1_mon_perc = perc(contact_hour_21to8_rece_min_tot_1_mon, contact_hour_21to8_rece_min_tot_6_mon)

        contact_hour_9to20_rece_cnt_2_wk_perc = perc(contact_hour_9to20_rece_cnt_2_wk, contact_hour_9to20_rece_cnt_6_mon)
        contact_hour_21to8_rece_cnt_2_wk_perc = perc(contact_hour_21to8_rece_cnt_2_wk, contact_hour_21to8_rece_cnt_6_mon)

        contact_hour_9to20_rece_min_tot_2_wk_perc = perc(contact_hour_9to20_rece_min_tot_2_wk, contact_hour_9to20_rece_min_tot_6_mon)
        contact_hour_21to8_rece_min_tot_2_wk_perc = perc(contact_hour_21to8_rece_min_tot_2_wk, contact_hour_21to8_rece_min_tot_6_mon)

        # call cnt perc
        contact_hour_1to6_call_cnt_inout_perc = perc(contact_hour_1to6_call_cnt, contact_hour_1to6_cnt)
        contact_hour_7to12_call_cnt_inout_perc = perc(contact_hour_7to12_call_cnt, contact_hour_7to12_cnt)
        contact_hour_13to18_call_cnt_inout_perc = perc(contact_hour_13to18_call_cnt, contact_hour_13to18_cnt)
        contact_hour_19to0_call_cnt_inout_perc = perc(contact_hour_19to0_call_cnt, contact_hour_19to0_cnt)

        contact_hour_1to6_call_min_tot_inout_perc = perc(contact_hour_1to6_call_min_tot, contact_hour_1to6_min_tot)
        contact_hour_7to12_call_min_tot_inout_perc = perc(contact_hour_7to12_call_min_tot, contact_hour_7to12_min_tot)
        contact_hour_13to18_call_min_tot_inout_perc = perc(contact_hour_13to18_call_min_tot, contact_hour_13to18_min_tot)
        contact_hour_19to0_call_min_tot_inout_perc = perc(contact_hour_19to0_call_min_tot, contact_hour_19to0_min_tot)

        contact_hour_1to6_call_cnt_6_mon_inout_perc = perc(contact_hour_1to6_call_cnt_6_mon, contact_hour_1to6_cnt_6_mon)
        contact_hour_7to12_call_cnt_6_mon_inout_perc = perc(contact_hour_7to12_call_cnt_6_mon, contact_hour_7to12_cnt_6_mon)
        contact_hour_13to18_call_cnt_6_mon_inout_perc = perc(contact_hour_13to18_call_cnt_6_mon, contact_hour_13to18_cnt_6_mon)
        contact_hour_19to0_call_cnt_6_mon_inout_perc = perc(contact_hour_19to0_call_cnt_6_mon, contact_hour_19to0_cnt_6_mon)

        contact_hour_1to6_call_min_tot_6_mon_inout_perc = perc(contact_hour_1to6_call_min_tot_6_mon, contact_hour_1to6_min_tot_6_mon)
        contact_hour_7to12_call_min_tot_6_mon_inout_perc = perc(contact_hour_7to12_call_min_tot_6_mon, contact_hour_7to12_min_tot_6_mon)
        contact_hour_13to18_call_min_tot_6_mon_inout_perc = perc(contact_hour_13to18_call_min_tot_6_mon, contact_hour_13to18_min_tot_6_mon)
        contact_hour_19to0_call_min_tot_6_mon_inout_perc = perc(contact_hour_19to0_call_min_tot_6_mon, contact_hour_19to0_min_tot_6_mon)

        contact_hour_1to6_call_cnt_3_mon_inout_perc = perc(contact_hour_1to6_call_cnt_3_mon, contact_hour_1to6_cnt_3_mon)
        contact_hour_7to12_call_cnt_3_mon_inout_perc = perc(contact_hour_7to12_call_cnt_3_mon, contact_hour_7to12_cnt_3_mon)
        contact_hour_13to18_call_cnt_3_mon_inout_perc = perc(contact_hour_13to18_call_cnt_3_mon, contact_hour_13to18_cnt_3_mon)
        contact_hour_19to0_call_cnt_3_mon_inout_perc = perc(contact_hour_19to0_call_cnt_3_mon, contact_hour_19to0_cnt_3_mon)

        contact_hour_1to6_call_min_tot_3_mon_inout_perc = perc(contact_hour_1to6_call_min_tot_3_mon, contact_hour_1to6_min_tot_3_mon)
        contact_hour_7to12_call_min_tot_3_mon_inout_perc = perc(contact_hour_7to12_call_min_tot_3_mon, contact_hour_7to12_min_tot_3_mon)
        contact_hour_13to18_call_min_tot_3_mon_inout_perc = perc(contact_hour_13to18_call_min_tot_3_mon, contact_hour_13to18_min_tot_3_mon)
        contact_hour_19to0_call_min_tot_3_mon_inout_perc = perc(contact_hour_19to0_call_min_tot_3_mon, contact_hour_19to0_min_tot_3_mon)

        contact_hour_1to6_call_cnt_2_mon_inout_perc = perc(contact_hour_1to6_call_cnt_2_mon, contact_hour_1to6_cnt_2_mon)
        contact_hour_7to12_call_cnt_2_mon_inout_perc = perc(contact_hour_7to12_call_cnt_2_mon, contact_hour_7to12_cnt_2_mon)
        contact_hour_13to18_call_cnt_2_mon_inout_perc = perc(contact_hour_13to18_call_cnt_2_mon, contact_hour_13to18_cnt_2_mon)
        contact_hour_19to0_call_cnt_2_mon_inout_perc = perc(contact_hour_19to0_call_cnt_2_mon, contact_hour_19to0_cnt_2_mon)

        contact_hour_1to6_call_min_tot_2_mon_inout_perc = perc(contact_hour_1to6_call_min_tot_2_mon, contact_hour_1to6_min_tot_2_mon)
        contact_hour_7to12_call_min_tot_2_mon_inout_perc = perc(contact_hour_7to12_call_min_tot_2_mon, contact_hour_7to12_min_tot_2_mon)
        contact_hour_13to18_call_min_tot_2_mon_inout_perc = perc(contact_hour_13to18_call_min_tot_2_mon, contact_hour_13to18_min_tot_2_mon)
        contact_hour_19to0_call_min_tot_2_mon_inout_perc = perc(contact_hour_19to0_call_min_tot_2_mon, contact_hour_19to0_min_tot_2_mon)

        contact_hour_1to6_call_cnt_1_mon_inout_perc = perc(contact_hour_1to6_call_cnt_1_mon, contact_hour_1to6_cnt_1_mon)
        contact_hour_7to12_call_cnt_1_mon_inout_perc = perc(contact_hour_7to12_call_cnt_1_mon, contact_hour_7to12_cnt_1_mon)
        contact_hour_13to18_call_cnt_1_mon_inout_perc = perc(contact_hour_13to18_call_cnt_1_mon, contact_hour_13to18_cnt_1_mon)
        contact_hour_19to0_call_cnt_1_mon_inout_perc = perc(contact_hour_19to0_call_cnt_1_mon, contact_hour_19to0_cnt_1_mon)

        contact_hour_1to6_call_min_tot_1_mon_inout_perc = perc(contact_hour_1to6_call_min_tot_1_mon, contact_hour_1to6_min_tot_1_mon)
        contact_hour_7to12_call_min_tot_1_mon_inout_perc = perc(contact_hour_7to12_call_min_tot_1_mon, contact_hour_7to12_min_tot_1_mon)
        contact_hour_13to18_call_min_tot_1_mon_inout_perc = perc(contact_hour_13to18_call_min_tot_1_mon, contact_hour_13to18_min_tot_1_mon)
        contact_hour_19to0_call_min_tot_1_mon_inout_perc = perc(contact_hour_19to0_call_min_tot_1_mon, contact_hour_19to0_min_tot_1_mon)

        contact_hour_1to6_call_cnt_2_wk_inout_perc = perc(contact_hour_1to6_call_cnt_2_wk, contact_hour_1to6_cnt_2_wk)
        contact_hour_7to12_call_cnt_2_wk_inout_perc = perc(contact_hour_7to12_call_cnt_2_wk, contact_hour_7to12_cnt_2_wk)
        contact_hour_13to18_call_cnt_2_wk_inout_perc = perc(contact_hour_13to18_call_cnt_2_wk, contact_hour_13to18_cnt_2_wk)
        contact_hour_19to0_call_cnt_2_wk_inout_perc = perc(contact_hour_19to0_call_cnt_2_wk, contact_hour_19to0_cnt_2_wk)

        contact_hour_1to6_call_min_tot_2_wk_inout_perc = perc(contact_hour_1to6_call_min_tot_2_wk, contact_hour_1to6_min_tot_2_wk)
        contact_hour_7to12_call_min_tot_2_wk_inout_perc = perc(contact_hour_7to12_call_min_tot_2_wk, contact_hour_7to12_min_tot_2_wk)
        contact_hour_13to18_call_min_tot_2_wk_inout_perc = perc(contact_hour_13to18_call_min_tot_2_wk, contact_hour_13to18_min_tot_2_wk)
        contact_hour_19to0_call_min_tot_2_wk_inout_perc = perc(contact_hour_19to0_call_min_tot_2_wk, contact_hour_19to0_min_tot_2_wk)

        contact_hour_1to8_call_cnt_inout_perc = perc(contact_hour_1to8_call_cnt, contact_hour_1to8_cnt)
        contact_hour_9to16_call_cnt_inout_perc = perc(contact_hour_9to16_call_cnt, contact_hour_9to16_cnt)
        contact_hour_17to0_call_cnt_inout_perc = perc(contact_hour_17to0_call_cnt, contact_hour_17to0_cnt)

        contact_hour_1to8_call_min_tot_inout_perc = perc(contact_hour_1to8_call_min_tot, contact_hour_1to8_min_tot)
        contact_hour_9to16_call_min_tot_inout_perc = perc(contact_hour_9to16_call_min_tot, contact_hour_9to16_min_tot)
        contact_hour_17to0_call_min_tot_inout_perc = perc(contact_hour_17to0_call_min_tot, contact_hour_17to0_min_tot)

        contact_hour_1to8_call_cnt_6_mon_inout_perc = perc(contact_hour_1to8_call_cnt_6_mon, contact_hour_1to8_cnt_6_mon)
        contact_hour_9to16_call_cnt_6_mon_inout_perc = perc(contact_hour_9to16_call_cnt_6_mon, contact_hour_9to16_cnt_6_mon)
        contact_hour_17to0_call_cnt_6_mon_inout_perc = perc(contact_hour_17to0_call_cnt_6_mon, contact_hour_17to0_cnt_6_mon)

        contact_hour_1to8_call_min_tot_6_mon_inout_perc = perc(contact_hour_1to8_call_min_tot_6_mon, contact_hour_1to8_min_tot_6_mon)
        contact_hour_9to16_call_min_tot_6_mon_inout_perc = perc(contact_hour_9to16_call_min_tot_6_mon, contact_hour_9to16_min_tot_6_mon)
        contact_hour_17to0_call_min_tot_6_mon_inout_perc = perc(contact_hour_17to0_call_min_tot_6_mon, contact_hour_17to0_min_tot_6_mon)

        contact_hour_1to8_call_cnt_3_mon_inout_perc = perc(contact_hour_1to8_call_cnt_3_mon, contact_hour_1to8_cnt_3_mon)
        contact_hour_9to16_call_cnt_3_mon_inout_perc = perc(contact_hour_9to16_call_cnt_3_mon, contact_hour_9to16_cnt_3_mon)
        contact_hour_17to0_call_cnt_3_mon_inout_perc = perc(contact_hour_17to0_call_cnt_3_mon, contact_hour_17to0_cnt_3_mon)

        contact_hour_1to8_call_min_tot_3_mon_inout_perc = perc(contact_hour_1to8_call_min_tot_3_mon, contact_hour_1to8_min_tot_3_mon)
        contact_hour_9to16_call_min_tot_3_mon_inout_perc = perc(contact_hour_9to16_call_min_tot_3_mon, contact_hour_9to16_min_tot_3_mon)
        contact_hour_17to0_call_min_tot_3_mon_inout_perc = perc(contact_hour_17to0_call_min_tot_3_mon, contact_hour_17to0_min_tot_3_mon)

        contact_hour_1to8_call_cnt_2_mon_inout_perc = perc(contact_hour_1to8_call_cnt_2_mon, contact_hour_1to8_cnt_2_mon)
        contact_hour_9to16_call_cnt_2_mon_inout_perc = perc(contact_hour_9to16_call_cnt_2_mon, contact_hour_9to16_cnt_2_mon)
        contact_hour_17to0_call_cnt_2_mon_inout_perc = perc(contact_hour_17to0_call_cnt_2_mon, contact_hour_17to0_cnt_2_mon)

        contact_hour_1to8_call_min_tot_2_mon_inout_perc = perc(contact_hour_1to8_call_min_tot_2_mon, contact_hour_1to8_min_tot_2_mon)
        contact_hour_9to16_call_min_tot_2_mon_inout_perc = perc(contact_hour_9to16_call_min_tot_2_mon, contact_hour_9to16_min_tot_2_mon)
        contact_hour_17to0_call_min_tot_2_mon_inout_perc = perc(contact_hour_17to0_call_min_tot_2_mon, contact_hour_17to0_min_tot_2_mon)

        contact_hour_1to8_call_cnt_1_mon_inout_perc = perc(contact_hour_1to8_call_cnt_1_mon, contact_hour_1to8_cnt_1_mon)
        contact_hour_9to16_call_cnt_1_mon_inout_perc = perc(contact_hour_9to16_call_cnt_1_mon, contact_hour_9to16_cnt_1_mon)
        contact_hour_17to0_call_cnt_1_mon_inout_perc = perc(contact_hour_17to0_call_cnt_1_mon, contact_hour_17to0_cnt_1_mon)

        contact_hour_1to8_call_min_tot_1_mon_inout_perc = perc(contact_hour_1to8_call_min_tot_1_mon, contact_hour_1to8_min_tot_1_mon)
        contact_hour_9to16_call_min_tot_1_mon_inout_perc = perc(contact_hour_9to16_call_min_tot_1_mon, contact_hour_9to16_min_tot_1_mon)
        contact_hour_17to0_call_min_tot_1_mon_inout_perc = perc(contact_hour_17to0_call_min_tot_1_mon, contact_hour_17to0_min_tot_1_mon)

        contact_hour_1to8_call_cnt_2_wk_inout_perc = perc(contact_hour_1to8_call_cnt_2_wk, contact_hour_1to8_cnt_2_wk)
        contact_hour_9to16_call_cnt_2_wk_inout_perc = perc(contact_hour_9to16_call_cnt_2_wk, contact_hour_9to16_cnt_2_wk)
        contact_hour_17to0_call_cnt_2_wk_inout_perc = perc(contact_hour_17to0_call_cnt_2_wk, contact_hour_17to0_cnt_2_wk)

        contact_hour_1to8_call_min_tot_2_wk_inout_perc = perc(contact_hour_1to8_call_min_tot_2_wk, contact_hour_1to8_min_tot_2_wk)
        contact_hour_9to16_call_min_tot_2_wk_inout_perc = perc(contact_hour_9to16_call_min_tot_2_wk, contact_hour_9to16_min_tot_2_wk)
        contact_hour_17to0_call_min_tot_2_wk_inout_perc = perc(contact_hour_17to0_call_min_tot_2_wk, contact_hour_17to0_min_tot_2_wk)

        contact_hour_9to20_call_cnt_inout_perc = perc(contact_hour_9to20_call_cnt, contact_hour_9to20_cnt)
        contact_hour_21to8_call_cnt_inout_perc = perc(contact_hour_21to8_call_cnt, contact_hour_21to8_cnt)

        contact_hour_9to20_call_min_tot_inout_perc = perc(contact_hour_9to20_call_min_tot, contact_hour_9to20_min_tot)
        contact_hour_21to8_call_min_tot_inout_perc = perc(contact_hour_21to8_call_min_tot, contact_hour_21to8_min_tot)

        contact_hour_9to20_call_cnt_6_mon_inout_perc = perc(contact_hour_9to20_call_cnt_6_mon, contact_hour_9to20_cnt_6_mon)
        contact_hour_21to8_call_cnt_6_mon_inout_perc = perc(contact_hour_21to8_call_cnt_6_mon, contact_hour_21to8_cnt_6_mon)

        contact_hour_9to20_call_min_tot_6_mon_inout_perc = perc(contact_hour_9to20_call_min_tot_6_mon, contact_hour_9to20_min_tot_6_mon)
        contact_hour_21to8_call_min_tot_6_mon_inout_perc = perc(contact_hour_21to8_call_min_tot_6_mon, contact_hour_21to8_min_tot_6_mon)

        contact_hour_9to20_call_cnt_3_mon_inout_perc = perc(contact_hour_9to20_call_cnt_3_mon, contact_hour_9to20_cnt_3_mon)
        contact_hour_21to8_call_cnt_3_mon_inout_perc = perc(contact_hour_21to8_call_cnt_3_mon, contact_hour_21to8_cnt_3_mon)

        contact_hour_9to20_call_min_tot_3_mon_inout_perc = perc(contact_hour_9to20_call_min_tot_3_mon, contact_hour_9to20_min_tot_3_mon)
        contact_hour_21to8_call_min_tot_3_mon_inout_perc = perc(contact_hour_21to8_call_min_tot_3_mon, contact_hour_21to8_min_tot_3_mon)

        contact_hour_9to20_call_cnt_2_mon_inout_perc = perc(contact_hour_9to20_call_cnt_2_mon, contact_hour_9to20_cnt_2_mon)
        contact_hour_21to8_call_cnt_2_mon_inout_perc = perc(contact_hour_21to8_call_cnt_2_mon, contact_hour_21to8_cnt_2_mon)

        contact_hour_9to20_call_min_tot_2_mon_inout_perc = perc(contact_hour_9to20_call_min_tot_2_mon, contact_hour_9to20_min_tot_2_mon)
        contact_hour_21to8_call_min_tot_2_mon_inout_perc = perc(contact_hour_21to8_call_min_tot_2_mon, contact_hour_21to8_min_tot_2_mon)

        contact_hour_9to20_call_cnt_1_mon_inout_perc = perc(contact_hour_9to20_call_cnt_1_mon, contact_hour_9to20_cnt_1_mon)
        contact_hour_21to8_call_cnt_1_mon_inout_perc = perc(contact_hour_21to8_call_cnt_1_mon, contact_hour_21to8_cnt_1_mon)

        contact_hour_9to20_call_min_tot_1_mon_inout_perc = perc(contact_hour_9to20_call_min_tot_1_mon, contact_hour_9to20_min_tot_1_mon)
        contact_hour_21to8_call_min_tot_1_mon_inout_perc = perc(contact_hour_21to8_call_min_tot_1_mon, contact_hour_21to8_min_tot_1_mon)

        contact_hour_9to20_call_cnt_2_wk_inout_perc = perc(contact_hour_9to20_call_cnt_2_wk, contact_hour_9to20_cnt_2_wk)
        contact_hour_21to8_call_cnt_2_wk_inout_perc = perc(contact_hour_21to8_call_cnt_2_wk, contact_hour_21to8_cnt_2_wk)

        contact_hour_9to20_call_min_tot_2_wk_inout_perc = perc(contact_hour_9to20_call_min_tot_2_wk, contact_hour_9to20_min_tot_2_wk)
        contact_hour_21to8_call_min_tot_2_wk_inout_perc = perc(contact_hour_21to8_call_min_tot_2_wk, contact_hour_21to8_min_tot_2_wk)

        # contact weekday and weekend avg
        contact_weekday_min_avg = perc(contact_weekday_min_tot, contact_weekday_cnt)
        contact_weekday_min_avg_6_mon = perc(contact_weekday_min_tot_6_mon, contact_weekday_cnt_6_mon)
        contact_weekday_min_avg_3_mon = perc(contact_weekday_min_tot_3_mon, contact_weekday_cnt_3_mon)
        contact_weekday_min_avg_2_mon = perc(contact_weekday_min_tot_2_mon, contact_weekday_cnt_2_mon)
        contact_weekday_min_avg_1_mon = perc(contact_weekday_min_tot_1_mon, contact_weekday_cnt_1_mon)
        contact_weekday_min_avg_2_wk = perc(contact_weekday_min_tot_2_wk, contact_weekday_cnt_2_wk)

        contact_weekend_min_avg = perc(contact_weekend_min_tot, contact_weekend_cnt)
        contact_weekend_min_avg_6_mon = perc(contact_weekend_min_tot_6_mon, contact_weekend_cnt_6_mon)
        contact_weekend_min_avg_3_mon = perc(contact_weekend_min_tot_3_mon, contact_weekend_cnt_3_mon)
        contact_weekend_min_avg_2_mon = perc(contact_weekend_min_tot_2_mon, contact_weekend_cnt_2_mon)
        contact_weekend_min_avg_1_mon = perc(contact_weekend_min_tot_1_mon, contact_weekend_cnt_1_mon)
        contact_weekend_min_avg_2_wk = perc(contact_weekend_min_tot_2_wk, contact_weekend_cnt_2_wk)

        contact_weekday_call_min_avg = perc(contact_weekday_call_min_tot, contact_weekday_call_cnt)
        contact_weekday_call_min_avg_6_mon = perc(contact_weekday_call_min_tot_6_mon, contact_weekday_call_cnt_6_mon)
        contact_weekday_call_min_avg_3_mon = perc(contact_weekday_call_min_tot_3_mon, contact_weekday_call_cnt_3_mon)
        contact_weekday_call_min_avg_2_mon = perc(contact_weekday_call_min_tot_2_mon, contact_weekday_call_cnt_2_mon)
        contact_weekday_call_min_avg_1_mon = perc(contact_weekday_call_min_tot_1_mon, contact_weekday_call_cnt_1_mon)
        contact_weekday_call_min_avg_2_wk = perc(contact_weekday_call_min_tot_2_wk, contact_weekday_call_cnt_2_wk)

        contact_weekend_call_min_avg = perc(contact_weekend_call_min_tot, contact_weekend_call_cnt)
        contact_weekend_call_min_avg_6_mon = perc(contact_weekend_call_min_tot_6_mon, contact_weekend_call_cnt_6_mon)
        contact_weekend_call_min_avg_3_mon = perc(contact_weekend_call_min_tot_3_mon, contact_weekend_call_cnt_3_mon)
        contact_weekend_call_min_avg_2_mon = perc(contact_weekend_call_min_tot_2_mon, contact_weekend_call_cnt_2_mon)
        contact_weekend_call_min_avg_1_mon = perc(contact_weekend_call_min_tot_1_mon, contact_weekend_call_cnt_1_mon)
        contact_weekend_call_min_avg_2_wk = perc(contact_weekend_call_min_tot_2_wk, contact_weekend_call_cnt_2_wk)

        contact_weekday_rece_min_avg = perc(contact_weekday_rece_min_tot, contact_weekday_rece_cnt)
        contact_weekday_rece_min_avg_6_mon = perc(contact_weekday_rece_min_tot_6_mon, contact_weekday_rece_cnt_6_mon)
        contact_weekday_rece_min_avg_3_mon = perc(contact_weekday_rece_min_tot_3_mon, contact_weekday_rece_cnt_3_mon)
        contact_weekday_rece_min_avg_2_mon = perc(contact_weekday_rece_min_tot_2_mon, contact_weekday_rece_cnt_2_mon)
        contact_weekday_rece_min_avg_1_mon = perc(contact_weekday_rece_min_tot_1_mon, contact_weekday_rece_cnt_1_mon)
        contact_weekday_rece_min_avg_2_wk = perc(contact_weekday_rece_min_tot_2_wk, contact_weekday_rece_cnt_2_wk)

        contact_weekend_rece_min_avg = perc(contact_weekend_rece_min_tot, contact_weekend_rece_cnt)
        contact_weekend_rece_min_avg_6_mon = perc(contact_weekend_rece_min_tot_6_mon, contact_weekend_rece_cnt_6_mon)
        contact_weekend_rece_min_avg_3_mon = perc(contact_weekend_rece_min_tot_3_mon, contact_weekend_rece_cnt_3_mon)
        contact_weekend_rece_min_avg_2_mon = perc(contact_weekend_rece_min_tot_2_mon, contact_weekend_rece_cnt_2_mon)
        contact_weekend_rece_min_avg_1_mon = perc(contact_weekend_rece_min_tot_1_mon, contact_weekend_rece_cnt_1_mon)
        contact_weekend_rece_min_avg_2_wk = perc(contact_weekend_rece_min_tot_2_wk, contact_weekend_rece_cnt_2_wk)

        # contact weekday and weekend 6 mon perc
        contact_weekday_cnt_3_mon_perc = perc(contact_weekday_cnt_3_mon, contact_weekday_cnt_6_mon)
        contact_weekday_min_tot_3_mon_perc = perc(contact_weekday_min_tot_3_mon, contact_weekday_min_tot_6_mon)
        contact_weekday_call_cnt_3_mon_perc = perc(contact_weekday_call_cnt_3_mon, contact_weekday_call_cnt_6_mon)
        contact_weekday_rece_cnt_3_mon_perc = perc(contact_weekday_rece_cnt_3_mon, contact_weekday_rece_cnt_6_mon)
        contact_weekday_call_min_tot_3_mon_perc = perc(contact_weekday_call_min_tot_3_mon, contact_weekday_call_min_tot_6_mon)
        contact_weekday_rece_min_tot_3_mon_perc = perc(contact_weekday_rece_min_tot_3_mon, contact_weekday_rece_min_tot_6_mon)

        contact_weekday_cnt_2_mon_perc = perc(contact_weekday_cnt_2_mon, contact_weekday_cnt_6_mon)
        contact_weekday_min_tot_2_mon_perc = perc(contact_weekday_min_tot_2_mon, contact_weekday_min_tot_6_mon)
        contact_weekday_call_cnt_2_mon_perc = perc(contact_weekday_call_cnt_2_mon, contact_weekday_call_cnt_6_mon)
        contact_weekday_rece_cnt_2_mon_perc = perc(contact_weekday_rece_cnt_2_mon, contact_weekday_rece_cnt_6_mon)
        contact_weekday_call_min_tot_2_mon_perc = perc(contact_weekday_call_min_tot_2_mon, contact_weekday_call_min_tot_6_mon)
        contact_weekday_rece_min_tot_2_mon_perc = perc(contact_weekday_rece_min_tot_2_mon, contact_weekday_rece_min_tot_6_mon)

        contact_weekday_cnt_1_mon_perc = perc(contact_weekday_cnt_1_mon, contact_weekday_cnt_6_mon)
        contact_weekday_min_tot_1_mon_perc = perc(contact_weekday_min_tot_1_mon, contact_weekday_min_tot_6_mon)
        contact_weekday_call_cnt_1_mon_perc = perc(contact_weekday_call_cnt_1_mon, contact_weekday_call_cnt_6_mon)
        contact_weekday_rece_cnt_1_mon_perc = perc(contact_weekday_rece_cnt_1_mon, contact_weekday_rece_cnt_6_mon)
        contact_weekday_call_min_tot_1_mon_perc = perc(contact_weekday_call_min_tot_1_mon, contact_weekday_call_min_tot_6_mon)
        contact_weekday_rece_min_tot_1_mon_perc = perc(contact_weekday_rece_min_tot_1_mon, contact_weekday_rece_min_tot_6_mon)

        contact_weekday_cnt_2_wk_perc = perc(contact_weekday_cnt_2_wk, contact_weekday_cnt_6_mon)
        contact_weekday_min_tot_2_wk_perc = perc(contact_weekday_min_tot_2_wk, contact_weekday_min_tot_6_mon)
        contact_weekday_call_cnt_2_wk_perc = perc(contact_weekday_call_cnt_2_wk, contact_weekday_call_cnt_6_mon)
        contact_weekday_rece_cnt_2_wk_perc = perc(contact_weekday_rece_cnt_2_wk, contact_weekday_rece_cnt_6_mon)
        contact_weekday_call_min_tot_2_wk_perc = perc(contact_weekday_call_min_tot_2_wk, contact_weekday_call_min_tot_6_mon)
        contact_weekday_rece_min_tot_2_wk_perc = perc(contact_weekday_rece_min_tot_2_wk, contact_weekday_rece_min_tot_6_mon)

        contact_weekend_cnt_3_mon_perc = perc(contact_weekend_cnt_3_mon, contact_weekend_cnt_6_mon)
        contact_weekend_min_tot_3_mon_perc = perc(contact_weekend_min_tot_3_mon, contact_weekend_min_tot_6_mon)
        contact_weekend_call_cnt_3_mon_perc = perc(contact_weekend_call_cnt_3_mon, contact_weekend_call_cnt_6_mon)
        contact_weekend_rece_cnt_3_mon_perc = perc(contact_weekend_rece_cnt_3_mon, contact_weekend_rece_cnt_6_mon)
        contact_weekend_call_min_tot_3_mon_perc = perc(contact_weekend_call_min_tot_3_mon, contact_weekend_call_min_tot_6_mon)
        contact_weekend_rece_min_tot_3_mon_perc = perc(contact_weekend_rece_min_tot_3_mon, contact_weekend_rece_min_tot_6_mon)

        contact_weekend_cnt_2_mon_perc = perc(contact_weekend_cnt_2_mon, contact_weekend_cnt_6_mon)
        contact_weekend_min_tot_2_mon_perc = perc(contact_weekend_min_tot_2_mon, contact_weekend_min_tot_6_mon)
        contact_weekend_call_cnt_2_mon_perc = perc(contact_weekend_call_cnt_2_mon, contact_weekend_call_cnt_6_mon)
        contact_weekend_rece_cnt_2_mon_perc = perc(contact_weekend_rece_cnt_2_mon, contact_weekend_rece_cnt_6_mon)
        contact_weekend_call_min_tot_2_mon_perc = perc(contact_weekend_call_min_tot_2_mon, contact_weekend_call_min_tot_6_mon)
        contact_weekend_rece_min_tot_2_mon_perc = perc(contact_weekend_rece_min_tot_2_mon, contact_weekend_rece_min_tot_6_mon)

        contact_weekend_cnt_1_mon_perc = perc(contact_weekend_cnt_1_mon, contact_weekend_cnt_6_mon)
        contact_weekend_min_tot_1_mon_perc = perc(contact_weekend_min_tot_1_mon, contact_weekend_min_tot_6_mon)
        contact_weekend_call_cnt_1_mon_perc = perc(contact_weekend_call_cnt_1_mon, contact_weekend_call_cnt_6_mon)
        contact_weekend_rece_cnt_1_mon_perc = perc(contact_weekend_rece_cnt_1_mon, contact_weekend_rece_cnt_6_mon)
        contact_weekend_call_min_tot_1_mon_perc = perc(contact_weekend_call_min_tot_1_mon, contact_weekend_call_min_tot_6_mon)
        contact_weekend_rece_min_tot_1_mon_perc = perc(contact_weekend_rece_min_tot_1_mon, contact_weekend_rece_min_tot_6_mon)

        contact_weekend_cnt_2_wk_perc = perc(contact_weekend_cnt_2_wk, contact_weekend_cnt_6_mon)
        contact_weekend_min_tot_2_wk_perc = perc(contact_weekend_min_tot_2_wk, contact_weekend_min_tot_6_mon)
        contact_weekend_call_cnt_2_wk_perc = perc(contact_weekend_call_cnt_2_wk, contact_weekend_call_cnt_6_mon)
        contact_weekend_rece_cnt_2_wk_perc = perc(contact_weekend_rece_cnt_2_wk, contact_weekend_rece_cnt_6_mon)
        contact_weekend_call_min_tot_2_wk_perc = perc(contact_weekend_call_min_tot_2_wk, contact_weekend_call_min_tot_6_mon)
        contact_weekend_rece_min_tot_2_wk_perc = perc(contact_weekend_rece_min_tot_2_wk, contact_weekend_rece_min_tot_6_mon)

        # sum of weekday and weekend
        contact_week_cnt = contact_weekday_cnt + contact_weekend_cnt
        contact_week_min_tot = contact_weekday_min_tot + contact_weekend_min_tot
        contact_week_call_cnt = contact_weekday_call_cnt + contact_weekend_call_cnt
        contact_week_rece_cnt = contact_weekday_rece_cnt + contact_weekend_rece_cnt
        contact_week_call_min_tot = contact_weekday_call_min_tot + contact_weekend_call_min_tot
        contact_week_rece_min_tot = contact_weekday_rece_min_tot + contact_weekend_rece_min_tot

        contact_week_cnt_6_mon = contact_weekday_cnt_6_mon + contact_weekend_cnt_6_mon
        contact_week_min_tot_6_mon = contact_weekday_min_tot_6_mon + contact_weekend_min_tot_6_mon
        contact_week_call_cnt_6_mon = contact_weekday_call_cnt_6_mon + contact_weekend_call_cnt_6_mon
        contact_week_rece_cnt_6_mon = contact_weekday_rece_cnt_6_mon + contact_weekend_rece_cnt_6_mon
        contact_week_call_min_tot_6_mon = contact_weekday_call_min_tot_6_mon + contact_weekend_call_min_tot_6_mon
        contact_week_rece_min_tot_6_mon = contact_weekday_rece_min_tot_6_mon + contact_weekend_rece_min_tot_6_mon

        contact_week_cnt_3_mon = contact_weekday_cnt_3_mon + contact_weekend_cnt_3_mon
        contact_week_min_tot_3_mon = contact_weekday_min_tot_3_mon + contact_weekend_min_tot_3_mon
        contact_week_call_cnt_3_mon = contact_weekday_call_cnt_3_mon + contact_weekend_call_cnt_3_mon
        contact_week_rece_cnt_3_mon = contact_weekday_rece_cnt_3_mon + contact_weekend_rece_cnt_3_mon
        contact_week_call_min_tot_3_mon = contact_weekday_call_min_tot_3_mon + contact_weekend_call_min_tot_3_mon
        contact_week_rece_min_tot_3_mon = contact_weekday_rece_min_tot_3_mon + contact_weekend_rece_min_tot_3_mon

        contact_week_cnt_2_mon = contact_weekday_cnt_2_mon + contact_weekend_cnt_2_mon
        contact_week_min_tot_2_mon = contact_weekday_min_tot_2_mon + contact_weekend_min_tot_2_mon
        contact_week_call_cnt_2_mon = contact_weekday_call_cnt_2_mon + contact_weekend_call_cnt_2_mon
        contact_week_rece_cnt_2_mon = contact_weekday_rece_cnt_2_mon + contact_weekend_rece_cnt_2_mon
        contact_week_call_min_tot_2_mon = contact_weekday_call_min_tot_2_mon + contact_weekend_call_min_tot_2_mon
        contact_week_rece_min_tot_2_mon = contact_weekday_rece_min_tot_2_mon + contact_weekend_rece_min_tot_2_mon

        contact_week_cnt_1_mon = contact_weekday_cnt_1_mon + contact_weekend_cnt_1_mon
        contact_week_min_tot_1_mon = contact_weekday_min_tot_1_mon + contact_weekend_min_tot_1_mon
        contact_week_call_cnt_1_mon = contact_weekday_call_cnt_1_mon + contact_weekend_call_cnt_1_mon
        contact_week_rece_cnt_1_mon = contact_weekday_rece_cnt_1_mon + contact_weekend_rece_cnt_1_mon
        contact_week_call_min_tot_1_mon = contact_weekday_call_min_tot_1_mon + contact_weekend_call_min_tot_1_mon
        contact_week_rece_min_tot_1_mon = contact_weekday_rece_min_tot_1_mon + contact_weekend_rece_min_tot_1_mon

        contact_week_cnt_2_wk = contact_weekday_cnt_2_wk + contact_weekend_cnt_2_wk
        contact_week_min_tot_2_wk = contact_weekday_min_tot_2_wk + contact_weekend_min_tot_2_wk
        contact_week_call_cnt_2_wk = contact_weekday_call_cnt_2_wk + contact_weekend_call_cnt_2_wk
        contact_week_rece_cnt_2_wk = contact_weekday_rece_cnt_2_wk + contact_weekend_rece_cnt_2_wk
        contact_week_call_min_tot_2_wk = contact_weekday_call_min_tot_2_wk + contact_weekend_call_min_tot_2_wk
        contact_week_rece_min_tot_2_wk = contact_weekday_rece_min_tot_2_wk + contact_weekend_rece_min_tot_2_wk

        # weekday week perc
        contact_weekday_cnt_week_perc = perc(contact_weekday_cnt, contact_week_cnt)
        contact_weekday_min_tot_week_perc = perc(contact_weekday_min_tot, contact_week_min_tot)
        contact_weekday_call_cnt_week_perc = perc(contact_weekday_call_cnt, contact_week_call_cnt)
        contact_weekday_rece_cnt_week_perc = perc(contact_weekday_rece_cnt, contact_week_rece_cnt)
        contact_weekday_call_min_tot_week_perc = perc(contact_weekday_call_min_tot, contact_week_call_min_tot)
        contact_weekday_rece_min_tot_week_perc = perc(contact_weekday_rece_min_tot, contact_week_rece_min_tot)

        contact_weekday_cnt_6_mon_week_perc = perc(contact_weekday_cnt_6_mon, contact_week_cnt_6_mon)
        contact_weekday_min_tot_6_mon_week_perc = perc(contact_weekday_min_tot_6_mon, contact_week_min_tot_6_mon)
        contact_weekday_call_cnt_6_mon_week_perc = perc(contact_weekday_call_cnt_6_mon, contact_week_call_cnt_6_mon)
        contact_weekday_rece_cnt_6_mon_week_perc = perc(contact_weekday_rece_cnt_6_mon, contact_week_rece_cnt_6_mon)
        contact_weekday_call_min_tot_6_mon_week_perc = perc(contact_weekday_call_min_tot_6_mon, contact_week_call_min_tot_6_mon)
        contact_weekday_rece_min_tot_6_mon_week_perc = perc(contact_weekday_rece_min_tot_6_mon, contact_week_rece_min_tot_6_mon)

        contact_weekday_cnt_3_mon_week_perc = perc(contact_weekday_cnt_3_mon, contact_week_cnt_3_mon)
        contact_weekday_min_tot_3_mon_week_perc = perc(contact_weekday_min_tot_3_mon, contact_week_min_tot_3_mon)
        contact_weekday_call_cnt_3_mon_week_perc = perc(contact_weekday_call_cnt_3_mon, contact_week_call_cnt_3_mon)
        contact_weekday_rece_cnt_3_mon_week_perc = perc(contact_weekday_rece_cnt_3_mon, contact_week_rece_cnt_3_mon)
        contact_weekday_call_min_tot_3_mon_week_perc = perc(contact_weekday_call_min_tot_3_mon, contact_week_call_min_tot_3_mon)
        contact_weekday_rece_min_tot_3_mon_week_perc = perc(contact_weekday_rece_min_tot_3_mon, contact_week_rece_min_tot_3_mon)

        contact_weekday_cnt_2_mon_week_perc = perc(contact_weekday_cnt_2_mon, contact_week_cnt_2_mon)
        contact_weekday_min_tot_2_mon_week_perc = perc(contact_weekday_min_tot_2_mon, contact_week_min_tot_2_mon)
        contact_weekday_call_cnt_2_mon_week_perc = perc(contact_weekday_call_cnt_2_mon, contact_week_call_cnt_2_mon)
        contact_weekday_rece_cnt_2_mon_week_perc = perc(contact_weekday_rece_cnt_2_mon, contact_week_rece_cnt_2_mon)
        contact_weekday_call_min_tot_2_mon_week_perc = perc(contact_weekday_call_min_tot_2_mon, contact_week_call_min_tot_2_mon)
        contact_weekday_rece_min_tot_2_mon_week_perc = perc(contact_weekday_rece_min_tot_2_mon, contact_week_rece_min_tot_2_mon)

        contact_weekday_cnt_1_mon_week_perc = perc(contact_weekday_cnt_1_mon, contact_week_cnt_1_mon)
        contact_weekday_min_tot_1_mon_week_perc = perc(contact_weekday_min_tot_1_mon, contact_week_min_tot_1_mon)
        contact_weekday_call_cnt_1_mon_week_perc = perc(contact_weekday_call_cnt_1_mon, contact_week_call_cnt_1_mon)
        contact_weekday_rece_cnt_1_mon_week_perc = perc(contact_weekday_rece_cnt_1_mon, contact_week_rece_cnt_1_mon)
        contact_weekday_call_min_tot_1_mon_week_perc = perc(contact_weekday_call_min_tot_1_mon, contact_week_call_min_tot_1_mon)
        contact_weekday_rece_min_tot_1_mon_week_perc = perc(contact_weekday_rece_min_tot_1_mon, contact_week_rece_min_tot_1_mon)

        contact_weekday_cnt_2_wk_week_perc = perc(contact_weekday_cnt_2_wk, contact_week_cnt_2_wk)
        contact_weekday_min_tot_2_wk_week_perc = perc(contact_weekday_min_tot_2_wk, contact_week_min_tot_2_wk)
        contact_weekday_call_cnt_2_wk_week_perc = perc(contact_weekday_call_cnt_2_wk, contact_week_call_cnt_2_wk)
        contact_weekday_rece_cnt_2_wk_week_perc = perc(contact_weekday_rece_cnt_2_wk, contact_week_rece_cnt_2_wk)
        contact_weekday_call_min_tot_2_wk_week_perc = perc(contact_weekday_call_min_tot_2_wk, contact_week_call_min_tot_2_wk)
        contact_weekday_rece_min_tot_2_wk_week_perc = perc(contact_weekday_rece_min_tot_2_wk, contact_week_rece_min_tot_2_wk)



        # contact duration avg 15, 30, 60s
        contact_min_over_15s_min_avg = perc(contact_min_over_15s_min_tot, contact_min_over_15s_cnt)
        contact_min_over_15s_call_min_avg = perc(contact_min_over_15s_call_min_tot, contact_min_over_15s_call_cnt)
        contact_min_over_15s_rece_min_avg = perc(contact_min_over_15s_rece_min_tot, contact_min_over_15s_rece_cnt)

        contact_min_over_30s_min_avg = perc(contact_min_over_30s_min_tot, contact_min_over_30s_cnt)
        contact_min_over_30s_call_min_avg = perc(contact_min_over_30s_call_min_tot, contact_min_over_30s_call_cnt)
        contact_min_over_30s_rece_min_avg = perc(contact_min_over_30s_rece_min_tot, contact_min_over_30s_rece_cnt)

        contact_min_over_60s_min_avg = perc(contact_min_over_60s_min_tot, contact_min_over_60s_cnt)
        contact_min_over_60s_call_min_avg = perc(contact_min_over_60s_call_min_tot, contact_min_over_60s_call_cnt)
        contact_min_over_60s_rece_min_avg = perc(contact_min_over_60s_rece_min_tot, contact_min_over_60s_rece_cnt)

        contact_min_over_15s_min_avg_6_mon = perc(contact_min_over_15s_min_tot_6_mon, contact_min_over_15s_cnt_6_mon)
        contact_min_over_15s_call_min_avg_6_mon = perc(contact_min_over_15s_call_min_tot_6_mon,
                                                       contact_min_over_15s_call_cnt_6_mon)
        contact_min_over_15s_rece_min_avg_6_mon = perc(contact_min_over_15s_rece_min_tot_6_mon,
                                                       contact_min_over_15s_rece_cnt_6_mon)

        contact_min_over_30s_min_avg_6_mon = perc(contact_min_over_30s_min_tot_6_mon, contact_min_over_30s_cnt_6_mon)
        contact_min_over_30s_call_min_avg_6_mon = perc(contact_min_over_30s_call_min_tot_6_mon,
                                                       contact_min_over_30s_call_cnt_6_mon)
        contact_min_over_30s_rece_min_avg_6_mon = perc(contact_min_over_30s_rece_min_tot_6_mon,
                                                       contact_min_over_30s_rece_cnt_6_mon)

        contact_min_over_60s_min_avg_6_mon = perc(contact_min_over_60s_min_tot_6_mon, contact_min_over_60s_cnt_6_mon)
        contact_min_over_60s_call_min_avg_6_mon = perc(contact_min_over_60s_call_min_tot_6_mon,
                                                       contact_min_over_60s_call_cnt_6_mon)
        contact_min_over_60s_rece_min_avg_6_mon = perc(contact_min_over_60s_rece_min_tot_6_mon,
                                                       contact_min_over_60s_rece_cnt_6_mon)

        contact_min_over_15s_min_avg_3_mon = perc(contact_min_over_15s_min_tot_3_mon, contact_min_over_15s_cnt_3_mon)
        contact_min_over_15s_call_min_avg_3_mon = perc(contact_min_over_15s_call_min_tot_3_mon,
                                                       contact_min_over_15s_call_cnt_3_mon)
        contact_min_over_15s_rece_min_avg_3_mon = perc(contact_min_over_15s_rece_min_tot_3_mon,
                                                       contact_min_over_15s_rece_cnt_3_mon)

        contact_min_over_30s_min_avg_3_mon = perc(contact_min_over_30s_min_tot_3_mon, contact_min_over_30s_cnt_3_mon)
        contact_min_over_30s_call_min_avg_3_mon = perc(contact_min_over_30s_call_min_tot_3_mon,
                                                       contact_min_over_30s_call_cnt_3_mon)
        contact_min_over_30s_rece_min_avg_3_mon = perc(contact_min_over_30s_rece_min_tot_3_mon,
                                                       contact_min_over_30s_rece_cnt_3_mon)

        contact_min_over_60s_min_avg_3_mon = perc(contact_min_over_60s_min_tot_3_mon, contact_min_over_60s_cnt_3_mon)
        contact_min_over_60s_call_min_avg_3_mon = perc(contact_min_over_60s_call_min_tot_3_mon,
                                                       contact_min_over_60s_call_cnt_3_mon)
        contact_min_over_60s_rece_min_avg_3_mon = perc(contact_min_over_60s_rece_min_tot_3_mon,
                                                       contact_min_over_60s_rece_cnt_3_mon)

        contact_min_over_15s_min_avg_2_mon = perc(contact_min_over_15s_min_tot_2_mon, contact_min_over_15s_cnt_2_mon)
        contact_min_over_15s_call_min_avg_2_mon = perc(contact_min_over_15s_call_min_tot_2_mon,
                                                       contact_min_over_15s_call_cnt_2_mon)
        contact_min_over_15s_rece_min_avg_2_mon = perc(contact_min_over_15s_rece_min_tot_2_mon,
                                                       contact_min_over_15s_rece_cnt_2_mon)

        contact_min_over_30s_min_avg_2_mon = perc(contact_min_over_30s_min_tot_2_mon, contact_min_over_30s_cnt_2_mon)
        contact_min_over_30s_call_min_avg_2_mon = perc(contact_min_over_30s_call_min_tot_2_mon,
                                                       contact_min_over_30s_call_cnt_2_mon)
        contact_min_over_30s_rece_min_avg_2_mon = perc(contact_min_over_30s_rece_min_tot_2_mon,
                                                       contact_min_over_30s_rece_cnt_2_mon)

        contact_min_over_60s_min_avg_2_mon = perc(contact_min_over_60s_min_tot_2_mon, contact_min_over_60s_cnt_2_mon)
        contact_min_over_60s_call_min_avg_2_mon = perc(contact_min_over_60s_call_min_tot_2_mon,
                                                       contact_min_over_60s_call_cnt_2_mon)
        contact_min_over_60s_rece_min_avg_2_mon = perc(contact_min_over_60s_rece_min_tot_2_mon,
                                                       contact_min_over_60s_rece_cnt_2_mon)

        contact_min_over_15s_min_avg_1_mon = perc(contact_min_over_15s_min_tot_1_mon, contact_min_over_15s_cnt_1_mon)
        contact_min_over_15s_call_min_avg_1_mon = perc(contact_min_over_15s_call_min_tot_1_mon,
                                                       contact_min_over_15s_call_cnt_1_mon)
        contact_min_over_15s_rece_min_avg_1_mon = perc(contact_min_over_15s_rece_min_tot_1_mon,
                                                       contact_min_over_15s_rece_cnt_1_mon)

        contact_min_over_30s_min_avg_1_mon = perc(contact_min_over_30s_min_tot_1_mon, contact_min_over_30s_cnt_1_mon)
        contact_min_over_30s_call_min_avg_1_mon = perc(contact_min_over_30s_call_min_tot_1_mon,
                                                       contact_min_over_30s_call_cnt_1_mon)
        contact_min_over_30s_rece_min_avg_1_mon = perc(contact_min_over_30s_rece_min_tot_1_mon,
                                                       contact_min_over_30s_rece_cnt_1_mon)

        contact_min_over_60s_min_avg_1_mon = perc(contact_min_over_60s_min_tot_1_mon, contact_min_over_60s_cnt_1_mon)
        contact_min_over_60s_call_min_avg_1_mon = perc(contact_min_over_60s_call_min_tot_1_mon,
                                                       contact_min_over_60s_call_cnt_1_mon)
        contact_min_over_60s_rece_min_avg_1_mon = perc(contact_min_over_60s_rece_min_tot_1_mon,
                                                       contact_min_over_60s_rece_cnt_1_mon)

        contact_min_over_15s_min_avg_2_wk = perc(contact_min_over_15s_min_tot_2_wk, contact_min_over_15s_cnt_2_wk)
        contact_min_over_15s_call_min_avg_2_wk = perc(contact_min_over_15s_call_min_tot_2_wk,
                                                      contact_min_over_15s_call_cnt_2_wk)
        contact_min_over_15s_rece_min_avg_2_wk = perc(contact_min_over_15s_rece_min_tot_2_wk,
                                                      contact_min_over_15s_rece_cnt_2_wk)

        contact_min_over_30s_min_avg_2_wk = perc(contact_min_over_30s_min_tot_2_wk, contact_min_over_30s_cnt_2_wk)
        contact_min_over_30s_call_min_avg_2_wk = perc(contact_min_over_30s_call_min_tot_2_wk,
                                                      contact_min_over_30s_call_cnt_2_wk)
        contact_min_over_30s_rece_min_avg_2_wk = perc(contact_min_over_30s_rece_min_tot_2_wk,
                                                      contact_min_over_30s_rece_cnt_2_wk)

        contact_min_over_60s_min_avg_2_wk = perc(contact_min_over_60s_min_tot_2_wk, contact_min_over_60s_cnt_2_wk)
        contact_min_over_60s_call_min_avg_2_wk = perc(contact_min_over_60s_call_min_tot_2_wk,
                                                      contact_min_over_60s_call_cnt_2_wk)
        contact_min_over_60s_rece_min_avg_2_wk = perc(contact_min_over_60s_rece_min_tot_2_wk,
                                                      contact_min_over_60s_rece_cnt_2_wk)

        # contact duration 15, 30, 60 inout perc
        contact_min_over_15s_call_cnt_inout_perc = perc(contact_min_over_15s_call_cnt, contact_min_over_15s_cnt)
        contact_min_over_15s_rece_cnt_inout_perc = perc(contact_min_over_15s_rece_cnt, contact_min_over_15s_cnt)

        contact_min_over_30s_call_cnt_inout_perc = perc(contact_min_over_30s_call_cnt, contact_min_over_30s_cnt)
        contact_min_over_30s_rece_cnt_inout_perc = perc(contact_min_over_30s_rece_cnt, contact_min_over_30s_cnt)

        contact_min_over_60s_call_cnt_inout_perc = perc(contact_min_over_60s_call_cnt, contact_min_over_60s_cnt)
        contact_min_over_60s_rece_cnt_inout_perc = perc(contact_min_over_60s_rece_cnt, contact_min_over_60s_cnt)

        contact_min_over_15s_call_cnt_6_mon_inout_perc = perc(contact_min_over_15s_call_cnt_6_mon,
                                                              contact_min_over_15s_cnt_6_mon)
        contact_min_over_15s_rece_cnt_6_mon_inout_perc = perc(contact_min_over_15s_rece_cnt_6_mon,
                                                              contact_min_over_15s_cnt_6_mon)

        contact_min_over_30s_call_cnt_6_mon_inout_perc = perc(contact_min_over_30s_call_cnt_6_mon,
                                                              contact_min_over_30s_cnt_6_mon)
        contact_min_over_30s_rece_cnt_6_mon_inout_perc = perc(contact_min_over_30s_rece_cnt_6_mon,
                                                              contact_min_over_30s_cnt_6_mon)

        contact_min_over_60s_call_cnt_6_mon_inout_perc = perc(contact_min_over_60s_call_cnt_6_mon,
                                                              contact_min_over_60s_cnt_6_mon)
        contact_min_over_60s_rece_cnt_6_mon_inout_perc = perc(contact_min_over_60s_rece_cnt_6_mon,
                                                              contact_min_over_60s_cnt_6_mon)

        contact_min_over_15s_call_cnt_3_mon_inout_perc = perc(contact_min_over_15s_call_cnt_3_mon,
                                                              contact_min_over_15s_cnt_3_mon)
        contact_min_over_15s_rece_cnt_3_mon_inout_perc = perc(contact_min_over_15s_rece_cnt_3_mon,
                                                              contact_min_over_15s_cnt_3_mon)

        contact_min_over_30s_call_cnt_3_mon_inout_perc = perc(contact_min_over_30s_call_cnt_3_mon,
                                                              contact_min_over_30s_cnt_3_mon)
        contact_min_over_30s_rece_cnt_3_mon_inout_perc = perc(contact_min_over_30s_rece_cnt_3_mon,
                                                              contact_min_over_30s_cnt_3_mon)

        contact_min_over_60s_call_cnt_3_mon_inout_perc = perc(contact_min_over_60s_call_cnt_3_mon,
                                                              contact_min_over_60s_cnt_3_mon)
        contact_min_over_60s_rece_cnt_3_mon_inout_perc = perc(contact_min_over_60s_rece_cnt_3_mon,
                                                              contact_min_over_60s_cnt_3_mon)

        contact_min_over_15s_call_cnt_2_mon_inout_perc = perc(contact_min_over_15s_call_cnt_2_mon,
                                                              contact_min_over_15s_cnt_2_mon)
        contact_min_over_15s_rece_cnt_2_mon_inout_perc = perc(contact_min_over_15s_rece_cnt_2_mon,
                                                              contact_min_over_15s_cnt_2_mon)

        contact_min_over_30s_call_cnt_2_mon_inout_perc = perc(contact_min_over_30s_call_cnt_2_mon,
                                                              contact_min_over_30s_cnt_2_mon)
        contact_min_over_30s_rece_cnt_2_mon_inout_perc = perc(contact_min_over_30s_rece_cnt_2_mon,
                                                              contact_min_over_30s_cnt_2_mon)

        contact_min_over_60s_call_cnt_2_mon_inout_perc = perc(contact_min_over_60s_call_cnt_2_mon,
                                                              contact_min_over_60s_cnt_2_mon)
        contact_min_over_60s_rece_cnt_2_mon_inout_perc = perc(contact_min_over_60s_rece_cnt_2_mon,
                                                              contact_min_over_60s_cnt_2_mon)

        contact_min_over_15s_call_cnt_1_mon_inout_perc = perc(contact_min_over_15s_call_cnt_1_mon,
                                                              contact_min_over_15s_cnt_1_mon)
        contact_min_over_15s_rece_cnt_1_mon_inout_perc = perc(contact_min_over_15s_rece_cnt_1_mon,
                                                              contact_min_over_15s_cnt_1_mon)

        contact_min_over_30s_call_cnt_1_mon_inout_perc = perc(contact_min_over_30s_call_cnt_1_mon,
                                                              contact_min_over_30s_cnt_1_mon)
        contact_min_over_30s_rece_cnt_1_mon_inout_perc = perc(contact_min_over_30s_rece_cnt_1_mon,
                                                              contact_min_over_30s_cnt_1_mon)

        contact_min_over_60s_call_cnt_1_mon_inout_perc = perc(contact_min_over_60s_call_cnt_1_mon,
                                                              contact_min_over_60s_cnt_1_mon)
        contact_min_over_60s_rece_cnt_1_mon_inout_perc = perc(contact_min_over_60s_rece_cnt_1_mon,
                                                              contact_min_over_60s_cnt_1_mon)

        contact_min_over_15s_call_cnt_2_wk_inout_perc = perc(contact_min_over_15s_call_cnt_2_wk,
                                                             contact_min_over_15s_cnt_2_wk)
        contact_min_over_15s_rece_cnt_2_wk_inout_perc = perc(contact_min_over_15s_rece_cnt_2_wk,
                                                             contact_min_over_15s_cnt_2_wk)

        contact_min_over_30s_call_cnt_2_wk_inout_perc = perc(contact_min_over_30s_call_cnt_2_wk,
                                                             contact_min_over_30s_cnt_2_wk)
        contact_min_over_30s_rece_cnt_2_wk_inout_perc = perc(contact_min_over_30s_rece_cnt_2_wk,
                                                             contact_min_over_30s_cnt_2_wk)

        contact_min_over_60s_call_cnt_2_wk_inout_perc = perc(contact_min_over_60s_call_cnt_2_wk,
                                                             contact_min_over_60s_cnt_2_wk)
        contact_min_over_60s_rece_cnt_2_wk_inout_perc = perc(contact_min_over_60s_rece_cnt_2_wk,
                                                             contact_min_over_60s_cnt_2_wk)

        # duration over 15s, 30s, 60s 6 mon perc
        contact_min_over_15s_cnt_3_mon_perc = perc(contact_min_over_15s_cnt_3_mon, contact_min_over_15s_cnt_6_mon)
        contact_min_over_15s_min_tot_3_mon_perc = perc(contact_min_over_15s_min_tot_3_mon,
                                                       contact_min_over_15s_min_tot_6_mon)
        contact_min_over_15s_call_cnt_3_mon_perc = perc(contact_min_over_15s_call_cnt_3_mon,
                                                        contact_min_over_15s_call_cnt_6_mon)
        contact_min_over_15s_call_min_tot_3_mon_perc = perc(contact_min_over_15s_call_min_tot_3_mon,
                                                            contact_min_over_15s_call_min_tot_6_mon)
        contact_min_over_15s_rece_cnt_3_mon_perc = perc(contact_min_over_15s_rece_cnt_3_mon,
                                                        contact_min_over_15s_rece_cnt_6_mon)
        contact_min_over_15s_rece_min_tot_3_mon_perc = perc(contact_min_over_15s_rece_min_tot_3_mon,
                                                            contact_min_over_15s_rece_min_tot_6_mon)

        contact_min_over_30s_cnt_3_mon_perc = perc(contact_min_over_30s_cnt_3_mon, contact_min_over_30s_cnt_6_mon)
        contact_min_over_30s_min_tot_3_mon_perc = perc(contact_min_over_30s_min_tot_3_mon,
                                                       contact_min_over_30s_min_tot_6_mon)
        contact_min_over_30s_call_cnt_3_mon_perc = perc(contact_min_over_30s_call_cnt_3_mon,
                                                        contact_min_over_30s_call_cnt_6_mon)
        contact_min_over_30s_call_min_tot_3_mon_perc = perc(contact_min_over_30s_call_min_tot_3_mon,
                                                            contact_min_over_30s_call_min_tot_6_mon)
        contact_min_over_30s_rece_cnt_3_mon_perc = perc(contact_min_over_30s_rece_cnt_3_mon,
                                                        contact_min_over_30s_rece_cnt_6_mon)
        contact_min_over_30s_rece_min_tot_3_mon_perc = perc(contact_min_over_30s_rece_min_tot_3_mon,
                                                            contact_min_over_30s_rece_min_tot_6_mon)

        contact_min_over_60s_cnt_3_mon_perc = perc(contact_min_over_60s_cnt_3_mon, contact_min_over_60s_cnt_6_mon)
        contact_min_over_60s_min_tot_3_mon_perc = perc(contact_min_over_60s_min_tot_3_mon,
                                                       contact_min_over_60s_min_tot_6_mon)
        contact_min_over_60s_call_cnt_3_mon_perc = perc(contact_min_over_60s_call_cnt_3_mon,
                                                        contact_min_over_60s_call_cnt_6_mon)
        contact_min_over_60s_call_min_tot_3_mon_perc = perc(contact_min_over_60s_call_min_tot_3_mon,
                                                            contact_min_over_60s_call_min_tot_6_mon)
        contact_min_over_60s_rece_cnt_3_mon_perc = perc(contact_min_over_60s_rece_cnt_3_mon,
                                                        contact_min_over_60s_rece_cnt_6_mon)
        contact_min_over_60s_rece_min_tot_3_mon_perc = perc(contact_min_over_60s_rece_min_tot_3_mon,
                                                            contact_min_over_60s_rece_min_tot_6_mon)

        contact_min_over_15s_cnt_2_mon_perc = perc(contact_min_over_15s_cnt_2_mon, contact_min_over_15s_cnt_6_mon)
        contact_min_over_15s_min_tot_2_mon_perc = perc(contact_min_over_15s_min_tot_2_mon,
                                                       contact_min_over_15s_min_tot_6_mon)
        contact_min_over_15s_call_cnt_2_mon_perc = perc(contact_min_over_15s_call_cnt_2_mon,
                                                        contact_min_over_15s_call_cnt_6_mon)
        contact_min_over_15s_call_min_tot_2_mon_perc = perc(contact_min_over_15s_call_min_tot_2_mon,
                                                            contact_min_over_15s_call_min_tot_6_mon)
        contact_min_over_15s_rece_cnt_2_mon_perc = perc(contact_min_over_15s_rece_cnt_2_mon,
                                                        contact_min_over_15s_rece_cnt_6_mon)
        contact_min_over_15s_rece_min_tot_2_mon_perc = perc(contact_min_over_15s_rece_min_tot_2_mon,
                                                            contact_min_over_15s_rece_min_tot_6_mon)

        contact_min_over_30s_cnt_2_mon_perc = perc(contact_min_over_30s_cnt_2_mon, contact_min_over_30s_cnt_6_mon)
        contact_min_over_30s_min_tot_2_mon_perc = perc(contact_min_over_30s_min_tot_2_mon,
                                                       contact_min_over_30s_min_tot_6_mon)
        contact_min_over_30s_call_cnt_2_mon_perc = perc(contact_min_over_30s_call_cnt_2_mon,
                                                        contact_min_over_30s_call_cnt_6_mon)
        contact_min_over_30s_call_min_tot_2_mon_perc = perc(contact_min_over_30s_call_min_tot_2_mon,
                                                            contact_min_over_30s_call_min_tot_6_mon)
        contact_min_over_30s_rece_cnt_2_mon_perc = perc(contact_min_over_30s_rece_cnt_2_mon,
                                                        contact_min_over_30s_rece_cnt_6_mon)
        contact_min_over_30s_rece_min_tot_2_mon_perc = perc(contact_min_over_30s_rece_min_tot_2_mon,
                                                            contact_min_over_30s_rece_min_tot_6_mon)

        contact_min_over_60s_cnt_2_mon_perc = perc(contact_min_over_60s_cnt_2_mon, contact_min_over_60s_cnt_6_mon)
        contact_min_over_60s_min_tot_2_mon_perc = perc(contact_min_over_60s_min_tot_2_mon,
                                                       contact_min_over_60s_min_tot_6_mon)
        contact_min_over_60s_call_cnt_2_mon_perc = perc(contact_min_over_60s_call_cnt_2_mon,
                                                        contact_min_over_60s_call_cnt_6_mon)
        contact_min_over_60s_call_min_tot_2_mon_perc = perc(contact_min_over_60s_call_min_tot_2_mon,
                                                            contact_min_over_60s_call_min_tot_6_mon)
        contact_min_over_60s_rece_cnt_2_mon_perc = perc(contact_min_over_60s_rece_cnt_2_mon,
                                                        contact_min_over_60s_rece_cnt_6_mon)
        contact_min_over_60s_rece_min_tot_2_mon_perc = perc(contact_min_over_60s_rece_min_tot_2_mon,
                                                            contact_min_over_60s_rece_min_tot_6_mon)

        contact_min_over_15s_cnt_1_mon_perc = perc(contact_min_over_15s_cnt_1_mon, contact_min_over_15s_cnt_6_mon)
        contact_min_over_15s_min_tot_1_mon_perc = perc(contact_min_over_15s_min_tot_1_mon,
                                                       contact_min_over_15s_min_tot_6_mon)
        contact_min_over_15s_call_cnt_1_mon_perc = perc(contact_min_over_15s_call_cnt_1_mon,
                                                        contact_min_over_15s_call_cnt_6_mon)
        contact_min_over_15s_call_min_tot_1_mon_perc = perc(contact_min_over_15s_call_min_tot_1_mon,
                                                            contact_min_over_15s_call_min_tot_6_mon)
        contact_min_over_15s_rece_cnt_1_mon_perc = perc(contact_min_over_15s_rece_cnt_1_mon,
                                                        contact_min_over_15s_rece_cnt_6_mon)
        contact_min_over_15s_rece_min_tot_1_mon_perc = perc(contact_min_over_15s_rece_min_tot_1_mon,
                                                            contact_min_over_15s_rece_min_tot_6_mon)

        contact_min_over_30s_cnt_1_mon_perc = perc(contact_min_over_30s_cnt_1_mon, contact_min_over_30s_cnt_6_mon)
        contact_min_over_30s_min_tot_1_mon_perc = perc(contact_min_over_30s_min_tot_1_mon,
                                                       contact_min_over_30s_min_tot_6_mon)
        contact_min_over_30s_call_cnt_1_mon_perc = perc(contact_min_over_30s_call_cnt_1_mon,
                                                        contact_min_over_30s_call_cnt_6_mon)
        contact_min_over_30s_call_min_tot_1_mon_perc = perc(contact_min_over_30s_call_min_tot_1_mon,
                                                            contact_min_over_30s_call_min_tot_6_mon)
        contact_min_over_30s_rece_cnt_1_mon_perc = perc(contact_min_over_30s_rece_cnt_1_mon,
                                                        contact_min_over_30s_rece_cnt_6_mon)
        contact_min_over_30s_rece_min_tot_1_mon_perc = perc(contact_min_over_30s_rece_min_tot_1_mon,
                                                            contact_min_over_30s_rece_min_tot_6_mon)

        contact_min_over_60s_cnt_1_mon_perc = perc(contact_min_over_60s_cnt_1_mon, contact_min_over_60s_cnt_6_mon)
        contact_min_over_60s_min_tot_1_mon_perc = perc(contact_min_over_60s_min_tot_1_mon,
                                                       contact_min_over_60s_min_tot_6_mon)
        contact_min_over_60s_call_cnt_1_mon_perc = perc(contact_min_over_60s_call_cnt_1_mon,
                                                        contact_min_over_60s_call_cnt_6_mon)
        contact_min_over_60s_call_min_tot_1_mon_perc = perc(contact_min_over_60s_call_min_tot_1_mon,
                                                            contact_min_over_60s_call_min_tot_6_mon)
        contact_min_over_60s_rece_cnt_1_mon_perc = perc(contact_min_over_60s_rece_cnt_1_mon,
                                                        contact_min_over_60s_rece_cnt_6_mon)
        contact_min_over_60s_rece_min_tot_1_mon_perc = perc(contact_min_over_60s_rece_min_tot_1_mon,
                                                            contact_min_over_60s_rece_min_tot_6_mon)

        contact_min_over_15s_cnt_2_wk_perc = perc(contact_min_over_15s_cnt_2_wk, contact_min_over_15s_cnt_6_mon)
        contact_min_over_15s_min_tot_2_wk_perc = perc(contact_min_over_15s_min_tot_2_wk,
                                                      contact_min_over_15s_min_tot_6_mon)
        contact_min_over_15s_call_cnt_2_wk_perc = perc(contact_min_over_15s_call_cnt_2_wk,
                                                       contact_min_over_15s_call_cnt_6_mon)
        contact_min_over_15s_call_min_tot_2_wk_perc = perc(contact_min_over_15s_call_min_tot_2_wk,
                                                           contact_min_over_15s_call_min_tot_6_mon)
        contact_min_over_15s_rece_cnt_2_wk_perc = perc(contact_min_over_15s_rece_cnt_2_wk,
                                                       contact_min_over_15s_rece_cnt_6_mon)
        contact_min_over_15s_rece_min_tot_2_wk_perc = perc(contact_min_over_15s_rece_min_tot_2_wk,
                                                           contact_min_over_15s_rece_min_tot_6_mon)

        contact_min_over_30s_cnt_2_wk_perc = perc(contact_min_over_30s_cnt_2_wk, contact_min_over_30s_cnt_6_mon)
        contact_min_over_30s_min_tot_2_wk_perc = perc(contact_min_over_30s_min_tot_2_wk,
                                                      contact_min_over_30s_min_tot_6_mon)
        contact_min_over_30s_call_cnt_2_wk_perc = perc(contact_min_over_30s_call_cnt_2_wk,
                                                       contact_min_over_30s_call_cnt_6_mon)
        contact_min_over_30s_call_min_tot_2_wk_perc = perc(contact_min_over_30s_call_min_tot_2_wk,
                                                           contact_min_over_30s_call_min_tot_6_mon)
        contact_min_over_30s_rece_cnt_2_wk_perc = perc(contact_min_over_30s_rece_cnt_2_wk,
                                                       contact_min_over_30s_rece_cnt_6_mon)
        contact_min_over_30s_rece_min_tot_2_wk_perc = perc(contact_min_over_30s_rece_min_tot_2_wk,
                                                           contact_min_over_30s_rece_min_tot_6_mon)

        contact_min_over_60s_cnt_2_wk_perc = perc(contact_min_over_60s_cnt_2_wk, contact_min_over_60s_cnt_6_mon)
        contact_min_over_60s_min_tot_2_wk_perc = perc(contact_min_over_60s_min_tot_2_wk,
                                                      contact_min_over_60s_min_tot_6_mon)
        contact_min_over_60s_call_cnt_2_wk_perc = perc(contact_min_over_60s_call_cnt_2_wk,
                                                       contact_min_over_60s_call_cnt_6_mon)
        contact_min_over_60s_call_min_tot_2_wk_perc = perc(contact_min_over_60s_call_min_tot_2_wk,
                                                           contact_min_over_60s_call_min_tot_6_mon)
        contact_min_over_60s_rece_cnt_2_wk_perc = perc(contact_min_over_60s_rece_cnt_2_wk,
                                                       contact_min_over_60s_rece_cnt_6_mon)
        contact_min_over_60s_rece_min_tot_2_wk_perc = perc(contact_min_over_60s_rece_min_tot_2_wk,
                                                           contact_min_over_60s_rece_min_tot_6_mon)

        # duration over 15s, 30s, 60s min perc
        contact_min_over_15s_cnt_min_perc = perc(contact_min_over_15s_cnt, contact_week_cnt)
        contact_min_over_15s_min_tot_min_perc = perc(contact_min_over_15s_min_tot, contact_week_min_tot)
        contact_min_over_15s_call_cnt_min_perc = perc(contact_min_over_15s_call_cnt, contact_week_call_cnt)
        contact_min_over_15s_call_min_tot_min_perc = perc(contact_min_over_15s_call_min_tot, contact_week_call_min_tot)
        contact_min_over_15s_rece_cnt_min_perc = perc(contact_min_over_15s_rece_cnt, contact_week_rece_cnt)
        contact_min_over_15s_rece_min_tot_min_perc = perc(contact_min_over_15s_rece_min_tot, contact_week_rece_min_tot)

        contact_min_over_30s_cnt_min_perc = perc(contact_min_over_30s_cnt, contact_week_cnt)
        contact_min_over_30s_min_tot_min_perc = perc(contact_min_over_30s_min_tot, contact_week_min_tot)
        contact_min_over_30s_call_cnt_min_perc = perc(contact_min_over_30s_call_cnt, contact_week_call_cnt)
        contact_min_over_30s_call_min_tot_min_perc = perc(contact_min_over_30s_call_min_tot, contact_week_call_min_tot)
        contact_min_over_30s_rece_cnt_min_perc = perc(contact_min_over_30s_rece_cnt, contact_week_rece_cnt)
        contact_min_over_30s_rece_min_tot_min_perc = perc(contact_min_over_30s_rece_min_tot, contact_week_rece_min_tot)

        contact_min_over_60s_cnt_min_perc = perc(contact_min_over_60s_cnt, contact_week_cnt)
        contact_min_over_60s_min_tot_min_perc = perc(contact_min_over_60s_min_tot, contact_week_min_tot)
        contact_min_over_60s_call_cnt_min_perc = perc(contact_min_over_60s_call_cnt, contact_week_call_cnt)
        contact_min_over_60s_call_min_tot_min_perc = perc(contact_min_over_60s_call_min_tot, contact_week_call_min_tot)
        contact_min_over_60s_rece_cnt_min_perc = perc(contact_min_over_60s_rece_cnt, contact_week_rece_cnt)
        contact_min_over_60s_rece_min_tot_min_perc = perc(contact_min_over_60s_rece_min_tot, contact_week_rece_min_tot)

        contact_min_over_15s_cnt_6_mon_min_perc = perc(contact_min_over_15s_cnt_6_mon, contact_week_cnt_6_mon)
        contact_min_over_15s_min_tot_6_mon_min_perc = perc(contact_min_over_15s_min_tot_6_mon,
                                                           contact_week_min_tot_6_mon)
        contact_min_over_15s_call_cnt_6_mon_min_perc = perc(contact_min_over_15s_call_cnt_6_mon,
                                                            contact_week_call_cnt_6_mon)
        contact_min_over_15s_call_min_tot_6_mon_min_perc = perc(contact_min_over_15s_call_min_tot_6_mon,
                                                                contact_week_call_min_tot_6_mon)
        contact_min_over_15s_rece_cnt_6_mon_min_perc = perc(contact_min_over_15s_rece_cnt_6_mon,
                                                            contact_week_rece_cnt_6_mon)
        contact_min_over_15s_rece_min_tot_6_mon_min_perc = perc(contact_min_over_15s_rece_min_tot_6_mon,
                                                                contact_week_rece_min_tot_6_mon)

        contact_min_over_30s_cnt_6_mon_min_perc = perc(contact_min_over_30s_cnt_6_mon, contact_week_cnt_6_mon)
        contact_min_over_30s_min_tot_6_mon_min_perc = perc(contact_min_over_30s_min_tot_6_mon,
                                                           contact_week_min_tot_6_mon)
        contact_min_over_30s_call_cnt_6_mon_min_perc = perc(contact_min_over_30s_call_cnt_6_mon,
                                                            contact_week_call_cnt_6_mon)
        contact_min_over_30s_call_min_tot_6_mon_min_perc = perc(contact_min_over_30s_call_min_tot_6_mon,
                                                                contact_week_call_min_tot_6_mon)
        contact_min_over_30s_rece_cnt_6_mon_min_perc = perc(contact_min_over_30s_rece_cnt_6_mon,
                                                            contact_week_rece_cnt_6_mon)
        contact_min_over_30s_rece_min_tot_6_mon_min_perc = perc(contact_min_over_30s_rece_min_tot_6_mon,
                                                                contact_week_rece_min_tot_6_mon)

        contact_min_over_60s_cnt_6_mon_min_perc = perc(contact_min_over_60s_cnt_6_mon, contact_week_cnt_6_mon)
        contact_min_over_60s_min_tot_6_mon_min_perc = perc(contact_min_over_60s_min_tot_6_mon,
                                                           contact_week_min_tot_6_mon)
        contact_min_over_60s_call_cnt_6_mon_min_perc = perc(contact_min_over_60s_call_cnt_6_mon,
                                                            contact_week_call_cnt_6_mon)
        contact_min_over_60s_call_min_tot_6_mon_min_perc = perc(contact_min_over_60s_call_min_tot_6_mon,
                                                                contact_week_call_min_tot_6_mon)
        contact_min_over_60s_rece_cnt_6_mon_min_perc = perc(contact_min_over_60s_rece_cnt_6_mon,
                                                            contact_week_rece_cnt_6_mon)
        contact_min_over_60s_rece_min_tot_6_mon_min_perc = perc(contact_min_over_60s_rece_min_tot_6_mon,
                                                                contact_week_rece_min_tot_6_mon)

        contact_min_over_15s_cnt_3_mon_min_perc = perc(contact_min_over_15s_cnt_3_mon, contact_week_cnt_3_mon)
        contact_min_over_15s_min_tot_3_mon_min_perc = perc(contact_min_over_15s_min_tot_3_mon,
                                                           contact_week_min_tot_3_mon)
        contact_min_over_15s_call_cnt_3_mon_min_perc = perc(contact_min_over_15s_call_cnt_3_mon,
                                                            contact_week_call_cnt_3_mon)
        contact_min_over_15s_call_min_tot_3_mon_min_perc = perc(contact_min_over_15s_call_min_tot_3_mon,
                                                                contact_week_call_min_tot_3_mon)
        contact_min_over_15s_rece_cnt_3_mon_min_perc = perc(contact_min_over_15s_rece_cnt_3_mon,
                                                            contact_week_rece_cnt_3_mon)
        contact_min_over_15s_rece_min_tot_3_mon_min_perc = perc(contact_min_over_15s_rece_min_tot_3_mon,
                                                                contact_week_rece_min_tot_3_mon)

        contact_min_over_30s_cnt_3_mon_min_perc = perc(contact_min_over_30s_cnt_3_mon, contact_week_cnt_3_mon)
        contact_min_over_30s_min_tot_3_mon_min_perc = perc(contact_min_over_30s_min_tot_3_mon,
                                                           contact_week_min_tot_3_mon)
        contact_min_over_30s_call_cnt_3_mon_min_perc = perc(contact_min_over_30s_call_cnt_3_mon,
                                                            contact_week_call_cnt_3_mon)
        contact_min_over_30s_call_min_tot_3_mon_min_perc = perc(contact_min_over_30s_call_min_tot_3_mon,
                                                                contact_week_call_min_tot_3_mon)
        contact_min_over_30s_rece_cnt_3_mon_min_perc = perc(contact_min_over_30s_rece_cnt_3_mon,
                                                            contact_week_rece_cnt_3_mon)
        contact_min_over_30s_rece_min_tot_3_mon_min_perc = perc(contact_min_over_30s_rece_min_tot_3_mon,
                                                                contact_week_rece_min_tot_3_mon)

        contact_min_over_60s_cnt_3_mon_min_perc = perc(contact_min_over_60s_cnt_3_mon, contact_week_cnt_3_mon)
        contact_min_over_60s_min_tot_3_mon_min_perc = perc(contact_min_over_60s_min_tot_3_mon,
                                                           contact_week_min_tot_3_mon)
        contact_min_over_60s_call_cnt_3_mon_min_perc = perc(contact_min_over_60s_call_cnt_3_mon,
                                                            contact_week_call_cnt_3_mon)
        contact_min_over_60s_call_min_tot_3_mon_min_perc = perc(contact_min_over_60s_call_min_tot_3_mon,
                                                                contact_week_call_min_tot_3_mon)
        contact_min_over_60s_rece_cnt_3_mon_min_perc = perc(contact_min_over_60s_rece_cnt_3_mon,
                                                            contact_week_rece_cnt_3_mon)
        contact_min_over_60s_rece_min_tot_3_mon_min_perc = perc(contact_min_over_60s_rece_min_tot_3_mon,
                                                                contact_week_rece_min_tot_3_mon)

        contact_min_over_15s_cnt_2_mon_min_perc = perc(contact_min_over_15s_cnt_2_mon, contact_week_cnt_2_mon)
        contact_min_over_15s_min_tot_2_mon_min_perc = perc(contact_min_over_15s_min_tot_2_mon,
                                                           contact_week_min_tot_2_mon)
        contact_min_over_15s_call_cnt_2_mon_min_perc = perc(contact_min_over_15s_call_cnt_2_mon,
                                                            contact_week_call_cnt_2_mon)
        contact_min_over_15s_call_min_tot_2_mon_min_perc = perc(contact_min_over_15s_call_min_tot_2_mon,
                                                                contact_week_call_min_tot_2_mon)
        contact_min_over_15s_rece_cnt_2_mon_min_perc = perc(contact_min_over_15s_rece_cnt_2_mon,
                                                            contact_week_rece_cnt_2_mon)
        contact_min_over_15s_rece_min_tot_2_mon_min_perc = perc(contact_min_over_15s_rece_min_tot_2_mon,
                                                                contact_week_rece_min_tot_2_mon)

        contact_min_over_30s_cnt_2_mon_min_perc = perc(contact_min_over_30s_cnt_2_mon, contact_week_cnt_2_mon)
        contact_min_over_30s_min_tot_2_mon_min_perc = perc(contact_min_over_30s_min_tot_2_mon,
                                                           contact_week_min_tot_2_mon)
        contact_min_over_30s_call_cnt_2_mon_min_perc = perc(contact_min_over_30s_call_cnt_2_mon,
                                                            contact_week_call_cnt_2_mon)
        contact_min_over_30s_call_min_tot_2_mon_min_perc = perc(contact_min_over_30s_call_min_tot_2_mon,
                                                                contact_week_call_min_tot_2_mon)
        contact_min_over_30s_rece_cnt_2_mon_min_perc = perc(contact_min_over_30s_rece_cnt_2_mon,
                                                            contact_week_rece_cnt_2_mon)
        contact_min_over_30s_rece_min_tot_2_mon_min_perc = perc(contact_min_over_30s_rece_min_tot_2_mon,
                                                                contact_week_rece_min_tot_2_mon)

        contact_min_over_60s_cnt_2_mon_min_perc = perc(contact_min_over_60s_cnt_2_mon, contact_week_cnt_2_mon)
        contact_min_over_60s_min_tot_2_mon_min_perc = perc(contact_min_over_60s_min_tot_2_mon,
                                                           contact_week_min_tot_2_mon)
        contact_min_over_60s_call_cnt_2_mon_min_perc = perc(contact_min_over_60s_call_cnt_2_mon,
                                                            contact_week_call_cnt_2_mon)
        contact_min_over_60s_call_min_tot_2_mon_min_perc = perc(contact_min_over_60s_call_min_tot_2_mon,
                                                                contact_week_call_min_tot_2_mon)
        contact_min_over_60s_rece_cnt_2_mon_min_perc = perc(contact_min_over_60s_rece_cnt_2_mon,
                                                            contact_week_rece_cnt_2_mon)
        contact_min_over_60s_rece_min_tot_2_mon_min_perc = perc(contact_min_over_60s_rece_min_tot_2_mon,
                                                                contact_week_rece_min_tot_2_mon)

        contact_min_over_15s_cnt_1_mon_min_perc = perc(contact_min_over_15s_cnt_1_mon, contact_week_cnt_1_mon)
        contact_min_over_15s_min_tot_1_mon_min_perc = perc(contact_min_over_15s_min_tot_1_mon,
                                                           contact_week_min_tot_1_mon)
        contact_min_over_15s_call_cnt_1_mon_min_perc = perc(contact_min_over_15s_call_cnt_1_mon,
                                                            contact_week_call_cnt_1_mon)
        contact_min_over_15s_call_min_tot_1_mon_min_perc = perc(contact_min_over_15s_call_min_tot_1_mon,
                                                                contact_week_call_min_tot_1_mon)
        contact_min_over_15s_rece_cnt_1_mon_min_perc = perc(contact_min_over_15s_rece_cnt_1_mon,
                                                            contact_week_rece_cnt_1_mon)
        contact_min_over_15s_rece_min_tot_1_mon_min_perc = perc(contact_min_over_15s_rece_min_tot_1_mon,
                                                                contact_week_rece_min_tot_1_mon)

        contact_min_over_30s_cnt_1_mon_min_perc = perc(contact_min_over_30s_cnt_1_mon, contact_week_cnt_1_mon)
        contact_min_over_30s_min_tot_1_mon_min_perc = perc(contact_min_over_30s_min_tot_1_mon,
                                                           contact_week_min_tot_1_mon)
        contact_min_over_30s_call_cnt_1_mon_min_perc = perc(contact_min_over_30s_call_cnt_1_mon,
                                                            contact_week_call_cnt_1_mon)
        contact_min_over_30s_call_min_tot_1_mon_min_perc = perc(contact_min_over_30s_call_min_tot_1_mon,
                                                                contact_week_call_min_tot_1_mon)
        contact_min_over_30s_rece_cnt_1_mon_min_perc = perc(contact_min_over_30s_rece_cnt_1_mon,
                                                            contact_week_rece_cnt_1_mon)
        contact_min_over_30s_rece_min_tot_1_mon_min_perc = perc(contact_min_over_30s_rece_min_tot_1_mon,
                                                                contact_week_rece_min_tot_1_mon)

        contact_min_over_60s_cnt_1_mon_min_perc = perc(contact_min_over_60s_cnt_1_mon, contact_week_cnt_1_mon)
        contact_min_over_60s_min_tot_1_mon_min_perc = perc(contact_min_over_60s_min_tot_1_mon,
                                                           contact_week_min_tot_1_mon)
        contact_min_over_60s_call_cnt_1_mon_min_perc = perc(contact_min_over_60s_call_cnt_1_mon,
                                                            contact_week_call_cnt_1_mon)
        contact_min_over_60s_call_min_tot_1_mon_min_perc = perc(contact_min_over_60s_call_min_tot_1_mon,
                                                                contact_week_call_min_tot_1_mon)
        contact_min_over_60s_rece_cnt_1_mon_min_perc = perc(contact_min_over_60s_rece_cnt_1_mon,
                                                            contact_week_rece_cnt_1_mon)
        contact_min_over_60s_rece_min_tot_1_mon_min_perc = perc(contact_min_over_60s_rece_min_tot_1_mon,
                                                                contact_week_rece_min_tot_1_mon)

        contact_min_over_15s_cnt_2_wk_min_perc = perc(contact_min_over_15s_cnt_2_wk, contact_week_cnt_2_wk)
        contact_min_over_15s_min_tot_2_wk_min_perc = perc(contact_min_over_15s_min_tot_2_wk, contact_week_min_tot_2_wk)
        contact_min_over_15s_call_cnt_2_wk_min_perc = perc(contact_min_over_15s_call_cnt_2_wk,
                                                           contact_week_call_cnt_2_wk)
        contact_min_over_15s_call_min_tot_2_wk_min_perc = perc(contact_min_over_15s_call_min_tot_2_wk,
                                                               contact_week_call_min_tot_2_wk)
        contact_min_over_15s_rece_cnt_2_wk_min_perc = perc(contact_min_over_15s_rece_cnt_2_wk,
                                                           contact_week_rece_cnt_2_wk)
        contact_min_over_15s_rece_min_tot_2_wk_min_perc = perc(contact_min_over_15s_rece_min_tot_2_wk,
                                                               contact_week_rece_min_tot_2_wk)

        contact_min_over_30s_cnt_2_wk_min_perc = perc(contact_min_over_30s_cnt_2_wk, contact_week_cnt_2_wk)
        contact_min_over_30s_min_tot_2_wk_min_perc = perc(contact_min_over_30s_min_tot_2_wk, contact_week_min_tot_2_wk)
        contact_min_over_30s_call_cnt_2_wk_min_perc = perc(contact_min_over_30s_call_cnt_2_wk,
                                                           contact_week_call_cnt_2_wk)
        contact_min_over_30s_call_min_tot_2_wk_min_perc = perc(contact_min_over_30s_call_min_tot_2_wk,
                                                               contact_week_call_min_tot_2_wk)
        contact_min_over_30s_rece_cnt_2_wk_min_perc = perc(contact_min_over_30s_rece_cnt_2_wk,
                                                           contact_week_rece_cnt_2_wk)
        contact_min_over_30s_rece_min_tot_2_wk_min_perc = perc(contact_min_over_30s_rece_min_tot_2_wk,
                                                               contact_week_rece_min_tot_2_wk)

        contact_min_over_60s_cnt_2_wk_min_perc = perc(contact_min_over_60s_cnt_2_wk, contact_week_cnt_2_wk)
        contact_min_over_60s_min_tot_2_wk_min_perc = perc(contact_min_over_60s_min_tot_2_wk, contact_week_min_tot_2_wk)
        contact_min_over_60s_call_cnt_2_wk_min_perc = perc(contact_min_over_60s_call_cnt_2_wk,
                                                           contact_week_call_cnt_2_wk)
        contact_min_over_60s_call_min_tot_2_wk_min_perc = perc(contact_min_over_60s_call_min_tot_2_wk,
                                                               contact_week_call_min_tot_2_wk)
        contact_min_over_60s_rece_cnt_2_wk_min_perc = perc(contact_min_over_60s_rece_cnt_2_wk,
                                                           contact_week_rece_cnt_2_wk)
        contact_min_over_60s_rece_min_tot_2_wk_min_perc = perc(contact_min_over_60s_rece_min_tot_2_wk,
                                                               contact_week_rece_min_tot_2_wk)

        contact_weekday_min_avg_2_wk_1_mon_diff = contact_weekday_min_avg_1_mon - contact_weekday_min_avg_2_wk
        contact_weekday_min_avg_1_mon_2_mon_diff = contact_weekday_min_avg_2_mon - contact_weekday_min_avg_1_mon
        contact_weekday_min_avg_2_mon_3_mon_diff = contact_weekday_min_avg_3_mon - contact_weekday_min_avg_2_mon
        contact_weekday_min_avg_3_mon_6_mon_diff = contact_weekday_min_avg_6_mon - contact_weekday_min_avg_3_mon

        contact_weekend_min_avg_2_wk_1_mon_diff = contact_weekend_min_avg_1_mon - contact_weekend_min_avg_2_wk
        contact_weekend_min_avg_1_mon_2_mon_diff = contact_weekend_min_avg_2_mon - contact_weekend_min_avg_1_mon
        contact_weekend_min_avg_2_mon_3_mon_diff = contact_weekend_min_avg_3_mon - contact_weekend_min_avg_2_mon
        contact_weekend_min_avg_3_mon_6_mon_diff = contact_weekend_min_avg_6_mon - contact_weekend_min_avg_3_mon

        contact_weekday_weekend_min_avg_diff = contact_weekday_min_avg - contact_weekend_min_avg

        contact_weekday_call_min_avg_2_wk_1_mon_diff = float(contact_weekday_call_min_tot_1_mon - contact_weekday_call_min_tot_2_wk)/1
        contact_weekday_call_min_avg_1_mon_2_mon_diff = float(contact_weekday_call_min_tot_2_mon - contact_weekday_call_min_tot_1_mon)/2
        contact_weekday_call_min_avg_2_mon_3_mon_diff = float(contact_weekday_call_min_tot_3_mon - contact_weekday_call_min_tot_2_mon)/3
        contact_weekday_call_min_avg_3_mon_6_mon_diff = float(contact_weekday_call_min_tot_6_mon - contact_weekday_call_min_tot_3_mon)/6

        contact_weekend_call_min_avg_2_wk_1_mon_diff = float(contact_weekend_call_min_tot_1_mon - contact_weekend_call_min_tot_2_wk)/1
        contact_weekend_call_min_avg_1_mon_2_mon_diff = float(contact_weekend_call_min_tot_2_mon - contact_weekend_call_min_tot_1_mon)/2
        contact_weekend_call_min_avg_2_mon_3_mon_diff = float(contact_weekend_call_min_tot_3_mon - contact_weekend_call_min_tot_2_mon)/3
        contact_weekend_call_min_avg_3_mon_6_mon_diff = float(contact_weekend_call_min_tot_6_mon - contact_weekend_call_min_tot_3_mon)/6

        contact_weekday_weekend_call_min_avg_diff = contact_weekday_call_min_avg - contact_weekend_call_min_avg

        contact_weekday_rece_min_avg_2_wk_1_mon_diff = float(contact_weekday_rece_min_tot_1_mon - contact_weekday_rece_min_tot_2_wk)/1
        contact_weekday_rece_min_avg_1_mon_2_mon_diff = float(contact_weekday_rece_min_tot_2_mon - contact_weekday_rece_min_tot_1_mon)/2
        contact_weekday_rece_min_avg_2_mon_3_mon_diff = float(contact_weekday_rece_min_tot_3_mon - contact_weekday_rece_min_tot_2_mon)/3
        contact_weekday_rece_min_avg_3_mon_6_mon_diff = float(contact_weekday_rece_min_tot_6_mon - contact_weekday_rece_min_tot_3_mon)/6

        contact_weekend_rece_min_avg_2_wk_1_mon_diff = float(contact_weekend_rece_min_tot_1_mon - contact_weekend_rece_min_tot_2_wk)/1
        contact_weekend_rece_min_avg_1_mon_2_mon_diff = float(contact_weekend_rece_min_tot_2_mon - contact_weekend_rece_min_tot_1_mon)/2
        contact_weekend_rece_min_avg_2_mon_3_mon_diff = float(contact_weekend_rece_min_tot_3_mon - contact_weekend_rece_min_tot_2_mon)/3
        contact_weekend_rece_min_avg_3_mon_6_mon_diff = float(contact_weekend_rece_min_tot_6_mon - contact_weekend_rece_min_tot_3_mon)/6

        contact_weekday_weekend_rece_min_avg_diff = contact_weekday_rece_min_avg - contact_weekend_rece_min_avg

        contact_week_call_rece_cnt_diff = contact_week_call_cnt - contact_week_rece_cnt
        contact_week_call_rece_min_tot_diff = contact_week_call_min_tot - contact_week_rece_min_tot
        contact_week_call_rece_cnt_6_mon_diff = contact_week_call_cnt_6_mon - contact_week_rece_cnt_6_mon
        contact_week_call_rece_cnt_3_mon_diff = contact_week_call_cnt_3_mon - contact_week_rece_cnt_3_mon
        contact_week_call_rece_cnt_2_mon_diff = contact_week_call_cnt_2_mon - contact_week_rece_cnt_2_mon
        contact_week_call_rece_cnt_1_mon_diff = contact_week_call_cnt_1_mon - contact_week_rece_cnt_1_mon

    return [contact_hour_0_cnt_6_mon, contact_hour_1_cnt_6_mon, contact_hour_2_cnt_6_mon, contact_hour_3_cnt_6_mon, contact_hour_4_cnt_6_mon, contact_hour_5_cnt_6_mon, contact_hour_6_cnt_6_mon, contact_hour_7_cnt_6_mon, contact_hour_8_cnt_6_mon, contact_hour_9_cnt_6_mon, contact_hour_10_cnt_6_mon, contact_hour_11_cnt_6_mon, contact_hour_12_cnt_6_mon, contact_hour_13_cnt_6_mon, contact_hour_14_cnt_6_mon, contact_hour_15_cnt_6_mon, contact_hour_16_cnt_6_mon, contact_hour_17_cnt_6_mon, contact_hour_18_cnt_6_mon, contact_hour_19_cnt_6_mon, contact_hour_20_cnt_6_mon, contact_hour_21_cnt_6_mon, contact_hour_22_cnt_6_mon, contact_hour_23_cnt_6_mon, contact_hour_0_min_tot_6_mon, contact_hour_1_min_tot_6_mon, contact_hour_2_min_tot_6_mon, contact_hour_3_min_tot_6_mon, contact_hour_4_min_tot_6_mon, contact_hour_5_min_tot_6_mon, contact_hour_6_min_tot_6_mon, contact_hour_7_min_tot_6_mon, contact_hour_8_min_tot_6_mon, contact_hour_9_min_tot_6_mon, contact_hour_10_min_tot_6_mon, contact_hour_11_min_tot_6_mon, contact_hour_12_min_tot_6_mon, contact_hour_13_min_tot_6_mon, contact_hour_14_min_tot_6_mon, contact_hour_15_min_tot_6_mon, contact_hour_16_min_tot_6_mon, contact_hour_17_min_tot_6_mon, contact_hour_18_min_tot_6_mon, contact_hour_19_min_tot_6_mon, contact_hour_20_min_tot_6_mon, contact_hour_21_min_tot_6_mon, contact_hour_22_min_tot_6_mon, contact_hour_23_min_tot_6_mon, contact_hour_0_call_cnt_6_mon, contact_hour_1_call_cnt_6_mon, contact_hour_2_call_cnt_6_mon, contact_hour_3_call_cnt_6_mon, contact_hour_4_call_cnt_6_mon, contact_hour_5_call_cnt_6_mon, contact_hour_6_call_cnt_6_mon, contact_hour_7_call_cnt_6_mon, contact_hour_8_call_cnt_6_mon, contact_hour_9_call_cnt_6_mon, contact_hour_10_call_cnt_6_mon, contact_hour_11_call_cnt_6_mon, contact_hour_12_call_cnt_6_mon, contact_hour_13_call_cnt_6_mon, contact_hour_14_call_cnt_6_mon, contact_hour_15_call_cnt_6_mon, contact_hour_16_call_cnt_6_mon, contact_hour_17_call_cnt_6_mon, contact_hour_18_call_cnt_6_mon, contact_hour_19_call_cnt_6_mon, contact_hour_20_call_cnt_6_mon, contact_hour_21_call_cnt_6_mon, contact_hour_22_call_cnt_6_mon, contact_hour_23_call_cnt_6_mon, contact_hour_0_call_min_tot_6_mon, contact_hour_1_call_min_tot_6_mon, contact_hour_2_call_min_tot_6_mon, contact_hour_3_call_min_tot_6_mon, contact_hour_4_call_min_tot_6_mon, contact_hour_5_call_min_tot_6_mon, contact_hour_6_call_min_tot_6_mon, contact_hour_7_call_min_tot_6_mon, contact_hour_8_call_min_tot_6_mon, contact_hour_9_call_min_tot_6_mon, contact_hour_10_call_min_tot_6_mon, contact_hour_11_call_min_tot_6_mon, contact_hour_12_call_min_tot_6_mon, contact_hour_13_call_min_tot_6_mon, contact_hour_14_call_min_tot_6_mon, contact_hour_15_call_min_tot_6_mon, contact_hour_16_call_min_tot_6_mon, contact_hour_17_call_min_tot_6_mon, contact_hour_18_call_min_tot_6_mon, contact_hour_19_call_min_tot_6_mon, contact_hour_20_call_min_tot_6_mon, contact_hour_21_call_min_tot_6_mon, contact_hour_22_call_min_tot_6_mon, contact_hour_23_call_min_tot_6_mon, contact_hour_0_rece_cnt_6_mon, contact_hour_1_rece_cnt_6_mon, contact_hour_2_rece_cnt_6_mon, contact_hour_3_rece_cnt_6_mon, contact_hour_4_rece_cnt_6_mon, contact_hour_5_rece_cnt_6_mon, contact_hour_6_rece_cnt_6_mon, contact_hour_7_rece_cnt_6_mon, contact_hour_8_rece_cnt_6_mon, contact_hour_9_rece_cnt_6_mon, contact_hour_10_rece_cnt_6_mon, contact_hour_11_rece_cnt_6_mon, contact_hour_12_rece_cnt_6_mon, contact_hour_13_rece_cnt_6_mon, contact_hour_14_rece_cnt_6_mon, contact_hour_15_rece_cnt_6_mon, contact_hour_16_rece_cnt_6_mon, contact_hour_17_rece_cnt_6_mon, contact_hour_18_rece_cnt_6_mon, contact_hour_19_rece_cnt_6_mon, contact_hour_20_rece_cnt_6_mon, contact_hour_21_rece_cnt_6_mon, contact_hour_22_rece_cnt_6_mon, contact_hour_23_rece_cnt_6_mon, contact_hour_0_rece_min_tot_6_mon, contact_hour_1_rece_min_tot_6_mon, contact_hour_2_rece_min_tot_6_mon, contact_hour_3_rece_min_tot_6_mon, contact_hour_4_rece_min_tot_6_mon, contact_hour_5_rece_min_tot_6_mon, contact_hour_6_rece_min_tot_6_mon, contact_hour_7_rece_min_tot_6_mon, contact_hour_8_rece_min_tot_6_mon, contact_hour_9_rece_min_tot_6_mon, contact_hour_10_rece_min_tot_6_mon, contact_hour_11_rece_min_tot_6_mon, contact_hour_12_rece_min_tot_6_mon, contact_hour_13_rece_min_tot_6_mon, contact_hour_14_rece_min_tot_6_mon, contact_hour_15_rece_min_tot_6_mon, contact_hour_16_rece_min_tot_6_mon, contact_hour_17_rece_min_tot_6_mon, contact_hour_18_rece_min_tot_6_mon, contact_hour_19_rece_min_tot_6_mon, contact_hour_20_rece_min_tot_6_mon, contact_hour_21_rece_min_tot_6_mon, contact_hour_22_rece_min_tot_6_mon, contact_hour_23_rece_min_tot_6_mon, contact_hour_0_cnt_3_mon, contact_hour_1_cnt_3_mon, contact_hour_2_cnt_3_mon, contact_hour_3_cnt_3_mon, contact_hour_4_cnt_3_mon, contact_hour_5_cnt_3_mon, contact_hour_6_cnt_3_mon, contact_hour_7_cnt_3_mon, contact_hour_8_cnt_3_mon, contact_hour_9_cnt_3_mon, contact_hour_10_cnt_3_mon, contact_hour_11_cnt_3_mon, contact_hour_12_cnt_3_mon, contact_hour_13_cnt_3_mon, contact_hour_14_cnt_3_mon, contact_hour_15_cnt_3_mon, contact_hour_16_cnt_3_mon, contact_hour_17_cnt_3_mon, contact_hour_18_cnt_3_mon, contact_hour_19_cnt_3_mon, contact_hour_20_cnt_3_mon, contact_hour_21_cnt_3_mon, contact_hour_22_cnt_3_mon, contact_hour_23_cnt_3_mon, contact_hour_0_min_tot_3_mon, contact_hour_1_min_tot_3_mon, contact_hour_2_min_tot_3_mon, contact_hour_3_min_tot_3_mon, contact_hour_4_min_tot_3_mon, contact_hour_5_min_tot_3_mon, contact_hour_6_min_tot_3_mon, contact_hour_7_min_tot_3_mon, contact_hour_8_min_tot_3_mon, contact_hour_9_min_tot_3_mon, contact_hour_10_min_tot_3_mon, contact_hour_11_min_tot_3_mon, contact_hour_12_min_tot_3_mon, contact_hour_13_min_tot_3_mon, contact_hour_14_min_tot_3_mon, contact_hour_15_min_tot_3_mon, contact_hour_16_min_tot_3_mon, contact_hour_17_min_tot_3_mon, contact_hour_18_min_tot_3_mon, contact_hour_19_min_tot_3_mon, contact_hour_20_min_tot_3_mon, contact_hour_21_min_tot_3_mon, contact_hour_22_min_tot_3_mon, contact_hour_23_min_tot_3_mon, contact_hour_0_call_cnt_3_mon, contact_hour_1_call_cnt_3_mon, contact_hour_2_call_cnt_3_mon, contact_hour_3_call_cnt_3_mon, contact_hour_4_call_cnt_3_mon, contact_hour_5_call_cnt_3_mon, contact_hour_6_call_cnt_3_mon, contact_hour_7_call_cnt_3_mon, contact_hour_8_call_cnt_3_mon, contact_hour_9_call_cnt_3_mon, contact_hour_10_call_cnt_3_mon, contact_hour_11_call_cnt_3_mon, contact_hour_12_call_cnt_3_mon, contact_hour_13_call_cnt_3_mon, contact_hour_14_call_cnt_3_mon, contact_hour_15_call_cnt_3_mon, contact_hour_16_call_cnt_3_mon, contact_hour_17_call_cnt_3_mon, contact_hour_18_call_cnt_3_mon, contact_hour_19_call_cnt_3_mon, contact_hour_20_call_cnt_3_mon, contact_hour_21_call_cnt_3_mon, contact_hour_22_call_cnt_3_mon, contact_hour_23_call_cnt_3_mon, contact_hour_0_call_min_tot_3_mon, contact_hour_1_call_min_tot_3_mon, contact_hour_2_call_min_tot_3_mon, contact_hour_3_call_min_tot_3_mon, contact_hour_4_call_min_tot_3_mon, contact_hour_5_call_min_tot_3_mon, contact_hour_6_call_min_tot_3_mon, contact_hour_7_call_min_tot_3_mon, contact_hour_8_call_min_tot_3_mon, contact_hour_9_call_min_tot_3_mon, contact_hour_10_call_min_tot_3_mon, contact_hour_11_call_min_tot_3_mon, contact_hour_12_call_min_tot_3_mon, contact_hour_13_call_min_tot_3_mon, contact_hour_14_call_min_tot_3_mon, contact_hour_15_call_min_tot_3_mon, contact_hour_16_call_min_tot_3_mon, contact_hour_17_call_min_tot_3_mon, contact_hour_18_call_min_tot_3_mon, contact_hour_19_call_min_tot_3_mon, contact_hour_20_call_min_tot_3_mon, contact_hour_21_call_min_tot_3_mon, contact_hour_22_call_min_tot_3_mon, contact_hour_23_call_min_tot_3_mon, contact_hour_0_rece_cnt_3_mon, contact_hour_1_rece_cnt_3_mon, contact_hour_2_rece_cnt_3_mon, contact_hour_3_rece_cnt_3_mon, contact_hour_4_rece_cnt_3_mon, contact_hour_5_rece_cnt_3_mon, contact_hour_6_rece_cnt_3_mon, contact_hour_7_rece_cnt_3_mon, contact_hour_8_rece_cnt_3_mon, contact_hour_9_rece_cnt_3_mon, contact_hour_10_rece_cnt_3_mon, contact_hour_11_rece_cnt_3_mon, contact_hour_12_rece_cnt_3_mon, contact_hour_13_rece_cnt_3_mon, contact_hour_14_rece_cnt_3_mon, contact_hour_15_rece_cnt_3_mon, contact_hour_16_rece_cnt_3_mon, contact_hour_17_rece_cnt_3_mon, contact_hour_18_rece_cnt_3_mon, contact_hour_19_rece_cnt_3_mon, contact_hour_20_rece_cnt_3_mon, contact_hour_21_rece_cnt_3_mon, contact_hour_22_rece_cnt_3_mon, contact_hour_23_rece_cnt_3_mon, contact_hour_0_rece_min_tot_3_mon, contact_hour_1_rece_min_tot_3_mon, contact_hour_2_rece_min_tot_3_mon, contact_hour_3_rece_min_tot_3_mon, contact_hour_4_rece_min_tot_3_mon, contact_hour_5_rece_min_tot_3_mon, contact_hour_6_rece_min_tot_3_mon, contact_hour_7_rece_min_tot_3_mon, contact_hour_8_rece_min_tot_3_mon, contact_hour_9_rece_min_tot_3_mon, contact_hour_10_rece_min_tot_3_mon, contact_hour_11_rece_min_tot_3_mon, contact_hour_12_rece_min_tot_3_mon, contact_hour_13_rece_min_tot_3_mon, contact_hour_14_rece_min_tot_3_mon, contact_hour_15_rece_min_tot_3_mon, contact_hour_16_rece_min_tot_3_mon, contact_hour_17_rece_min_tot_3_mon, contact_hour_18_rece_min_tot_3_mon, contact_hour_19_rece_min_tot_3_mon, contact_hour_20_rece_min_tot_3_mon, contact_hour_21_rece_min_tot_3_mon, contact_hour_22_rece_min_tot_3_mon, contact_hour_23_rece_min_tot_3_mon, contact_hour_0_cnt_2_mon, contact_hour_1_cnt_2_mon, contact_hour_2_cnt_2_mon, contact_hour_3_cnt_2_mon, contact_hour_4_cnt_2_mon, contact_hour_5_cnt_2_mon, contact_hour_6_cnt_2_mon, contact_hour_7_cnt_2_mon, contact_hour_8_cnt_2_mon, contact_hour_9_cnt_2_mon, contact_hour_10_cnt_2_mon, contact_hour_11_cnt_2_mon, contact_hour_12_cnt_2_mon, contact_hour_13_cnt_2_mon, contact_hour_14_cnt_2_mon, contact_hour_15_cnt_2_mon, contact_hour_16_cnt_2_mon, contact_hour_17_cnt_2_mon, contact_hour_18_cnt_2_mon, contact_hour_19_cnt_2_mon, contact_hour_20_cnt_2_mon, contact_hour_21_cnt_2_mon, contact_hour_22_cnt_2_mon, contact_hour_23_cnt_2_mon, contact_hour_0_min_tot_2_mon, contact_hour_1_min_tot_2_mon, contact_hour_2_min_tot_2_mon, contact_hour_3_min_tot_2_mon, contact_hour_4_min_tot_2_mon, contact_hour_5_min_tot_2_mon, contact_hour_6_min_tot_2_mon, contact_hour_7_min_tot_2_mon, contact_hour_8_min_tot_2_mon, contact_hour_9_min_tot_2_mon, contact_hour_10_min_tot_2_mon, contact_hour_11_min_tot_2_mon, contact_hour_12_min_tot_2_mon, contact_hour_13_min_tot_2_mon, contact_hour_14_min_tot_2_mon, contact_hour_15_min_tot_2_mon, contact_hour_16_min_tot_2_mon, contact_hour_17_min_tot_2_mon, contact_hour_18_min_tot_2_mon, contact_hour_19_min_tot_2_mon, contact_hour_20_min_tot_2_mon, contact_hour_21_min_tot_2_mon, contact_hour_22_min_tot_2_mon, contact_hour_23_min_tot_2_mon, contact_hour_0_call_cnt_2_mon, contact_hour_1_call_cnt_2_mon, contact_hour_2_call_cnt_2_mon, contact_hour_3_call_cnt_2_mon, contact_hour_4_call_cnt_2_mon, contact_hour_5_call_cnt_2_mon, contact_hour_6_call_cnt_2_mon, contact_hour_7_call_cnt_2_mon, contact_hour_8_call_cnt_2_mon, contact_hour_9_call_cnt_2_mon, contact_hour_10_call_cnt_2_mon, contact_hour_11_call_cnt_2_mon, contact_hour_12_call_cnt_2_mon, contact_hour_13_call_cnt_2_mon, contact_hour_14_call_cnt_2_mon, contact_hour_15_call_cnt_2_mon, contact_hour_16_call_cnt_2_mon, contact_hour_17_call_cnt_2_mon, contact_hour_18_call_cnt_2_mon, contact_hour_19_call_cnt_2_mon, contact_hour_20_call_cnt_2_mon, contact_hour_21_call_cnt_2_mon, contact_hour_22_call_cnt_2_mon, contact_hour_23_call_cnt_2_mon, contact_hour_0_call_min_tot_2_mon, contact_hour_1_call_min_tot_2_mon, contact_hour_2_call_min_tot_2_mon, contact_hour_3_call_min_tot_2_mon, contact_hour_4_call_min_tot_2_mon, contact_hour_5_call_min_tot_2_mon, contact_hour_6_call_min_tot_2_mon, contact_hour_7_call_min_tot_2_mon, contact_hour_8_call_min_tot_2_mon, contact_hour_9_call_min_tot_2_mon, contact_hour_10_call_min_tot_2_mon, contact_hour_11_call_min_tot_2_mon, contact_hour_12_call_min_tot_2_mon, contact_hour_13_call_min_tot_2_mon, contact_hour_14_call_min_tot_2_mon, contact_hour_15_call_min_tot_2_mon, contact_hour_16_call_min_tot_2_mon, contact_hour_17_call_min_tot_2_mon, contact_hour_18_call_min_tot_2_mon, contact_hour_19_call_min_tot_2_mon, contact_hour_20_call_min_tot_2_mon, contact_hour_21_call_min_tot_2_mon, contact_hour_22_call_min_tot_2_mon, contact_hour_23_call_min_tot_2_mon, contact_hour_0_rece_cnt_2_mon, contact_hour_1_rece_cnt_2_mon, contact_hour_2_rece_cnt_2_mon, contact_hour_3_rece_cnt_2_mon, contact_hour_4_rece_cnt_2_mon, contact_hour_5_rece_cnt_2_mon, contact_hour_6_rece_cnt_2_mon, contact_hour_7_rece_cnt_2_mon, contact_hour_8_rece_cnt_2_mon, contact_hour_9_rece_cnt_2_mon, contact_hour_10_rece_cnt_2_mon, contact_hour_11_rece_cnt_2_mon, contact_hour_12_rece_cnt_2_mon, contact_hour_13_rece_cnt_2_mon, contact_hour_14_rece_cnt_2_mon, contact_hour_15_rece_cnt_2_mon, contact_hour_16_rece_cnt_2_mon, contact_hour_17_rece_cnt_2_mon, contact_hour_18_rece_cnt_2_mon, contact_hour_19_rece_cnt_2_mon, contact_hour_20_rece_cnt_2_mon, contact_hour_21_rece_cnt_2_mon, contact_hour_22_rece_cnt_2_mon, contact_hour_23_rece_cnt_2_mon, contact_hour_0_rece_min_tot_2_mon, contact_hour_1_rece_min_tot_2_mon, contact_hour_2_rece_min_tot_2_mon, contact_hour_3_rece_min_tot_2_mon, contact_hour_4_rece_min_tot_2_mon, contact_hour_5_rece_min_tot_2_mon, contact_hour_6_rece_min_tot_2_mon, contact_hour_7_rece_min_tot_2_mon, contact_hour_8_rece_min_tot_2_mon, contact_hour_9_rece_min_tot_2_mon, contact_hour_10_rece_min_tot_2_mon, contact_hour_11_rece_min_tot_2_mon, contact_hour_12_rece_min_tot_2_mon, contact_hour_13_rece_min_tot_2_mon, contact_hour_14_rece_min_tot_2_mon, contact_hour_15_rece_min_tot_2_mon, contact_hour_16_rece_min_tot_2_mon, contact_hour_17_rece_min_tot_2_mon, contact_hour_18_rece_min_tot_2_mon, contact_hour_19_rece_min_tot_2_mon, contact_hour_20_rece_min_tot_2_mon, contact_hour_21_rece_min_tot_2_mon, contact_hour_22_rece_min_tot_2_mon, contact_hour_23_rece_min_tot_2_mon, contact_hour_0_cnt_1_mon, contact_hour_1_cnt_1_mon, contact_hour_2_cnt_1_mon, contact_hour_3_cnt_1_mon, contact_hour_4_cnt_1_mon, contact_hour_5_cnt_1_mon, contact_hour_6_cnt_1_mon, contact_hour_7_cnt_1_mon, contact_hour_8_cnt_1_mon, contact_hour_9_cnt_1_mon, contact_hour_10_cnt_1_mon, contact_hour_11_cnt_1_mon, contact_hour_12_cnt_1_mon, contact_hour_13_cnt_1_mon, contact_hour_14_cnt_1_mon, contact_hour_15_cnt_1_mon, contact_hour_16_cnt_1_mon, contact_hour_17_cnt_1_mon, contact_hour_18_cnt_1_mon, contact_hour_19_cnt_1_mon, contact_hour_20_cnt_1_mon, contact_hour_21_cnt_1_mon, contact_hour_22_cnt_1_mon, contact_hour_23_cnt_1_mon, contact_hour_0_min_tot_1_mon, contact_hour_1_min_tot_1_mon, contact_hour_2_min_tot_1_mon, contact_hour_3_min_tot_1_mon, contact_hour_4_min_tot_1_mon, contact_hour_5_min_tot_1_mon, contact_hour_6_min_tot_1_mon, contact_hour_7_min_tot_1_mon, contact_hour_8_min_tot_1_mon, contact_hour_9_min_tot_1_mon, contact_hour_10_min_tot_1_mon, contact_hour_11_min_tot_1_mon, contact_hour_12_min_tot_1_mon, contact_hour_13_min_tot_1_mon, contact_hour_14_min_tot_1_mon, contact_hour_15_min_tot_1_mon, contact_hour_16_min_tot_1_mon, contact_hour_17_min_tot_1_mon, contact_hour_18_min_tot_1_mon, contact_hour_19_min_tot_1_mon, contact_hour_20_min_tot_1_mon, contact_hour_21_min_tot_1_mon, contact_hour_22_min_tot_1_mon, contact_hour_23_min_tot_1_mon, contact_hour_0_call_cnt_1_mon, contact_hour_1_call_cnt_1_mon, contact_hour_2_call_cnt_1_mon, contact_hour_3_call_cnt_1_mon, contact_hour_4_call_cnt_1_mon, contact_hour_5_call_cnt_1_mon, contact_hour_6_call_cnt_1_mon, contact_hour_7_call_cnt_1_mon, contact_hour_8_call_cnt_1_mon, contact_hour_9_call_cnt_1_mon, contact_hour_10_call_cnt_1_mon, contact_hour_11_call_cnt_1_mon, contact_hour_12_call_cnt_1_mon, contact_hour_13_call_cnt_1_mon, contact_hour_14_call_cnt_1_mon, contact_hour_15_call_cnt_1_mon, contact_hour_16_call_cnt_1_mon, contact_hour_17_call_cnt_1_mon, contact_hour_18_call_cnt_1_mon, contact_hour_19_call_cnt_1_mon, contact_hour_20_call_cnt_1_mon, contact_hour_21_call_cnt_1_mon, contact_hour_22_call_cnt_1_mon, contact_hour_23_call_cnt_1_mon, contact_hour_0_call_min_tot_1_mon, contact_hour_1_call_min_tot_1_mon, contact_hour_2_call_min_tot_1_mon, contact_hour_3_call_min_tot_1_mon, contact_hour_4_call_min_tot_1_mon, contact_hour_5_call_min_tot_1_mon, contact_hour_6_call_min_tot_1_mon, contact_hour_7_call_min_tot_1_mon, contact_hour_8_call_min_tot_1_mon, contact_hour_9_call_min_tot_1_mon, contact_hour_10_call_min_tot_1_mon, contact_hour_11_call_min_tot_1_mon, contact_hour_12_call_min_tot_1_mon, contact_hour_13_call_min_tot_1_mon, contact_hour_14_call_min_tot_1_mon, contact_hour_15_call_min_tot_1_mon, contact_hour_16_call_min_tot_1_mon, contact_hour_17_call_min_tot_1_mon, contact_hour_18_call_min_tot_1_mon, contact_hour_19_call_min_tot_1_mon, contact_hour_20_call_min_tot_1_mon, contact_hour_21_call_min_tot_1_mon, contact_hour_22_call_min_tot_1_mon, contact_hour_23_call_min_tot_1_mon, contact_hour_0_rece_cnt_1_mon, contact_hour_1_rece_cnt_1_mon, contact_hour_2_rece_cnt_1_mon, contact_hour_3_rece_cnt_1_mon, contact_hour_4_rece_cnt_1_mon, contact_hour_5_rece_cnt_1_mon, contact_hour_6_rece_cnt_1_mon, contact_hour_7_rece_cnt_1_mon, contact_hour_8_rece_cnt_1_mon, contact_hour_9_rece_cnt_1_mon, contact_hour_10_rece_cnt_1_mon, contact_hour_11_rece_cnt_1_mon, contact_hour_12_rece_cnt_1_mon, contact_hour_13_rece_cnt_1_mon, contact_hour_14_rece_cnt_1_mon, contact_hour_15_rece_cnt_1_mon, contact_hour_16_rece_cnt_1_mon, contact_hour_17_rece_cnt_1_mon, contact_hour_18_rece_cnt_1_mon, contact_hour_19_rece_cnt_1_mon, contact_hour_20_rece_cnt_1_mon, contact_hour_21_rece_cnt_1_mon, contact_hour_22_rece_cnt_1_mon, contact_hour_23_rece_cnt_1_mon, contact_hour_0_rece_min_tot_1_mon, contact_hour_1_rece_min_tot_1_mon, contact_hour_2_rece_min_tot_1_mon, contact_hour_3_rece_min_tot_1_mon, contact_hour_4_rece_min_tot_1_mon, contact_hour_5_rece_min_tot_1_mon, contact_hour_6_rece_min_tot_1_mon, contact_hour_7_rece_min_tot_1_mon, contact_hour_8_rece_min_tot_1_mon, contact_hour_9_rece_min_tot_1_mon, contact_hour_10_rece_min_tot_1_mon, contact_hour_11_rece_min_tot_1_mon, contact_hour_12_rece_min_tot_1_mon, contact_hour_13_rece_min_tot_1_mon, contact_hour_14_rece_min_tot_1_mon, contact_hour_15_rece_min_tot_1_mon, contact_hour_16_rece_min_tot_1_mon, contact_hour_17_rece_min_tot_1_mon, contact_hour_18_rece_min_tot_1_mon, contact_hour_19_rece_min_tot_1_mon, contact_hour_20_rece_min_tot_1_mon, contact_hour_21_rece_min_tot_1_mon, contact_hour_22_rece_min_tot_1_mon, contact_hour_23_rece_min_tot_1_mon, contact_hour_0_cnt_2_wk, contact_hour_1_cnt_2_wk, contact_hour_2_cnt_2_wk, contact_hour_3_cnt_2_wk, contact_hour_4_cnt_2_wk, contact_hour_5_cnt_2_wk, contact_hour_6_cnt_2_wk, contact_hour_7_cnt_2_wk, contact_hour_8_cnt_2_wk, contact_hour_9_cnt_2_wk, contact_hour_10_cnt_2_wk, contact_hour_11_cnt_2_wk, contact_hour_12_cnt_2_wk, contact_hour_13_cnt_2_wk, contact_hour_14_cnt_2_wk, contact_hour_15_cnt_2_wk, contact_hour_16_cnt_2_wk, contact_hour_17_cnt_2_wk, contact_hour_18_cnt_2_wk, contact_hour_19_cnt_2_wk, contact_hour_20_cnt_2_wk, contact_hour_21_cnt_2_wk, contact_hour_22_cnt_2_wk, contact_hour_23_cnt_2_wk, contact_hour_0_min_tot_2_wk, contact_hour_1_min_tot_2_wk, contact_hour_2_min_tot_2_wk, contact_hour_3_min_tot_2_wk, contact_hour_4_min_tot_2_wk, contact_hour_5_min_tot_2_wk, contact_hour_6_min_tot_2_wk, contact_hour_7_min_tot_2_wk, contact_hour_8_min_tot_2_wk, contact_hour_9_min_tot_2_wk, contact_hour_10_min_tot_2_wk, contact_hour_11_min_tot_2_wk, contact_hour_12_min_tot_2_wk, contact_hour_13_min_tot_2_wk, contact_hour_14_min_tot_2_wk, contact_hour_15_min_tot_2_wk, contact_hour_16_min_tot_2_wk, contact_hour_17_min_tot_2_wk, contact_hour_18_min_tot_2_wk, contact_hour_19_min_tot_2_wk, contact_hour_20_min_tot_2_wk, contact_hour_21_min_tot_2_wk, contact_hour_22_min_tot_2_wk, contact_hour_23_min_tot_2_wk, contact_hour_0_call_cnt_2_wk, contact_hour_1_call_cnt_2_wk, contact_hour_2_call_cnt_2_wk, contact_hour_3_call_cnt_2_wk, contact_hour_4_call_cnt_2_wk, contact_hour_5_call_cnt_2_wk, contact_hour_6_call_cnt_2_wk, contact_hour_7_call_cnt_2_wk, contact_hour_8_call_cnt_2_wk, contact_hour_9_call_cnt_2_wk, contact_hour_10_call_cnt_2_wk, contact_hour_11_call_cnt_2_wk, contact_hour_12_call_cnt_2_wk, contact_hour_13_call_cnt_2_wk, contact_hour_14_call_cnt_2_wk, contact_hour_15_call_cnt_2_wk, contact_hour_16_call_cnt_2_wk, contact_hour_17_call_cnt_2_wk, contact_hour_18_call_cnt_2_wk, contact_hour_19_call_cnt_2_wk, contact_hour_20_call_cnt_2_wk, contact_hour_21_call_cnt_2_wk, contact_hour_22_call_cnt_2_wk, contact_hour_23_call_cnt_2_wk, contact_hour_0_call_min_tot_2_wk, contact_hour_1_call_min_tot_2_wk, contact_hour_2_call_min_tot_2_wk, contact_hour_3_call_min_tot_2_wk, contact_hour_4_call_min_tot_2_wk, contact_hour_5_call_min_tot_2_wk, contact_hour_6_call_min_tot_2_wk, contact_hour_7_call_min_tot_2_wk, contact_hour_8_call_min_tot_2_wk, contact_hour_9_call_min_tot_2_wk, contact_hour_10_call_min_tot_2_wk, contact_hour_11_call_min_tot_2_wk, contact_hour_12_call_min_tot_2_wk, contact_hour_13_call_min_tot_2_wk, contact_hour_14_call_min_tot_2_wk, contact_hour_15_call_min_tot_2_wk, contact_hour_16_call_min_tot_2_wk, contact_hour_17_call_min_tot_2_wk, contact_hour_18_call_min_tot_2_wk, contact_hour_19_call_min_tot_2_wk, contact_hour_20_call_min_tot_2_wk, contact_hour_21_call_min_tot_2_wk, contact_hour_22_call_min_tot_2_wk, contact_hour_23_call_min_tot_2_wk, contact_hour_0_rece_cnt_2_wk, contact_hour_1_rece_cnt_2_wk, contact_hour_2_rece_cnt_2_wk, contact_hour_3_rece_cnt_2_wk, contact_hour_4_rece_cnt_2_wk, contact_hour_5_rece_cnt_2_wk, contact_hour_6_rece_cnt_2_wk, contact_hour_7_rece_cnt_2_wk, contact_hour_8_rece_cnt_2_wk, contact_hour_9_rece_cnt_2_wk, contact_hour_10_rece_cnt_2_wk, contact_hour_11_rece_cnt_2_wk, contact_hour_12_rece_cnt_2_wk, contact_hour_13_rece_cnt_2_wk, contact_hour_14_rece_cnt_2_wk, contact_hour_15_rece_cnt_2_wk, contact_hour_16_rece_cnt_2_wk, contact_hour_17_rece_cnt_2_wk, contact_hour_18_rece_cnt_2_wk, contact_hour_19_rece_cnt_2_wk, contact_hour_20_rece_cnt_2_wk, contact_hour_21_rece_cnt_2_wk, contact_hour_22_rece_cnt_2_wk, contact_hour_23_rece_cnt_2_wk, contact_hour_0_rece_min_tot_2_wk, contact_hour_1_rece_min_tot_2_wk, contact_hour_2_rece_min_tot_2_wk, contact_hour_3_rece_min_tot_2_wk, contact_hour_4_rece_min_tot_2_wk, contact_hour_5_rece_min_tot_2_wk, contact_hour_6_rece_min_tot_2_wk, contact_hour_7_rece_min_tot_2_wk, contact_hour_8_rece_min_tot_2_wk, contact_hour_9_rece_min_tot_2_wk, contact_hour_10_rece_min_tot_2_wk, contact_hour_11_rece_min_tot_2_wk, contact_hour_12_rece_min_tot_2_wk, contact_hour_13_rece_min_tot_2_wk, contact_hour_14_rece_min_tot_2_wk, contact_hour_15_rece_min_tot_2_wk, contact_hour_16_rece_min_tot_2_wk, contact_hour_17_rece_min_tot_2_wk, contact_hour_18_rece_min_tot_2_wk, contact_hour_19_rece_min_tot_2_wk, contact_hour_20_rece_min_tot_2_wk, contact_hour_21_rece_min_tot_2_wk, contact_hour_22_rece_min_tot_2_wk, contact_hour_23_rece_min_tot_2_wk, contact_hour_0_cnt, contact_hour_1_cnt, contact_hour_2_cnt, contact_hour_3_cnt, contact_hour_4_cnt, contact_hour_5_cnt, contact_hour_6_cnt, contact_hour_7_cnt, contact_hour_8_cnt, contact_hour_9_cnt, contact_hour_10_cnt, contact_hour_11_cnt, contact_hour_12_cnt, contact_hour_13_cnt, contact_hour_14_cnt, contact_hour_15_cnt, contact_hour_16_cnt, contact_hour_17_cnt, contact_hour_18_cnt, contact_hour_19_cnt, contact_hour_20_cnt, contact_hour_21_cnt, contact_hour_22_cnt, contact_hour_23_cnt, contact_hour_0_min_tot, contact_hour_1_min_tot, contact_hour_2_min_tot, contact_hour_3_min_tot, contact_hour_4_min_tot, contact_hour_5_min_tot, contact_hour_6_min_tot, contact_hour_7_min_tot, contact_hour_8_min_tot, contact_hour_9_min_tot, contact_hour_10_min_tot, contact_hour_11_min_tot, contact_hour_12_min_tot, contact_hour_13_min_tot, contact_hour_14_min_tot, contact_hour_15_min_tot, contact_hour_16_min_tot, contact_hour_17_min_tot, contact_hour_18_min_tot, contact_hour_19_min_tot, contact_hour_20_min_tot, contact_hour_21_min_tot, contact_hour_22_min_tot, contact_hour_23_min_tot, contact_hour_0_call_cnt, contact_hour_1_call_cnt, contact_hour_2_call_cnt, contact_hour_3_call_cnt, contact_hour_4_call_cnt, contact_hour_5_call_cnt, contact_hour_6_call_cnt, contact_hour_7_call_cnt, contact_hour_8_call_cnt, contact_hour_9_call_cnt, contact_hour_10_call_cnt, contact_hour_11_call_cnt, contact_hour_12_call_cnt, contact_hour_13_call_cnt, contact_hour_14_call_cnt, contact_hour_15_call_cnt, contact_hour_16_call_cnt, contact_hour_17_call_cnt, contact_hour_18_call_cnt, contact_hour_19_call_cnt, contact_hour_20_call_cnt, contact_hour_21_call_cnt, contact_hour_22_call_cnt, contact_hour_23_call_cnt, contact_hour_0_call_min_tot, contact_hour_1_call_min_tot, contact_hour_2_call_min_tot, contact_hour_3_call_min_tot, contact_hour_4_call_min_tot, contact_hour_5_call_min_tot, contact_hour_6_call_min_tot, contact_hour_7_call_min_tot, contact_hour_8_call_min_tot, contact_hour_9_call_min_tot, contact_hour_10_call_min_tot, contact_hour_11_call_min_tot, contact_hour_12_call_min_tot, contact_hour_13_call_min_tot, contact_hour_14_call_min_tot, contact_hour_15_call_min_tot, contact_hour_16_call_min_tot, contact_hour_17_call_min_tot, contact_hour_18_call_min_tot, contact_hour_19_call_min_tot, contact_hour_20_call_min_tot, contact_hour_21_call_min_tot, contact_hour_22_call_min_tot, contact_hour_23_call_min_tot, contact_hour_0_rece_cnt, contact_hour_1_rece_cnt, contact_hour_2_rece_cnt, contact_hour_3_rece_cnt, contact_hour_4_rece_cnt, contact_hour_5_rece_cnt, contact_hour_6_rece_cnt, contact_hour_7_rece_cnt, contact_hour_8_rece_cnt, contact_hour_9_rece_cnt, contact_hour_10_rece_cnt, contact_hour_11_rece_cnt, contact_hour_12_rece_cnt, contact_hour_13_rece_cnt, contact_hour_14_rece_cnt, contact_hour_15_rece_cnt, contact_hour_16_rece_cnt, contact_hour_17_rece_cnt, contact_hour_18_rece_cnt, contact_hour_19_rece_cnt, contact_hour_20_rece_cnt, contact_hour_21_rece_cnt, contact_hour_22_rece_cnt, contact_hour_23_rece_cnt, contact_hour_0_rece_min_tot, contact_hour_1_rece_min_tot, contact_hour_2_rece_min_tot, contact_hour_3_rece_min_tot, contact_hour_4_rece_min_tot, contact_hour_5_rece_min_tot, contact_hour_6_rece_min_tot, contact_hour_7_rece_min_tot, contact_hour_8_rece_min_tot, contact_hour_9_rece_min_tot, contact_hour_10_rece_min_tot, contact_hour_11_rece_min_tot, contact_hour_12_rece_min_tot, contact_hour_13_rece_min_tot, contact_hour_14_rece_min_tot, contact_hour_15_rece_min_tot, contact_hour_16_rece_min_tot, contact_hour_17_rece_min_tot, contact_hour_18_rece_min_tot, contact_hour_19_rece_min_tot, contact_hour_20_rece_min_tot, contact_hour_21_rece_min_tot, contact_hour_22_rece_min_tot, contact_hour_23_rece_min_tot, contact_weekday_cnt, contact_weekday_min_tot, contact_weekday_call_cnt, contact_weekday_call_min_tot, contact_weekday_rece_cnt, contact_weekday_rece_min_tot, contact_weekend_cnt, contact_weekend_min_tot, contact_weekend_call_cnt, contact_weekend_call_min_tot, contact_weekend_rece_cnt, contact_weekend_rece_min_tot, contact_weekday_cnt_6_mon, contact_weekday_min_tot_6_mon, contact_weekday_call_cnt_6_mon, contact_weekday_call_min_tot_6_mon, contact_weekday_rece_cnt_6_mon, contact_weekday_rece_min_tot_6_mon, contact_weekend_cnt_6_mon, contact_weekend_min_tot_6_mon, contact_weekend_call_cnt_6_mon, contact_weekend_call_min_tot_6_mon, contact_weekend_rece_cnt_6_mon, contact_weekend_rece_min_tot_6_mon, contact_weekday_cnt_3_mon, contact_weekday_min_tot_3_mon, contact_weekday_call_cnt_3_mon, contact_weekday_call_min_tot_3_mon, contact_weekday_rece_cnt_3_mon, contact_weekday_rece_min_tot_3_mon, contact_weekend_cnt_3_mon, contact_weekend_min_tot_3_mon, contact_weekend_call_cnt_3_mon, contact_weekend_call_min_tot_3_mon, contact_weekend_rece_cnt_3_mon, contact_weekend_rece_min_tot_3_mon, contact_weekday_cnt_2_mon, contact_weekday_min_tot_2_mon, contact_weekday_call_cnt_2_mon, contact_weekday_call_min_tot_2_mon, contact_weekday_rece_cnt_2_mon, contact_weekday_rece_min_tot_2_mon, contact_weekend_cnt_2_mon, contact_weekend_min_tot_2_mon, contact_weekend_call_cnt_2_mon, contact_weekend_call_min_tot_2_mon, contact_weekend_rece_cnt_2_mon, contact_weekend_rece_min_tot_2_mon, contact_weekday_cnt_1_mon, contact_weekday_min_tot_1_mon, contact_weekday_call_cnt_1_mon, contact_weekday_call_min_tot_1_mon, contact_weekday_rece_cnt_1_mon, contact_weekday_rece_min_tot_1_mon, contact_weekend_cnt_1_mon, contact_weekend_min_tot_1_mon, contact_weekend_call_cnt_1_mon, contact_weekend_call_min_tot_1_mon, contact_weekend_rece_cnt_1_mon, contact_weekend_rece_min_tot_1_mon, contact_weekday_cnt_2_wk, contact_weekday_min_tot_2_wk, contact_weekday_call_cnt_2_wk, contact_weekday_call_min_tot_2_wk, contact_weekday_rece_cnt_2_wk, contact_weekday_rece_min_tot_2_wk, contact_weekend_cnt_2_wk, contact_weekend_min_tot_2_wk, contact_weekend_call_cnt_2_wk, contact_weekend_call_min_tot_2_wk, contact_weekend_rece_cnt_2_wk, contact_weekend_rece_min_tot_2_wk, contact_min_over_15s_cnt, contact_min_over_15s_min_tot, contact_min_over_15s_call_cnt, contact_min_over_15s_call_min_tot, contact_min_over_15s_rece_cnt, contact_min_over_15s_rece_min_tot, contact_min_over_30s_cnt, contact_min_over_30s_min_tot, contact_min_over_30s_call_cnt, contact_min_over_30s_call_min_tot, contact_min_over_30s_rece_cnt, contact_min_over_30s_rece_min_tot, contact_min_over_60s_cnt, contact_min_over_60s_min_tot, contact_min_over_60s_call_cnt, contact_min_over_60s_call_min_tot, contact_min_over_60s_rece_cnt, contact_min_over_60s_rece_min_tot, contact_min_over_15s_cnt_6_mon, contact_min_over_15s_min_tot_6_mon, contact_min_over_15s_call_cnt_6_mon, contact_min_over_15s_call_min_tot_6_mon, contact_min_over_15s_rece_cnt_6_mon, contact_min_over_15s_rece_min_tot_6_mon, contact_min_over_30s_cnt_6_mon, contact_min_over_30s_min_tot_6_mon, contact_min_over_30s_call_cnt_6_mon, contact_min_over_30s_call_min_tot_6_mon, contact_min_over_30s_rece_cnt_6_mon, contact_min_over_30s_rece_min_tot_6_mon, contact_min_over_60s_cnt_6_mon, contact_min_over_60s_min_tot_6_mon, contact_min_over_60s_call_cnt_6_mon, contact_min_over_60s_call_min_tot_6_mon, contact_min_over_60s_rece_cnt_6_mon, contact_min_over_60s_rece_min_tot_6_mon, contact_min_over_15s_cnt_3_mon, contact_min_over_15s_min_tot_3_mon, contact_min_over_15s_call_cnt_3_mon, contact_min_over_15s_call_min_tot_3_mon, contact_min_over_15s_rece_cnt_3_mon, contact_min_over_15s_rece_min_tot_3_mon, contact_min_over_30s_cnt_3_mon, contact_min_over_30s_min_tot_3_mon, contact_min_over_30s_call_cnt_3_mon, contact_min_over_30s_call_min_tot_3_mon, contact_min_over_30s_rece_cnt_3_mon, contact_min_over_30s_rece_min_tot_3_mon, contact_min_over_60s_cnt_3_mon, contact_min_over_60s_min_tot_3_mon, contact_min_over_60s_call_cnt_3_mon, contact_min_over_60s_call_min_tot_3_mon, contact_min_over_60s_rece_cnt_3_mon, contact_min_over_60s_rece_min_tot_3_mon, contact_min_over_15s_cnt_2_mon, contact_min_over_15s_min_tot_2_mon, contact_min_over_15s_call_cnt_2_mon, contact_min_over_15s_call_min_tot_2_mon, contact_min_over_15s_rece_cnt_2_mon, contact_min_over_15s_rece_min_tot_2_mon, contact_min_over_30s_cnt_2_mon, contact_min_over_30s_min_tot_2_mon, contact_min_over_30s_call_cnt_2_mon, contact_min_over_30s_call_min_tot_2_mon, contact_min_over_30s_rece_cnt_2_mon, contact_min_over_30s_rece_min_tot_2_mon, contact_min_over_60s_cnt_2_mon, contact_min_over_60s_min_tot_2_mon, contact_min_over_60s_call_cnt_2_mon, contact_min_over_60s_call_min_tot_2_mon, contact_min_over_60s_rece_cnt_2_mon, contact_min_over_60s_rece_min_tot_2_mon, contact_min_over_15s_cnt_1_mon, contact_min_over_15s_min_tot_1_mon, contact_min_over_15s_call_cnt_1_mon, contact_min_over_15s_call_min_tot_1_mon, contact_min_over_15s_rece_cnt_1_mon, contact_min_over_15s_rece_min_tot_1_mon, contact_min_over_30s_cnt_1_mon, contact_min_over_30s_min_tot_1_mon, contact_min_over_30s_call_cnt_1_mon, contact_min_over_30s_call_min_tot_1_mon, contact_min_over_30s_rece_cnt_1_mon, contact_min_over_30s_rece_min_tot_1_mon, contact_min_over_60s_cnt_1_mon, contact_min_over_60s_min_tot_1_mon, contact_min_over_60s_call_cnt_1_mon, contact_min_over_60s_call_min_tot_1_mon, contact_min_over_60s_rece_cnt_1_mon, contact_min_over_60s_rece_min_tot_1_mon, contact_min_over_15s_cnt_2_wk, contact_min_over_15s_min_tot_2_wk, contact_min_over_15s_call_cnt_2_wk, contact_min_over_15s_call_min_tot_2_wk, contact_min_over_15s_rece_cnt_2_wk, contact_min_over_15s_rece_min_tot_2_wk, contact_min_over_30s_cnt_2_wk, contact_min_over_30s_min_tot_2_wk, contact_min_over_30s_call_cnt_2_wk, contact_min_over_30s_call_min_tot_2_wk, contact_min_over_30s_rece_cnt_2_wk, contact_min_over_30s_rece_min_tot_2_wk, contact_min_over_60s_cnt_2_wk, contact_min_over_60s_min_tot_2_wk, contact_min_over_60s_call_cnt_2_wk, contact_min_over_60s_call_min_tot_2_wk, contact_min_over_60s_rece_cnt_2_wk, contact_min_over_60s_rece_min_tot_2_wk, contact_hour_0to1_cnt, contact_hour_2to3_cnt, contact_hour_4to5_cnt, contact_hour_6to7_cnt, contact_hour_8to9_cnt, contact_hour_10to11_cnt, contact_hour_12to13_cnt, contact_hour_14to15_cnt, contact_hour_16to17_cnt, contact_hour_18to19_cnt, contact_hour_20to21_cnt, contact_hour_22to23_cnt, contact_hour_0to1_min_tot, contact_hour_2to3_min_tot, contact_hour_4to5_min_tot, contact_hour_6to7_min_tot, contact_hour_8to9_min_tot, contact_hour_10to11_min_tot, contact_hour_12to13_min_tot, contact_hour_14to15_min_tot, contact_hour_16to17_min_tot, contact_hour_18to19_min_tot, contact_hour_20to21_min_tot, contact_hour_22to23_min_tot, contact_hour_0to1_cnt_6_mon, contact_hour_2to3_cnt_6_mon, contact_hour_4to5_cnt_6_mon, contact_hour_6to7_cnt_6_mon, contact_hour_8to9_cnt_6_mon, contact_hour_10to11_cnt_6_mon, contact_hour_12to13_cnt_6_mon, contact_hour_14to15_cnt_6_mon, contact_hour_16to17_cnt_6_mon, contact_hour_18to19_cnt_6_mon, contact_hour_20to21_cnt_6_mon, contact_hour_22to23_cnt_6_mon, contact_hour_0to1_min_tot_6_mon, contact_hour_2to3_min_tot_6_mon, contact_hour_4to5_min_tot_6_mon, contact_hour_6to7_min_tot_6_mon, contact_hour_8to9_min_tot_6_mon, contact_hour_10to11_min_tot_6_mon, contact_hour_12to13_min_tot_6_mon, contact_hour_14to15_min_tot_6_mon, contact_hour_16to17_min_tot_6_mon, contact_hour_18to19_min_tot_6_mon, contact_hour_20to21_min_tot_6_mon, contact_hour_22to23_min_tot_6_mon, contact_hour_0to1_cnt_3_mon, contact_hour_2to3_cnt_3_mon, contact_hour_4to5_cnt_3_mon, contact_hour_6to7_cnt_3_mon, contact_hour_8to9_cnt_3_mon, contact_hour_10to11_cnt_3_mon, contact_hour_12to13_cnt_3_mon, contact_hour_14to15_cnt_3_mon, contact_hour_16to17_cnt_3_mon, contact_hour_18to19_cnt_3_mon, contact_hour_20to21_cnt_3_mon, contact_hour_22to23_cnt_3_mon, contact_hour_0to1_min_tot_3_mon, contact_hour_2to3_min_tot_3_mon, contact_hour_4to5_min_tot_3_mon, contact_hour_6to7_min_tot_3_mon, contact_hour_8to9_min_tot_3_mon, contact_hour_10to11_min_tot_3_mon, contact_hour_12to13_min_tot_3_mon, contact_hour_14to15_min_tot_3_mon, contact_hour_16to17_min_tot_3_mon, contact_hour_18to19_min_tot_3_mon, contact_hour_20to21_min_tot_3_mon, contact_hour_22to23_min_tot_3_mon, contact_hour_0to1_cnt_2_mon, contact_hour_2to3_cnt_2_mon, contact_hour_4to5_cnt_2_mon, contact_hour_6to7_cnt_2_mon, contact_hour_8to9_cnt_2_mon, contact_hour_10to11_cnt_2_mon, contact_hour_12to13_cnt_2_mon, contact_hour_14to15_cnt_2_mon, contact_hour_16to17_cnt_2_mon, contact_hour_18to19_cnt_2_mon, contact_hour_20to21_cnt_2_mon, contact_hour_22to23_cnt_2_mon, contact_hour_0to1_min_tot_2_mon, contact_hour_2to3_min_tot_2_mon, contact_hour_4to5_min_tot_2_mon, contact_hour_6to7_min_tot_2_mon, contact_hour_8to9_min_tot_2_mon, contact_hour_10to11_min_tot_2_mon, contact_hour_12to13_min_tot_2_mon, contact_hour_14to15_min_tot_2_mon, contact_hour_16to17_min_tot_2_mon, contact_hour_18to19_min_tot_2_mon, contact_hour_20to21_min_tot_2_mon, contact_hour_22to23_min_tot_2_mon, contact_hour_0to1_cnt_1_mon, contact_hour_2to3_cnt_1_mon, contact_hour_4to5_cnt_1_mon, contact_hour_6to7_cnt_1_mon, contact_hour_8to9_cnt_1_mon, contact_hour_10to11_cnt_1_mon, contact_hour_12to13_cnt_1_mon, contact_hour_14to15_cnt_1_mon, contact_hour_16to17_cnt_1_mon, contact_hour_18to19_cnt_1_mon, contact_hour_20to21_cnt_1_mon, contact_hour_22to23_cnt_1_mon, contact_hour_0to1_min_tot_1_mon, contact_hour_2to3_min_tot_1_mon, contact_hour_4to5_min_tot_1_mon, contact_hour_6to7_min_tot_1_mon, contact_hour_8to9_min_tot_1_mon, contact_hour_10to11_min_tot_1_mon, contact_hour_12to13_min_tot_1_mon, contact_hour_14to15_min_tot_1_mon, contact_hour_16to17_min_tot_1_mon, contact_hour_18to19_min_tot_1_mon, contact_hour_20to21_min_tot_1_mon, contact_hour_22to23_min_tot_1_mon, contact_hour_0to1_cnt_2_wk, contact_hour_2to3_cnt_2_wk, contact_hour_4to5_cnt_2_wk, contact_hour_6to7_cnt_2_wk, contact_hour_8to9_cnt_2_wk, contact_hour_10to11_cnt_2_wk, contact_hour_12to13_cnt_2_wk, contact_hour_14to15_cnt_2_wk, contact_hour_16to17_cnt_2_wk, contact_hour_18to19_cnt_2_wk, contact_hour_20to21_cnt_2_wk, contact_hour_22to23_cnt_2_wk, contact_hour_0to1_min_tot_2_wk, contact_hour_2to3_min_tot_2_wk, contact_hour_4to5_min_tot_2_wk, contact_hour_6to7_min_tot_2_wk, contact_hour_8to9_min_tot_2_wk, contact_hour_10to11_min_tot_2_wk, contact_hour_12to13_min_tot_2_wk, contact_hour_14to15_min_tot_2_wk, contact_hour_16to17_min_tot_2_wk, contact_hour_18to19_min_tot_2_wk, contact_hour_20to21_min_tot_2_wk, contact_hour_22to23_min_tot_2_wk, contact_hour_1to6_cnt, contact_hour_7to12_cnt, contact_hour_13to18_cnt, contact_hour_19to0_cnt, contact_hour_1to6_min_tot, contact_hour_7to12_min_tot, contact_hour_13to18_min_tot, contact_hour_19to0_min_tot, contact_hour_1to6_cnt_6_mon, contact_hour_7to12_cnt_6_mon, contact_hour_13to18_cnt_6_mon, contact_hour_19to0_cnt_6_mon, contact_hour_1to6_min_tot_6_mon, contact_hour_7to12_min_tot_6_mon, contact_hour_13to18_min_tot_6_mon, contact_hour_19to0_min_tot_6_mon, contact_hour_1to6_cnt_3_mon, contact_hour_7to12_cnt_3_mon, contact_hour_13to18_cnt_3_mon, contact_hour_19to0_cnt_3_mon, contact_hour_1to6_min_tot_3_mon, contact_hour_7to12_min_tot_3_mon, contact_hour_13to18_min_tot_3_mon, contact_hour_19to0_min_tot_3_mon, contact_hour_1to6_cnt_2_mon, contact_hour_7to12_cnt_2_mon, contact_hour_13to18_cnt_2_mon, contact_hour_19to0_cnt_2_mon, contact_hour_1to6_min_tot_2_mon, contact_hour_7to12_min_tot_2_mon, contact_hour_13to18_min_tot_2_mon, contact_hour_19to0_min_tot_2_mon, contact_hour_1to6_cnt_1_mon, contact_hour_7to12_cnt_1_mon, contact_hour_13to18_cnt_1_mon, contact_hour_19to0_cnt_1_mon, contact_hour_1to6_min_tot_1_mon, contact_hour_7to12_min_tot_1_mon, contact_hour_13to18_min_tot_1_mon, contact_hour_19to0_min_tot_1_mon, contact_hour_1to6_cnt_2_wk, contact_hour_7to12_cnt_2_wk, contact_hour_13to18_cnt_2_wk, contact_hour_19to0_cnt_2_wk, contact_hour_1to6_min_tot_2_wk, contact_hour_7to12_min_tot_2_wk, contact_hour_13to18_min_tot_2_wk, contact_hour_19to0_min_tot_2_wk, contact_hour_1to8_cnt, contact_hour_9to16_cnt, contact_hour_17to0_cnt, contact_hour_1to8_min_tot, contact_hour_9to16_min_tot, contact_hour_17to0_min_tot, contact_hour_1to8_cnt_6_mon, contact_hour_9to16_cnt_6_mon, contact_hour_17to0_cnt_6_mon, contact_hour_1to8_min_tot_6_mon, contact_hour_9to16_min_tot_6_mon, contact_hour_17to0_min_tot_6_mon, contact_hour_1to8_cnt_3_mon, contact_hour_9to16_cnt_3_mon, contact_hour_17to0_cnt_3_mon, contact_hour_1to8_min_tot_3_mon, contact_hour_9to16_min_tot_3_mon, contact_hour_17to0_min_tot_3_mon, contact_hour_1to8_cnt_2_mon, contact_hour_9to16_cnt_2_mon, contact_hour_17to0_cnt_2_mon, contact_hour_1to8_min_tot_2_mon, contact_hour_9to16_min_tot_2_mon, contact_hour_17to0_min_tot_2_mon, contact_hour_1to8_cnt_1_mon, contact_hour_9to16_cnt_1_mon, contact_hour_17to0_cnt_1_mon, contact_hour_1to8_min_tot_1_mon, contact_hour_9to16_min_tot_1_mon, contact_hour_17to0_min_tot_1_mon, contact_hour_1to8_cnt_2_wk, contact_hour_9to16_cnt_2_wk, contact_hour_17to0_cnt_2_wk, contact_hour_1to8_min_tot_2_wk, contact_hour_9to16_min_tot_2_wk, contact_hour_17to0_min_tot_2_wk, contact_hour_9to20_cnt, contact_hour_21to8_cnt, contact_hour_9to20_min_tot, contact_hour_21to8_min_tot, contact_hour_9to20_cnt_6_mon, contact_hour_21to8_cnt_6_mon, contact_hour_9to20_min_tot_6_mon, contact_hour_21to8_min_tot_6_mon, contact_hour_9to20_cnt_3_mon, contact_hour_21to8_cnt_3_mon, contact_hour_9to20_min_tot_3_mon, contact_hour_21to8_min_tot_3_mon, contact_hour_9to20_cnt_2_mon, contact_hour_21to8_cnt_2_mon, contact_hour_9to20_min_tot_2_mon, contact_hour_21to8_min_tot_2_mon, contact_hour_9to20_cnt_1_mon, contact_hour_21to8_cnt_1_mon, contact_hour_9to20_min_tot_1_mon, contact_hour_21to8_min_tot_1_mon, contact_hour_9to20_cnt_2_wk, contact_hour_21to8_cnt_2_wk, contact_hour_9to20_min_tot_2_wk, contact_hour_21to8_min_tot_2_wk, contact_hour_0to1_call_cnt, contact_hour_2to3_call_cnt, contact_hour_4to5_call_cnt, contact_hour_6to7_call_cnt, contact_hour_8to9_call_cnt, contact_hour_10to11_call_cnt, contact_hour_12to13_call_cnt, contact_hour_14to15_call_cnt, contact_hour_16to17_call_cnt, contact_hour_18to19_call_cnt, contact_hour_20to21_call_cnt, contact_hour_22to23_call_cnt, contact_hour_0to1_call_min_tot, contact_hour_2to3_call_min_tot, contact_hour_4to5_call_min_tot, contact_hour_6to7_call_min_tot, contact_hour_8to9_call_min_tot, contact_hour_10to11_call_min_tot, contact_hour_12to13_call_min_tot, contact_hour_14to15_call_min_tot, contact_hour_16to17_call_min_tot, contact_hour_18to19_call_min_tot, contact_hour_20to21_call_min_tot, contact_hour_22to23_call_min_tot, contact_hour_0to1_call_cnt_6_mon, contact_hour_2to3_call_cnt_6_mon, contact_hour_4to5_call_cnt_6_mon, contact_hour_6to7_call_cnt_6_mon, contact_hour_8to9_call_cnt_6_mon, contact_hour_10to11_call_cnt_6_mon, contact_hour_12to13_call_cnt_6_mon, contact_hour_14to15_call_cnt_6_mon, contact_hour_16to17_call_cnt_6_mon, contact_hour_18to19_call_cnt_6_mon, contact_hour_20to21_call_cnt_6_mon, contact_hour_22to23_call_cnt_6_mon, contact_hour_0to1_call_min_tot_6_mon, contact_hour_2to3_call_min_tot_6_mon, contact_hour_4to5_call_min_tot_6_mon, contact_hour_6to7_call_min_tot_6_mon, contact_hour_8to9_call_min_tot_6_mon, contact_hour_10to11_call_min_tot_6_mon, contact_hour_12to13_call_min_tot_6_mon, contact_hour_14to15_call_min_tot_6_mon, contact_hour_16to17_call_min_tot_6_mon, contact_hour_18to19_call_min_tot_6_mon, contact_hour_20to21_call_min_tot_6_mon, contact_hour_22to23_call_min_tot_6_mon, contact_hour_0to1_call_cnt_3_mon, contact_hour_2to3_call_cnt_3_mon, contact_hour_4to5_call_cnt_3_mon, contact_hour_6to7_call_cnt_3_mon, contact_hour_8to9_call_cnt_3_mon, contact_hour_10to11_call_cnt_3_mon, contact_hour_12to13_call_cnt_3_mon, contact_hour_14to15_call_cnt_3_mon, contact_hour_16to17_call_cnt_3_mon, contact_hour_18to19_call_cnt_3_mon, contact_hour_20to21_call_cnt_3_mon, contact_hour_22to23_call_cnt_3_mon, contact_hour_0to1_call_min_tot_3_mon, contact_hour_2to3_call_min_tot_3_mon, contact_hour_4to5_call_min_tot_3_mon, contact_hour_6to7_call_min_tot_3_mon, contact_hour_8to9_call_min_tot_3_mon, contact_hour_10to11_call_min_tot_3_mon, contact_hour_12to13_call_min_tot_3_mon, contact_hour_14to15_call_min_tot_3_mon, contact_hour_16to17_call_min_tot_3_mon, contact_hour_18to19_call_min_tot_3_mon, contact_hour_20to21_call_min_tot_3_mon, contact_hour_22to23_call_min_tot_3_mon, contact_hour_0to1_call_cnt_2_mon, contact_hour_2to3_call_cnt_2_mon, contact_hour_4to5_call_cnt_2_mon, contact_hour_6to7_call_cnt_2_mon, contact_hour_8to9_call_cnt_2_mon, contact_hour_10to11_call_cnt_2_mon, contact_hour_12to13_call_cnt_2_mon, contact_hour_14to15_call_cnt_2_mon, contact_hour_16to17_call_cnt_2_mon, contact_hour_18to19_call_cnt_2_mon, contact_hour_20to21_call_cnt_2_mon, contact_hour_22to23_call_cnt_2_mon, contact_hour_0to1_call_min_tot_2_mon, contact_hour_2to3_call_min_tot_2_mon, contact_hour_4to5_call_min_tot_2_mon, contact_hour_6to7_call_min_tot_2_mon, contact_hour_8to9_call_min_tot_2_mon, contact_hour_10to11_call_min_tot_2_mon, contact_hour_12to13_call_min_tot_2_mon, contact_hour_14to15_call_min_tot_2_mon, contact_hour_16to17_call_min_tot_2_mon, contact_hour_18to19_call_min_tot_2_mon, contact_hour_20to21_call_min_tot_2_mon, contact_hour_22to23_call_min_tot_2_mon, contact_hour_0to1_call_cnt_1_mon, contact_hour_2to3_call_cnt_1_mon, contact_hour_4to5_call_cnt_1_mon, contact_hour_6to7_call_cnt_1_mon, contact_hour_8to9_call_cnt_1_mon, contact_hour_10to11_call_cnt_1_mon, contact_hour_12to13_call_cnt_1_mon, contact_hour_14to15_call_cnt_1_mon, contact_hour_16to17_call_cnt_1_mon, contact_hour_18to19_call_cnt_1_mon, contact_hour_20to21_call_cnt_1_mon, contact_hour_22to23_call_cnt_1_mon, contact_hour_0to1_call_min_tot_1_mon, contact_hour_2to3_call_min_tot_1_mon, contact_hour_4to5_call_min_tot_1_mon, contact_hour_6to7_call_min_tot_1_mon, contact_hour_8to9_call_min_tot_1_mon, contact_hour_10to11_call_min_tot_1_mon, contact_hour_12to13_call_min_tot_1_mon, contact_hour_14to15_call_min_tot_1_mon, contact_hour_16to17_call_min_tot_1_mon, contact_hour_18to19_call_min_tot_1_mon, contact_hour_20to21_call_min_tot_1_mon, contact_hour_22to23_call_min_tot_1_mon, contact_hour_0to1_call_cnt_2_wk, contact_hour_2to3_call_cnt_2_wk, contact_hour_4to5_call_cnt_2_wk, contact_hour_6to7_call_cnt_2_wk, contact_hour_8to9_call_cnt_2_wk, contact_hour_10to11_call_cnt_2_wk, contact_hour_12to13_call_cnt_2_wk, contact_hour_14to15_call_cnt_2_wk, contact_hour_16to17_call_cnt_2_wk, contact_hour_18to19_call_cnt_2_wk, contact_hour_20to21_call_cnt_2_wk, contact_hour_22to23_call_cnt_2_wk, contact_hour_0to1_call_min_tot_2_wk, contact_hour_2to3_call_min_tot_2_wk, contact_hour_4to5_call_min_tot_2_wk, contact_hour_6to7_call_min_tot_2_wk, contact_hour_8to9_call_min_tot_2_wk, contact_hour_10to11_call_min_tot_2_wk, contact_hour_12to13_call_min_tot_2_wk, contact_hour_14to15_call_min_tot_2_wk, contact_hour_16to17_call_min_tot_2_wk, contact_hour_18to19_call_min_tot_2_wk, contact_hour_20to21_call_min_tot_2_wk, contact_hour_22to23_call_min_tot_2_wk, contact_hour_1to6_call_cnt, contact_hour_7to12_call_cnt, contact_hour_13to18_call_cnt, contact_hour_19to0_call_cnt, contact_hour_1to6_call_min_tot, contact_hour_7to12_call_min_tot, contact_hour_13to18_call_min_tot, contact_hour_19to0_call_min_tot, contact_hour_1to6_call_cnt_6_mon, contact_hour_7to12_call_cnt_6_mon, contact_hour_13to18_call_cnt_6_mon, contact_hour_19to0_call_cnt_6_mon, contact_hour_1to6_call_min_tot_6_mon, contact_hour_7to12_call_min_tot_6_mon, contact_hour_13to18_call_min_tot_6_mon, contact_hour_19to0_call_min_tot_6_mon, contact_hour_1to6_call_cnt_3_mon, contact_hour_7to12_call_cnt_3_mon, contact_hour_13to18_call_cnt_3_mon, contact_hour_19to0_call_cnt_3_mon, contact_hour_1to6_call_min_tot_3_mon, contact_hour_7to12_call_min_tot_3_mon, contact_hour_13to18_call_min_tot_3_mon, contact_hour_19to0_call_min_tot_3_mon, contact_hour_1to6_call_cnt_2_mon, contact_hour_7to12_call_cnt_2_mon, contact_hour_13to18_call_cnt_2_mon, contact_hour_19to0_call_cnt_2_mon, contact_hour_1to6_call_min_tot_2_mon, contact_hour_7to12_call_min_tot_2_mon, contact_hour_13to18_call_min_tot_2_mon, contact_hour_19to0_call_min_tot_2_mon, contact_hour_1to6_call_cnt_1_mon, contact_hour_7to12_call_cnt_1_mon, contact_hour_13to18_call_cnt_1_mon, contact_hour_19to0_call_cnt_1_mon, contact_hour_1to6_call_min_tot_1_mon, contact_hour_7to12_call_min_tot_1_mon, contact_hour_13to18_call_min_tot_1_mon, contact_hour_19to0_call_min_tot_1_mon, contact_hour_1to6_call_cnt_2_wk, contact_hour_7to12_call_cnt_2_wk, contact_hour_13to18_call_cnt_2_wk, contact_hour_19to0_call_cnt_2_wk, contact_hour_1to6_call_min_tot_2_wk, contact_hour_7to12_call_min_tot_2_wk, contact_hour_13to18_call_min_tot_2_wk, contact_hour_19to0_call_min_tot_2_wk, contact_hour_1to8_call_cnt, contact_hour_9to16_call_cnt, contact_hour_17to0_call_cnt, contact_hour_1to8_call_min_tot, contact_hour_9to16_call_min_tot, contact_hour_17to0_call_min_tot, contact_hour_1to8_call_cnt_6_mon, contact_hour_9to16_call_cnt_6_mon, contact_hour_17to0_call_cnt_6_mon, contact_hour_1to8_call_min_tot_6_mon, contact_hour_9to16_call_min_tot_6_mon, contact_hour_17to0_call_min_tot_6_mon, contact_hour_1to8_call_cnt_3_mon, contact_hour_9to16_call_cnt_3_mon, contact_hour_17to0_call_cnt_3_mon, contact_hour_1to8_call_min_tot_3_mon, contact_hour_9to16_call_min_tot_3_mon, contact_hour_17to0_call_min_tot_3_mon, contact_hour_1to8_call_cnt_2_mon, contact_hour_9to16_call_cnt_2_mon, contact_hour_17to0_call_cnt_2_mon, contact_hour_1to8_call_min_tot_2_mon, contact_hour_9to16_call_min_tot_2_mon, contact_hour_17to0_call_min_tot_2_mon, contact_hour_1to8_call_cnt_1_mon, contact_hour_9to16_call_cnt_1_mon, contact_hour_17to0_call_cnt_1_mon, contact_hour_1to8_call_min_tot_1_mon, contact_hour_9to16_call_min_tot_1_mon, contact_hour_17to0_call_min_tot_1_mon, contact_hour_1to8_call_cnt_2_wk, contact_hour_9to16_call_cnt_2_wk, contact_hour_17to0_call_cnt_2_wk, contact_hour_1to8_call_min_tot_2_wk, contact_hour_9to16_call_min_tot_2_wk, contact_hour_17to0_call_min_tot_2_wk, contact_hour_9to20_call_cnt, contact_hour_21to8_call_cnt, contact_hour_9to20_call_min_tot, contact_hour_21to8_call_min_tot, contact_hour_9to20_call_cnt_6_mon, contact_hour_21to8_call_cnt_6_mon, contact_hour_9to20_call_min_tot_6_mon, contact_hour_21to8_call_min_tot_6_mon, contact_hour_9to20_call_cnt_3_mon, contact_hour_21to8_call_cnt_3_mon, contact_hour_9to20_call_min_tot_3_mon, contact_hour_21to8_call_min_tot_3_mon, contact_hour_9to20_call_cnt_2_mon, contact_hour_21to8_call_cnt_2_mon, contact_hour_9to20_call_min_tot_2_mon, contact_hour_21to8_call_min_tot_2_mon, contact_hour_9to20_call_cnt_1_mon, contact_hour_21to8_call_cnt_1_mon, contact_hour_9to20_call_min_tot_1_mon, contact_hour_21to8_call_min_tot_1_mon, contact_hour_9to20_call_cnt_2_wk, contact_hour_21to8_call_cnt_2_wk, contact_hour_9to20_call_min_tot_2_wk, contact_hour_21to8_call_min_tot_2_wk, contact_hour_0to1_rece_cnt, contact_hour_2to3_rece_cnt, contact_hour_4to5_rece_cnt, contact_hour_6to7_rece_cnt, contact_hour_8to9_rece_cnt, contact_hour_10to11_rece_cnt, contact_hour_12to13_rece_cnt, contact_hour_14to15_rece_cnt, contact_hour_16to17_rece_cnt, contact_hour_18to19_rece_cnt, contact_hour_20to21_rece_cnt, contact_hour_22to23_rece_cnt, contact_hour_0to1_rece_min_tot, contact_hour_2to3_rece_min_tot, contact_hour_4to5_rece_min_tot, contact_hour_6to7_rece_min_tot, contact_hour_8to9_rece_min_tot, contact_hour_10to11_rece_min_tot, contact_hour_12to13_rece_min_tot, contact_hour_14to15_rece_min_tot, contact_hour_16to17_rece_min_tot, contact_hour_18to19_rece_min_tot, contact_hour_20to21_rece_min_tot, contact_hour_22to23_rece_min_tot, contact_hour_0to1_rece_cnt_6_mon, contact_hour_2to3_rece_cnt_6_mon, contact_hour_4to5_rece_cnt_6_mon, contact_hour_6to7_rece_cnt_6_mon, contact_hour_8to9_rece_cnt_6_mon, contact_hour_10to11_rece_cnt_6_mon, contact_hour_12to13_rece_cnt_6_mon, contact_hour_14to15_rece_cnt_6_mon, contact_hour_16to17_rece_cnt_6_mon, contact_hour_18to19_rece_cnt_6_mon, contact_hour_20to21_rece_cnt_6_mon, contact_hour_22to23_rece_cnt_6_mon, contact_hour_0to1_rece_min_tot_6_mon, contact_hour_2to3_rece_min_tot_6_mon, contact_hour_4to5_rece_min_tot_6_mon, contact_hour_6to7_rece_min_tot_6_mon, contact_hour_8to9_rece_min_tot_6_mon, contact_hour_10to11_rece_min_tot_6_mon, contact_hour_12to13_rece_min_tot_6_mon, contact_hour_14to15_rece_min_tot_6_mon, contact_hour_16to17_rece_min_tot_6_mon, contact_hour_18to19_rece_min_tot_6_mon, contact_hour_20to21_rece_min_tot_6_mon, contact_hour_22to23_rece_min_tot_6_mon, contact_hour_0to1_rece_cnt_3_mon, contact_hour_2to3_rece_cnt_3_mon, contact_hour_4to5_rece_cnt_3_mon, contact_hour_6to7_rece_cnt_3_mon, contact_hour_8to9_rece_cnt_3_mon, contact_hour_10to11_rece_cnt_3_mon, contact_hour_12to13_rece_cnt_3_mon, contact_hour_14to15_rece_cnt_3_mon, contact_hour_16to17_rece_cnt_3_mon, contact_hour_18to19_rece_cnt_3_mon, contact_hour_20to21_rece_cnt_3_mon, contact_hour_22to23_rece_cnt_3_mon, contact_hour_0to1_rece_min_tot_3_mon, contact_hour_2to3_rece_min_tot_3_mon, contact_hour_4to5_rece_min_tot_3_mon, contact_hour_6to7_rece_min_tot_3_mon, contact_hour_8to9_rece_min_tot_3_mon, contact_hour_10to11_rece_min_tot_3_mon, contact_hour_12to13_rece_min_tot_3_mon, contact_hour_14to15_rece_min_tot_3_mon, contact_hour_16to17_rece_min_tot_3_mon, contact_hour_18to19_rece_min_tot_3_mon, contact_hour_20to21_rece_min_tot_3_mon, contact_hour_22to23_rece_min_tot_3_mon, contact_hour_0to1_rece_cnt_2_mon, contact_hour_2to3_rece_cnt_2_mon, contact_hour_4to5_rece_cnt_2_mon, contact_hour_6to7_rece_cnt_2_mon, contact_hour_8to9_rece_cnt_2_mon, contact_hour_10to11_rece_cnt_2_mon, contact_hour_12to13_rece_cnt_2_mon, contact_hour_14to15_rece_cnt_2_mon, contact_hour_16to17_rece_cnt_2_mon, contact_hour_18to19_rece_cnt_2_mon, contact_hour_20to21_rece_cnt_2_mon, contact_hour_22to23_rece_cnt_2_mon, contact_hour_0to1_rece_min_tot_2_mon, contact_hour_2to3_rece_min_tot_2_mon, contact_hour_4to5_rece_min_tot_2_mon, contact_hour_6to7_rece_min_tot_2_mon, contact_hour_8to9_rece_min_tot_2_mon, contact_hour_10to11_rece_min_tot_2_mon, contact_hour_12to13_rece_min_tot_2_mon, contact_hour_14to15_rece_min_tot_2_mon, contact_hour_16to17_rece_min_tot_2_mon, contact_hour_18to19_rece_min_tot_2_mon, contact_hour_20to21_rece_min_tot_2_mon, contact_hour_22to23_rece_min_tot_2_mon, contact_hour_0to1_rece_cnt_1_mon, contact_hour_2to3_rece_cnt_1_mon, contact_hour_4to5_rece_cnt_1_mon, contact_hour_6to7_rece_cnt_1_mon, contact_hour_8to9_rece_cnt_1_mon, contact_hour_10to11_rece_cnt_1_mon, contact_hour_12to13_rece_cnt_1_mon, contact_hour_14to15_rece_cnt_1_mon, contact_hour_16to17_rece_cnt_1_mon, contact_hour_18to19_rece_cnt_1_mon, contact_hour_20to21_rece_cnt_1_mon, contact_hour_22to23_rece_cnt_1_mon, contact_hour_0to1_rece_min_tot_1_mon, contact_hour_2to3_rece_min_tot_1_mon, contact_hour_4to5_rece_min_tot_1_mon, contact_hour_6to7_rece_min_tot_1_mon, contact_hour_8to9_rece_min_tot_1_mon, contact_hour_10to11_rece_min_tot_1_mon, contact_hour_12to13_rece_min_tot_1_mon, contact_hour_14to15_rece_min_tot_1_mon, contact_hour_16to17_rece_min_tot_1_mon, contact_hour_18to19_rece_min_tot_1_mon, contact_hour_20to21_rece_min_tot_1_mon, contact_hour_22to23_rece_min_tot_1_mon, contact_hour_0to1_rece_cnt_2_wk, contact_hour_2to3_rece_cnt_2_wk, contact_hour_4to5_rece_cnt_2_wk, contact_hour_6to7_rece_cnt_2_wk, contact_hour_8to9_rece_cnt_2_wk, contact_hour_10to11_rece_cnt_2_wk, contact_hour_12to13_rece_cnt_2_wk, contact_hour_14to15_rece_cnt_2_wk, contact_hour_16to17_rece_cnt_2_wk, contact_hour_18to19_rece_cnt_2_wk, contact_hour_20to21_rece_cnt_2_wk, contact_hour_22to23_rece_cnt_2_wk, contact_hour_0to1_rece_min_tot_2_wk, contact_hour_2to3_rece_min_tot_2_wk, contact_hour_4to5_rece_min_tot_2_wk, contact_hour_6to7_rece_min_tot_2_wk, contact_hour_8to9_rece_min_tot_2_wk, contact_hour_10to11_rece_min_tot_2_wk, contact_hour_12to13_rece_min_tot_2_wk, contact_hour_14to15_rece_min_tot_2_wk, contact_hour_16to17_rece_min_tot_2_wk, contact_hour_18to19_rece_min_tot_2_wk, contact_hour_20to21_rece_min_tot_2_wk, contact_hour_22to23_rece_min_tot_2_wk, contact_hour_1to6_rece_cnt, contact_hour_7to12_rece_cnt, contact_hour_13to18_rece_cnt, contact_hour_19to0_rece_cnt, contact_hour_1to6_rece_min_tot, contact_hour_7to12_rece_min_tot, contact_hour_13to18_rece_min_tot, contact_hour_19to0_rece_min_tot, contact_hour_1to6_rece_cnt_6_mon, contact_hour_7to12_rece_cnt_6_mon, contact_hour_13to18_rece_cnt_6_mon, contact_hour_19to0_rece_cnt_6_mon, contact_hour_1to6_rece_min_tot_6_mon, contact_hour_7to12_rece_min_tot_6_mon, contact_hour_13to18_rece_min_tot_6_mon, contact_hour_19to0_rece_min_tot_6_mon, contact_hour_1to6_rece_cnt_3_mon, contact_hour_7to12_rece_cnt_3_mon, contact_hour_13to18_rece_cnt_3_mon, contact_hour_19to0_rece_cnt_3_mon, contact_hour_1to6_rece_min_tot_3_mon, contact_hour_7to12_rece_min_tot_3_mon, contact_hour_13to18_rece_min_tot_3_mon, contact_hour_19to0_rece_min_tot_3_mon, contact_hour_1to6_rece_cnt_2_mon, contact_hour_7to12_rece_cnt_2_mon, contact_hour_13to18_rece_cnt_2_mon, contact_hour_19to0_rece_cnt_2_mon, contact_hour_1to6_rece_min_tot_2_mon, contact_hour_7to12_rece_min_tot_2_mon, contact_hour_13to18_rece_min_tot_2_mon, contact_hour_19to0_rece_min_tot_2_mon, contact_hour_1to6_rece_cnt_1_mon, contact_hour_7to12_rece_cnt_1_mon, contact_hour_13to18_rece_cnt_1_mon, contact_hour_19to0_rece_cnt_1_mon, contact_hour_1to6_rece_min_tot_1_mon, contact_hour_7to12_rece_min_tot_1_mon, contact_hour_13to18_rece_min_tot_1_mon, contact_hour_19to0_rece_min_tot_1_mon, contact_hour_1to6_rece_cnt_2_wk, contact_hour_7to12_rece_cnt_2_wk, contact_hour_13to18_rece_cnt_2_wk, contact_hour_19to0_rece_cnt_2_wk, contact_hour_1to6_rece_min_tot_2_wk, contact_hour_7to12_rece_min_tot_2_wk, contact_hour_13to18_rece_min_tot_2_wk, contact_hour_19to0_rece_min_tot_2_wk, contact_hour_1to8_rece_cnt, contact_hour_9to16_rece_cnt, contact_hour_17to0_rece_cnt, contact_hour_1to8_rece_min_tot, contact_hour_9to16_rece_min_tot, contact_hour_17to0_rece_min_tot, contact_hour_1to8_rece_cnt_6_mon, contact_hour_9to16_rece_cnt_6_mon, contact_hour_17to0_rece_cnt_6_mon, contact_hour_1to8_rece_min_tot_6_mon, contact_hour_9to16_rece_min_tot_6_mon, contact_hour_17to0_rece_min_tot_6_mon, contact_hour_1to8_rece_cnt_3_mon, contact_hour_9to16_rece_cnt_3_mon, contact_hour_17to0_rece_cnt_3_mon, contact_hour_1to8_rece_min_tot_3_mon, contact_hour_9to16_rece_min_tot_3_mon, contact_hour_17to0_rece_min_tot_3_mon, contact_hour_1to8_rece_cnt_2_mon, contact_hour_9to16_rece_cnt_2_mon, contact_hour_17to0_rece_cnt_2_mon, contact_hour_1to8_rece_min_tot_2_mon, contact_hour_9to16_rece_min_tot_2_mon, contact_hour_17to0_rece_min_tot_2_mon, contact_hour_1to8_rece_cnt_1_mon, contact_hour_9to16_rece_cnt_1_mon, contact_hour_17to0_rece_cnt_1_mon, contact_hour_1to8_rece_min_tot_1_mon, contact_hour_9to16_rece_min_tot_1_mon, contact_hour_17to0_rece_min_tot_1_mon, contact_hour_1to8_rece_cnt_2_wk, contact_hour_9to16_rece_cnt_2_wk, contact_hour_17to0_rece_cnt_2_wk, contact_hour_1to8_rece_min_tot_2_wk, contact_hour_9to16_rece_min_tot_2_wk, contact_hour_17to0_rece_min_tot_2_wk, contact_hour_9to20_rece_cnt, contact_hour_21to8_rece_cnt, contact_hour_9to20_rece_min_tot, contact_hour_21to8_rece_min_tot, contact_hour_9to20_rece_cnt_6_mon, contact_hour_21to8_rece_cnt_6_mon, contact_hour_9to20_rece_min_tot_6_mon, contact_hour_21to8_rece_min_tot_6_mon, contact_hour_9to20_rece_cnt_3_mon, contact_hour_21to8_rece_cnt_3_mon, contact_hour_9to20_rece_min_tot_3_mon, contact_hour_21to8_rece_min_tot_3_mon, contact_hour_9to20_rece_cnt_2_mon, contact_hour_21to8_rece_cnt_2_mon, contact_hour_9to20_rece_min_tot_2_mon, contact_hour_21to8_rece_min_tot_2_mon, contact_hour_9to20_rece_cnt_1_mon, contact_hour_21to8_rece_cnt_1_mon, contact_hour_9to20_rece_min_tot_1_mon, contact_hour_21to8_rece_min_tot_1_mon, contact_hour_9to20_rece_cnt_2_wk, contact_hour_21to8_rece_cnt_2_wk, contact_hour_9to20_rece_min_tot_2_wk, contact_hour_21to8_rece_min_tot_2_wk, contact_hour_0_min_avg, contact_hour_1_min_avg, contact_hour_2_min_avg, contact_hour_3_min_avg, contact_hour_4_min_avg, contact_hour_5_min_avg, contact_hour_6_min_avg, contact_hour_7_min_avg, contact_hour_8_min_avg, contact_hour_9_min_avg, contact_hour_10_min_avg, contact_hour_11_min_avg, contact_hour_12_min_avg, contact_hour_13_min_avg, contact_hour_14_min_avg, contact_hour_15_min_avg, contact_hour_16_min_avg, contact_hour_17_min_avg, contact_hour_18_min_avg, contact_hour_19_min_avg, contact_hour_20_min_avg, contact_hour_21_min_avg, contact_hour_22_min_avg, contact_hour_23_min_avg, contact_hour_0_min_avg_6_mon, contact_hour_1_min_avg_6_mon, contact_hour_2_min_avg_6_mon, contact_hour_3_min_avg_6_mon, contact_hour_4_min_avg_6_mon, contact_hour_5_min_avg_6_mon, contact_hour_6_min_avg_6_mon, contact_hour_7_min_avg_6_mon, contact_hour_8_min_avg_6_mon, contact_hour_9_min_avg_6_mon, contact_hour_10_min_avg_6_mon, contact_hour_11_min_avg_6_mon, contact_hour_12_min_avg_6_mon, contact_hour_13_min_avg_6_mon, contact_hour_14_min_avg_6_mon, contact_hour_15_min_avg_6_mon, contact_hour_16_min_avg_6_mon, contact_hour_17_min_avg_6_mon, contact_hour_18_min_avg_6_mon, contact_hour_19_min_avg_6_mon, contact_hour_20_min_avg_6_mon, contact_hour_21_min_avg_6_mon, contact_hour_22_min_avg_6_mon, contact_hour_23_min_avg_6_mon, contact_hour_0_min_avg_3_mon, contact_hour_1_min_avg_3_mon, contact_hour_2_min_avg_3_mon, contact_hour_3_min_avg_3_mon, contact_hour_4_min_avg_3_mon, contact_hour_5_min_avg_3_mon, contact_hour_6_min_avg_3_mon, contact_hour_7_min_avg_3_mon, contact_hour_8_min_avg_3_mon, contact_hour_9_min_avg_3_mon, contact_hour_10_min_avg_3_mon, contact_hour_11_min_avg_3_mon, contact_hour_12_min_avg_3_mon, contact_hour_13_min_avg_3_mon, contact_hour_14_min_avg_3_mon, contact_hour_15_min_avg_3_mon, contact_hour_16_min_avg_3_mon, contact_hour_17_min_avg_3_mon, contact_hour_18_min_avg_3_mon, contact_hour_19_min_avg_3_mon, contact_hour_20_min_avg_3_mon, contact_hour_21_min_avg_3_mon, contact_hour_22_min_avg_3_mon, contact_hour_23_min_avg_3_mon, contact_hour_0_min_avg_2_mon, contact_hour_1_min_avg_2_mon, contact_hour_2_min_avg_2_mon, contact_hour_3_min_avg_2_mon, contact_hour_4_min_avg_2_mon, contact_hour_5_min_avg_2_mon, contact_hour_6_min_avg_2_mon, contact_hour_7_min_avg_2_mon, contact_hour_8_min_avg_2_mon, contact_hour_9_min_avg_2_mon, contact_hour_10_min_avg_2_mon, contact_hour_11_min_avg_2_mon, contact_hour_12_min_avg_2_mon, contact_hour_13_min_avg_2_mon, contact_hour_14_min_avg_2_mon, contact_hour_15_min_avg_2_mon, contact_hour_16_min_avg_2_mon, contact_hour_17_min_avg_2_mon, contact_hour_18_min_avg_2_mon, contact_hour_19_min_avg_2_mon, contact_hour_20_min_avg_2_mon, contact_hour_21_min_avg_2_mon, contact_hour_22_min_avg_2_mon, contact_hour_23_min_avg_2_mon, contact_hour_0_min_avg_1_mon, contact_hour_1_min_avg_1_mon, contact_hour_2_min_avg_1_mon, contact_hour_3_min_avg_1_mon, contact_hour_4_min_avg_1_mon, contact_hour_5_min_avg_1_mon, contact_hour_6_min_avg_1_mon, contact_hour_7_min_avg_1_mon, contact_hour_8_min_avg_1_mon, contact_hour_9_min_avg_1_mon, contact_hour_10_min_avg_1_mon, contact_hour_11_min_avg_1_mon, contact_hour_12_min_avg_1_mon, contact_hour_13_min_avg_1_mon, contact_hour_14_min_avg_1_mon, contact_hour_15_min_avg_1_mon, contact_hour_16_min_avg_1_mon, contact_hour_17_min_avg_1_mon, contact_hour_18_min_avg_1_mon, contact_hour_19_min_avg_1_mon, contact_hour_20_min_avg_1_mon, contact_hour_21_min_avg_1_mon, contact_hour_22_min_avg_1_mon, contact_hour_23_min_avg_1_mon, contact_hour_0_min_avg_2_wk, contact_hour_1_min_avg_2_wk, contact_hour_2_min_avg_2_wk, contact_hour_3_min_avg_2_wk, contact_hour_4_min_avg_2_wk, contact_hour_5_min_avg_2_wk, contact_hour_6_min_avg_2_wk, contact_hour_7_min_avg_2_wk, contact_hour_8_min_avg_2_wk, contact_hour_9_min_avg_2_wk, contact_hour_10_min_avg_2_wk, contact_hour_11_min_avg_2_wk, contact_hour_12_min_avg_2_wk, contact_hour_13_min_avg_2_wk, contact_hour_14_min_avg_2_wk, contact_hour_15_min_avg_2_wk, contact_hour_16_min_avg_2_wk, contact_hour_17_min_avg_2_wk, contact_hour_18_min_avg_2_wk, contact_hour_19_min_avg_2_wk, contact_hour_20_min_avg_2_wk, contact_hour_21_min_avg_2_wk, contact_hour_22_min_avg_2_wk, contact_hour_23_min_avg_2_wk, contact_hour_0to1_min_avg, contact_hour_2to3_min_avg, contact_hour_4to5_min_avg, contact_hour_6to7_min_avg, contact_hour_8to9_min_avg, contact_hour_10to11_min_avg, contact_hour_12to13_min_avg, contact_hour_14to15_min_avg, contact_hour_16to17_min_avg, contact_hour_18to19_min_avg, contact_hour_20to21_min_avg, contact_hour_22to23_min_avg, contact_hour_0to1_min_avg_6_mon, contact_hour_2to3_min_avg_6_mon, contact_hour_4to5_min_avg_6_mon, contact_hour_6to7_min_avg_6_mon, contact_hour_8to9_min_avg_6_mon, contact_hour_10to11_min_avg_6_mon, contact_hour_12to13_min_avg_6_mon, contact_hour_14to15_min_avg_6_mon, contact_hour_16to17_min_avg_6_mon, contact_hour_18to19_min_avg_6_mon, contact_hour_20to21_min_avg_6_mon, contact_hour_22to23_min_avg_6_mon, contact_hour_0to1_min_avg_3_mon, contact_hour_2to3_min_avg_3_mon, contact_hour_4to5_min_avg_3_mon, contact_hour_6to7_min_avg_3_mon, contact_hour_8to9_min_avg_3_mon, contact_hour_10to11_min_avg_3_mon, contact_hour_12to13_min_avg_3_mon, contact_hour_14to15_min_avg_3_mon, contact_hour_16to17_min_avg_3_mon, contact_hour_18to19_min_avg_3_mon, contact_hour_20to21_min_avg_3_mon, contact_hour_22to23_min_avg_3_mon, contact_hour_0to1_min_avg_2_mon, contact_hour_2to3_min_avg_2_mon, contact_hour_4to5_min_avg_2_mon, contact_hour_6to7_min_avg_2_mon, contact_hour_8to9_min_avg_2_mon, contact_hour_10to11_min_avg_2_mon, contact_hour_12to13_min_avg_2_mon, contact_hour_14to15_min_avg_2_mon, contact_hour_16to17_min_avg_2_mon, contact_hour_18to19_min_avg_2_mon, contact_hour_20to21_min_avg_2_mon, contact_hour_22to23_min_avg_2_mon, contact_hour_0to1_min_avg_1_mon, contact_hour_2to3_min_avg_1_mon, contact_hour_4to5_min_avg_1_mon, contact_hour_6to7_min_avg_1_mon, contact_hour_8to9_min_avg_1_mon, contact_hour_10to11_min_avg_1_mon, contact_hour_12to13_min_avg_1_mon, contact_hour_14to15_min_avg_1_mon, contact_hour_16to17_min_avg_1_mon, contact_hour_18to19_min_avg_1_mon, contact_hour_20to21_min_avg_1_mon, contact_hour_22to23_min_avg_1_mon, contact_hour_0to1_min_avg_2_wk, contact_hour_2to3_min_avg_2_wk, contact_hour_4to5_min_avg_2_wk, contact_hour_6to7_min_avg_2_wk, contact_hour_8to9_min_avg_2_wk, contact_hour_10to11_min_avg_2_wk, contact_hour_12to13_min_avg_2_wk, contact_hour_14to15_min_avg_2_wk, contact_hour_16to17_min_avg_2_wk, contact_hour_18to19_min_avg_2_wk, contact_hour_20to21_min_avg_2_wk, contact_hour_22to23_min_avg_2_wk, contact_hour_1to8_min_avg, contact_hour_9to16_min_avg, contact_hour_17to0_min_avg, contact_hour_1to8_min_avg_6_mon, contact_hour_9to16_min_avg_6_mon, contact_hour_17to0_min_avg_6_mon, contact_hour_1to8_min_avg_3_mon, contact_hour_9to16_min_avg_3_mon, contact_hour_17to0_min_avg_3_mon, contact_hour_1to8_min_avg_2_mon, contact_hour_9to16_min_avg_2_mon, contact_hour_17to0_min_avg_2_mon, contact_hour_1to8_min_avg_1_mon, contact_hour_9to16_min_avg_1_mon, contact_hour_17to0_min_avg_1_mon, contact_hour_1to8_min_avg_2_wk, contact_hour_9to16_min_avg_2_wk, contact_hour_17to0_min_avg_2_wk, contact_hour_1to6_call_min_avg, contact_hour_7to12_call_min_avg, contact_hour_13to18_call_min_avg, contact_hour_19to0_call_min_avg, contact_hour_1to6_call_min_avg_6_mon, contact_hour_7to12_call_min_avg_6_mon, contact_hour_13to18_call_min_avg_6_mon, contact_hour_19to0_call_min_avg_6_mon, contact_hour_1to6_call_min_avg_3_mon, contact_hour_7to12_call_min_avg_3_mon, contact_hour_13to18_call_min_avg_3_mon, contact_hour_19to0_call_min_avg_3_mon, contact_hour_1to6_call_min_avg_2_mon, contact_hour_7to12_call_min_avg_2_mon, contact_hour_13to18_call_min_avg_2_mon, contact_hour_19to0_call_min_avg_2_mon, contact_hour_1to6_call_min_avg_1_mon, contact_hour_7to12_call_min_avg_1_mon, contact_hour_13to18_call_min_avg_1_mon, contact_hour_19to0_call_min_avg_1_mon, contact_hour_1to6_call_min_avg_2_wk, contact_hour_7to12_call_min_avg_2_wk, contact_hour_13to18_call_min_avg_2_wk, contact_hour_19to0_call_min_avg_2_wk, contact_hour_1to8_call_min_avg, contact_hour_9to16_call_min_avg, contact_hour_17to0_call_min_avg, contact_hour_1to8_call_min_avg_6_mon, contact_hour_9to16_call_min_avg_6_mon, contact_hour_17to0_call_min_avg_6_mon, contact_hour_1to8_call_min_avg_3_mon, contact_hour_9to16_call_min_avg_3_mon, contact_hour_17to0_call_min_avg_3_mon, contact_hour_1to8_call_min_avg_2_mon, contact_hour_9to16_call_min_avg_2_mon, contact_hour_17to0_call_min_avg_2_mon, contact_hour_1to8_call_min_avg_1_mon, contact_hour_9to16_call_min_avg_1_mon, contact_hour_17to0_call_min_avg_1_mon, contact_hour_1to8_call_min_avg_2_wk, contact_hour_9to16_call_min_avg_2_wk, contact_hour_17to0_call_min_avg_2_wk, contact_hour_9to20_call_min_avg, contact_hour_21to8_call_min_avg, contact_hour_9to20_call_min_avg_6_mon, contact_hour_21to8_call_min_avg_6_mon, contact_hour_9to20_call_min_avg_3_mon, contact_hour_21to8_call_min_avg_3_mon, contact_hour_9to20_call_min_avg_2_mon, contact_hour_21to8_call_min_avg_2_mon, contact_hour_9to20_call_min_avg_1_mon, contact_hour_21to8_call_min_avg_1_mon, contact_hour_9to20_call_min_avg_2_wk, contact_hour_21to8_call_min_avg_2_wk, contact_hour_1to6_rece_min_avg, contact_hour_7to12_rece_min_avg, contact_hour_13to18_rece_min_avg, contact_hour_19to0_rece_min_avg, contact_hour_1to6_rece_min_avg_6_mon, contact_hour_7to12_rece_min_avg_6_mon, contact_hour_13to18_rece_min_avg_6_mon, contact_hour_19to0_rece_min_avg_6_mon, contact_hour_1to6_rece_min_avg_3_mon, contact_hour_7to12_rece_min_avg_3_mon, contact_hour_13to18_rece_min_avg_3_mon, contact_hour_19to0_rece_min_avg_3_mon, contact_hour_1to6_rece_min_avg_2_mon, contact_hour_7to12_rece_min_avg_2_mon, contact_hour_13to18_rece_min_avg_2_mon, contact_hour_19to0_rece_min_avg_2_mon, contact_hour_1to6_rece_min_avg_1_mon, contact_hour_7to12_rece_min_avg_1_mon, contact_hour_13to18_rece_min_avg_1_mon, contact_hour_19to0_rece_min_avg_1_mon, contact_hour_1to6_rece_min_avg_2_wk, contact_hour_7to12_rece_min_avg_2_wk, contact_hour_13to18_rece_min_avg_2_wk, contact_hour_19to0_rece_min_avg_2_wk, contact_hour_1to8_rece_min_avg, contact_hour_9to16_rece_min_avg, contact_hour_17to0_rece_min_avg, contact_hour_1to8_rece_min_avg_6_mon, contact_hour_9to16_rece_min_avg_6_mon, contact_hour_17to0_rece_min_avg_6_mon, contact_hour_1to8_rece_min_avg_3_mon, contact_hour_9to16_rece_min_avg_3_mon, contact_hour_17to0_rece_min_avg_3_mon, contact_hour_1to8_rece_min_avg_2_mon, contact_hour_9to16_rece_min_avg_2_mon, contact_hour_17to0_rece_min_avg_2_mon, contact_hour_1to8_rece_min_avg_1_mon, contact_hour_9to16_rece_min_avg_1_mon, contact_hour_17to0_rece_min_avg_1_mon, contact_hour_1to8_rece_min_avg_2_wk, contact_hour_9to16_rece_min_avg_2_wk, contact_hour_17to0_rece_min_avg_2_wk, contact_hour_9to20_rece_min_avg, contact_hour_21to8_rece_min_avg, contact_hour_9to20_rece_min_avg_6_mon, contact_hour_21to8_rece_min_avg_6_mon, contact_hour_9to20_rece_min_avg_3_mon, contact_hour_21to8_rece_min_avg_3_mon, contact_hour_9to20_rece_min_avg_2_mon, contact_hour_21to8_rece_min_avg_2_mon, contact_hour_9to20_rece_min_avg_1_mon, contact_hour_21to8_rece_min_avg_1_mon, contact_hour_9to20_rece_min_avg_2_wk, contact_hour_21to8_rece_min_avg_2_wk, contact_hour_1to6_cnt_24h_perc, contact_hour_7to12_cnt_24h_perc, contact_hour_13to18_cnt_24h_perc, contact_hour_19to0_cnt_24h_perc, contact_hour_1to6_min_tot_24h_perc, contact_hour_7to12_min_tot_24h_perc, contact_hour_13to18_min_tot_24h_perc, contact_hour_19to0_min_tot_24h_perc, contact_hour_1to6_cnt_6_mon_24h_perc, contact_hour_7to12_cnt_6_mon_24h_perc, contact_hour_13to18_cnt_6_mon_24h_perc, contact_hour_19to0_cnt_6_mon_24h_perc, contact_hour_1to6_min_tot_6_mon_24h_perc, contact_hour_7to12_min_tot_6_mon_24h_perc, contact_hour_13to18_min_tot_6_mon_24h_perc, contact_hour_19to0_min_tot_6_mon_24h_perc, contact_hour_1to6_cnt_3_mon_24h_perc, contact_hour_7to12_cnt_3_mon_24h_perc, contact_hour_13to18_cnt_3_mon_24h_perc, contact_hour_19to0_cnt_3_mon_24h_perc, contact_hour_1to6_min_tot_3_mon_24h_perc, contact_hour_7to12_min_tot_3_mon_24h_perc, contact_hour_13to18_min_tot_3_mon_24h_perc, contact_hour_19to0_min_tot_3_mon_24h_perc, contact_hour_1to6_cnt_2_mon_24h_perc, contact_hour_7to12_cnt_2_mon_24h_perc, contact_hour_13to18_cnt_2_mon_24h_perc, contact_hour_19to0_cnt_2_mon_24h_perc, contact_hour_1to6_min_tot_2_mon_24h_perc, contact_hour_7to12_min_tot_2_mon_24h_perc, contact_hour_13to18_min_tot_2_mon_24h_perc, contact_hour_19to0_min_tot_2_mon_24h_perc, contact_hour_1to6_cnt_1_mon_24h_perc, contact_hour_7to12_cnt_1_mon_24h_perc, contact_hour_13to18_cnt_1_mon_24h_perc, contact_hour_19to0_cnt_1_mon_24h_perc, contact_hour_1to6_min_tot_1_mon_24h_perc, contact_hour_7to12_min_tot_1_mon_24h_perc, contact_hour_13to18_min_tot_1_mon_24h_perc, contact_hour_19to0_min_tot_1_mon_24h_perc, contact_hour_1to6_cnt_2_wk_24h_perc, contact_hour_7to12_cnt_2_wk_24h_perc, contact_hour_13to18_cnt_2_wk_24h_perc, contact_hour_19to0_cnt_2_wk_24h_perc, contact_hour_1to6_min_tot_2_wk_24h_perc, contact_hour_7to12_min_tot_2_wk_24h_perc, contact_hour_13to18_min_tot_2_wk_24h_perc, contact_hour_19to0_min_tot_2_wk_24h_perc, contact_hour_1to8_cnt_24h_perc, contact_hour_9to16_cnt_24h_perc, contact_hour_17to0_cnt_24h_perc, contact_hour_1to8_min_tot_24h_perc, contact_hour_9to16_min_tot_24h_perc, contact_hour_17to0_min_tot_24h_perc, contact_hour_1to8_cnt_6_mon_24h_perc, contact_hour_9to16_cnt_6_mon_24h_perc, contact_hour_17to0_cnt_6_mon_24h_perc, contact_hour_1to8_min_tot_6_mon_24h_perc, contact_hour_9to16_min_tot_6_mon_24h_perc, contact_hour_17to0_min_tot_6_mon_24h_perc, contact_hour_1to8_cnt_3_mon_24h_perc, contact_hour_9to16_cnt_3_mon_24h_perc, contact_hour_17to0_cnt_3_mon_24h_perc, contact_hour_1to8_min_tot_3_mon_24h_perc, contact_hour_9to16_min_tot_3_mon_24h_perc, contact_hour_17to0_min_tot_3_mon_24h_perc, contact_hour_1to8_cnt_2_mon_24h_perc, contact_hour_9to16_cnt_2_mon_24h_perc, contact_hour_17to0_cnt_2_mon_24h_perc, contact_hour_1to8_min_tot_2_mon_24h_perc, contact_hour_9to16_min_tot_2_mon_24h_perc, contact_hour_17to0_min_tot_2_mon_24h_perc, contact_hour_1to8_cnt_1_mon_24h_perc, contact_hour_9to16_cnt_1_mon_24h_perc, contact_hour_17to0_cnt_1_mon_24h_perc, contact_hour_1to8_min_tot_1_mon_24h_perc, contact_hour_9to16_min_tot_1_mon_24h_perc, contact_hour_17to0_min_tot_1_mon_24h_perc, contact_hour_1to8_cnt_2_wk_24h_perc, contact_hour_9to16_cnt_2_wk_24h_perc, contact_hour_17to0_cnt_2_wk_24h_perc, contact_hour_1to8_min_tot_2_wk_24h_perc, contact_hour_9to16_min_tot_2_wk_24h_perc, contact_hour_17to0_min_tot_2_wk_24h_perc, contact_hour_9to20_cnt_24_hour_perc, contact_hour_21to8_cnt_24_hour_perc, contact_hour_9to20_min_tot_24_hour_perc, contact_hour_21to8_min_tot_24_hour_perc, contact_hour_9to20_cnt_6_mon_24_hour_perc, contact_hour_21to8_cnt_6_mon_24_hour_perc, contact_hour_9to20_min_tot_6_mon_24_hour_perc, contact_hour_21to8_min_tot_6_mon_24_hour_perc, contact_hour_9to20_cnt_3_mon_24_hour_perc, contact_hour_21to8_cnt_3_mon_24_hour_perc, contact_hour_9to20_min_tot_3_mon_24_hour_perc, contact_hour_21to8_min_tot_3_mon_24_hour_perc, contact_hour_9to20_cnt_2_mon_24_hour_perc, contact_hour_21to8_cnt_2_mon_24_hour_perc, contact_hour_9to20_min_tot_2_mon_24_hour_perc, contact_hour_21to8_min_tot_2_mon_24_hour_perc, contact_hour_9to20_cnt_2_wk_24_hour_perc, contact_hour_21to8_cnt_2_wk_24_hour_perc, contact_hour_9to20_min_tot_2_wk_24_hour_perc, contact_hour_21to8_min_tot_2_wk_24_hour_perc, contact_hour_1to6_call_cnt_24h_perc, contact_hour_7to12_call_cnt_24h_perc, contact_hour_13to18_call_cnt_24h_perc, contact_hour_19to0_call_cnt_24h_perc, contact_hour_1to6_call_min_tot_24h_perc, contact_hour_7to12_call_min_tot_24h_perc, contact_hour_13to18_call_min_tot_24h_perc, contact_hour_19to0_call_min_tot_24h_perc, contact_hour_1to6_call_cnt_6_mon_24h_perc, contact_hour_7to12_call_cnt_6_mon_24h_perc, contact_hour_13to18_call_cnt_6_mon_24h_perc, contact_hour_19to0_call_cnt_6_mon_24h_perc, contact_hour_1to6_call_min_tot_6_mon_24h_perc, contact_hour_7to12_call_min_tot_6_mon_24h_perc, contact_hour_13to18_call_min_tot_6_mon_24h_perc, contact_hour_19to0_call_min_tot_6_mon_24h_perc, contact_hour_1to6_call_cnt_3_mon_24h_perc, contact_hour_7to12_call_cnt_3_mon_24h_perc, contact_hour_13to18_call_cnt_3_mon_24h_perc, contact_hour_19to0_call_cnt_3_mon_24h_perc, contact_hour_1to6_call_min_tot_3_mon_24h_perc, contact_hour_7to12_call_min_tot_3_mon_24h_perc, contact_hour_13to18_call_min_tot_3_mon_24h_perc, contact_hour_19to0_call_min_tot_3_mon_24h_perc, contact_hour_1to6_call_cnt_2_mon_24h_perc, contact_hour_7to12_call_cnt_2_mon_24h_perc, contact_hour_13to18_call_cnt_2_mon_24h_perc, contact_hour_19to0_call_cnt_2_mon_24h_perc, contact_hour_1to6_call_min_tot_2_mon_24h_perc, contact_hour_7to12_call_min_tot_2_mon_24h_perc, contact_hour_13to18_call_min_tot_2_mon_24h_perc, contact_hour_19to0_call_min_tot_2_mon_24h_perc, contact_hour_1to6_call_cnt_1_mon_24h_perc, contact_hour_7to12_call_cnt_1_mon_24h_perc, contact_hour_13to18_call_cnt_1_mon_24h_perc, contact_hour_19to0_call_cnt_1_mon_24h_perc, contact_hour_1to6_call_min_tot_1_mon_24h_perc, contact_hour_7to12_call_min_tot_1_mon_24h_perc, contact_hour_13to18_call_min_tot_1_mon_24h_perc, contact_hour_19to0_call_min_tot_1_mon_24h_perc, contact_hour_1to6_call_cnt_2_wk_24h_perc, contact_hour_7to12_call_cnt_2_wk_24h_perc, contact_hour_13to18_call_cnt_2_wk_24h_perc, contact_hour_19to0_call_cnt_2_wk_24h_perc, contact_hour_1to6_call_min_tot_2_wk_24h_perc, contact_hour_7to12_call_min_tot_2_wk_24h_perc, contact_hour_13to18_call_min_tot_2_wk_24h_perc, contact_hour_19to0_call_min_tot_2_wk_24h_perc, contact_hour_1to8_call_cnt_24h_perc, contact_hour_9to16_call_cnt_24h_perc, contact_hour_17to0_call_cnt_24h_perc, contact_hour_1to8_call_min_tot_24h_perc, contact_hour_9to16_call_min_tot_24h_perc, contact_hour_17to0_call_min_tot_24h_perc, contact_hour_1to8_call_cnt_6_mon_24h_perc, contact_hour_9to16_call_cnt_6_mon_24h_perc, contact_hour_17to0_call_cnt_6_mon_24h_perc, contact_hour_1to8_call_min_tot_6_mon_24h_perc, contact_hour_9to16_call_min_tot_6_mon_24h_perc, contact_hour_17to0_call_min_tot_6_mon_24h_perc, contact_hour_1to8_call_cnt_3_mon_24h_perc, contact_hour_9to16_call_cnt_3_mon_24h_perc, contact_hour_17to0_call_cnt_3_mon_24h_perc, contact_hour_1to8_call_min_tot_3_mon_24h_perc, contact_hour_9to16_call_min_tot_3_mon_24h_perc, contact_hour_17to0_call_min_tot_3_mon_24h_perc, contact_hour_1to8_call_cnt_2_mon_24h_perc, contact_hour_9to16_call_cnt_2_mon_24h_perc, contact_hour_17to0_call_cnt_2_mon_24h_perc, contact_hour_1to8_call_min_tot_2_mon_24h_perc, contact_hour_9to16_call_min_tot_2_mon_24h_perc, contact_hour_17to0_call_min_tot_2_mon_24h_perc, contact_hour_1to8_call_cnt_1_mon_24h_perc, contact_hour_9to16_call_cnt_1_mon_24h_perc, contact_hour_17to0_call_cnt_1_mon_24h_perc, contact_hour_1to8_call_min_tot_1_mon_24h_perc, contact_hour_9to16_call_min_tot_1_mon_24h_perc, contact_hour_17to0_call_min_tot_1_mon_24h_perc, contact_hour_1to8_call_cnt_2_wk_24h_perc, contact_hour_9to16_call_cnt_2_wk_24h_perc, contact_hour_17to0_call_cnt_2_wk_24h_perc, contact_hour_1to8_call_min_tot_2_wk_24h_perc, contact_hour_9to16_call_min_tot_2_wk_24h_perc, contact_hour_17to0_call_min_tot_2_wk_24h_perc, contact_hour_9to20_call_cnt_24_hour_perc, contact_hour_21to8_call_cnt_24_hour_perc, contact_hour_9to20_call_min_tot_24_hour_perc, contact_hour_21to8_call_min_tot_24_hour_perc, contact_hour_9to20_call_cnt_6_mon_24_hour_perc, contact_hour_21to8_call_cnt_6_mon_24_hour_perc, contact_hour_9to20_call_min_tot_6_mon_24_hour_perc, contact_hour_21to8_call_min_tot_6_mon_24_hour_perc, contact_hour_9to20_call_cnt_3_mon_24_hour_perc, contact_hour_21to8_call_cnt_3_mon_24_hour_perc, contact_hour_9to20_call_min_tot_3_mon_24_hour_perc, contact_hour_21to8_call_min_tot_3_mon_24_hour_perc, contact_hour_9to20_call_cnt_2_mon_24_hour_perc, contact_hour_21to8_call_cnt_2_mon_24_hour_perc, contact_hour_9to20_call_min_tot_2_mon_24_hour_perc, contact_hour_21to8_call_min_tot_2_mon_24_hour_perc, contact_hour_9to20_call_cnt_2_wk_24_hour_perc, contact_hour_21to8_call_cnt_2_wk_24_hour_perc, contact_hour_9to20_call_min_tot_2_wk_24_hour_perc, contact_hour_21to8_call_min_tot_2_wk_24_hour_perc, contact_hour_1to6_rece_cnt_24h_perc, contact_hour_7to12_rece_cnt_24h_perc, contact_hour_13to18_rece_cnt_24h_perc, contact_hour_19to0_rece_cnt_24h_perc, contact_hour_1to6_rece_min_tot_24h_perc, contact_hour_7to12_rece_min_tot_24h_perc, contact_hour_13to18_rece_min_tot_24h_perc, contact_hour_19to0_rece_min_tot_24h_perc, contact_hour_1to6_rece_cnt_6_mon_24h_perc, contact_hour_7to12_rece_cnt_6_mon_24h_perc, contact_hour_13to18_rece_cnt_6_mon_24h_perc, contact_hour_19to0_rece_cnt_6_mon_24h_perc, contact_hour_1to6_rece_min_tot_6_mon_24h_perc, contact_hour_7to12_rece_min_tot_6_mon_24h_perc, contact_hour_13to18_rece_min_tot_6_mon_24h_perc, contact_hour_19to0_rece_min_tot_6_mon_24h_perc, contact_hour_1to6_rece_cnt_3_mon_24h_perc, contact_hour_7to12_rece_cnt_3_mon_24h_perc, contact_hour_13to18_rece_cnt_3_mon_24h_perc, contact_hour_19to0_rece_cnt_3_mon_24h_perc, contact_hour_1to6_rece_min_tot_3_mon_24h_perc, contact_hour_7to12_rece_min_tot_3_mon_24h_perc, contact_hour_13to18_rece_min_tot_3_mon_24h_perc, contact_hour_19to0_rece_min_tot_3_mon_24h_perc, contact_hour_1to6_rece_cnt_2_mon_24h_perc, contact_hour_7to12_rece_cnt_2_mon_24h_perc, contact_hour_13to18_rece_cnt_2_mon_24h_perc, contact_hour_19to0_rece_cnt_2_mon_24h_perc, contact_hour_1to6_rece_min_tot_2_mon_24h_perc, contact_hour_7to12_rece_min_tot_2_mon_24h_perc, contact_hour_13to18_rece_min_tot_2_mon_24h_perc, contact_hour_19to0_rece_min_tot_2_mon_24h_perc, contact_hour_1to6_rece_cnt_1_mon_24h_perc, contact_hour_7to12_rece_cnt_1_mon_24h_perc, contact_hour_13to18_rece_cnt_1_mon_24h_perc, contact_hour_19to0_rece_cnt_1_mon_24h_perc, contact_hour_1to6_rece_min_tot_1_mon_24h_perc, contact_hour_7to12_rece_min_tot_1_mon_24h_perc, contact_hour_13to18_rece_min_tot_1_mon_24h_perc, contact_hour_19to0_rece_min_tot_1_mon_24h_perc, contact_hour_1to6_rece_cnt_2_wk_24h_perc, contact_hour_7to12_rece_cnt_2_wk_24h_perc, contact_hour_13to18_rece_cnt_2_wk_24h_perc, contact_hour_19to0_rece_cnt_2_wk_24h_perc, contact_hour_1to6_rece_min_tot_2_wk_24h_perc, contact_hour_7to12_rece_min_tot_2_wk_24h_perc, contact_hour_13to18_rece_min_tot_2_wk_24h_perc, contact_hour_19to0_rece_min_tot_2_wk_24h_perc, contact_hour_1to8_rece_cnt_24h_perc, contact_hour_9to16_rece_cnt_24h_perc, contact_hour_17to0_rece_cnt_24h_perc, contact_hour_1to8_rece_min_tot_24h_perc, contact_hour_9to16_rece_min_tot_24h_perc, contact_hour_17to0_rece_min_tot_24h_perc, contact_hour_1to8_rece_cnt_6_mon_24h_perc, contact_hour_9to16_rece_cnt_6_mon_24h_perc, contact_hour_17to0_rece_cnt_6_mon_24h_perc, contact_hour_1to8_rece_min_tot_6_mon_24h_perc, contact_hour_9to16_rece_min_tot_6_mon_24h_perc, contact_hour_17to0_rece_min_tot_6_mon_24h_perc, contact_hour_1to8_rece_cnt_3_mon_24h_perc, contact_hour_9to16_rece_cnt_3_mon_24h_perc, contact_hour_17to0_rece_cnt_3_mon_24h_perc, contact_hour_1to8_rece_min_tot_3_mon_24h_perc, contact_hour_9to16_rece_min_tot_3_mon_24h_perc, contact_hour_17to0_rece_min_tot_3_mon_24h_perc, contact_hour_1to8_rece_cnt_2_mon_24h_perc, contact_hour_9to16_rece_cnt_2_mon_24h_perc, contact_hour_17to0_rece_cnt_2_mon_24h_perc, contact_hour_1to8_rece_min_tot_2_mon_24h_perc, contact_hour_9to16_rece_min_tot_2_mon_24h_perc, contact_hour_17to0_rece_min_tot_2_mon_24h_perc, contact_hour_1to8_rece_cnt_1_mon_24h_perc, contact_hour_9to16_rece_cnt_1_mon_24h_perc, contact_hour_17to0_rece_cnt_1_mon_24h_perc, contact_hour_1to8_rece_min_tot_1_mon_24h_perc, contact_hour_9to16_rece_min_tot_1_mon_24h_perc, contact_hour_17to0_rece_min_tot_1_mon_24h_perc, contact_hour_1to8_rece_cnt_2_wk_24h_perc, contact_hour_9to16_rece_cnt_2_wk_24h_perc, contact_hour_17to0_rece_cnt_2_wk_24h_perc, contact_hour_1to8_rece_min_tot_2_wk_24h_perc, contact_hour_9to16_rece_min_tot_2_wk_24h_perc, contact_hour_17to0_rece_min_tot_2_wk_24h_perc, contact_hour_9to20_rece_cnt_24_hour_perc, contact_hour_21to8_rece_cnt_24_hour_perc, contact_hour_9to20_rece_min_tot_24_hour_perc, contact_hour_21to8_rece_min_tot_24_hour_perc, contact_hour_9to20_rece_cnt_6_mon_24_hour_perc, contact_hour_21to8_rece_cnt_6_mon_24_hour_perc, contact_hour_9to20_rece_min_tot_6_mon_24_hour_perc, contact_hour_21to8_rece_min_tot_6_mon_24_hour_perc, contact_hour_9to20_rece_cnt_3_mon_24_hour_perc, contact_hour_21to8_rece_cnt_3_mon_24_hour_perc, contact_hour_9to20_rece_min_tot_3_mon_24_hour_perc, contact_hour_21to8_rece_min_tot_3_mon_24_hour_perc, contact_hour_9to20_rece_cnt_2_mon_24_hour_perc, contact_hour_21to8_rece_cnt_2_mon_24_hour_perc, contact_hour_9to20_rece_min_tot_2_mon_24_hour_perc, contact_hour_21to8_rece_min_tot_2_mon_24_hour_perc, contact_hour_9to20_rece_cnt_2_wk_24_hour_perc, contact_hour_21to8_rece_cnt_2_wk_24_hour_perc, contact_hour_9to20_rece_min_tot_2_wk_24_hour_perc, contact_hour_21to8_rece_min_tot_2_wk_24_hour_perc, contact_hour_1to6_cnt_3_mon_perc, contact_hour_7to12_cnt_3_mon_perc, contact_hour_13to18_cnt_3_mon_perc, contact_hour_19to0_cnt_3_mon_perc, contact_hour_1to6_min_tot_3_mon_perc, contact_hour_7to12_min_tot_3_mon_perc, contact_hour_13to18_min_tot_3_mon_perc, contact_hour_19to0_min_tot_3_mon_perc, contact_hour_1to6_cnt_2_mon_perc, contact_hour_7to12_cnt_2_mon_perc, contact_hour_13to18_cnt_2_mon_perc, contact_hour_19to0_cnt_2_mon_perc, contact_hour_1to6_min_tot_2_mon_perc, contact_hour_7to12_min_tot_2_mon_perc, contact_hour_13to18_min_tot_2_mon_perc, contact_hour_19to0_min_tot_2_mon_perc, contact_hour_1to6_cnt_1_mon_perc, contact_hour_7to12_cnt_1_mon_perc, contact_hour_13to18_cnt_1_mon_perc, contact_hour_19to0_cnt_1_mon_perc, contact_hour_1to6_min_tot_1_mon_perc, contact_hour_7to12_min_tot_1_mon_perc, contact_hour_13to18_min_tot_1_mon_perc, contact_hour_19to0_min_tot_1_mon_perc, contact_hour_1to6_cnt_2_wk_perc, contact_hour_7to12_cnt_2_wk_perc, contact_hour_13to18_cnt_2_wk_perc, contact_hour_19to0_cnt_2_wk_perc, contact_hour_1to6_min_tot_2_wk_perc, contact_hour_7to12_min_tot_2_wk_perc, contact_hour_13to18_min_tot_2_wk_perc, contact_hour_19to0_min_tot_2_wk_perc, contact_hour_1to8_cnt_3_mon_perc, contact_hour_9to16_cnt_3_mon_perc, contact_hour_17to0_cnt_3_mon_perc, contact_hour_1to8_min_tot_3_mon_perc, contact_hour_9to16_min_tot_3_mon_perc, contact_hour_17to0_min_tot_3_mon_perc, contact_hour_1to8_cnt_2_mon_perc, contact_hour_9to16_cnt_2_mon_perc, contact_hour_17to0_cnt_2_mon_perc, contact_hour_1to8_min_tot_2_mon_perc, contact_hour_9to16_min_tot_2_mon_perc, contact_hour_17to0_min_tot_2_mon_perc, contact_hour_1to8_cnt_1_mon_perc, contact_hour_9to16_cnt_1_mon_perc, contact_hour_17to0_cnt_1_mon_perc, contact_hour_1to8_min_tot_1_mon_perc, contact_hour_9to16_min_tot_1_mon_perc, contact_hour_17to0_min_tot_1_mon_perc, contact_hour_1to8_cnt_2_wk_perc, contact_hour_9to16_cnt_2_wk_perc, contact_hour_17to0_cnt_2_wk_perc, contact_hour_1to8_min_tot_2_wk_perc, contact_hour_9to16_min_tot_2_wk_perc, contact_hour_17to0_min_tot_2_wk_perc, contact_hour_9to20_cnt_3_mon_perc, contact_hour_21to8_cnt_3_mon_perc, contact_hour_9to20_min_tot_3_mon_perc, contact_hour_21to8_min_tot_3_mon_perc, contact_hour_9to20_cnt_2_mon_perc, contact_hour_21to8_cnt_2_mon_perc, contact_hour_9to20_min_tot_2_mon_perc, contact_hour_21to8_min_tot_2_mon_perc, contact_hour_9to20_cnt_1_mon_perc, contact_hour_21to8_cnt_1_mon_perc, contact_hour_9to20_min_tot_1_mon_perc, contact_hour_21to8_min_tot_1_mon_perc, contact_hour_9to20_cnt_2_wk_perc, contact_hour_21to8_cnt_2_wk_perc, contact_hour_9to20_min_tot_2_wk_perc, contact_hour_21to8_min_tot_2_wk_perc, contact_hour_1to6_call_cnt_3_mon_perc, contact_hour_7to12_call_cnt_3_mon_perc, contact_hour_13to18_call_cnt_3_mon_perc, contact_hour_19to0_call_cnt_3_mon_perc, contact_hour_1to6_call_min_tot_3_mon_perc, contact_hour_7to12_call_min_tot_3_mon_perc, contact_hour_13to18_call_min_tot_3_mon_perc, contact_hour_19to0_call_min_tot_3_mon_perc, contact_hour_1to6_call_cnt_2_mon_perc, contact_hour_7to12_call_cnt_2_mon_perc, contact_hour_13to18_call_cnt_2_mon_perc, contact_hour_19to0_call_cnt_2_mon_perc, contact_hour_1to6_call_min_tot_2_mon_perc, contact_hour_7to12_call_min_tot_2_mon_perc, contact_hour_13to18_call_min_tot_2_mon_perc, contact_hour_19to0_call_min_tot_2_mon_perc, contact_hour_1to6_call_cnt_1_mon_perc, contact_hour_7to12_call_cnt_1_mon_perc, contact_hour_13to18_call_cnt_1_mon_perc, contact_hour_19to0_call_cnt_1_mon_perc, contact_hour_1to6_call_min_tot_1_mon_perc, contact_hour_7to12_call_min_tot_1_mon_perc, contact_hour_13to18_call_min_tot_1_mon_perc, contact_hour_19to0_call_min_tot_1_mon_perc, contact_hour_1to6_call_cnt_2_wk_perc, contact_hour_7to12_call_cnt_2_wk_perc, contact_hour_13to18_call_cnt_2_wk_perc, contact_hour_19to0_call_cnt_2_wk_perc, contact_hour_1to6_call_min_tot_2_wk_perc, contact_hour_7to12_call_min_tot_2_wk_perc, contact_hour_13to18_call_min_tot_2_wk_perc, contact_hour_19to0_call_min_tot_2_wk_perc, contact_hour_1to8_call_cnt_3_mon_perc, contact_hour_9to16_call_cnt_3_mon_perc, contact_hour_17to0_call_cnt_3_mon_perc, contact_hour_1to8_call_min_tot_3_mon_perc, contact_hour_9to16_call_min_tot_3_mon_perc, contact_hour_17to0_call_min_tot_3_mon_perc, contact_hour_1to8_call_cnt_2_mon_perc, contact_hour_9to16_call_cnt_2_mon_perc, contact_hour_17to0_call_cnt_2_mon_perc, contact_hour_1to8_call_min_tot_2_mon_perc, contact_hour_9to16_call_min_tot_2_mon_perc, contact_hour_17to0_call_min_tot_2_mon_perc, contact_hour_1to8_call_cnt_1_mon_perc, contact_hour_9to16_call_cnt_1_mon_perc, contact_hour_17to0_call_cnt_1_mon_perc, contact_hour_1to8_call_min_tot_1_mon_perc, contact_hour_9to16_call_min_tot_1_mon_perc, contact_hour_17to0_call_min_tot_1_mon_perc, contact_hour_1to8_call_cnt_2_wk_perc, contact_hour_9to16_call_cnt_2_wk_perc, contact_hour_17to0_call_cnt_2_wk_perc, contact_hour_1to8_call_min_tot_2_wk_perc, contact_hour_9to16_call_min_tot_2_wk_perc, contact_hour_17to0_call_min_tot_2_wk_perc, contact_hour_9to20_call_cnt_3_mon_perc, contact_hour_21to8_call_cnt_3_mon_perc, contact_hour_9to20_call_min_tot_3_mon_perc, contact_hour_21to8_call_min_tot_3_mon_perc, contact_hour_9to20_call_cnt_2_mon_perc, contact_hour_21to8_call_cnt_2_mon_perc, contact_hour_9to20_call_min_tot_2_mon_perc, contact_hour_21to8_call_min_tot_2_mon_perc, contact_hour_9to20_call_cnt_1_mon_perc, contact_hour_21to8_call_cnt_1_mon_perc, contact_hour_9to20_call_min_tot_1_mon_perc, contact_hour_21to8_call_min_tot_1_mon_perc, contact_hour_9to20_call_cnt_2_wk_perc, contact_hour_21to8_call_cnt_2_wk_perc, contact_hour_9to20_call_min_tot_2_wk_perc, contact_hour_21to8_call_min_tot_2_wk_perc, contact_hour_1to6_rece_cnt_3_mon_perc, contact_hour_7to12_rece_cnt_3_mon_perc, contact_hour_13to18_rece_cnt_3_mon_perc, contact_hour_19to0_rece_cnt_3_mon_perc, contact_hour_1to6_rece_min_tot_3_mon_perc, contact_hour_7to12_rece_min_tot_3_mon_perc, contact_hour_13to18_rece_min_tot_3_mon_perc, contact_hour_19to0_rece_min_tot_3_mon_perc, contact_hour_1to6_rece_cnt_2_mon_perc, contact_hour_7to12_rece_cnt_2_mon_perc, contact_hour_13to18_rece_cnt_2_mon_perc, contact_hour_19to0_rece_cnt_2_mon_perc, contact_hour_1to6_rece_min_tot_2_mon_perc, contact_hour_7to12_rece_min_tot_2_mon_perc, contact_hour_13to18_rece_min_tot_2_mon_perc, contact_hour_19to0_rece_min_tot_2_mon_perc, contact_hour_1to6_rece_cnt_1_mon_perc, contact_hour_7to12_rece_cnt_1_mon_perc, contact_hour_13to18_rece_cnt_1_mon_perc, contact_hour_19to0_rece_cnt_1_mon_perc, contact_hour_1to6_rece_min_tot_1_mon_perc, contact_hour_7to12_rece_min_tot_1_mon_perc, contact_hour_13to18_rece_min_tot_1_mon_perc, contact_hour_19to0_rece_min_tot_1_mon_perc, contact_hour_1to6_rece_cnt_2_wk_perc, contact_hour_7to12_rece_cnt_2_wk_perc, contact_hour_13to18_rece_cnt_2_wk_perc, contact_hour_19to0_rece_cnt_2_wk_perc, contact_hour_1to6_rece_min_tot_2_wk_perc, contact_hour_7to12_rece_min_tot_2_wk_perc, contact_hour_13to18_rece_min_tot_2_wk_perc, contact_hour_19to0_rece_min_tot_2_wk_perc, contact_hour_1to8_rece_cnt_3_mon_perc, contact_hour_9to16_rece_cnt_3_mon_perc, contact_hour_17to0_rece_cnt_3_mon_perc, contact_hour_1to8_rece_min_tot_3_mon_perc, contact_hour_9to16_rece_min_tot_3_mon_perc, contact_hour_17to0_rece_min_tot_3_mon_perc, contact_hour_1to8_rece_cnt_2_mon_perc, contact_hour_9to16_rece_cnt_2_mon_perc, contact_hour_17to0_rece_cnt_2_mon_perc, contact_hour_1to8_rece_min_tot_2_mon_perc, contact_hour_9to16_rece_min_tot_2_mon_perc, contact_hour_17to0_rece_min_tot_2_mon_perc, contact_hour_1to8_rece_cnt_1_mon_perc, contact_hour_9to16_rece_cnt_1_mon_perc, contact_hour_17to0_rece_cnt_1_mon_perc, contact_hour_1to8_rece_min_tot_1_mon_perc, contact_hour_9to16_rece_min_tot_1_mon_perc, contact_hour_17to0_rece_min_tot_1_mon_perc, contact_hour_1to8_rece_cnt_2_wk_perc, contact_hour_9to16_rece_cnt_2_wk_perc, contact_hour_17to0_rece_cnt_2_wk_perc, contact_hour_1to8_rece_min_tot_2_wk_perc, contact_hour_9to16_rece_min_tot_2_wk_perc, contact_hour_17to0_rece_min_tot_2_wk_perc, contact_hour_9to20_rece_cnt_3_mon_perc, contact_hour_21to8_rece_cnt_3_mon_perc, contact_hour_9to20_rece_min_tot_3_mon_perc, contact_hour_21to8_rece_min_tot_3_mon_perc, contact_hour_9to20_rece_cnt_2_mon_perc, contact_hour_21to8_rece_cnt_2_mon_perc, contact_hour_9to20_rece_min_tot_2_mon_perc, contact_hour_21to8_rece_min_tot_2_mon_perc, contact_hour_9to20_rece_cnt_1_mon_perc, contact_hour_21to8_rece_cnt_1_mon_perc, contact_hour_9to20_rece_min_tot_1_mon_perc, contact_hour_21to8_rece_min_tot_1_mon_perc, contact_hour_9to20_rece_cnt_2_wk_perc, contact_hour_21to8_rece_cnt_2_wk_perc, contact_hour_9to20_rece_min_tot_2_wk_perc, contact_hour_21to8_rece_min_tot_2_wk_perc, contact_hour_1to6_call_cnt_inout_perc, contact_hour_7to12_call_cnt_inout_perc, contact_hour_13to18_call_cnt_inout_perc, contact_hour_19to0_call_cnt_inout_perc, contact_hour_1to6_call_min_tot_inout_perc, contact_hour_7to12_call_min_tot_inout_perc, contact_hour_13to18_call_min_tot_inout_perc, contact_hour_19to0_call_min_tot_inout_perc, contact_hour_1to6_call_cnt_6_mon_inout_perc, contact_hour_7to12_call_cnt_6_mon_inout_perc, contact_hour_13to18_call_cnt_6_mon_inout_perc, contact_hour_19to0_call_cnt_6_mon_inout_perc, contact_hour_1to6_call_min_tot_6_mon_inout_perc, contact_hour_7to12_call_min_tot_6_mon_inout_perc, contact_hour_13to18_call_min_tot_6_mon_inout_perc, contact_hour_19to0_call_min_tot_6_mon_inout_perc, contact_hour_1to6_call_cnt_3_mon_inout_perc, contact_hour_7to12_call_cnt_3_mon_inout_perc, contact_hour_13to18_call_cnt_3_mon_inout_perc, contact_hour_19to0_call_cnt_3_mon_inout_perc, contact_hour_1to6_call_min_tot_3_mon_inout_perc, contact_hour_7to12_call_min_tot_3_mon_inout_perc, contact_hour_13to18_call_min_tot_3_mon_inout_perc, contact_hour_19to0_call_min_tot_3_mon_inout_perc, contact_hour_1to6_call_cnt_2_mon_inout_perc, contact_hour_7to12_call_cnt_2_mon_inout_perc, contact_hour_13to18_call_cnt_2_mon_inout_perc, contact_hour_19to0_call_cnt_2_mon_inout_perc, contact_hour_1to6_call_min_tot_2_mon_inout_perc, contact_hour_7to12_call_min_tot_2_mon_inout_perc, contact_hour_13to18_call_min_tot_2_mon_inout_perc, contact_hour_19to0_call_min_tot_2_mon_inout_perc, contact_hour_1to6_call_cnt_1_mon_inout_perc, contact_hour_7to12_call_cnt_1_mon_inout_perc, contact_hour_13to18_call_cnt_1_mon_inout_perc, contact_hour_19to0_call_cnt_1_mon_inout_perc, contact_hour_1to6_call_min_tot_1_mon_inout_perc, contact_hour_7to12_call_min_tot_1_mon_inout_perc, contact_hour_13to18_call_min_tot_1_mon_inout_perc, contact_hour_19to0_call_min_tot_1_mon_inout_perc, contact_hour_1to6_call_cnt_2_wk_inout_perc, contact_hour_7to12_call_cnt_2_wk_inout_perc, contact_hour_13to18_call_cnt_2_wk_inout_perc, contact_hour_19to0_call_cnt_2_wk_inout_perc, contact_hour_1to6_call_min_tot_2_wk_inout_perc, contact_hour_7to12_call_min_tot_2_wk_inout_perc, contact_hour_13to18_call_min_tot_2_wk_inout_perc, contact_hour_19to0_call_min_tot_2_wk_inout_perc, contact_hour_1to8_call_cnt_inout_perc, contact_hour_9to16_call_cnt_inout_perc, contact_hour_17to0_call_cnt_inout_perc, contact_hour_1to8_call_min_tot_inout_perc, contact_hour_9to16_call_min_tot_inout_perc, contact_hour_17to0_call_min_tot_inout_perc, contact_hour_1to8_call_cnt_6_mon_inout_perc, contact_hour_9to16_call_cnt_6_mon_inout_perc, contact_hour_17to0_call_cnt_6_mon_inout_perc, contact_hour_1to8_call_min_tot_6_mon_inout_perc, contact_hour_9to16_call_min_tot_6_mon_inout_perc, contact_hour_17to0_call_min_tot_6_mon_inout_perc, contact_hour_1to8_call_cnt_3_mon_inout_perc, contact_hour_9to16_call_cnt_3_mon_inout_perc, contact_hour_17to0_call_cnt_3_mon_inout_perc, contact_hour_1to8_call_min_tot_3_mon_inout_perc, contact_hour_9to16_call_min_tot_3_mon_inout_perc, contact_hour_17to0_call_min_tot_3_mon_inout_perc, contact_hour_1to8_call_cnt_2_mon_inout_perc, contact_hour_9to16_call_cnt_2_mon_inout_perc, contact_hour_17to0_call_cnt_2_mon_inout_perc, contact_hour_1to8_call_min_tot_2_mon_inout_perc, contact_hour_9to16_call_min_tot_2_mon_inout_perc, contact_hour_17to0_call_min_tot_2_mon_inout_perc, contact_hour_1to8_call_cnt_1_mon_inout_perc, contact_hour_9to16_call_cnt_1_mon_inout_perc, contact_hour_17to0_call_cnt_1_mon_inout_perc, contact_hour_1to8_call_min_tot_1_mon_inout_perc, contact_hour_9to16_call_min_tot_1_mon_inout_perc, contact_hour_17to0_call_min_tot_1_mon_inout_perc, contact_hour_1to8_call_cnt_2_wk_inout_perc, contact_hour_9to16_call_cnt_2_wk_inout_perc, contact_hour_17to0_call_cnt_2_wk_inout_perc, contact_hour_1to8_call_min_tot_2_wk_inout_perc, contact_hour_9to16_call_min_tot_2_wk_inout_perc, contact_hour_17to0_call_min_tot_2_wk_inout_perc, contact_hour_9to20_call_cnt_inout_perc, contact_hour_21to8_call_cnt_inout_perc, contact_hour_9to20_call_min_tot_inout_perc, contact_hour_21to8_call_min_tot_inout_perc, contact_hour_9to20_call_cnt_6_mon_inout_perc, contact_hour_21to8_call_cnt_6_mon_inout_perc, contact_hour_9to20_call_min_tot_6_mon_inout_perc, contact_hour_21to8_call_min_tot_6_mon_inout_perc, contact_hour_9to20_call_cnt_3_mon_inout_perc, contact_hour_21to8_call_cnt_3_mon_inout_perc, contact_hour_9to20_call_min_tot_3_mon_inout_perc, contact_hour_21to8_call_min_tot_3_mon_inout_perc, contact_hour_9to20_call_cnt_2_mon_inout_perc, contact_hour_21to8_call_cnt_2_mon_inout_perc, contact_hour_9to20_call_min_tot_2_mon_inout_perc, contact_hour_21to8_call_min_tot_2_mon_inout_perc, contact_hour_9to20_call_cnt_1_mon_inout_perc, contact_hour_21to8_call_cnt_1_mon_inout_perc, contact_hour_9to20_call_min_tot_1_mon_inout_perc, contact_hour_21to8_call_min_tot_1_mon_inout_perc, contact_hour_9to20_call_cnt_2_wk_inout_perc, contact_hour_21to8_call_cnt_2_wk_inout_perc, contact_hour_9to20_call_min_tot_2_wk_inout_perc, contact_hour_21to8_call_min_tot_2_wk_inout_perc, contact_weekday_min_avg, contact_weekday_min_avg_6_mon, contact_weekday_min_avg_3_mon, contact_weekday_min_avg_2_mon, contact_weekday_min_avg_1_mon, contact_weekday_min_avg_2_wk, contact_weekend_min_avg, contact_weekend_min_avg_6_mon, contact_weekend_min_avg_3_mon, contact_weekend_min_avg_2_mon, contact_weekend_min_avg_1_mon, contact_weekend_min_avg_2_wk, contact_weekday_call_min_avg, contact_weekday_call_min_avg_6_mon, contact_weekday_call_min_avg_3_mon, contact_weekday_call_min_avg_2_mon, contact_weekday_call_min_avg_1_mon, contact_weekday_call_min_avg_2_wk, contact_weekend_call_min_avg, contact_weekend_call_min_avg_6_mon, contact_weekend_call_min_avg_3_mon, contact_weekend_call_min_avg_2_mon, contact_weekend_call_min_avg_1_mon, contact_weekend_call_min_avg_2_wk, contact_weekday_rece_min_avg, contact_weekday_rece_min_avg_6_mon, contact_weekday_rece_min_avg_3_mon, contact_weekday_rece_min_avg_2_mon, contact_weekday_rece_min_avg_1_mon, contact_weekday_rece_min_avg_2_wk, contact_weekend_rece_min_avg, contact_weekend_rece_min_avg_6_mon, contact_weekend_rece_min_avg_3_mon, contact_weekend_rece_min_avg_2_mon, contact_weekend_rece_min_avg_1_mon, contact_weekend_rece_min_avg_2_wk, contact_weekday_cnt_3_mon_perc, contact_weekday_min_tot_3_mon_perc, contact_weekday_call_cnt_3_mon_perc, contact_weekday_rece_cnt_3_mon_perc, contact_weekday_call_min_tot_3_mon_perc, contact_weekday_rece_min_tot_3_mon_perc, contact_weekday_cnt_2_mon_perc, contact_weekday_min_tot_2_mon_perc, contact_weekday_call_cnt_2_mon_perc, contact_weekday_rece_cnt_2_mon_perc, contact_weekday_call_min_tot_2_mon_perc, contact_weekday_rece_min_tot_2_mon_perc, contact_weekday_cnt_1_mon_perc, contact_weekday_min_tot_1_mon_perc, contact_weekday_call_cnt_1_mon_perc, contact_weekday_rece_cnt_1_mon_perc, contact_weekday_call_min_tot_1_mon_perc, contact_weekday_rece_min_tot_1_mon_perc, contact_weekday_cnt_2_wk_perc, contact_weekday_min_tot_2_wk_perc, contact_weekday_call_cnt_2_wk_perc, contact_weekday_rece_cnt_2_wk_perc, contact_weekday_call_min_tot_2_wk_perc, contact_weekday_rece_min_tot_2_wk_perc, contact_weekend_cnt_3_mon_perc, contact_weekend_min_tot_3_mon_perc, contact_weekend_call_cnt_3_mon_perc, contact_weekend_rece_cnt_3_mon_perc, contact_weekend_call_min_tot_3_mon_perc, contact_weekend_rece_min_tot_3_mon_perc, contact_weekend_cnt_2_mon_perc, contact_weekend_min_tot_2_mon_perc, contact_weekend_call_cnt_2_mon_perc, contact_weekend_rece_cnt_2_mon_perc, contact_weekend_call_min_tot_2_mon_perc, contact_weekend_rece_min_tot_2_mon_perc, contact_weekend_cnt_1_mon_perc, contact_weekend_min_tot_1_mon_perc, contact_weekend_call_cnt_1_mon_perc, contact_weekend_rece_cnt_1_mon_perc, contact_weekend_call_min_tot_1_mon_perc, contact_weekend_rece_min_tot_1_mon_perc, contact_weekend_cnt_2_wk_perc, contact_weekend_min_tot_2_wk_perc, contact_weekend_call_cnt_2_wk_perc, contact_weekend_rece_cnt_2_wk_perc, contact_weekend_call_min_tot_2_wk_perc, contact_weekend_rece_min_tot_2_wk_perc, contact_weekday_cnt_week_perc, contact_weekday_min_tot_week_perc, contact_weekday_call_cnt_week_perc, contact_weekday_rece_cnt_week_perc, contact_weekday_call_min_tot_week_perc, contact_weekday_rece_min_tot_week_perc, contact_weekday_cnt_6_mon_week_perc, contact_weekday_min_tot_6_mon_week_perc, contact_weekday_call_cnt_6_mon_week_perc, contact_weekday_rece_cnt_6_mon_week_perc, contact_weekday_call_min_tot_6_mon_week_perc, contact_weekday_rece_min_tot_6_mon_week_perc, contact_weekday_cnt_3_mon_week_perc, contact_weekday_min_tot_3_mon_week_perc, contact_weekday_call_cnt_3_mon_week_perc, contact_weekday_rece_cnt_3_mon_week_perc, contact_weekday_call_min_tot_3_mon_week_perc, contact_weekday_rece_min_tot_3_mon_week_perc, contact_weekday_cnt_2_mon_week_perc, contact_weekday_min_tot_2_mon_week_perc, contact_weekday_call_cnt_2_mon_week_perc, contact_weekday_rece_cnt_2_mon_week_perc, contact_weekday_call_min_tot_2_mon_week_perc, contact_weekday_rece_min_tot_2_mon_week_perc, contact_weekday_cnt_1_mon_week_perc, contact_weekday_min_tot_1_mon_week_perc, contact_weekday_call_cnt_1_mon_week_perc, contact_weekday_rece_cnt_1_mon_week_perc, contact_weekday_call_min_tot_1_mon_week_perc, contact_weekday_rece_min_tot_1_mon_week_perc, contact_weekday_cnt_2_wk_week_perc, contact_weekday_min_tot_2_wk_week_perc, contact_weekday_call_cnt_2_wk_week_perc, contact_weekday_rece_cnt_2_wk_week_perc, contact_weekday_call_min_tot_2_wk_week_perc, contact_weekday_rece_min_tot_2_wk_week_perc, contact_min_over_15s_min_avg, contact_min_over_15s_call_min_avg, contact_min_over_15s_rece_min_avg, contact_min_over_30s_min_avg, contact_min_over_30s_call_min_avg, contact_min_over_30s_rece_min_avg, contact_min_over_60s_min_avg, contact_min_over_60s_call_min_avg, contact_min_over_60s_rece_min_avg, contact_min_over_15s_min_avg_6_mon, contact_min_over_15s_call_min_avg_6_mon, contact_min_over_15s_rece_min_avg_6_mon, contact_min_over_30s_min_avg_6_mon, contact_min_over_30s_call_min_avg_6_mon, contact_min_over_30s_rece_min_avg_6_mon, contact_min_over_60s_min_avg_6_mon, contact_min_over_60s_call_min_avg_6_mon, contact_min_over_60s_rece_min_avg_6_mon, contact_min_over_15s_min_avg_3_mon, contact_min_over_15s_call_min_avg_3_mon, contact_min_over_15s_rece_min_avg_3_mon, contact_min_over_30s_min_avg_3_mon, contact_min_over_30s_call_min_avg_3_mon, contact_min_over_30s_rece_min_avg_3_mon, contact_min_over_60s_min_avg_3_mon, contact_min_over_60s_call_min_avg_3_mon, contact_min_over_60s_rece_min_avg_3_mon, contact_min_over_15s_min_avg_2_mon, contact_min_over_15s_call_min_avg_2_mon, contact_min_over_15s_rece_min_avg_2_mon, contact_min_over_30s_min_avg_2_mon, contact_min_over_30s_call_min_avg_2_mon, contact_min_over_30s_rece_min_avg_2_mon, contact_min_over_60s_min_avg_2_mon, contact_min_over_60s_call_min_avg_2_mon, contact_min_over_60s_rece_min_avg_2_mon, contact_min_over_15s_min_avg_1_mon, contact_min_over_15s_call_min_avg_1_mon, contact_min_over_15s_rece_min_avg_1_mon, contact_min_over_30s_min_avg_1_mon, contact_min_over_30s_call_min_avg_1_mon, contact_min_over_30s_rece_min_avg_1_mon, contact_min_over_60s_min_avg_1_mon, contact_min_over_60s_call_min_avg_1_mon, contact_min_over_60s_rece_min_avg_1_mon, contact_min_over_15s_min_avg_2_wk, contact_min_over_15s_call_min_avg_2_wk, contact_min_over_15s_rece_min_avg_2_wk, contact_min_over_30s_min_avg_2_wk, contact_min_over_30s_call_min_avg_2_wk, contact_min_over_30s_rece_min_avg_2_wk, contact_min_over_60s_min_avg_2_wk, contact_min_over_60s_call_min_avg_2_wk, contact_min_over_60s_rece_min_avg_2_wk, contact_min_over_15s_call_cnt_inout_perc, contact_min_over_15s_rece_cnt_inout_perc, contact_min_over_30s_call_cnt_inout_perc, contact_min_over_30s_rece_cnt_inout_perc, contact_min_over_60s_call_cnt_inout_perc, contact_min_over_60s_rece_cnt_inout_perc, contact_min_over_15s_call_cnt_6_mon_inout_perc, contact_min_over_15s_rece_cnt_6_mon_inout_perc, contact_min_over_30s_call_cnt_6_mon_inout_perc, contact_min_over_30s_rece_cnt_6_mon_inout_perc, contact_min_over_60s_call_cnt_6_mon_inout_perc, contact_min_over_60s_rece_cnt_6_mon_inout_perc, contact_min_over_15s_call_cnt_3_mon_inout_perc, contact_min_over_15s_rece_cnt_3_mon_inout_perc, contact_min_over_30s_call_cnt_3_mon_inout_perc, contact_min_over_30s_rece_cnt_3_mon_inout_perc, contact_min_over_60s_call_cnt_3_mon_inout_perc, contact_min_over_60s_rece_cnt_3_mon_inout_perc, contact_min_over_15s_call_cnt_2_mon_inout_perc, contact_min_over_15s_rece_cnt_2_mon_inout_perc, contact_min_over_30s_call_cnt_2_mon_inout_perc, contact_min_over_30s_rece_cnt_2_mon_inout_perc, contact_min_over_60s_call_cnt_2_mon_inout_perc, contact_min_over_60s_rece_cnt_2_mon_inout_perc, contact_min_over_15s_call_cnt_1_mon_inout_perc, contact_min_over_15s_rece_cnt_1_mon_inout_perc, contact_min_over_30s_call_cnt_1_mon_inout_perc, contact_min_over_30s_rece_cnt_1_mon_inout_perc, contact_min_over_60s_call_cnt_1_mon_inout_perc, contact_min_over_60s_rece_cnt_1_mon_inout_perc, contact_min_over_15s_call_cnt_2_wk_inout_perc, contact_min_over_15s_rece_cnt_2_wk_inout_perc, contact_min_over_30s_call_cnt_2_wk_inout_perc, contact_min_over_30s_rece_cnt_2_wk_inout_perc, contact_min_over_60s_call_cnt_2_wk_inout_perc, contact_min_over_60s_rece_cnt_2_wk_inout_perc, contact_min_over_15s_cnt_3_mon_perc, contact_min_over_15s_min_tot_3_mon_perc, contact_min_over_15s_call_cnt_3_mon_perc, contact_min_over_15s_call_min_tot_3_mon_perc, contact_min_over_15s_rece_cnt_3_mon_perc, contact_min_over_15s_rece_min_tot_3_mon_perc, contact_min_over_30s_cnt_3_mon_perc, contact_min_over_30s_min_tot_3_mon_perc, contact_min_over_30s_call_cnt_3_mon_perc, contact_min_over_30s_call_min_tot_3_mon_perc, contact_min_over_30s_rece_cnt_3_mon_perc, contact_min_over_30s_rece_min_tot_3_mon_perc, contact_min_over_60s_cnt_3_mon_perc, contact_min_over_60s_min_tot_3_mon_perc, contact_min_over_60s_call_cnt_3_mon_perc, contact_min_over_60s_call_min_tot_3_mon_perc, contact_min_over_60s_rece_cnt_3_mon_perc, contact_min_over_60s_rece_min_tot_3_mon_perc, contact_min_over_15s_cnt_2_mon_perc, contact_min_over_15s_min_tot_2_mon_perc, contact_min_over_15s_call_cnt_2_mon_perc, contact_min_over_15s_call_min_tot_2_mon_perc, contact_min_over_15s_rece_cnt_2_mon_perc, contact_min_over_15s_rece_min_tot_2_mon_perc, contact_min_over_30s_cnt_2_mon_perc, contact_min_over_30s_min_tot_2_mon_perc, contact_min_over_30s_call_cnt_2_mon_perc, contact_min_over_30s_call_min_tot_2_mon_perc, contact_min_over_30s_rece_cnt_2_mon_perc, contact_min_over_30s_rece_min_tot_2_mon_perc, contact_min_over_60s_cnt_2_mon_perc, contact_min_over_60s_min_tot_2_mon_perc, contact_min_over_60s_call_cnt_2_mon_perc, contact_min_over_60s_call_min_tot_2_mon_perc, contact_min_over_60s_rece_cnt_2_mon_perc, contact_min_over_60s_rece_min_tot_2_mon_perc, contact_min_over_15s_cnt_1_mon_perc, contact_min_over_15s_min_tot_1_mon_perc, contact_min_over_15s_call_cnt_1_mon_perc, contact_min_over_15s_call_min_tot_1_mon_perc, contact_min_over_15s_rece_cnt_1_mon_perc, contact_min_over_15s_rece_min_tot_1_mon_perc, contact_min_over_30s_cnt_1_mon_perc, contact_min_over_30s_min_tot_1_mon_perc, contact_min_over_30s_call_cnt_1_mon_perc, contact_min_over_30s_call_min_tot_1_mon_perc, contact_min_over_30s_rece_cnt_1_mon_perc, contact_min_over_30s_rece_min_tot_1_mon_perc, contact_min_over_60s_cnt_1_mon_perc, contact_min_over_60s_min_tot_1_mon_perc, contact_min_over_60s_call_cnt_1_mon_perc, contact_min_over_60s_call_min_tot_1_mon_perc, contact_min_over_60s_rece_cnt_1_mon_perc, contact_min_over_60s_rece_min_tot_1_mon_perc, contact_min_over_15s_cnt_2_wk_perc, contact_min_over_15s_min_tot_2_wk_perc, contact_min_over_15s_call_cnt_2_wk_perc, contact_min_over_15s_call_min_tot_2_wk_perc, contact_min_over_15s_rece_cnt_2_wk_perc, contact_min_over_15s_rece_min_tot_2_wk_perc, contact_min_over_30s_cnt_2_wk_perc, contact_min_over_30s_min_tot_2_wk_perc, contact_min_over_30s_call_cnt_2_wk_perc, contact_min_over_30s_call_min_tot_2_wk_perc, contact_min_over_30s_rece_cnt_2_wk_perc, contact_min_over_30s_rece_min_tot_2_wk_perc, contact_min_over_60s_cnt_2_wk_perc, contact_min_over_60s_min_tot_2_wk_perc, contact_min_over_60s_call_cnt_2_wk_perc, contact_min_over_60s_call_min_tot_2_wk_perc, contact_min_over_60s_rece_cnt_2_wk_perc, contact_min_over_60s_rece_min_tot_2_wk_perc, contact_min_over_15s_cnt_min_perc, contact_min_over_15s_min_tot_min_perc, contact_min_over_15s_call_cnt_min_perc, contact_min_over_15s_call_min_tot_min_perc, contact_min_over_15s_rece_cnt_min_perc, contact_min_over_15s_rece_min_tot_min_perc, contact_min_over_30s_cnt_min_perc, contact_min_over_30s_min_tot_min_perc, contact_min_over_30s_call_cnt_min_perc, contact_min_over_30s_call_min_tot_min_perc, contact_min_over_30s_rece_cnt_min_perc, contact_min_over_30s_rece_min_tot_min_perc, contact_min_over_60s_cnt_min_perc, contact_min_over_60s_min_tot_min_perc, contact_min_over_60s_call_cnt_min_perc, contact_min_over_60s_call_min_tot_min_perc, contact_min_over_60s_rece_cnt_min_perc, contact_min_over_60s_rece_min_tot_min_perc, contact_min_over_15s_cnt_6_mon_min_perc, contact_min_over_15s_min_tot_6_mon_min_perc, contact_min_over_15s_call_cnt_6_mon_min_perc, contact_min_over_15s_call_min_tot_6_mon_min_perc, contact_min_over_15s_rece_cnt_6_mon_min_perc, contact_min_over_15s_rece_min_tot_6_mon_min_perc, contact_min_over_30s_cnt_6_mon_min_perc, contact_min_over_30s_min_tot_6_mon_min_perc, contact_min_over_30s_call_cnt_6_mon_min_perc, contact_min_over_30s_call_min_tot_6_mon_min_perc, contact_min_over_30s_rece_cnt_6_mon_min_perc, contact_min_over_30s_rece_min_tot_6_mon_min_perc, contact_min_over_60s_cnt_6_mon_min_perc, contact_min_over_60s_min_tot_6_mon_min_perc, contact_min_over_60s_call_cnt_6_mon_min_perc, contact_min_over_60s_call_min_tot_6_mon_min_perc, contact_min_over_60s_rece_cnt_6_mon_min_perc, contact_min_over_60s_rece_min_tot_6_mon_min_perc, contact_min_over_15s_cnt_3_mon_min_perc, contact_min_over_15s_min_tot_3_mon_min_perc, contact_min_over_15s_call_cnt_3_mon_min_perc, contact_min_over_15s_call_min_tot_3_mon_min_perc, contact_min_over_15s_rece_cnt_3_mon_min_perc, contact_min_over_15s_rece_min_tot_3_mon_min_perc, contact_min_over_30s_cnt_3_mon_min_perc, contact_min_over_30s_min_tot_3_mon_min_perc, contact_min_over_30s_call_cnt_3_mon_min_perc, contact_min_over_30s_call_min_tot_3_mon_min_perc, contact_min_over_30s_rece_cnt_3_mon_min_perc, contact_min_over_30s_rece_min_tot_3_mon_min_perc, contact_min_over_60s_cnt_3_mon_min_perc, contact_min_over_60s_min_tot_3_mon_min_perc, contact_min_over_60s_call_cnt_3_mon_min_perc, contact_min_over_60s_call_min_tot_3_mon_min_perc, contact_min_over_60s_rece_cnt_3_mon_min_perc, contact_min_over_60s_rece_min_tot_3_mon_min_perc, contact_min_over_15s_cnt_2_mon_min_perc, contact_min_over_15s_min_tot_2_mon_min_perc, contact_min_over_15s_call_cnt_2_mon_min_perc, contact_min_over_15s_call_min_tot_2_mon_min_perc, contact_min_over_15s_rece_cnt_2_mon_min_perc, contact_min_over_15s_rece_min_tot_2_mon_min_perc, contact_min_over_30s_cnt_2_mon_min_perc, contact_min_over_30s_min_tot_2_mon_min_perc, contact_min_over_30s_call_cnt_2_mon_min_perc, contact_min_over_30s_call_min_tot_2_mon_min_perc, contact_min_over_30s_rece_cnt_2_mon_min_perc, contact_min_over_30s_rece_min_tot_2_mon_min_perc, contact_min_over_60s_cnt_2_mon_min_perc, contact_min_over_60s_min_tot_2_mon_min_perc, contact_min_over_60s_call_cnt_2_mon_min_perc, contact_min_over_60s_call_min_tot_2_mon_min_perc, contact_min_over_60s_rece_cnt_2_mon_min_perc, contact_min_over_60s_rece_min_tot_2_mon_min_perc, contact_min_over_15s_cnt_1_mon_min_perc, contact_min_over_15s_min_tot_1_mon_min_perc, contact_min_over_15s_call_cnt_1_mon_min_perc, contact_min_over_15s_call_min_tot_1_mon_min_perc, contact_min_over_15s_rece_cnt_1_mon_min_perc, contact_min_over_15s_rece_min_tot_1_mon_min_perc, contact_min_over_30s_cnt_1_mon_min_perc, contact_min_over_30s_min_tot_1_mon_min_perc, contact_min_over_30s_call_cnt_1_mon_min_perc, contact_min_over_30s_call_min_tot_1_mon_min_perc, contact_min_over_30s_rece_cnt_1_mon_min_perc, contact_min_over_30s_rece_min_tot_1_mon_min_perc, contact_min_over_60s_cnt_1_mon_min_perc, contact_min_over_60s_min_tot_1_mon_min_perc, contact_min_over_60s_call_cnt_1_mon_min_perc, contact_min_over_60s_call_min_tot_1_mon_min_perc, contact_min_over_60s_rece_cnt_1_mon_min_perc, contact_min_over_60s_rece_min_tot_1_mon_min_perc, contact_min_over_15s_cnt_2_wk_min_perc, contact_min_over_15s_min_tot_2_wk_min_perc, contact_min_over_15s_call_cnt_2_wk_min_perc, contact_min_over_15s_call_min_tot_2_wk_min_perc, contact_min_over_15s_rece_cnt_2_wk_min_perc, contact_min_over_15s_rece_min_tot_2_wk_min_perc, contact_min_over_30s_cnt_2_wk_min_perc, contact_min_over_30s_min_tot_2_wk_min_perc, contact_min_over_30s_call_cnt_2_wk_min_perc, contact_min_over_30s_call_min_tot_2_wk_min_perc, contact_min_over_30s_rece_cnt_2_wk_min_perc, contact_min_over_30s_rece_min_tot_2_wk_min_perc, contact_min_over_60s_cnt_2_wk_min_perc, contact_min_over_60s_min_tot_2_wk_min_perc, contact_min_over_60s_call_cnt_2_wk_min_perc, contact_min_over_60s_call_min_tot_2_wk_min_perc, contact_min_over_60s_rece_cnt_2_wk_min_perc, contact_min_over_60s_rece_min_tot_2_wk_min_perc, contact_weekday_min_avg_2_wk_1_mon_diff, contact_weekday_min_avg_1_mon_2_mon_diff, contact_weekday_min_avg_2_mon_3_mon_diff, contact_weekday_min_avg_3_mon_6_mon_diff,contact_weekend_min_avg_2_wk_1_mon_diff, contact_weekend_min_avg_1_mon_2_mon_diff, contact_weekend_min_avg_2_mon_3_mon_diff, contact_weekend_min_avg_3_mon_6_mon_diff, contact_weekday_weekend_min_avg_diff, contact_weekday_call_min_avg_2_wk_1_mon_diff, contact_weekday_call_min_avg_1_mon_2_mon_diff,contact_weekday_call_min_avg_2_mon_3_mon_diff,contact_weekday_call_min_avg_3_mon_6_mon_diff, contact_weekday_rece_min_avg_2_wk_1_mon_diff, contact_weekday_rece_min_avg_1_mon_2_mon_diff,contact_weekday_rece_min_avg_2_mon_3_mon_diff,contact_weekday_rece_min_avg_3_mon_6_mon_diff,contact_weekend_call_min_avg_2_wk_1_mon_diff, contact_weekend_call_min_avg_1_mon_2_mon_diff,contact_weekend_call_min_avg_2_mon_3_mon_diff,contact_weekend_call_min_avg_3_mon_6_mon_diff, contact_weekend_rece_min_avg_2_wk_1_mon_diff, contact_weekend_rece_min_avg_1_mon_2_mon_diff,contact_weekend_rece_min_avg_2_mon_3_mon_diff,contact_weekend_rece_min_avg_3_mon_6_mon_diff, contact_weekday_weekend_rece_min_avg_diff, contact_weekday_weekend_call_min_avg_diff, contact_week_call_rece_cnt_diff, contact_week_call_rece_min_tot_diff, contact_week_call_rece_cnt_6_mon_diff, contact_week_call_rece_cnt_3_mon_diff, contact_week_call_rece_cnt_2_mon_diff, contact_week_call_rece_cnt_1_mon_diff]
