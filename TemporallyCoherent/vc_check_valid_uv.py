# coding=utf8

def vc_check_valid_uv(uv_sub, valid_mask):
    """
        check if uv_sub are out of bounds
    """

    interpolationKernel = 'linear'

    uvValidInd = vc_interp3(valid_mask, uv_sub, interpolationKernel)
    uvValidInd = uvValidInd > 0.99

    return uvValidInd