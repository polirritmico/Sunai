#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pandas as pd
import datetime
#import time


class PowerPlant():
    def __init__(self, filename="default"):
        self.filename = filename
        self.file_data = None

        self.active_energy = None
        self.active_power = None
        self.dates = None

        self.graph_data = None
        self.grap_line = None


    def load_file(self):
        try:
            self.file_data = pd.read_excel(self.filename).fillna(0)
        except Exception as err:
            print("ERROR: Can't read the file: ")
            raise err
        # Parse the data
        self.file_data.info()
        self.active_energy = self.file_data["active_energy_im"]
        self.active_power = self.file_data["active_power_im"]
        self.dates = self.file_data["fecha_im"]


    def make_graph(self):
        """
        Generar gráfico line chart:
            - Eje x fecha
            - Eje y active power
            - Guardar archivo
        """
        self.graph_data = pd.DataFrame(self.active_power, self.dates)
        #df['date'] = pd.to_datetime(df['date'])
        #df.groupby(df['date'].dt.date)

        self.graph_line = self.graph_data.plot(
            kind="line", grid=True, ylabel="Active power", xlabel="Fecha"
        )


    def save_graph(self, output_file):
        self.graph_line.get_figure().savefig(output_file)


    def get_active_energy_val_by_index(self, index) -> int():
        return self.active_energy.values[index]


    def get_date_by_index(self, index) -> str():
        date = self.dates.values[index]
        return pd.to_datetime(str(date)).strftime("%Y-%m-%d %H:%M:%S")
        

# =============================================================================


    def get_active_power_sum(self):
        """
        Generar txt con:
            - Suma por día del active power
            - Valor mínimo de active energy
            - Valor máximo de active energy
            - Path al archivo del gráfico
        """
        pass


    def dummy(self):
        """
        Output consola:
            - Suma total del active power por día de todas las plantas
        """
        pass


