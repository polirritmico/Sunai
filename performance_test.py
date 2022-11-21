#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os

from src.sunai_challenge import SunaiChallenge

INPUT_TEST_FOLDER = "test/performance_full"
OUTPUT_TEST_FOLDER = "test/performance_output"

if __name__ == "__main__":
    print("Simple Performance Test\n=======================")
    sunai = SunaiChallenge()
    print("Starting test...", end="", flush=True)
    start = time.time()
    sunai.run([INPUT_TEST_FOLDER, OUTPUT_TEST_FOLDER])
    end = time.time()
    print(" Done")

    t = end - start
    h, rem = divmod(t, 3600)
    min, sec = divmod(rem, 60)
    processed_files = sunai.processed_files_count()
    print("Processed input files: {}".format(processed_files))
    print("Runtime: {:0>2}:{:05.2f}".format(int(min), sec))
    t = t * (1000 / processed_files)
    h, rem = divmod(t, 3600)
    min, sec = divmod(rem, 60)
    print("Estimated time for 1000 repetitions: {:0>2}:{:0>2}:{:0>2}"
          .format(int(h), int(min), int(sec)))
    output_path = os.path.abspath(OUTPUT_TEST_FOLDER)
    print("Output folder:\n{}".format(output_path))

