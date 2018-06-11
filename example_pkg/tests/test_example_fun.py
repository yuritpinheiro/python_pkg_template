from unittest import TestCase

import example_pkg


class TestJoke(TestCase):
    def test_is_string(self):
        s = example_pkg.example_fun()
        self.assertTrue(isinstance(s, str))

