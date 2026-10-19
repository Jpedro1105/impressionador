import unittest
from soma import somar


class TesteSoma(unittest.TestCase):
    def test_soma_dois_valores(self):
        self.assertEqual(somar(100, 200), 300)


if __name__ == "__main__":
    unittest.main()