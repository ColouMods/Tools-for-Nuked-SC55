# Import modules
import configparser
import os
import pathlib
import shutil
from tabulate import tabulate

def exitmessage(message):
	print(message)
	input("Press Enter to exit...")
	exit()
	return

expansions_folder = "expansions"
bin_filename = "jv880_waverom_expansion.bin"

config = configparser.ConfigParser()

# Read INI file if it exists
if os.path.isfile("nuked-expansion-selector.ini"):
	config.read("nuked-expansion-selector.ini")
	expansions_folder = config.get("settings","expansions_folder",fallback=expansions_folder)
	bin_filename = config.get("settings","bin_filename",fallback=bin_filename)
	
if not os.path.isdir(expansions_folder):
	exitmessage(f"Error: '{expansions_folder}' folder not found!")

files = os.listdir(expansions_folder)
expansions = []

# Find all bin files in the expansions folder
for i in range(len(files)):
	currentfile = pathlib.Path(os.path.join("expansions",files[i]))
	if currentfile.is_file() and currentfile.suffix.lower() == ".bin":
		expansions.append(files[i])

if len(expansions) == 0:
	exitmessage("Error: Could not find any .bin files!")

# Print list of bin files
print("Available .bin files:\n")

expansions_table = []
for i in range(len(expansions)):
	expansions_table.append([i+1,expansions[i]])

print(tabulate(expansions_table, ["No.", "Name"], tablefmt="simple", colalign=("left","left")))

# Get expansion no. from user
selected = int(input("\nSelect .bin to use: "))

# Copy selected expansion to correct location
selected_file = pathlib.Path(os.path.join(expansions_folder,expansions[selected-1]))
shutil.copyfile(selected_file,bin_filename)

exitmessage("\nSuccesfully copied expansion!")