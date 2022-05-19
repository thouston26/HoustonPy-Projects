import tkinter

import tkinter.messagebox


class GUI:
    def __init__(self):
        # create a main window

        self.main_window = tkinter.Tk()
        # Create the three frames

        self.frame1 = tkinter.Frame(self.main_window)

        self.frame2 = tkinter.Frame(self.main_window)

        self.frame3 = tkinter.Frame(self.main_window)
        # create the Labels widgets to display the text

        self.label1 = tkinter.Label(self.frame1, text ='Enter Celcius Calue:')
        # create the Entries to get the input from user.

        self.entry1 = tkinter.Entry(self.frame1, width = 10)
        # call the pack method of label1 and arrange

        # the widget horizontally from the left of the frame

        self.label1.pack(side='left')

        # call the pack method of entry1 and arrange

        # the widget horizontally from the left of the frame

        self.entry1.pack(side='left')
        # associate StringVar to each buttons

        self.far = tkinter.StringVar()

        self.res = tkinter.Label(self.frame2, text ='The Farenheit value is:')

        # creating a label for the second frame

        self.result = tkinter.Label(self.frame2, textvariable = self.far)

        self.res.pack(side='left')

        # call the pack method of result label and arrange

        # the widget horizontally from the left of the frame

        self.result.pack(side='left')

        self.calc = tkinter.Button(self.frame3, text='Calculate Fahrenheit',command = self.calfahr)
#exit window
        self.quit_button = tkinter.Button(self.frame3, text ='Quit', command=self.main_window.destroy)
        self.calc.pack(side='left')

        # call the pack method of quit_button and arrange

        # the widget horizontally from the left of the frame

        self.quit_button.pack(side='left')

        self.frame1.pack()

        self.frame2.pack()

        self.frame3.pack()
 # create the mainloop for running the program

        tkinter.mainloop()
    def calfahr(self):

        self.test1=float(self.entry1.get())
        self.thisanswer = float((1.8 * (self.test1)) + 32)
        self.far.set(self.thisanswer)
g= GUI()
