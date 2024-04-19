# Import modules
import configparser
import mido
import mido.backends.rtmidi
import os
import os.path
import sys
from tabulate import tabulate

executable_path = "sc55emu"
arguments = ""

config = configparser.ConfigParser()

# Read INI file if it exists
if os.path.isfile("nuked-port-selector.ini"):
	config.read("nuked-port-selector.ini")
	executable_path = config.get("settings","executable_path",fallback=executable_path)
	arguments = config.get("settings","arguments",fallback=arguments)

# Get MIDI input ports
inputs = mido.get_input_names()

# Check input ports are available
if len(inputs) == 0:
	print("Error: No MIDI input ports found!")
	input("Press Enter to exit...")
	exit()

# Display input ports in a table
inputs_split = []
for i in range(len(inputs)):
	inputs_split.append([inputs[i][0:-2],inputs[i][-1]])

print("Available MIDI input ports:\n")
print(tabulate(inputs_split, ["Device", "Port No."], tablefmt="simple", colalign=("left","left")))

# Get port no. from user
port = input("\nSelect port to use: ")

# Launch executable with the specified arguments
print("\nLaunching Nuked-SC55...")

if sys.platform == "win32":
	os.system(f"{executable_path} -p:{port} {arguments} "+" ".join(sys.argv[1:]))
else:
	os.system(f"./{executable_path} -p:{port} {arguments} "+" ".join(sys.argv[1:]))