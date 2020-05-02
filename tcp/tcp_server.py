import calendar, datetime, logging, socket
import config
from tcp_recvall import TcpRecvall

class TcpServer():
    def __init__(self):
        self.logger = logging.getLogger()
 
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('127.0.0.1', config.SERVER_PORT))
        sock.listen(1)
        print('Listening at: ', sock.getsockname()) 

        while True:
            print('Waiting for a new connection')
            sc, sockname = sock.accept()
            print('Connection from', sockname)
            print('Socket name:', sc.getsockname())
            print('Socket peer:', sc.getpeername())
            data = TcpRecvall.send(self, sock=sc, length=10)
            print('Message from client:', data.decode('UTF-8'))

            message = data.decode('UTF-8')
            error = self.validate_input(message)
            if not error:
                day_born=self.get_week_day(message)
                reply_message = 'The day you were born on is {}'.format(day_born)
            else:
                reply_message = error

            reply = reply_message.encode('UTF-8')
            sc.sendall(reply)
            sc.close()
            print('Closing socket')

    def get_week_day(self, dt: str):
        born = datetime.datetime.strptime(dt, '%d-%m-%Y').weekday() 
        return (calendar.day_name[born]) 

if __name__ == '__main__':
    TcpServer().run()
