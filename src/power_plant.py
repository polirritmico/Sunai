#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pandas as pd
import datetime
import matplotlib.pyplot as plt
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


    def load_days_data(self):
        for day in self.days_collection:
            day.load_file()


    def make_all_summaries(self):
        for day in self.days_collection:
            day_graph_filename = self.make_day_graph_filename(day)
            day.make_summary(day_graph_filename)
            day_summary_filename = self.make_day_summary_filename(day)
            day.save_summary_txt(day_summary_filename)


    def make_all_graphs(self):
        for day in self.days_collection:
            day_graph_filename = self.make_day_graph_filename(day)
            day.make_graph()
            day.save_graph(day_graph_filename)
            #plt.clf()
            plt.close("all")


    def make_day_graph_filename(self, day):
        filename = "{}_{}.jpg".format(self.id, day.date)
        filename = os.path.join(self.graph_output_dir, filename)
        return filename


    def make_day_summary_filename(self, day):
        filename = "{}_{}_summary.txt".format(self.id, day.date)
        filename = os.path.join(self.output_dir, filename)
        return filename


