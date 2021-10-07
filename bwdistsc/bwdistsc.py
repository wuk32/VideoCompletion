# coding=utf8

def bwdistsc(bw, aspect):
    """
        BWDISTSC computes Euclidean distance transform of a binary 3D image BW.
        Distance transform assigns to each pixel in BW a number that is the distance
        from that pixel to the nearest nonzero pixel in BW. BWDISTSC can accept a 
        regular 2D imaage, a 3D array, and a cell array of 2D slices
        ASPECT is a 3-component vector defining the voxel-aspect-ratio for BW
        If ASPECT is not given, [1 1 1] isotropic aspect ratio is assumed

        BWDISTSC uses fast optimized scan algorithm and cell-arrays to 
        represent internal data, and is less demanding to physical memory as
        well as in many cases up to 10 times faster than MATLAB's native bwdist

        Scan algorithms below use following Lema:
            
    """