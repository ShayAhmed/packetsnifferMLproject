#following this: http://www.bitforestinfo.com/2017/01/how-to-write-simple-packet-sniffer.html
import socket

#inet socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP) 
#below is windows code for the line above
#s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
#s.bind(("YOUR_INTERFACE_IP",0))
#s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
#s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

while True:
     # print output on terminal
    print(s.recvfrom(65565))
