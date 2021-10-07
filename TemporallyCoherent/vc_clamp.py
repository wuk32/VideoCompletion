# coding=utf8

def vc_clamp(x, lb, ub):
    """
        clamp valus to [lb, ub]
        Args:
            x: input array
            lb: lower bound value
            ub: upper bound value
        Output:
            y : clamped results
    """

    y = min(x, ub)
    y = max(y, lb)

    return y