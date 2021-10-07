# coding=utf8
import cv2

from Optical.Coarse2FineTwoFrames import Coarse2FineTwoFrames
from Optical.utils import 

def test():
    im1 = cv2.imread('data/1.jpg')
    im2 = cv2.imread('data/2.jpg')

    alpha = 0.012
    ratio = 0.75
    minWidth = 20
    OuterFPIteration = 7
    InnerFPIteration = 1
    SORIterations = 30

    vx, vy, warpI2 = Coarse2FineTwoFrames(im1, im2, )



if __name__ == "__main__":
    test()