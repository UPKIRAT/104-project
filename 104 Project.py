import csv 
import pandas as pd
import plotly.express as px
from scipy import stats
import numpy as np


with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

n = len(new_data)
total = 0
for x in new_data:
    total += x
mean = total/n

median = np.median(new_data)
mode = stats.mode(new_data)

print('Mean for the data of weights is : ' + str(mean))
print('Median for the data of weights is : ' + str(median))
print('Mode for the data of weights is : ' + str(mode))






