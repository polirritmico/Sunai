#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from src.sunai_challenge import SunaiChallenge


#@unittest.skip
class TestSunaiChallenge(unittest.TestCase):
    def setUp(self):
        self.sunai = SunaiChallenge()
        self.sunai.input_folder = "test/cases"


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
        expected_graph = "output/images"
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
        output = self.sunai.get_input_files()
        output.sort()
        expected.sort()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_make_days_by_plant(self):
        expected = 4
        self.sunai.get_input_files()
        plant = self.sunai.make_days_by_plant()
        output = len(plant)
        self.assertEqual(expected, output)

        expected = 2
        output = len(plant["321"])
        self.assertEqual(expected, output)

        expected = 1
        print(plant)
        output = len(plant["218"])
        self.assertEqual(expected, output)


    #@unittest.skip
    def test_make_power_plants(self):
        expected = ["0031", "0032", "0218", "0321" ]
        self.sunai.get_input_files()
        days_collection = self.sunai.make_days_by_plant()
        self.sunai.make_power_plants(days_collection)
        output = self.sunai.get_power_plants_id()
        output.sort()

        self.assertEqual(expected, output)

        expected = "321"
        output = self.sunai.power_plants[2].days_collection[1].plant_id
        self.assertEqual(expected, output)




