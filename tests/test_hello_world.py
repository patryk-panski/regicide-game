import unittest

from regicide_game.hello_world import greet

class TestGreet(unittest.TestCase):

    def test_greet_returns_hello_and_name(self):
        self.assertEqual(greet("Patryk"), "Hello Patryk")

if __name__ == "__main__":
    unittest.main()
