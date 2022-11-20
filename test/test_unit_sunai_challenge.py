#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from src.sunai_challenge import SunaiChallenge


#@unittest.skip
class TestSunaiChallenge(unittest.TestCase):
    def setUp(self):
        self.sunai = SunaiChallenge()


    #@unittest.skip
    def test_argparse(self):
        expected_input = "input_test_folder"
        expected_output = "output_TEST"
        expected_graph = "alternative_folder"
        expected_force_mode = True
        args = ["-F", "-g", expected_graph, expected_input, expected_output]
        parsed_args = self.sunai.parse_args(args)

        self.assertEqual(expected_input, parsed_args.input_folder[0])
        self.assertEqual(expected_output, parsed_args.output_folder)
        self.assertEqual(expected_graph, parsed_args.graphs_folder[0])
        self.assertEqual(expected_force_mode, parsed_args.force_mode)


    #@unittest.skip
    def test_argparse_defaults(self):
        expected_input = "input_test_folder"
        expected_output = "output"
        expected_graph = "images"
        expected_force = False
        args = [expected_input]
        parsed_args = self.sunai.parse_args(args)

        self.assertEqual(expected_input, parsed_args.input_folder[0])
        self.assertEqual(expected_output, parsed_args.output_folder)
        self.assertEqual(expected_graph, parsed_args.graphs_folder[0])
        self.assertEqual(expected_force, parsed_args.force_mode)


    #@unittest.skip
    def test_read_input_files(self):
        expected = [
            "test/cases/data_plantas_python_1_1.xlsx",
            "test/cases/data_plantas_python_2.xlsx",
            "test/cases/dummy.xlsx",
            "test/cases/small_data.xlsx",
            "test/cases/subfolder/dummy.xlsx",
        ]
        self.sunai.input_folder = "test/cases"
        output = self.sunai.get_input_files()
        output.sort()
        expected.sort()

        self.assertEqual(expected, output)


