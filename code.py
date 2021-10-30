import plotly.express as px
import csv
import numpy as np 

def getDataSource(data_path):
    Marks_In_Percentage = []
    Days_Present = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))
    
    return{"x": Marks_In_Percentage, "y": Days_Present}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0,1])

def plotFigure(data_path):
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        fig = px.scatter(csv_reader, x = "Days Present", y = "Marks In Percentage")
        fig.show()

def setup():
    data_path = "students.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source) 
    plotFigure(data_path)

setup()