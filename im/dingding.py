# -*- coding: utf-8 -*-
"""
    <项目名称>:<文件名称>
    <文件描述>
    :copyright: (c) 2019 by debris.
    :license: GPLv3, see LICENSE File for more details.
"""
import config as config
import json
import requests

def sendmessage(name):
    # 钉钉机器人的webhook地址
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % (config.token)
    message =  config.project + name + config.mail_default_content
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": message},
        "at": {
            "atMobiles": [
                "%s" % config.imuser
            ],
            "isAtAll": False
        }
    }
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)
