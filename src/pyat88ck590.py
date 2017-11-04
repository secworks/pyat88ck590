#!/usr/bin/env python
# -*- coding: utf-8 -*-
#=======================================================================
#
# pyat88ck590.py
# --------------
# Code to talk to the Atmel/Microchip Crypto Authentication Eval
# Kit USB dongle.
#
# path:                "USB_03eb_2312_14100000"
# vendor_id:           0x03eb
# product_id:          0x2312
# serial_number:       ""
# release_number:      0x1000
# manufacturer_string: "ATMEL"
# product_string:      "Crypto Device Demo"
# usage_page:          65535
# usage:               1
# interface_number:    -1
#
#=======================================================================

import sys
import hidapi


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def dump_all_devices():
    for dev in hidapi.hid_enumerate():
        print dev.description()


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def main():
    hidapi.hid_init()
    dump_all_devices()


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
