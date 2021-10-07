# coding=utf8


def update_color(z, r1, r2, alpha):
    """
        Args:
            z: spatial voting
            r1: forward temporal neighbor
            r2: backward temporal neighbor
            I: update color
                argmin || I - X ||_2^2 + alpha * \phi(||I - R1||_2^2) + alpha*\phi(||I - R2||_2^2)
    """

    numIter = 5
    eps = 1e-3

    v1 = 
    v2 = 

    I_k = Z
    for k in range(numIter):
        dZ = Z - I_k
        dR1 = R1 - I_k
        dR2 = R2 - I_k

        # Compute the weights
        w1 = alpha * 0.5 / 
        w2 = alpha * 0.5 

        # Put invalid flow neighbor to zeros
        w1 = 
        w2 = 

        # Weighted average 
        dI = (dZ + dR1 * w1 + dR2 * w2) / (1 + w1 + w2)

        I_k = I_k + dI

    return I_k 