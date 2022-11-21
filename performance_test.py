#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from src.sunai_challenge import SunaiChallenge

if __name__ == "__main__":
    print("Simple Performance Test\n=======================\n")
    sunai = SunaiChallenge()
    print("Starting test...", end="")
    start = time.time()
    sunai.run(["test/performance_pretest", "test/performance_output"])
    end = time.time()
    print(" Done")

    t = end - start
    h, rem = divmod(t, 3600)
    min, sec = divmod(rem, 60)
    processed_files = sunai.processed_files_count()
    print("Processed input files: {}".format(processed_files))
    print("Runtime: {:0>2}:{:05.2f}".format(int(min), sec))
    t = int(t * (1000 / processed_files))
    h, rem = divmod(t, 3600)
    min, sec = divmod(rem, 60)
    print("Estimated time for 1000 repetitions: {:0>2}:{:0>2}:{:0>2}"
          .format(int(h), int(min), int(sec)))
