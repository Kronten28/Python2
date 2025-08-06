import socket
import pickle
from typing import Any, Tuple

def start_server() -> None:
    host: str = 'localhost'
    port: int = 9000
    backlog: int = 1
    buffer_size: int = 4096

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(backlog)
        print("Waiting for connection...")
        conn: socket.socket
        addr: Tuple[str, int]
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            data: bytes = b''
            while True:
                packet: bytes = conn.recv(buffer_size)
                if not packet:
                    break
                data += packet
            try:
                obj: Any = pickle.loads(data)
                print("Received:", obj)
            except (pickle.UnpicklingError, EOFError) as e:
                print("Failed to unpickle data:", e)

if __name__ == '__main__':
    start_server()
