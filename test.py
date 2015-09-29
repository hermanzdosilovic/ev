#!/usr/bin/env python

import ev
import mock
import pdb
import subprocess
import unittest


class SimpleCEvTest(unittest.TestCase):
    def setUp(self):
        self.valid_c_file_name = "hello.c"
        self.valid_c_problem_name = "hello"
        self.valid_c_file_type = "c"

        self.invalid_c_file_name = "hello.cpp"
        self.invalid_c_problem_name = "hello"
        self.invalid_c_file_type = "cpp"


class CEvTest(SimpleCEvTest):
    def test_compile_with_gcc_invalid_params(self):
        with self.assertRaises(Exception):
            ev.compile(
                self.invalid_c_file_name,
                self.invalid_c_problem_name,
                self.invalid_c_file_type
            )

    def test_compile_with_gcc_valid_params(self):
        subprocess.check_output = mock.MagicMock(return_value="")
        self.assertEqual(ev.compile(
            self.valid_c_file_name,
            self.valid_c_problem_name,
            self.valid_c_file_type
        ), "")

if __name__ == '__main__':
    unittest.main()
