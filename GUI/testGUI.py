import tkinter as tk
import Plots.RequestHandler as request


# Function used to clear the window to prepare it for a new page
def clear():
    background.destroy()


def front_page():
    clear()

    background = tk.Frame(window, bg='white')
    background.place(relwidth=1, relheight=1)

    # Create a new label to hold the title text
    title = tk.Label(background, bg='white', text="Project Carrot")
    font_style = ('', 25)  # can be used to edit font style, '' can be replaced with a new font name
    title.config(font=font_style)  # applies the new font style
    # places the label in the top middle of the screen
    title.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.15, anchor='n')

    # Creates a new frame to hold new widgets
    lower_frame = tk.Frame(background, bg='white')
    # Places the frame near the center of the screen
    lower_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')

    # Creates a label indicating to the user to select a chart type
    text = tk.Label(lower_frame, bg='white', text="Please select the type of chart you would like to build: ")
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
    background = tk.Frame(window, bg='white')
    background.place(relwidth=1, relheight=1)

    # Creates a back button to allow the user to go back to the chart selection page
    bck_button = tk.Button(background, text="Back", command=front_page)
    bck_button.place(relx=0.01, rely=0.92)


def bubble_chart():
    clear()
    # The two lines of code below create an empty background frame that can be added to
    # Widgets should be added to background so the clear method can delete the frame for a new page
    background = tk.Frame(window, bg='white')
    background.place(relwidth=1, relheight=1)

    # Creates a back button to allow the user to go back to the chart selection page
    bck_button = tk.Button(background, text="Back", command=front_page)
    bck_button.place(relx=0.01, rely=0.92)


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
    file_path_label = tk.Label(body_frame, bg='gray', text="Please enter the file path:")
    file_path_label.place(relx=0.01, rely=0.01)

    # Create an entry box for the user to input the file path
    file_path_entry = tk.Entry(body_frame)
    file_path_entry.place(relx=0.23, rely=0.01, relwidth=0.3)

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
    option.set("Please make a selection")  # sets the default text on the menu selection
    chart_selection = tk.OptionMenu(body_frame, option, "None", "Sum", "Mean")
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
    submit_button = tk.Button(background, text="Submit", command=lambda: get_heat_map(file_path_entry.get(),
                                                                                      chart_title_entry.get(),
                                                                                      x_title_entry.get(),
                                                                                      x_entry.get(),
                                                                                      y_title_entry.get(),
                                                                                      y_entry.get(),
                                                                                      z_entry.get(),
                                                                                      option.get(),
                                                                                      limit_menu.get(),
                                                                                      limit_entry.get(),
                                                                                      "Heat Map"))
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
    file_path_label = tk.Label(body_frame, bg='gray', text="Please enter the file path:")
    file_path_label.place(relx=0.01, rely=0.01)

    # Create an entry box for the user to input the file path
    file_path_entry = tk.Entry(body_frame)
    file_path_entry.place(relx=0.23, rely=0.01, relwidth=0.3)

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

    # Create a submit button to send all user entries to a variable
    # The parameters are each of the entries returning their user input
    submit_button = tk.Button(background, text="Submit", command=lambda: get_heat_map(file_path_entry.get(),
                                                                                      chart_title_entry.get(),
                                                                                      x_title_entry.get(),
                                                                                      x_entry.get(),
                                                                                      y_title_entry.get(),
                                                                                      y_entry.get(),
                                                                                      z_entry.get()))
    submit_button.place(relx=0.91, rely=0.92)


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

    file_path_label = tk.Label(background, text='File Path:')
    font_style = ('', 15)
    file_path_label.config(font=font_style)
    file_path_label.place(relx=0.05, rely=0.2,)

    file_path_entry = tk.Entry(background, bd=5)
    file_path_entry.place(relx=0.20, rely=0.2)

    chart_title_label = tk.Label(background, text= 'Chart name:')
    font_style = ('', 15)
    chart_title_label.config(font=font_style)
    chart_title_label.place(relx=0.05, rely=0.30)

    chart_title_entry = tk.Entry(background, bd=5)
    chart_title_entry.place(relx=0.20, rely=0.30)

    line_number= tk.Label(background, text='Number of lines:')
    font_style = ('', 15)
    line_number.config(font = font_style)
    line_number.place(relx=0.05, rely=0.40)

    line_number_entry = tk.Entry(background, bd=5)
    line_number_entry.place(relx=0.20, rely=0.40)

    x_axis_label = tk.Label(background, text="X axis title:")
    font_style = ('', 15)
    x_axis_label.config(font= font_style)
    x_axis_label.place(relx=0.05, rely=0.50)

    x_axis_entry = tk.Entry(background, bd = 5)
    x_axis_entry.place(relx=0.20, rely =0.50)

    y_axis_label = tk.Label(background, text = "Y axis title:")
    font_style = ('', 15)
    y_axis_label.config(font = font_style)
    y_axis_label.place(relx=.05, rely =.60)

    y_axis_entry = tk.Entry(background, bd=5)
    y_axis_entry.place(relx=0.20, rely=0.60)

    x_data_label = tk.Label(background, text= 'X data:')
    font_style = ('', 15)
    x_data_label.config(font=font_style)
    x_data_label.place(relx=.05, rely=.70)

    x_data_entry = tk.Entry(background, bd = 5)
    x_data_entry.place(relx=0.20, rely=0.70)

    y_data_label = tk.Label(background, text='Y data:')
    font_style = ('', 15)
    y_data_label.config(font=font_style)
    y_data_label.place(relx=.05, rely=.80)

    y_data_entry = tk.Entry(background, bd=5)
    y_data_entry.place(relx=0.20, rely=0.80)

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

    file_path_label = tk.Label(background, text='File Path:')
    font_style = ('', 15)
    file_path_label.config(font=font_style)
    file_path_label.place(relx=0.05, rely=0.2, )

    file_path_entry = tk.Entry(background, bd=5)
    file_path_entry.place(relx=0.20, rely=0.2)

    chart_title_label = tk.Label(background, text='Chart name:')
    font_style = ('', 15)
    chart_title_label.config(font=font_style)
    chart_title_label.place(relx=0.05, rely=0.30)

    chart_title_entry = tk.Entry(background, bd=5)
    chart_title_entry.place(relx=0.20, rely=0.30)

    line_number = tk.Label(background, text='Number of bars:')
    font_style = ('', 15)
    line_number.config(font=font_style)
    line_number.place(relx=0.05, rely=0.40)

    line_number_entry = tk.Entry(background, bd=5)
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

    y_data_label = tk.Label(background, text='Y data:')
    font_style = ('', 15)
    y_data_label.config(font=font_style)
    y_data_label.place(relx=.05, rely=.80)

    y_data_entry = tk.Entry(background, bd=5)
    y_data_entry.place(relx=0.20, rely=0.80)

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
def get_heat_map(file, chart_title, x_title, x, y_title, y, z, sum_mean, limit_option, limit_value, chart_key):
    chart_data['file'] = file
    chart_data['title'] = chart_title
    chart_data['x_title'] = x_title
    chart_data['x'] = x
    chart_data['y_title'] = y_title
    chart_data['y'] = y
    chart_data['z'] = z
    chart_data['limit_num'] = limit_value

    if sum_mean == "Sum":
        chart_data['sum'] = 1
    elif sum_mean == "Mean":
        chart_data['mean'] = 1

    if limit_option == "Yes":
        chart_data['limit'] = 1

    if chart_key == "Heat Map":
        request.request_heat(chart_data, 0)


# Create a global dictionary that can be sent to RequestHandler.py
chart_data = {'file': None, 'title': None, 'x_title': None, 'x': None, 'y_title': None, 'y': None, 'z': None,
              'sum': 0, 'mean': 0, 'limit': 0, 'limit_num': 0}

# Create a new window
window = tk.Tk()

# Change the title of the window
window.title("Project Carrot")

# Creates a tkinter variable to use in functions
option = tk.StringVar(window)
limit_menu = tk.StringVar(window)

# Create a canvas to adjust the window size
window_size = tk.Canvas(window, width=800, height=400)
window_size.pack()

# Create a frame to act as the background for GUI
background = tk.Frame(window, bg='white')
# The background takes up the entire window, all widgets will be placed inside this frame
background.place(relwidth=1, relheight=1)

front_page()

window.mainloop()
