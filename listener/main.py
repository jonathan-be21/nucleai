import os
import listener

sourceDir = os.getenv("SOURCE_FOLDER_PATH")
destDir = os.getenv("DEST_FOLDER_PATH")
pollTime = 5

if sourceDir != None and destDir != None:
    try:
        print("Watching the folder: "+sourceDir)
        listener.fileWatcher(sourceDir, destDir, pollTime)
    except TypeError as e:
        print("Something went wrong: "+e)

