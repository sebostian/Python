import json
import shutil
import os
import datetime

COMMON_PATHS = "paths"
SOURCE_PATH = "source"
DESTINATION_PATH = "destination"

def copyDirectory(src, dest):
    try:
        print(f"Copying {src} to {dest}")
        shutil.copytree(src, dest, dirs_exist_ok=True)
    # Directories are the same
    except shutil.Error as e:
        print('Directory is not copied. Error: %s' % e)
    # Any error saying that the source directory doesn't exist
    except OSError as e:
        print('Directory is not copied. Error: %s' % e)

def renameIfExists(dest):
    try:
        print(f"Checking directory {dest} exists")
        if os.path.isdir(dest):
            src = "{:%Y_%m_%d_%H_%M_%S}".format(datetime.datetime.now())
            os.rename(dest, f"{dest}_{src}")
    except OSError as e:
        print('Directory is not renamed. Error: %s' % e)

with open("setup.json", "r") as read_file:
    data = json.load(read_file)

source = data[COMMON_PATHS][SOURCE_PATH]
destination = data[COMMON_PATHS][DESTINATION_PATH]

renameIfExists(destination)
copyDirectory(source, destination)