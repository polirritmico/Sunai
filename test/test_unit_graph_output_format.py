#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from src.power_plant_day import PowerPlantDay
import matplotlib.pyplot as plt


@unittest.skip
class TestDayGraphFormat(unittest.TestCase):
    def setUp(self):
        filename = "test/cases/data_plantas_python_1_1.xlsx"
        self.day = PowerPlantDay(filename)

        # To avoid distorting output graphs from other tests:
        plt.clf()
        plt.close("all")


    def test_make_graph_output_format_helper(self):
        output_filename = "test/output_day_graph_format.jpg"
        try:
            os.remove(os.path.join(output_filename))
        except:
            pass

        self.day.load_file()
        self.day.graph_filename = output_filename
        self.day.plant_id = "0221"
        self.day.make_graph()
        self.day.save_graph_image()

        filename = os.path.abspath(output_filename)
        self.assertTrue(os.path.isfile(filename))

        # Clean created folders or file
        #os.remove(os.path.join(output_filename))


