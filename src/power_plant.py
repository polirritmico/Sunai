#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pandas as pd
import datetime
#import time


class PowerPlant():
    def __init__(self, filename="default", outdir=""):
        self.filename = filename
        self.grap_filename = None
        self.output_dir = self.default_output_dir() if outdir == "" else outdir

        self.datafile = None
        self.active_energy = None
        self.active_power = None
        self.dates = None

        self.graph_data = None
        self.grap_line = None


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
        print("HERE")
        date = self.datafile["fecha_im"].values[index]
        print(date)
        #date = self.dates.values[index]
        return pd.to_datetime(str(date)).strftime("%Y-%m-%d %H:%M:%S")


    def min_active_energy(self) -> int():
        return self.active_energy.min()[1]


    def max_active_energy(self) -> int():
        return self.active_energy.max()[1]


    def active_power_sum_by_day(self):
        return int(self.active_power["active_power_im"].sum())


    def default_output_dir(self):
        #self.filename → test/cases/data_plantas_python_1_1.xlsx
        subfolder = os.path.splitext(self.filename)[0].split('/')[-1]
        outdir = "output" + '/' + subfolder + '/'
        return outdir


    def check_output_dir(self):
        """Create the output directory if it doesn't exist"""
        try:
            os.makedirs(os.path.dirname(self.get_outpath()), exist_ok=True)
        except Exception as err:
            print("ERROR: Can't read/write the output folder")



    def make_summary_txt(self):
        """
        Generar txt con:
            - [x] Suma por día del active power
            - [x] Valor mínimo de active energy
            - [x] Valor máximo de active energy
            - [x] Path al archivo del gráfico
        """
        txt_content = [
            str(self.active_power_sum_by_day()),
            str(self.min_active_energy()),
            str(self.max_active_energy()),
            #self.filename, 
        ]
        file_data = "\n".join(txt_content)

        self.check_output_dir()
        filename = self.output_dir + "daily_summary.txt"
        try:
            with open(filename, encoding="utf-8") as file:
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


