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

#change to 
file_loc = 'C:\Users\ZoeDefreitas\Documents\Collaborations\suncode2018\'

sunrundata = pd.read_csv(file_loc+'suncodeTSdata\\b9c5abaa-28bd-4c7b-9632-01ca823fb585.csv')
unique_customer = table.index.get_level_values('srhid').unique()

power_cons = sunrundata[sunrundata['timeseriesname'] == 'powerConsumption']
power_cons_cust1 = power_cons[power_cons['srhid'] == unique_customer[0]]

del power_cons_cust1['srhid']
del power_cons_cust1['timeseriesname']
power_cons_cust1 = power_cons_cust1.set_index('timeseriestimestamp')
power_cons_cust1.plot()

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
import datetime

start_date = datetime.date(iyr,1,1)
start_date_tuple = time.mktime(start_date.timetuple())

s = requests.session()
r = s.get('https://api.darksky.net/forecast/f7470ac1d48fe6bb06b2afb10dbacfa4/42.3601,-71.0589,255657600?extend=hourly')
r = s.get('https://api.darksky.net/forecast/f7470ac1d48fe6bb06b2afb10dbacfa4/42.3601,-71.0589')

print json.dumps(r.json(), indent=2)
print r.content

wtag_df = pd.DataFrame(r.json())







