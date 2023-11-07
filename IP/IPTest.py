import socket
import requests
import os
import time
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from ssl import PROTOCOL_TLS_SERVER, SSLContext

class WifiFinder:
    def __init__(self, *args, **kwargs):
        self.server_name = kwargs['server_name']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}

    def run(self):
        command = """sudo iwlist wlp2s0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
        result = os.popen(command.format(self.server_name))
        result = list(result)

        if "Device or resource busy" in result:
                return None
        else:
            ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]
            print("Successfully get ssids {}".format(str(ssid_list)))

        for name in ssid_list:
            try:
                result = self.connection(name)
            except Exception as exp:
                print("Couldn't connect to name : {}. {}".format(name, exp))
            else:
                if result:
                    print("Successfully connected to {}".format(name))

    def connection(self, name):
        try:
            os.system("nmcli d wifi connect {} password {} iface {}".format(name,
       self.password,
       self.interface_name))
        except:
            raise
        else:
            return True

def get_internal_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def create_server():
	ssl_context = SSLContext(PROTOCOL_TLS_SERVER)
	ssl_context.load_cert_chain("/home/password/Certificate/cert.pem", "/home/password/Certificate/private.key")
	server = HTTPServer(("0.0.0.0", 8420), SimpleHTTPRequestHandler)
	server.socket = ssl_context.wrap_socket(server.socket, server_side=True)
	print("Server Started")
	server.serve_forever()
     
def internet_on():
    try:
        requests.get('https://google.com', timeout=1)
        return True
    except Exception as err: 
        return False
    
def run_server():
	threading.Thread(target=create_server).start()
	time.sleep(1)
	print("The Robot's IP Address Is: " + get_internal_ip())
	print("Please Connect To The Following Address To Continue Setup: https://" + get_internal_ip() + ":8420")
	while True:
		time.sleep(1)
    
while not internet_on():
	print("Please connect to a network: ")
	server_name = "example_name"
	password = "your_password"
	interface_name = "your_interface_name" # i. e wlp2s0
	WF = WifiFinder(server_name=server_name,password=password,interface=interface_name)
	WF.run()   
run_server()