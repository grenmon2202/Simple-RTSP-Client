import re
from connection.rtsp_socket import RTSPSocket
from exceptions.client_exceptions import NoTrack

class RTSPClient:
    
    def __init__(self, address: str, port: int, cam_uri: str) -> None:
        self.uri : str = cam_uri
        self.connection : RTSPSocket = RTSPSocket(address, port)
        self.track : str | None = None

    def __init_track(self) -> None:
        describe_response = self.connection.describe(self.uri)
        matches = re.search(r'a=control:(\S+)', describe_response.text)
        
        if not matches:
            return None

        track = None

        for group in matches.groups():
            track = group
        
        self.track = track

    def __init_stream(self) -> None:
        if not self.track:
            raise NoTrack('Track has not been initialised yet')

        print(self.connection.setup(self.track))

    def play(self) -> None:
        self.__init_track()
        self.__init_stream()
