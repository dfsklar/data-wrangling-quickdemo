import random
import sys
import pytz
import datetime


start_time = datetime.datetime(2018, 04, 11, 0, 0, 0, 0)  #, pytz.timezone('UTC'))
day_start = int(start_time.strftime("%s"))  - (4 * 60 * 60)



station_ids = [ 15, 348, 3892, 7724, 84721 ]

date = '2018-04-11'

for id in station_ids:
    sec_in_day = 0
    while sec_in_day < (24 * 60 * 60):
        temp = 56 + random.random() * 20;
        humidity = 36 + random.random() * 40;

        print date + '\t' + datetime.datetime.utcfromtimestamp(day_start+sec_in_day).strftime('%H:%M:%S') + '\t' + str(id) + '\t' + str(humidity) + '\t' + str(temp)
        sec_in_day += 60 * 5


    


