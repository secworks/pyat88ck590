#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# pyat88ck590.py
# --------------
# Code to talk to the Atmel/Microchip Crypto Authentication Eval
# Kit USB dongle.
#
# PID, VID etc info for the dongle:
# idVendor               : 0x03eb
# idProduct              : 0x2312
# bcdDevice              : 0x1000 Device 16.0
# iManufacturer          : 0x1 ATMEL
# iProduct               : 0x2 Crypto Device Demo
#
#=======================================================================

import sys
import usb.core
import usb.util




#-------------------------------------------------------------------
#-------------------------------------------------------------------
def dump_all_devices():
    all_devs = usb.core.find(find_all=True)
    for d in all_devs:
        print(d)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_device(pid, vid):
    dev = usb.core.find(idProduct = pid, idVendor = vid)

    if dev is None:
        raise ValueError('Device not found')
    return dev


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def main():
#    dump_all_devices()
    print("Specific device - ATMEL Crypto Dongle:\n")
    my_dev = find_device(pid = 0x2312, vid = 0x03eb)
    print(my_dev)


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
