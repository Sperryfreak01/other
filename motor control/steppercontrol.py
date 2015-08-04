"""
Motor control script for use with Phidget 1067 Bipolar Stepper Controller

API reference:
http://www.phidgets.com/documentation/web/PythonDoc/Phidgets.html

Basic workflow:
1. Create Phidget object - gives access to device specific functions
2. Open Phidget using object
3. Detect when a device is attached using object
4. Call functions the device object provides
5. Close object

