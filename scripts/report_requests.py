#!/usr/bin/env python
# encoding: utf-8

import re
import smtplib
from email.mime.text import MIMEText
from collections import Counter

result_log_file = "/var/log/report_nginx_access.log"
nginx_log_file = "/var/log/nginx/access.log"

def nginx_log_parser(logfile):

  status_code = '"GET\s\D{1,20}\sHTTP/\d.\d\D\s\d{1,3}'

  with open(logfile) as parser:
    log = parser.read()
    find = re.findall(status_code,log)
    codes = Counter(find)
    f = open(result_log_file, 'w').close()
    for content, count in codes.items():
      result = (str(content) + " " + "Numero requisicoes "  + ":" + str(count))
      f = open(result_log_file, 'a')
      f.write(result + '\n')
      f.close()


def envia_email():
  fp = open(result_log_file, 'rb')
  msg = MIMEText(fp.read())
  fp.close()
  from_email = "root"
  to_email = "root"

  msg['Subject'] = 'Relatorio diario quantidade de requisicoes WEB %s' % result_log_file
  msg['From'] = from_email
  msg['To'] = to_email

  s = smtplib.SMTP('localhost')
  s.sendmail(from_email, [to_email], msg.as_string())
  s.quit()
  
if __name__ == '__main__':
  nginx_log_parser(nginx_log_file)
  envia_email()
