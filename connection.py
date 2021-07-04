from midi import MidiConnector
import serial.tools.list_ports
import usb

def list_usb_devices():
	devlist = usb.core.find(find_all=True)

	count = 1
	for dev in devlist:
		dev_string = str(count) + ") " + str(dev.manufacturer) + " " + str(dev.product)
		print(dev_string)
		count += 1


def get_serial_port():
	# TODO Using the selected serial port connecting to the device instance.
	pass


def connect_to_midi():
	print('Discovering USB devices...')

	list_usb_devices()
	
	#connection = MidiConnector('')

	
	
		
		  
