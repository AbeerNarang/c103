import pandas as x
import plotly_express as px
v1 = x.read_csv("data.csv")
v2 = px.bar(v1, x = 'Country', y = 'InternetUsers')
v2.show()
