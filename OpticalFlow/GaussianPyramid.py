# coding=utf8

import numpy as np


class GuassianPyramid(object):
    def __init__(self):
        self.pyramid = []

    def construct_pyramid(self, image, ratio, minWidth):
        if ratio > 0.98  or ratio < 0.4:
            ratio = 0.75

        height, width, _ = image.shape
        nlevels = int(np.log(minWidth/width) / np.log(ratio))
        self.pyramid.append(image)
        base_sigma = 1 / ratio - 1
        n = np.log(0.25) / np.log(ratio)
        nsigma = base_sigma * n
        for i in range(nlevels):
            if i <= n:
                sigma = base_sigma * i
                GuassianSmoothing(image, )
            else:
                GuassianPyramid

    def construct_pyramidlevels(self, image, ratio, nlevels):
        if ratio > 0.98  or ratio < 0.4:
            ratio = 0.75

        height, width, _ = image.shape
        nlevels = int(np.log(minWidth/width) / np.log(ratio))
        self.pyramid.append(image)
        base_sigma = 1 / ratio - 1
        n = np.log(0.25) / np.log(ratio)
        nsigma = base_sigma * n
        for i in range(nlevels):
            if i <= n:
                sigma = base_sigma * i
                GuassianSmoothing(image, )
            else:
                GuassianPyramid

