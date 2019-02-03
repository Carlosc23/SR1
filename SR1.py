import struct
from random import randint

from math import ceil
from Bitmap import *


class software_render(object):
    def __init__(self, filename):
        self.window = ""
        self.filename = filename
        self.glInit()

    def glInit(self):
        pass

    def glCreateWindow(self, width, height):
        self.window = Bitmap(width, height)

    def glViewPort(self, x, y, width, height):
        self.window.glViewPort(x, y, width, height)

    def glClear(self):
        self.window.clear()

    def glClearColor(self, r, g, b):
        self.window.glClearColor(r, g, b)

    def glVertex(self, x, y):
        self.window.glVertex(x, y)

    def glColor(self, r, g, b):
        self.window.glColor(r, g, b)

    def glFinish(self):
        self.window.write(self.filename)


x = software_render('outazo.bmp')
x.glCreateWindow(400,400)
x.glClearColor(0, 0, 0)
x.glClear()
x.glViewPort(0, 0, 300, 300)
x.glColor(255, 255, 255)
x.glVertex(randint(-1, 1), randint(-1, 1))
x.glFinish()
