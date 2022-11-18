#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eduardo Bray (ejbray@uc.cl)

import sys
import argparse
import traceback
import time

from src.power_plant import PowerPlant


def main():
    print("Begin")
    time_begin = time.time()

    # power_plant = PowerPlant("test/cases/small_data.xlsx")
    power_plant = PowerPlant("test/cases/data_plantas_python_1_1.xlsx")
    power_plant.load_file()
    power_plant.make_graph()
    power_plant.save_graph("test/cases/output_image_file.jpg")

    time_end = time.time()
    print("Done in {:0.2f}s".format(time_end - time_begin))


if __name__ == "__main__":
    main()

