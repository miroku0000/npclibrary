import os
import json
from collections import defaultdict

output_directory="npcs"

def rename_dirs_to_lowercase(path):
    """
    Rename all subdirectories within the given path to lowercase.
    
    Args:
    - path (str): The path to the directory whose subdirectories will be renamed.
    """
    # Iterate over the items in the directory
    for name in os.listdir(path):
        # Full path of the item
        full_path = os.path.join(path, name)
        
        # Check if the item is a directory
        if os.path.isdir(full_path):
            # Generate the lowercase version of the full path
            new_full_path = os.path.join(path, name.lower())
            
            # Rename the directory if the new name is different
            if new_full_path != full_path:
                os.rename(full_path, new_full_path)
                print(f"Renamed '{full_path}' to '{new_full_path}'")

def remove_empty_subdirs(dir_path):
    try:
        # Walk through all subdirectories in the given directory
        for root, dirs, files in os.walk(dir_path, topdown=False):
            for dir_name in dirs:
                # Construct the full path to the directory
                full_dir_path = os.path.join(root, dir_name)
                
                # Check if the directory is empty
                if not os.listdir(full_dir_path):
                    # Remove the empty directory
                    os.rmdir(full_dir_path)
                    print(f"Removed empty directory: {full_dir_path}")
    except:
        pass

# Delete any existing HTML files in the output directory
for file in os.listdir(output_directory):
    if file.endswith(".html"):
        os.remove(os.path.join(output_directory, file))

rename_dirs_to_lowercase(output_directory)
remove_empty_subdirs(output_directory)
