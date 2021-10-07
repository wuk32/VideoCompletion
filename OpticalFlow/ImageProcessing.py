# coding=utf8

import numpy


def EnforceRange(x, max_value):
    return min(max(x, 0), MaxValue-1)


def BilinearInterpolate(image, width, height, channels, x, y):
    xx, yy = x, y
    dx = max(min(x-xx, 1), 0)
    dy = max(min(y-yy, 1), 0)

    for m in range(0, 2):
        for n in range(0, 2):
            u = EnforceRange(xx + m, width)
            v = EnforceRange(yy + n, height)
            offset = (v * width + u) * channels

            s = fabs(1-m-dx) * fabs(1-n-dy)
            for l in range(channels):
                result[l] += image[offset+l] * s
    
    return result


def BilinearInterpolate_transpose(inputs, width, height, channels, x, y, image):
    xx, yy = x, y
    dx = max(min(x-xx, 1), 0)
    dy = max(min(y-yy, 1), 0)

    for m in range(0, 2):
        for n in range(0, 2):
            u = EnforceRange(xx + m, width)
            v = EnforceRange(yy + n, height)
            offset = (v * width + u) * channels

            s = fabs(1-m-dx) * fabs(1-n-dy)
            for l in range(channels):
                image[l] += inputs[offset+l] * s


# def resize_image(src_image, dst_image, src_width, src_height, channels, dst_width, dst_height):
#     x_ratio = dst_width / src_width
#     y_ratio = dst_height / src_height

#     image = 
#     for 

def hfiltering(src_image, dst_image, width, height, channels, filter1D, fsize):
    """ horizontal direction filtering """
    buffer = np.zeros()
    for i in range(height):
        for j in range(width):
            offset = i * width * channels
            for l -= 
                w = filter1D[l+fsize]
                jj = EnforceRange(j+l, width)
                for k in range(channels):
                    buffer[k] = src_image[offset + jj*channels+ + k] * w


def hfiltering_transpose(src_image, dst_image, width, height, channels, filter1D, fsize):
    """ horizontal direction filtering transpose """


def Laplacian(src_image, dst_image, width, height, channels):


def vfiltering(src_image, dst_image, width, height, channels, filter1D, fsize):
    """ vertical direction filtering """


def vfiltering_transpose(src_image, dst_image, width, height, channels, filter1D, fsize):


def filtering(src_image, dst_image, width, height, channels, filter2D, fsize):
    " 2D filtering "


def filtering_transpose():



def getPatch(src_image, patch, width, height, channels, x0, y0, wsize):
    """ function to sample a patch from the source image """


def warpImage():
    """ """

def warpImageFlow():
    """ """

def warpImage_transpose():


def cropImage():
    """ function to crop an image from the source
        assume that dst_image has been allocated
        also Left and Top must be valid, dst_width and dst_height should ensure that the image lies
        inside the image boundry    
    """

def generate2DGuassian(image, wsize, sigma):
    """ function to generate a 2D Gaussian image
        image must be allocated before calling the function
    """


def generate1DGaussian(image, wsize, sigma):



