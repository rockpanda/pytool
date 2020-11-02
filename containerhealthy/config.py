# -*- coding: utf-8 -*-
"""
    <容器健康检查>:<config>
    <配置文件>
    :copyright: (c) 2019 by debris.
    :license: GPLv3, see LICENSE File for more details.
"""
NameList = ["bigscreen", "propagation-server", "decision-center"]
# 容器重启等待时间
Waiting_Time = 220
# 达到重启次数最大值则报警
RetriesNumber = 3
# 钉钉token
token = "20b3fa01e7e16dfde3deedbe83b5ddc94a6017d398157b68ecac483ff79b8958"
# 钉钉指定通知人(手机号)
imuser = ""
# 邮件发送者
sender = 'ContainerHealthy@trs.com.cn'
# 邮件接收者
receivers = ['zeng.chaojun@trs.com.cn']
