import os

def remove_desktop_ini_files(directory_path):
    """
    Removes 'desktop.ini' files from the specified directory and its subdirectories.
    """
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower() == "desktop.ini":
                os.remove(os.path.join(root, file))
                print(f"Removed: {os.path.join(root, file)}")

def clean_directory(directory):
    """
    Cleans the specified directory by deleting PNG files without a corresponding JSON file,
    and vice versa.
    """
    for root, dirs, files in os.walk(directory):
        png_files = {os.path.splitext(f)[0] for f in files if f.endswith('.png')}
        json_files = {os.path.splitext(f)[0] for f in files if f.endswith('.json')}

        # Find PNG files without a corresponding JSON file and delete them
        png_without_json = png_files - json_files
        for base_name in png_without_json:
            os.remove(os.path.join(root, base_name + '.png'))
            print(f"Deleted {os.path.join(root, base_name + '.png')} as no corresponding JSON file found.")

        # Find JSON files without a corresponding PNG file and delete them
        json_without_png = json_files - png_files
        for base_name in json_without_png:
            os.remove(os.path.join(root, base_name + '.json'))
            print(f"Deleted {os.path.join(root, base_name + '.json')} as no corresponding PNG file found.")

if os.path.isdir('output'):
    print("Cleaning 'output' directory.")
    clean_directory("output")
    remove_desktop_ini_files("output")

if os.path.isdir('npcs'):
    print("Cleaning 'npcs' directory.")
    clean_directory("npcs")
    remove_desktop_ini_files("npcs")
