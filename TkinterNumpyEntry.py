import tkinter as tk
from matplotlib.pylab import *

class AWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.aFrame = tk.Frame(self.root)
        self.aVar = tk.StringVar()
        self.bVar = tk.StringVar()
        self.cVar = tk.StringVar()
        self.smallx = tk.StringVar()
        self.bigx = tk.StringVar()
        tk.Label(self.root, text = 'Coefficient a:').grid(row = 1, column = 1)
        tk.Label(self.root, text = 'Coefficient b:').grid(row = 2, column = 1)
        tk.Label(self.root, text = 'Coefficient c:').grid(row = 3, column = 1)
        tk.Label(self.root, text = 'Smallest x:').grid(row = 4, column = 1)
        tk.Label(self.root, text = 'Largest x:').grid(row = 5, column = 1)
        self.aEntry = tk.Entry(self.root, textvariable = self.aVar)
        self.bEntry = tk.Entry(self.root, textvariable = self.bVar)
        self.cEntry = tk.Entry(self.root, textvariable = self.cVar)
        self.sxEntry = tk.Entry(self.root, textvariable = self.smallx)
        self.bxEntry = tk.Entry(self.root, textvariable = self.bigx)
        self.aEntry.grid(row = 1, column = 2)
        self.bEntry.grid(row = 2, column = 2)
        self.cEntry.grid(row = 3, column = 2)
        self.sxEntry.grid(row = 4, column = 2)
        self.bxEntry.grid(row = 5, column = 2)
        self.button1 = tk.Button(self.aFrame, text = 'Graph It', command = self.graphit)
        self.button1.grid(row = 1, column = 1)
        self.button2 = tk.Button(self.aFrame, text = 'Close Graph Window', command = self.killIt)
        self.button2.grid(row = 1, column = 2)
        self.aFrame.grid(row = 6, column = 1, columnspan = 2)
        self.root.mainloop()
        return

    def killIt(self):
        close()
        return

    def f(self, x, a, b, c):
        return a*x**2 + b*x + c

    def df(self, x):
        y1 = self.f(x, eval(self.aVar.get()), eval(self.bVar.get()), eval(self.cVar.get()))
        dx = (eval(self.smallx.get()) - eval(self.bigx.get())) / 50
        dy = diff(y1)/dx
        return dy

    def graphit(self):
        x = linspace(eval(self.smallx.get()), eval(self.smallx.get()), 101)
        y = self.f(x, eval(self.aVar.get()), eval(self.bVar.get()), eval(self.cVar.get()))
        D = self.df(x)
        plot(x, y)
        plot(x[:-1], D)
        xlabel('x')
        ylabel('y')
        legendString = self.aVar.get() + 'x^2 + ' + self.bVar.get() + 'x + ' + self.cVar.get()
        legend([legendString])
        gmin = amin(y)
        gmax = amax(y)
        axis([eval(self.smallx.get()), eval(self.bigx.get()), gmin, gmax])
        title('My first plot')
        grid(True)
        axhline(0, color='black', lw=2)
        axvline(0, color='black', lw=2)
        show()

AWindow()