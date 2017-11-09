import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '15861347259@163.com'
msg['to'] = '2602831739@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('15861347259@163.com', '1998.6.29zy')
smtp.sendmail('15861347259@163.com', '2602831739@qq.com', str(msg))
smtp.quit()
