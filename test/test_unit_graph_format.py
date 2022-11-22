#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from src.day import Day
import matplotlib.pyplot as plt


#@unittest.skip
class TestDayGraphFormat(unittest.TestCase):
    def setUp(self):
        filename = "test/cases/data_plantas_python_1_1.xlsx"
        self.day = Day(filename)
        self.day.graph_filename = "test/output_day_graph_format.jpg"
        self.day.plant_id = "0221"
        plt.clf()
        plt.close("all")


    def test_make_graph(self):
        output_filename = "test/output_day_graph_format.jpg"
        try:
            os.remove(os.path.join(output_filename))
        except:
            pass

        self.day.load_file()
        self.day.make_graph()
        self.day.save_graph(output_filename)

        filename = os.path.abspath(output_filename)
        self.assertTrue(os.path.isfile(filename))

        # Clean created folders and file
        #os.remove(os.path.join(output_filename))

