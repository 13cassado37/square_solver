import unittest as ut
from sequance import SquareSequence


class TestSequance_1_2_1(ut.TestCase):
    def setUp(self):
        self.seq = SquareSequence(1, 2, 1)

    def test_get_discriminant(self):
        self.assertEqual(self.seq.get_discriminant(), 0)

    def test_sequance_handler(self):
        self.assertEqual(self.seq.sequance_handler(), {'x1': -1.0, 'x2': -1.0})


class TestSequance_1_1_1(ut.TestCase):
    def setUp(self):
        self.seq = SquareSequence(1, 1, 1)

    def test_get_discriminant(self):
        self.assertEqual(self.seq.get_discriminant(), -3.0)

    def test_sequance_handler(self):
        self.assertEqual(self.seq.sequance_handler(), {'x1': None, 'x2': None})


class TestSequance_0_0_1(ut.TestCase):
    def setUp(self):
        self.seq = SquareSequence(0, 0, 1)

    def test_get_discriminant(self):
        self.assertEqual(self.seq.get_discriminant(), 0)

    def test_sequance_handler(self):
        self.assertEqual(self.seq.sequance_handler(), '[!] - ZeroDivision')


class TestSequance_0_0_0(ut.TestCase):
    def setUp(self):
        self.seq = SquareSequence(0, 0, 0)

    def test_get_discriminant(self):
        self.assertEqual(self.seq.get_discriminant(), 0)

    def test_sequance_handler(self):
        self.assertEqual(self.seq.sequance_handler(), '[!] - ZeroDivision')


class TestSequance_0_1_1(ut.TestCase):
    def setUp(self):
        self.seq = SquareSequence(0, 1, 1)

    def test_get_discriminant(self):
        self.assertEqual(self.seq.get_discriminant(), 1)

    def test_sequance_handler(self):
        self.assertEqual(self.seq.sequance_handler(), {'x': -1})


if __name__ == '__main__':
    ut.main()
