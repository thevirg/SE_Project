import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go




class Barchart:
    limit_num = 0
    limit = 0
    sum = 0

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
        # Creating sum of Y column group by X Column
        if self.sum:
            new_df = filtered_df.groupby(self.x)[self.y].sum().reset_index()

        # Sorting values and select first limit_num entries
        if self.limit:
            new_df = new_df.sort_values(by=[self.y], ascending=[False]).head(self.limit_num)

        # Preparing data
        graph_data = [go.Bar(x=new_df[self.x], y=new_df[self.y])]

        # if for a dashboard, return graph_data. Otherwise, generate HTML form
        if for_dash:
            return graph_data
        else:

            # Preparing layout
            layout = go.Layout(title=self.title, xaxis_title=self.x_title,
                               yaxis_title=self.y_title)

            # Plot the figure
            fig = go.Figure(data=graph_data, layout=layout)
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

    def get_dash_titles(self):
        data = {'Title': self.title,
                'XAxis': self.x_title,
                'YAxis': self.y_title}
        return data