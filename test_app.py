import app
import unittest

class TestApp(unittest.TestCase):
    def setUp(self):
        self.players = [
            { 'first_name' : 'a',
              'last_name'  : 'A',
              'h_in'       : '1' },
            { 'first_name' : 'b',
              'last_name'  : 'B',
              'h_in'       : '2' },
            { 'first_name' : 'c',
              'last_name'  : 'C',
              'h_in'       : '3' },
            { 'first_name' : 'd',
              'last_name'  : 'D',
              'h_in'       : '3' },
            { 'first_name' : 'e',
              'last_name'  : 'E',
              'h_in'       : '4' },
            { 'first_name' : 'f',
              'last_name'  : 'F',
              'h_in'       : '5' },
            { 'first_name' : 'g',
              'last_name'  : 'G',
              'h_in'       : '6' }
        ]

    def test_name(self):
        self.assertEqual(app.get_name(self.players[0], False), 'a A')
        self.assertEqual(app.get_name(self.players[0], True), 'a A(1)')

    def test_pairs(self):
        self.assertEqual(app.get_pairs(self.players, 5, False),
                         'a A - e E\nb B - c C\nb B - d D\n')
        self.assertEqual(app.get_pairs(self.players, 7, False),
                         'a A - g G\nb B - f F\nc C - e E\nd D - e E\n')

    def test_edge_cases(self):
        # test no duplicated pairs and no pairing with itself
        self.assertEqual(app.get_pairs(self.players, 6, False),
                         'a A - f F\nb B - e E\nc C - d D\n')

    def test_no_matches_found(self):
        # test zero and negative weights, even if it is validated in
        # another part of the program
        self.assertEqual(app.get_pairs(self.players, 12, False), '')
        self.assertEqual(app.get_pairs(self.players, 0, False), '')
        self.assertEqual(app.get_pairs(self.players, -1, False), '')

    def test_get_players(self):
        self.assertEqual(len(app.get_players()), 435)
