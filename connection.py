from midi import MidiConnector
import pygame, pygame.midi

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
	user_input = input('Select your input device:')
	return int(user_input)
	
		
		  
