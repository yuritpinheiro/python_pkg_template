from unittest import TestCase

from example_pkg.command_line import main


class TestCmd(TestCase):
    def test_basic(self):
        main()

