import socket
import pickle

def start_server():
    s = socket.socket()
    s.bind(('localhost', 9000))
    s.listen(1)
    
    print "Waiting for connection..."
    conn, addr = s.accept()
    print "Connected by", addr

    data = conn.recv(1024)
    
    obj = pickle.loads(data)
    
    print "Received:", obj
    conn.close()

if __name__ == '__main__':
    start_server()
