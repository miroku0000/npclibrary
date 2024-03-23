import os
import os

def remove_desktop_ini_files(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower() == "desktop.ini":
                os.remove(os.path.join(root, file))
                print(f"Removed: {os.path.join(root, file)}")

# Assuming "npcs" directory is located at a certain path, e.g., "/mnt/data/npcs"
# Uncomment and modify the path as necessary when running the function.
# remove_desktop_ini_files("/mnt/data/npcs")


def clean_directory(directory):
    for root, dirs, files in os.walk(directory):
        # Create sets to hold the base filenames without extensions for quick lookup
        png_files = {os.path.splitext(f)[0] for f in files if f.endswith('.png')}
        json_files = {os.path.splitext(f)[0] for f in files if f.endswith('.json')}
        
        # Find PNG files without a corresponding JSON file and delete them
        png_without_json = png_files - json_files
        for base_name in png_without_json:
            os.remove(os.path.join(root, base_name + '.png'))
            print(f"Deleted {os.path.join(root, base_name )} as no corresponding JSON file found.")
        
        # Find JSON files without a corresponding PNG file and delete them
        json_without_png = json_files - png_files
        for base_name in json_without_png:
            os.remove(os.path.join(root, base_name + '.json'))
            print(f"Deleted {os.path.join(root, base_name)} as no corresponding PNG file found.")

# Usage example:
if  os.path.isdir('output'):
	print("cleaning output")
	clean_directory("output")
    remove_desktop_ini_files("output")
if  os.path.isdir('npcs'):
	print("cleaning npcs")
	clean_directory("npcs")
    remove_desktop_ini_files("npcs")
