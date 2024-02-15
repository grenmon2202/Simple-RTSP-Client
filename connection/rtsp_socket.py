import socket
from connection.response import Response

class RTSPSocket:
    
    from .methods.describe import describe
    from .methods.setup import setup

    def __init__(self, address: str, port: int) -> None:
        
        self.__address : str = address
        self.__port : int = port

        self.__websocket : socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    

        self.__connect()

    def __connect(self) -> None:
        self.__websocket.connect((self.__address, self.__port))

    def send_request(self, request: str) -> None:
        self.__websocket.send(request.encode())

    def receive_response(self) -> Response:
        return Response(self.__websocket.recv(5242880).decode())
