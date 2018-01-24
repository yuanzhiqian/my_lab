#!/usr/bin/python

import json
import os.path
import codecs
import sys
import os
import chardet

reload(sys)
sys.setdefaultencoding("utf-8")

from ipip import IP
from ipip import IPX

# usage: python deal_log.py inmobi pv.log
if (len(sys.argv) != 3) :
    print "param number error!"
    print "sample: python deal_log.py adsmogo pv.log"
    exit()

# set input file
pv_path=sys.argv[2]
if (os.path.exists(pv_path) == False):
    print "pv file not find"
    exit()
pv_file=open(pv_path,"r")

# set output file
exchange=sys.argv[1]
save_file_path="./%s_pv"%(exchange)
result_file=codecs.open(save_file_path, 'w', 'utf-8')

# load dict files
carrier_path = "./transform/device_carrier_%s"%(exchange)
make_path = "./transform/device_make_%s"%(exchange)
model_path = "./transform/device_model_%s"%(exchange)
osv_path = "./transform/device_osv_%s"%(exchange)

if (os.path.exists(carrier_path) == False):
    print "carrier file not find"
    exit()

if (os.path.exists(make_path)==False):
    print "make file not find"
    exit()

if (os.path.exists(model_path)==False):
    print "model file not find"
    exit()

if (os.path.exists(osv_path)==False):
    print "osv file not find"
    exit()

carrier_dict={}
make_dict={}
model_dict={}
osv_dict={}

with open(carrier_path, 'r') as carrier_file:
    for line in carrier_file:
        kv = line.strip().split('\t')
        if (len(kv) == 1):
            carrier_dict[""] = kv[0]
        elif (len(kv) == 2):
            carrier_dict[kv[0]] = kv[1]
        else:
            print "error dict file!"
            print line
            exit()

with open(make_path, 'r') as make_file:
    for line in make_file:
        kv = line.strip().split('\t')
        if (len(kv) == 1):
            make_dict[""] = kv[0]
        elif (len(kv) == 2):
            make_dict[kv[0]] = kv[1]
        else:
            print "error dict file!"
            print line
            exit()

with open(model_path, 'r') as model_file:
    for line in model_file:
        kv = line.strip().split('\t')
        if (len(kv) == 1):
            model_dict[""] = kv[0]
        elif (len(kv) == 2):
            model_dict[kv[0]] = kv[1]
        else:
            print "error dict file!"
            print line
            exit()

with open(osv_path, 'r') as osv_file:
    for line in osv_file:
        kv = line.strip().split('\t')
        if (len(kv) == 1):
            osv_dict[""] = kv[0]
        elif (len(kv) == 2):
            osv_dict[kv[0]] = kv[1]
        else:
            print "error dict file!"
            print line
            exit()

# load ipip dat
IP.load(os.path.abspath("ip_location.dat"))

district_encode_path = "./district_encode"
if (os.path.exists(district_encode_path)==False):
    print "district_encode file not find"
    exit()

district_encode_dict={}

with open(district_encode_path, 'r') as district_encode_file:
    for line in district_encode_file:
        kv = line.strip().split('\t')
        try:
            if (len(kv) == 1):
                district_encode_dict[""] = kv[0]
            elif (len(kv) == 2):
                district_encode_dict[(kv[0])] = kv[1]
            else:
                print "error dict file!"
                print line
                exit()
        except:
            print kv[0], kv[1]

# start to analyze
except_cnt = 0;
parse_cnt = 0;
for line in pv_file:
    json_str = line.split("\t")[2]
    try:
        line_json = json.loads(json_str)
        app_or_site = ""
        carrier_str = ""
        make_str = ""
        model_str = ""                      # todo real model
        cat_str = ""
        os_str = ""
        osv_str = ""                        # real osv
        ip_str = ""                         # real province
        wifi_str = ""
        format_str = ""

        if (line_json.has_key("app")):
            app_or_site = "app"

            if (line_json["app"].has_key("cat")):
                cat_str = line_json["app"]["cat"][0]

        elif (line_json.has_key("site")):
            app_or_site = "site"
        else :
            app_or_site = "unknown"

        if (line_json.has_key("device")):
            if (line_json["device"].has_key("carrier")):
                carrier_str = line_json["device"]["carrier"]

            if (line_json["device"].has_key("make")):
                make_str = line_json["device"]["make"]

            if (line_json["device"].has_key("model")):
                model_str = line_json["device"]["model"]

            if (line_json["device"].has_key("os")):
                os_str = line_json["device"]["os"]

            if (line_json["device"].has_key("osv")):
                osv_str = line_json["device"]["osv"]

            if (line_json["device"].has_key("connectiontype")):
                wifi_str = line_json["device"]["connectiontype"]

        if (line_json.has_key("ipAddress")):
            ip_str = line_json["ipAddress"]

        if (line_json.has_key("imp")):
            imp_str = line_json["imp"][0]

            if (imp_str.has_key("formats")):
                format_str = imp_str["formats"][0]

        parse_cnt = parse_cnt+1
    except:
        except_cnt = except_cnt+1

    if (carrier_str in carrier_dict.keys()):
        carrier_str = carrier_dict[carrier_str]
    else:
        carrier_str = "46999"

    if (make_str in make_dict.keys()):
        make_str = make_dict[make_str]
    else:
        make_str = "others"

    if (model_str in model_dict.keys()):
        model_str = model_dict[model_str]
    else:
        model_str = "0"

    if (osv_str in osv_dict.keys()):
        osv_str = osv_dict[osv_str]
    else:
        osv_str = "0.0"

    geo_str = IP.find(ip_str)
    geos = geo_str.split('\t')

    if (len(geos) >= 2):
        geo_str = geos[1]
    else:
        geo_str = ""

    geo_str = geo_str.encode('utf-8')
    if (geo_str in district_encode_dict.keys()):
        province_str = district_encode_dict[geo_str]
    else:
        province_str = "-"

    result_file.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(app_or_site, carrier_str, make_str, model_str, cat_str, os_str, osv_str, province_str, wifi_str, format_str))

# final counts
print "unparsed:", except_cnt
print "parsed:", parse_cnt

# close files
pv_file.close
result_file.close

