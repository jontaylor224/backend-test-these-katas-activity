import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(2, 2), 4)
        # self.fail("TODO: Write add unit test")

    def test_multiply(self):
        self.assertEqual(katas.multiply(2, 3), 6)
        # self.fail("TODO: Write multiply unit test")

    def test_power(self):
        self.assertEqual(katas.power(9, 2), 81)
        # self.fail("TODO: Write power unit test")

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)
        # self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(8), 13)
        # self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
