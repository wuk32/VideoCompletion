# coding=utf8

def getDxs(imdx, imdy, imdt, im1, im2):
    """ function to compute dx, dy, dy and dt for motion estimation """

    filter = [0.02, 0.11, 0.74, 0.11, 0.02]

    imfilter_hv(im1, f)


def SanityCheck(imdx, imdy, imdt, du, dv):
    """ function to do sanity check: imdx * du + imdy * dy + imdt = 0 """


def warpFL(warpIm2, Im1, Im2, vx, vy):
    """ function to warp image based on the flow field """

def genInImageMask(mask, vx, vy, interval):
    """ function to generate mask of the pixels that move inside the image boundary """


def SmoothFlowSOR(im1, im2, warpim2, u, v, alpha, outerFPIterations, innerFPIterations, SORIterations):
    """ function to compute optical flow field using two fixed point iterations
        Input aarguments:
            Im1, Im2: frame 1 and frame 2
            warpIm2: the warped frame 2 according to the current flow field u and v
            u, v:   the current flow field, NOTICE that they are also output arguments     

    """


def SmoothFlowPDE(im1, im2, warpim2, u, v, alpha, outerFPIterations, innerFPIterations, CGIterations):
    """ function to compute optical flow field using two fixed point iterations
        Input aarguments:
            Im1, Im2: frame 1 and frame 2
            warpIm2: the warped frame 2 according to the current flow field u and v
            u, v:   the current flow field, NOTICE that they are also output arguments     

    """

def estGaussianMixture(im1, im2, para, prior):


def estLaplacianNoise(im1, im2, para):


def Laplacian(output, input, weight):