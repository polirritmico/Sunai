#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
# Needed for test_make_graph
from PIL import Image
from PIL.ExifTags import TAGS

from src.power_plant_day import PowerPlantDay


@unittest.skip
class TestPowerPlantDay(unittest.TestCase):
    def setUp(self):
        filename = "test/cases/data_plantas_python_1_1.xlsx"
        self.day = PowerPlantDay(filename)
        self.day.graph_filename = "test/output/plantid_date.jpg"
        self.day.graph_title = "test_day_title"
        self.day.summary_data_filename = "test/output/plantid_date_summary.txt"
        self.day.plant_id = "0218"


    #@unittest.skip
    def test_get_plant_id_from_file(self):
        expected = "0321"
        self.day.filename = "test/cases/dummy.xlsx"
        self.day.load_file()
        output = self.day.plant_id

        self.assertEqual(expected, output)


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
    def test_load_xlsx_get_active_max_active_energy(self):
        expected = 76978296
        self.day.load_file()
        output = self.day.max_active_energy()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_load_xlsx_get_active_min_active_energy(self):
        expected = 46870800
        self.day.load_file()
        output = self.day.min_active_energy()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_active_power_day_sum(self):
        expected = 3664916
        self.day.load_file()
        output = self.day.active_power_day_sum()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_load_xlsx_file_date_data(self):
        expected_date_42 = "2022-11-10"
        expected_date_586 = "2022-11-10"
        expected_date_1408 = "2022-11-10"

        self.day.load_file()
        output_date_42 = self.day.date
        output_date_586 = self.day.date
        output_date_1408 = self.day.date

        self.assertEqual(expected_date_42, output_date_42)
        self.assertEqual(expected_date_586, output_date_586)
        self.assertEqual(expected_date_1408, output_date_1408)


    #@unittest.skip
    def test_load_xlsx_file_dummy(self):
        expected_active_power_im = "fecha_im\n2022-11-17    987654321\nName: active_power_im, dtype: int64"
        expected_active_energy_im = "   active_energy_im\n0         123456789"
        expected_date = "2022-11-17"
        self.day.filename = "test/cases/dummy.xlsx"

        self.day.load_file()
        self.assertEqual(expected_active_power_im, str(self.day.active_power))
        self.assertEqual(expected_active_energy_im, str(self.day.active_energy))
        self.assertEqual(expected_date, self.day.date)


    #@unittest.skip
    def test_make_graph_title(self):
        expected = "2022-11-17_planta_id-0321"
        filename = "test/cases/dummy.xlsx"
        self.day.plant_id = "0321"
        self.day.filename = filename
        self.day.load_file()
        output = self.day.graph_title

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_graph_and_summary_filename(self):
        expected_graph_name = "0321_2022-11-18.jpg"
        expected_summary_name = "0321_2022-11-18_summary.txt"

        filename = "test/cases/subfolder/dummy.xlsx"
        output_dir = "test/output"
        graph_output = "test/output/images"
        self.day = PowerPlantDay(filename)
        self.day.load_file()

        output_graph_name = self.day.graph_filename
        output_summary_name = self.day.summary_filename
        self.assertEqual(expected_graph_name, output_graph_name)
        self.assertEqual(expected_summary_name, output_summary_name)



    #@unittest.skip
    def test_set_output_filenames_fullpath(self):
        expected_graph_name = "test/output/images/0321_2022-11-18.jpg"
        expected_summary_name = "test/output/0321_2022-11-18_summary.txt"
        filename = "test/cases/subfolder/dummy.xlsx"
        output_dir = "test/output"
        graph_output = "test/output/images"

        self.day = PowerPlantDay(filename)
        self.day.load_file()
        self.day.set_output_filenames_fullpath(output_dir, graph_output)
        output_graph_name = self.day.graph_filename
        output_summary_name = self.day.summary_filename

        self.assertEqual(expected_graph_name, output_graph_name)
        self.assertEqual(expected_summary_name, output_summary_name)


    #@unittest.skip
    def test_make_summary_data(self):
        expected_1 = "3664916"
        expected_2 = "46870800"
        expected_3 = "76978296"
        graph_filename = "test/cases/output_test_make_summary_data_graph.jpg"

        self.day.load_file()
        self.day.graph_filename = graph_filename
        output = self.day.make_summary()

        self.assertIn(expected_1, output)
        self.assertIn(expected_2, output)
        self.assertIn(expected_3, output)
        self.assertIn(graph_filename, output)


    #@unittest.skip
    def test_make_graph_and_save_graph(self):
        expected_format = "JPEG"
        expected_size = (640, 480)

        input_datafile = "test/cases/small_data.xlsx"
        output_filename = "test/output_image_file.jpg"
        self.day = PowerPlantDay(input_datafile)
        self.day.load_file()
        self.day.plant_id = "0032"
        self.day.graph_filename = output_filename
        self.day.make_graph()
        self.day.save_graph_image()

        filename = os.path.abspath(output_filename)
        image = Image.open(filename)
        output_format = image.format
        output_size = image.size
        image.close()
        self.assertEqual(expected_format, output_format)
        self.assertEqual(expected_size, output_size)

        # Clean created folders and file
        os.remove(os.path.join(output_filename))


    #@unittest.skip
    def test_save_summary_txt(self):
        filename = "test/daily_summary.txt"
        self.day.load_file()
        self.day.summary_filename = filename

        self.day.make_summary()
        self.day.save_summary_txt()

        self.assertTrue(os.path.exists(filename))
        # Clean created file
        os.remove(filename)


