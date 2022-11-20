#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pandas as pd
import datetime
#import time


class PowerPlant():
    def __init__(self, plant_id: str, input_dir: str, output_dir: str="output"):
        self.id = plant_id
        self.input_dir = input_dir
        self.output_dir = output_dir

        self.days_collection = []


    def setup_output_dir(self):
        if self.output_dir == "":
            raise Warning("ERROR: No output directory assigned")
            return
        try:
            if os.path.exists(self.output_dir):
                return
            os.makedirs(self.output_dir)
        except Exception as err:
            print("ERROR: Can't read/write the output folder")
            raise err


    def console_output(self):
        """
        Output consola:
            - Suma total del active power por día de todas las plantas
        """
        pass


