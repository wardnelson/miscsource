# Import the os module, for the os.walk function
import os
import hashlib
import sys

def GetHashOfFile(filename):
    blocksize = 64*1024
    hasher = hashlib.md5()
    
    inf = open(filename, 'rb')
    
    buf = inf.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = inf.read(blocksize)
    inf.close()
    
    return hasher.hexdigest()

 
# Set the directory you want to start from
rootDir = '.'
count = 0
toolbar_width = 100

sys.stderr.write("[%s]" % (" " * toolbar_width))
sys.stderr.flush()
sys.stderr.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for dirName, subdirList, fileList in os.walk(rootDir):

    for fileBaseName in fileList:
        fileNameNoExt, fileExtension = os.path.splitext(fileBaseName)
        fullPathName = '%s\\%s' % (dirName, fileBaseName)
        fileStatInfo = os.stat(fullPathName)

        hashString = GetHashOfFile(fullPathName)

        sys.stderr.write("-")
        sys.stderr.flush()
        

        print('"%s","%s","%s","%s","%s",%d,%s' % (fullPathName, dirName, fileBaseName, fileNameNoExt, fileExtension, fileStatInfo.st_size, hashString))
        count = count + 1

        if (count % 100 == 0):
            sys.stderr.write("[%s]" % (" " * toolbar_width))
            sys.stderr.flush()
            sys.stderr.write("\b" * (toolbar_width+1)) # return to start of line, after '['
            print("count = ", count, file=sys.stderr)
    


