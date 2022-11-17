#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.sunai import Sunai


#@unittest.skip
class TestSunai(unittest.TestCase):
    def setUp(self):
        self.sunai = Sunai()


    #@unittest.skip
    def test_load_file_data(self):
        filepath = "test/cases/data_plantas_python_2.xlsx"
        expected_first_value = 100358904
        expected_last_value = 112923304

        self.sunai.load_xlsx(filepath)
        active_energy = self.sunai.get_active_energy()

        self.assertEqual(expected_first_value, active_energy[0])
        self.assertEqual(expected_last_value, active_energy[-1])


