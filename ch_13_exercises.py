"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import tkinter

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Sedona Szczepaniak')
        self.label.pack(side='left')
        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = MyGUI2()


# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.top_frame, text='Major: Undecided')
        self.label2 = tkinter.Label(self.bottom_frame, text='AP Physics I')
        self.label3 = tkinter.Label(self.bottom_frame, text='AP Lit')
        self.label4 = tkinter.Label(self.bottom_frame, text='Programming Logic')
        self.label5 = tkinter.Label(self.bottom_frame, text='PE')
        self.label6 = tkinter.Label(self.bottom_frame, text='Spanish IV')
        self.label7 = tkinter.Label(self.bottom_frame, text='Organics/Biochemistry')
        self.label8 = tkinter.Label(self.bottom_frame, text='AP Gov')
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')
        self.label4.pack(side='top')
        self.label5.pack(side='top')
        self.label6.pack(side='top')
        self.label7.pack(side='top')
        self.label8.pack(side='top')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()


if __name__ == '__main__':
    my_gui3 = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class MyGUI4:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.button = tkinter.Button(self.main_window, text='What do you call a dog that does magic?', command=self.punchline)
        self.button.pack()
        tkinter.mainloop()

    def punchline(self):
        self.label = tkinter.Label(self.main_window, text='A Labracadabrador!')
        self.label.pack(side='top')


if __name__ == '__main__':
    my_gui4 = MyGUI4()


# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


import tkinter.messagebox


class MyGUI28:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a measurement in inches:')
        self.inches_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side='left')
        self.inches_entry.pack(side='left')
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        inch = float(self.inches_entry.get())
        centimeters = inch * 2.54
        tkinter.messagebox.showinfo('Results', str(inch) + ' inches is equal to ' + str(centimeters) + ' centimeters.')

if __name__ == '__main__':
    centi_conv = MyGUI28()