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
# Create Manager object
try:
	manage = Manager()
except RuntimeError as error:
	print ('Python Runtime Exception: %s' % error.details)
	exit(1)

# Create event handler callabacks (skip the server related ones, don't need right now)
def device_attached_callback(i):
	attached = i.device
	# methods are from Phidgets.Phidget.Phidget base class
	print ('Memo from Management: Device - %i: %s is attached!' % (attached.getSerialNumber(), attached.getDeviceName()))

def device_detached_callback(i):
	detached = i.device
	print ('Memo from Management: Device - %i: %s is detached!' % (detached.getSerialNumber(), detached.getDeviceName()))

def device_error_callback(i):
	print ('Sadly, a Phidget error has occured: %i: %s' % (i.Code, i.description))

# Set the event handlers
# These get called when a Phidget is physically plugged-in or removed. They require the event callback handlers defined above as parameters
try:
	manage.setOnAttachHandler(device_attached_callback)
	manage.setOnDetachHandler(device_detached_callback)
	manage.setOnErrorHandler(device_error_callback)
except PhidgetException as error:
	print ('A device exception occured while setting event handlers, better check it out - %i: %s' % (error.code, error,details))
	exit(1)

# Open the Manager from the object defined above
try:
	manage.openManager()
except PhidgetException as error:
	print ('A device exception occured while opening the Manager - %i: %s' % (error.code, error,details))
	exit(1)

# Display info for all attached devices
attached_devices = manage.getAttachedDevices()
for device in attached_devices:
	print ('Attached: %8s, Type: %30s, Serial: %10d, Version: %8d' % (device.isAttached(), device.getDeviceName(), device.getSerialNumber(), device.getDeviceVersion()))