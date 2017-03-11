from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import time
import matplotlib.animation as animation
from matplotlib import style

#Figure creation and assignment
fig = plt.figure()
ax = fig.add_subplot(111,  projection='3d', axisbg = 'grey')

#sets background color
rect = fig.patch
rect.set_facecolor('grey')

#delta how often we're going to compute the line
x, y, z = axes3d.get_test_data(0.05)

def onclick(event):
    print('x=%d, y=%d, xdata=%f, ydata=%f'%(
        event.x, event.y, event.xdata, event.ydata))

'''def animation(animate):
    dataPull = open('Data.txt', 'r').read()
    dataArray = dataPull.split('\n')
    xArray = []
    yArray = []
    zArray = []
    for line in dataArray:
        if len(line) > 1:
            x,y,z = line.split(',')
            xArray.append(int(x))
            yArray.append(int(y))
            zArray.append(int(z))
    ax.clear()
    ax.plot(x,y,z)
animator = animation.FuncAnimation(fig,animation, interval = 10000)

x = []
y = []
z = []

readFile = open('Data.txt', 'r')

sepFile = readFile.read().split('\n')

readFile.close()

for plotPoints in sepFile:
    xAndyAndz = plotPoints.split(',')
    x.append(int(xAndyAndz[0]))
    y.append(int(xAndyAndz[1]))
    z.append(int(xAndyAndz[2]))

print(x)
print(y)
print(z)'''

#rstride is how often we draw a line
ax.plot_surface(x, y, z, cmap=cm.coolwarm, rstride=2, cstride=2, alpha=0.3)
cset = ax.contour(x, y, z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contour(z, y, z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contour(z, y, z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.spines['bottom'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['top'].set_color('white')

ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-100, 100)

plt.title('Testing', color = 'white')
plt.xlabel('X Label', color = 'white')
plt.ylabel('Y Label', color = 'white')

style.use("ggplot")

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()


'''Title = StringVar()
        xLabel = StringVar()
        yLabel = StringVar()
        zLabel = StringVar()

        titleLabel = Label(text="Title")
        xAxisLabel = Label(text="x axis")
        yAxisLabel = Label(text="y axis")
        zAxisLabel = Label(text="z axis")

        titleLabel.pack()
        xAxisLabel.pack()
        yAxisLabel.pack()
        zAxisLabel.pack()

        TitleEntry = Entry()
        xAxisEntry = Entry()
        yAxisEntry = Entry()
        zAxisEntry = Entry()

        TitleEntry.pack()
        xAxisEntry.pack()
        yAxisEntry.pack()
        zAxisEntry.pack()


#STATUS BAR STUFF
pb_hd = ttk.Progressbar(self, orient='horizontal', mode='determinate')
        #pb_hD = ttk.Progressbar(self, orient='horizontal', mode='indeterminate')
        #pb_vd = ttk.Progressbar(self, orient='vertical', mode='determinate')
        #pb_vD = ttk.Progressbar(self, orient='vertical', mode='indeterminate')

        pb_hd.pack(expand=True, fill=BOTH, side=tkinter.TOP)
        #pb_hD.pack(expand=True, fill=BOTH, side=tkinter.TOP)
        #pb_vd.pack(expand=True, fill=BOTH, side=tkinter.LEFT)
        #pb_vD.pack(expand=True, fill=BOTH, side=tkinter.LEFT)

        pb_hd.start(20)
        #pb_hD.start(70)

        #status= Label(self, text="Loading...", border=1, relief=SUNKEN, anchor=W)
        #status.pack(side=BOTTOM, fill=X)


        style = ttk.Style()
        style.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
        self.progress = ttk.Progressbar(self)
        self.progress.configure(style="red.Horizontal.TProgressbar")
        self.progress.pack(expand=True, fill=BOTH, side=tkinter.TOP)
        self.progress.start(10000)
        '''