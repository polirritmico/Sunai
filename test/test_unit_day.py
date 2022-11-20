#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
# Needed for test_make_graph
from PIL import Image
from PIL.ExifTags import TAGS

from src.day import Day


#@unittest.skip
class TestDay(unittest.TestCase):
    def setUp(self):
        filename = "test/cases/data_plantas_python_1_1.xlsx"
        self.day = Day(filename)
        self.day.graph_filename = "test/output/output_test_graph.jpg"


    #@unittest.skip
    def test_load_xlsx_file_dummy(self):
        expected = "   id_i   fecha_im  active_energy_im  active_power_im\n" \
                   "0    42 2022-11-17         123456789        987654321"
        self.day.filename = "test/cases/dummy.xlsx"

        self.day.load_file()
        output = str(self.day.data)

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_get_plants_id(self):
        expected = "321"
        self.day.filename = "test/cases/dummy.xlsx"
        output = self.day.get_plant_id_from_file()

        self.assertEquals(expected, output)



    #@unittest.skip
    def test_load_xlsx_file_active_energy_data(self):
        expected_first_value = 100358904
        expected_mid_value = 100384504 # row 288 -> index 286
        expected_last_value = 112923304

        self.day.filename = "test/cases/data_plantas_python_2.xlsx"
        self.day.load_file()
        output_first_value = self.day.get_active_energy_value(0)
        output_mid_value = self.day.get_active_energy_value(286)
        output_last_value = self.day.get_active_energy_value(-1)

        self.assertEqual(expected_first_value, output_first_value)
        self.assertEqual(expected_mid_value, output_mid_value)
        self.assertEqual(expected_last_value, output_last_value)


    #@unittest.skip
    def test_load_xlsx_file_date_data(self):
        expected_date_42 = "2022-11-10 00:40:00"
        expected_date_586 = "2022-11-10 09:15:00"
        expected_date_1408 = "2022-11-10 23:00:00"

        self.day.load_file()
        output_date_42 = self.day.get_date(40)
        output_date_586 = self.day.get_date(584)
        output_date_1408 = self.day.get_date(1406)

        self.assertEqual(expected_date_42, output_date_42)
        self.assertEqual(expected_date_586, output_date_586)
        self.assertEqual(expected_date_1408, output_date_1408)


    #@unittest.skip
    def test_active_power_sum_by_day(self):
        expected = 3664916
        self.day.load_file()
        output = self.day.active_power_sum_by_day()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_active_max_active_energy(self):
        expected = 76978296
        self.day.load_file()
        output = self.day.max_active_energy()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_active_min_active_energy(self):
        expected = 46870800
        self.day.load_file()
        output = self.day.min_active_energy()

        self.assertEqual(expected, output)


    ##@unittest.skip
    #def test_default_output_dir(self):
    #    expected = "test/output"
    #    outdir = "test/output"

    #    filename = "test/cases/dummy.xlsx"
    #    test_plant = Day(filename)
    #    self.assertEqual(expected, test_plant.output_dir)

    #    filename = "any_folder/dummy.xlsx"
    #    test_plant = Day(filename)
    #    self.assertEqual(expected, test_plant.output_dir)

    #    filename = "dummy.xlsx"
    #    test_plant = Day(filename)
    #    self.assertEqual(expected, test_plant.output_dir)


    #@unittest.skip
    def test_make_summary_data(self):
        expected_1 = "3664916"
        expected_2 = "46870800"
        expected_3 = "76978296"
        filename = "test/output/output_test_graph.jpg"

        self.day.load_file()
        output = self.day.make_summary()

        self.assertIn(expected_1, output)
        self.assertIn(expected_2, output)
        self.assertIn(expected_3, output)
        self.assertIn(filename, output)


    #@unittest.skip
    def test_save_summary_txt(self):
        filename = "test/daily_summary.txt"
        self.day.load_file()
        self.day.make_summary()
        self.day.save_summary_txt(filename)

        self.assertTrue(os.path.exists(filename))
        # Clean created file
        os.remove(filename)


    #@unittest.skip
    def test_make_graph(self):
        expected_format = "JPEG"
        expected_size = (640, 480)

        input_datafile = "test/cases/small_data.xlsx"
        output_filename = "test/output_image_file.jpg"
        day = Day(input_datafile)
        day.load_file()
        day.make_graph("test_make_graph")
        day.save_graph(output_filename)

        filename = os.path.abspath(day.graph_filename)
        image = Image.open(filename)
        output_format = image.format
        output_size = image.size
        image.close()
        self.assertEqual(expected_format, output_format)
        self.assertEqual(expected_size, output_size)

        # Clean created folders and file
        os.remove(os.path.join(output_filename))



