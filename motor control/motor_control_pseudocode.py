"""
PF 8/5/15

Pseudo code to describe the motor control logic & data output with Phidget 1065 Motor Controller

API reference:
http://www.phidgets.com/documentation/web/PythonDoc/Phidgets.html

Requirements
	1. Input: ability to control motor speed
	2. Input: ability to control motor rotation angle
	3. Output: CSV file with
		a. Run time
		b. Position
		c. Current draw
		d. Torque 

Basic workflow:
Step 1. Create Phidget object(s) - gives access to device specific functions
Step 2. Open Phidget using object
Step 3. Detect when a device is attached using object
Step 4. Call API methods to control the system
Step 5. Close object
Step 6. Output CSV

Key Methods:
a. Motor
	.setVelocity(self, index, value) where 'value' range is -100 to 100 as percent duty cycle for PWM
	.getVelocity(self, index)
	.setAcceleration(self, index, value) where 'value' range is range between .getAccelerationMin and .getAccelerationMax based on the motor used
	.getAcceleration(self, index)
b. Encoder
	.setPosition(self, index, position) where 'position' resets the internal library position to calculate new absoluate position changes via the change handler
	.getPosition(self, index) is the absolute position calculated since the encoder was plugged in, can be reset to anything with .setPosition()
c. Rotary Potentiometer
	.getSensorValue(self, index)
d. Torque Sensor 
	.getSensorValue(self, index)
"""


# General Python imports
import sys
from time import sleep

# Device specific imports
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import *
from Phidgets.Manager import Manager
from Phidgets.Devices.MotorControl import MotorControl
from Phidgets.Devices.Encoder import Encoder
from Phidgets.Phidget import PhidgetLogLevel

"""
Step 1 - Create device objects(s) [I'm skipping the event handlers & their callbacks for simplicity]
"""
try:
	motor = MotorControl()
except RuntimeError as error:
	print ('Python Runtime Exception relating to motor object: %s' % error.details)
	exit(1)

"""
Step 2: Open device(s) using the object created above
"""
try:
	motor.openPhidget()
except PhidgetException as error:
	print ('Device error %i, %s' % (error.code, error.details))
	exit(1)

"""
Step 3: Detect when a device is attached
"""
try:
	# method has units of milliseconds, so wait for 5 seconds
	motor.waitForAttach(5000)
except PhidgetException as error:
	print ('Device Error %i: %s' % (error.code, error.details))
    try:
        motor.closePhidget()
    except PhidgetException as error:
        print ('Phidget Error %i: %s' % (error.code, error.details))
        exit(1)
    exit(1)
else:
    info()