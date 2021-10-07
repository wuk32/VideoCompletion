# coding=utf8

def addInnerStroke(img, t, c):

    h, w, c = img.shape

    img2 = img1 = 


def addOuterStroke(img, t, c):
    h, w, c = img.shape


def addCenterStroke(img, t, c):

    img2 = addInnerStroke(img1, float(t/2), c)
    img2 = addOuterStroke(img2, )
    return img2


def addborder(img, t, c, stroke):
    """
        Draws a border around an image

        Args:
            img:
            t: thickness in pixels
            c: color
            stroke: indicates the positions of the border
                'inner' - border is added to the inside of the image. OUT will be the same as IMG
                'outer' - border sits completely outside of the image, and does not obscure any portion of it
                'center' - the border stradddles the edges of the image
    """

    if 

    if 

    c = 

    s = lower(stroke[0])
    if s == 'i':
        img = addInnerStroke(img, t, c)
    elif s == 'o':
        img = addOuterStroke(img, t, c)
    elif s == 'c':
        img = addCenterStroke(img, t, c)
    else:
        raise NotImplementedError

