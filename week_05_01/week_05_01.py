import socket
import time


class Client():
    @staticmethod
    def parse_server_response(response):


    def __init__(self, host, port, timeout=None):
        self.sock = socket.create_connection(
            address=(host, port),
            timeout=timeout)

    def put(self, metrics, metrics_value, timestamp=None):
        timestamp = timestamp or int(time.time())
        request = 'put ' + str(metrics) + str(metrics_value) + str(timestamp) + '\n'
        self.sock.send(request.encode('utf8'))

    def get(self, metrics_name):
        request = str(metrics_name)
        self.sock.send('get ' + metrics_name + '\n', )
        response = self.sock.recv(1024).decode('utf8')
        response = response.rstrip(['\n'])
        if response == 'ok':
            return {}