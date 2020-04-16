import pandas as pd
import numpy as np
from Plots.barchart import Barchart
from Plots.bubblechart import Bubblechart
from Plots.heatmap import Heatmap

test_bool = 0
df2 = pd.read_csv('../Datasets/Olympic2016Rio.csv', usecols=['NOC'])
# print(df2)
# array_test = df2.to_numpy()

# test = []
# for x in range(0,df2.size):
#     test.append({'label': df2.iloc[x]['NOC'], 'value': df2.iloc[x]['NOC']})
#
# print(test)
#
# if test_bool:
#     print("1 is true")
# else:
#     print("0 is false")
#
# testbar = Barchart()
# testbar.title = 'test'
# print(testbar.title)
#
# noc = 'NOC'
#
#
# print(df2['NOC'])
# print(df2[noc])

# #Test Barchart
# testchart = Barchart()
# testchart.title = "test"
# testchart.file = '../Datasets/Olympic2016Rio.csv'
# testchart.limit_true(20)
# testchart.sum_true()
# testchart.x = 'NOC'
# testchart.y = 'Total'
# testchart.title = "Olympics"
# testchart.x_title = "Country"
# testchart.y_title = "Total Medals"
# testchart.generate(0)


# #Test Bubblechart
# testchart = Bubblechart()
# testchart.title = "test"
# testchart.file = '../Datasets/Olympic2016Rio.csv'
# testchart.limit_true(20)
# testchart.x = 'Total'
# testchart.y = 'Gold'
# testchart.marker_data = 'Total'
# testchart.category = 'NOC'
# testchart.title = "Olympics"
# testchart.x_title = "Total Medal"
# testchart.y_title = "Gold Medals"
# testchart.bubble_scale = 1
# testchart.generate(0)

#Test Barchart
testchart = Heatmap()
testchart.title = "test"
testchart.file = '../Datasets/CoronaTimeSeries.csv'
testchart.x = 'Day'
testchart.y = 'WeekofMonth'
testchart.z = 'Recovered'
testchart.title = "Recovered"
testchart.x_title = "Day of Week"
testchart.y_title = "Week of Month"
testchart.generate(0)