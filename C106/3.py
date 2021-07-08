import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    size_of_tv = []
    avg_time_spend = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row['Size of TV']))
            avg_time_spend.append(float(row['\tAverage time spent watching TV in a week (hours)']))
    return {'x':size_of_tv,'y':avg_time_spend}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print("Correlation is  : ",correlation[0,1])

def setup():
    data_path = 'data/size of tv vs avg time spend.csv'
    data_source = getDataSource(data_path)
    find_correlation(data_source)

setup()

