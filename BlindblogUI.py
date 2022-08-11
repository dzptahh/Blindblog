import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import ttk
import matplotlib.pyplot
from matplotlib.figure import Figure
from tkinter.scrolledtext import ScrolledText
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Canvas, PhotoImage

matplotlib.use('TkAgg')


class File:
    """For open files text"""

    def __init__(self):
        self.lines = []
        with open('10facts.txt', 'r') as f:
            self.lines = f.readlines()
        self.lines_2 = []
        with open('info.txt', 'r') as f:
            self.lines_2 = f.readlines()


class PageUI(tk.Tk):
    def __init__(self, blinds: File):
        super().__init__()
        self.blinder = pd.read_csv("registered-blind-and-partially-sighted-people-by-age-group.csv")
        self.blind = blinds
        self.title('Blindblog')
        self.component_3()

    def init_components(self):
        """Page about 10 facts"""
        self.geometry("1000x700")
        self.clear_frame()

        # set the label as background
        frame1 = tk.Frame(bd=0, highlightthickness=0, background="#EEF4ED")
        frame1.place(x=0, y=0, relwidth=1.0, relheight=.5, anchor="nw")
        frame2 = tk.Frame(bd=0, highlightthickness=0, background="#F2EFC7")
        frame2.place(x=0, rely=.5, relwidth=1.0, relheight=.5, anchor="nw")
        heading = tk.Label(self, text='BLINDBLOG - 10 facts about blindness', font=('Garamond', 36),
                           foreground='#36827F', background='#EEF4ED')
        heading.pack(padx=12, pady=12, fill=tk.BOTH)

        # create button
        page_st_button = tk.Button(self, width=45, height=2, text='Next Page', fg='#3a86ff', command=self.component_4)
        page_st_button.pack(side='bottom', pady=7)

        # create ScrolledText and insert text
        st = ScrolledText(self, width=10, height=20, font=('Verdana', 16), foreground='#36827F')
        st.pack(padx=12, pady=7, fill=tk.BOTH, side='top', expand=True)
        for i in self.blind.lines:
            st.insert(tk.END, str(i) + "\n")
        st['state'] = 'disable'  # the text can't rewrite

    def component_2(self):
        """Page for plotting"""
        self.geometry("1000x700")
        self.clear_frame()

        # set quit button for exit the program
        self.quit = tk.Button(self, text="Quit", fg='#3a86ff', command=self.destroy)
        self.quit.pack(side='bottom', expand=False, pady=4)

        # set previous button
        button2 = tk.Button(self, width=45, text='Previous Page', fg='#3a86ff', command=self.component_4)
        button2.pack(side='bottom', pady=7, expand=False)

        self.for_plot_graph()
        self.pic(self)

    def component_3(self):
        """Login page"""
        self.geometry("400x400")
        self.clear_frame()
        frame = tk.Frame(bd=0, highlightthickness=0, background="#F3EFE0")
        frame.place(x=0, rely=.6, relwidth=1.0, relheight=.5, anchor="nw")

        text = tk.Label(self, text="Enter the details", font=('Garamond', 36, 'bold'), fg='#3A405A')
        text.pack(pady=5)

        # create register system
        username = tk.StringVar()
        password = tk.StringVar()

        # set username label and username entry
        username_label = tk.Label(self, text="Username", fg='#99B2DD')
        username_label.pack()
        self.entry_username = tk.Entry(self, textvariable=username, fg='#E9AFA3')
        self.entry_username.pack()

        # set password label and password entry
        password_label = tk.Label(self, text="Password", fg='#99B2DD')
        password_label.pack()
        self.entry_password = tk.Entry(self, textvariable=password, fg='#E9AFA3', show='*')
        self.entry_password.pack()

        # set button
        register_button = tk.Button(self, width=10, height=1, text='Register', fg='#685044',
                                    command=self.handler)
        register_button.pack(pady=7)

        # set quit button
        self.quit = tk.Button(self, text="log out", fg='#685044', command=self.destroy)
        self.quit.pack(expand=False)

    def handler(self):
        # set the conditions for username and password
        if self.entry_username.get() != "" and self.entry_password.get() != "":
            self.init_components()
        else:
            fail = tk.Label(self, text='Registration fail', fg='red')
            fail.pack()
            self.after(2000, fail.destroy)

    def component_4(self):
        """Page for information"""
        self.clear_frame()
        self.geometry("1000x700")
        tk.Frame(background="#F7F3E3", bd=0, highlightthickness=0).place(x=0, rely=.6, relwidth=1.0, relheight=.5,
                                                                         anchor="nw")
        head = tk.Label(self, text='What You Need to Know About Blindness', font=('Garamond', 36, 'bold'), fg='#A8763E')
        head.pack()

        # set button
        button = tk.Button(self, width=45, text='Next Page', fg='#3a86ff', command=self.component_2)
        button.pack(side='bottom', pady=7)
        button2 = tk.Button(self, width=45, text='Previous Page', fg='#3a86ff', command=self.init_components)
        button2.pack(side='bottom', pady=7, expand=False)

        # set scrolled-text
        st = ScrolledText(self, width=10, height=20, font=('Verdana', 16), foreground='#083D77')
        st.pack(padx=12, pady=7, fill=tk.BOTH, side='top', expand=True)
        for i in self.blind.lines_2:
            st.insert(tk.END, str(i) + "\n")
        st['state'] = 'disable'  # the text can't rewrite

    def clear_frame(self):
        # clear frame for next page
        for widgets in self.winfo_children():
            widgets.destroy()

    def for_plot_graph(self):
        # create filter
        self.frame_filter = ttk.LabelFrame(self, text="Select Topic")
        self.frame_filter.pack(fill='both', side='top')

        # create label
        label1 = ttk.Label(self.frame_filter, text="Topic")
        label1.pack(fill='both', side='top')

        # create combobox
        self.cbb = tk.StringVar()
        self.cbb1 = ttk.Combobox(self, width=18)
        self.cbb1['state'] = 'readonly'
        self.cbb1.pack(fill='both', side='top', expand=False)
        self.cbb1.bind('<<ComboboxSelected>>', self.update)

        # load columns for plot graph
        self.load_data()

        # Matplotlib of blindness
        self.fig_blindness = Figure()
        self.axis_blindness = self.fig_blindness.add_subplot()
        self.fig_canvas1 = FigureCanvasTkAgg(self.fig_blindness, master=self)
        self.fig_canvas1.get_tk_widget().pack(fill='both')

    def plot_blindness(self):
        self.axis_blindness.clear()
        self.fig_blindness.subplots_adjust(bottom=0.50)
        blinder = self.blinder
        sett = blinder.set_index("Area")
        gett = sett[self.cbb1.get()]
        gett.plot.bar(ax=self.axis_blindness)
        self.axis_blindness.set(xlabel='Area',
                                title='Registered blind and partially sighted people')
        plt.xticks(rotation=90)
        self.fig_canvas1.draw()

    def load_data(self):
        # load all column
        lst = []
        select_ = self.blinder.columns[2:]
        for i in select_:
            lst.append(i)
        self.cbb1['values'] = lst

    def update(self, blind):
        self.plot_blindness()

    def pic(self, pics):
        # add picture
        self.canvas = Canvas(pics, width=500, height=1000)
        self.canvas.pack(side='bottom', expand=True)
        self.image = PhotoImage(file='blinder.png')
        self.canvas.create_image(180, 200, image=self.image)

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    blind = File()
    ui = PageUI(blind)
    ui.run()
