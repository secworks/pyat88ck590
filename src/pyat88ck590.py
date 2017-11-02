#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# pyat88ck590.py
# --------------
# Code to talk to the Atmel/Microchip Crypto Authentication Eval
# Kit USB dongle.
#
#=======================================================================

import sys
import usb.core
import usb.util


def show_usb_devices():
    dev = usb.core.find(find_all=True)
    for d in dev:
        print(d)


def main():
    show_usb_devices()


#-------------------------------------------------------------------
# __name__
# Python thingy which allows the file to be run standalone as
# well as parsed from within a Python interpreter.
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())

#=======================================================================
# EOF pyat88ck590.py
#=======================================================================
