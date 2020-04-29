import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.colorchooser import askcolor
import Plots.RequestHandler as request
import pandas as pd


def main():


    # Function used to clear the window to prepare it for a new page
    def clear():
        background.destroy()


    def front_page():
        global for_dash
        for_dash = 0  # changes the value back to 0 in case the user uses the back button
        clear()

        background = tk.Frame(window, bg='#10435e')
        background.place(relwidth=1, relheight=1)

        # Create a new label to hold the title text
        title = tk.Label(background, bg='#10435e', fg='white', text="Project Carrot")
        font_style = ('', 25)  # can be used to edit font style, '' can be replaced with a new font name
        title.config(font=font_style)  # applies the new font style
        # places the label in the top middle of the screen
        title.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.15, anchor='n')

        # Creates a new frame to hold new widgets
        lower_frame = tk.Frame(background, bg='#10435e')
        # Places the frame near the center of the screen
        lower_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')

        # Creates a label indicating to the user to select a chart type
        text = tk.Label(lower_frame, bg='#10435e', fg='white', text="Please select the type of chart you "
                                                                    "would like to build: ")
        font_style = ('', 12)
        text.config(font=font_style)
        text.place(relx=0.5, rely=0.35, anchor='n')

        # Creates a menu with the charts as options
        chart_selection = ttk.OptionMenu(lower_frame, option, "Select a Chart", "Bar Chart", "Bubble Chart", "Heat Map",
                                         "Line Chart", "MultiLine Chart", "Stacked Bar Chart", "Dashboard")
        chart_selection.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.15, anchor='n')

        # Create a button that will get the chart selected from the menu
        next_button = ttk.Button(background, text="Next Page", command=get_chart)
        # places the button in the lower right corner of the screen
        next_button.place(relx=0.9, rely=0.92)


    def bar_chart():
        global for_dash
        clear()
        # The two lines of code below create an empty background frame that can be added to
        # Widgets should be added to background so the clear method can delete the frame for a new page
        background = tk.Frame(window, bg='#10435e')
        background.place(relwidth=1, relheight=1)

        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = ttk.Button(background, text="Back", command=back_front_page)
        bck_button.place(relx=0.01, rely=0.92, relwidth=0.05)

        # Create a title label to be placed at the top of the page
        title_label = tk.Label(background, bg='#10435e', fg='white', text="Bar Chart")
        font_style = ('', 20)  # configure font size
        title_label.config(font=font_style)  # change the font size of the title
        title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

        # Create a frame for the widgets on this page to be placed in
        body_frame = tk.Frame(background, bg='#10435e')
        body_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')

        # Creates a label to indicate to the user to select a
        file_path_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Please Select a File:")
        file_path_label.place(relx=0.01, rely=0.01)

        # Create a button for the user to select the file
        file_path_entry = ttk.Button(body_frame, text="Select file", command=lambda: [file_selector(file_path_entry),
                                                                                      update_dropdown(x_entry, x_option),
                                                                                      update_dropdown(y_entry, y1_option)])
        file_path_entry.place(relx=0.19, rely=0.01, relwidth=0.40)

        chart_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Chart Title:")
        chart_title_label.place(relx=0.6, rely=0.01)

        chart_title_entry = ttk.Entry(body_frame)
        chart_title_entry.place(relx=0.701, rely=0.01, relwidth=0.25)

        x_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="X Axis Title:")
        x_title_label.place(relx=0.01, rely=0.2)

        x_title_entry = ttk.Entry(body_frame)
        x_title_entry.place(relx=0.12, rely=0.2, relwidth=0.3)

        x_column_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of X-Axis Data:")
        x_column_label.place(relx=0.45, rely=0.2)

        x_entry = ttk.OptionMenu(body_frame, x_option, column_choices)
        x_entry.place(relx=0.66, rely=0.2, relwidth=0.3)

        y_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Y Axis Title:")
        y_title_label.place(relx=0.01, rely=0.39)

        y_title_entry = ttk.Entry(body_frame)
        y_title_entry.place(relx=0.12, rely=0.39, relwidth=0.3)

        y_column_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of Y-Axis Data:")
        y_column_label.place(relx=0.45, rely=0.39)

        y_entry = ttk.OptionMenu(body_frame, y1_option, column_choices)
        y_entry.place(relx=0.66, rely=0.39, relwidth=0.3)

        # Create a drop down menu
        chart_selection = ttk.OptionMenu(body_frame, sum_mean, "Please make a selection", "None", "Sum", "Mean")
        chart_selection.place(relx=0.01, rely=0.75, relwidth=0.25)

        limit_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Would you like to place a limit?")
        limit_label.place(relx=0.01, rely=0.58)

        chart_selection = ttk.OptionMenu(body_frame, limit_menu, "Please make a selection", "Yes", "No")
        chart_selection.place(relx=0.3, rely=0.58, relwidth=0.25)

        value_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Enter a limit, or 0 for none")
        value_label.place(relx=0.6, rely=0.58)

        limit_entry = tk.Entry(body_frame)
        limit_entry.place(relx=0.84, rely=0.58)


        limit_entry = ttk.Entry(body_frame)
        limit_entry.place(relx=0.84, rely=0.58, relwidth=0.15)

        # This if statement checks to see if the user selected to generate a dashboard
        # If a dashboard was selected the submit button will take the user to the next chart to enter data for
        # Because this option occurs when the user selects to generate a dashboard, bubble chart is also called
        if for_dash:
            # Create a submit button to send all user entries to a variable
            # The parameters are each of the entries returning their user input
            next_button = ttk.Button(background, text="Next Page", command=lambda: [submit_info(chart_title_entry.get(),
                                                                                                x_title_entry.get(),
                                                                                                x_option.get(),
                                                                                                y_title_entry.get(),
                                                                                                y1_option.get(), None,
                                                                                                sum_mean.get(),
                                                                                                limit_menu.get(),
                                                                                                limit_entry.get(), None,
                                                                                                None, None, None,
                                                                                                "Bar Chart"),
                                                                                    bubble_chart()])
            next_button.place(relx=0.9, rely=0.92)
        else:
            submit_button = ttk.Button(background, text="Generate Chart", command=lambda: submit_info(
                                                                                                chart_title_entry.get(),
                                                                                                x_title_entry.get(),
                                                                                                x_option.get(),
                                                                                                y_title_entry.get(),
                                                                                                y1_option.get(),
                                                                                                None,
                                                                                                sum_mean.get(),
                                                                                                limit_menu.get(),
                                                                                                limit_entry.get(), None, None,
                                                                                                None, None,
                                                                                                "Bar Chart"))
            submit_button.place(relx=0.88, rely=0.92)


    def bubble_chart():
        global for_dash
        clear()
        # The two lines of code below create an empty background frame that can be added to
        # Widgets should be added to background so the clear method can delete the frame for a new page
        background = tk.Frame(window, bg='#10435e')
        background.place(relwidth=1, relheight=1)

        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = ttk.Button(background, text="Back", command=back_front_page)
        bck_button.place(relx=0.01, rely=0.92, relwidth=0.05)

        # Create a title label to be placed at the top of the page
        title_label = tk.Label(background, bg='#10435e', fg='white', text="Bubble Chart")
        font_style = ('', 20)  # configure font size
        title_label.config(font=font_style)  # change the font size of the title
        title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

        # Create a frame for the widgets on this page to be placed in
        body_frame = tk.Frame(background, bg='#10435e')
        body_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')

        # Create a label to indicate to the user to enter the file path
        file_path_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Please Select a File:")
        file_path_label.place(relx=0.01, rely=0.01)

        # Create a button for the user to select the file
        file_path_entry = ttk.Button(body_frame, text="Select file", command=lambda: [file_selector(file_path_entry),
                                                                                      update_dropdown(x_entry, x_option),
                                                                                      update_dropdown(y_entry, y1_option),
                                                                                      update_dropdown(marker_entry, marker_option),
                                                                                      update_dropdown(category_entry, category_option)])
        file_path_entry.place(relx=0.19, rely=0.01, relwidth=0.40)

        chart_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Chart Title:")
        chart_title_label.place(relx=0.6, rely=0.01)

        chart_title_entry = ttk.Entry(body_frame)
        chart_title_entry.place(relx=0.701, rely=0.01, relwidth=0.25)

        x_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="X Axis Title:")
        x_title_label.place(relx=0.01, rely=0.2)

        x_title_entry = ttk.Entry(body_frame)
        x_title_entry.place(relx=0.12, rely=0.2, relwidth=0.3)

        x_column_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of X-Axis Data:")
        x_column_label.place(relx=0.45, rely=0.2)

        x_entry = ttk.OptionMenu(body_frame, x_option, column_choices)
        x_entry.place(relx=0.66, rely=0.2, relwidth=0.3)

        y_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Y Axis Title:")
        y_title_label.place(relx=0.01, rely=0.39)

        y_title_entry = ttk.Entry(body_frame)
        y_title_entry.place(relx=0.12, rely=0.39, relwidth=0.3)

        y_column_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of Y-Axis Data:")
        y_column_label.place(relx=0.45, rely=0.39)

        y_entry = ttk.OptionMenu(body_frame, y1_option, column_choices)
        y_entry.place(relx=0.66, rely=0.39, relwidth=0.3)

        marker_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Marker Data:")
        marker_label.place(relx=0.01, rely=0.58)

        marker_entry = ttk.OptionMenu(body_frame, marker_option, column_choices)
        marker_entry.place(relx=0.13, rely=0.58, relwidth=0.3)

        # Create a drop down menu
        chart_selection = ttk.OptionMenu(body_frame, sum_mean, "Please make a selection", "None", "Sum", "Mean")
        chart_selection.place(relx=0.65, rely=0.58, relwidth=0.25)

        limit_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Would you like to place a limit?")
        limit_label.place(relx=0.01, rely=0.75)

        chart_selection = ttk.OptionMenu(body_frame, limit_menu, "Please make a selection", "Yes", "No")
        chart_selection.place(relx=0.3, rely=0.75, relwidth=0.25)

        value_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Enter a limit, or 0 for none")
        value_label.place(relx=0.6, rely=0.75)

        limit_entry = ttk.Entry(body_frame)
        limit_entry.place(relx=0.84, rely=0.75, relwidth=0.15)

        category_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Enter Category:")
        category_label.place(relx=0.01, rely=0.9)

        category_entry = ttk.OptionMenu(body_frame, category_option, column_choices)
        category_entry.place(relx=0.15, rely=0.9)



        # This if statement checks to see if the user selected to generate a dashboard
        # If a dashboard was selected the submit button will take the user to the next chart to enter data for
        if for_dash:
            # Create a submit button to send all user entries to a variable
            # The parameters are each of the entries returning their user input
            # because this option occurs when the user has selected to generate a dashboard, the button also calls heat map
            submit_button = ttk.Button(background, text="Next Page", command=lambda: [submit_info(chart_title_entry.get(),
                                                                                                  x_title_entry.get(),
                                                                                                  x_option.get(),
                                                                                                  y_title_entry.get(),
                                                                                                  y1_option.get(), None,
                                                                                                  sum_mean.get(),
                                                                                                  limit_menu.get(),
                                                                                                  limit_entry.get(), None,
                                                                                                  marker_option.get(),
                                                                                                  category_option.get(), None,
                                                                                                  "Bubble Chart"),
                                                                                      heat_map()])
            submit_button.place(relx=0.9, rely=0.92)
        else:
            submit_button = ttk.Button(background, text="Generate Chart",
                                       command=lambda: submit_info(chart_title_entry.get(),
                                                                   x_title_entry.get(),
                                                                   x_option.get(),
                                                                   y_title_entry.get(),
                                                                   y1_option.get(), None,
                                                                   sum_mean.get(),
                                                                   limit_menu.get(),
                                                                   limit_entry.get(), None,
                                                                   marker_option.get(),
                                                                   category_option.get(), None,
                                                                   "Bubble Chart"))
            submit_button.place(relx=0.88, rely=0.92)


    def heat_map():
        global for_dash
        clear()
        # The two lines of code below create an empty background frame that can be added to
        # Widgets should be added to background so the clear method can delete the frame for a new page
        background = tk.Frame(window, bg='#10435e')
        background.place(relwidth=1, relheight=1)

        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = ttk.Button(background, text="Back", command=back_front_page)
        bck_button.place(relx=0.01, rely=0.92, relwidth=0.05)

        # Create a title label to be placed at the top of the page
        title_label = tk.Label(background, bg='#10435e', fg='white', text="Heat Map")
        font_style = ('', 20)  # configure font size
        title_label.config(font=font_style)  # change the font size of the title
        title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

        # Create a frame for the widgets on this page to be placed in
        body_frame = tk.Frame(background, bg='#10435e')
        body_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')

        # Create a label to indicate to the user to enter the file path
        file_path_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Please Select a File:")
        file_path_label.place(relx=0.01, rely=0.01)

        # Create a button for the user to select the file
        file_path_entry = ttk.Button(body_frame, text="Select file", command=lambda: [file_selector(file_path_entry),
                                                                                      update_dropdown(x_entry, x_option),
                                                                                      update_dropdown(y_entry, y1_option),
                                                                                      update_dropdown(z_entry, z_option)])

        file_path_entry.place(relx=0.19, rely=0.01, relwidth=0.40)

        chart_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Chart Title:")
        chart_title_label.place(relx=0.6, rely=0.01)

        chart_title_entry = ttk.Entry(body_frame)
        chart_title_entry.place(relx=0.701, rely=0.01, relwidth=0.25)

        x_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="X Axis Title:")
        x_title_label.place(relx=0.01, rely=0.2)

        x_title_entry = ttk.Entry(body_frame)
        x_title_entry.place(relx=0.12, rely=0.2, relwidth=0.3)

        x_column_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of X-Axis Data:")
        x_column_label.place(relx=0.45, rely=0.2)

        x_entry = ttk.OptionMenu(body_frame, x_option, column_choices)
        x_entry.place(relx=0.66, rely=0.2, relwidth=0.3)

        y_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Y Axis Title:")
        y_title_label.place(relx=0.01, rely=0.39)

        y_title_entry = ttk.Entry(body_frame)
        y_title_entry.place(relx=0.12, rely=0.39, relwidth=0.3)

        y_column_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of Y-Axis Data:")
        y_column_label.place(relx=0.45, rely=0.39)

        y_entry = ttk.OptionMenu(body_frame, y1_option, column_choices)
        y_entry.place(relx=0.66, rely=0.39, relwidth=0.3)

        z_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of Z-Axis Data:")
        z_label.place(relx=0.01, rely=0.58)

        z_entry = ttk.OptionMenu(body_frame, z_option, column_choices)
        z_entry.place(relx=0.22, rely=0.58, relwidth=0.3)

        # Create a drop down menu
        chart_selection = ttk.OptionMenu(body_frame, sum_mean, "Please make a selection", "None", "Sum", "Mean")
        chart_selection.place(relx=0.65, rely=0.58, relwidth=0.25)

        limit_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Would you like to place a limit?")
        limit_label.place(relx=0.01, rely=0.75)

        chart_selection = ttk.OptionMenu(body_frame, limit_menu, "Please make a selection", "Yes", "No")
        chart_selection.place(relx=0.3, rely=0.75, relwidth=0.25)

        value_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Enter a limit, or 0 for none")
        value_label.place(relx=0.6, rely=0.75)

        limit_entry = tk.Entry(body_frame)
        limit_entry.place(relx=0.84, rely=0.75)


        if for_dash:
            # Create a submit button to send all user entries to a variable
            # The parameters are each of the entries returning their user input
            submit_button = ttk.Button(background, text="Next Page", command=lambda: [submit_info(chart_title_entry.get(),
                                                                                                  x_title_entry.get(),
                                                                                                  x_option.get(),
                                                                                                  y_title_entry.get(),
                                                                                                  y1_option.get(),
                                                                                                  z_option.get(),
                                                                                                  sum_mean.get(),
                                                                                                  limit_menu.get(),
                                                                                                  limit_entry.get(), None,
                                                                                                  None, None, None, "Heat Map"),
                                                                                      line_chart()])
            submit_button.place(relx=0.9, rely=0.92)
        else:
            submit_button = ttk.Button(background, text="Submit", command=lambda: submit_info(chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y1_option.get(),
                                                                                              z_option.get(),
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(), None, None,
                                                                                              None, None, "Heat Map"))
            submit_button.place(relx=0.9, rely=0.92)


    def line_chart():
        clear()
        # The two lines of code below create an empty background frame that can be added to
        # Widgets should be added to background so the clear method can delete the frame for a new page
        background = tk.Frame(window, bg='#10435e')
        background.place(relwidth=1, relheight=1)

        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = ttk.Button(background, text="Back", command=back_front_page)
        bck_button.place(relx=0.01, rely=0.92, relwidth=0.05)

        # Create a title label to be placed at the top of the page
        title_label = tk.Label(background, bg='#10435e', fg='white', text="Line Chart")
        font_style = ('', 20)  # configure font size
        title_label.config(font=font_style)  # change the font size of the title
        title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

        # Create a frame for the widgets on this page to be placed in
        body_frame = tk.Frame(background, bg='#10435e')
        body_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')

        # Create a label to indicate to the user to enter the file path
        file_path_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Please Select a File:")
        file_path_label.place(relx=0.01, rely=0.01)

        # Create a button for the user to select the file
        file_path_entry = ttk.Button(body_frame, text="Select file", command=lambda: [file_selector(file_path_entry),
                                                                                      update_dropdown(x_entry, x_option),
                                                                                      update_dropdown(y_entry, y1_option)])

        file_path_entry.place(relx=0.19, rely=0.01, relwidth=0.40)

        chart_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Chart Title:")
        chart_title_label.place(relx=0.6, rely=0.01)

        chart_title_entry = ttk.Entry(body_frame)
        chart_title_entry.place(relx=0.701, rely=0.01, relwidth=0.25)

        x_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="X Axis Title:")
        x_title_label.place(relx=0.01, rely=0.2)

        x_title_entry = ttk.Entry(body_frame)
        x_title_entry.place(relx=0.12, rely=0.2, relwidth=0.3)

        x_column_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of X-Axis Data:")
        x_column_label.place(relx=0.45, rely=0.2)


        x_entry = ttk.OptionMenu(body_frame, x_option, column_choices)
        x_entry.place(relx=0.66, rely=0.2, relwidth=0.3)

        y_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Y Axis Title:")
        y_title_label.place(relx=0.01, rely=0.39)

        y_title_entry = ttk.Entry(body_frame)
        y_title_entry.place(relx=0.12, rely=0.39, relwidth=0.3)

        y_column_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of Y-Axis Data:")
        y_column_label.place(relx=0.45, rely=0.39)

        y_entry = ttk.OptionMenu(body_frame, y1_option, column_choices)
        y_entry.place(relx=0.66, rely=0.39, relwidth=0.3)

        z_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Does the X-Axis Show a Period of Time?:")
        z_label.place(relx=0.01, rely=0.58)

        chart_selection = ttk.OptionMenu(body_frame, line_chart_date, "Please make a selection", "Yes", "No")
        chart_selection.place(relx=0.36, rely=0.58, relwidth=0.25)

        # Create a drop down menu
        chart_selection = ttk.OptionMenu(body_frame, sum_mean, "Please make a selection", "None", "Sum", "Mean")
        chart_selection.place(relx=0.65, rely=0.58, relwidth=0.25)

        limit_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Would you like to place a limit?")
        limit_label.place(relx=0.01, rely=0.75)

        chart_selection = ttk.OptionMenu(body_frame, limit_menu, "Please make a selection", "Yes", "No")
        chart_selection.place(relx=0.3, rely=0.75, relwidth=0.25)

        value_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Enter a limit, or 0 for none")
        value_label.place(relx=0.6, rely=0.75)

        limit_entry = ttk.Entry(body_frame)
        limit_entry.place(relx=0.84, rely=0.75, relwidth=0.15)

        if for_dash:
            # Create a submit button to send all user entries to a variable
            # The parameters are each of the entries returning their user input
            submit_button = ttk.Button(background, text="Next Page", command=lambda: [submit_info(chart_title_entry.get(),
                                                                                                  x_title_entry.get(),
                                                                                                  x_option.get(),
                                                                                                  y_title_entry.get(),
                                                                                                  y1_option.get(), None,
                                                                                                  sum_mean.get(),
                                                                                                  limit_menu.get(),
                                                                                                  limit_entry.get(),
                                                                                                  line_chart_date.get(),
                                                                                                  None, None, None, "Line Chart"),
                                                                                      multi_line_number()])
            submit_button.place(relx=0.9, rely=0.92)
        else:
            submit_button = ttk.Button(background, text="Submit", command=lambda: submit_info(chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y1_option.get(), None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(), None,
                                                                                              None, None, "Line Chart"))
            submit_button.place(relx=0.9, rely=0.92)


    def multi_line(num_lines):

        count = int(num_lines)

        y_data_label = [None] * count
        y_entry = [None] * count
        y_name_label = [None] * count
        y_name_entry = [None] * count
        y_array = []
        y_option_var = [y1_option, y2_option, y3_option, y4_option]

        clear()
        # The two lines of code below create an empty background frame that can be added to
        # Widgets should be added to background so the clear method can delete the frame for a new page
        # The two lines of code below create an empty background frame that can be added to
        # Widgets should be added to background so the clear method can delete the frame for a new page
        background = tk.Frame(window, bg='#10435e')
        background.place(relwidth=1, relheight=1)

        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = ttk.Button(background, text="Back", command=back_front_page)
        bck_button.place(relx=0.01, rely=0.92, relwidth=0.05)

        # Create a title label to be placed at the top of the page
        title_label = tk.Label(background, bg='#10435e', fg='white', text="Multi-Line Chart")
        font_style = ('', 20)  # configure font size
        title_label.config(font=font_style)  # change the font size of the title
        title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

        # Create a frame for the widgets on this page to be placed in
        body_frame = tk.Frame(background, bg='#10435e')
        body_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')

        # Create a label to indicate to the user to enter the file path
        file_path_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Please Select a File:")
        file_path_label.place(relx=0.01, rely=0.01)

        # Create a button for the user to select the file.
        if count == 2:
            file_path_entry= ttk.Button(body_frame, text="Select file", command=lambda: [file_selector(file_path_entry),
                                                                                          update_dropdown(x_entry, x_option),
                                                                                          update_dropdown(y_entry[0], y1_option),
                                                                                         update_dropdown(y_entry[1], y2_option)])
        elif count == 3:
            file_path_entry = ttk.Button(body_frame, text="Select file", command=lambda: [file_selector(file_path_entry),
                                                                                          update_dropdown(x_entry, x_option),
                                                                                          update_dropdown(y_entry[0], y1_option),
                                                                                          update_dropdown(y_entry[1], y2_option),
                                                                                          update_dropdown(y_entry[2], y2_option)])
        elif count == 4:
            file_path_entry = ttk.Button(body_frame, text="Select file", command=lambda: [file_selector(file_path_entry),
                                                                                          update_dropdown(x_entry, x_option),
                                                                                          update_dropdown(y_entry[0], y1_option),
                                                                                          update_dropdown(y_entry[1], y2_option),
                                                                                          update_dropdown(y_entry[2], y2_option),
                                                                                          update_dropdown(y_entry[3], y2_option)])


        file_path_entry.place(relx=0.19, rely=0.01, relwidth=0.40)

        chart_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Chart Title:")
        chart_title_label.place(relx=0.6, rely=0.01)

        chart_title_entry = ttk.Entry(body_frame)
        chart_title_entry.place(relx=0.701, rely=0.01, relwidth=0.25)

        x_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="X Axis Title:")
        x_title_label.place(relx=0.01, rely=0.1)

        x_title_entry = ttk.Entry(body_frame)
        x_title_entry.place(relx=0.12, rely=0.1, relwidth=0.3)

        x_column_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of X-Axis Data:")
        x_column_label.place(relx=0.45, rely=0.1)

        x_entry = ttk.OptionMenu(body_frame, x_option, column_choices)
        x_entry.place(relx=0.66, rely=0.1, relwidth=0.3)

        y_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Y Axis Title:")
        y_title_label.place(relx=0.01, rely=0.2)

        y_title_entry = ttk.Entry(body_frame)
        y_title_entry.place(relx=0.12, rely=0.2, relwidth=0.3)

        for i in range(count):
            number = str(i+1)

            y_data_label[i] = tk.Label(body_frame, bg='#10435e', fg='white', text="Y"+number+" data:")
            y_data_label[i].place(relx=0.55, rely=(.3+(.1*i)))

            y_entry[i] = ttk.OptionMenu(body_frame, y_option_var[i], column_choices)
            y_entry[i].place(relx=0.66, rely=(.3+(.1*i)), relwidth=0.3)

            y_name_label[i] = tk.Label(body_frame, bg='#10435e', fg='white', text="Y" + number + " Label:")
            y_name_label[i].place(relx=.01, rely=(.3+(.1*i)))

            y_name_entry[i] = ttk.Entry(body_frame)
            y_name_entry[i].place(relx=0.12, rely=(.3+(.1*i)), relwidth=0.3)


        z_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Does the X-Axis Show a Period of Time?:")
        z_label.place(relx=0.01, rely=0.7)

        chart_selection = ttk.OptionMenu(body_frame, line_chart_date, "Please make a selection", "Yes", "No")
        chart_selection.place(relx=0.36, rely=0.7, relwidth=0.25)

        # Create a drop down menu
        chart_selection = ttk.OptionMenu(body_frame, sum_mean, "Please make a selection", "None", "Sum", "Mean")
        chart_selection.place(relx=0.65, rely=0.7, relwidth=0.25)

        limit_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Would you like to place a limit?")
        limit_label.place(relx=0.01, rely=0.8)

        chart_selection = ttk.OptionMenu(body_frame, limit_menu, "Please make a selection", "Yes", "No")
        chart_selection.place(relx=0.3, rely=0.8, relwidth=0.25)

        value_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Enter a limit, or 0 for none")
        value_label.place(relx=0.6, rely=0.8)

        limit_entry = ttk.Entry(body_frame)
        limit_entry.place(relx=0.84, rely=0.8, relwidth=0.15)

        if for_dash:
            # Create a submit button to send all user entries to a variable
            # The parameters are each of the entries returning their user input
            # each if loop checks how many lines there are, and makes the submit command get all appropriate y_data and
            # place it in the proper place in an array to pass to submit_info
            if count == 2:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get()]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get()]),
                                                                                          submit_info(chart_title_entry.get(),
                                                                                                      x_title_entry.get(),
                                                                                                      x_option.get(),
                                                                                                      y_title_entry.get(),
                                                                                                      y_array, None,
                                                                                                      sum_mean.get(),
                                                                                                      limit_menu.get(),
                                                                                                      limit_entry.get(),
                                                                                                      line_chart_date.get(),
                                                                                                      None, None, None, "Multi Line"),
                                                                                          stacked_bar_number()])
            elif count == 3:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get()]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get()]),
                                                                                          y_array.append([y3_option.get(),
                                                                                                          y_name_entry[2].get()]),
                                                                                          submit_info(
                                                                                              chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y_array, None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(),
                                                                                              None, None, None, "Multi Line"),
                                                                                          stacked_bar_number()])
            else:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get()]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get()]),
                                                                                          y_array.append([y3_option.get(),
                                                                                                          y_name_entry[2].get()]),
                                                                                          y_array.append([y4_option.get(),
                                                                                                          y_name_entry[3].get()]),
                                                                                          submit_info(
                                                                                              chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y_array, None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(),
                                                                                              None, None, None, "Multi Line"),
                                                                                          stacked_bar_number()])
            submit_button.place(relx=0.9, rely=0.92)
        else:
            # each if loop checks how many lines there are, and makes the submit command get all appropriate y_data and
            # place it in the proper place in an array to pass to submit_info
            if count == 2:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get()]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get()]),
                                                                                          submit_info(
                                                                                              chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y_array, None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(),
                                                                                              None, None, None, "Multi Line")])
            elif count == 3:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get()]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get()]),
                                                                                          y_array.append([y3_option.get(),
                                                                                                          y_name_entry[2].get()]),
                                                                                          submit_info(
                                                                                              chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y_array, None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(),
                                                                                              None, None, None, "Multi Line")])
            else:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get()]),
                                                                                          y_array.append([y2_option.get().get(),
                                                                                                          y_name_entry[1].get()]),
                                                                                          y_array.append([y3_option.get().get(),
                                                                                                          y_name_entry[2].get()]),
                                                                                          y_array.append([y4_option.get().get(),
                                                                                                          y_name_entry[3].get()]),
                                                                                          submit_info(
                                                                                              chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y_array, None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(),
                                                                                              None, None, None, "Multi Line")])

            submit_button.place(relx=0.9, rely=0.92)


        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = tk.Button(background, text="Back", command=front_page)
        bck_button.place(relx=0.01, rely=0.92)


    def stacked_bar(num_bars):

        count = int(num_bars)

        y_option_var = [y1_option, y2_option, y3_option, y4_option]
        y_data_label = [None] * count
        y_entry = [None] * count
        y_name_label = [None] * count
        y_name_entry = [None] * count
        y_array = []
        y_color_button = [None] * count

        clear()
        # The two lines of code below create an empty background frame that can be added to
        # Widgets should be added to background so the clear method can delete the frame for a new page
        # The two lines of code below create an empty background frame that can be added to
        # Widgets should be added to background so the clear method can delete the frame for a new page
        background = tk.Frame(window, bg='#10435e')
        background.place(relwidth=1, relheight=1)

        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = ttk.Button(background, text="Back", command=back_front_page)
        bck_button.place(relx=0.01, rely=0.92, relwidth=0.05)

        # Create a title label to be placed at the top of the page
        title_label = tk.Label(background, bg='#10435e', fg='white', text="Stacked Bar Chart")
        font_style = ('', 20)  # configure font size
        title_label.config(font=font_style)  # change the font size of the title
        title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

        # Create a frame for the widgets on this page to be placed in
        body_frame = tk.Frame(background, bg='#10435e')
        body_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')

        # Create a label to indicate to the user to enter the file path
        file_path_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Please Select a File:")
        file_path_label.place(relx=0.01, rely=0.01)

        if count == 2:
            file_path_entry = ttk.Button(body_frame, text="Select file", command=lambda: [file_selector(file_path_entry),
                                                                                          update_dropdown(x_entry,
                                                                                                          x_option),
                                                                                          update_dropdown(y_entry[0],
                                                                                                          y1_option),
                                                                                          update_dropdown(y_entry[1],
                                                                                                          y2_option)])
        elif count == 3:
            file_path_entry = ttk.Button(body_frame, text="Select file", command=lambda: [file_selector(file_path_entry),
                                                                                          update_dropdown(x_entry,
                                                                                                          x_option),
                                                                                          update_dropdown(y_entry[0],
                                                                                                          y1_option),
                                                                                          update_dropdown(y_entry[1],
                                                                                                          y2_option),
                                                                                          update_dropdown(y_entry[2],
                                                                                                          y2_option)])
        elif count == 4:
            file_path_entry = ttk.Button(body_frame, text="Select file", command=lambda: [file_selector(file_path_entry),
                                                                                          update_dropdown(x_entry,
                                                                                                          x_option),
                                                                                          update_dropdown(y_entry[0],
                                                                                                          y1_option),
                                                                                          update_dropdown(y_entry[1],
                                                                                                          y2_option),
                                                                                          update_dropdown(y_entry[2],
                                                                                                          y2_option),
                                                                                          update_dropdown(y_entry[3],
                                                                                                          y2_option)])

        file_path_entry.place(relx=0.19, rely=0.01, relwidth=0.40)

        chart_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Chart Title:")
        chart_title_label.place(relx=0.6, rely=0.01)

        chart_title_entry = ttk.Entry(body_frame)
        chart_title_entry.place(relx=0.701, rely=0.01, relwidth=0.25)

        x_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="X Axis Title:")
        x_title_label.place(relx=0.01, rely=0.1)

        x_title_entry = ttk.Entry(body_frame)
        x_title_entry.place(relx=0.12, rely=0.1, relwidth=0.3)

        x_column_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Column of X-Axis Data:")
        x_column_label.place(relx=0.45, rely=0.1)

        x_entry = ttk.OptionMenu(body_frame, x_option, column_choices)
        x_entry.place(relx=0.66, rely=0.1, relwidth=0.3)

        y_title_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Y Axis Title:")
        y_title_label.place(relx=0.01, rely=0.2)

        y_title_entry = ttk.Entry(body_frame)
        y_title_entry.place(relx=0.12, rely=0.2, relwidth=0.3)


    # popultes the fields based on number of data entries selected.

        for i in range(count):
            number = str(i+1)

            y_data_label[i] = tk.Label(body_frame, bg='#10435e', fg='white', text="Y"+number+" data:")
            y_data_label[i].place(relx=.45, rely=(.3+(.1*i)))

            y_entry[i] = ttk.OptionMenu(body_frame, y_option_var[i], column_choices)
            y_entry[i].place(relx=0.55, rely=(.3+(.1*i)), relwidth=0.3)

            y_name_label[i] = tk.Label(body_frame, bg='#10435e', fg='white', text="Y" + number + " Label:")
            y_name_label[i].place(relx=.01, rely=(.3+(.1*i)))

            y_name_entry[i] = ttk.Entry(body_frame)
            y_name_entry[i].place(relx=0.12, rely=(.3+(.1*i)), relwidth=0.3)

    # Based on current iteration, adds a color selection button. The current index on generation is passed to the get_color
            # function, then the frame is updated to change button color
            if i == 0:
                y_color_button[i] = tk.Button(body_frame, text="Color", command=lambda: [get_color(0, y_color_button),
                                                                                                         body_frame.update()])
                y_color_button[i].place(relx=0.88, rely=(.3+(.1*i)))
            elif i == 1:
                y_color_button[i] = tk.Button(body_frame, text="Color", command=lambda: [get_color(1, y_color_button),
                                                                                                         body_frame.update()])
                y_color_button[i].place(relx=0.88, rely=(.3+(.1*i)))
            elif i == 2:
                y_color_button[i] = tk.Button(body_frame, text="Color", command=lambda: [get_color(2, y_color_button),
                                                                                                         body_frame.update()])
                y_color_button[i].place(relx=0.88, rely=(.3+(.1*i)))
            elif i == 3:
                y_color_button[i] = tk.Button(body_frame, text="Color", command=lambda: [get_color(3, y_color_button),
                                                                                                         body_frame.update()])
                y_color_button[i].place(relx=0.88, rely=(.3+(.1*i)))


        z_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Does the X-Axis Show a Period of Time?:")
        z_label.place(relx=0.01, rely=0.7)

        chart_selection = ttk.OptionMenu(body_frame, line_chart_date, "Please make a selection", "Yes", "No")
        chart_selection.place(relx=0.36, rely=0.7, relwidth=0.25)

        # Create a drop down menu
        chart_selection = ttk.OptionMenu(body_frame, sum_mean, "Please make a selection", "None", "Sum", "Mean")
        chart_selection.place(relx=0.65, rely=0.7, relwidth=0.25)

        limit_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Would you like to place a limit?")
        limit_label.place(relx=0.01, rely=0.8)

        chart_selection = ttk.OptionMenu(body_frame, limit_menu, "Please make a selection", "Yes", "No")
        chart_selection.place(relx=0.3, rely=0.8, relwidth=0.25)

        value_label = tk.Label(body_frame, bg='#10435e', fg='white', text="Enter a limit, or 0 for none")
        value_label.place(relx=0.6, rely=0.8)

        limit_entry = ttk.Entry(body_frame)
        limit_entry.place(relx=0.84, rely=0.8, relwidth=0.15)

        if for_dash:
            # Create a submit button to send all user entries to a variable
            # The parameters are each of the entries returning their user input
            # each if loop checks how many lines there are, and makes the submit command get all appropriate y_data and
            # place it in the proper place in an array to pass to submit_info
            if count == 2:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get(),
                                                                                                          stack_color[0]]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get(),
                                                                                                          stack_color[1]]),
                                                                                          submit_info(chart_title_entry.get(),
                                                                                                      x_title_entry.get(),
                                                                                                      x_option.get(),
                                                                                                      y_title_entry.get(),
                                                                                                      y_array, None,
                                                                                                      sum_mean.get(),
                                                                                                      limit_menu.get(),
                                                                                                      limit_entry.get(),
                                                                                                      line_chart_date.get(),
                                                                                                      None, None, None, "Stack Bar"),
                                                                                          request.request_dash(dash_data)])
            elif count == 3:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get(),
                                                                                                          stack_color[0]]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get(),
                                                                                                          stack_color[1]]),
                                                                                          y_array.append([y3_option.get(),
                                                                                                          y_name_entry[2].get(),
                                                                                                          stack_color[2]]),
                                                                                          submit_info(
                                                                                              chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y_array, None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(),
                                                                                              None, None, None, "Stack Bar"),
                                                                                          request.request_dash(dash_data)])
            else:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get(),
                                                                                                          stack_color[0]]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get(),
                                                                                                          stack_color[1]]),
                                                                                          y_array.append([y3_option.get(),
                                                                                                          y_name_entry[2].get(),
                                                                                                          stack_color[2]]),
                                                                                          y_array.append([y4_option.get(),
                                                                                                          y_name_entry[3].get(),
                                                                                                          stack_color[3]]),
                                                                                          submit_info(
                                                                                              chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y_array, None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(),
                                                                                              None, None, None, "Stack Bar"),
                                                                                          request.request_dash(dash_data)])
            submit_button.place(relx=0.9, rely=0.92)
        else:
            # each if loop checks how many lines there are, and makes the submit command get all appropriate y_data and
            # place it in the proper place in an array to pass to submit_info
            if count == 2:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get(),
                                                                                                          stack_color[0]]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get(),
                                                                                                          stack_color[1]]),
                                                                                          submit_info(
                                                                                              chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y_array, None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(),
                                                                                              None, None, None, "Stack Bar")])
            elif count == 3:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get(),
                                                                                                          stack_color[0]]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get(),
                                                                                                          stack_color[1]]),
                                                                                          y_array.append([y3_option.get(),
                                                                                                          y_name_entry[2].get(),
                                                                                                          stack_color[2]]),
                                                                                          submit_info(
                                                                                              chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y_array, None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(),
                                                                                              None, None, None, "Stack Bar")])
            else:
                submit_button = ttk.Button(background, text="Next Page", command=lambda: [y_array.append([y1_option.get(),
                                                                                                          y_name_entry[0].get(),
                                                                                                          stack_color[0]]),
                                                                                          y_array.append([y2_option.get(),
                                                                                                          y_name_entry[1].get(),
                                                                                                          stack_color[1]]),
                                                                                          y_array.append([y3_option.get(),
                                                                                                          y_name_entry[2].get(),
                                                                                                          stack_color[2]]),
                                                                                          y_array.append([y4_option.get(),
                                                                                                          y_name_entry[3].get(),
                                                                                                          stack_color[3]]),
                                                                                          submit_info(
                                                                                              chart_title_entry.get(),
                                                                                              x_title_entry.get(),
                                                                                              x_option.get(),
                                                                                              y_title_entry.get(),
                                                                                              y_array, None,
                                                                                              sum_mean.get(),
                                                                                              limit_menu.get(),
                                                                                              limit_entry.get(),
                                                                                              line_chart_date.get(),
                                                                                              None, None, None, "Stack Bar")])

            submit_button.place(relx=0.9, rely=0.92)


        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = tk.Button(background, text="Back", command=front_page)
        bck_button.place(relx=0.01, rely=0.92)


    def dashboard():
        global for_dash
        for_dash = 1  # changes the value to 1 so that charts will be generated for the dashboard
        clear()
        # The two lines of code below create an empty background frame that can be added to
        # Widgets should be added to background so the clear method can delete the frame for a new page
        background = tk.Frame(window, bg='#10435e')
        background.place(relwidth=1, relheight=1)

        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = ttk.Button(background, text="Back", command=back_front_page)
        bck_button.place(relx=0.01, rely=0.92, relwidth=0.05)

        # Create a title label to be placed at the top of the page
        title_label = tk.Label(background, bg='#10435e', fg='white', text="Dashboard Generation")
        font_style = ('', 20)  # configure font size
        title_label.config(font=font_style)  # change the font size of the title
        title_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.2, anchor='n')

        title_entry_label = tk.Label(background, bg='#10435e', fg='white', text="Please Enter a Title for the Dashboard:")
        title_entry_label.place(relx=0.1, rely=0.3)

        title_entry = ttk.Entry(background)
        title_entry.place(relx=0.37, rely=0.3, relwidth=0.3)

        # Create a button that will get the chart selected from the menu
        next_button = ttk.Button(background, text="Next Page", command=lambda: [set_dash_title(title_entry.get()),
                                                                                bar_chart()])
        # places the button in the lower right corner of the screen
        next_button.place(relx=0.9, rely=0.92)

        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = tk.Button(background, text="Back", command=front_page)
        bck_button.place(relx=0.01, rely=0.92)


    def multi_line_number():

        clear()

        background = tk.Frame(window, bg='#10435e')
        background.place(relwidth=1, relheight=1)

        # Create a new label to hold the title text
        title = tk.Label(background, bg='#10435e', fg='white', text="Project Carrot")
        font_style = ('', 25)  # can be used to edit font style, '' can be replaced with a new font name
        title.config(font=font_style)  # applies the new font style
        # places the label in the top middle of the screen
        title.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.15, anchor='n')

        # Creates a new frame to hold new widgets
        lower_frame = tk.Frame(background, bg='#10435e')
        # Places the frame near the center of the screen
        lower_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')

        # Creates a label indicating to the user to select a chart type
        text = tk.Label(lower_frame, bg='#10435e', fg='white', text="Please select the number of data sources for"
                                                                    "the multi-line chart: ")
        font_style = ('', 12)
        text.config(font=font_style)
        text.place(relx=0.5, rely=0.35, anchor='n')

        # Creates a menu with the charts as options
        chart_selection = ttk.OptionMenu(lower_frame, option, "Select a Number", "2", "3",
                                         "4")
        chart_selection.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.15, anchor='n')

        # Create a button that will get the chart selected from the menu
        next_button = ttk.Button(background, text="Next Page", command=lambda: multi_line(option.get()))
        # places the button in the lower right corner of the screen
        next_button.place(relx=0.9, rely=0.92)

        # Creates a back button to allow the user to go back to the chart selection page
        bck_button = tk.Button(background, text="Back", command=front_page)
        bck_button.place(relx=0.01, rely=0.92)

    def stacked_bar_number():

        clear()

        background = tk.Frame(window, bg='#10435e')
        background.place(relwidth=1, relheight=1)

        # Create a new label to hold the title text
        title = tk.Label(background, bg='#10435e', fg='white', text="Project Carrot")
        font_style = ('', 25)  # can be used to edit font style, '' can be replaced with a new font name
        title.config(font=font_style)  # applies the new font style
        # places the label in the top middle of the screen
        title.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.15, anchor='n')

        # Creates a new frame to hold new widgets
        lower_frame = tk.Frame(background, bg='#10435e')
        # Places the frame near the center of the screen
        lower_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')

        # Creates a label indicating to the user to select a chart type
        text = tk.Label(lower_frame, bg='#10435e', fg='white', text="Please select the number of data sources for"
                                                                    "the Stacked Bar chart: ")
        font_style = ('', 12)
        text.config(font=font_style)
        text.place(relx=0.5, rely=0.35, anchor='n')

        # Creates a menu with the charts as options
        chart_selection = ttk.OptionMenu(lower_frame, option, "Select a Number", "2", "3",
                                         "4")
        chart_selection.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.15, anchor='n')

        # Create a button that will get the chart selected from the menu
        next_button = ttk.Button(background, text="Next Page", command=lambda: stacked_bar(option.get()))
        # places the button in the lower right corner of the screen
        next_button.place(relx=0.9, rely=0.92)

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
            multi_line_number()

        elif option.get() == "Stacked Bar Chart":
            stacked_bar_number()

        elif option.get() == "Dashboard":
            dashboard()

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
            button = ttk.Button(error_box, text="OK", command=error_box.destroy)
            button.place(relx=0.5, rely=0.5, anchor='n')


    # This method gets the data from the heat map entry widgets to populate the dictionary that can be handled by the
    # RequestHandler.py
    # The chart key should be different depending on which chart calls this method so that the correct method from the
    # RequestHandler.py can be called
    def submit_info(chart_title, x_title, x, y_title, y, z, sum_or_mean, limit_option, limit_value, date, marker, category,
                    sort, chart_key):
        global for_dash

        chart_data['title'] = chart_title
        chart_data['x_title'] = x_title
        chart_data['x'] = x
        chart_data['y_title'] = y_title
        chart_data['y'] = y
        chart_data['z'] = z
        chart_data['marker_data'] = marker
        chart_data['category'] = category
        chart_data['sort'] = sort

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
            if int(limit_value) == 0:
                chart_data['limit'] = 0
            else:
                chart_data['limit_num'] = int(limit_value)

        # Reads the chart key to determine which type of chart should be generated from the request handler
        if chart_key == "Bar Chart":
            if for_dash:  # Checks to see if the chart will be generated as a dashboard
                dash_data['bar'] = request.request_bar(chart_data, for_dash)  # stores data inside global dictionary
            else:
                request.request_bar(chart_data, for_dash)
        elif chart_key == "Bubble Chart":
            if for_dash:
                dash_data['bubble'] = request.request_bubble(chart_data, for_dash)
            else:
                request.request_bubble(chart_data, for_dash)
        elif chart_key == "Heat Map":
            if for_dash:
                dash_data['heat'] = request.request_heat(chart_data, for_dash)
            else:
                request.request_heat(chart_data, for_dash)
        elif chart_key == "Line Chart":

            request.request_line(chart_data, 0)
        elif chart_key == "MultiLine Chart":
            request.request_multi(chart_data, 0)
        elif chart_key == "Stacked Bar Chart":
            request.request_stack(chart_data, 0)
            if for_dash:
                dash_data['line'] = request.request_line(chart_data, for_dash)
            else:
                request.request_line(chart_data, for_dash)
        elif chart_key == "Multi Line":
            if for_dash:
                dash_data['multi'] = request.request_multi(chart_data, for_dash)
            else:
                request.request_multi(chart_data, for_dash)
        elif chart_key == "Stack Bar":
            if for_dash:
                dash_data['stack'] = request.request_stack(chart_data, for_dash)
            else:
                request.request_stack(chart_data, for_dash)



    # Function that can be called by a button or other widget that will allow the user to select the file they
    # wish to open, this function will change the value in the global dictionary
    # This function is used so that the user does not have to type the file path themselves
    def file_selector(button):
        chart_data['file'] = filedialog.askopenfilename()
        if chart_data['file'] == '':
            return
        button_update = chart_data['file'].split('/')
        print(button_update)
        button_update = "../"+button_update[-2]+"/"+button_update[-1]
        button.config(text = button_update)
        df = pd.read_csv(chart_data['file'])
        array = list(df.columns)
        for x in array:
            column_choices.append(x)

    def update_dropdown(dropdown, option_var):
        menu = dropdown["menu"]
        for x in column_choices:
            menu.add_command(label=x, command=lambda value=x: option_var.set(value))



    def set_dash_title(title):
        dash_data['dash_title'] = title


    # Takes in the index of the calling button (specified in the for loop in stacked_bar(), and uses it to assign
    # a color to the corresponding stack_color nased on the tkinter colorpicker. Then, sets the color of the calling button
    # to the selected color.
    def get_color(index, button_array):
        stack_color[index] = askcolor()[1]
        button_array[index].config(bg=stack_color[index])

    def back_front_page():
        column_choices.clear()
        column_choices.append('Select a File')
        front_page()

    # Create a global dictionary that can be sent to RequestHandler.py
    chart_data = {'file': None, 'title': None, 'x_title': None, 'x': None, 'y_title': None, 'y': None, 'z': None,
                  'sum': 0, 'mean': 0, 'limit': 0, 'limit_num': 0, 'date': 0, 'marker_data': None, 'category': None,
                  'sort': None, 'y_array': None}
    dash_data = {'bar': None, 'bubble': None, 'heat': None, 'line': None, 'multi': None, 'stack': None, 'dash_title': None}

    column_choices = ['Select a File']

    stack_color = ['','','','']
    # Create a new window
    window = tk.Tk()

    # Change the title of the window
    window.title("Project Carrot")
    # Changes the icon in upper left corner for Windows users
    # window.iconbitmap(default="icon.ico")
    # Creates a tkinter variable to be used in drop down menu for chart selection on front page
    option = tk.StringVar(window)
    # Creates a tkinter variable to be used in drop down menu to select a sum or mean
    sum_mean = tk.StringVar(window)
    # Creates a tkinter variable to be used in the drop down menu to select whether a limit should be used
    limit_menu = tk.StringVar(window)
    # Creates a tkinter variable to be used in the drop down menu to select date for line_chart()
    line_chart_date = tk.StringVar(window)

    # Creates a tkinter variable to be used in the drop down menu to select whether the chart will be sorted
    sort_menu = tk.StringVar(window)

    # Creates a tkinter variable to be used in the drop down menu to select X data column
    x_option = tk.StringVar(window)

    # Creates a tkinter variable to be used in the drop down menu to select y data columns

    y1_option = tk.StringVar(window)
    y2_option = tk.StringVar(window)
    y3_option = tk.StringVar(window)
    y4_option = tk.StringVar(window)

    z_option = tk.StringVar(window)
    category_option = tk.StringVar(window)
    marker_option = tk.StringVar(window)
    # Holds a boolean value to determine if the charts should be generated for a dashboard
    # if the user selects a dashboard on the front page the value changes to 1
    for_dash = 0

    # Create a canvas to adjust the window size
    window_size = tk.Canvas(window, width=800, height=400)
    window_size.pack()

    # Create a frame to act as the background for GUI
    background = tk.Frame(window, bg='#10435e')
    # The background takes up the entire window, all widgets will be placed inside this frame
    background.place(relwidth=1, relheight=1)

    front_page()

    window.mainloop()

