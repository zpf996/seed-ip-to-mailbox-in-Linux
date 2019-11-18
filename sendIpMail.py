import socket
import fcntl
import struct
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', ifname[:15]))[20:24])

localIP=get_ip_address('eth0')

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr="qqliao_shu_feng@163.com"
password="4＊＊＊"
smtp_server="smtp.163.com"
to_addr="619692290@qq.com"
server = smtplib.SMTP(smtp_server, 25)

msg = MIMEText('%s'%localIP, 'plain', 'utf-8')
msg['From'] = _format_addr(u'Alex <%s>' % from_addr)
msg['To'] = _format_addr(u'QQ邮箱 <%s>' % to_addr)
msg['Subject'] = Header(u'树莓派的ip……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
