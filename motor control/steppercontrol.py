"""
PF 8/4/15

Motor control script for use with Phidget 1067 Bipolar Stepper Controller

API reference:
http://www.phidgets.com/documentation/web/PythonDoc/Phidgets.html

Basic workflow:
Step 1. Create Phidget object - gives access to device specific functions
Step 2. Open Phidget using object
Step 3. Detect when a device is attached using object
Step 4. Call functions the device object provides
Step 5. Close object
"""

# General Python imports
import sys
from ctypes import *
from time import sleep

# Device specific imports
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import *
from Phidgets.Manager import Manager
from Phidgets.Devices.Stepper import Stepper
from Phidgets.Devices.Encoder import Encoder
from Phidgets.Phidget import PhidgetLogLevel

"""
Step 1
a. Create Manager object
b. Create event handler callback functions
c. Set the event handlers
d. Open the Manager via the object
e. Display device info
"""
