import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

class Stackbar:

    color_array = []

    sum = 0
    limit = 0
    limit_num = 0
    date = 0
    sort = 0

    def __init__(self):
        self.file = ''
        self.x = ''

        # array of trace information. will be 2d array. with THREE columns. First column, such as [0][0], is the name of the column in the
        # data. Second column, such as [0][1], is the name to be attached to that line. Third column, [0][2], is the color of the bar
        self.y_array = []
        self.title = ''
        self.x_title = ''
        self.y_title = ''
        self.mean = 0

    # generates Bubblechart using provided data. MUST SET DATA BY ASSIGNING DIRECTLY TO VARIABLES FIRST
    # Call with a 0 to generate a chart by itself, call with a 1 to send to a dashboard
    def generate(self, for_dash):
        # Load CSV file give by File variable
        df = pd.read_csv(self.file)

        # Removing empty spaces to avoid errors
        filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        new_df = filtered_df

        # Creating sum of x and y column group by category Column
        if self.date:
            new_df[self.x] = pd.to_datetime(new_df[self.x])

        # If limit is true, selecting first limit_num entries of y data. Always uses first trace
        if self.limit:
            new_df = new_df.sort_values(by=[self.y_array[0][0]], ascending=[False]).head(self.limit_num)
        if self.sort:
            new_df = new_df.sort_values(by=[self.sortby], ascending=[False])

        new_df2 = new_df
        # Preparing data
        graph_data = []
        for i in range(len(self.y_array)):
            if self.sum:
                new_df2 = new_df.agg({self.y_array[i][0]: 'sum'}).reset_index()
            elif self.mean:
                new_df2 = new_df.agg({self.y_array[i][0]: 'mean'}).reset_index()

            trace = go.Bar(x=new_df[self.x],
                           y=new_df[self.y_array[i][0]],
                           name=self.y_array[i][1],
                           marker={'color': self.y_array[i][2]})
            graph_data.append(trace)

        # if for a dashboard, return graph_data. Otherwise, generate HTML form


            # Preparing layout
            layout = go.Layout(title=self.title, xaxis_title=self.x_title,
                               yaxis_title=self.y_title, barmode='stack')

            # Plot the figure
            fig = go.Figure(data=graph_data, layout=layout)
            if for_dash:
                return fig
            else:
                pyo.plot(fig, filename='stackbarchart.html')


# sets sum boolean to 1, mean to 0. Defaults to 0, so only call this if you need it to be true
    def sum_true(self):
        self.sum = 1
        self.mean = 0

    # sets limit boolean. Defaults to 0, so only call this if you need it to be true
    def limit_true(self, limit_num):
        self.limit = 1
        self.limit_num = limit_num

# sets mean boolean to 1, sum to 0. Defaults to 0, so only call this if you need it to be true
    def mean_true(self):
        self.mean = 1
        self.sum = 0

# sets date boolean to true. Used if X Axis is a collection of dates. This method sets it to true
    def date_true(self):
        self.date = 1

# populates array of trace information. will be 2d array. First column, such as [0][0], is the name of the column in the
# data. Second column, such as [0][1], is the name to be attached to that line. see y_data test in test.py to see more
    def populate_yaxis(self, ydata):
        for x in range(len(ydata)):
            self.y_array.append(ydata[x])

    def sortby(self, column):
        self.sort = 1
        self.sortby = column

    def get_dash_titles(self):
        data = {'Title': self.title,
                'XAxis': self.x_title,
                'YAxis': self.y_title,}
        return data


