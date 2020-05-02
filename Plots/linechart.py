import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

class Line:
    # limit_num: Holds the number of X entries to limit the dataframe to
    # limit = integer boolean, 1=true=use limit, 0=false=don't use limit
    # sum = integer boolean, 1=true=use sum, 0=false=don't use sum
    # mean = integer boolean, 1=true=use mean, 0=false=don't use mean
    # date = integer boolean for converting x axis to date time
    sum = 0
    limit = 0
    limit_num = 0
    date = 0
    mean = 0


    # Initializes Barchart object and sets the basic variables to empty strings. These variables must be populated in
    # request handler to use this code
    # file = path to csv
    # x = column to use for x axis data
    # y = column to use for y axis data
    # title, x_title, y_title: Titles of graph, x axis, and y axis respectively
    def __init__(self):
        self.file = ''
        self.x = ''
        self.y = ''
        self.title = ''
        self.x_title = ''
        self.y_title = ''


    # generates Linechart using provided data. MUST SET DATA BY ASSIGNING DIRECTLY TO VARIABLES FIRST
    # Call with a 0 to generate a chart by itself, call with a 1 to send to a dashboard
    def generate(self, for_dash):
        # Load CSV file give by File variable
        df = pd.read_csv(self.file)

        # Removing empty spaces to avoid errors
        filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        new_df = filtered_df

        try:
            # Creating sum of x and y column group by category Column
            if self.date:
                new_df[self.x] = pd.to_datetime(new_df[self.x])

        except:
            self.date(0)
            print("Error with Period of Time. Check that X axis is numerical series of time. Generating without Period "
                  "of Time")
            self.generate(for_dash)

        try:
            if self.sum:
                new_df = filtered_df.groupby(self.x)[self.y].sum().reset_index()
            elif self.mean:
                new_df = filtered_df.groupby(self.x)[self.y].mean().reset_index()
        # if error occurs for sum/mean, regenerates after setting sum/mean boolean to false. Prints out error message
        # to console saying why error occuered (Y is not a number)
        except:
            self.sum = 0
            self.mean = 0
            print("Error with Sum/Mean. Check that Y is numerical to use this feature. Generating without Sum/Mean")
            self.generate(for_dash)

        # If limit is true, selecting first limit_num entries of y data
        if self.limit:
            new_df = new_df.sort_values(by=[self.y], ascending=[False]).head(self.limit_num)

        # Preparing data
        graph_data = [go.Scatter(x=new_df[self.x], y=new_df[self.y], mode='lines', name=self.y)]

        # Preparing layout
        layout = go.Layout(title=self.title, xaxis_title=self.x_title,
                           yaxis_title=self.y_title, hovermode='closest')

        # Plot the figure
        fig = go.Figure(data=graph_data, layout=layout)

        if for_dash:
            return fig
        else:
            pyo.plot(fig, filename='linechart.html')


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

    # Gets the titles for dashboard. Usec by RequestHandler to get descriptions for Dashboard
    def get_dash_titles(self):
        data = {'Title': self.title,
                'XAxis': self.x_title,
                'YAxis': self.y_title,}
        return data