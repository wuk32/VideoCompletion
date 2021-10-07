# coding=utf8

def P_interp(first, last, frames):
    """
        Linear interpolation between 2 projection matrices

        Creates a series off projection matrices interpolated from two projection matrices

        Args:
            first: 3 * 4 The first projection matrix in the series, and the first
                   projection matrix between which the output matrices are interpolated from
            last: 3 * 4 The second projection matrix between which the output matrices are interpolated from
            frames: N * 1 The frames to interpolate along a line, where 0 is the position of first and 1 the position of last
    """

    