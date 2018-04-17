import sys

for line in sys.stdin:
   f = line.rstrip().split('\t')
   f[2] = str(int(round(float(f[2]))))
   f[3] = str(int(round(float(f[3]))))
   print '\t'.join(f)
