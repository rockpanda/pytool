#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import config as config


# 根据对象生成用于发送的用户串
def email_bean_to_user_str(mail_user):
    user_str = ""
    for EmailBean in mail_user:
        user_str += "," + str(formataddr([EmailBean["name"], EmailBean["email"]]))
    if len(user_str) > 1:
        return user_str[1:]
    else:
        return


# 获取邮箱的数组
def email_bean_to_array(mail_user):
    user_array = []
    for Email in mail_user:
        user_array.append(Email["email"])
    return user_array


def mail(info=config.mail_default_content, subject=config.mail_default_subject):
    ret = True
    # noinspection PyBroadException
    try:
        msg = MIMEText(info, 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["TRS", config.mail_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = email_bean_to_user_str(config.mail_user)
        # 邮件的主题，也可以说是标题
        msg['Subject'] = subject
        # 发件人邮箱中的SMTP服务器，端口是25
        server = smtplib.SMTP(config.mail_stmp, 25)
        # 括号中对应的是发件人邮箱账号、邮箱密码
        server.login(config.mail_sender, config.mail_pass)
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(config.mail_sender, email_bean_to_array(config.mail_user), msg.as_string())
        # 关闭连接
        server.quit()
    # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    except Exception:
        ret = False
    return ret
