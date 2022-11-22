#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import datetime
import logging
import os


log = logging.getLogger(__name__)


class PowerPlantDay():
    def __init__(self, filename: str):
        self.filename = filename
        self.active_energy = None
        self.active_power = None
        self.plant_id = ""
        self.date = ""

        self.graph = None
        self.graph_title = ""
        self.graph_filename = None
        self.summary = None
        self.summary_filename = None


    def load_file(self):
        try:
            filedata = pd.read_excel(self.filename, parse_dates=True,
                                     na_values="data_faltante", usecols="A,B,L,M")
            # TODO: Check performance. Maybe also adding the C column to
            #       filedata is faster that two read_excel calls
            plant_id = pd.read_excel(self.filename, index_col=None, usecols="C",
                                     header=1, nrows=0)
        except Exception as err:
            log.error("Couldn't read the input file: {}".format(self.filename))
            raise err

        # Parse the data
        self.plant_id = str(plant_id.columns.values[0]).zfill(4)
        if plant_id is None or self.plant_id == "":
            log.error("Couldn't get plant_id data from '{}'".format(filename))

        self.active_energy = filedata[["active_energy_im"]]
        if self.active_energy is None:
            log.error("Couldn't get active_energy_im data from '{}'"
                      .format(filename))

        self.active_power = filedata.groupby("fecha_im")["active_power_im"].sum()
        if self.active_power is None:
            log.error("Couldn't get active_power_im data from '{}'"
                      .format(filename))

        date = str(filedata["fecha_im"].values[0])
        self.date = pd.to_datetime(date).strftime("%Y-%m-%d")
        if self.date == "":
            log.error("Couldn't get fecha_im data from '{}'".format(filename))

        # Set missing output string variables (filename only, missing dir path)
        self.summary_filename = "{}_{}_summary.txt".format(self.plant_id,
                                                           self.date)
        self.graph_filename = "{}_{}.jpg".format(self.plant_id, self.date)
        self.graph_title = "{}_planta_id-{}".format(self.date, self.plant_id)

        # Call destructor
        del filedata


    def set_output_filenames_fullpath(self, output_dir, graph_dir):
        self.graph_filename = os.path.join(graph_dir, self.graph_filename)
        self.summary_filename = os.path.join(output_dir, self.summary_filename)


    def get_active_energy_value(self, index) -> int():
        return self.active_energy.iloc[index, 0]


    def min_active_energy(self) -> int():
        return self.active_energy.min()[0]


    def max_active_energy(self) -> int():
        return self.active_energy.max()[0]


    def active_power_day_sum(self):
        return int(self.active_power.sum())


    def make_summary(self):
        if self.graph_filename is None or self.graph_filename == "":
            log.error("Variable graph_filename not set")
            raise Exception("Missing required graph_filename var in make_summary")

        active_power_per_day = self.active_power_day_sum()
        min_active_energy = self.min_active_energy()
        max_active_energy = self.max_active_energy()
        data = [
            "Daily Summary\n=============\n"
            "Input file:\n{}\n".format(self.filename),
            "Active power per day sum: {:9}".format(active_power_per_day),
            "Minimum active energy: {:12}".format(min_active_energy),
            "Maximum active energy: {:12}".format(max_active_energy),
            "\nGenerated graph full filename:\n{}".format(self.graph_filename),
            "" # trailing newline
        ]
        self.summary = "\n".join(data)
        return self.summary


    def make_graph(self):
        """
        Make a line chart:
            - X axis with date
            - Y axis with active power

        Series self.active_power:
            fecha_im
            2022-11-10 00:00:00    0.0
            2022-11-10 00:05:00    0.0
            ...
            Name: active_power_im, Length: 260, dtype: float64
        """
        #self.active_power = self.active_power.resample("30min").max()
        self.active_power.index = self.active_power.index.strftime("%H:%M")
        self.graph = self.active_power.plot(
                color = "tab:orange",
                grid = True,
                kind = "line",
                legend = False,
                title = self.graph_title,
                xlabel = "",
                ylabel = "Active power",
        )


    def save_summary_txt(self):
        # Check data and filename
        if self.summary_filename is None or self.summary_filename == "":
            log.error("Variable summary_filename not set")
            raise Exception("Missing var summary_filename in save_summary")
        if self.summary is None:
            log.error("No summary data to save")
            raise Exception("Missing summary data, try make_summary first.")

        try:
            with open(self.summary_filename, "w", encoding="utf-8") as file:
                file.write(self.summary)
        except Exception as err:
            log.error("Couldn't write the summary txt file")
            raise err


    def save_graph_image(self):
        # Check data and filename
        if self.graph_filename is None or self.graph_filename == "":
            log.error("Variable graph_filename not set")
            raise Exception("Missing var graph_filename in save_graph")
        if self.graph is None:
            log.error("No graph data to save")
            raise Exception("Missing graph data, try make_graph first.")

        try:
            self.graph.get_figure().savefig(self.graph_filename)
        except Exception as err:
            log.error("Couldn't write the graph image file.")
            raise err


