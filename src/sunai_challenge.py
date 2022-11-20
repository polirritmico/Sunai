#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import argparse

from src.power_plant import PowerPlant
from src.day import Day


class SunaiChallenge():
    def __init__(self):
        self.input_folder = None
        self.output_folder = None
        self.graphs_folder = None

        self.files_collection = []
        self.power_plants = []


    def run(self):
        args = self.parse_args()

    def parse_args(self, argv=None):
        parser = argparse.ArgumentParser(
            prog = "SunaiChallenge",
            description = "Process power plant data and make info and graphs.",
            epilog = "My Sunai application project"
        )
        parser.add_argument(
            "input_folder",
            metavar="<input_folder>",
            type=str,
            nargs=1,
            help="The input folder containing all the files to be processed.",
        )
        parser.add_argument(
            "output_folder",
            metavar="<output_folder>",
            type=str,
            nargs=1,
            help="The output folder. Will contain a summary txt for every\n" \
                 "day and a images subfolder with all the graphs.",
        )
        return parser.parse_args(argv)


    def read_files(self):
        pass


    def make_power_plants(self):
        pass


    def make_graphs_filename(self):
        pass


    def make_summaries_filename(self):
        pass


    def print_summary(self):
        pass

