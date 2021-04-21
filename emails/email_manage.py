import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailManage:

    def send_email(self):

        #定义SMTP服务器
        smtpserver = 'smtp.qq.com'
        #发送邮件的用户名合密码
        username = "1024269771@qq.com"
        password = "zhftjoormxbpbcgf"
        #接受邮件的邮箱
        receiver = "3547208134@qq.com"
        #创建邮件对象
        message = MIMEMultipart("related")
        subject = "最新LPR数据"    #邮件的主题
        fujian = MIMEText(open("test.png","rb").read(),"html","utf-8")
        #邮件信息组装到邮件对象里面
        message["form"] = username
        message["to"] = receiver
        message["subject"] = subject
        message.attach(fujian)
        #登录smtp服务器发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username,password)
        smtp.sendmail(username,receiver,message.as_string())
        smtp.quit()
if __name__ == '__main__':

    EmailManage().send_email()