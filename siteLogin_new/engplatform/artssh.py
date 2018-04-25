# -*- coding: UTF-8 -*-
import paramiko

class init_ssh():
    def __init__(self,ipaddr,reuser,repasswd,port):
        self.ipaddr = ipaddr
        self.reuser = reuser
        self.repasswd = repasswd
        self.port = port
        try:
            self.new_connector = paramiko.SSHClient()
            self.new_connector.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.new_connector.connect(self.ipaddr, self.port, self.reuser, self.repasswd)
        except Exception,e:
            print e.message
    def run_ssh(self,ssh_command):
        stdin, stdout, stderr = self.new_connector.exec_command(ssh_command)
        outmsg, errmsg = stdout.read(), stderr.read()
        # 去掉空行
        print outmsg.strip()
        return outmsg
    def close_ssh(self):
        self.new_connector.close()


# if __name__ == '__main__':
#     new_ssh_operator = init_ssh('192.168.135.133','root','sonyw320',22)
#     new_ssh_operator.run_ssh("ls")
#     new_ssh_operator.close_ssh()



