import pandas as pd
import numpy as np
from Plots.barchart import Barchart
from Plots.bubblechart import Bubblechart
from Plots.heatmap import Heatmap
from Plots.multilinechart import Multiline
from Plots.linechart import Line

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

# Test Barchart
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


# Test Bubblechart
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


# Test heatmap

# testchart = Heatmap()
# testchart.title = "test"
# testchart.file = '../Datasets/CoronaTimeSeries.csv'
# testchart.x = 'Day'
# testchart.y = 'WeekofMonth'
# testchart.z = 'Recovered'
# testchart.title = "Recovered"
# testchart.x_title = "Day of Week"
# testchart.y_title = "Week of Month"
# testchart.generate(0)

ydata = [["column1","test"], ["column2", "test2"], ["column3", "test3"]]
y_array = []

for x in range(len(ydata)):
    y_array.append(ydata[x])

print(y_array)
print(y_array[0][0])



example_dict = {"title": "test title", "xtitle": ""}

bar_data = {"file": '', "x": '', }

example_dict["xtitle"] = "dict entry"

print(example_dict["title"])
print(example_dict["xtitle"])

# # test multiline
# #
# # testmulti = Multiline()
# # testmulti.title = "test"
# # testmulti.file = '../Datasets/CoronaTimeSeries.csv'
# # testmulti.x = 'Date'
# # testmulti.date_true()
# # ytest = [["Death", "Death"],["Recovered", "Recovered"],["Unrecovered", "Unrecovered"]]
# # testmulti.populate_yaxis(ytest)
# # testmulti.x_title = "Date"
# # testmulti.y_title = "Number of cases"
# # testmulti.generate(0)

# # test multiline

testline = Line()
testline.title = "test"
testline.file = '../Datasets/CoronaTimeSeries.csv'
testline.x = 'Date'
testline.date_true()
testline.y = 'Confirmed'
testline.x_title = "Date"
testline.y_title = "Number of cases"
testline.generate(0)