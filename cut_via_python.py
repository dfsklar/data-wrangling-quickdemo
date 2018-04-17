import sys

for line in sys.stdin:
   f = line.rstrip().split('\t')
   print '\t'.join([f[1], f[2], f[5], f[3]])
