import tkinter as tk


# Function used to clear the window and replace it with an empty frame
# Can be used to create a new page
def clear():
    background.destroy()
    rebuild()


# Creates an empty frame covering the full size of the window
def rebuild():
    background = tk.Frame(window)
    background.place(relwidth=1, relheight=1)


def front_page():
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
    text.place(relx=0.5, rely=0.35, anchor='n')

    option.set("Select a Chart")  # sets the default text on the menu selection
    # Creates a menu with the charts as options
    chart_selection = tk.OptionMenu(lower_frame, option, "Bar Chart", "Bubble Chart", "Heat Map", "Line Chart",
                                    "MultiLine Chart", "Stacked Bar Chart")
    chart_selection.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.1, anchor='n')

    # Create a button that will get the chart selected from the menu
    next_button = tk.Button(background, text="Next Page", command=get_chart)
    # places the button in the lower right corner of the screen
    next_button.place(relx=0.91, rely=0.92)


def bar_chart():
    clear()


# Function used to get the chart that the user selected from the option menu
def get_chart():
    print("The Chart selected is: ", option.get())


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
