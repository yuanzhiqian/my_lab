#!/usr/bin/python

import json
import os.path
import codecs
import sys
import os
import chardet

reload(sys)
sys.setdefaultencoding("utf-8")

# usage: python deal_ad.py inmobi bayesbidder.json
if (len(sys.argv) != 3):
    print "param number error!"
    print "sample: python deal_ad.py inmobi bayesbidder.json"
    exit()

# set output file
exchange=sys.argv[1]
save_file_path="./%s_ad"%(exchange)
result_file=codecs.open(save_file_path, 'w', 'utf-8')

# load ad_file
ad_file_path =sys.argv[2]
if (os.path.exists(ad_file_path) == False):
    print "bayesbidder.json not found!"
    exit()
ad_file = open(ad_file_path, "r")
ad_all_json = json.loads(ad_file.read())

if (ad_all_json.has_key("creatives") != True):
    print "no creatives!"
    exit()

creatives_json = ad_all_json["creatives"]

# get ads limit info
for creative_json in (creatives_json):
    ad_id = ""
    type_str = "app"
    carrier_type = "0"
    carrier_str = ""
    make_type = "0"
    make_str = ""
    model_type = "0"
    model_str = ""
    cat_type = "0"
    cat_str = ""
    os_type = "0"
    os_str = ""
    osv_type = "0"
    osv_str = ""
    province_type = "0"
    province_str = ""
    wifi_type = "0"
    wifi_str = ""

    if (creative_json["providerConfig"].has_key("%s"%(exchange)) == False):
        continue;
    ad_id = creative_json["id"]

    # device_carrier_info
    if (creative_json.has_key("device_carrier_filters")):
        exclude_size = len(creative_json["device_carrier_filters"]["exclude"])
        include_size = len(creative_json["device_carrier_filters"]["include"])
        if (include_size > 0):
            carrier_type = "1";
            for carrier_id in creative_json["device_carrier_filters"]["include"]:
                carrier_str += carrier_id
                carrier_str += "\1"
        elif (exclude_size > 0):
            carrier_type = "-1"
            for carrier_id in creative_json["device_carrier_filters"]["exclude"]:
                carrier_str += carrier_id
                carrier_str += "\1"
        else:
            carrier_type = "0"
            carrier_str = ""
    else:
        carrier_type = 0
        carrier_str = ""

    # device_make_info
    if (creative_json.has_key("device_make_filters")):
        exclude_size = len(creative_json["device_make_filters"]["exclude"])
        include_size = len(creative_json["device_make_filters"]["include"])
        if (include_size > 0):
            make_type = "1";
            for make_id in creative_json["device_make_filters"]["include"]:
                make_str += make_id
                make_str += "\1"
        elif (exclude_size > 0):
            make_type = "-1"
            for make_id in creative_json["device_make_filters"]["exclude"]:
                make_str += make_id
                make_str += "\1"
        else:
            make_type = "0"
            make_str = ""
    else:
        make_type = 0
        make_str = ""

    # device_model_info
    if (creative_json.has_key("device_model_filters")):
        exclude_size = len(creative_json["device_model_filters"]["exclude"])
        include_size = len(creative_json["device_model_filters"]["include"])
        if (include_size > 0):
            model_type = "1";
            for model_id in creative_json["device_model_filters"]["include"]:
                model_str += model_id
                model_str += "\1"
        elif (exclude_size > 0):
            model_type = "-1"
            for model_id in creative_json["device_model_filters"]["exclude"]:
                model_str += model_id
                model_str += "\1"
        else:
            model_type = "0"
            model_str = ""
    else:
        model_type = 0
        model_str = ""

    # cat_info
    if (creative_json.has_key("iab_filters")):
        if (creative_json["iab_filters"].has_key("exclude") == False):
            exclude_size = 0
        elif (creative_json["iab_filters"].has_key("include") == False):
            include_size = 0
        else:
            exclude_size = len(creative_json["iab_filters"]["exclude"])
            include_size = len(creative_json["iab_filters"]["include"])

        if (include_size > 0):
            cat_type = "1";
            for cat_id in creative_json["iab_filters"]["include"]:
                cat_str += cat_id
                cat_str += "\1"
        elif (exclude_size > 0):
            cat_type = "-1"
            for cat_id in creative_json["iab_filters"]["exclude"]:
                cat_str += cat_id
                cat_str += "\1"
        else:
            cat_type = "0"
            cat_str = ""
    else:
        cat_type = 0
        cat_str = ""

    # os_info
    if (creative_json.has_key("os_filters")):
        if (creative_json["os_filters"].has_key("exclude") == False):
            exclude_size = 0
        elif (creative_json["os_filters"].has_key("include") == False):
            include_size = 0
        else:
            exclude_size = len(creative_json["os_filters"]["exclude"])
            include_size = len(creative_json["os_filters"]["include"])

        if (include_size > 0):
            os_type = "1";
            for os_id in creative_json["os_filters"]["include"]:
                os_str += os_id
                os_str += "\1"
        elif (exclude_size > 0):
            os_type = "-1"
            for os_id in creative_json["os_filters"]["exclude"]:
                os_str += os_id
                os_str += "\1"
        else:
            os_type = "0"
            os_str = ""
    else:
        os_type = 0
        os_str = ""

    # osv_info
    if (creative_json.has_key("osv_filters")):
        if (creative_json["osv_filters"].has_key("exclude") == False):
            exclude_size = 0
        elif (creative_json["osv_filters"].has_key("include") == False):
            include_size = 0
        else:
            exclude_size = len(creative_json["osv_filters"]["exclude"])
            include_size = len(creative_json["osv_filters"]["include"])

        if (include_size > 0):
            osv_type = "1";
            for osv_id in creative_json["osv_filters"]["include"]:
                osv_str += osv_id
                osv_str += "\1"
        elif (exclude_size > 0):
            osv_type = "-1"
            for osv_id in creative_json["osv_filters"]["exclude"]:
                osv_str += osv_id
                osv_str += "\1"
        else:
            osv_type = "0"
            osv_str = ""
    else:
        osv_type = 0
        osv_str = ""

    # province_info
    if (creative_json.has_key("province_filters")):
        if (creative_json["province_filters"].has_key("exclude") == False):
            exclude_size = 0
        elif (creative_json["province_filters"].has_key("include") == False):
            include_size = 0
        else:
            exclude_size = len(creative_json["province_filters"]["exclude"])
            include_size = len(creative_json["province_filters"]["include"])

        if (include_size > 0):
            province_type = "1";
            for province_id in creative_json["province_filters"]["include"]:
                province_str += province_id
                province_str += "\1"
        elif (exclude_size > 0):
            province_type = "-1"
            for province_id in creative_json["province_filters"]["exclude"]:
                province_str += province_id
                province_str += "\1"
        else:
            province_type = "0"
            province_str = ""
    else:
        province_type = 0
        province_str = ""

    # wifi_info
    if (creative_json.has_key("wifi_filters")):
        if (creative_json["wifi_filters"].has_key("exclude") == False):
            exclude_size = 0
        elif (creative_json["wifi_filters"].has_key("include") == False):
            include_size = 0
        else:
            exclude_size = len(creative_json["wifi_filters"]["exclude"])
            include_size = len(creative_json["wifi_filters"]["include"])

        if (include_size > 0):
            wifi_type = "1";
            for wifi_id in creative_json["wifi_filters"]["include"]:
                wifi_str += str(wifi_id)
                wifi_str += "\1"
        elif (exclude_size > 0):
            wifi_type = "-1"
            for wifi_id in creative_json["wifi_filters"]["exclude"]:
                wifi_str += str(wifi_id)
                wifi_str += "\1"
        else:
            wifi_type = "0"
            wifi_str = ""
    else:
        wifi_type = 0
        wifi_str = ""

    # formats_info
    width = creative_json["width"]
    height = creative_json["height"]
    formats_str = str(width) + "x" + str(height)
    formats_type = "1"

    result_file.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(ad_id, type_str, carrier_type, carrier_str, make_type, make_str, model_type, model_str, cat_type, cat_str, os_type, os_str, osv_type, osv_str, province_type, province_str, wifi_type, wifi_str, formats_type, formats_str))
