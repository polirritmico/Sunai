#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os


from PIL import Image
from PIL.ExifTags import TAGS

from src.power_plant import PowerPlant
from src.day import Day


#@unittest.skip
class TestDayGraphFormat(unittest.TestCase):
    def setUp(self):
        filename = "test/cases/data_plantas_python_1_1.xlsx"
        self.day = Day(filename)
        self.day.graph_filename = "test/make_graph.jpg"
        self.day.plant_id = "0221"


    def test_make_graph(self):
        expected_format = "JPEG"
        expected_size = (640, 480)

        output_filename = "test/output_day_graph_format.jpg"
        try:
            os.remove(os.path.join(output_filename))
        except:
            pass

        self.day.load_file()
        self.day.make_graph()
        self.day.save_graph(output_filename)

        filename = os.path.abspath(output_filename)
        image = Image.open(filename)
        output_format = image.format
        output_size = image.size
        image.close()
        self.assertEqual(expected_format, output_format)
        self.assertEqual(expected_size, output_size)

        # Clean created folders and file
        #os.remove(os.path.join(output_filename))

