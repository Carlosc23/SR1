# Carlos Calderon, 15219
# SR1. py
# Module with a class Software Render that use bitmap to abstract a software render and use it to make a file with a
# point with a screen
from Bitmap import *


class SoftwareRender(object):
    """
    Class that use bitmap to abstract a software render
    """

    def __init__(self, filename):
        self.glInit()
        self.filename = filename

    def glInit(self):
        """
        Function that start necessary variables for software renderer
        :return:
        """
        self.window = ""

    def glCreateWindow(self, width, height):
        """
        Function that instantiate a new Object from Bitmap, this initialize the framebuffer
        :param width: width of the image that will be render
        :param height: height of the the image that will be render
        :return:
        """
        self.window = Bitmap(width, height)

    def glViewPort(self, x, y, width, height):
        """
        Function that call glViewPort of Bitmap and create a viewport
        where the image will be visible
        :param x: number that represent the horizontal coord where the viewport will be drawn
        :param y: number that represent the vertical coord where the viewport will be drawn
        :param width: width of the viewport
        :param height: heigth of the viewport
        :return:
        """
        self.window.glViewPort(x, y, width, height)

    def glClear(self):
        """
        Function that use glclear() function from Bitmap
        :return:
        """
        self.window.glclear()

    def glClearColor(self, r, g, b):
        """
        Function that use glClearColor from Bitmap
        :param r: amount of red
        :param g: amount of green
        :param b: amount of blue
        :return:
        """
        self.window.glClearColor(r, g, b)

    def glVertex(self, x, y):
        """
         Function that use glVertex from Bitmap
        :param x: relative horizontal coord of the point
        :param y: relative vertical coord of the point
        :return:
        """
        self.window.glVertex(x, y)

    def glColor(self, r, g, b):
        """
        Function that use glColor from Bitmap
        :param r: amount of red
        :param g: amount of green
        :param b: amount of b
        :return:
        """
        self.window.glColor(r, g, b)

    def glFinish(self):
        """
        Function that use write method from Bitmap, it save the specifications of the image in a file with filename
        specified by the user
        :return:
        """
        self.window.write(self.filename)

# Instructions to generate the point
x = SoftwareRender('outazo.bmp')
x.glCreateWindow(900, 400)
x.glViewPort(0, 0, 300, 300)
x.glClear()
x.glColor(0, 1, 0.01)
x.glVertex(1, 1)
x.glFinish()
