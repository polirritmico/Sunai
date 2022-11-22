#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    SunaiChallenge
    A pandas wrapper to read xlsx and generate summary data and linear plots.
"""

__author__ = "Eduardo Bray"
__version__ = "0.1"
__email__ = "ejbray@uc.cl"
__date__ = "2022-11-22"
__status__ = "Prototype"


import os
import argparse
import logging
import concurrent.futures

from src.power_plant_day import PowerPlantDay


log = logging.getLogger(__name__)


class SunaiChallenge():
    def __init__(self):
        self.input_path = None
        self.output_folder = None
        self.graphs_folder = None
        self.parallel_mode = False

        self.input_files = []
        self.days_collection = []
        self.power_plants = {}


    def run(self, argv=None):
        # Get all variables
        args = self.parse_args(argv)
        self.input_path = args.input_path[0]
        self.output_folder = args.output_folder
        self.graphs_folder = args.graphs_folder[0]
        self.parallel_mode = args.parallel_mode

        # Get input files and setup output folders and days objects
        self.input_files = self.get_input_files()
        self.setup_output_paths()
        for file in self.input_files:
            day = PowerPlantDay(file)
            self.days_collection.append(day)

        # Read the datafiles, process the data and write files
        for day in self.days_collection:
            day.load_file()
            day.set_output_filenames_fullpath(self.output_folder,
                                              self.graphs_folder)
            day.make_summary()
            day.make_graph()

            day.save_summary_txt()
            day.save_graph_image()



    #def parallel_process_mode(self):
    #    with concurrent.futures.ThreadPoolExecutor() as executor:
    #        processed_days = executor.map(self.load_day_data,
    #                                      self.days_collection)
    #    for day in processed_days:
    #        plant_id = day.plant_id
    #        if plant_id not int self.power_plants:
    #            pass


    def load_day_data(self, day):
        day.load_file()
        #day.set_output_filenames_fullpath(self.output_folder, self.graph_dir)
        return day


    def single_process_mode(self):
        pass


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
            "-p", "--parallel",
            dest = "parallel_mode",
            action = argparse.BooleanOptionalAction,
            default = False,
            help = "Use multiprocess and multithreads Python capabilities."
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
        """Open single file or recursively get xlsx files in the input folder."""
        # Check pased input path
        if self.input_path.endswith(".xlsx"):
            self.input_files = [self.input_path]
            return self.input_files
        if not os.path.isdir(self.input_path):
            log.critical("Not valid input path: {}".format(self.input_path))
            raise Exception("Input it's not a xlsx file nor a directory")

        # Get the xlsx files
        files_collection = []
        for path, _, files in os.walk(self.input_path):
            for file in files:
                # Check file extension
                if os.path.splitext(file)[-1] != ".xlsx":
                    continue
                files_collection.append(os.path.join(path, file))
        if len(files_collection) == 0:
            log.critical("Not found xlsx files in input path: {}"
                         .format(self.input_path))
            raise Exception("No input files detected in <input_path>")

        return files_collection


    def processed_files_count(self):
        return len(self.input_files)


    def setup_output_paths(self):
        """Creates the output directories if they don't exists"""
        # Validates inputs
        if self.output_folder == "":
            log.critical("Missing output path")
            raise Exception("No output directory assigned")
        if self.graphs_folder == "":
            log.critical("Missing graph output path")
            raise Exception("No output directory assigned")

        try:
            if not os.path.exists(self.output_folder):
                os.makedirs(self.output_folder)
            if not os.path.exists(self.graphs_folder):
                os.makedirs(self.graphs_folder)
        except Exception as err:
            log.critical("Couldn't read/write output folder")
            raise err



    #def print_full_summary(self):
    #    """Show total sum of active power by day of all plants"""
    #    pass


