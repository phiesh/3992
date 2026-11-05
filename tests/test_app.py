import unittest

import app


class TestApp(unittest.TestCase):

    def test_main_exists(self):
        self.assertTrue(callable(app.main))


if __name__ == "__main__":
    unittest.main()