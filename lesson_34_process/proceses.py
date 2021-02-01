import socket
from typing import Tuple
import logging
import multiprocessing

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] {%(filename)s:%(lineno)d} {%(process)d:%(threadName)s} - %(message)s")

CESAR_SHIFT = 3
LETTERS_CNT = 26
SPACE_ID = 32


class ConnectionHander(multiprocessing.Process):

    def __init__(self, connection: socket.socket, addr: Tuple[str, int]):
        super().__init__()
        self.connection = connection
        self.host, self.port = addr[0], addr[1]
        logger.info(f'Accepted connection from {self.host}:{self.port}')

    def run(self, *args, **kwargs):
        data = self.connection.recv(1024)
        while data:
            encrypted_data = self._encrypt(data.decode())
            logger.info(f'{self.host}:{self.port} - {data.decode()} / {encrypted_data}')
            self.connection.send(encrypted_data.encode())
            data = self.connection.recv(1024)
        else:
            logger.info(f'Closed: {self.host}:{self.port}')

    def _encrypt(self, data: str):
        char_ids = []
        for char in data:

            if char == ' ':
                char_ids.append(SPACE_ID)
                continue

            char_id = ord(char)
            new_char_id = char_id + CESAR_SHIFT

            if char_id + CESAR_SHIFT > 90:
                new_char_id = char_id + CESAR_SHIFT - 90 + 65 - 1

            char_ids.append(new_char_id)
        return ''.join([chr(char_id) for char_id in char_ids])


with socket.socket() as s:
    try:
        s.bind(('localhost', 8088))
        s.listen(2)
        while 1:
            connection, address = s.accept()
            ConnectionHander(connection, address).start()
    except Exception:
        s.close()
