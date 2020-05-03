import logging, socket
from udp import constants

class Client():
    def __init__(self):
        self.logger = logging.getLogger()

    def run(self):
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        while True:
            message = input('Enter your date of birth to find out what day of the week it was\nType dob as dd-mm-yyyy here: ')
            data = message.encode(encoding='ascii')
            s.sendto(data, ('127.0.0.1', 3000))
            self.logger.info('The OS assigned the address {} to client'.format(s.getsockname()))
            data, address = s.recvfrom(constants.MAX_SIZE_BYTES)
            text = data.decode(encoding='ascii')
            print('The server {} replied with {!r}'.format(address, text))

if __name__ == '__main__':
    Client().run()
