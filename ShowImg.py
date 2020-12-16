import json
import pylab as pl
import random
import numpy as np
from cv2 import cv2 as cv
import anno_func
from PyQt5.QtGui import QImage, QPixmap
from PIL import Image
import sys

class ShowImg():

    def __init__(self):
        self.datadir = sys.path[0] + "/tt100k/data"
        self.filedir = self.datadir + "/annotations.json"
        self.ids = open(self.datadir + "/test/ids.txt").read().splitlines()
        self.annos = json.loads(open(self.filedir).read())

    def loadInput(self):
        self.imgid = random.sample(self.ids, 1)[0]
        self.indata = anno_func.load_img(self.annos, self.datadir, self.imgid)
        return self.imgid

    def list2str(self, lst):
        string = ''
        for box in lst:
            string += '(\n(' + str(box[0][0]) + ', ' + str(box[0][1]) + '), \n'
            string += '(' + str(box[1][0]) + ', ' + str(box[1][1]) + '), \n' + str(box[2]) + '\n), \n'
        return string

    def getOutput(self):
        outbox = anno_func.draw_all(self.annos, self.datadir, self.imgid, self.indata)
        self.outdata = outbox[0]
        print(outbox[1])
        return self.list2str(outbox[1])

    def ndarr2qpix(self, data):
        img = data*255
        img = img.astype("uint8")
        img = cv.cvtColor(img, cv.COLOR_RGB2RGBA)
        im = Image.fromarray(img)
        return im.toqpixmap().scaled(350, 350)

    def ShowInput(self):
        return self.ndarr2qpix(self.indata)

    def ShowOutput(self):
        return self.ndarr2qpix(self.outdata)