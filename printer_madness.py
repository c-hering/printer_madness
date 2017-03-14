#!/us/bin/python
import socket

s = socket.socket()
port = "TBD"
targets = open('target', 'r')
target_ip = targets.readline()
ip_list = []
file_to_print = 'txt.txt'

def print_proc(host):
    s.connect((host,port))
    try:
        s.send('print command')
        s.close()
        
while not target_ip == null:
    ip_list.append(target_ip)
map(print_proc, ip_list)
