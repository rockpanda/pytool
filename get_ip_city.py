# -*- coding: utf-8 -*-
"""
    <项目名称>:<文件名称>
    <文件描述>
    :copyright: (c) 2019 by debris.
    :license: GPLv3, see LICENSE File for more details.
"""
import json
import requests
import os
"""
shell版本
IP=$(awk -F " " '{print $1}' /var/log/nginx/access.log)
for i in $IP
do
        curl https://ip.cn/?ip=$i > ip_city.txt  2>/dev/null &
done
"""
# access log
# grep -E "\w+.\w+.\w+.\w+ - - " /var/log/nginx/access.log | awk -F " - - " '{print $1}' | sort | uniq
# awk -F " " '{print $1}' /var/log/nginx/access.log | sort | uniq > /tmp/ip.txt

# error log
# nginx统计日志中客户端ip访问次数的方式
# cat access.log |awk -F"-"  '{print $1}'|sort -t $'.' -k 1n  |uniq -c
# cat access.log |awk -F"-"  '{print $1}'|sort -t $'.' -k 1nr  |uniq -c
# awk '{eng[$1]++}END{for(i in eng)print i "\t" eng[i]}' access.log

# 可以得到访问次数并按照降序排列
# awk -F " " '{print $1}' access.log | sort | uniq -c | sort -k 1 -n -r

# 命令如下：
# awk -F " " '{print $1}' /var/log/nginx/access.log | sort | uniq|sort -k 1 -n -r
# 可查询IP来源信息的网址
# https://ip.cn/?ip=


url = "http://ip.taobao.com/service/getIpInfo.php?ip="
# url = "https://ip.cn/?ip="
# os.popen("awk -F " " '{print $1}' /var/log/nginx/access.log | sort | uniq|sort -k 1 -n -r > /tmp/ip.txt")

ip_address = []


# header = {'user-agent': 'curl'}

def ip_list():
    with open('/Users/debris/Downloads/ip.txt', 'r') as f:
        for ip in f.readlines():
            if ip != None:
                ip_address.append(ip.strip("\n"))
                data = requests.get(url + ip).text
                get_city(data)
    f.close()


def get_city(data):
    test = json.loads(data)['data']
    print(test['ip'].strip("\n"), test['country'] + test['region'] + test['city'], test['isp'])

if __name__ == __name__:
    ip_list()
