# Midi-To-Shawzin
*This project is still being developed, thank you for your patience*

This simple, lightweight, and portable python script allows you to play the Warframe shawzin through any USB-MIDI input compliant device connected to your computer.

By acting as a keymapper it converts your MIDI signals into Shawzin compatible strumming (ie. Waterfret2)

Typically when playing the Shawzin as DE intended you mark frets with the arrow keys, and stum with 1-3. Using Midi-to-shawzin lets you map that onto a MIDI-device!

Across all 9 scales, the effective range is C4 to D#6. However by design, it is impossible to play a B5 without bending notes with the whammy button.
This is not an issue when playing within the provided scales.

All in-game musical scales are supported:
- Pentatonic Minor
- Pentatonic Major
- Chromatic
- Hexatonic
- Major
- Minor
- Hirajoshi
- Phrygian
- Yo

Midi-To-Shawzin is a free and open-source fan-made project for musicians from beginner to expert to enjoy.

*If this is something that you end up liking, I may add the ability to load MIDI-files in too!*

# Features
- Shawzin pitch-bending
- Music scale select

# How to use
1. Launch Warframe
2. Bind Shawzin to gearwheel
3. Equip Shawzin
4. Launch 'main.py' from terminal
5. Follow on-screen prompts to bind music scale select and the whammy bar
6. You will now be in Pentatonic Minor scale by default
7. Enjoy!

# Technical
*If this project is well received then I will add options for this to be built into executable scripts for ease of use to all.*

To execute the program, simply run "main.py" and follow the console instructions.

## Pip packages
You may require to install several pip modules
```
pygame
pynput
```

## Issues
During testing I have found that the default key for switching musical scales 'Tab' is a little "stiff".
I have done the best I can on my side of the interface, sometimes if this occurs and music scale desyncronisation happens. Make sure you are actually 'focused' on the right screen (ie. no chat windows). To fix just use your PC keyboard to go to the current musical scale in the program displayed in the terminal.
