import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row['Temperature']))
            cold_drink_sales.append(float(row['Ice-cream Sales']))
    return {'x':ice_cream_sales,'y':cold_drink_sales}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print("Correlation between temperature and ice cream sale is : ",correlation[0,1])

def setup():
    data_path = 'data/temperature vs ice cream.csv'
    data_source = getDataSource(data_path)
    find_correlation(data_source)

setup()

