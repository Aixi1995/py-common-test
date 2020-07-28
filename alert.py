# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json
import socket
import time
from urllib import request
from urllib import error
import psutil
import logging

check_health_url = 'http://localhost:12581/qrCodeActuator/health'
from_addr = 'XXX@163.com'  # account to send
to_addrs = 'XXX@qq.com'  # account to receive
qqCode = 'HQGZZNZZGHNDEZMF'  # authorization code
smtp_server = 'smtp.163.com'  # smtp server
smtp_port = 465  # smtp port
stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
stmp.login(from_addr, qqCode)
local_ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))


def check_health():
    try:
        resp = request.urlopen(url=check_health_url)
        if resp is None or 'UP' != json.loads(resp.read().decode())['status']:
            return False
        return True
    except error.URLError as e:
        logging.error('http request failed')
        return False


def check_memory():
    mem_percent = psutil.virtual_memory().percent
    if mem_percent > 60:
        return False
    return True


def check_disk():
    pass


def send_warn_email(warn_msg):
    message = MIMEText(warn_msg, 'plain', 'utf-8')
    message['From'] = Header("服务告警系统", 'utf-8')
    message['To'] = Header("开发者", 'utf-8')
    message['Subject'] = Header('服务告警', 'utf-8')  # subject of the email
    try:
        stmp.sendmail(from_addr, to_addrs, message.as_string())
    except Exception as e:
        logging.error('邮件发送失败, 报警信息: %s 异常信息: %s' % (warn_msg, e))


if __name__ == '__main__':
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    if not check_health():
        warn_msg = '时间: %s \nip: %s \n报警详情: 服务不可用' % (current_time, local_ip)
        send_warn_email(warn_msg)
    if not check_memory():
        warn_msg = '时间: %s \nip: %s \n报警详情: 内存告警, total: %s(Mb), used: %s(Mb), free: %s(Mb), percent: %.2f%%' % \
                   (current_time, local_ip, psutil.virtual_memory().total, psutil.virtual_memory().used,
                    psutil.virtual_memory().free, psutil.virtual_memory().percent)
        send_warn_email(warn_msg)
