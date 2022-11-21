#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit

test_code = """
from src.sunai_challenge import SunaiChallenge

sunai = SunaiChallenge()
sunai.run(["test/performance_full", "test/performance_output"])
"""

if __name__ == "__main__":
    t = timeit.timeit(test_code, number=1)
    print("Repetitions: 1\nRuntime: {0:.2f} s".format(t))
