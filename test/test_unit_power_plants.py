#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.power_plant import PowerPlant


#@unittest.skip
class TestPowerPlant(unittest.TestCase):
    def setUp(self):
        self.power_plant = PowerPlant()


    def test_load_xlsx_file_dummy(self):
        expected = "    fecha_im  active_energy_im\n0 2022-11-17         123456789"
        self.power_plant.filename = "test/cases/dummy.xlsx"
        self.power_plant.load_file()
        output = str(self.power_plant.dataframe)
        print(output)

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_load_xlsx_file_active_energy_data(self):
        self.power_plant.filename = "test/cases/data_plantas_python_2.xlsx"
        expected_first_value = 100358904
        expected_mid_value = 100384504 # row 288 -> index 286
        expected_last_value = 112923304

        self.power_plant.load_file()
        output_first_value = self.power_plant.get_active_energy_val_by_index(0)
        output_mid_value = self.power_plant.get_active_energy_val_by_index(286)
        output_last_value = self.power_plant.get_active_energy_val_by_index(-1)

        self.assertEqual(expected_first_value, output_first_value)
        self.assertEqual(expected_mid_value, output_mid_value)
        self.assertEqual(expected_last_value, output_last_value)


    #@unittest.skip
    def test_load_xlsx_file_date_data(self):
        self.power_plant.filename = "test/cases/data_plantas_python_1_1.xlsx"
        expected_date_42 = "2022-11-10 00:40:00"
        expected_date_586 = "2022-11-10 09:15:00"
        expected_date_1408 = "2022-11-10 23:00:00"

        self.power_plant.load_file()
        output_date_42 = self.power_plant.get_date_by_index(40)
        output_date_586 = self.power_plant.get_date_by_index(584)
        output_date_1408 = self.power_plant.get_date_by_index(1406)

        self.assertEqual(expected_date_42, output_date_42)
        self.assertEqual(expected_date_586, output_date_586)
        self.assertEqual(expected_date_1408, output_date_1408)


    @unittest.skip
    def test_make_graph(self):
        #self.power_plant.filename = "test/cases/dummy.xlsx"
        self.power_plant.filename = "test/cases/small_data.xlsx"
        output_filename = "test/cases/output_image_file.jpg"
        self.power_plant.load_file()

        self.power_plant.make_graph(output_filename)

        # from PIL import Image
        # from PIL.ExifTags import TAGS
        # image = Image.open(output_filename)

        # # extracting the exif metadata
        # exifdata = image.getexif()
        # for tagid in exifdata:
        #     tagname = TAGS.get(tagid, tagid)
        #     value = exifdata.get(tagid)
        #     # printing the final result
        #     print(f"{tagname:25}: {value}")
        # assertEqual(False, True)




