def setup(self, url: str) -> str:
    self.send_request("SETUP {} RTSP/1.0\r\nCSeq: 3\r\nTransport: RTP/AVP;unicast;client_port=8000-8001\r\n\r\n".format(url))
    return self.receive_response()
