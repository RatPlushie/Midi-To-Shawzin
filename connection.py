from midi import MidiConnector
import serial.tools.list_ports
import usb

def list_usb_devices():
	devlist = list(usb.core.find(find_all=True))

	count = 1
	for dev in devlist:
		dev_string = str(count) + ") " + str(dev.manufacturer) + " " + str(dev.product)
		print(dev_string)
		count += 1
	
	print()
	midi_input = input('Select Midi device: ')

	print(str(devlist[int(midi_input) - 1].manufacturer), str(devlist[int(midi_input) - 1].product) + ' selected')

	return devlist[int(midi_input) - 1]
	

'''
def get_serial_port():
	# TODO Using the selected serial port connecting to the device instance.
	pass
'''

def connect_to_midi():
	print()
	print('Discovering USB devices...')

	# Displaying and asking the user for the correct USB Midi device
	usb_dev = list_usb_devices()

	#connection = MidiConnector('')

	
	
		
		  
