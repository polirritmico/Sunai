#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.power_plant import PowerPlant


#@unittest.skip
class TestPowerPlant(unittest.TestCase):
    def setUp(self):
        self.power_plant = PowerPlant()


    #@unittest.skip
    def test_load_xlsx_file_data(self):
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


