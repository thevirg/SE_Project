import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go




class Barchart:

    # limit_num: Holds the number of X entries to limit the dataframe to
    # limit = integer boolean, 1=true=use limit, 0=false=don't use limit
    # sum = integer boolean, 1=true=use sum, 0=false=don't use sum
    # mean = integer boolean, 1=true=use mean, 0=false=don't use mean
    limit_num = 0
    limit = 0
    sum = 0
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

    # generates Barchart using provided data. MUST SET DATA BY ASSIGNING DIRECTLY TO VARIABLES FIRST
    # Call with a 0 to generate a chart by itself, call with a 1 to send to a dashboard
    def generate(self, for_dash):
        # Load CSV file give by File variable
        df = pd.read_csv(self.file)

        # Removing empty spaces to avoid errors
        filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        new_df = filtered_df
        try:
            # Creating sum or mean of Y column group by X Column if boolean set
            if self.sum:
                new_df = filtered_df.groupby(self.x)[self.y].sum().reset_index()
            elif self.mean:
                new_df = filtered_df.groupby(self.x)[self.y].mean().reset_index()
            # Sorting values and select first limit_num entries
        except:
            # if error occurs for sum/mean, regenerates after setting sum/mean boolean to false. Prints out error message
            # to console saying why error occuered (y is not a number)
            self.sum = 0
            self.mean = 0
            print("Error with Sum/Mean. Check that passed Y is numerical")
            self.generate(for_dash)

        if self.limit:
            new_df = new_df.sort_values(by=[self.y], ascending=[False]).head(self.limit_num)

        # Preparing data
        graph_data = [go.Bar(x=new_df[self.x], y=new_df[self.y])]

        # if for a dashboard, return graph_data. Otherwise, generate HTML form

        # Preparing layout
        layout = go.Layout(title=self.title, xaxis_title=self.x_title,
                           yaxis_title=self.y_title)

        # Plot the figure

        fig = go.Figure(data=graph_data, layout=layout)
        if for_dash:
            return fig
        else:
            pyo.plot(fig, filename='barchart.html')

    # sets variables in data[]. Variables can be acceessed directly from object, but this allows implementation of
    # additional uses without having to know how dictionary is structured

    # sets sum boolean. Defaults to 0, so only call this if you need it to be true
    def sum_true(self):
        self.sum = 1

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
                'YAxis': self.y_title}
        return data