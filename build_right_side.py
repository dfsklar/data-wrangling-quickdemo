import random
import sys
import pytz
import datetime


with open('leftside.tab', 'r') as myfile:
    for line in myfile:
        fields = line.split('\t')
        var1 = random.random() * 0.15;
        var2 = random.random() * 0.15;
        out_fields = [ fields[1], fields[2], str(int(round(var1+float(fields[3])))), str(int(round(var2+float(fields[5])))) ]
        print '\t'.join(out_fields)
