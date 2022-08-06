from email import header
import pandas as pd
from csv import reader
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
from datetime import datetime
import numpy as np
import math

header = ['DATE', 'Producer Price Index(By  Industry in $)', 'No. of employed peoples in semiconductor industry', 'Industrial Production: Non-Energy Excluding Motor Vehicles & Parts, Computers, Communications Equipment, and Semiconductors', 'Relative Importance Weights (Contribution to the Total Industrial Production Index WISE)']
df = pd.read_csv('/Users/adriancarranza/Documents/finalCloudProject/Semiconductor_shortage_affects.csv')
#print (df)

df['DATE'] = df['DATE'].map(lambda x: datetime.strptime(str(x), '%m-%d-%Y'))

x = df['DATE']
y = df['Producer Price Index(By  Industry in $)']
y1 = df['No. of employed peoples in semiconductor industry']
y2 = df['Industrial Production: Non-Energy Excluding Motor Vehicles & Parts, Computers, Communications Equipment, and Semiconductors']
y3= df['Relative Importance Weights (Contribution to the Total Industrial Production Index WISE)']

figure, axis = plt.subplots(2, 2)
plt.gcf().autofmt_xdate()
axis[0, 0].plot(x, y)
axis[0, 0].set_title("Price per Year")

axis[0, 1].plot(x, y1)
axis[0, 1].set_title("People Employed in Field")

axis[1, 0].plot(x, y2)
axis[1, 0].set_title("Import Price")

axis[1, 1].plot(x, y3)
axis[1, 1].set_title("Total Industrial Production Index WISE")


plt.show()




