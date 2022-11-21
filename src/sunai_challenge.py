#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    SunaiChallenge
    A pandas wrapper to read xlsx and generate summary data
    and linear plots.
"""

__author__ = "Eduardo Bray"
__version__ = "0.1"
__email__ = "ejbray@uc.cl"
__date__ = "2022-11-21"
__status__ = "Prototype"


import os
import argparse

from src.power_plant import PowerPlant
from src.day import Day


class SunaiChallenge():
    def __init__(self):
        self.input_path = None
        self.output_folder = None
        self.graphs_folder = None

        self.input_files = []
        self.power_plants = []

        self.force_mode = False


    def run(self, argv=None):
        # Get all variables
        args = self.parse_args(argv)
        self.input_path = args.input_path[0]
        self.output_folder = args.output_folder
        self.graphs_folder = args.graphs_folder[0]
        self.force_mode = args.force_mode

        self.get_input_files()
        self.setup_output_paths()
        days_collection = self.make_days_by_plant()
        plants_colection = self.make_power_plants(days_collection)

        for plant in plants_colection:
            plant.load_days_data()
            plant.make_all_summaries()
            plant.make_all_graphs()
            del plant



    def parse_args(self, argv=None):
        parser = argparse.ArgumentParser(
            prog = "SunaiChallenge",
            usage = "sunai_challenge [options] <input_folder> [<output_folder>]",
            description = "Process power plant data and make info and graphs.",
            epilog = "Sunai application project " \
                     "by Eduardo Bray (ejbray@uc.cl)"
        )
        parser.add_argument(
            "input_path",
            metavar = "input_path",
            type = str,
            nargs = 1,
            help = "The input file or folder containing all the files to be " \
                   "processed.",
        )
        parser.add_argument(
            "output_folder",
            metavar = "output_folder",
            default = "output",
            type = str,
            nargs = "?",
            help = "The output folder. Will contain a summary txt for each " \
                    "day and a images subfolder with all the graphs. " \
                    "(Default: output)",
        )
        parser.add_argument(
            "-g", "--graphs-output",
            metavar = "<folder>",
            dest = "graphs_folder",
            default = [""],
            type = str,
            nargs = 1,
            required = False,
            help = "Set the output folder for the generated graph images. " \
                   "(Default: <output_folder>/images)",
        )
        parser.add_argument(
            "-F", "--FORCE",
            dest = "force_mode",
            action = argparse.BooleanOptionalAction,
            default = False,
            help = "Remove previous files and folders in <output_folder>. " \
                   "Use with caution.",
        )
        parser.add_argument(
            "-v", "--version",
            action = "version",
            version="%(prog)s v" + __version__,
        )
        parser = parser.parse_args(argv)
        if parser.graphs_folder[0] == "":
            parser.graphs_folder[0] = os.path.join(parser.output_folder, "images")
        return parser


    def get_input_files(self):
        """Recursively get xlsx files in the input folder."""
        files_collection = []
        for path, _, files in os.walk(self.input_path):
            for file in files:
                # Check file extension
                if os.path.splitext(file)[-1] != ".xlsx":
                    continue
                files_collection.append((os.path.join(path, file)))
        self.input_files = files_collection
        return self.input_files


    def make_days_by_plant(self):
        days_collection = {}
        for file in self.input_files:
            day = Day(file)
            plant_id = day.get_plant_id_from_file()
            if plant_id not in days_collection:
                days_collection[plant_id] = []
            days_collection[plant_id].append(day)
        return days_collection


    def make_power_plants(self, days):
        plants = []
        for plant_id in days.keys():
            plant = PowerPlant(plant_id, self.input_path, self.output_folder,
                               self.graphs_folder)
            plant.days_collection = days[plant_id]
            plants.append(plant)
        self.power_plants = plants
        return plants


    def get_power_plants_id(self):
        plants_id = []
        for plant in self.power_plants:
             plants_id.append(plant.id)
        return plants_id


    def setup_output_paths(self):
        if self.output_folder == "":
            raise Exception("ERROR: No output directory assigned")
            return
        if self.graphs_folder == "":
            raise Exception("ERROR: No graphs output directory assigned")
            return
        try:
            if not os.path.exists(self.output_folder):
                os.makedirs(self.output_folder)
            if not os.path.exists(self.graphs_folder):
                os.makedirs(self.graphs_folder)
        except Exception as err:
            print("ERROR: Can't read/write output folder")
            raise err


    def processed_files_count(self):
        return len(self.input_files)


    def print_summary(self):
        """
        Output consola:
            - Suma total del active power por día de todas las plantas
        """
        pass

