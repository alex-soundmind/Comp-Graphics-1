from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def cda(x1, y1, x2, y2):
    """Алгоритм ЦДА"""
    img = Image.new('RGB', (800, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    for i in range(steps + 1):
        x = x1 + dx * i // steps
        y = y1 + dy * i // steps
        draw.point((x, y), fill=(255, 0, 0))
        
    return np.array(img)

def brezenhem(x1, y1, x2, y2):
    """Алгоритм Брезенхема"""
    img = Image.new('RGB', (800, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    dx = x2 - x1
    dy = y2 - y1
    t = 0
    while t <= 1:
        x = x1 + t * dx
        y = y1 + t * dy
        draw.point((int(x), int(y)), fill=(0, 255, 0))
        t += 0.01

    return np.array(img)

def brezenhem_int(x1, y1, x2, y2):
    """Целочисленный алгоритм Брезенхема"""
    img = Image.new('RGB', (800, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    while True:
        if x1 == x2 and y1 == y2:
            break
        draw.point((x1, y1), fill=(0, 0, 255))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return np.array(img)

class AlgorithmPlot:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Алгоритмы")
        self.ax.set_axis_off()
        self.buttons = [
            plt.Button(plt.axes([0.1, 0.05, 0.2, 0.075]), 'ЦДА'),
            plt.Button(plt.axes([0.4, 0.05, 0.2, 0.075]), 'Брезенхем'),
            plt.Button(plt.axes([0.7, 0.05, 0.2, 0.075]), 'Целочисл. Брезенхем')
        ]
        self.buttons[0].on_clicked(self.plot_cda)
        self.buttons[1].on_clicked(self.plot_brezenhem)
        self.buttons[2].on_clicked(self.plot_brezenhem_int)

    def plot_cda(self, event):
        self.ax.clear()
        plt.show(block=False)
        self.ax.imshow(cda(self.x1, self.y1, self.x2, self.y2))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.ax.set_title("Алгоритм ЦДА")

    def plot_brezenhem(self, event):
        self.ax.clear()
        plt.show(block=False)
        self.ax.imshow(brezenhem(self.x1, self.y1, self.x2, self.y2))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.ax.set_title("Алгоритм Брезенхема")

    def plot_brezenhem_int(self, event):
        self.ax.clear()
        plt.show(block=False)
        self.ax.imshow(brezenhem_int(self.x1, self.y1, self.x2, self.y2))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.ax.set_title("Целочисленный алгоритм Брезенхема")

def main():
    x1, y1 = map(int, input("Введите координаты начала отрезка (x y): ").split())
    x2, y2 = map(int, input("Введите координаты конца отрезка (x y): ").split())
    plot = AlgorithmPlot(x1, y1, x2, y2)
    plt.show()

if __name__ == "__main__":
    main()