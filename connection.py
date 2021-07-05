import pygame, pygame.midi
from exceptions import *

def device_select():
	print('Finding devices...')
	print()

	# Discovering all midi devices
	dev_list = []
	for n in range (pygame.midi.get_count()):
		dev_list.append(pygame.midi.get_device_info(n))

	# Printing out the list of input devices
	count = 0
	for dev in dev_list:
		dev_interface = dev[0]
		dev_name = dev[1]
		is_input = dev[2] # if true then it is an input
		is_output = dev[3] # if true then it is an output
		is_opened = dev[4] # if true then it is opened

		dev_io = ''
		if is_input:
			dev_io = 'INPUT Device'
		elif is_output:
			dev_io = 'OUTPUT Device'
		else:
			dev_io = 'INVALID Device'

		print('{count}) {io}: {name}, interface: {interface}'.format(count = count, io = dev_io, name = dev_name, interface = dev_interface))
		count += 1

	# Asking user for desired device
	loop = True
	while loop:
		try:
			user_input = input('Select your input device:')
			
			# Test if NaN
			float(user_input)

			# Test if user input is within valid range
			if int(user_input) < 0 or int(user_input) > len(dev_list) - 1:
				raise InvalidRangeException

			# Test if device is midi input
			if dev_list[int(user_input)][3]:
				raise NotInputDeviceException

			# Breaking out of loop if all condition are met
			loop =  False
		except (ValueError, InvalidRangeException, NotInputDeviceException) as e:
			print('Please enter a valid selection')
			print()

	return int(user_input)


def connect_midi():
	pygame.midi.init()
	dev = device_select()
	midi_input = pygame.midi.Input(dev)

	return midi_input


def watch_midi(connection):
	while True:
		if connection.poll():
			event = connection.read(1)
			print(event)
	
		
		  
