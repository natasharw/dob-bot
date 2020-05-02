import argparse, calendar, datetime, logging, socket
import constants

class UdpServer():
    def __init__(self):
        self.logger = logging.getLogger()

    def run(self):
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        port = constants.SERVER_PORT
        hostname = constants.SERVER_HOSTNAME
        s.bind((hostname,port))
        print('Listening at {}'.format(s.getsockname()))

        while True:
            data, client_address = s.recvfrom(constants.MAX_SIZE_BYTES)
            message = data.decode(encoding='ascii')
            self.logger.info('The client at {} says {!r}'.format(client_address, message))
            error = self.validate_input(message)

            if not error:
                day_born=self.get_week_day(message)
                reply_message = 'The day you were born on is {}'.format(day_born)
            else:
                reply_message = error

            data = reply_message.encode(encoding='ascii')
            s.sendto(data, client_address)
    
    def validate_input(self, message: str):
        try:
            datetime.datetime.strptime(message, '%d-%m-%Y')
        except ValueError:
            message = "Incorrect data format, please enter date as mm-dd-yyyy"
            return message

    def get_week_day(self, dt: str):
        born = datetime.datetime.strptime(dt, '%d-%m-%Y').weekday() 
        return (calendar.day_name[born]) 

if __name__ == '__main__':
    UdpServer().run()
