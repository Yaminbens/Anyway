import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import folium
import math
import csv

# pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
# plt.rcParams['figure.figsize'] = (15, 5)

def readCsv():
    df = pd.read_csv('views_2019\involved_hebrew.csv')

# import csv
# with open('views_2019\involved_hebrew.csv', encoding='utf-8', errors='ignore', newline='') as csvfile:
#     linereader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     for row in linereader:
#          print(', '.join(row))
#          1/0

readCsv()