# coding=utf8

def vc_clamp_ch(x, lb, ub):
    c = x.shape[2]
    for i in range(c):
        x[:, i] = vc_clamp(x[:, i], lb[i], ub[i])
    
    return x