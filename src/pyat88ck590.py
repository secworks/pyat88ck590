# Code to read out and display info about all USB devices connected.
# Code use PyUSB and working backend such as libusb.

import usb.core
import usb.util

dev = usb.core.find(find_all=True)
for d in dev:
    print(d)
