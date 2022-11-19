#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pandas as pd
import datetime
#import time


class PowerPlant():
    def __init__(self, filename: str()="default", outdir: str()=""):
        self.filename = filename
        self.output_dir = outdir

        self.datafile = None
        self.active_energy = None
        self.active_power = None
        self.dates = None

        self.graph_data = None
        self.grap_line = None


    def set_default_output_dir(self):
        #self.filename → test/cases/data_plantas_python_1_1.xlsx
        subfolder = os.path.splitext(self.filename)[0].split('/')[-1]
        outdir = "output" + '/' + subfolder + '/'
        self.output_dir = outdir
        return outdir


    def check_output_dir(self):
        """Check if the output dir exist or is setted, else set or create it."""
        if self.output_dir == "":
            self.set_default_output_dir()
        try:
            if os.path.exists(self.output_dir):
                return
            os.makedirs(self.output_dir)
        except Exception as err:
            print("ERROR: Can't read/write the output folder")
            raise err


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


    def save_graph(self, output_file):
        self.graph_line.get_figure().savefig(output_file)


    def get_active_energy_val_by_index(self, index) -> int():
        return self.active_energy.values[index][1]


    def get_date_by_index(self, index) -> str():
        date = self.datafile["fecha_im"].values[index]
        #date = self.dates.values[index]
        return pd.to_datetime(str(date)).strftime("%Y-%m-%d %H:%M:%S")


    def min_active_energy(self) -> int():
        return self.active_energy.min()[1]


    def max_active_energy(self) -> int():
        return self.active_energy.max()[1]


    def active_power_sum_by_day(self):
        return int(self.active_power["active_power_im"].sum())


    def make_summary_txt(self):
        """
        Generar txt con:
            - [x] Suma por día del active power
            - [x] Valor mínimo de active energy
            - [x] Valor máximo de active energy
            - [x] Path al archivo del gráfico
        """
        # First, set the filename so we can add it to txt_content
        self.check_output_dir()
        filename = self.output_dir + "daily_summary.txt"
        filename = os.path.abspath(filename)

        active_power_per_day = self.active_power_sum_by_day()
        min_active_energy = self.min_active_energy()
        max_active_energy = self.max_active_energy()

        txt_content = [
            "Daily Summary\n=============\n"
            "Input file:\n'{}'\n".format(self.filename),
            "Active power per day sum: {:9}".format(active_power_per_day),
            "Minimum active energy: {:12}".format(min_active_energy),
            "Maximum active energy: {:12}".format(max_active_energy),
            "\nGenerated graph full filename:\n'{}'".format(filename), 
        ]
        file_data = "\n".join(txt_content)


        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(file_data)
        except Exception as err:
            print("ERROR: Can't write the summary file")
            raise err

        return file_data


    def console_output(self):
        """
        Output consola:
            - Suma total del active power por día de todas las plantas
        """
        pass


