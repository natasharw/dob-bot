import datetime, logging, socket
import config
from recvall import Recvall

class Client():
    def __init__(self):
        self.logger = logging.getLogger()
            
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((config.SERVER_HOSTNAME, config.SERVER_PORT))

        print('Client has been assigned the socket: {}'.format(s.getsockname()))

        while True:
            try:
                dt = input('Enter your date of birth to find out what day of the week it was\nType dob as dd-mm-yyyy here: ')
                datetime.datetime.strptime(dt, '%d-%m-%Y')
            except ValueError:
                print("Incorrect data format, please enter date as mm-dd-yyyy")
            else:
                break

        message = dt.encode('UTF-8')
        s.sendall(message)
        reply = Recvall.send(self, sock=s, length=31)
        print('The server replied with {!r}'.format(reply.decode('UTF-8')))
        print('Closing socket')
        s.close()

if __name__ == '__main__':
    Client().run()
