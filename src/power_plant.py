#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pandas as pd
import datetime
from src.day import Day
#import time


class PowerPlant():
    def __init__(self, plant_id: str, input_dir: str, output_dir: str,
                 graph_output_dir: str):
        self.id = plant_id.zfill(4)
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.graph_output_dir = graph_output_dir

        self.days_collection = []


    def setup_output_path(self):
        if self.output_dir == "":
            raise Exception("ERROR: No output directory assigned")
            return
        if self.graph_output_dir == "":
            raise Exception("ERROR: No graphs output directory assigned")
            return
        try:
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
            if not os.path.exists(self.graph_output_dir):
                os.makedirs(self.graph_output_dir)
        except Exception as err:
            print("ERROR: Can't read/write output folder")
            raise err


    def load_days_data(self):
        for day in self.days_collection:
            day.load_file()


    def make_day_graph_filename(self, day):
        filename = "{}_{}.jpg".format(self.id, day.date)
        filename = os.path.join(self.graph_output_dir, filename)
        return filename


    def make_day_summary_filename(self, day):
        filename = "{}_{}_summary.txt".format(self.id, day.date)
        filename = os.path.join(self.output_dir, filename)
        return filename



    def console_output(self):
        """
        Output consola:
            - Suma total del active power por día de todas las plantas
        """
        pass


