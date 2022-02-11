#auther: Manlou
#date: 2020/10/08

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SendMail:
    """
    发送邮件
    """
    def __init__(self, mail_host):
        self.mail_host = mail_host

    def send(self, title, content, sender, auth_code, receivers):
        """
        发送
        :param title: 邮件标题
        :param content: 内容
        :param sender: 发送人
        :param auth_code: 授权码
        :param receivers: 接收人
        :return:
        """
        message = MIMEText(content, 'html', 'utf-8')
        message['From'] = "{}".format(sender)  # 配置发送人
        message['To'] = ",".join(receivers)    # 配置接收人
        message["Subject"] = title  # 标题
        try:
            smtp_obj = smtplib.SMTP_SSL(self.mail_host, 465)  # 启用ssl发信，端口一般是465
            smtp_obj.login(sender, auth_code)  # 授权码登录
            smtp_obj.sendmail(sender, receivers, message.as_string())
            print("测试报告发送成功")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    mail = SendMail("smtp.163.com")
    sender = "manlou117@163.com"
    receivers = ['manlou117@163.com', 'manlou117@163.com']
    title = "邮件"
    content = """
    <a href="https://www.baidu.com">点我</a>
    """
    # 授权码获取
    auth_code = "GPTTVZWBQOYAGSJB"
    mail.send(title, content, sender, auth_code, receivers)
