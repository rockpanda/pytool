# -*- coding: utf-8 -*-
"""
    learn python:ContainerHealthy
    <容器故障自愈>
    :copyright: (c) 2019 by learn python.
    :license: GPLv3, see LICENSE File for more details.
"""
"""
1 使用docker API 来获取容器健康状态以及运行状态？
	https://docker-py.readthedocs.io/en/stable/containers.html(只能获取容器运行状态，不能获取容器健康状态)
2 使用docker inspect --format  '{{.Name}} {{ .State.Health.Status}}' [Name] 命令获取docker健康状态？
3 容器故障自愈参数根据compose的健康检查时间即可
        interval: 60s
        timeout: 10s
        retries: 3
4 该程序根据compose的结果来判断，如果uhealthy达到了一定的次数就通知报警,重启后需要等待compose的健康结果出来了才能继续循环
"""

# import  docker
# 初始化
# client = docker.from_env()
# 通过获取ID，打印出自己需要的内容
# for container in client.containers.list():
#     print(container.status)
# subprocess.call(["docker","inspect","--format='{{.Name}},{{.State.Health.Status}}'","bigscreen"])

# 基础配置
import subprocess
import time
import os
import json
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from .config import *


# 遍历容器名称
def ContaineresName():
    for name in NameList:
        ContainerSatus(name)


# py通过调用shell命令获取容器状态
def ContainerSatus(name):
    cmd = (
            "docker inspect --format='{{.Name}},{{.State.Health.Status}}'  %s | awk -F ',' '{print $2}'" %
            name)
    status = os.popen(cmd).read()
    count = 0
    while status.split('\n')[0] != "healthy":
        print(time.strftime("%Y-%m-%d %H:%M:%S",
                            time.localtime()) + " %s container status is unhealthy,Please check the service" % (name))
        ContainerHealing(name)
        time.sleep(Waiting_Time)
        status = str(os.system(cmd))
        count += 1
        print(count)
        if count >= RetriesNumber:
            sendmessage(name, status)


# 故障自愈函数
def ContainerHealing(name):
    restart_cmd = "docker restart %r" % name
    os.system(restart_cmd)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " The container is restarting")


def sendmessage(name):
    # 钉钉机器人的webhook地址
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % token
    message = '%s container status  is unhealthy,please check the service!' % (name,)
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": message},
        "at": {
            "atMobiles": [
                "%s" % imuser
            ],
            "isAtAll": False
        }
    }
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)


# 启动函数
if __name__ == '__main__':
    ContaineresName()

# 在系统中后台运行命令持续运行
# nohup python -u ihealthy.py params1 > nohup.out &
