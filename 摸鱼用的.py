import smtplib
from email.mime.text import MIMEText
SMTPServer ="smtp.qq.com"
Sender = "1875385776@qq.com"
passwd = "hbnmvyqzxeudeiae"
message = "当你收到这封邮件证明我写的代码完成了"
msg = MIMEText(message)
msg["Subject"] = "聂佬你好哇"
mailServer = smtplib.SMTP(SMTPServer,25)
mailServer.login(Sender,passwd)
mailServer.sendmail(Sender,["1078948862@qq.com"],msg.as_string())
mailServer.quit()