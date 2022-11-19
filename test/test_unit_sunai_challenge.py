#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from src.power_plant import PowerPlant


#@unittest.skip
class TestPowerPlant(unittest.TestCase):
    def setUp(self):
        pass


    #@unittest.skip
    def test_read_files(self):
        expected = ["data_plantas_python_1_1.xlsx",
                "data_plantas_python_2.xlsx",
                "dummy.xlsx",
                "small_data.xlsx"]

        power_plant = PowerPlant()
        output = power_plant.files_collection

        self.assertEqual(expected, output)


