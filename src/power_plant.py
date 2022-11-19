#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pandas as pd
import datetime
#import time


class PowerPlant():
    def __init__(self, filename: str="default", outdir: str="output"):
        self.filename = filename
        self.output_dir = outdir

        self.datafile = None
        self.active_energy = None
        self.active_power = None
        self.dates = None

        self.graph_data = None
        self.graph_line = None
        self.graph_filename = None
        self.summary_data = None

        # Setup the output dir. Add filename without extension as subfolder
        subfolder = os.path.splitext(os.path.basename(self.filename))[0]
        self.output_dir = os.path.join(self.output_dir, subfolder)


    def load_file(self):
        try:
            datafile = pd.read_excel(self.filename, parse_dates=True).fillna(0)
        except Exception as err:
            print("ERROR: Can't read the file: ")
            raise err

        # Parse the data
        self.datafile = datafile
        self.active_energy = datafile[["id_i", "active_energy_im"]]
        self.active_power = datafile.set_index("fecha_im")[["id_i", "active_power_im"]]


    def make_output_dir(self):
        if self.output_dir == "":
            raise Exception("ERROR: No output directory assigned")
        try:
            if os.path.exists(self.output_dir):
                return
            os.makedirs(self.output_dir)
        except Exception as err:
            print("ERROR: Can't read/write the output folder")
            raise err


    def get_active_energy_value(self, index) -> int():
        return self.active_energy.values[index][1]


    def get_date(self, index) -> str():
        date = self.datafile["fecha_im"].values[index]
        #date = self.dates.values[index]
        return pd.to_datetime(str(date)).strftime("%Y-%m-%d %H:%M:%S")


    def min_active_energy(self) -> int():
        return self.active_energy.min()[1]


    def max_active_energy(self) -> int():
        return self.active_energy.max()[1]


    def active_power_sum_by_day(self):
        return int(self.active_power["active_power_im"].sum())


    def make_graph(self):
        """
        Generar gráfico line chart:
            - Eje x fecha
            - Eje y active power
            - Guardar archivo
        """
        self.graph_line = self.active_power.plot(
                kind="line",
                title="Active power by inversor",
                grid=True,
                #ylabel="Active power",
                xlabel="Timestamp",
                #x_compat=True,
                #color="tab:orange",
                #legend=False,
        )


    def save_graph(self, filename):
        self.graph_filename = filename
        try:
            self.graph_line.get_figure().savefig(filename)
        except Exception as err:
            print("ERROR: Can't save the graph to disk.")
            raise err


    def make_summary(self):
        """
        Generar txt con:
            - [x] Suma por día del active power
            - [x] Valor mínimo de active energy
            - [x] Valor máximo de active energy
            - [x] Path al archivo del gráfico
        """

        # Set the graph filename so we can add it to txt_content
        graph_filename = os.path.join(self.output_dir, self.graph_filename)
        graph_filename = os.path.abspath(graph_filename)

        active_power_per_day = self.active_power_sum_by_day()
        min_active_energy = self.min_active_energy()
        max_active_energy = self.max_active_energy()
        data = [
            "Daily Summary\n=============\n"
            "Input file:\n'{}'\n".format(self.filename),
            "Active power per day sum: {:9}".format(active_power_per_day),
            "Minimum active energy: {:12}".format(min_active_energy),
            "Maximum active energy: {:12}".format(max_active_energy),
            "\nGenerated graph full filename:\n'{}'".format(graph_filename),
            "" # trailing newline
        ]
        self.summary_data = "\n".join(data)

        return self.summary_data


    def save_summary_txt(self, filename="daily_summary.txt"):
        if self.summary_data is None:
            print("ERROR: No summary data")
            raise Exception("Missing summary data, try make_summary_txt()")

        if not filename.endswith(".txt"):
            filename += ".txt"
        filename = os.path.join(self.output_dir, filename)
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(self.summary_data)
        except Exception as err:
            print("ERROR: Can't write the summary file")
            raise err


    def console_output(self):
        """
        Output consola:
            - Suma total del active power por día de todas las plantas
        """
        pass


