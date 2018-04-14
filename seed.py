import csv
from database import session, Dataset, PowerProduction#, BatteryPercentageState, PowerFeedIn, PowerSelfConsumption, PowerPurchased, PowerConsumption

dataset = Dataset()

filepath = 'b9c5abaa-28bd-4c7b-9632-01ca823fb585.csv'  
with open(filepath) as fp:  
  line = fp.readline()
  cnt = 1
  while line:
    print("Line {}: {}".format(cnt, line.strip()))
    line = fp.readline()
    cnt += 1
