from midi import MidiConnector
import serial.tools.list_ports
import usb

def connect_to_midi():
	print('Discovering USB devices...')

	devlist = usb.core.find(find_all=True)

	count = 1
	for dev in devlist:
		dev_string = str(count) + ") Product: " + str(dev.product) + ", Manufacturer: " + str(dev.manufacturer) + ", Serial No: " + str(dev.serial_number)
		print(dev_string)
		count += 1
		
		
		



	# Using the selected serial port connecting to the device instance.
	#connection = MidiConnector('')

	
	
		
		  
