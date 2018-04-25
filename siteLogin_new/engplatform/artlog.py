import datetime
# coding:utf-8


def info(logfilename,loginfo):
    with open(logfilename,'a') as logfile:
        loginfo = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") + " [INFO]: " + loginfo + "\n"
        logfile.write(loginfo)

def errlog(logfilename,errinfo):
    with open(logfilename,'a') as logfile:
        loginfo = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") + " [ERROR]: " + errinfo + "\n"
        logfile.write(loginfo)

def warnlog(logfilename,warninfo):
    with open(logfilename,'a') as logfile:
        loginfo = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") + " [WARNING]: " + warninfo + "\n"
        logfile.write(loginfo)

def readfile(filename):
    with open(filename, 'r') as readfile:
        return readfile.readlines()

