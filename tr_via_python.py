import sys

for line in sys.stdin:
   f = line.rstrip().split('\001')
   print '\t'.join(f)
