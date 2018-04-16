# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:20:04 2018

@author: ZoeDefreitas
"""
import requests
import json
import datetime as dt
import time
import datetime
import pandas as pd

start_date = datetime.date(2017,6,1)
start_date_tuple = time.mktime(start_date.timetuple())
end_date = datetime.date(2017,6,30)
end_date_tuple = time.mktime(end_date.timetuple())

file_loc = 'C:\\Users\\ZoeDefreitas\\Documents\\Collaborations\\suncode2018\\'

site_loc = pd.read_csv(file_loc+'Georeference.csv')

s = requests.session()

for count, customer in enumerate(site_loc):
    lat = site_loc['lat'][count]
    lon = site_loc['lon'][count]
    srhid = site_loc['srhid'][count]
    for t in range(int(start_date_tuple), int(end_date_tuple),86400):
        print t
        r = s.get('https://api.darksky.net/forecast/f7470ac1d48fe6bb06b2afb10dbacfa4/'+str(lat)+','+str(lon)+','+str(t)+'?extend=hourly')
    #r = s.get('https://api.darksky.net/forecast/f7470ac1d48fe6bb06b2afb10dbacfa4/42.3601,-71.0589')
    #    print json.dumps(r.json(), indent=2)
    #    print r.content
        df = pd.DataFrame(r.json()['hourly']['data'])
        if t == int(start_date_tuple):
            df_all = df
        else:
            df_all = pd.concat([df_all,df], axis = 0)

#df_all['time'] = dt.datetime.fromtimestamp(df_all[0]['time']).strftime('%Y-%m-%d %H:%M:%S')
#1811000851
df_all['time'] = pd.to_datetime(df_all['time'],unit='s')
df_all = df_all.set_index('time')
df_all.to_csv('weather'+str(srhid)+'june.csv')

print r.json()['hour]

df_f = pd.DataFrame(r.json()['hourly']['data'])
df_f['time'] = pd.to_datetime(df_f['time'],unit='s')
df_f = df_f.set_index('time')
df_f.to_csv('forecast'+str(srhid)+'june.csv')

with open('data.txt', 'w') as outfile:
    json.dump(r.json(), outfile)