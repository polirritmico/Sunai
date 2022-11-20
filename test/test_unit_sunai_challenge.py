#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from src.sunai_challenge import SunaiChallenge


#@unittest.skip
class TestSunaiChallenge(unittest.TestCase):
    def setUp(self):
        pass


    #@unittest.skip
    def test_read_files(self):
        expected = ["data_plantas_python_1_1.xlsx",
                "data_plantas_python_2.xlsx",
                "dummy.xlsx",
                "small_data.xlsx"]

        sunai = SunaiChallenge()
        output = sunai.files_collection

        self.assertEqual(expected, output)


