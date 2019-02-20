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
rootDir = 'c:/temp'
count = 0
toolbar_width = 100

sys.stderr.write("[%s]" % (" " * toolbar_width))
sys.stderr.flush()
sys.stderr.write("\b" * (toolbar_width+1)) # return to start of line, after '['

outstring = ''
fillchar = '-'

for dirName, subdirList, fileList in os.walk(rootDir):

    for fileBaseName in fileList:
        fileNameNoExt, fileExtension = os.path.splitext(fileBaseName)
        fullPathName = os.path.join(dirName, fileBaseName)
        fileStatInfo = os.stat(fullPathName)

        hashString = GetHashOfFile(fullPathName)

        sys.stderr.write(fillchar)
        sys.stderr.flush()
        
        outstring += '"{}","{}","{}","{}","{}",{},{}\n'.format(fullPathName, dirName, fileBaseName, fileNameNoExt, fileExtension, fileStatInfo.st_size, hashString)

        count = count + 1

        if (count % 100 == 0):
            if (fillchar == '-'):
                fillchar = ' '
            else :
                fillchar = '-'
            sys.stderr.write("\b" * (toolbar_width)) # return to start of line, after '['
            sys.stderr.flush()
            #sys.stderr.write("[%s]" % ("-" * toolbar_width))
            #print("count = ", count, file=sys.stderr)
sys.stderr.write("\n")
sys.stderr.flush()
    

print(outstring)


