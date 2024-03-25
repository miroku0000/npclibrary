import os
import sys

def count_files(directory):
    """
    Count the number of files in a directory.
    """
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

def find_directory_with_least_files(root_directory, search_pattern):
    """
    Find the subdirectory with the least number of files containing the search pattern.
    """
    subdirectories = [d for d in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, d)) and search_pattern in d]
    min_files = float('inf')
    min_files_directory = None

    for subdir in subdirectories:
        subdir_path = os.path.join(root_directory, subdir)
        num_files = count_files(subdir_path)
        if num_files < min_files:
            min_files = num_files
            min_files_directory = subdir_path

    return min_files_directory

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <search_pattern>")
        sys.exit(1)

    search_pattern = sys.argv[1]
    root_directory = "npcs"  # Change this to your desired root directory
    result_directory = find_directory_with_least_files(root_directory, search_pattern)
    if result_directory:
        print("'{}':".format(search_pattern), result_directory)
    else:
        print("No directories found containing pattern '{}'.".format(search_pattern))
