# coding=utf8

def vc_compute_affine_2d_p(P, Q):
    numPix = P.shape[2]

    # compute inv(P'P)
    PtP_11 = 
    PtP_22 = 
    PtP_12 = 

    PtP_det = 
    PtPinv = 
    PtPinv = 

    # Compute P'Q
    PtQ_11 = 
    PtQ_21 = 
    PtQ_12 = 
    PtQ_22 = 

    PtQ = 
    PtPinv = 
    PtQ = 

    # Compute tform

    return 


def vc_compute_affine_2d_s(P, Q):
    K = P.shape[0]
    N = P.shape[2]

    tform = 

    



def vc_compute_affine_2d(P, Q):
    """
        Compute affine transformation from 2D point sets
        Args:
            P: K * 2 * N
            Q: K * 2 * M
        Output:
            tform: N * 4
    """
    # tform1 = vc_compute_affine_2d_s(P, Q)

    # Faster implementation 
    t_form = vc_compute_affine_2d_p()

    return t_form

