#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eduardo Bray (ejbray@uc.cl)

import sys
import argparse
import traceback
#import time

from src.sunai_challenge import SunaiChallenge


def main():
    #if len(sys.argv) != 2:
    #    print("Error: Check usage: ./sunai_challenge.py -h")
    #    sys.exit()
    try:
        sunai_challenge = SunaiChallenge()
        sunai_challenge.run()

        sys.exit()
    except Exception:
        print("Catched exception: \n  {}".format(traceback.format_exc()))
        print("Closing SunaiChallenge...")
        sys.exit()



if __name__ == "__main__":
    main()

