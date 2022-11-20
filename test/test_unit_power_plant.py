#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from src.power_plant import PowerPlant
from src.day import Day


#@unittest.skip
class TestPowerPlant(unittest.TestCase):
    def setUp(self):
        filename = "test/cases/data_plantas_python_2.xlsx"
        output_dir = "test/output"
        plant_id = "31"
        graph_output_dir = "test/output/images"
        self.power_plant = PowerPlant(plant_id, filename, output_dir,
                                      graph_output_dir)
        day = Day(filename)
        self.power_plant.days_collection.append(day)


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
    def test_set_day_output_filenames(self):
        expected_summary_file = "test/cases/output/0031_2022-11-10_summary.txt"
        expected_graph_file = "test/cases/output/images/0031-21-11-10.jpg"


