import csv
from datetime import datetime
from database import session, Dataset, PowerProduction, BatteryPercentageState, PowerFeedIn, PowerSelfConsumption,\
    PowerPurchased, PowerConsumption

dataset = Dataset()

#session.query(Dataset).filter_by(name = 'josh').first().name

filepath = 'b9c5abaa-28bd-4c7b-9632-01ca823fb585.csv'  
with open(filepath) as fp:  
  line = fp.readline()
  cnt = 1
  while line:
    sp = line.strip().split(",")
    if sp[1] == '"timeseriestimestamp"':
      print('starting')
    else:
      name = sp[0].replace('"', '')
      timestamp = datetime.strptime(sp[1].replace('"', ''), '%Y-%m-%d %H:%M:%S')
      seriesname = sp[2].replace('"', '')
      seriesvalue = sp[3].replace('"', '')

      n = session.query(Dataset).filter_by(name=name).first()

      if n:
        print(n.name)
      else:
        n = Dataset()
        n.name = name
        session.add(n)
      
      if seriesname == 'powerProduction':
        pp = PowerProduction(timeseriesvalue=seriesvalue, time=timestamp)
        n.power_productions.append(pp)
      elif seriesname == 'batteryPercentageState':
        pp = BatteryPercentageState(timeseriesvalue=seriesvalue, time=timestamp)
        n.battery_percentage_states.append(pp)
      elif seriesname == 'powerFeedIn':
        pp = PowerFeedIn(timeseriesvalue=seriesvalue, time=timestamp)
        n.power_feed_ins.append(pp)
      elif seriesname == 'powerSelfConsumption':
        pp = PowerSelfConsumption(timeseriesvalue=seriesvalue, time=timestamp)
        n.power_self_consumptions.append(pp)
      elif seriesname == 'powerPurchased':
        pp = PowerPurchased(timeseriesvalue=seriesvalue, time=timestamp)
        n.power_purchaseds.append(pp)
      elif seriesname == 'powerConsumption':
        pp = PowerConsumption(timeseriesvalue=seriesvalue, time=timestamp)
        n.power_consumptions.append(pp)
      else:
        print('couldnt find it') 
      session.commit()
      #session.close()
    line = fp.readline()
    cnt += 1
