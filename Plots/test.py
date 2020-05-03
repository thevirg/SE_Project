import pandas as pd
import numpy as np
from Plots.barchart import Barchart
from Plots.bubblechart import Bubblechart
from Plots.heatmap import Heatmap
from Plots.multilinechart import Multiline
from Plots.linechart import Line
from Plots.stackbarchart import Stackbar

test_bool = 0
df2 = pd.read_csv('../Datasets/Olympic2016Rio.csv', usecols=['NOC'])
# print(df2)
# array_test = df2.to_numpy()

# test = []
# for x in range(0,df.size):
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
#

# Test Bubblechart

# testbubble = Bubblechart()
# testbubble.title = "test"
# testbubble.file = '../Datasets/Olympic2016Rio.csv'
# testbubble.limit_true(20)
# testbubble.x = 'Total'
# testbubble.y = 'Gold'
# testbubble.marker_data = 'Total'
# testbubble.category = 'NOC'
# testbubble.title = "Olympics"
# testbubble.x_title = "Total Medal"
# testbubble.y_title = "Gold Medals"
# testbubble.bubble_scale = 1
# testbubble.generate(0)


# Test heatmap

# testheat = Heatmap()
# testheat.title = "test"
# testheat.file = '../Datasets/CoronaTimeSeries.csv'
# testheat.x = 'Day'
# testheat.y = 'WeekofMonth'
# testheat.z = 'Recovered'
# testheat.title = "Recovered"
# testheat.x_title = "Day of Week"
# testheat.y_title = "Week of Month"
# testheat.generate(0)
#
# ydata = [["column1","test"], ["column2", "test2"], ["column3", "test3"]]
# y_array = []
#
# for x in range(len(ydata)):
#     y_array.append(ydata[x])
#
# print(y_array)
# print(y_array[0][0])
#
#
example_dict = {"title": {"test": [["a","z"],"b","c"]}, "xtitle": ""}

bar_data = {"file": '', "x": '', }

example_dict["xtitle"] = "dict entry"

print(example_dict["title"]["test"][0][1])
# print(example_dict["xtitle"])

#
# # # test multiline
# # #
# # # testmulti = Multiline()
# # # testmulti.title = "test"
# # # testmulti.file = '../Datasets/CoronaTimeSeries.csv'
# # # testmulti.x = 'Date'
# # # testmulti.date_true()
# # # ytest = [["Death", "Death"],["Recovered", "Recovered"],["Unrecovered", "Unrecovered"]]
# # # testmulti.populate_yaxis(ytest)
# # # testmulti.x_title = "Date"
# # # testmulti.y_title = "Number of cases"
# # # testmulti.generate(0)
#
# # # test multiline
# #
# # testline = Line()
# # testline.title = "test"
# # testline.file = '../Datasets/CoronaTimeSeries.csv'
# # testline.x = 'Date'
# # testline.date_true()
# # testline.y = 'Confirmed'
# # testline.x_title = "Date"
# # testline.y_title = "Number of cases"
# # testline.generate(0)
#
# # test stack bar
#
# teststack = Stackbar()
# teststack.title = "test"
# teststack.file = '../Datasets/Olympic2016Rio.csv'
# teststack.x = 'NOC'
# ytest = [["Gold", "Gold", '#ffff00'],["Silver", "Silver", '#cccccc'],["Bronze", "Bronze", '#cc9900']]
# teststack.populate_yaxis(ytest)
# teststack.x_title = "Medals"
# teststack.y_title = "Number of cases"
# teststack.limit_true(20)
# teststack.sum_true()
# teststack.generate(0)

# test = "1"
# print(int(test))
# string = "test" + str(int(test)+1)
#
#
# if int(test) == 1:
#     print(string)


# testarray = []
# testarray.append(["a","b"])
# print(testarray)
# print(testarray[0][0])


def test1():
    testarray = [1,2]
    test2(testarray)

    print(testarray)

def test2(array):
    array[0] = 5
    array[1] = 7

test1()