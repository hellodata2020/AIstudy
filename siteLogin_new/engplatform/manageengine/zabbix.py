# coding:utf-8
import urllib2
import json
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from artlog import *


class init_zabbix():
    def __init__(self,zabbix_server_ip,zabbix_user,zabbix_pwd):
        self.serverip = zabbix_server_ip
        self.header = {"Content-Type": "application/json"}
        self.url = "http://" + zabbix_server_ip + "/zabbix/api_jsonrpc.php"
        self.data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
            "user": zabbix_user,
            "password": zabbix_pwd
        },
        "id": 0
        })
        self.request = urllib2.Request(self.url,self.data)
        for key in self.header:
            self.request.add_header(key,self.header[key])
        try:
            result = urllib2.urlopen(self.request)
        except Exception,e:
            self.authid = None
            print "failed."
            info("messages.log","helloworld.")
        else:
            response = json.loads(result.read())
            result.close()
            print "Auth Successful. The Auth ID Is:%s " % response['result']
            info("messages.log", "Auth Successful. The Auth ID Is:%s " % response['result'])
            self.authid = response['result']
        self.data_querybyhost = {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "itemids",
                "hostids":"10084",
                "search":{"key_":"system.cpu.util[,user]"}
            },
            "auth": self.authid,
            "id": 1,
        }
    def getID(self):
        return self.authid
    def get_host(self,getfilter,*args):
        get_url = "http://" + self.serverip + "/zabbix/api_jsonrpc.php"
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                    "output": list(args),
                    "filter": {getfilter: ""}
                },
                "auth": self.authid,
            # the auth id is what auth script returns, remeber it is string
                "id": 1,
            })
        get_request = urllib2.Request(get_url,data)
        for key in self.header:
            get_request.add_header(key,self.header[key])
        try:
            response = urllib2.urlopen(get_request)
        except Exception as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(response.read())
            # response.close()
            print "Number Of Hosts: ", len(response['result'])
            host_list = []
            for host in response['result']:
                print "Host ID:", host['hostid'], "Host Name:", host['name']
                host_list.append(str(host['hostid']))
            return host_list
        pass

    def add_host(self,host_ip):
        print 123

    def exec_data(self,data):
        get_url = "http://" + self.serverip + "/zabbix/api_jsonrpc.php"
        get_request = urllib2.Request(get_url, data)
        for key in self.header:
            get_request.add_header(key, self.header[key])
        try:
            response = urllib2.urlopen(get_request)
        except Exception as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(response.read())
            return response


    def host_query(self,host_list,para_list):
        self.para = {}
        id = 0
        for hostid in host_list:
            self.data_querybyhost['params']['hostids'] = hostid
            paralist = []
            new_paralist = []
            for kv in para_list:
                self.data_querybyhost['params']['search']['key_'] = kv
                self.data_querybyhost['id'] = id
                tmp_json = json.dumps(self.data_querybyhost)
                res = self.exec_data(tmp_json)
                if len(res['result']) > 0:
                    print res['result'][0]['itemid']
                    paralist.append(str(res['result'][0]['itemid']))
            print paralist
            self.para[hostid] = paralist
        print self.para

    # def get_cpu(self,hostid):
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "item.get",
                "params": {
                    "output": "itemids",
                    "hostids":"10084",
                    "search":{"key_":"system.cpu.util[,user]"}
                },
                "auth": self.authid,
            # the auth id is what auth script returns, remeber it is string
                "id": 1,
            })


if __name__ == '__main__':
    iz = init_zabbix('192.168.135.133','Admin','zabbix')
    authID = iz.getID()
    data = json.dumps(
    {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": "itemids",
            "hostids":"10084",
            "search":{"key_":"system.cpu.util[,user]"}
        },
        "auth": authID,
    # the auth id is what auth script returns, remeber it is string
        "id": 1,
    })
    #iz.exec_data(data)
    data = json.dumps(
    {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "history": 0,
            "itemids": ["23306"],
            "output": "extend"
        },
        "auth": authID,
    # the auth id is what auth script returns, remeber it is string
        "id": 1,
    })
    #iz.exec_data(data)

    # iz.test()
    host_list=iz.get_host("host","hostid", "name")
    iz.host_query(host_list,['system.cpu.util[,user]','vm.memory.size[available]','vfs.fs.size'])


#思路:获取全部hostid、获取每个hostid对应监控项目的itemid，然后获取每个id的lastvalue
