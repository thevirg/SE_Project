import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


class Bubblechart:
    sum = 0
    limit = 0
    limit_num = 0

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
        self.bubble_scale = 1

    # generates Bubblechart using provided data. MUST SET DATA BY ASSIGNING DIRECTLY TO VARIABLES FIRST
    # Call with a 0 to generate a chart by itself, call with a 1 to send to a dashboard
    def generate(self, for_dash):
        # Load CSV file give by File variable
        df = pd.read_csv(self.file)

        # Removing empty spaces to avoid errors
        filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        new_df = filtered_df

        # Creating sum of x and y column group by category Column
        if self.sum:
            new_df = filtered_df.groupby([self.category]).agg({self.x: 'sum', self.y: 'sum', self.marker_data: 'sum'}).reset_index()
        elif self.mean:
            new_df = filtered_df.groupby([self.category]).agg({self.x: 'mean', self.y: 'mean', self.marker_data: 'mean'}).reset_index()
        # If limit is true, selecting first limit_num entries of y data
        if self.limit:
            new_df = new_df.sort_values(by=[self.y], ascending=[False]).head(self.limit_num)

        # Preparing data
        graph_data = [go.Scatter(x=new_df[self.x], y=new_df[self.y], text=new_df[self.category], mode='markers',
                   marker=dict(size=new_df[self.marker_data] / self.bubble_scale,
                               color=new_df[self.marker_data] / self.bubble_scale, showscale=True))]

        # if for a dashboard, return graph_data. Otherwise, generate HTML form
        if for_dash:
            return graph_data
        else:

            # Preparing layout
            layout = go.Layout(title=self.title, xaxis_title=self.x_title,
                               yaxis_title=self.y_title, hovermode='closest')

            # Plot the figure
            fig = go.Figure(data=graph_data, layout=layout)
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

    def get_dash_titles(self):
        data = {'Title': self.title,
                'XAxis': self.x_title,
                'YAxis': self.y_title,}
        return data

