import shutil
import os

def tempFilesDelete():
    path = input('Enter the full path to the temp folder: ')

    if(os.path.exists(path)):
        for folders, files in os.walk(path):

            for folder in folders:
                folderPath = os.path.join(path, folder)
                removeFolder(folderPath)

            for file in files:
                filePath = os.path.join(path, file)
                name, ext = os.path.splitext(file)
                ext = ext[1:]
                if(ext == 'temp'):
                    removeFile(filePath)    
    else:
        print('Oops, the path is wrong.')

def removeFolder(path):
    if not shutil.rmtree(path):
        print(path, ' is removed successfully!')

    else: 
        print('Unable to delete', path)

def removeFile(path):
    if not os.remove(path):
        print(path+'has been removed successfully!')
    else:
        print('Unable to delete ', path)

tempFilesDelete()