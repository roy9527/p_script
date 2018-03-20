import kin_slice as slice
# from kin_mongo import client

# t_log = "223.104.4.118 - - [14/Mar/2018:10:33:19 +0800] \"GET / log / sdk_update?sdkVersion = 122 HTTP / 1.1\" 200 2 \" - \" \"Dalvik / 1.6.0 (Linux; U; Android 4.4.4; OPPO R7s Build / KTU84P) | c36d126e448f2ec8e0ac33515801c8f1 | 860268037142249\""


# ip = slice.sliceIp(t_log)
# print(ip)

# date = slice.sliceDate(t_log)
# print(date)

# ovi = slice.sliceOsVersionInt(t_log)
# print(ovi)

# brand = slice.sliceBrand(t_log)
# print(brand)

# guid = slice.sliceGUid(t_log)
# print(guid)

# imei = slice.sliceImei(t_log)
# print(imei)

d=set()

with open('access.log-20180320', 'rt') as f:
    for line in f:
        if 'sdkVersion=121' in line or 'sdkVersion=122' in line:
            guid = slice.sliceGUid(line)
            if guid and not 'null'==guid:
                d.add(guid)
                # print(d)
print(len(d))