#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from src.power_plant import PowerPlant
from src.day import Day


#@unittest.skip
class TestPowerPlant(unittest.TestCase):
    def setUp(self):
        filename_1 = "test/cases/dummy.xlsx"
        filename_2 = "test/cases/subfolder/dummy.xlsx"
        input_dir = "test/cases"
        output_dir = "test/output"
        plant_id = "321"
        graph_output_dir = "test/output/images"
        self.power_plant = PowerPlant(plant_id, input_dir, output_dir,
                                      graph_output_dir)
        self.day1 = Day(filename_1)
        self.day2 = Day(filename_2)
        self.day1.get_plant_id_from_file()
        self.day2.get_plant_id_from_file()
        self.power_plant.days_collection.append(self.day1)
        self.power_plant.days_collection.append(self.day2)


    #@unittest.skip
    def test_setup_output_path(self):
        self.assertFalse(os.path.exists(self.power_plant.graph_output_dir))
        self.assertFalse(os.path.exists(self.power_plant.output_dir))

        self.power_plant.setup_output_path()

        self.assertTrue(os.path.exists(self.power_plant.output_dir))
        self.assertTrue(os.path.exists(self.power_plant.graph_output_dir))

        # Remove test folders
        os.removedirs(self.power_plant.graph_output_dir)


    #@unittest.skip
    def test_load_days_data(self):
        expected = "321"
        input_dir = "test/cases/subfolder"
        output_dir = "test/output"
        graph_output_dir = "test/output/images"

        power_plant = PowerPlant("321", input_dir, output_dir, graph_output_dir)
        power_plant.days_collection.append(self.day1)
        power_plant.days_collection.append(self.day2)
        power_plant.load_days_data()

        output = power_plant.days_collection[0].plant_id
        self.assertEqual(expected, output)


    #@unittest.skip
    def test_set_day_output_filenames(self):
        expected_summary_file = "test/cases/output/0321_2022-11-17_summary.txt"
        expected_graph_file = "test/cases/output/images/0031-21-11-17.jpg"

        self.power_plant.setup_days_outputs_filenames()
        output_graph = self.power_plant.days_collection[1].graph_filename
        output_summary = self.power_plant.days_collection[1].summary_data_filename

        self.assertEqual(expected_summary_file, output_summary)
        self.assertEqual(expected_graph_file, output_graph)


