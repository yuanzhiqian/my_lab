# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

from ipip import IP
from ipip import IPX

ip_file = open("ip_data")

ip_arr = []
for line in ip_file:
  ip_arr.append(line)

ip_file.close()

IP.load(os.path.abspath("ip_location.dat"))

for ip in ip_arr:
    print IP.find(ip)



