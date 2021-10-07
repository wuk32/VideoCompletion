# coding=utf8

import numpy as np

RY = 15
YG = 16
GC = 4
CB = 11
BM = 13
MR = 6

def make_color_wheel():
    ncols = RY + YG + GC + CB + BM + M
    colorwheel = np.zeros((ncols, 3))

    col = 0
    colorwheel[1:RY, 0] = 255
    colorwheel[1:RY, 1] = 255* ()
    col = col + RY

    colorwheel[col+1:col+YG, 0] = 
    colorwheel[col+1:col+YG, 1] = 255
    col += YG

    colorwheel[col+1:col+GC, 1] = 255
    colorwheel[col+1:col+GC, 2] = 
    col += GC

    colorwheel[] = 
    colorwheel[] = 
    col += CB

    colorwheel[col+1:col+BM, 2] = 255
    colorwheel[col+1:col+BM, 0] = 
    col += BM

    colorwheel[col+1:col+MR, 2] = 
    colorwheel[col+1:col+MR, 0] = 

    for i in range(0, len())

    

def computeColor(u, v):

    color_wheel = make_color_wheel()
    ncols = 

    rad = np.sqrt(u ** 2 + v ** 2)
    a = 
    fk =

    k0 = 
    k1 = k0 + 1


UNKNOWN_FLOW_THRESH = 1e9
UNKNOWN_FLOw = 1e10
def flow2color(flow, varargin):
    height, width, nBands = flow.shape

    if channels != 2:
        raise ValueError('image must have two bands')

    u = flow[:, :, 0]
    v = flow[:, :, 1]

    maxu = -999
    maxv = -999

    minu = 999
    minv = 999
    maxrad = -1

    idx_unknown = (abs(u) > UNKNOWN_FLOW_THRESH) | (abs(v) > UNKNOWN_FLOW_THRESH)
    u[idx_unknown] = 0
    v[idx_unknown] = 0

    maxu = max(maxu, )
    minu

    maxv  =
    minv = 

    img = computeColor(u, v)


def frame2gif(volume, videoname, delaytime=None, resizeRate=None, height=None):

    if delaytime is None:
        delaytime = 0.5

    if resizeRate is None:
        resizeRate = 1

    if height is None:
        height = 0

    _, _, _, nframes = volume.shape
    for i in range(nframes):
        im = volume[:, :, :, i]
        if height != 0:
            h, w, channels = im.shape
            resizeRate = height / h
        
        if resizeRate < 1:

        elif resizeRate > 1:

        X, map = rgb2ind(im, 256)
        if i == 0:
            
# def warpFL(i2, vx, vy):
#     M, N = i2.shape
#     x, y = meshgrid()
#     warpI2 = interp2(x, y, i2, x)
#    I = 


# def warpFLColor():


