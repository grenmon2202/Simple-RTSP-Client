from connection.response import Response

def describe(self, url: str) -> Response:
    self.send_request("DESCRIBE {} RTSP/1.0\r\nCSeq: 2\r\n\r\n".format(url))
    return self.receive_response()
