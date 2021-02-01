import threading
import socket


class ConnectionHander(threading.Thread):

    def __init__(self, connection: socket.socket):
        super().__init__()
        self.connection = connection

    def run(self, *args, **kwargs):
        while 1:
            data = s.recv(1024)
            if not data:
                break
            print(f'\nEncrypted message: {data.decode()}')


with socket.socket() as s:
    try:
        s.connect(('127.0.0.1', 3003))
        ConnectionHander(s).start()
        while 1:
            s.send(
                str(dict(
                    user_name='Ivan2',
                    message=input('What data send?'),
                    recipient=input('Recipient')
                )).encode()
            )
    except Exception:
        s.close()