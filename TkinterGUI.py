import tkinter
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import time
import matplotlib.animation as animation
from matplotlib import style
from tkinter import *
from tkinter.ttk import *
from mpl_toolkits.mplot3d import Axes3D
from tkinter import filedialog

title = ""
xAxis = ""
yAxis = ""
zAxis = ""
Description = ""

class TinyAnalytics(tk.Tk):

    #NEED
    def updateGraph(self):
        self.frames[Wireframe].updateGraph()

    def clientExit(self):
        exit()

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="TinyAnalytics.ico")
        tk.Tk.wm_title(self, "Tiny Analytics")

        container = tk.Frame(self, bg="orange")
        container.pack(side="top", fill ="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (FirstPage, Wireframe, ScatterPlot, BarGraph, PieChart, Histogram, RadarChart, WireFrameInfo,
                  ScatterPlotInfo, BarGraphInfo, PieChartInfo, HistogramInfo, RadarChartInfo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

        menu = Menu(self)
        self.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Exit', command=self.clientExit)
        menu.add_cascade(label='File', menu=file)

class FirstPage(ttk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        ttk.Style().configure("RB.TButton", foreground='black', background='orange')

        Button1 = ttk.Button(self, text="Wireframe 3 Var", style="RB.TButton",
                            command=lambda: controller.show_frame(WireFrameInfo)).pack()
        Button2 = ttk.Button(self, text="ScatterPlot MultiVar", style="RB.TButton",
                            command=lambda: controller.show_frame(ScatterPlotInfo)).pack()
        Button3 = ttk.Button(self, text="BarGraph MultiVar", style="RB.TButton",
                            command=lambda: controller.show_frame(BarGraphInfo)).pack()
        Button4 = ttk.Button(self, text="PieChart MultiVar", style="RB.TButton",
                            command=lambda: controller.show_frame(PieChartInfo)).pack()
        Button5 = ttk.Button(self, text="Histogram MultiVar", style="RB.TButton",
                            command=lambda: controller.show_frame(HistogramInfo)).pack()
        Button6 = ttk.Button(self, text="RadarChart MultiVar", style="RB.TButton",
                            command=lambda: controller.show_frame(RadarChartInfo)).pack()

        self.configure(background='orange')

class WireFrameInfo(ttk.Frame):

    def FileDialog(self, event):
        file_path = filedialog.askopenfilename()
        Path = ttk.Label(self, text=file_path, background='orange'). place(x=110, y=195)

    #NEED
    def DataInput(self):
        global title
        global xAxis
        global yAxis
        global zAxis
        global Description
        title=self.titleText.get()
        xAxis = self.xAxisText.get()
        yAxis = self.yAxisText.get()
        zAxis = self.zAxisText.get()
        Description = self.descriptionText.get()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        ttk.Style().configure("RB.TButton", foreground='black', background='orange')

        ButtonHome = ttk.Button(self, text="Back", style="RB.TButton")

        fileFile = PhotoImage(file="File.gif")
        buttonFile = Label(self, image = fileFile, background = "orange", foreground = "orange")
        buttonFile.image = fileFile
        buttonFile.bind("<Button-1>", self.FileDialog)
        buttonFile.place(x=580, y=0)

        graphGraph = PhotoImage(file='Graph.gif')
        graphFile = Label(self, image = graphGraph, background = "orange", foreground = "orange")
        graphFile.image = graphGraph
        graphFile.bind("<Button-1>", self.Anything)
        graphFile.place(x=610, y=0)

        backFile = PhotoImage(file="Back.gif")
        buttonBack = Label(self, image = backFile, background = "orange", foreground = "orange")
        buttonBack.image = backFile
        buttonBack.bind("<Button-1>", self.Back)
        buttonBack.place(x=0, y=0)

        bottomBar = Label(self, text = '...', background = "grey", foreground = "white").place(x=0, y=546)

        self.initUI()

    #NEED
    def Anything(self, event):
        plt.title(self.titleText.get(), color = 'black')
        plt.xlabel(self.xAxisText.get(), color = 'black')
        plt.ylabel(self.yAxisText.get(), color = 'black')
        self.controller.updateGraph()
        self.controller.show_frame(Wireframe)

    def Back(self, event):
        self.controller.show_frame(FirstPage)

    def initUI(self):

        self.titleText = StringVar()
        self.titleEntry = Entry(self, textvariable=self.titleText).place(x=110, y=50)

        self.xAxisText = StringVar()
        self.xEntry = Entry(self, textvariable=self.xAxisText).place(x=110, y=70)

        self.yAxisText = StringVar()
        self.yEntry = Entry(self, textvariable=self.yAxisText).place(x=110, y=90)

        self.zAxisText = StringVar()
        self.zEntry = Entry(self, textvariable=self.zAxisText).place(x=110, y=110)

        self.descriptionText = StringVar()
        self.descriptionEntry = Entry(self, textvariable=self.descriptionText).place(x=110, y=130)

        TitleLabel = ttk.Label(self, text="Title").place(x=30, y=50)
        xAxisLabel = ttk.Label(self, text="X Axis").place(x=30, y=70)
        yAxisLabel = ttk.Label(self, text="Y Axis").place(x=30, y=90)
        zAxisLabel = ttk.Label(self, text="Z Axis").place(x=30, y=110)
        DescriptionLabel = ttk.Label(self, text="Description").place(x=30, y=130)

        self.configure(background='orange')

class ScatterPlotInfo(ttk.Frame):

    def fileDialog(self):
        file_path = filedialog.askopenfilename()
        Path = ttk.Label(self, text=file_path, background='orange').place(x=110, y=195)

    def Anything(self):
        plt.title(self.titleText.get(), color = 'black')
        plt.xlabel(self.xAxisText.get(), color = 'black')
        plt.ylabel(self.yAxisText.get(), color = 'black')
        self.controller.updateGraph()
        self.controller.show_frame(ScatterPlot)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.controller = controller

        ttk.Style().configure("RB.TButton", foreground='black', background='orange')

        ButtonHome = ttk.Button(self, text="Back", style="RB.TButton",
                               command=lambda: controller.show_frame(FirstPage)).place(x=0, y=0)

        FileDialog = ttk.Button(self, text="Load File", style = "RB.TButton",
                                command = self.fileDialog).place(x=110, y=170)

        Graph = ttk.Button(self, text="Show Graph", style="RB.TButton",
                           command = self.Anything).pack()

        self.configure(background='orange')

        self.initUI()

    def initUI(self):

        self.titleText = StringVar()
        self.titleEntry = Entry(self, textvariable=self.titleText).place(x=110, y=50)

        self.xAxisText = StringVar()
        self.xEntry = Entry(self, textvariable=self.xAxisText).place(x=110, y=70)

        self.yAxisText = StringVar()
        self.yEntry = Entry(self, textvariable=self.yAxisText).place(x=110, y=90)

        self.zAxisText = StringVar()
        self.zEntry = Entry(self, textvariable=self.zAxisText).place(x=110, y=110)

        self.descriptionText = StringVar()
        self.descriptionEntry = Entry(self, textvariable=self.descriptionText).place(x=110, y=130)

        TitleLabel = ttk.Label(self, text="Title").place(x=30, y=50)
        xAxisLabel = ttk.Label(self, text="X Axis").place(x=30, y=70)
        yAxisLabel = ttk.Label(self, text="Y Axis").place(x=30, y=90)
        zAxisLabel = ttk.Label(self, text="Z Axis").place(x=30, y=110)
        DescriptionLabel = ttk.Label(self, text="Description").place(x=30, y=130)

class BarGraphInfo(ttk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        OK = ttk.Button(self, text="OK",
                            command=lambda: controller.show_frame(BarGraph))

        OK.pack()

class PieChartInfo(ttk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        OK = ttk.Button(self, text="OK",
                            command=lambda: controller.show_frame(PieChart))

        OK.pack()

class HistogramInfo(ttk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        OK = ttk.Button(self, text="OK",
                            command=lambda: controller.show_frame(Histogram))

        OK.pack()

class RadarChartInfo(ttk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        OK = ttk.Button(self, text="OK",
                            command=lambda: controller.show_frame(RadarChart))

        OK.pack()

class Wireframe(ttk.Frame):

    def updateGraph(self):
        self.fig.canvas.draw()

    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text="Wireframe")
        label.pack(pady=10, padx=10)

        ttk.Style().configure("RB.TButton", foreground='black', background='orange')

        ButtonHome = ttk.Button(self, text="Back", style="RB.TButton",
                               command=lambda: controller.show_frame(WireFrameInfo)).place(x=0, y=0)

        #Figure creation and assignment
        self.fig = plt.figure()
        ax = self.fig.add_subplot(111,  projection='3d', axisbg = 'orange')

        #sets background color
        rect = self.fig.patch
        rect.set_facecolor('orange')

        #delta how often we're going to compute the line
        x, y, z = axes3d.get_test_data(0.05)

        #rstride is how often we draw a line
        ax.plot_surface(x, y, z, cmap=cm.autumn, rstride=2, cstride=2, alpha=0.3)
        cset = ax.contour(x, y, z, zdir='z', offset=-100, cmap=cm.autumn)
        cset = ax.contour(z, y, z, zdir='x', offset=-40, cmap=cm.autumn)
        cset = ax.contour(z, y, z, zdir='y', offset=40, cmap=cm.autumn)

        ax.spines['bottom'].set_color('orange')
        ax.spines['right'].set_color('orange')
        ax.spines['left'].set_color('orange')
        ax.spines['top'].set_color('orange')

        ax.set_xlim(-40, 40)
        ax.set_ylim(-40, 40)
        ax.set_zlim(-100, 100)

        style.use("ggplot")

        canvas = FigureCanvasTkAgg(self.fig, self)
        #Canvas border color
        canvas.get_tk_widget().configure(background='orange',  highlightcolor='orange', highlightbackground='orange')
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()

        self.configure(background='orange')

class ScatterPlot(ttk.Frame):

    def __init__(self, parent, controller):

        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="ScatterPlot")
        label.pack(pady=10, padx=10)

        ttk.Style().configure("RB.TButton", foreground='black', background='orange')

        ButtonHome = ttk.Button(self, text="Back", style="RB.TButton",
                               command=lambda: controller.show_frame(ScatterPlotInfo)).place(x=0, y=0)

class BarGraph(ttk.Frame):

    def __init__(self, parent, controller):

        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="BarGraph")
        label.pack(pady=10, padx=10)

        ButtonHome = ttk.Button(self, text="Home",
                               command=lambda: controller.show_frame(FirstPage))
        ButtonHome.pack()

class PieChart(ttk.Frame):

    def __init__(self, parent, controller):

        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="PieChart")
        label.pack(pady=10, padx=10)

        ButtonHome = ttk.Button(self, text="Home",
                               command=lambda: controller.show_frame(FirstPage))
        ButtonHome.pack()

class Histogram(ttk.Frame):

    def __init__(self, parent, controller):

        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Histogram")
        label.pack(pady=10, padx=10)

        ButtonHome = ttk.Button(self, text="Home",
                               command=lambda: controller.show_frame(FirstPage))
        ButtonHome.pack()

class RadarChart(ttk.Frame):

    def __init__(self, parent, controller):

        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Radar Chart")
        label.pack(pady=10, padx=10)

        ButtonHome = ttk.Button(self, text="Home",
                               command=lambda: controller.show_frame(FirstPage))
        ButtonHome.pack()


app = TinyAnalytics()
app.mainloop()