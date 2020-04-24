import tkinter as tk
from tkinter import filedialog
import Plots.RequestHandler as request


# Function used to clear the window to prepare it for a new page
def clear():
    background.destroy()


def front_page():
    clear()

    background = tk.Frame(window, bg='gray')
    background.place(relwidth=1, relheight=1)

    # Create a new label to hold the title text
    title = tk.Label(background, bg='gray', text="Project Carrot")
    font_style = ('', 25)  # can be used to edit font style, '' can be replaced with a new font name
    title.config(font=font_style)  # applies the new font style
    # places the label in the top middle of the screen
    title.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.15, anchor='n')

    # Creates a new frame to hold new widgets
    lower_frame = tk.Frame(background, bg='gray')
    # Places the frame near the center of the screen
    lower_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')

    # Creates a label indicating to the user to select a chart type
    text = tk.Label(lower_frame, bg='gray', text="Please select the type of chart you would like to build: ")
    font_style = ('', 12)
    text.config(font=font_style)
    text.place(relx=0.5, rely=0.35, anchor='n')

    option.set("Select a Chart")  # sets the default text on the menu selection
    # Creates a menu with the charts as options
    chart_selection = tk.OptionMenu(lower_frame, option, "Bar Chart", "Bubble Chart", "Heat Map", "Line Chart",
                                    "MultiLine Chart", "Stacked Bar Chart")
    chart_selection.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.15, anchor='n')

    # Create a button that will get the chart selected from the menu
    next_button = tk.Button(background, text="Next Page", command=get_chart)
    # places the button in the lower right corner of the screen
    next_button.place(relx=0.91, rely=0.92)


def bar_chart():
    clear()
    # The two lines of code below create an empty background frame that can be added to
    # Widgets should be added to background so the clear method can delete the frame for a new page
    background = tk.Frame(window, bg='gray')
    background.place(relwidth=1, relheight=1)

    # Creates a back button to allow the user to go back to the chart selection page
    bck_button = tk.Button(background, text="Back", command=front_page)
    bck_button.place(relx=0.01, rely=0.92)

    # Create a title label to be placed at the top of the page
    title_label = tk.Label(background, bg='gray', text="Bar Chart")
    font_style = ('', 20)  # configure font size
    title_label.config(font=font_style)  # change the font size of the title
    title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

    # Create a frame for the widgets on this page to be placed in
    body_frame = tk.Frame(background, bg='gray')
    body_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')

    # Creates a label to indicate to the user to select a
    file_path_label = tk.Label(body_frame, bg='gray', text="Please Select a File:")
    file_path_label.place(relx=0.01, rely=0.01)

    # Create a button for the user to select the file
    file_path_entry = tk.Button(body_frame, text="Select file", command=lambda: file_selector())
    file_path_entry.place(relx=0.2, rely=0.01)

    chart_title_label = tk.Label(body_frame, bg='gray', text="Chart Title:")
    chart_title_label.place(relx=0.6, rely=0.01)

    chart_title_entry = tk.Entry(body_frame)
    chart_title_entry.place(relx=0.701, rely=0.01, relwidth=0.25)

    x_title_label = tk.Label(body_frame, bg='gray', text="X Axis Title:")
    x_title_label.place(relx=0.01, rely=0.2)

    x_title_entry = tk.Entry(body_frame)
    x_title_entry.place(relx=0.12, rely=0.2, relwidth=0.3)

    x_column_label = tk.Label(body_frame, bg='gray', text="Column of X-Axis Data:")
    x_column_label.place(relx=0.45, rely=0.2)

    x_entry = tk.Entry(body_frame)
    x_entry.place(relx=0.66, rely=0.2, relwidth=0.3)

    y_title_label = tk.Label(body_frame, bg='gray', text="Y Axis Title:")
    y_title_label.place(relx=0.01, rely=0.39)

    y_title_entry = tk.Entry(body_frame)
    y_title_entry.place(relx=0.12, rely=0.39, relwidth=0.3)

    y_column_label = tk.Label(body_frame, bg='gray', text="Column of Y-Axis Data:")
    y_column_label.place(relx=0.45, rely=0.39)

    y_entry = tk.Entry(body_frame)
    y_entry.place(relx=0.66, rely=0.39, relwidth=0.3)

    # Create a drop down menu
    sum_mean.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(body_frame, sum_mean, "None", "Sum", "Mean")
    chart_selection.place(relx=0.01, rely=0.75, relwidth=0.25)

    limit_label = tk.Label(body_frame, bg='gray', text="Would you like to place a limit?")
    limit_label.place(relx=0.01, rely=0.58)

    limit_menu.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(body_frame, limit_menu, "Yes", "No")
    chart_selection.place(relx=0.3, rely=0.58, relwidth=0.25)

    value_label = tk.Label(body_frame, bg='gray', text="Enter a limit, or 0 for none")
    value_label.place(relx=0.6, rely=0.58)

    limit_entry = tk.Entry(body_frame)
    limit_entry.place(relx=0.84, rely=0.58)

    # Create a submit button to send all user entries to a variable
    # The parameters are each of the entries returning their user input
    submit_button = tk.Button(background, text="Submit", command=lambda: submit_info(chart_title_entry.get(),
                                                                                     x_title_entry.get(),
                                                                                     x_entry.get(),
                                                                                     y_title_entry.get(),
                                                                                     y_entry.get(),
                                                                                     None,
                                                                                     sum_mean.get(),
                                                                                     limit_menu.get(),
                                                                                     limit_entry.get(), None, None,
                                                                                     None,
                                                                                     "Bar Chart"))
    submit_button.place(relx=0.93, rely=0.92)


def bubble_chart():
    clear()
    # The two lines of code below create an empty background frame that can be added to
    # Widgets should be added to background so the clear method can delete the frame for a new page
    background = tk.Frame(window, bg='gray')
    background.place(relwidth=1, relheight=1)

    # Creates a back button to allow the user to go back to the chart selection page
    bck_button = tk.Button(background, text="Back", command=front_page)
    bck_button.place(relx=0.01, rely=0.92)

    # Create a title label to be placed at the top of the page
    title_label = tk.Label(background, bg='gray', text="Bubble Chart")
    font_style = ('', 20)  # configure font size
    title_label.config(font=font_style)  # change the font size of the title
    title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

    # Create a frame for the widgets on this page to be placed in
    body_frame = tk.Frame(background, bg='gray')
    body_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')

    # Create a label to indicate to the user to enter the file path
    file_path_label = tk.Label(body_frame, bg='gray', text="Please Select a File:")
    file_path_label.place(relx=0.01, rely=0.01)

    # Create a button for the user to select the file
    file_path_entry = tk.Button(body_frame, text="Select file", command=lambda: file_selector())
    file_path_entry.place(relx=0.2, rely=0.01)

    chart_title_label = tk.Label(body_frame, bg='gray', text="Chart Title:")
    chart_title_label.place(relx=0.6, rely=0.01)

    chart_title_entry = tk.Entry(body_frame)
    chart_title_entry.place(relx=0.701, rely=0.01, relwidth=0.25)

    x_title_label = tk.Label(body_frame, bg='gray', text="X Axis Title:")
    x_title_label.place(relx=0.01, rely=0.2)

    x_title_entry = tk.Entry(body_frame)
    x_title_entry.place(relx=0.12, rely=0.2, relwidth=0.3)

    x_column_label = tk.Label(body_frame, bg='gray', text="Column of X-Axis Data:")
    x_column_label.place(relx=0.45, rely=0.2)

    x_entry = tk.Entry(body_frame)
    x_entry.place(relx=0.66, rely=0.2, relwidth=0.3)

    y_title_label = tk.Label(body_frame, bg='gray', text="Y Axis Title:")
    y_title_label.place(relx=0.01, rely=0.39)

    y_title_entry = tk.Entry(body_frame)
    y_title_entry.place(relx=0.12, rely=0.39, relwidth=0.3)

    y_column_label = tk.Label(body_frame, bg='gray', text="Column of Y-Axis Data:")
    y_column_label.place(relx=0.45, rely=0.39)

    y_entry = tk.Entry(body_frame)
    y_entry.place(relx=0.66, rely=0.39, relwidth=0.3)

    marker_label = tk.Label(body_frame, bg='gray', text="Marker Data:")
    marker_label.place(relx=0.01, rely=0.58)

    marker_entry = tk.Entry(body_frame)
    marker_entry.place(relx=0.13, rely=0.58, relwidth=0.3)

    # Create a drop down menu
    sum_mean.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(body_frame, sum_mean, "None", "Sum", "Mean")
    chart_selection.place(relx=0.65, rely=0.58, relwidth=0.25)

    limit_label = tk.Label(body_frame, bg='gray', text="Would you like to place a limit?")
    limit_label.place(relx=0.01, rely=0.75)

    limit_menu.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(body_frame, limit_menu, "Yes", "No")
    chart_selection.place(relx=0.3, rely=0.75, relwidth=0.25)

    value_label = tk.Label(body_frame, bg='gray', text="Enter a limit, or 0 for none")
    value_label.place(relx=0.6, rely=0.75)

    limit_entry = tk.Entry(body_frame)
    limit_entry.place(relx=0.84, rely=0.75)

    category_label = tk.Label(body_frame, bg='gray', text="Enter Category:")
    category_label.place(relx=0.01, rely=0.9)

    category_entry = tk.Entry(body_frame)
    category_entry.place(relx=0.15, rely=0.9)

    # Create a submit button to send all user entries to a variable
    # The parameters are each of the entries returning their user input
    submit_button = tk.Button(background, text="Submit", command=lambda: submit_info(chart_title_entry.get(),
                                                                                     x_title_entry.get(),
                                                                                     x_entry.get(),
                                                                                     y_title_entry.get(),
                                                                                     y_entry.get(),
                                                                                     None,
                                                                                     sum_mean.get(),
                                                                                     limit_menu.get(),
                                                                                     limit_entry.get(), None,
                                                                                     marker_entry.get(),
                                                                                     category_entry.get(),
                                                                                     "Bubble Chart"))
    submit_button.place(relx=0.93, rely=0.92)


def heat_map():
    clear()
    # The two lines of code below create an empty background frame that can be added to
    # Widgets should be added to background so the clear method can delete the frame for a new page
    background = tk.Frame(window, bg='gray')
    background.place(relwidth=1, relheight=1)

    # Creates a back button to allow the user to go back to the chart selection page
    bck_button = tk.Button(background, text="Back", command=front_page)
    bck_button.place(relx=0.01, rely=0.92)

    # Create a title label to be placed at the top of the page
    title_label = tk.Label(background, bg='gray', text="Heat Map")
    font_style = ('', 20)  # configure font size
    title_label.config(font=font_style)  # change the font size of the title
    title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

    # Create a frame for the widgets on this page to be placed in
    body_frame = tk.Frame(background, bg='gray')
    body_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')

    # Create a label to indicate to the user to enter the file path
    file_path_label = tk.Label(body_frame, bg='gray', text="Please Select a File:")
    file_path_label.place(relx=0.01, rely=0.01)

    # Create a button for the user to select the file
    file_path_entry = tk.Button(body_frame, text="Select file", command=lambda: file_selector())
    file_path_entry.place(relx=0.2, rely=0.01)

    chart_title_label = tk.Label(body_frame, bg='gray', text="Chart Title:")
    chart_title_label.place(relx=0.6, rely=0.01)

    chart_title_entry = tk.Entry(body_frame)
    chart_title_entry.place(relx=0.701, rely=0.01, relwidth=0.25)

    x_title_label = tk.Label(body_frame, bg='gray', text="X Axis Title:")
    x_title_label.place(relx=0.01, rely=0.2)

    x_title_entry = tk.Entry(body_frame)
    x_title_entry.place(relx=0.12, rely=0.2, relwidth=0.3)

    x_column_label = tk.Label(body_frame, bg='gray', text="Column of X-Axis Data:")
    x_column_label.place(relx=0.45, rely=0.2)

    x_entry = tk.Entry(body_frame)
    x_entry.place(relx=0.66, rely=0.2, relwidth=0.3)

    y_title_label = tk.Label(body_frame, bg='gray', text="Y Axis Title:")
    y_title_label.place(relx=0.01, rely=0.39)

    y_title_entry = tk.Entry(body_frame)
    y_title_entry.place(relx=0.12, rely=0.39, relwidth=0.3)

    y_column_label = tk.Label(body_frame, bg='gray', text="Column of Y-Axis Data:")
    y_column_label.place(relx=0.45, rely=0.39)

    y_entry = tk.Entry(body_frame)
    y_entry.place(relx=0.66, rely=0.39, relwidth=0.3)

    z_label = tk.Label(body_frame, bg='gray', text="Column of Z-Axis Data:")
    z_label.place(relx=0.01, rely=0.58)

    z_entry = tk.Entry(body_frame)
    z_entry.place(relx=0.22, rely=0.58, relwidth=0.3)

    # Create a drop down menu
    sum_mean.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(body_frame, sum_mean, "None", "Sum", "Mean")
    chart_selection.place(relx=0.65, rely=0.58, relwidth=0.25)

    limit_label = tk.Label(body_frame, bg='gray', text="Would you like to place a limit?")
    limit_label.place(relx=0.01, rely=0.75)

    limit_menu.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(body_frame, limit_menu, "Yes", "No")
    chart_selection.place(relx=0.3, rely=0.75, relwidth=0.25)

    value_label = tk.Label(body_frame, bg='gray', text="Enter a limit, or 0 for none")
    value_label.place(relx=0.6, rely=0.75)

    limit_entry = tk.Entry(body_frame)
    limit_entry.place(relx=0.84, rely=0.75)

    # Create a submit button to send all user entries to a variable
    # The parameters are each of the entries returning their user input
    submit_button = tk.Button(background, text="Submit", command=lambda: submit_info(chart_title_entry.get(),
                                                                                     x_title_entry.get(),
                                                                                     x_entry.get(),
                                                                                     y_title_entry.get(),
                                                                                     y_entry.get(),
                                                                                     z_entry.get(),
                                                                                     sum_mean.get(),
                                                                                     limit_menu.get(),
                                                                                     limit_entry.get(), None, None,
                                                                                     None, "Heat Map"))
    submit_button.place(relx=0.93, rely=0.92)


def line_chart():
    clear()
    # The two lines of code below create an empty background frame that can be added to
    # Widgets should be added to background so the clear method can delete the frame for a new page
    background = tk.Frame(window, bg='gray')
    background.place(relwidth=1, relheight=1)

    # Creates a back button to allow the user to go back to the chart selection page
    bck_button = tk.Button(background, text="Back", command=front_page)
    bck_button.place(relx=0.01, rely=0.92)

    # Create a title label to be placed at the top of the page
    title_label = tk.Label(background, bg='gray', text="Line Chart")
    font_style = ('', 20)  # configure font size
    title_label.config(font=font_style)  # change the font size of the title
    title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

    # Create a frame for the widgets on this page to be placed in
    body_frame = tk.Frame(background, bg='gray')
    body_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')

    # Create a label to indicate to the user to enter the file path
    file_path_label = tk.Label(body_frame, bg='gray', text="Please Select a File:")
    file_path_label.place(relx=0.01, rely=0.01)

    # Create a button for the user to select the file
    file_path_entry = tk.Button(body_frame, text="Select file", command=lambda: file_selector())
    file_path_entry.place(relx=0.2, rely=0.01)

    chart_title_label = tk.Label(body_frame, bg='gray', text="Chart Title:")
    chart_title_label.place(relx=0.6, rely=0.01)

    chart_title_entry = tk.Entry(body_frame)
    chart_title_entry.place(relx=0.701, rely=0.01, relwidth=0.25)

    x_title_label = tk.Label(body_frame, bg='gray', text="X Axis Title:")
    x_title_label.place(relx=0.01, rely=0.2)

    x_title_entry = tk.Entry(body_frame)
    x_title_entry.place(relx=0.12, rely=0.2, relwidth=0.3)

    x_column_label = tk.Label(body_frame, bg='gray', text="Column of X-Axis Data:")
    x_column_label.place(relx=0.45, rely=0.2)

    x_entry = tk.Entry(body_frame)
    x_entry.place(relx=0.66, rely=0.2, relwidth=0.3)

    y_title_label = tk.Label(body_frame, bg='gray', text="Y Axis Title:")
    y_title_label.place(relx=0.01, rely=0.39)

    y_title_entry = tk.Entry(body_frame)
    y_title_entry.place(relx=0.12, rely=0.39, relwidth=0.3)

    y_column_label = tk.Label(body_frame, bg='gray', text="Column of Y-Axis Data:")
    y_column_label.place(relx=0.45, rely=0.39)

    y_entry = tk.Entry(body_frame)
    y_entry.place(relx=0.66, rely=0.39, relwidth=0.3)

    z_label = tk.Label(body_frame, bg='gray', text="Does the X-Axis Show a Period of Time?:")
    z_label.place(relx=0.01, rely=0.58)

    line_chart_date.set("Please make a selection")
    chart_selection = tk.OptionMenu(body_frame, line_chart_date, "Yes", "No")
    chart_selection.place(relx=0.36, rely=0.58, relwidth=0.25)

    # Create a drop down menu
    sum_mean.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(body_frame, sum_mean, "None", "Sum", "Mean")
    chart_selection.place(relx=0.65, rely=0.58, relwidth=0.25)

    limit_label = tk.Label(body_frame, bg='gray', text="Would you like to place a limit?")
    limit_label.place(relx=0.01, rely=0.75)

    limit_menu.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(body_frame, limit_menu, "Yes", "No")
    chart_selection.place(relx=0.3, rely=0.75, relwidth=0.25)

    value_label = tk.Label(body_frame, bg='gray', text="Enter a limit, or 0 for none")
    value_label.place(relx=0.6, rely=0.75)

    limit_entry = tk.Entry(body_frame)
    limit_entry.place(relx=0.84, rely=0.75)

    # Create a submit button to send all user entries to a variable
    # The parameters are each of the entries returning their user input
    submit_button = tk.Button(background, text="Submit", command=lambda: submit_info(chart_title_entry.get(),
                                                                                     x_title_entry.get(),
                                                                                     x_entry.get(),
                                                                                     y_title_entry.get(),
                                                                                     y_entry.get(), None,
                                                                                     sum_mean.get(),
                                                                                     limit_menu.get(),
                                                                                     limit_entry.get(),
                                                                                     line_chart_date.get(), None, None,
                                                                                     "Line Chart"))
    submit_button.place(relx=0.93, rely=0.92)


def multi_line():
    clear()
    # The two lines of code below create an empty background frame that can be added to
    # Widgets should be added to background so the clear method can delete the frame for a new page
    background = tk.Frame(window, bg='white')
    background.place(relwidth=1, relheight=1)

    label = tk.Label(background, text='Multi-Line Chart')
    font_style = ('', 25)
    label.config(font=font_style)
    label.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.15, anchor='n')

    # Creates a label to indicate to the user to select a
    file_path_label = tk.Label(background, bg='gray', text="Please Select a File:")
    file_path_label.place(relx=0.01, rely=0.01)

    # Create a button for the user to select the file
    file_path_entry = tk.Button(background, text="Select file", command=lambda: file_selector())
    file_path_entry.place(relx=0.2, rely=0.01)

    chart_title_label = tk.Label(background, text='Chart name:')
    font_style = ('', 15)
    chart_title_label.config(font=font_style)
    chart_title_label.place(relx=0.05, rely=0.30)

    chart_title_entry = tk.Entry(background, bd=5)
    chart_title_entry.place(relx=0.20, rely=0.30)

    line_number = tk.Label(background, text='Number of lines:')
    font_style = ('', 15)
    line_number.config(font=font_style)
    line_number.place(relx=0.05, rely=0.40)

    option.set("Please make a selection")
    line_number_entry = tk.OptionMenu(background, option, "1", "2", "3")
    line_number_entry.place(relx=0.20, rely=0.40)

    x_axis_label = tk.Label(background, text="X axis title:")
    font_style = ('', 15)
    x_axis_label.config(font=font_style)
    x_axis_label.place(relx=0.05, rely=0.50)

    x_axis_entry = tk.Entry(background, bd=5)
    x_axis_entry.place(relx=0.20, rely=0.50)

    y_axis_label = tk.Label(background, text="Y axis title:")
    font_style = ('', 15)
    y_axis_label.config(font=font_style)
    y_axis_label.place(relx=.05, rely=.60)

    y_axis_entry = tk.Entry(background, bd=5)
    y_axis_entry.place(relx=0.20, rely=0.60)

    x_data_label = tk.Label(background, text='X data:')
    font_style = ('', 15)
    x_data_label.config(font=font_style)
    x_data_label.place(relx=.05, rely=.70)

    x_data_entry = tk.Entry(background, bd=5)
    x_data_entry.place(relx=0.20, rely=0.70)

    y_data_label = _data_label = tk.Label(background, text='Y data:')
    font_style = ('', 15)
    y_data_label.config(font=font_style)
    y_data_label.place(relx=.05, rely=.80)

    y1_entry = tk.Entry(background, bd=5)
    y1_entry.place(relx=0.20, rely=0.80, relwidth=0.2)

    y2_entry = tk.Entry(background, bd=5)
    y2_entry.place(relx=0.40, rely=0.80, relwidth=0.2)

    y3_entry = tk.Entry(background, bd=5)
    y3_entry.place(relx=0.60, rely=0.80, relwidth=0.2)

    y4_entry = tk.Entry(background, bd=5)
    y4_entry.place(relx=0.20, rely=0.90, relwidth=0.2)

    y5_entry = tk.Entry(background, bd=5)
    y5_entry.place(relx=0.40, rely=0.90, relwidth=0.2)

    y6_entry = tk.Entry(background, bd=5)
    y6_entry.place(relx=0.60, rely=0.90, relwidth=0.2)

    z_label = tk.Label(background, bg='gray', text="Does the X-Axis Show a Period of Time?:")
    z_label.place(relx=0.41, rely=0.2)

    line_chart_date.set("Please make a selection")
    chart_selection = tk.OptionMenu(background, line_chart_date, "Yes", "No")
    chart_selection.place(relx=0.6, rely=0.2, relwidth=0.25)

    sum_mean.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(background, sum_mean, "None", "Sum", "Mean")
    chart_selection.place(relx=0.6, rely=0.30, relwidth=0.25)

    limit_label = tk.Label(background, text="Would you like to place a limit?")
    limit_label.place(relx=0.41, rely=0.40)

    limit_menu.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(background, limit_menu, "Yes", "No")
    chart_selection.place(relx=0.6, rely=0.40, relwidth=0.25)

    value_label = tk.Label(background, text="Enter a limit, or 0 for none")
    value_label.place(relx=0.41, rely=0.5)

    limit_entry = tk.Entry(background)
    limit_entry.place(relx=0.6, rely=0.5)

    y1 = y1_entry.get()
    y2 = y2_entry.get()
    y3 = y3_entry.get()
    y4 = y4_entry.get()
    y5 = y5_entry.get()
    y6 = y6_entry.get()

    submit_button = tk.Button(background, text="Submit", command=lambda: submit_info(chart_title_entry.get(),
                                                                                     x_axis_entry.get(),
                                                                                     x_data_entry.get(),
                                                                                     y_axis_entry.get(),
                                                                                     y_data(y1, y2, y3, y4, y5, y6),
                                                                                     None,
                                                                                     sum_mean.get(),
                                                                                     limit_menu.get(),
                                                                                     limit_entry.get(),
                                                                                     line_chart_date.get(), None, None,
                                                                                     "MultiLine Chart"))

    submit_button.place(relx=0.91, rely=0.92)

    # Creates a back button to allow the user to go back to the chart selection page
    bck_button = tk.Button(background, text="Back", command=front_page)
    bck_button.place(relx=0.01, rely=0.92)


def stacked_bar():
    clear()
    # The two lines of code below create an empty background frame that can be added to
    # Widgets should be added to background so the clear method can delete the frame for a new page
    background = tk.Frame(window, bg='white')
    background.place(relwidth=1, relheight=1)

    label = tk.Label(background, text='Stacked Bar Chart')
    font_style = ('', 25)
    label.config(font=font_style)
    label.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.15, anchor='n')

    # Creates a label to indicate to the user to select a
    file_path_label = tk.Label(background, bg='gray', text="Please Select a File:")
    file_path_label.place(relx=0.01, rely=0.01)

    # Create a button for the user to select the file
    file_path_entry = tk.Button(background, text="Select file", command=lambda: file_selector())
    file_path_entry.place(relx=0.2, rely=0.01)

    chart_title_label = tk.Label(background, text='Chart name:')
    font_style = ('', 15)
    chart_title_label.config(font=font_style)
    chart_title_label.place(relx=0.05, rely=0.30)

    chart_title_entry = tk.Entry(background, bd=5)
    chart_title_entry.place(relx=0.20, rely=0.30)

    line_number = tk.Label(background, text='Number of Bars:')
    font_style = ('', 15)
    line_number.config(font=font_style)
    line_number.place(relx=0.05, rely=0.40)

    option.set("Please make a selection")
    line_number_entry = tk.OptionMenu(background, option, "1", "2", "3")
    line_number_entry.place(relx=0.20, rely=0.40)

    x_axis_label = tk.Label(background, text="X axis title:")
    font_style = ('', 15)
    x_axis_label.config(font=font_style)
    x_axis_label.place(relx=0.05, rely=0.50)

    x_axis_entry = tk.Entry(background, bd=5)
    x_axis_entry.place(relx=0.20, rely=0.50)

    y_axis_label = tk.Label(background, text="Y axis title:")
    font_style = ('', 15)
    y_axis_label.config(font=font_style)
    y_axis_label.place(relx=.05, rely=.60)

    y_axis_entry = tk.Entry(background, bd=5)
    y_axis_entry.place(relx=0.20, rely=0.60)

    x_data_label = tk.Label(background, text='X data:')
    font_style = ('', 15)
    x_data_label.config(font=font_style)
    x_data_label.place(relx=.05, rely=.70)

    x_data_entry = tk.Entry(background, bd=5)
    x_data_entry.place(relx=0.20, rely=0.70)

    y_data_label = _data_label = tk.Label(background, text='Y data:')
    font_style = ('', 15)
    y_data_label.config(font=font_style)
    y_data_label.place(relx=.05, rely=.80)

    y1_entry = tk.Entry(background, bd=5)
    y1_entry.place(relx=0.20, rely=0.80, relwidth=0.2)

    y2_entry = tk.Entry(background, bd=5)
    y2_entry.place(relx=0.40, rely=0.80, relwidth=0.2)

    y3_entry = tk.Entry(background, bd=5)
    y3_entry.place(relx=0.60, rely=0.80, relwidth=0.2)

    y4_entry = tk.Entry(background, bd=5)
    y4_entry.place(relx=0.20, rely=0.90, relwidth=0.2)

    y5_entry = tk.Entry(background, bd=5)
    y5_entry.place(relx=0.40, rely=0.90, relwidth=0.2)

    # y6_entry = tk.Entry(background, bd=5)
    # y6_entry.place(relx=0.60, rely=0.90, relwidth=0.2)

    z_label = tk.Label(background, bg='gray', text="Does the X-Axis Show a Period of Time?:")
    z_label.place(relx=0.41, rely=0.2)

    line_chart_date.set("Please make a selection")
    chart_selection = tk.OptionMenu(background, line_chart_date, "Yes", "No")
    chart_selection.place(relx=0.6, rely=0.2, relwidth=0.25)

    sum_mean.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(background, sum_mean, "None", "Sum", "Mean")
    chart_selection.place(relx=0.6, rely=0.30, relwidth=0.25)

    limit_label = tk.Label(background, text="Would you like to place a limit?")
    limit_label.place(relx=0.41, rely=0.40)

    limit_menu.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(background, limit_menu, "Yes", "No")
    chart_selection.place(relx=0.6, rely=0.40, relwidth=0.25)

    value_label = tk.Label(background, text="Enter a limit, or 0 for none")
    value_label.place(relx=0.41, rely=0.5)

    limit_entry = tk.Entry(background)
    limit_entry.place(relx=0.6, rely=0.5)

    y_data_entry = [["Death", "Death", '#ffff00'], ["Recovered", "Recovered", '#cccccc'],
                    ["Unrecovered", "Unrecovered", '#cc9900']]

    submit_button = tk.Button(background, text="Submit", command=lambda: submit_info(chart_title_entry.get(),
                                                                                     x_axis_entry.get(),
                                                                                     x_data_entry.get(),
                                                                                     y_axis_entry.get(),
                                                                                     y_data_entry, None,
                                                                                     sum_mean.get(),
                                                                                     limit_menu.get(),
                                                                                     limit_entry.get(),
                                                                                     line_chart_date.get(), None, None,
                                                                                     "Stacked Bar Chart"))
    submit_button.place(relx=0.91, rely=0.92)

    # Creates a back button to allow the user to go back to the chart selection page
    bck_button = tk.Button(background, text="Back", command=front_page)
    bck_button.place(relx=0.01, rely=0.92)


# Function used to get the chart that the user selected from the option menu on the front page
def get_chart():
    if option.get() == "Bar Chart":
        bar_chart()

    elif option.get() == "Bubble Chart":
        bubble_chart()

    elif option.get() == "Heat Map":
        heat_map()

    elif option.get() == "Line Chart":
        line_chart()

    elif option.get() == "MultiLine Chart":
        multi_line()

    elif option.get() == "Stacked Bar Chart":
        stacked_bar()

    # This else statement would indicate that the user did not select a graph from the drop down menu
    else:
        # Create an error box pop up to alert user to select a graph to continue
        error_box = tk.Toplevel(width=300, height=150, bg='white')
        error_box.title("Error: Select Graph")

        # Create a label at the top of the box
        error_title = tk.Label(error_box, bg='white', text="Error")
        font_style = ('', 20)
        error_title.config(font=font_style)
        error_title.place(relx=0.5, relwidth=0.75, relheight=0.25, anchor='n')

        # Create error message to user
        error_content = tk.Label(error_box, bg='white', text="Please select a graph to continue.")
        error_content.place(relx=0.5, rely=0.3, anchor='n')

        # Create button to close error box
        button = tk.Button(error_box, text="OK", command=error_box.destroy)
        button.place(relx=0.5, rely=0.5, anchor='n')


# This method gets the data from the heat map entry widgets to populate the dictionary that can be handled by the
# RequestHandler.py
# The chart key should be different depending on which chart calls this method so that the correct method from the
# RequestHandler.py can be called
def submit_info(chart_title, x_title, x, y_title, y, z, sum_or_mean, limit_option, limit_value, date, marker, category,
                chart_key):
    chart_data['title'] = chart_title
    chart_data['x_title'] = x_title
    chart_data['x'] = x
    chart_data['y_title'] = y_title
    chart_data['y'] = y
    chart_data['z'] = z
    chart_data['marker_data'] = marker
    chart_data['category'] = category

    # Determines if the user selected to include a sum or a mean
    if sum_or_mean == "Sum":
        chart_data['sum'] = 1
    elif sum_or_mean == "Mean":
        chart_data['mean'] = 1

    # Determines if the user selected the x-axis to show a period of time for the line graph
    if date == "Yes":
        chart_data['date'] = 1

    # Determines if the user selected to include a limit
    if limit_option == "Yes":
        chart_data['limit'] = 1

    # Checks to see if the user entered a value for the limit, makes sure there is an integer value to cast to
    if limit_value != "":
        chart_data['limit_num'] = int(limit_value)

    # Reads the chart key to determine which type of chart should be generated from the request handler
    if chart_key == "Bar Chart":
        request.request_bar(chart_data, 0)
    elif chart_key == "Bubble Chart":
        request.request_bubble(chart_data, 0)
    elif chart_key == "Heat Map":
        request.request_heat(chart_data, 0)
    elif chart_key == "Line Chart":
        request.request_line(chart_data, 0)
    elif chart_key == "MultiLine Chart":
        request.request_multi(chart_data, 0)
    elif chart_key == "Stacked Bar Chart":
        request.request_stack(chart_data, 0)


def y_data(y1, y2, y3, y4, y5, y6):
    y_array = [[y1, y4], [y2, y5], [y3, y6]]
    return y_array


# Function that can be called by a button or other widget that will allow the user to select the file they
# wish to open, this function will change the value in the global dictionary
# This function is used so that the user does not have to type the file path themselves
def file_selector():
    chart_data['file'] = filedialog.askopenfilename()


# Create a global dictionary that can be sent to RequestHandler.py
chart_data = {'file': None, 'title': None, 'x_title': None, 'x': None, 'y_title': None, 'y': None, 'z': None,
              'sum': 0, 'mean': 0, 'limit': 0, 'limit_num': 0, 'date': 0, 'marker_data': None, 'category': None,
              'y_array': None}

# Create a new window
window = tk.Tk()

# Change the title of the window
window.title("Project Carrot")

# Creates a tkinter variable to be used in drop down menu for chart selection on front page
option = tk.StringVar(window)
# Creates a tkinter variable to be used in drop down menu to select a sum or mean
sum_mean = tk.StringVar(window)
# Creates a tkinter variable to be used in the drop down menu to select whether a limit should be used
limit_menu = tk.StringVar(window)
# Creates a tkinter variable to be used in the drop down menu to select date for line_chart()
line_chart_date = tk.StringVar(window)

# Create a canvas to adjust the window size
window_size = tk.Canvas(window, width=800, height=400)
window_size.pack()

# Create a frame to act as the background for GUI
background = tk.Frame(window, bg='white')
# The background takes up the entire window, all widgets will be placed inside this frame
background.place(relwidth=1, relheight=1)

front_page()

window.mainloop()
