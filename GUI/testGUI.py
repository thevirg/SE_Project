import tkinter as tk
# heres my test comment, please work

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
    background = tk.Frame(window, bg='white')
    background.place(relwidth=1, relheight=1)

    # Creates a back button to allow the user to go back to the chart selection page
    bck_button = tk.Button(background, text="Back", command=front_page)
    bck_button.place(relx=0.01, rely=0.92)


def line_chart():
    clear()
    # The two lines of code below create an empty background frame that can be added to
    # Widgets should be added to background so the clear method can delete the frame for a new page
    background = tk.Frame(window, bg='white')
    background.place(relwidth=1, relheight=1)

    # Creates a back button to allow the user to go back to the chart selection page
    bck_button = tk.Button(background, text="Back", command=front_page)
    bck_button.place(relx=0.01, rely=0.92)


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

<<<<<<< Updated upstream
=======
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

>>>>>>> Stashed changes
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


# Create a new window
window = tk.Tk()
# Change the title of the window
window.title("Project Carrot")
# Creates a tkinter variable to use in functions
option = tk.StringVar(window)
# Create a canvas to adjust the window size
window_size = tk.Canvas(window, width=800, height=400)
window_size.pack()

# Create a frame to act as the background for GUI
background = tk.Frame(window, bg='white')
# The background takes up the entire window, all widgets will be placed inside this frame
background.place(relwidth=1, relheight=1)

front_page()

window.mainloop()
