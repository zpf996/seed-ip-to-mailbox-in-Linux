# seed-ip-to-mailbox-in-Linux
自动发送ip至邮箱  Automatically send IP to mailbox


在/etc/rc.local的exit 0前加入加入开机执行脚本

vim /etc/rc.local
python /mnt/sendIpMail.py
