# coding=utf8

def vis_flow_consistency(video_name):

    opt = vc_init_opt(video_name)

    flowDataFileName = 
    videoFlow = vc_compute_flow 

    videoFlowF = videoFlow[]
    videoFlowB = videoFlow[]

    imgH, imgW, _, nFrame = size()

    errFwBw = 
    errBwFw = 

    flowFwInc = 1
    flowBwInc = -1

    # Compute flow errors   
    for i in range(1, nFrame-1):
        pCur = 

        # Compute forward-backward errors
        flowF = vc_interp3()

        pFw = pCur
        pFw =
        pFw  = 
