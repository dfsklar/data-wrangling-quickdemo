import random
import sys
import pytz
import datetime


start_time = datetime.datetime(2018, 04, 11, 0, 0, 0, 0)  #, pytz.timezone('UTC'))
day_start = int(start_time.strftime("%s"))  - (4 * 60 * 60)


station_ids = [ 2348, 2892, 9892, 7724, 11421, 88948, 347274, 988472,
                82348, 82892, 89892, 87724, 811421, 888948, 8347274, 8988472 
 ]

date = '2018-04-11'

for id in station_ids:
    sec_in_day = 0
    while sec_in_day < (24 * 60 * 60):
        temp = 56 + random.random() * 20;
        humidity = 36 + random.random() * 40;
        barom = 1000 + random.random() * 15;

        print date + '\t' + datetime.datetime.utcfromtimestamp(day_start+sec_in_day).strftime('%H:%M:%S') + '\t' + str(id) + '\t' + str(humidity) + '\t' + str(barom) + '\t' + str(temp)
        sec_in_day += 1

    


