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
        self.input_folder = None
        self.output_folder = None
        self.graphs_folder = None

        self.files_collection = []
        self.power_plants = []

        self.force_mode = False


    def run(self):
        # Get all variables
        args = self.parse_args()
        self.input_folder = args.input_folder[0]
        self.output_folder = args.output_folder[0]
        self.graphs_folder = args.graphs_folder[0]
        self.force_mode = args.force_mode

        self.files_collection = self.read_files()


    def parse_args(self, argv=None):
        parser = argparse.ArgumentParser(
            prog = "SunaiChallenge",
            usage = "sunai_challenge [options] <input_folder> [<output_folder>]",
            description = "Process power plant data and make info and graphs.",
            epilog = "Sunai application project " \
                     "by Eduardo Bray (ejbray@uc.cl)"
        )
        parser.add_argument(
            "input_folder",
            metavar = "input_folder",
            type = str,
            nargs = 1,
            help = "The input folder containing all the files to be processed.",
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
            default = ["images"],
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
        return parser.parse_args(argv)


    def get_input_files(self):
        """Recursively read files in the input folder."""
        files_collection = []
        for path, _, files in os.walk(self.input_folder):
            for file in files:
                files_collection.append((os.path.join(path, file)))
        return files_collection


    def make_power_plants(self):
        pass


    def make_graphs_filename(self):
        pass


    def make_summaries_filename(self):
        pass


    def print_summary(self):
        pass

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

