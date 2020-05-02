import unittest
from tcp_server import TcpServer

class TestTcpServer(unittest.TestCase):
    def setUp(self):
        self.server = TcpServer()

    def test_get_week_day_1(self):
        dt = '05-05-1992'
        self.assertEqual(self.server.get_week_day(dt), 'Tuesday')

    def test_get_week_day_2(self):
        dt = '01-01-2000'
        self.assertEqual(self.server.get_week_day(dt), 'Saturday')
