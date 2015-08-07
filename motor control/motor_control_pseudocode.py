"""
PF 8/5/15

Pseudo code to describe the motor control logic & data output with Phidget 1065 Motor Controller

API reference:
http://www.phidgets.com/documentation/web/PythonDoc/Phidgets.html

Requirements:
	1. Input: user defined speed for open & close
	2. Input: user defined rotation angle for open & close
	3. Output: CSV file with
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
	.getCurrent(index) - motor current draw in Amps
b. Encoder
	.setPosition(index, position) where 'position' resets the internal library position to calculate new absoluate position changes via the change handler
	.getPosition(index) is the absolute position calculated since the encoder was plugged in, can be reset to anything with .setPosition()
c. Torque Sensor 
	.getSensorValue(index)
"""

# General Python imports
import sys
import time

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
	encoder = Encoder()
	torque_sensor = AnalogInput()
except RuntimeError as error:
	print ('Python Runtime Exception relating to motor object: %s' % error.details)
	exit(1)

"""
Step 2 - Open device(s) using the object created above
"""
try:
	motor.openPhidget()
	encoder.openPhidget()
	torque_sensor.openPhidget()
except PhidgetException as error:
	print ('Device error %i, %s' % (error.code, error.details))
	exit(1)

"""
Step 3 - Detect when a device is attached
"""
try:
	# method has units of milliseconds, so wait for 5 seconds
	motor.waitForAttach(5000)
	encoder.waitForAttach(5000)
	torque_sensor.waitForAttach(5000)
except PhidgetException as error:
	print ('Device Error %i: %s' % (error.code, error.details))
    try:
        motor.closePhidget()
        encoder.closePhidget()
        torque_sensor.closePhidget()
    except PhidgetException as error:
        print ('Phidget Error %i: %s' % (error.code, error.details))
        exit(1)
    exit(1)

"""
Step 4 - Main Control Program 
"""
# Collect user inputs
user_input_position_open = input('Enter the angle to rotate OPEN in degrees: ')
user_input_speed_open = input('Enter the OPEN speed in degrees/second: ')
user_input_position_close = input('Enter the angle to rotate CLOSE in degrees: ')
user_input_speed_close = input('Enter the CLOSE speed in degrees/second: ')

# direction: [speed, position]
inputs = {
	'Open': [int(user_input_speed_open), int(user_input_position_open)],
	'Close': [int(user_input_speed_close), int(user_input_position_close)]
}

# Convert speed: deg/sec -> RPM -> % duty cycle. Motor rotation: 33 RPM at 100% voltage (24 VDC)
# Convert position to counts for the encoder. Encoder has 300 counts/revolution = 0.833 counts/degree
PWM_duty_cycle = []
commanded_position = []

# each list ordered [open, close]
for key, value in inputs.items():
	PWM_duty_cycle.append((value[0] * 0.16666) / 33)
	commanded_position.append(value[1] * 0.83333)

# Set encoder & calculate position difference [open, close]
encoder.setPosition(0, 0)
position_difference = []
position_difference[:] = [i - encoder.getPosition(0) for i in commanded_position]

# Create simple PID controller
# Reference: http://examples.oreilly.com/9780596809577/CH09/PID.py
class PID:
	"""
	Simple PID control from "Real-World Instrumentation with Python" 
	by J. M. Hughes, published by O'Reilly Media, December 2010"
	"""
	 def __init__(self):
        # initialze gains
        self.Kp = 0
        self.Kd = 0
        self.Ki = 0

        self.Initialize()

    def SetKp(self, invar):
        # Set proportional gain
        self.Kp = invar

    def SetKi(self, invar):
        #  Set integral gain
        self.Ki = invar

    def SetKd(self, invar):
        #  Set derivative gain
        self.Kd = invar

    def SetPrevErr(self, preverr):
        # Set previous error value
        self.prev_err = preverr

    def Initialize(self):
        # initialize delta t variables
        self.currtm = time.time()
        self.prevtm = self.currtm

        self.prev_err = 0

        # Term result variables
        self.Cp = 0
        self.Ci = 0
        self.Cd = 0

    def GenOut(self, error):
        """ Performs a PID computation and returns a control value based on
            the elapsed time (dt) and the error signal from a summing junction
            (the error parameter).
        """
        self.currtm = time.time()               # get t
        dt = self.currtm - self.prevtm          # get delta t
        de = error - self.prev_err              # get delta error

        self.Cp = self.Kp * error               # Proportional term
        self.Ci += error * dt                   # Integral term

        self.Cd = 0
        if dt > 0:                              # no div by zero
            self.Cd = de/dt                     # Derivative term

        self.prevtm = self.currtm               # save t for next pass
        self.prev_err = error                   # save t-1 error

        # Sum the terms and return the result:
        # Proportional + Integral*IntegralError + Derivative*DerivativeError
        return self.Cp + (self.Ki * self.Ci) + (self.Kd * self.Cd)

# Now instantiate the PID controller & set the initial gains (WAG)
pid = PID()
pid.SetKp(1.1)
pid.SetKd(1)
pid.SetKi(1)

# Create lists to store output's of interest
motor_current_output = []
torque_sensor_output = []
position_output = []
velocity_output = []

"""
Plain text description

for each direction
	while position error is large
		drive the motor at input speed
		use the PID controller to control time step
		collect motor current & torque sensor data for output file
		check that current & torque haven't gone crazy which may indicate a mechanical problem
		calculated update position error
"""
for direction in inputs.keys():
	if direction == 'Open':
		difference = position_difference[0]
	else:
		difference = position_difference[1]

	while difference > 1:
		# Set accleeration to 50%
		try:
			motor.setAcceleration(0, 50)
		except PhidgetException as error:
			print ('Phidget Error %i: %s' % (error.code, error.details))

		# Speed & error depend on the direction we're going
		if direction == 'Open':
			try:
				motor.setVelocity(0, PWM_duty_cycle[0]) # Set the OPEN speed as positive
			except PhidgetException as error:
				print ('Phidget Error %i: %s' % (error.code, error.details))
			commanded_position = commanded_position[0] # Set using the OPEN index

		else:
			try:
				motor.setVelocity(0, -PWM_duty_cycle[1]) # Set the CLOSE speed as negative
			except PhidgetException as error:
				print ('Phidget Error %i: %s' % (error.code, error.details))
			commanded_position = commanded_position[1] # Set using the CLOSE index

		error = commanded_position[0] - encoder.getPosition(0)
		pid_out = pid.GenOut(error)

		# Build output lists
		motor_current_output.append(motor.getCurrent(0))
		torque_sensor_output.append(torque_sensor.getSensorValue(0))
		position_output.append(encoder.getPosition(0))
		velocity_output.append(motor.getVelocity(0))

		# Monitor sensors to make sure nothing is breaking too bad!
		# Rated current is 2.2 Amps. Stall current is 10 Amps
		if motor.getCurrent(0) > 3:   
			motor.setVelocity(0, 0)
			motor.closePhidget()
			exit(1)
		# Torque sensor outputs 0-5 VDC linearly with full-scale torque = 89 in-lbs. So 64 in-lbs ~ 3.6 VDC
		if torque_sensor.getSensorValue(0) > 3.6:
			motor.setVelocity(0, 0)
			motor.closePhidget()
			exti(1)

		# Evaluate new position to check against
		updated_position = encoder.getPosition(0)
		difference = commanded_position - updated_position

"""
Step 5 - Close the objects
"""
try:
	motor.closePhidget()
	encoder.closePhidget()
except PhidgetException as error:
	print ('Phidget Error %i: %s' % (error.code, error.details))

"""
Step 6 - Output recorded data as CSV file
"""
