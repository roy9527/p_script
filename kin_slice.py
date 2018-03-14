import re,time

#ip regax
reg_ip = r'((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))'

#date regax
reg_date = r'((.*)(\d{2,}/\w{1,}/\d{1,}\:\d{1,}\:\d{1,}\:\d{1,}))'

#Android os version code
reg_os_version = r'((.*)(\d\.\d\.\d))'

#client brand
reg_brand = r'((.*)(\d\.\d\.\d; )(.*)( Build))'

#client guid
reg_gUid = r'((.*)(\| )(.*)( \|))'

#client imei
reg_imei = r'((.*)(\| )(.*)(\"))$'

#date format
format_date = "%d/%b/%Y:%H:%M:%S"

#date format str
format_data_str = "%Y-%m-%d"

def sliceIp(line):
    d = re.match(reg_ip, line, 0)
    if d:
        ip = d.group(0)
        return ip.rstrip()
    else:
        return ''

def sliceDate(line):
    d = re.match(reg_date, line, 0)
    if d:
        date = d.groups()[-1]
        return date.rstrip()
    else:
        return ''

def sliceOsVersionInt(line):
    d = re.match(reg_os_version, line, 0)
    if d:
        ovi = d.groups()[-1]
        return ovi.rstrip()
    else:
        return ''


def sliceBrand(line):
    d = re.match(reg_brand, line, 0)
    if d:
        brand = d.groups()[-2]
        return brand.rstrip()
    else:
        return ''


def sliceGUid(line):
    d = re.match(reg_gUid, line, 0)
    if d:
        uid = d.groups()[-2]
        return uid.rstrip()
    else:
        return ''


def sliceImei(line):
    d = re.match(reg_imei, line, 0)
    if d:
        imei = d.groups()[-2]
        return imei.rstrip()
    else:
        return ''

def covertToTime(rawTime):
    return time.strptime(rawTime, format_date)


def covertToTimeStr(time_):
    return time.strftime(format_date_str, time_)
