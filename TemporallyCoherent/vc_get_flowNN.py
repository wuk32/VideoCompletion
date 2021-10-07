# coding=utf8

import numpy as np

def vc_get_flowNN(video_flow, hole_pix):
    # Assign each hole pixel is flow-based nearest neighbor with the shortest geodesic distance

    # flowNN numPix * 3 

    # Initialization
    flowNN = 

    H, W, C, nFrame = video_flow.shape

    # Initialization 
    initDist = nFrame