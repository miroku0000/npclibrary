import os
import json
from collections import defaultdict
import shutil

         
# Define the directory for reading the data and for writing the HTML files
data_directory = "npcs"
output_directory = "npcs"


# Delete any existing HTML files in the output directory
for file in os.listdir(output_directory):
    if file.endswith(".html"):
        os.remove(os.path.join(output_directory, file))

