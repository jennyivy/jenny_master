#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    > File Name: calculate_KS.py
    > Author: rick
    > Mail: xurui@herobt.com
    > Created Time: Wed 11 Dec 2017 16:19:05 PM CST
'''


import csv
import string
import math

def load_scores(in_file):
    inputs = csv.reader(open(in_file, 'rb'))
    score_list = []
    for i, lines in enumerate(inputs):
        if i <= 0:
            continue
        else:
            try:
                score = int(lines[5])
                print score
                print type(score)
                case_flag = int(lines[6])
                print case_flag
                print type(case_flag)
            except:
                print i
            score_list.append([score, case_flag])
    return score_list

def calculate_max_ks(in_file, out_file, ks_buckets):
    score_list = load_scores(in_file)
    score_ordered_list = sorted(score_list, key=lambda x : (x[0], x[1]), reverse = True)
    obs = len(score_ordered_list)
    bucket_size = float(obs)/float(ks_buckets)
    rank_dict = {}.fromkeys(range(1, ks_buckets+1))
    rank = 1
    current_rank = bucket_size
    rank_dict[rank] = []
    for i, items in enumerate(score_ordered_list):
        if i + 1 > current_rank:
            rank += 1
            current_rank = bucket_size * rank
            rank_dict[rank] = []
        rank_dict[rank].append(items)
         
    cum_cases = 0
    cum_non_cases = 0
    cum_trade = 0
    ks_list = []
    all_case = sum([case_flag for score, case_flag in score_ordered_list])
    with open(out_file, 'wb') as f:
        writer=csv.writer(f)
        writer.writerow(['rank','total_trade','sum_case','total_cases_percent','KS'])
        for rank, component in rank_dict.iteritems():
            total_trade = len(component)
            cum_trade += total_trade
            scores = [score for score, case_flag in component]
            mean_score = reduce(lambda x, y : x+y, scores)/total_trade
            sum_case = sum([case_flag for score, case_flag in component])
            total_cases_percent = float(sum_case)/float(all_case)
            cum_cases += sum_case
            cum_cases_percent = float(cum_cases)/float(all_case)
            case_percent = float(sum_case)/float(total_trade)
            cum_non_cases += (total_trade-sum_case)
            cum_non_case_percent = float(cum_non_cases) / float(obs - all_case)
            KS = cum_cases_percent - cum_non_case_percent
            ks_list.append(KS)
            writer.writerow([rank, total_trade, sum_case, total_cases_percent, KS])
    #last row, summary
        max_ks = max(ks_list)
        writer.writerow([obs, cum_cases, all_case, max_ks])
    
        
    
if __name__ == '__main__':
    in_file = r'./baidu_blacklist.csv'
    out_file = r'./baidu_blacklist_level_3_ks.csv'
    ks_buckets = 10
    calculate_max_ks(in_file, out_file, ks_buckets)
    
    
