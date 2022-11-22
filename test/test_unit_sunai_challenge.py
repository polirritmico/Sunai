#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from src.sunai_challenge import SunaiChallenge


#@unittest.skip
class TestSunaiChallenge(unittest.TestCase):
    def setUp(self):
        self.sunai = SunaiChallenge()
        self.sunai.input_path = "test/cases"


    #@unittest.skip
    def test_argparse(self):
        expected_input = "input_test_folder"
        expected_output = "output_TEST"
        expected_graph = "alternative_folder"
        expected_parallel_mode = True
        args = ["-p", "-g", expected_graph, expected_input, expected_output]
        parsed_args = self.sunai.parse_args(args)

        self.assertEqual(expected_input, parsed_args.input_path[0])
        self.assertEqual(expected_output, parsed_args.output_folder)
        self.assertEqual(expected_graph, parsed_args.graphs_folder[0])
        self.assertEqual(expected_parallel_mode, parsed_args.parallel_mode)


    #@unittest.skip
    def test_argparse_defaults(self):
        expected_input = "input_test_folder"
        expected_output = "output"
        expected_graph = "output/images"
        expected_force = False
        expected_parallel = False
        args = [expected_input]
        parsed_args = self.sunai.parse_args(args)

        self.assertEqual(expected_input, parsed_args.input_path[0])
        self.assertEqual(expected_output, parsed_args.output_folder)
        self.assertEqual(expected_graph, parsed_args.graphs_folder[0])
        self.assertEqual(expected_force, parsed_args.parallel_mode)


    #@unittest.skip
    def test_read_input_files(self):
        expected = [
            "test/cases/data_plantas_python_1_1.xlsx",
            "test/cases/data_plantas_python_2.xlsx",
            "test/cases/dummy.xlsx",
            "test/cases/small_data.xlsx",
            "test/cases/subfolder/dummy.xlsx",
        ]
        output = self.sunai.get_input_files()
        output.sort()
        expected.sort()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_processed_files_count(self):
        expected = 5
        output = len(self.sunai.get_input_files())

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_setup_output_paths(self):
        output_dir = "test/output_sunai"
        graph_output_dir = "test/output_sunai/graphs_folder"
        self.assertFalse(os.path.exists(graph_output_dir))
        self.assertFalse(os.path.exists(output_dir))

        self.sunai.output_folder = output_dir
        self.sunai.graphs_folder = graph_output_dir
        self.sunai.setup_output_paths()

        self.assertTrue(os.path.exists(output_dir))
        self.assertTrue(os.path.exists(graph_output_dir))

        # Remove test folders
        os.removedirs(graph_output_dir)


    @unittest.skip
    def test_run(self):
        expected_input = "test/cases"
        expected_output = "test/output/sunai_run"
        expected_graph = "test/output/sunai_run/images"
        expected_parallel_mode = True
        args = ["-p", expected_input, expected_output]
        self.sunai.run(args)


    @unittest.skip
    def test_make_full_summary(self):
        expected = """Full Summary
============
Daily Active Power by Power Plant:
plant_id    active_power_im
0000            123456
0000            123123
0000            123123
0000            123123
0000            123123
0000            123123
----------------------
total:       123123123"""

        self.sunai.get_input_files()
        self.sunai.process_all_days()
        #self.sunai.sort_days_by_plant()
        output = self.sunai.make_full_summary()

        self.assertEqual(expected, output)


