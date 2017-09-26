'''
Created on Apr 13, 2016

@author: ryan3971
'''
import sys
from cx_Freeze import setup, Executable
import Dice
import Label
import Photo
import Picture
import Player
import PygButton
import ryan_game
import Spinner 

# Dependencies are automatically detected, but it might need fine tuning.

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

setup(  name = "Test",
        version = "0.1",
        description = "My GUI application!",
        excludes = ["OpenGL.GL", "Numeric", "copyreg", "itertools.imap", "numpy", "pkg_resources", "queue", "winreg", "pygame.SRCALPHA", "pygame.sdlmain_osx"],
        executables = [Executable("Data Game\Data\Other\ryan_game.py", base=base)])
