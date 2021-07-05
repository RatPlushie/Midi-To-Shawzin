import pygame, pygame.midi
from connection import *

'''
To play shawzin the user selects which fret (if any) and then presses either 1,2,3 on the keyboard
To achieve a whammy, or a B5 note, the user modifies this further with the spacebar
Across all 9 scales, the range is C4 to D#6

https://pypi.org/project/py-midi/
https://warframe.fandom.com/wiki/Shawzin
'''

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







