import logging

class Recvall():
    def __init__(self):
        self.logger = logging.getLogger()

    def send(self, sock, length):
        data = b''
        while len(data) < length:
            self.logger.info('Sending data...')
            more = sock.recv(length - len(data))
            if not more:
                raise EOFError('was expecting %d bytes but only received'
                            ' %d bytes before the socket closed'
                            % (length, len(data)))
            data += more
        return data
