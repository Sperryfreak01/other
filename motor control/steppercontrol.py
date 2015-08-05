"""
PF 8/4/15

Motor control script for use with Phidget 1067 Bipolar Stepper Controller

API reference:
http://www.phidgets.com/documentation/web/PythonDoc/Phidgets.html

Basic workflow:
Step 1. Create Phidget object(s) - gives access to device specific functions
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
a. Create device object(s)
b. Create event handler callback functions
c. Set the event handlers
"""
# Create device objects
try:
	stepper = Stepper()
except RuntimeError as error:
	print ('Python Runtime Exception relating to stepper object: %s' % error.details)
	exit(1)

try:
	encoder = Encoder()
except RuntimeError as error:
	print ('Python Runtime Exception relating to encoder object: %s' % error.details)
	exit(1)

# Info display function
def info():
	print ('Attached: %8s, Type: %30s, Serial: %10d, Version: %8d' % (stepper.isAttached(), stepper.getDeviceName(), stepper.getSerialNum(), stepper.getDeviceVersion()))

# Create the common event handler callabacks (skip the server related ones, don't need right now)
def device_attached_callback(i):
	attached = i.device
	# methods are from Phidgets.Phidget.Phidget base class
	print ('Memo from Management: Device - %i: %s is attached!' % (attached.getSerialNumber(), attached.getDeviceName()))

def device_detached_callback(i):
	detached = i.device
	print ('Memo from Management: Device - %i: %s is detached!' % (detached.getSerialNumber(), detached.getDeviceName()))

def device_error_callback(i):
	try:
        source = i.device
        print ('Device: %s, Phidget Error %i: %s' % (source.getSerialNum(), i.code, i.description))
    except PhidgetException as error:
        print ("Phidget Exception %i: %s" % (error.code, error.details))

# Create Encoder specific event handler callabacks
def encoder_input_change(i):
	source = i.device
    print ('Encoder %i: Input %i: %s' % (source.getSerialNum(), i.index, i.state))

def encoder_position_change(i):
	source = i.device
	print ('Encoder %i: Encoder %i -- Change: %i -- Time: %i -- Position: %i' % (source.getSerialNum(), i.index, i.positionChange, i.time, encoder.getPosition(i.index)))

# Create Stepper specific event handler callabacks
def stepper_current_changed(i):
	source = i.device
	print ('Stepper %i: Motor %i -- Current Draw: %6f' % (source.getSerialNum(), i.index, i.current))

def stepper_input_change(i):
	source = e.device
	print ('Stepper %i: Input %i -- State: %s' % (source.getSerialNum(), i.index, i.state))

def stepper_position_changed(i):
	source = e.device
	print ('Stepper %i: Motor %i -- Position: %f' % (source.getSerialNum(), i.index, i.position))

def stepper_velocity_change(i):
	source = e.device
	print ('Stepper %i: Motor %i -- Velocity: %f' % (source.getSerialNum(), i.index, i.velocity))

# Set the event handlers
# These get called when a Phidget is physically plugged-in or removed. They require the event callback handlers defined above as parameters
try:
	# Set common handlers
	encoder.setOnAttachHandler(device_attached_callback)
	encoder.setOnDetachHandler(device_detached_callback)
	encoder.setOnErrorHandler(device_error_callback)
	stepper.setOnAttachHandler(device_attached_callback)
	stepper.setOnDetachHandler(device_detached_callback)
	stepper.setOnErrorHandler(device_error_callback)
	# Set specific handlers
    encoder.setOnInputChangeHandler(encoder_input_change)
    encoder.setOnPositionChangeHandler(encoder_position_change)
    stepper.setOnCurrentChangeHandler(stepper_current_changed)
    stepper.setOnInputChangeHandler(stepper_input_change)
    stepper.setOnPositionChangeHandler(stepper_position_changed)
    stepper.setOnVelocityChangeHandler(stepper_velocity_change)
except PhidgetException as error:
	print ('A device exception occured while setting event handlers, better check it out - %i: %s' % (error.code, error,details))
	exit(1)

"""
Step 2: Open device(s) using object
"""
try:
	stepper.openPhidget()
	encoder.openPhidget()
except PhidgetException as error:
	print ('Device error %i, %s' % (error.code, error.details))
	exit(1)

"""
Step 3: Detect when a device is attached and display its info
"""
try:
	# method has units of milliseconds, so wait for 10 seconds
	stepper.waitForAttach(10000)
	encoder.waitForAttach(10000)
except PhidgetException as error:
	print ('Device Error %i: %s' % (error.code, error.details))
    try:
        encoder.closePhidget()
        stepper.closePhidget()
    except PhidgetException as e:
        print ('Phidget Error %i: %s' % (i.code, i.details))
        exit(1)
    exit(1)
else:
    info()