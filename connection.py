import pygame, pygame.midi
from prettytable import PrettyTable
from pynput.keyboard import Key, Controller
from exceptions import *
from scales import *

class Shawzin:
	def __init__(self):
		self.scale_list = Scales.scale_list
		self.current_scale_index = 0
		self.current_scale = self.scale_list[self.current_scale_index]
		self.keyboard_controller = Controller()


	def next_scale(self):
		# Iterating to the next scale, rolling back to zero if reaching out of bounds of the list
		if self.current_scale_index + 1 >= len(self.scale_list):
			self.current_scale_index = 0
			self.current_scale = self.scale_list[self.current_scale_index]

		else:
			self.current_scale_index += 1
			self.current_scale = self.scale_list[self.current_scale_index]


	def get_scale_table(self):
		scale_table = PrettyTable()

		scale_table.field_names = [
			'NoFret1', 
			'NoFret2', 
			'NoFret3', 

			'SkyFret1', 
			'SkyFret2', 
			'SkyFret3', 

			'EarthFret1', 
			'EarthFret2', 
			'EarthFret3', 

			'WaterFret1', 
			'WaterFret2', 
			'WaterFret3'
		]

		scale_table.add_row([
			self.current_scale.get('NoFret1'), 
			self.current_scale.get('NoFret2'), 
			self.current_scale.get('NoFret3'),

			self.current_scale.get('SkyFret1'), 
			self.current_scale.get('SkyFret2'), 
			self.current_scale.get('SkyFret3'),

			self.current_scale.get('EarthFret1'), 
			self.current_scale.get('EarthFret2'), 
			self.current_scale.get('EarthFret3'), 

			self.current_scale.get('WaterFret1'), 
			self.current_scale.get('WaterFret2'), 
			self.current_scale.get('WaterFret3'), 
		])

		return (self.current_scale.get('Scale'), scale_table)


	def get_shawzin_strum(self, ansi_note):
		for key, value in self.current_scale.items():
			if ansi_note == value:
				return key


	def play_note(self, ansi_note, io):
		strum = self.get_shawzin_strum(ansi_note)

		if strum == 'NoFret1':
			if io:
				self.keyboard_controller.press(Key.right)
				self.keyboard_controller.press('1')

			else:
				self.keyboard_controller.release(Key.right)
				self.keyboard_controller.release('1')







		elif strum == 'NoFret2':
			pass

		elif strum == 'NoFret3':
			pass

		elif strum == 'SkyFret1':
			pass

		elif strum == 'SkyFret2':
			pass

		elif strum == 'SkyFret3':
			pass

		elif strum == 'EarthFret1':
			pass

		elif strum == 'EarthFret2':
			pass

		elif strum == 'EarthFret3':
			pass

		elif strum == 'WaterFret1':
			pass

		elif strum == 'WaterFret2':
			pass

		elif strum == 'WaterFret3':
			pass


	def whammy(self, io):
		pass



class MIDI_Event:
	'''
	MIDI commands:
		176 - Button press (velocity 127 for pressON, velocity 0 for pressOFF)
		224 - Rotary (0 velocity for lowest, 127 velocity for highest. Some models will rest in center - velocity 64)
		144 - Note press
		128 - Note release
	'''

	def __init__(self, event):
		self.command = event[0][0][0]
		self.note = event[0][0][1]
		self.ansi_note = pygame.midi.midi_to_ansi_note(self.note)
		self.velocity = velocity = event[0][0][2] # I have no clue what this one is, or if it's the right name
		self.etc = event[0][0][3]
		self.clock = event[0][1]


	def __str__(self):
		return 'Command: {command}, Note: {note}, Velocity: {velocity}, ETC: {etc}, Clock: {clock}'.format(command = self.command, note = self.ansi_note, velocity = self.velocity, etc = self.etc, clock = self.clock)


	def is_button(self):
		if self.command == 176:
			return True
		else:
			return False


	def is_dial(self):
		if self.command == 224:
			return True
		else:
			return False


	def is_note(self):
		if self.command == 144 or self.command == 128:
			return True
		else:
			return False


	def compare_key(self, key):
		if self.command == key.command and self.ansi_note == key.ansi_note:
			return True
		else:
			return False


def device_select():
	print('Finding devices...')
	print()

	# Discovering all midi devices
	dev_list=[]
	for n in range(pygame.midi.get_count()):
		dev_list.append(pygame.midi.get_device_info(n))

	# Printing out the list of input devices
	count=0
	for dev in dev_list:
		dev_interface = dev[0]
		dev_name = dev[1]
		is_input = dev[2]  # if true then it is an input
		is_output = dev[3]  # if true then it is an output
		is_opened = dev[4]  # if true then it is opened

		dev_io=''
		if is_input:
			dev_io = 'INPUT Device'
		elif is_output:
			dev_io = 'OUTPUT Device'
		else:
			dev_i = 'INVALID Device'

		print('{count}) {io}: {name}, interface: {interface}'.format(
		    count = count, io = dev_io, name = dev_name, interface = dev_interface))
		count += 1

	print()

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
			loop=False
		except (ValueError, InvalidRangeException, NotInputDeviceException) as e:
			print('Please enter a valid selection')
			print()

	return int(user_input)


def setup_midi():
	# Initialisation of midi device connection
	pygame.midi.init()
	dev = device_select()
	midi_input = pygame.midi.Input(dev)

	return midi_input


def capture_midi(connection):
	isCaptured = False
	while not isCaptured:
		if connection.poll():
			event = connection.read(1)
			midi_event = MIDI_Event(event)

			isCaptured = True
			return midi_event


def keyboard_controls(connection):
	# Asking user to make a MIDI input and capturing it as a returnable object
	print()
	print('Setting up midi keybinds...')

	# Getting the keybind for the button to change musical scale
	keybind_scale = None
	found_scale_button = False
	while not found_scale_button:
		try:
			print('Select non-note button on MIDI device for the music scale select button:')
			midi_event = capture_midi(connection)

			if midi_event.is_button():
				print('Scale keybinding successful')
				keybind_scale = midi_event
				found_scale_button = True
			
			else:
				raise InvalidMidiRange


		except (InvalidMidiRange):
			print('Please enter a non-note button')

	print()

	# Getting the keybind for the whammy button
	keybind_whammy = None
	found_whammy = False
	while not found_whammy:
		try:
			print('Select non-note button on MIDI device for the whammy:')
			midi_event = capture_midi(connection)

			if midi_event.is_dial() or midi_event.is_button():
				print('Whammy keybind successful')
				keybind_whammy = midi_event
				found_whammy = True

			else:
				raise InvalidMidiRange

		except (InvalidMidiRange):
			print('Please enter a non-note dial')

	print()
	print('Setup complete')
	print()

	return (keybind_scale, keybind_whammy)


def watch_midi(connection, keybind_scale, keybind_whammy):
	# Init of an instance of the shawin
	shawzin = Shawzin()

	while True:
		# Waiting for a midi event
		if connection.poll():
			# Grabbing midi event
			event = connection.read(1)
			midi_event = MIDI_Event(event)

			# Checking what has been pressed
			# Note press
			if midi_event.is_note():
				# TODO write translation between midi and shawzin controls
				'''
				key press
				ignore hold
				key release
				'''
				# Note press
				if midi_event.command == 144:
					shawzin.play_note(midi_event.ansi_note, True)
					
				# Note release
				elif midi_event.command == 128:
					shawzin.play_note(midi_event.ansi_note, False)



			# Scale select button binding pressed
			elif midi_event.compare_key(keybind_scale):
				shawzin.next_scale()
				scale_name, scale_table = shawzin.get_scale_table()
				print(scale_name)
				print(scale_table)
				print()

			# Whammy binding pressed
			elif midi_event.compare_key(keybind_whammy):
				# TODO test if the whammy is still being pressed
				pass
				#print(midi_event)




				#shawzin.whammy(True)

			# Storing the previous event for future use
			previous_event = midi_event


