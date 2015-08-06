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
Step 4. Main program - Call API methods to control the system
Step 5. Close object
Step 6. Output CSV

Key Methods:
a. Motor
	.setVelocity(index, value) where 'value' range is -100 to 100 as percent duty cycle for PWM
	.getVelocity(index)
	.setAcceleration(index, value) where 'value' range is range between .getAccelerationMin and .getAccelerationMax based on the motor used
	.getAcceleration(index)
b. Encoder
	.setPosition(index, position) where 'position' resets the internal library position to calculate new absoluate position changes via the change handler
	.getPosition(index) is the absolute position calculated since the encoder was plugged in, can be reset to anything with .setPosition()
c. Rotary Potentiometer
	.getSensorValue(index)
d. Torque Sensor 
	.getSensorValue(index)
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
Step 2 - Open device(s) using the object created above
"""
try:
	motor.openPhidget()
except PhidgetException as error:
	print ('Device error %i, %s' % (error.code, error.details))
	exit(1)

"""
Step 3 - Detect when a device is attached
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

"""
Step 4 - Main Control Program 
"""
user_input_position = input('Enter the angle to rotate in degrees: ')
user_input_speed = input('Enter the speed in degrees/second: ')

# Convert speed: deg/sec -> RPM -> %DC
PWM_duty_cycle = (int(user_input_speed) * 0.16666) / 33 # Motor rotates at 33 RPM at 100% voltage (24 VDC)

# Establish position difference. The motor encoder has 300 counts/rotation = 0.833 degree/count
Encoder.setPosition(0, 0)
initial_position = Encoder.getPosition(0)
initial_difference = user_input_position - initial_position