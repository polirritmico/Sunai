#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pandas as pd
import datetime
#import time


class PowerPlant():
    def __init__(self, filename="default"):
        self.filename = filename
        self.file_dataframe = None
        self.active_energy = None
        self.dates_serie = None


    def load_file(self):
        try:
            self.file_dataframe = pd.read_excel(self.filename)
        except Exception as err:
            print("ERROR: Can't read the file: ")
            raise err
        # Parse the data
        self.active_energy = pd.DataFrame(self.file_dataframe,
                                          columns=["active_energy_im"])
        self.dates = pd.DataFrame(self.file_dataframe, columns=["fecha_im"])


    def get_active_energy_val_by_index(self, index) -> list():
        return self.active_energy.iloc[index]["active_energy_im"]

        

