import hashlib
import sys
import argparse
BLOCKSIZE = 64*1024 

parser = argparse.ArgumentParser(description='Calculate a Hash of the file passed in')
parser.add_argument('-f', '--file', nargs='?', help='file to calulate a hash of')
parser.add_argument('-b', '--blocksize', nargs='?', type=int, help='block size to use when reading file')
args = parser.parse_args()

if (args.blocksize):
    BLOCKSIZE = args.blocksize;

# use stdin if there wasn't a file passed in
if args.file:
    inf = open(args.file, 'rb')
else:
    inf = sys.stdin.buffer.raw

hasher = hashlib.md5()
if 1:
    buf = inf.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = inf.read(BLOCKSIZE)
else: 
    buf = inf.read()
    hasher.update(buf)

print(hasher.hexdigest())


if inf is not sys.stdin:
    inf.close()

