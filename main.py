import midi
from scales import PentatonicMinor
from connection import connect_to_midi

'''
To play shawzin the user selects which fret (if any) and then presses either 1,2,3 on the keyboard
To achieve a whammy, or a B5 note, the user modifies this further with the spacebar
Across all 9 scales, the range is C4 to D#6

https://pypi.org/project/py-midi/
https://warframe.fandom.com/wiki/Shawzin
'''

if __name__ == "__main__":
	print('Midi to Shawzin:')

	connect_to_midi()







