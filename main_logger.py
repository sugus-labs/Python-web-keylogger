'''

Author: Gustavo Martin Vela
Python-web-keylogger
2013

'''

from evdev import InputDevice, list_devices

devices = map(InputDevice, list_devices())

main_devices = {}

for dev in devices:
	name_upper = dev.name.upper()
	if "USB" in name_upper:
		main_devices["USB"] = dev
	if "KEYBOARD" in name_upper:
		main_devices["KEYBOARD"] = dev 
	#print( '%-20s %-32s %s' % (dev.fn, dev.name, dev.phys) )

print main_devices