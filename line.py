import pandas as y
import plotly_express as py
v1 = y.read_csv("data.csv")
v2 = py.scatter(v1, x = 'Population', y = 'Per capita', color = 'Country', size = 'Percentage', size_max = 60)
v2.show()