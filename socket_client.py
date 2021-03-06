import socket
import time
import sys

HOSTNAME = "10.0.1.3"
PORT = 12345
INTERVAL = 3
RETRYTIMES = 10

def socket_connect(host, port, interval, retries):

    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       

    for x in range(retries):
        try:
            c_socket.connect((host, port))
            return c_socket
        except socket.error:
            print("wait"+str(interval)+"s")
            time.sleep(interval)

    c_socket.close()
    return None

def main():

    c_socket = socket_connect(HOSTNAME,PORT,INTERVAL,RETRYTIMES)

    if c_socket is None:
        print("system exit:connection error")
        sys.exit(0)

    while(1):
        recvdata = c_socket.recv(1024)
        print("ReciveData:"+str(recvdata))
        senddata = input("SendData:")
        c_socket.send(senddata.encode())
        if (recvdata == "quit") or (senddata == "quit"):
            c_socket.close()
            break
             
if __name__ == '__main__':
    main()