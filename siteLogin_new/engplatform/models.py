from django.db import models
# -*- coding:utf-8 -*-
# Create your models here.


class userdb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=32)
    dir=models.CharField(max_length=100)

class uploadFile(models.Model):
    username = models.CharField(max_length=30)
    headFile = models.FileField(upload_to='./upload/')
    def __unicode__(self):
        return self.username

class machinelist(models.Model):
    ipaddr = models.CharField(max_length=18)
    netmask = models.CharField(max_length=18)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    mcmark = models.CharField(max_length=30)
    mccpu = models.IntegerField(default=36)
    mcmem = models.IntegerField(default=36)
    mcalldisk = models.IntegerField(default=0)
    mcrundisk = models.IntegerField(default=0)
    mcprocessallnum = models.IntegerField(default=0)
    mcprocessrunnum = models.IntegerField(default=0)
    mcprocesszomnum = models.IntegerField(default=0)
    mcdiskspeed = models.IntegerField(default=0)
    mcnetspeed = models.IntegerField(default=0)





