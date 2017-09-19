#/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
#    File Name: cat_label_transform.py
#       Author: lliu
#        Email: lliu@herobt.com
# Created Time: 2017年08月16日 星期三 13时55分52秒
#########################################################################
import sys
sys.path.append('/home/lliu/model_package')
import numpy as np
from sklearn.preprocessing import LabelEncoder
import csv
import joblib


def label_transform(in_file):
    cat_var_val=np.load(in_file)
    print cat_var_val.shape()
    le=LabelEncoder()
    label_dict={}
    to_be_transformed=[]
    for i in range(0, len(cat_var_val.shape[1])):
        temp_out=cat_var_val[:,i]
        le.fit(temp_out)
        model_out_file=r'./transformation.pkl'
        joblib.dump(le, out_file)
        for class_s in le.classes_:
            label_dict[class_s]=str(le.transform(class_s))
        text_out_file=r'./transformation.txt'
        json.dump(label_dict, text_out_file)
        trans_temp_out=le.transform(temp_out)
        to_be_transformed.append(trans_temp_out)

    label_transformed=np.transpose(to_be_transformed)

    np.save(in_file, label_transformed)
        
