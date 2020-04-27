from Plots.bubblechart import Bubblechart
from Plots.barchart import Barchart
from Plots.stackbarchart import Stackbar
from Plots.linechart import Line
from Plots.multilinechart import Multiline
from Plots.heatmap import Heatmap
import Plots.Dashboard as d

def request_bar(chart_data, for_dash):
    chart = Barchart()
    chart.title = chart_data['title']
    chart.x = chart_data['x']
    chart.y = chart_data['y']
    chart.file = chart_data['file']
    chart.x_title = chart_data['x_title']
    chart.y_title = chart_data['y_title']

    if chart_data['sum'] == 1:
        chart.sum_true()
    elif chart_data['mean'] == 1:
        chart.mean_true()

    if chart_data['limit'] == 1:
        chart.limit_true(chart_data['limit_num'])

    if for_dash:
        fig = chart.generate(1)
        desc = chart.get_dash_titles()
        return fig, desc
    else:
        chart.generate(0)


def request_stack(chart_data, for_dash):
    chart = Stackbar()
    chart.title = chart_data['title']
    chart.x = chart_data['x']

    # pulls the y array from the passed dict. For multiline and stack bar, the 'y' value in the dict must be an array
    # as per the populate_yaxis comments
    chart.populate_yaxis(chart_data['y'])

    chart.file = chart_data['file']
    chart.x_title = chart_data['x_title']
    chart.y_title = chart_data['y_title']

    if chart_data['sum'] == 1:
        chart.sum_true()
    elif chart_data['mean'] == 1:
        chart.mean_true()

    if chart_data['limit'] == 1:
        chart.limit_true(chart_data['limit_num'])

    if chart_data['sort'] == 1:
        chart.sort_by(chart_data['sortby'])

    if chart_data['date'] == 1:
        chart.date_true()

    if for_dash:
        fig = chart.generate(1)
        desc = chart.get_dash_titles()
        return fig, desc
    else:
        chart.generate(0)


def request_multi(chart_data, for_dash):

    chart = Multiline()
    chart.title = chart_data['title']
    chart.x = chart_data['x']

    # pulls the y array from the passed dict. For multiline and stack bar, the 'y' value in the dict must be an array
    # as per the populate_yaxis comments
    chart.populate_yaxis(chart_data['y'])

    chart.file = chart_data['file']
    chart.x_title = chart_data['x_title']
    chart.y_title = chart_data['y_title']

    if chart_data['sum'] == 1:
        chart.sum_true()
    elif chart_data['mean'] == 1:
        chart.mean_true()

    if chart_data['limit'] == 1:
        chart.limit_true(chart_data['limit_num'])

    if chart_data['date'] == 1:
        chart.date_true()

    if for_dash:
        fig = chart.generate(1)
        desc = chart.get_dash_titles()
        return fig, desc
    else:
        chart.generate(0)


def request_line(chart_data, for_dash):

    chart = Line()
    chart.title = chart_data['title']
    chart.x = chart_data['x']

    chart.y=chart_data['y']

    chart.file = chart_data['file']
    chart.x_title = chart_data['x_title']
    chart.y_title = chart_data['y_title']

    if chart_data['sum'] == 1:
        chart.sum_true()
    elif chart_data['mean'] == 1:
        chart.mean_true()

    if chart_data['limit'] == 1:
        chart.limit_true(chart_data['limit_num'])

    if chart_data['date'] == 1:
        chart.date_true()

    if for_dash:
        fig = chart.generate(1)
        desc = chart.get_dash_titles()
        return fig, desc
    else:
        chart.generate(0)


def request_bubble(chart_data, for_dash):
    chart = Bubblechart()
    chart.title = chart_data['title']
    chart.x = chart_data['x']

    chart.y =chart_data['y']
    chart.z = chart_data['z']

    chart.file = chart_data['file']
    chart.x_title = chart_data['x_title']
    chart.y_title = chart_data['y_title']
    chart.category = chart_data['category']
    chart.marker_data = chart_data['marker_data']

    if chart_data['sum'] == 1:
        chart.sum_true()
    elif chart_data['mean'] == 1:
        chart.mean_true()

    if chart_data['limit'] == 1:
        chart.limit_true(chart_data['limit_num'])


    if for_dash:
        fig = chart.generate(1)
        desc = chart.get_dash_titles()
        return fig, desc
    else:
        chart.generate(0)


def request_heat(chart_data, for_dash):
    chart = Heatmap()
    chart.title = chart_data['title']
    chart.x = chart_data['x']

    chart.y =chart_data['y']
    chart.z = chart_data['z']

    chart.file = chart_data['file']
    chart.x_title = chart_data['x_title']
    chart.y_title = chart_data['y_title']

    if chart_data['sum'] == 1:
        chart.sum_true()
    elif chart_data['mean'] == 1:
        chart.mean_true()

    if chart_data['limit'] == 1:
        chart.limit_true(chart_data['limit_num'])


    if for_dash:
        fig = chart.generate(1)
        desc = chart.get_dash_titles()
        return fig, desc
    else:
        chart.generate(0)

# Dash request method. For the dash_data argument, looks for a dictionary of the format
# {'bar': bar_data, 'line': line_data, 'stack': stack_data, etc...}


def request_dash(dash_data):


    bar_fig, bar_desc = request_bar(dash_data['bar'], 1)
    stack_fig, stack_desc = request_stack(dash_data['stack'], 1)
    line_fig, line_desc = request_line(dash_data['line'], 1)
    multi_fig, multi_desc = request_multi(dash_data['multi'], 1)
    bubble_fig, bubble_desc = request_bubble(dash_data['bubble'], 1)
    heat_fig, heat_desc = request_heat(dash_data['heat'], 1)
    dash_title = dash_data['dash_title']

    d.generate_dash(bar_fig, bar_desc, stack_fig, stack_desc, line_fig, line_desc,
                    multi_fig, multi_desc, heat_fig, heat_desc, bubble_fig, bubble_desc, dash_title)