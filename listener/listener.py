import shutil
from os import listdir
from os.path import isfile, join
import time

def fileWatcher(sourceDir: str, destDir: str, pollTime: int):
    while True:                
        fileList = fileInDirectory(sourceDir)
        print("Filelist: "+str(fileList))

        if len(fileList) == 0: 
            time.sleep(pollTime)
            continue

        moveNewFiles(fileList, sourceDir, destDir)

#function to return files in a directory
def fileInDirectory(source_dir: str):
    currentFiles = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]
    return(currentFiles)

def moveNewFiles(fileList, sourceDir: str, destDir: str):
    for file in fileList:
        print(file)
        src_path = sourceDir+"/"+file
        print("Moving "+src_path+" To: "+destDir)
        shutil.move(src_path, destDir)

