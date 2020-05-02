import unittest
from udp_server import UdpServer

class TestUdpServer(unittest.TestCase):
    def setUp(self):
        self.server = UdpServer()

    def test_validate_input_1(self):
        message = '2001'
        self.assertEqual(self.server.validate_input(message), "Incorrect data format, please enter date as mm-dd-yyyy")
    
    def test_validate_input_2(self):
        message = '01-31-2000'
        self.assertEqual(self.server.validate_input(message), "Incorrect data format, please enter date as mm-dd-yyyy")
  
    def test_validate_input_3(self):
        message = 'foo bar foo'
        self.assertEqual(self.server.validate_input(message), "Incorrect data format, please enter date as mm-dd-yyyy")

    def test_validate_input_4(self):
        message = ''
        self.assertEqual(self.server.validate_input(message), "Incorrect data format, please enter date as mm-dd-yyyy")

    def test_validate_input_5(self):
        message = '05-05-1992'
        self.assertEqual(self.server.validate_input(message), None)

    def test_get_week_day_1(self):
        dt = '05-05-1992'
        self.assertEqual(self.server.get_week_day(dt), 'Tuesday')

    def test_get_week_day_2(self):
        dt = '01-01-2000'
        self.assertEqual(self.server.get_week_day(dt), 'Saturday')
