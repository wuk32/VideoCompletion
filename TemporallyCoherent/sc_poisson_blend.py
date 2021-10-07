# coding=utf8

def solve_poisson(hole_mask, img_src, img_trg):
    """ Prepare the linear system of equations for Poission blending """
    h, w = hole_mask.shape
    N = h * w

    # number of unknown variables
    numUnknownPix = 

    maxNumInd = 



def sc_poisson_blend(img_trg, img_src, hole_mask):
    """
        blend the source and target image using a simple discrete poisson solver

        Args:
            img_trg: original image with hole
            img_src: synthesized image
            hole_mask: specify the hole pixels
        Outputs:
            img_blend: blended image
    """

    h, w, c = img_src.shape

    # initialize the reconstructed image
    img_recon = 

    # independently process each channel
    for i in range(c):
        img_s = img_src[:, :, i]
        img_t = img_trg[:, :, i]

        # prepare discrete Poission equation
        A,b = 
        
        # solve Poisson equation
        x = A/b

        img_recon[:, :, i] = 

    # combined with the known region in the target
    hole_mask_c = 
    img_blend =

    return img_blend



