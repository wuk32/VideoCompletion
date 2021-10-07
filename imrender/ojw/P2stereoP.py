# coding=utf8

def P2stereoP(P, Zmin, view):
    """
        P2STEREOP Generates horizontally shifted viewpoints
        
        Generates horizontally shifted viewpoints, suitable for viewing in stereo

        Args:
            Pi: 3 * 4 * N input projection matrices
            Zmin: scalar, minimum depth in the scene
            View: scalar value of horizontal offset, where -1 is optimal left view and 1 is optimal
            right view, relative to the input matrix.
            Default: -1
    """
    if 