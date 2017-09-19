#/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
#    File Name: split_num_cat_data.py
#       Author: jenny
#        Email: yuxiaojiao@herobt.com
# Created Time: 2017年08月16日 星期三 12时10分20秒
#########################################################################
import sys
sys.path.append('/home/lliu/model_package')
import numpy as np
import csv

def load_data_types(var_types):
    cat_var_list=[]
    num_var_list=[]
    dep_var_list=[]
    with open(var_types, 'rb') as f:
        for i, lines in enumerate(f):
            if lines[1]=='cat':
                cat_var_list.append(lines[0])
            elif lines[1]=='num':
                num_var_list.append(lines[0])
            else:
                dep_var_list.append(lines[0])
   return cat_var_list, num_var_list, dep_var_list


def classify_data_types(var_types,in_file):
    cat_var_post=[]
    num_var_post=[]
    dep_var_post=[]
    cat_var_value=[]
    num_var_value=[]
    dep_var_value=[]
    cat_var_list, num_var_list, dep_var_list=load_data_types(var_types)
    with open(in_file, 'rb') as f:
        for i, lines in enumerate(f):
            if i==0:
                for m, items in lines:
                    if items in cat_var_list:
                        cat_var_post.append(m)
                    elif items in num_var_list:
                        num_var_post.append(m)
                    else:
                        dep_var_post.append(m)
            
            else:
                temp_out_cat_var=[]
                temp_out_num_var=[]
                temp_out_dep_var=[]
                for m, items in lines:
                    if m in cat_var_post:
                        temp_out_cat_var.append(lines[m])
                    elif m in num_var_post:
                        temp_out_num_var.append(lines[m])
                    else:
                        temp_out_dep_var.append(lines[m])

                cat_var_value.append(temp_out_cat_var)
                num_var_value.append(temp_out_num_var)
                dep_var_value.append(temp_out_dep_var)

           
        dep_out_file=in_file.split('.')[0] + '_dep.npy'
        cat_out_file=in_file.split('.')[0] + '_cat.npy'
        num_out_file=in_file.split('.')[0] + '_num.npy'

        cat_var_numpy_array=np.array(cat_var_value)
        num_var_numpy_array=np.array(num_var_value)
        dep_var_numpy_array=np.array(dep_var_value)

        np.save(dep_out_file, dep_var_numpy_array)
        np.save(num_out_file, num_var_numpy_array)
        np.save(cat_out_file, cat_var_numpy_array)


