import pygame
import pygame.midi
from exceptions import *
from scales import *

class Shawzin:
	def __init__(self):
		self.scale_list = Scales.scale_list
		self.current_scale_index = 0
		self.current_scale = self.scale_list[self.current_scale_index]

	def next_scale(self):
		# Iterating to the next scale, rolling back to zero if reaching out of bounds of the list
		if self.current_scale_index + 1 >= len(self.scale_list):
			self.current_scale_index = 0
			self.current_scale = self.scale_list[self.current_scale_index]

		else:
			self.current_scale_index += 1
			self.current_scale = self.scale_list[self.current_scale_index]


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

	def compare_key(self, keybinding):
		if self.command == keybinding.command and self.ansi_note == keybinding.ansi_note:
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
		if connection.poll():
			# Grabbing midi event
			event = connection.read(1)
			midi_event = MIDI_Event(event)

			# Checking what has been pressed
			# Note press
			if midi_event.is_note():
				# TODO write translation between midi and shawzin controls
				print('Note Played')

			# Scale select button binding pressed
			elif midi_event.compare_key(keybind_scale):
				# TODO write code to change between scale modes
				print('Scale selected')
				shawzin.next_scale()

			# Whammy binding pressed
			elif midi_event.compare_key(keybind_whammy):
				# TODO write code to activate the whammy
				print('whammy selected')


