from django.shortcuts import render,render_to_response,HttpResponse
import os,psutil
from models import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from artlog import *
import json



def auth(request):
    title="goodbye,2017."
    news="tommorw is another day."
    return_code=0

    if request.method == "POST":
        username=request.POST.get("username",None)
        password=request.POST.get("password", None)
        dir=os.path.dirname(__file__)
        #username=username.encode('utf-8').encode('bz2')
        #password=Code.db_encode(password)
        if not username:
            return_code=2 # username is null
        if not password:
            return_code=3 # password is null
        if return_code == 0:
            if userdb.objects.filter(username=username):
                return_code=5
        if return_code == 0:
            newer=userdb(username=username,password=password,dir=dir)
            newer.save()
            return_code=6
    return render_to_response("auth.html",locals())

@csrf_exempt
def mainpage(request):
    if request.is_ajax():
        return render_to_response("login.html", locals())

    cpuinfo=psutil.cpu_percent()
    meminfo = psutil.virtual_memory().percent
    diskinfo = psutil.net_io_counters(pernic=True)['\xce\xde\xcf\xdf\xcd\xf8\xc2\xe7\xc1\xac\xbd\xd3']
    localres={"cpuif":cpuinfo,"memif":meminfo}
    allres={"127.0.0.1":{"cpuif":cpuinfo,"memif":meminfo,"diskif":diskinfo,"password": "Root@123"}}
    allres["192.168.1.13"]={"cpuif": cpuinfo, "memif": meminfo,"diskif":diskinfo,"password": "Root@123"}

    if request.method == "POST":
        allres["192.168.1.14"] = {"cpuif": cpuinfo, "memif": meminfo, "diskif": diskinfo, "password": "Root@123"}

    #return render_to_response("main.html", locals())
    return render_to_response("bootstrap/pages/index.html", locals())


def tablespage(request):
    return render_to_response("bootstrap/pages/tables.html")


def addMachine(ipaddr,username,passwd,mcinfo):
    try:
        new_machine = machinelist()
        info("messages.log","%s_%s_%s_%s" % (ipaddr,username,passwd,mcinfo))
        new_machine = machinelist(ipaddr=ipaddr,netmask="255.255.255.0",username=username,password=passwd,mcmark=mcinfo)
        # new_machine.ipaddr = ipaddr
        # new_machine.username = username
        # new_machine.password = pwd
        # new_machine.mcmark = mcinfo
        new_machine.save()
    except Exception,e:
        errlog("messages.log","add new machine %s into DB failed,and reason is: %s" % (ipaddr,e.message))


def delMachine(tarip):
    try:
        machinelist.objects.filter(ipaddr=tarip).delete()
        info("messages.log", "del the machine %s from DB succeed." % tarip )
    except Exception,e:
        errlog("messages.log","del the machine %s from DB failed,and reason is: %s" % (tarip,e.message))


def login(request):
    cpuinfo=psutil.cpu_percent()
    meminfo = psutil.virtual_memory().percent

    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password", None)
        userlist = userdb.objects.all()
        err_code=0
        for theuser in userlist:
            if username == theuser.username:
                if password == theuser.password:
                    return render_to_response("main.html", locals())
                else:
                    err_code=1
        return render_to_response("login.html", locals())
    else:
        return render_to_response("login.html", locals())


def selectpage(request,selectUrl):
    info("messages.log", "hello post\r\n")
    allmclist = {}
    mcdata = machinelist.objects.all()
    for mc_obj in mcdata:
        allmclist[mc_obj.ipaddr] = {"username": mc_obj.username, "mcpwd": mc_obj.password, "mcnetmask": mc_obj.netmask,"mccpu": mc_obj.mccpu, "mcmem": mc_obj.mcmem,"mcalldisk":mc_obj.mcalldisk}

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            json_method = data['method']
            info("messages.log", request.body)
            # method = request.POST.get("method",None)
            if json_method == '1':
                ipaddr = data['ipaddr']
                username = data['username']
                passwd = data['pwd']
                mcinfo = data['info']
                addMachine(ipaddr,username,passwd,mcinfo)
                resp = {'code': 100, 'detail': 'Get success'}
                return HttpResponse(json.dumps(resp), content_type="application/json")
            if json_method == '2':
                mcdata = machinelist.objects.all()
                for mc_obj in mcdata:
                    allmclist[mc_obj.ipaddr] ={"username":mc_obj.username,"mcpwd":mc_obj.password,"mcnetmask":mc_obj.netmask,"mccpu":mc_obj.mccpu,"mcmem":mc_obj.mcmem,"mcalldisk":mc_obj.mcalldisk}
                #info("messages.log", allmclist)
                resp = {'code': 200, 'detail': 'Get success'}
                return HttpResponse(json.dumps(allmclist), content_type="application/json")
            if json_method == '3':
                ipaddrs = data['ipaddrs']
                for ips in ipaddrs:
                    delMachine(ips)
                    # info("messages.log", ips)
                # ipaddr = request.POST.get("ipaddr",'The ipaddrs is null.')
                resp = {'code': 100, 'detail': 'Del success'}
                return HttpResponse(json.dumps(resp), content_type="application/json")
        except Exception,e:
            errlog("messages.log", e.message)

    link_url= "bootstrap/pages/" + selectUrl
    return render_to_response(link_url,locals())





