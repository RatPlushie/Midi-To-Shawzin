from connection import *

if __name__ == "__main__":
	try:
		# Title
		print('Midi to Shawzin:')

		# Init connection
		connection = setup_midi()

		# Binding controls
		keybind_scale, keybind_whammy = keyboard_controls(connection)

		# Watching MIDI device and converting inputs to shawzin controls
		watch_midi(connection, keybind_scale, keybind_whammy)
	
	except (KeyboardInterrupt):
		print('Packing away Shawzin...')