#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import datetime


class Day():
    def __init__(self, filename: str):
        self.filename = filename
        self.data = None

        self.plant_id = ""
        self.active_energy = None
        self.active_power = None
        #self.dates = None

        self.date = ""
        self.graph = None
        self.graph_title = ""
        self.summary_data = None


    def load_file(self):
        try:
            datafile = pd.read_excel(self.filename, parse_dates=True,
                                     usecols="A,B,L,M").fillna(0)
        except Exception as err:
            print("ERROR: Can't read the file: ")
            raise err

        # Parse the data
        self.data = datafile
        self.active_energy = datafile[["id_i", "active_energy_im"]]
        self.active_power = datafile.set_index("fecha_im")[["id_i", "active_power_im"]]
        self.date = self.get_date(0)
        self.graph_title = "{}_planta_{}".format(self.date, self.plant_id)


    def get_plant_id_from_file(self):
        plant_id = pd.read_excel(self.filename, index_col=None, usecols = "C",
                                 header = 1, nrows=0)
        self.plant_id = str(plant_id.columns.values[0])
        if self.plant_id is None or self.plant_id == "":
            print("ERROR: Can't get plant_id")
            raise Exception("Missing plant_id data")
        return self.plant_id


    def get_active_energy_value(self, index) -> int():
        return self.active_energy.values[index][1]


    def get_date(self, index) -> str():
        date = self.data["fecha_im"].values[index]
        #date = self.dates.values[index]
        return pd.to_datetime(str(date)).strftime("%Y-%m-%d")


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
        self.graph = self.active_power.plot(
                kind = "line",
                title = self.graph_title,
                grid = True,
                #ylabel = "Active power",
                xlabel = "Timestamp",
                #x_compat = True,
                #color = "tab:orange",
                #legend = False,
        )


    def save_graph(self, filename):
        try:
            self.graph.get_figure().savefig(filename)
        except Exception as err:
            print("ERROR: Can't save the graph to disk.")
            raise err


    def make_summary(self, graph_filename):
        """
        Generar txt con:
            - Suma por día del active power
            - Valor mínimo de active energy
            - Valor máximo de active energy
            - Path al archivo del gráfico
        """
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


    def save_summary_txt(self, filename):
        if self.summary_data is None:
            print("ERROR: No summary data")
            raise Exception("Missing summary data, try make_summary_txt()")

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(self.summary_data)
        except Exception as err:
            print("ERROR: Can't write the summary file")
            raise err


