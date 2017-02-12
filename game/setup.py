import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["pygame"], "include_files": ["apple2.png", "snakehead.png"]}

# GUI applications require a different base on Windows (the default is for a
# console application).

setup(  name = "Snaky!!!",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("game.py")])