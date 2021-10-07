# coding=utf8

def vc_check_spatial_coherence(src_pos_map, src_tfrmg_map, trg_ind, trg_indn, src_pos, opt):
    """
        check target pixels that are not spatially coherent
        
    """
    # active pixel for random  search
    uvActiveInd = 

    # the geometric transform of the source patch
    src_tfrmg = vc_uvMat_from_uvMap(src_tfrmg_map, trg_ind)

    for i in range():

        v = 

        # source patch of the neighbors
        src_pos_n = vc_uvMat_from_uvMap(src_pos_map, )

        # predicted source patch position
        src_pos_p = vc_get_spatial_propagation(src_pos, src_tfrmg, v)

        # check if the prediction is correct
        dis



    return nvActiveInd