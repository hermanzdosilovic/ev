#!/usr/bin/env python

import unittest
import pdb
import ev


class SimpleEvTest(unittest.TestCase):
    def setUp(self):
        self.c_file_name = "hello.c"
        self.c_problem_name = "hello"
        self.c_file_type = "c"

class EvTest(SimpleEvTest):
    def test_compile_with_gcc(self):
        with self.assertRaises(Exception):
            ev.compile(self.c_file_name, self.c_problem_name, self.c_file_type)

if __name__ == '__main__':
    unittest.main()
