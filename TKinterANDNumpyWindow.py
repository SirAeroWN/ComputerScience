import tkinter as tk
from matplotlib.pylab import *

class AWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.aVar = tk.StringVar()
        self.bVar = tk.StringVar()
        self.aEntry = tk.Entry(self.root, textvariable = self.aVar)
        self.bEntry = tk.Entry(self.root, textvariable = self.bVar)
        self.aEntry.grid(row = 1, column = 1)
        self.bEntry.grid(row = 1, column = 2)
        self.button1 = tk.Button(self.root, text = 'Graph It', command = self.graphit)
        self.button1.grid(row = 2, columnspan = 2)
        self.root.mainloop()
        return

    def f(self, x):
        return eval(self.aVar.get()) * ((x**2) / 2) + eval(self.bVar.get())

    def graphit(self):
        x = linspace(-10, 10, 101)
        y = self.f(x)
        plot(x, y)
        xlabel('x')
        ylabel('y')
        legendString = self.aVar.get() + 'x^2/2 + ' + self.bVar.get()
        legend([legendString])
        axis([-10,10,-10,10])
        title('My first plot')
        grid(True)
        axhline(0, color='black', lw=2)
        axvline(0, color='black', lw=2)
        show()

AWindow()