# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 22:24:08 2018

@author: ZoeDefreitas
"""
# import data
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime as dt
import csv
#change to 
file_loc = '/Users/jesicasutandi/Documents/Others/SunCode18/'

sunrundata = pd.read_csv(file_loc+ 'b9c5abaa-28bd-4c7b-9632-01ca823fb585.csv')
table = pd.pivot_table(sunrundata, values='timeseriesvalue', index=['srhid', 'timeseriestimestamp'],\
columns=['timeseriesname'])
unique_customer = table.index.get_level_values('srhid').unique()


def determineprice(timestamp):
	datetime_object = timestamp.strftime('2017-04-11 08:30:00', '%Y-%m-%d %hr:%m:%s')
	if (datetime_object.weekday()) in range(0,5):
		if timestamp[11:12].int() in (range(8, 14) or range(20,22)):
			return 0.28
		if timestamp[11:12].int() in range (14, 20):
			return 0.48
		if timestamp[11:12].int() in (range (22, 24) or range(0, 8)):
			return 0.12
	if (timestamp.weekday()) in range (5, 7):	
		if timestamp[11:12].int() in range (8, 22):
			return 0.28
		else:
			return 0.12

print (determineprice('2017-04-11 08:30:00'))


#ratevalues = [determineprice('timeseriestimestamp')]


power_cons = sunrundata[sunrundata['timeseriesname'] == 'powerPurchased']
power_cons_cust1 = power_cons[power_cons['srhid'] == unique_customer[0]]

pricerates = pd.DataFrame({'pricerates': [determineprice(sunrundata.timeseriestimestamp[i])
				 for i in sunrundata.timeseriestimestamp]})
sunrundata = pd.concat([sunrundata, pricerates])


del power_cons_cust1['srhid']
del power_cons_cust1['timeseriesname']
power_cons_cust1 = power_cons_cust1.set_index('timeseriestimestamp')
#power_cons_cust1 = power_cons_cust1.set_index('pricerates')
power_cons_cust1.plot()
print(power_cons_cust1)


#pivot table not working
#table = pd.pivot_table(sunrundata, values='timeseriesvalue', index=['srhid', 'timeseriestimestamp'],\
#columns=['timeseriesname'])
#
#unique_customer = table.index.get_level_values('srhid').unique()
#
#for count, customer in enumerate(unique_customer):
##    table.xs(unique_customer[10])['2017-07-20':'2017-09-22'].plot()
#    customer_data = table.xs(unique_customer[count])
#    customer_data.plot()


#testing clearsky api
import requests
import json
import datetime as dt
import time


start_date = datetime.date(yr,1,1)
start_date_tuple = time.mktime(start_date.timetuple())

s = requests.session()
#r = s.get('https://api.darksky.net/forecast/f7470ac1d48fe6bb06b2afb10dbacfa4/42.3601,-71.0589,255657600?extend=hourly')
r = s.get('https://api.darksky.net/forecast/f7470ac1d48fe6bb06b2afb10dbacfa4/42.3601,-71.0589')

print (json.dumps(r.json(), indent=2))
print (r.content)

wtag_df = pd.DataFrame(r.json())







