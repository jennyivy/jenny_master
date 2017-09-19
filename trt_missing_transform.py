#/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
#    File Name: trt_missing_transform.py
#       Author: lliu
#        Email: lliu@herobt.com
# Created Time: 2017年08月16日 星期三 11时04分05秒
#########################################################################
import sys
sys.path.append('/home/lliu/model_package')
import csv
import ast

def trt_missing(in_file, out_file, missing_default):
    data_in=csv.reader(open(in_file, 'rb'))
    temp_out=[]
    data_out=csv.writer(open(out_file, 'wb'))
    for i, lines in enumerate(data_in):
        if i==0:
            
            data_out.writerow(lines)

        else:
            for items in lines:
                if items in ('null', 'Null', 'NULL', '-1', '1', 'None', '\N', 'NaN'):
                    items=missing_default
                    temp_out.append(items)
                else:
                    try:
                        items=ast.literal_eval(items)
                        temp_out.append(items)
                    except:
                        items=items
                        temp_out.append(items)

            data_out.writerow(temp_out)
            


