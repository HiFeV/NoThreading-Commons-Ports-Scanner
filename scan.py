import socket

host = input('Target to scan: ')
ip_res = socket.gethostbyname(host)

scanned_ports = [20, 21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443]
for port in scanned_ports:
    s = s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)
    try:
        connection = s.connect_ex((host, port))
        if connection == 0:
            print('Port {} OPEN'.format(port))
        connection.close()
        s.close()
    except:
        pass
