import sys
import socket
import concurrent.futures




def port_scanner(ip,port):

    if "-" in port:

        range_of_ports(ip,port)
    
    elif "," in port:
        
        multiple_ports(ip,port)
    
    else:

        single_port(ip,port)
        
        
def single_port(ip,port):
     
    try:
            
            print("Scanning...")

            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        
                if s.connect_ex((ip,int(port))) == 0:

                    print(f"Port {port} is open")
                
                else:

                    print(f"Port {port} is closed")


    except socket.error as e:
        
        print(f"Error connecting to {port}:{ip} - {e}")


def range_of_ports(ip,port):

    print(f"Scanning ports {port}")

    port_split = port.split("-")

    ports = range(int(port_split[0]), int(port_split[1])+ 1 )
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

        for port in ports:
            
            executor.submit(single_port,ip ,port)

        
    


def multiple_ports(ip,port):
    
    print(f"Scanning ports {port}")

    port_split = port.split("-")

    ports = range(int(port_split[0]), int(port_split[1])+ 1 )
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

        for port in ports:

            executor.submit(single_port,ip ,port)
        
    

if __name__ == "__main__":

    ip = sys.argv[1]

    port = sys.argv[2]

    port_scanner(ip,port)
