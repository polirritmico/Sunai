#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eduardo Bray (ejbray@uc.cl)

import sys
import traceback
#import time

from src.sunai_challenge import SunaiChallenge


def main():
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

