import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from numbers import Number

class Bubblechart:
    sum = 0
    limit = 0
    limit_num = 0


    # Initializes Barchart object and sets the basic variables to empty strings. These variables must be populated in
    # request handler to use this code
    # file = path to csv
    # x = column to use for x axis data. must be a positive number
    # y = column to use for y axis data. must be a positive number
    # title, x_title, y_title: Titles of graph, x axis, and y axis respectively
    # category = sets the column of data to use for bubble names/rows for marker_data.
    # maker_data = sets the column of data to use for bubble size/marker data. must be a positive number
    # bubble scale = currently unused, sets the scale to divide marker_data by
    def __init__(self):
        self.file = ''
        self.x = ''
        self.y = ''
        self.title = ''
        self.x_title = ''
        self.y_title = ''
        self.category = ''
        self.mean = 0
        self.marker_data = ''

        # sets the scale to be used for the bubbles.
        # 1 means data will be used as is, 10 means scale will be divided by 10, etc
        self.bubble_scale = 1

    # generates Bubblechart using provided data. MUST SET DATA BY ASSIGNING DIRECTLY TO VARIABLES FIRST
    # Call with a 0 to generate a chart by itself, call with a 1 to send to a dashboard
    def generate(self, for_dash):
        # Load CSV file give by File variable
        df = pd.read_csv(self.file)

        # Removing empty spaces to avoid errors
        filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        new_df = filtered_df

        try:

            # Creating sum of x and y column group by category Column
            if self.sum:
                new_df = filtered_df.groupby([self.category]).agg({self.x: 'sum', self.y: 'sum', self.marker_data: 'sum'}).reset_index()
            elif self.mean:
                new_df = filtered_df.groupby([self.category]).agg({self.x: 'mean', self.y: 'mean', self.marker_data: 'mean'}).reset_index()
            # If limit is true, selecting first limit_num entries of y data
            if self.limit:
                new_df = new_df.sort_values(by=[self.y], ascending=[False]).head(self.limit_num)

        # if error occurs for sum/mean, regenerates after setting sum/mean boolean to false. Prints out error message
        # to console saying why error occuered (y,x, marker is not a number)

        except:
            self.sum = 0
            self.mean = 0
            print("Error with Sum/Mean. Current implementation requires X, Y, and Marker data to be numerical for this "
                  "feature. Generating without Sum/Mean.")
            self.generate(for_dash)

        # Checks that marker is both a number and positive. Displays error message if either is false, as category
        # must contain only positive numbers
        marker_check = new_df.get(self.marker_data)
        for x in marker_check:
            if not isinstance(x, Number):
                print("Passed value is not a number. Category must hold numbers between [0,inf]")
                return
            elif x < 0:
                print("Passed category contains negative numbers. Category must hold numbers between [0,inf]")
                return

        # Checks that category is both a number and positive. Displays error message if either is false, as category
        # must contain only positive numbers

        category_check = new_df.get(self.category)
        for x in category_check:
            if not isinstance(x, Number):
                print("Passed value is not a number. Category must hold numbers between [0,inf]")
                return
            elif x < 0:
                print("Passed category contains negative numbers. Category must hold numbers between [0,inf]")
                return

        # Preparing data
        graph_data = [go.Scatter(x=new_df[self.x], y=new_df[self.y], text=new_df[self.category], mode='markers',
                   marker=dict(size=new_df[self.marker_data] / self.bubble_scale,
                               color=new_df[self.marker_data] / self.bubble_scale, showscale=True))]

        # Preparing layout
        layout = go.Layout(title=self.title, xaxis_title=self.x_title,
                           yaxis_title=self.y_title, hovermode='closest')

        # Plot the figure
        fig = go.Figure(data=graph_data, layout=layout)
        if for_dash:
            return fig
        else:
            pyo.plot(fig, filename='bubblechart.html')


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

# Gets the titles for dashboard. Usec by RequestHandler to get descriptions for Dashboard
    def get_dash_titles(self):
        data = {'Title': self.title,
                'XAxis': self.x_title,
                'YAxis': self.y_title,}
        return data

