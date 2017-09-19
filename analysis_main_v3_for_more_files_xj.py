# coding:utf-8

import json
from datetime import datetime as dt
import csv
import multiprocessing
from jxl_solo_xj import jxl
from jxl_call_time import jxl_time
from phone_bill import bill
from nets_subflow import nets_subflow
from qhoftenloaner import qhoftenloaner
from qhrisk import qhrisk
from tongdun import tongdun
from cr91 import cr91
from zhimaindustry import zhimaindustry
from zhimaIVS import zhimaIVS
from header_xj import title
import pickle
from net_place_cp import nets_place


# load dict
f = open(r'/home/lliu/model_package/phone_map.pickle', 'rb')
mobile_phone_num_attr_dict = pickle.load(f)
f.close()

f2=open(r'./city_prov.pkl','rb')
city_prov_dic=pickle.load(f2)
f2.close()

def calculating(str_in, bad_days,q):
    json_data = json.loads(str_in)
    nid = json_data['nid']

    # if int(nid[:6]) not in (201706, 201707, 201708):
    #    return 'not going into dataset'

    try:
        maxDelinquentDays = json_data['maxDelinquentDays']
    except:
        return 'not going into dataset'
        
    maxDelinquentDays = json_data['maxDelinquentDays']
    if maxDelinquentDays >= bad_days and maxDelinquentDays != 'null':
        bad = 1
    else:
        bad = 0
    updateTime_f = float(json_data['applyTime']) / 1000
    now_dt = dt.fromtimestamp(updateTime_f)
    income = json_data['income']
    delinquentDays = json_data['delinquentDays']
    mainContact1CallTimes = json_data['mainContact1CallTimes']
    deviceCallRecordCount = json_data['deviceCallRecordCount']
    mainContact2Phone = json_data['mainContact2Phone']
    clearTime = json_data['clearTime']
    qianhaiOftenloan = json_data['qianhaiOftenloan']
    mainContact2Match = json_data['mainContact2Match']
    credit91 = json_data['91credit']
    positionName = json_data['positionName']
    marrayStatus = json_data['marrayStatus']
    lastBorrowStatus = json_data['lastBorrowStatus']
    risk_items = json_data['risk_items']
    mainContact2CallTimes = json_data['mainContact2CallTimes']
    try:
        borrowHistory = json_data['borrowHistory']
    except:
        borrowHistory = None
    isRepay = json_data['isRepay']
    successCount = json_data['successCount']
    deviceContactCount = json_data['deviceContactCount']
    credooScore = json_data['credooScore']
    deviceContact = ''
    jxl_call_records = json_data['jxl_call_records']
    if jxl_call_records is not None and jxl_call_records not in ('', 'Null', 'null', 'Null'):
        try:
            call_records = jxl_call_records['call_records']
            phone_bill = jxl_call_records['phone_bill']
            nets = jxl_call_records['nets']
        except:
            return 'not going into dataset'
    else:
        return 'not going into dataset'

    gatherTime = json_data['gatherTime']
    if gatherTime is not None and gatherTime not in ('', 'Null', 'null', 'Null'):
        jxl_dt = dt.strptime(gatherTime[:19], '%Y-%m-%d %H:%M:%S')
    else:
        return 'not going into dataset'

   # deviceContact = "" # json_data['deviceContact']
    deviceMatchCount = json_data['deviceMatchCount']
    mainContact1Match = json_data['mainContact1Match']
    zhimaIvs = json_data['zhimaIvs']
    telMatchCount = json_data['telMatchCount']
    smsCount = json_data['smsCount']
    companyTel = json_data['companyTel']
    mainContact1Phone = json_data['mainContact1Phone']
    mainContact1CallLen = json_data['mainContact1CallLen']
    mainContact2CallLen = json_data['mainContact2CallLen']
    totalRepayAmount = json_data['totalRepayAmount']
    userId = json_data['userId']
    shouldRepayAmount = json_data['shouldRepayAmount']
    isClean = json_data['isClean']
    qh_riskmark = json_data['qh_riskmark']
    failedCount = json_data['failedCount']
    zhimaRiskScore = json_data['zhimaRiskScore']
    mainContact1Relation = json_data['mainContact1Relation']
    moreContact = json_data['moreContact']
    creditCards = json_data['creditCards']
    ivs = json_data['zhimaIvs']
    try:
        zhimaScore = json_data['zhimaScore']
    except:
        zhimaScore = None
    debitCards = json_data['debitCards']
    try:
        edu = json_data['edu']
    except:
        edu = None
    try:
        name = json_data['name']
    except:
        name = None
    zhima_industry = json_data['zhima_industry']
    mainContact2Relation = json_data['mainContact2Relation']

    ############################################################################################################
    # qianhaiOftenloan
    qhoftenloaner_return = qhoftenloaner(qianhaiOftenloan, now_dt)
    
    # 91credit, credit91
    cr91_return = cr91(credit91, now_dt)

    # risk_items
    tongdun_return = tongdun(risk_items)

    # qh_riskmark
    qhrisk_return = qhrisk(qh_riskmark, now_dt)

    # zhima_industry
    zhimaindustry_return = zhimaindustry(zhima_industry, now_dt)

    # jxl data
    jxl_call_return = jxl(call_records, jxl_dt, mainContact1Phone, mainContact2Phone, moreContact, mobile_phone_num_attr_dict)
    #print ("jxl_call_return : " + str(len(jxl_call_return)))

    jxl_call_time_return = jxl_time(call_records, jxl_dt)
    
    #jxl phone bill data
    bill_return = bill(phone_bill, jxl_dt)

    #jxl nets data
    nets_return = nets_subflow(nets, jxl_dt)
    
    nets_place_return = nets_place(nets, jxl_dt, city_prov_dic)

    # zhimaIVS
    zhimaIVS_return = zhimaIVS(ivs)

    # combine
    temp_out = [nid, userId, income, delinquentDays, mainContact1CallTimes, deviceCallRecordCount, clearTime,
                mainContact2Match, positionName, marrayStatus, lastBorrowStatus, mainContact2CallTimes, borrowHistory,
                isRepay, successCount, deviceContactCount, credooScore, deviceContact, deviceMatchCount,
                mainContact1Match, telMatchCount, smsCount, mainContact1CallLen, mainContact2CallLen, totalRepayAmount,
                shouldRepayAmount, isClean, failedCount, zhimaRiskScore, mainContact1Relation, zhimaScore, edu,
                mainContact2Relation]
    temp_out.extend(qhoftenloaner_return)
    temp_out.extend(cr91_return)
    temp_out.extend(tongdun_return)
    temp_out.extend(qhrisk_return)
    temp_out.extend(zhimaindustry_return)
    temp_out.extend(jxl_call_return)
    temp_out.extend(jxl_call_time_return)
    temp_out.extend(bill_return)
    temp_out.extend(nets_return)
    temp_out.extend(nets_place_return)
    temp_out.extend(zhimaIVS_return)
    temp_out.extend([maxDelinquentDays, bad])
    decode_data_list = [unicode(s).encode("utf-8") for s in temp_out]
    q.put(decode_data_list)
    return decode_data_list


def writer(q, out_file):
    ex_file = csv.writer(open(out_file, "ab"))
    while 1:
        m = q.get()
        if m == 'kill':
            break
        ex_file.writerow(m)


def out_putting(in_file_list, out_file, bad_days, jobs=8):
    inputs = open(out_file, "wb")
    ex_file = csv.writer(inputs)
    ex_file.writerow(title)
    inputs.close()
    manager = multiprocessing.Manager()
    q = manager.Queue()
    pool = multiprocessing.Pool(jobs)
    watcher = pool.apply_async(writer, (q, out_file))

    jobs = []
    for in_file in in_file_list:
        with open(in_file, 'rb') as f:
            print 'open ' + in_file
            jobs = []
            for i, lines in enumerate(f.readlines()):
                job = pool.apply_async(calculating, (lines, bad_days, q))
                jobs.append(job)
                for job in jobs:
                    job.get()

    q.put('kill')
    pool.close()


if __name__ == '__main__':
    # in_file = r'/Users/Mis_z/Desktop/data_test_1.txt'
    # out_file = r'/Users/Mis_z/Desktop/data_test_1.csv'
    in_file =[r'/data3/regular_model/2017_0806/2017_0806_model_21_n_old.txtac'] 
    out_file = r'./2017_0806_model_21_n_old_test_fields.csv'
    bad_days=1
    out_putting(in_file, out_file,bad_days, jobs=8)
