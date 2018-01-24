#!/usr/bin/python

import json
import os.path
import codecs
import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")

# usage: python judge.py inmobi_ad inmobi_pv
if (len(sys.argv) != 3):
    print "param number error!"
    print "sample: python judge.py inmobi_ad inmobi_pv"
    exit()

class ad:
    def __init__(self):
        self.ad_id = ''
        self.ad_type = ''
        self.carrier_type = '0'
        self.carrier_val = []
        self.make_type = '0'
        self.make_val = []
        self.model_type = '0'
        self.model_val = []
        self.cat_type = '0'
        self.cat_val = []
        self.os_type = '0'
        self.os_val = []
        self.osv_type = '0'
        self.osv_val = []
        self.province_type = '0'
        self.province_val = []
        self.wifi_type = '0'
        self.wifi_val = []
        self.formats_type = '0'
        self.formats_val = []

    def init_ad(self, line_str):
        items = line_str.split('\t')
        if (len(items) != 20):
            print "load ad info error"
            exit()
        self.ad_id = items[0]
        self.ad_type = items[1]

        self.carrier_type = items[2]
        carrier_type_vec = items[3].split('\1')
        for carrier_type_id in carrier_type_vec:
            if (carrier_type_id != ''):
                self.carrier_val.append(carrier_type_id)

        self.make_type = items[4]
        make_type_vec = items[5].split('\1')
        for make_type_id in make_type_vec:
            if (make_type_id != ''):
                self.make_val.append(make_type_id)

        self.model_type = items[6]
        model_type_vec = items[7].split('\1')
        for model_type_id in model_type_vec:
            if (model_type_id != ''):
                self.model_val.append(model_type_id)

        self.cat_type = items[8]
        cat_type_vec = items[9].split('\1')
        for cat_type_id in cat_type_vec:
            if (cat_type_id != ''):
                self.cat_val.append(cat_type_id)

        self.os_type = items[10]
        os_type_vec = items[11].split('\1')
        for os_type_id in os_type_vec:
            if (os_type_id != ''):
                self.os_val.append(os_type_id)

        self.osv_type = items[12]
        osv_type_vec = items[13].split('\1')
        for osv_type_id in osv_type_vec:
            if (osv_type_id != ''):
                self.osv_val.append(osv_type_id)

        self.province_type = items[14]
        province_type_vec = items[15].split('\1')
        for province_type_id in province_type_vec:
            if (province_type_id != ''):
                self.province_val.append(province_type_id)

        self.wifi_type = items[16]
        wifi_type_vec = items[17].split('\1')
        for wifi_type_id in wifi_type_vec:
            if (wifi_type_id != ''):
                self.wifi_val.append(wifi_type_id)

        self.formats_type = items[18]
        formats_type_vec = items[19].split('\1')
        for formats_type_id in formats_type_vec:
            if (formats_type_id != ''):
                self.formats_val.append(formats_type_id)

    def judge_pv(self, pv_val):
        if self.type_val != pv_val.type_val:
            return False
        if self.judge_one(self.carrier_type, self.carrier_val, pv_val.carrier_val) == False:
            return False

    def judge_one(self, type_val, ad_val, pv_val):
        if (type_val == '0'):
            return True
        if (type_val == '1'):
            if (pv_val in ad_val):
                return True
            else:
                return False
        if (type_val == '-1'):
            if (pv_val in ad_val):
                return False
            else:
                return True

class pv:
    def __init__(self):
        self.type_val = ''
        self.carrier_val = ''
        self.make_val = ''
        self.model_val = ''
        self.cat_val = ''
        self.os_val = ''
        self.osv_val = ''
        self.province_val = ''
        self.wifi_val = ''
        self.formats_val = ''

    def init_pv(self, line_str):
        items = line_str.split('\t')
        if (len(items) != 10):
            print "load pv_info error"
            exit()

        self.type_val = items[0]
        self.carrier_val = items[1]
        self.make_val = items[2]
        self.model_val = items[3]
        self.cat_val = items[4]
        self.os_val = items[5]
        self.osv_val = items[6]
        self.province_val = items[7]
        self.wifi_val = items[8]
        self.formats_val = items[9]


# load ad_file
ad_file_path = sys.argv[1]
if (os.path.exists(ad_file_path) == False):
    print "ad file not found!"
    exit()
ad_file = open(ad_file_path, "r")

all_ad=[]
for line in ad_file:
    one_ad = ad()
    one_ad.init_ad(line)
    all_ad.append(one_ad)


