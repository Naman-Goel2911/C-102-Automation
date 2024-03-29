import shutil
import os
import time

def tempFilesDelete():
    deletedFoldersCount = 0
    deletedFileCount = 0
    days = 7
    seconds = time.time() - (days*24*60*60)
    path = input('Enter the full path to the temp folder: ')

    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):
            if seconds>= getFileOrFolderAge(rootFolder):
                removeFolder(rootFolder)
                deletedFoldersCount += 1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)
                    if seconds >= getFileOrFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFoldersCount += 1

                for file in files:
                    filePath = os.path.join(rootFolder, file)
                    if seconds >= getFileOrFolderAge(filePath):
                        removeFile(filePath)
                        deletedFileCount += 1

        else:
            if seconds>= getFileOrFolderAge(path):
                removeFile(path)
                deletedFileCount += 1   

    else: 
        print(f'{path} is not found.')
        deletedFileCount += 1
        
    print(f'Total Folders deleted: {deletedFoldersCount}')
    print(f'Total Files deleted: {deletedFileCount}')

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

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