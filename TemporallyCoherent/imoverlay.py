# coding=utf8

def imoverlay(inputs, mask, color=(1, 1, 1)):
    """
        create a mask-based image overlay, whose pixels in the mask location have the specified color

        Args:
            inputs: a grayscale or an RGB image of class uint8, uint16, int16, logical, double, or single
                double or single should be in the range [0, 1]. 
            mask: a two-dimensional logical matrix
            color should be a 1-by-3 vector of values in the range [0, 1]. [0 0 0] is black and [1 1 1] is white
    """

    # force the mask to be logical
    mask = 

    # make the uint8 the working data class. The output is also uint8
    in_uint8 = im2uint8(inputs)
    color_uint8 = im2uint8(color)

    if in_unit8.ndims == 2:
        out_red = in_uint8
        out_green = in_uint8
        out_blue = in_uint8
    else:
        out_red = in_uint8[:, :, 0]
        out_green = in_uint8[:, :, 1]
        out_blue = in_uint8[:, :, 2]
    
    out_red()