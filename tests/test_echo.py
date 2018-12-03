#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_u(self):
        args = ['hello', '-u']
        namespace = self.parser.parse_args(args)

        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(namespace), 'HELLO')

    def test_upper(self):
        args = ['hello', '--upper']
        namespace = self.parser.parse_args(args)

        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(namespace), 'HELLO')

    def test_l(self):
        args = ['Hello', '-l']
        namespace = self.parser.parse_args(args)

        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(namespace), 'hello')

    def test_lower(self):
        args = ['Hello', '--lower']
        namespace = self.parser.parse_args(args)

        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(namespace), 'hello')

    def test_t(self):
        args = ['hello', '-t']
        namespace = self.parser.parse_args(args)

        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(namespace), 'Hello')

    def test_title(self):
        args = ['hello', '--title']
        namespace = self.parser.parse_args(args)

        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(namespace), 'Hello')

    # def test_all(self):
    #     process = subprocess.Popen(
    #         ["python", "echo.py", "-tul", "test"],
    #         stdout=subprocess.PIPE)
    #     stdout, _ = process.communicate()
    #     self.assertTrue(stdout.islower())

    #     process = subprocess.Popen(
    #         ["python", "echo.py", "-tlu", "test"],
    #         stdout=subprocess.PIPE)
    #     stdout, _ = process.communicate()
    #     self.assertTrue(stdout.isupper())

    #     process = subprocess.Popen(
    #         ["python", "echo.py", "-ult", "test"],
    #         stdout=subprocess.PIPE)
    #     stdout, _ = process.communicate()
    #     self.assertTrue(stdout.istitle())

    def test_none(self):
        args = ['Hello']
        namespace = self.parser.parse_args(args)

        self.assertTrue(namespace.text)
        self.assertEquals(echo.main(namespace), 'Hello')


if __name__ == '__main__':
    unittest.main()
