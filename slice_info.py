#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re, time

log = "223.104.4.118 - - [14/Mar/2018:10:33:19 +0800] \"GET / log / sdk_update?sdkVersion = 122 HTTP / 1.1\" 200 2 \" - \" \"Dalvik / 1.6.0 (Linux; U; Android 4.4.4; OPPO R7s Build / KTU84P) | c36d126e448f2ec8e0ac33515801c8f1 | 860268037142249\""

date = "14/Mar/2018:10:33:19"
t = "%d/%b/%Y:%H:%M:%S"

format_data_str = "%Y-%m-%d"

tt = time.strptime(date, t)
print(tt)

rtt = time.strftime(format_data_str, tt)

print(rtt)


date1 = "14/Mar/2018:10:33:19"
date2 = "14/Mar/2018:11:33:19"

t1 = time.strptime(date1, t)

t2 = time.strptime(date2, t)

if t1[0]==t2[0] and t1[1]==t2[1] and t1[2]==t2[2]:
    print("A")
else:
    print("B")
