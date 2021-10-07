# coding=utf8

def compute_sim_tform_2d(trg_pix_f, src_pix_f):
    """
        Compute the 2D similarity transformation that maps src_flow to trg_flow
    """

    


def vc_compute_flow_tform(video_flow_fw_bw, trg_pos, src_pos):
    trg_flow = vc_interp3(video_flow_fw_bw, trg_pos)
    src_flow = vc_interp3(video_flow_fw_bw, src_pos)

    src_tfm_fw = compute_sim_tform_2d(trg_flow[:, 0:1], src_flow[:, 0:1])
    src_tfm_bw = compute_sim_tform_2d(trg_flow[:, 2:3], src_flow[:, 2:3])

    return src_tfm_fw, src_tfm_bw
