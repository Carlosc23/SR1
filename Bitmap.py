import struct
from math import ceil

import math


def char(c):
    return struct.pack("=c", c.encode('ascii'))


def word(w):
    return struct.pack("=h", w)


def dword(d):
    return struct.pack("=l", d)


def color(r, g, b):
    return bytes([b, g, r])


class Bitmap(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []
        self.clear()

    def clear(self):
        self.pixels = [
            [color(255, 0, 0) for x in range(self.width)]
            for y in range(self.height)
        ]

    def glViewPort(self,x, y, width, height):
        if height <= 0 or width <= 0:
            print('Height and width must be positives')
            input()
        elif x < 0 or y < 0 or x > self.width or y > self.height:
            print('x and y must be positives and smaller tha height and width')
        else:
            self.vpWidth = width
            self.vpHeight = height
            self.vpX = x
            self.vpY = y

    def glClear(self):
        self.pixels= [
            [
                # show background color
                color(self.r, self.g, self.b) for x in range(self.width)
            ]
            for y in range(self.height)
        ]

    def glClearColor(self,r, g, b):
        self.r =  ceil(r * 255)
        self.g = ceil(g * 255)
        self.b = ceil(b * 255)

    def glVertex(self, x, y):
        pointSize = 10
        if self.vpHeight != 0 or self.vpWidth != 0:
            xx = x * ((self.vpWidth - pointSize) / 2)
            yy = y * ((self.vpHeight - pointSize) / 2)
            localX = self.vpX + int((self.vpWidth - pointSize) / 2) + int(xx)
            localY = self.vpY + int((self.vpHeight - pointSize) / 2) + int(yy)
            print(x, y, localX, localY)
            for x in range(pointSize):
                for y in range(pointSize):
                    self.point(localX + x, localY + y)
        else:
            print('Debe de ejecutar glViewPort para obtener un área a gráficar')

    def glColor(self, r, g, b):
        self.vr = r
        self.vg = g
        self.vb = b

    def write(self, filename):
        f = open(filename, 'bw')

        # file header (14)
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # image header (40)
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.pixels[x][y])
        f.close()

    def point(self, x, y, color=color(255, 255, 255)):
        self.pixels[y][x] = color


#r = Bitmap(600, 400)
#r.write('out.bmp')
#r.point(100, 200, color(255, 255, 0))
