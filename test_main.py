import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_func(self):
        self.assertEqual(main.func(1), 2)

if __name__ == '__main__':
    unittest.main()

