import sys
import socket





def port_scanner(ip,port):

    if "-" in port:
        range_of_ports(ip,port)
    
    elif "," in port:
        multiple_ports(ip,port)
    
    else:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    
            if s.connect_ex((ip,port)) == 0:
                print(f"Port {port} is open")
            
            else:
                print(f"Port {port} is closed")



def range_of_ports(ip,port):
    
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

        print("Scanning...")
        ports = port.split("-")
        for port in range(int(ports[0]), int(ports[1])+ 1 ):
            if s.connect_ex ((ip,port))== 0:
                print(f"Port {port} is open")
            
            else:
                print(f"Port {port} is closed")
                        



def multiple_ports(ip,port):

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

        ports = port.split(",")
        for port in range(int(ports[0]), int(ports[1])+ 1 ):
            if s.connect_ex ((ip,port))== 0:
                print(f"Port {port} is open")
            
            else:
                print(f"Port {port} is closed")
                


if __name__ == "__main__":
    ip = sys.argv[1]

    port = sys.argv[2]

    port_scanner(ip,port)