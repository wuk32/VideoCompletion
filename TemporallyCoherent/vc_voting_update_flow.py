# coding=utf8

def vc_voting_update_flow(videoFlow, NNF, holeMask, opt):
    """
        Fast voting update, instead of computing the weighted average from all
        source patches, here we only update patches that have been updated
    """
    imgH, imgW, nCh, nFrame, nFlow = size()

    numUvPix 

    if numUvPix != 0:
        # Prepare source patches
        uvTcur = 
        srcPatch = 

        # Apply the motion field transformation
        uv


        # Prepare spatila-temporal patch weight


        # Prepare cost-based patch weight


        # Combine two weights


        # Apply the weight for the source patch 


        # Get the target patch indices
