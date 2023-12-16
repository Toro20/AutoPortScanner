import socket
import nmap

portScanner = nmap.PortScanner()

addr = input("Please enter the address you would like to scan(xxx.xxx.xxx.xxx): ")
kindOfScan = input("""\nWhich kind of scan?:
                   1)UDP Scan
                   2)SYN ACK Scan
                   3)Comprehensive Scan\n""")


if kindOfScan == '1':
    portScanner.scan(addr, '1-1024', '-v -sU')
    scanInfo = portScanner[addr]
    print("IP Status: ", portScanner[addr].state())

    if 'udp' in scanInfo:
        udpData = scanInfo['udp']
        if udpData:
            print("Open ports: ", udpData.keys())
        else:
            print("No UDP data available")
    else:
        print("No UDP data available")
elif kindOfScan == '2':
    portScanner.scan(addr, '1-1024', '-v -sS')
    scanInfo = portScanner[addr]
    print("IP Status: ", portScanner[addr].state())

    if 'tcp' in scanInfo:
        tcpData = scanInfo['tcp']
        if tcpData:
            print("Open ports", tcpData.keys())
        else:
            print("No TCP data available")
    else:
        print("No TCP data available")
elif kindOfScan == '3':
    portScanner.scan(addr, '1-1024', '-v -sS -sC -sV -A -O')
    scanInfo = portScanner[addr]

    tcpData = scanInfo['tcp']

    print("IP Status: ", portScanner[addr].state())
    print("MAC : ", scanInfo)
    print("Name: ", scanInfo['hostnames'])
    print("Open ports", tcpData.keys())

else:
    print("Please enter a valid response")





# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.settimeout(5)

# host = "143.244.220.150"
# port = 443

# def scan(port):
#     if sock.connect_ex((host,port)):
#         print("Port", port, "is closed")
#     else:
#         print("Port", port, "is open")


