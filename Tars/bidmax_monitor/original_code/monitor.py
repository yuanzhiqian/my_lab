#!/usr/bin/env python

import os
import time 
import subprocess
import json

class Monitor(object):
    def __init__(self, script = "./test_online.sh", interval = 5):
        self.script = script;
        self.interval = interval;
        self.log = "mon_stat.log";
        self.reason_stat = {};
        self.total_req = 0;
        self.total_ok = 0;
        self.total_err = 0;

    def start(self):
        while True:
            time.sleep(self.interval);
            self.ping();
            self.dump_dict();

    def ping(self):
        #print "ping";
        FNULL = open(os.devnull, 'w')
        #p = subprocess.Popen([self.script], stdout=subprocess.PIPE, stderr=FNULL);
        p = subprocess.Popen([self.script], stdout=subprocess.PIPE, stderr=subprocess.PIPE);
        out, err = p.communicate();
        try:
            status, reason = self.parse_json(out);
        except ValueError as err:
            print "Error detected: "
            print err
            print "Raw response str: "
            print out
            status = 'no_ad'
            reason = str(err) 

        self.total_req += 1;
    
        if status == 'ok':
            self.total_ok += 1;
        elif status == 'no_ad':
            self.process_err(reason);
        else:
            None;
    
    def parse_json(self, str):
        status = None;
        reason = None;
        json_obj = json.loads(str);
        if type(json_obj) is dict:
            if "reason" in json_obj:
                status = 'no_ad';
                reason = json_obj["reason"];

            else:
                status = 'ok';
        else:
            None;
        
        return (status, reason)
    
    def process_err(self, reason):
        self.total_err += 1;

        if reason in self.reason_stat:
            self.reason_stat[reason] += 1;
        else:
            self.reason_stat[reason] = 1;

        self.trigger_notice(reason);

    def trigger_notice(self, reason):
        None;
        #TODO: noticing

    def dump_dict(self):
        #print "dump_dict"
        err_rate = float(self.total_err) / float(self.total_req);
        msg = "Total pings: " + str(self.total_req) + "\n";
        msg += "Total successes: " + str(self.total_ok) + "\n";
        msg += "Total errors: " + str(self.total_err) + "\n";
        msg += "Fail rate: " + str(err_rate * 100) + "%" + "\n";
        msg += "Reasons: {\n"
        for key in self.reason_stat:
            msg += "\t" + key + ": " + str(self.reason_stat[key]) + "\n";
        msg += "}\n"

        f = open(self.log, 'w');
        f.write(msg);
        f.close();

    
if __name__ == '__main__':
    monitor = Monitor(interval=1);
    monitor.start();
    
    

