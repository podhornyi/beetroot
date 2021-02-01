import socket
import json
from typing import Tuple, List
from dataclasses import dataclass, field
import threading
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] {%(filename)s:%(lineno)d} {%(process)d:%(threadName)s} - %(message)s")


@dataclass(unsafe_hash=False, eq=False)
class Client:
    connection: socket.socket
    addr: Tuple[str, int]
    name: str = field(default='')
    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self.name == other.name


@dataclass
class Error:
    code: int
    def as_dict(self):
        return dict(
            error=dict(
                code=self.code
            )
        )


@dataclass
class Message:
    message: str
    user_name: str
    recipient: str = field(default='')

    def as_dict(self):
        data = dict(
            user_name=self.user_name,
            message=self.message,
            recipient=self.recipient
        )
        if not self.recipient:
            del data['recipient']
        return data

    @classmethod
    def raw(cls, data: str):
        try:
            data = json.loads(data.replace('\'', '"'))
        except Exception:
            logger.warning(f'Can not parse message: {data}, {type(data)}')
            return None
        logger.debug(f'Encoded data: {data}')
        return cls(
            message=data.get('message'),
            user_name=data.get('user_name'),
            recipient=data.get('recipient')
        )


class Chat:
    clients: List[Client] = []

    class ClientProcessor(threading.Thread):

        def __init__(self, client: Client):
            super().__init__()
            self._client = client

        def run(self, *args, **kwargs):
            data = self._client.connection.recv(1024)
            while data:
                message: Message = Message.raw(data.decode())
                if message:
                    if not self._check_name(message):
                        self._client.connection.send(str(Error(403).as_dict()).encode())
                    else:
                        Chat.send_message(self._client, message)
                else:
                    self._client.connection.send(str(Error(402).as_dict()).encode())
                data = self._client.connection.recv(1024)
            else:
                logger.info(f'Closed: {self._client.addr[0]}:{self._client.addr[1]}')

        def _check_name(self, message: Message):
            if not self._client.name:
                self._client.name = message.user_name
            else:
                for client in Chat.clients:
                    if client.name == self._client.name:
                        return False
            return True

    def __init__(self, address: str, port: int):
        self._address = address
        self._port = port

    def start(self):
        with socket.socket() as s:
            try:
                s.bind((self._address, self._port))
                s.listen(2)
                while 1:
                    connection, address = s.accept()
                    client = Client(connection, address)
                    Chat.clients.append(client)
                    self.process_client(client)
            except KeyboardInterrupt:
                s.close()
            except Exception as e:
                logger.error(e)
                print(e)
                s.close()

    def process_client(self, client: Client):
        Chat.ClientProcessor(client).start()

    @classmethod
    def get_recipient(cls, recipient: str):
        recipients = [client for client in cls.clients if client.name == recipient]
        if recipients:
            return recipients[0]

    @classmethod
    def send_message(cls, sender: Client, message: Message):
        logger.info(f'Chat.send_message {message}, sender {sender}')
        if message.recipient:
            recipient: Client = cls.get_recipient(message.recipient)
            if recipient:
                recipient.connection.send(message.message.encode())
            else:
                sender.connection.send(str(Error(401).as_dict()).encode())
        else:
            for client in cls.clients:
                if client == sender:
                    continue
                client.connection.send(str(message.as_dict()).encode())


if __name__ == '__main__':
    chat = Chat('10.10.1.64', int(input('Port:')))
    chat.start()