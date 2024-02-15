from dataclasses import dataclass
import re
from exceptions.connection_exceptions import UnknownReponse
from typing import Dict

@dataclass
class Response:
    status: str
    status_code: int
    content: Dict
    text: str

    def __init__(self, response_string: str) -> None:
        status_line = response_string.split('\n')[0]
        splits = status_line.split(' ')

        if len(splits) != 3:
            raise UnknownReponse('Unable to parse response status: {}'.format(response_string))

        self.status = splits[-1]
        self.status_code = int(splits[1])
        self.content = self.__parse_content(response_string)
        self.text = response_string

    def __parse_content(self, response_string: str) -> Dict:
        splits = response_string.split('\n')

        content = dict()

        for split in splits:
            if '=' in split:
                line_split = split.split('=')
                content[line_split[0]] = '='.join(line_split[1:]).strip().replace('\r', '')
            elif ':' in split:
                line_split = split.split(':')
                content[line_split[0]] = ':'.join(line_split[1:]).strip().replace('\r', '')

        return content
