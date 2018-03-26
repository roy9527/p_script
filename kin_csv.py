#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys, csv
import kin_slice as slice

file_p = sys.argv[1]
file_out = sys.argv[2]

json_list = []

with open(file_p, 'rt') as f:
    for line in f:
        if 'qtradio=1' in line:
            p_date_ = slice.sliceDate(line)
            p_date_ = slice.covertToTime(p_date_)
            p_date = slice.covertToTimeStr(p_date_)
            p_time = slice.covertToDateTimeStr(p_date_)
            p_ip = slice.sliceIp(line)
            p_brand = slice.sliceBrand(line)
            p_imei = slice.sliceImei(line)
            raw_d = [p_imei, p_time, p_ip, p_brand]
            json_list.append(raw_d)
           
f_header=["date","imei","ip","brand"]
csv_f = open(file_out, 'a+',encoding='utf8',newline='')
writer = csv.writer(csv_f, dialect='excel')
writer.writerow(f_header)
writer.writerows(json_list)
csv_f.close()



