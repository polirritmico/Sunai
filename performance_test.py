#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import logging

from src.sunai_challenge import SunaiChallenge

INPUT_TEST_FOLDER = "test/performance_full"
OUTPUT_TEST_FOLDER = "test/performance_output"

logging.basicConfig(
        filename="performance.log",
        level=logging.INFO,
        format="Execution date: %(asctime)s\t%(message)s"
)

if __name__ == "__main__":
    print("Simple Performance Test\n=======================")
    sunai = SunaiChallenge()
    print("Running test...", end="", flush=True)
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

    logging.info("Runtime: {:0>2}:{:05.2f}\tProcessed files: {}"
                 .format(int(min), sec, processed_files))

    # Estimate 1000 repetitions:
    t = t * (1000 / processed_files)
    h, rem = divmod(t, 3600)
    min, sec = divmod(rem, 60)
    print("Estimated time for 1000 repetitions: {:0>2}:{:0>2}:{:0>2}"
          .format(int(h), int(min), int(sec)))
    output_path = os.path.abspath(OUTPUT_TEST_FOLDER)
    print("Output folder:\n{}".format(output_path))

