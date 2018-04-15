import random
import sys
import pytz
import datetime


with open('leftside.tab', 'r') as myfile:
    for line in myfile:
        fields = line.split('\t')
        out_fields = [ fields[1], fields[2], str(round(float(fields[3]))), str(round(float(fields[4]))) ]
        print '\t'.join(out_fields)
