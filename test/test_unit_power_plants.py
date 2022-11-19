#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from src.power_plant import PowerPlant


#@unittest.skip
class TestPowerPlant(unittest.TestCase):
    def setUp(self):
        filename = "test/cases/data_plantas_python_1_1.xlsx"
        output_dir = "test/output"
        self.power_plant = PowerPlant(filename, output_dir)
        self.power_plant.graph_filename = "output_test_graph.jpg"


    #@unittest.skip
    def test_load_xlsx_file_dummy(self):
        expected = "   id_i   fecha_im  active_energy_im  active_power_im\n0    42 2022-11-17         123456789        987654321"
        self.power_plant.filename = "test/cases/dummy.xlsx"
        self.power_plant.load_file()
        output = str(self.power_plant.datafile)
        print(output)

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_load_xlsx_file_active_energy_data(self):
        expected_first_value = 100358904
        expected_mid_value = 100384504 # row 288 -> index 286
        expected_last_value = 112923304

        self.power_plant.filename = "test/cases/data_plantas_python_2.xlsx"
        self.power_plant.load_file()
        output_first_value = self.power_plant.get_active_energy_value(0)
        output_mid_value = self.power_plant.get_active_energy_value(286)
        output_last_value = self.power_plant.get_active_energy_value(-1)

        self.assertEqual(expected_first_value, output_first_value)
        self.assertEqual(expected_mid_value, output_mid_value)
        self.assertEqual(expected_last_value, output_last_value)


    #@unittest.skip
    def test_load_xlsx_file_date_data(self):
        expected_date_42 = "2022-11-10 00:40:00"
        expected_date_586 = "2022-11-10 09:15:00"
        expected_date_1408 = "2022-11-10 23:00:00"

        self.power_plant.load_file()
        output_date_42 = self.power_plant.get_date(40)
        output_date_586 = self.power_plant.get_date(584)
        output_date_1408 = self.power_plant.get_date(1406)

        self.assertEqual(expected_date_42, output_date_42)
        self.assertEqual(expected_date_586, output_date_586)
        self.assertEqual(expected_date_1408, output_date_1408)


    #@unittest.skip
    def test_active_power_sum_by_day(self):
        expected = 3664916
        self.power_plant.load_file()
        output = self.power_plant.active_power_sum_by_day()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_active_max_active_energy(self):
        expected = 76978296
        self.power_plant.load_file()
        output = self.power_plant.max_active_energy()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_active_min_active_energy(self):
        expected = 46870800
        self.power_plant.load_file()
        output = self.power_plant.min_active_energy()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_default_output_dir(self):
        expected = "test/output"
        outdir = "test/output"

        filename = "test/cases/dummy.xlsx"
        test_plant = PowerPlant(filename, outdir=outdir)
        self.assertEqual(expected, test_plant.output_dir)

        filename = "any_folder/dummy.xlsx"
        test_plant = PowerPlant(filename, outdir=outdir)
        self.assertEqual(expected, test_plant.output_dir)

        filename = "dummy.xlsx"
        test_plant = PowerPlant(filename=filename, outdir=outdir)
        self.assertEqual(expected, test_plant.output_dir)


    #@unittest.skip
    def test_make_summary_data(self):
        expected_1 = "3664916"
        expected_2 = "46870800"
        expected_3 = "76978296"
        filename = "test/output/output_test_graph.jpg"

        self.power_plant.load_file()
        output = self.power_plant.make_summary()

        self.assertIn(expected_1, output)
        self.assertIn(expected_2, output)
        self.assertIn(expected_3, output)
        self.assertIn(filename, output)


    #@unittest.skip
    def test_save_summary_txt(self):
        filename = "test/output/daily_summary.txt"
        self.power_plant.load_file()
        self.power_plant.make_output_dir()
        self.power_plant.make_summary()
        self.power_plant.save_summary_txt()

        self.assertTrue(os.path.exists(filename))
        # Clean created folders and file
        os.remove(filename)
        os.removedirs("test/output")


    #@unittest.skip
    def test_make_graph(self):
        expected_format = "JPEG"
        expected_size = (640, 480)

        input_datafile = "test/cases/small_data.xlsx"
        output_dir = "test/output_make_graph"
        output_filename = "output_image_file.jpg"
        power_plant = PowerPlant(input_datafile, output_dir)
        power_plant.load_file()
        power_plant.make_output_dir()
        power_plant.make_graph()
        power_plant.save_graph(output_filename)

        from PIL import Image
        from PIL.ExifTags import TAGS
        filename = os.path.abspath(power_plant.graph_filename)
        image = Image.open(filename)
        output_format = image.format
        output_size = image.size
        image.close()
        self.assertEqual(expected_format, output_format)
        self.assertEqual(expected_size, output_size)

        # Clean created folders and file
        os.remove(output_dir + "/" + output_filename)
        os.removedirs("test/output_make_graph")



