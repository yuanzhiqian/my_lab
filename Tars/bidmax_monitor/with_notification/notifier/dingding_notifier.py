#!/usr/bin/env python

import urllib2
import json

class DingDingAPI(object):
    def __init__(self, corpid = "dingfb2d56d108d62c5e", 
                 corpsecret = "nOUTzrCDzMxQd2Sh_zZsgkGVyF5BjB9q8TcZbG61lbJuX3ivm7R3CFYcoG9jcJX0",
                 ssosecret = "-tcm1LOemBml7XlTZhMtYF1-TvmO2bRdzNieEVF_n0ihsKMRt5CWbr1cRx0GkL13", 
                 default_chatid = "chat9d72aa1778fadd00137d6c2148dc42a0"):
        self.corpid = corpid;
        self.corpsecret = corpsecret;
        self.ssosecret = ssosecret;
        self.access_token = None;
        self.default_chatid = default_chatid;
        self.auth_url = ("https://oapi.dingtalk.com/gettoken?corpid="
                        + self.corpid 
                        + "&corpsecret="
                        + self.corpsecret);

        self.sso_auth_url = ("https://oapi.dingtalk.com/sso/gettoken?corpid="
                            + self.corpid
                            + "&corpsecret="
                            + self.ssosecret);

    def http_get(self, url, body):
        req = urllib2.Request(url);
        response = urllib2.urlopen(req);
        the_page = response.read();

        ret_obj = json.loads(the_page);

        return ret_obj;

    def connect(self, sso = False):
        if sso == True:
            url = self.sso_auth_url;
        else:
            url = self.auth_url;
        
        ret_obj = self.http_get(url, None);

        if type(ret_obj) is dict and "errmsg" in ret_obj and ret_obj["errmsg"] == 'ok':
            self.access_token = ret_obj["access_token"];
        else:
            self.access_token = None;

        return self.access_token; 

    def reconnect(self):
        print "reconnecting";
        self.connect();
        if self.access_token == None:
            print "Cannot connect to the server"
            return False;
        else:
            return True;

    def post_json(self, url, body):
        # alternative way
        #opener = urllib2.build_opener()
        #req = urllib2.Request(url, data=body,
        #                      headers={'Content-Type': 'application/json'})
        #response = opener.open(req)

        req = urllib2.Request(url, body, {'Content-Type': 'application/json'});
        response = urllib2.urlopen(req);
        the_page = response.read();
        ret_obj = json.loads(the_page);

        return ret_obj;


    def notify(self, msg, chatid = None, sender = "011656529229"):
        if chatid == None:
            chatid = self.default_chatid;

        if self.access_token == None:
            if self.reconnect() == False:
                return False;

        url = "https://oapi.dingtalk.com/chat/send?access_token=" + self.access_token;

        content = {
            "chatid": chatid,
            "sender": sender,
            "msgtype": "text",
            "text": {
                "content": msg 
            }
        }

        body = json.dumps(content);

        return self.req_with_retry(self.post_json, (url, body));

    def req_with_retry(self, func, args):
        # only when access_token expires should we retry; you can see from the code that for other cases we simply return
        for x in range(0, 2):
            ret_obj = func(*args); 

            if type(ret_obj) is dict and "errmsg" in ret_obj:
                if ret_obj["errmsg"] == 'ok':
                    print "msg sent successfully"
                    return (True, ret_obj); 
                elif "errcode" in ret_obj and ret_obj["errcode"] == 40014:
                    if self.reconnect() == False:
                        return (False, ret_obj);
                    else:
                        continue;
            else    :
                print "unable to send msg";
                print ret_obj;
                return (False, ret_obj);

    def department_list(self):
        if self.access_token == None:
            if self.reconnect() == False:
                return False;

        url = "https://oapi.dingtalk.com/department/list?access_token=" + self.access_token;

        return self.req_with_retry(self.http_get, (url, None));

    def list_users(self, department = 1):
        if self.access_token == None:
            if self.reconnect() == False:
                return False;
       
        url = "https://oapi.dingtalk.com/user/simplelist?access_token=" + self.access_token + "&department_id=" + str(department);

        return self.req_with_retry(self.http_get, (url, None));

if __name__ == '__main__':
    # test
    dingding = DingDingAPI();

    print dingding.department_list();
    print dingding.list_users();
    print dingding.notify("test function object");











