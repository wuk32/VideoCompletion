# coding=utf8

def vc_export_video_vis(video_data, hole_mask, video_res_path, video_name, video_type):
    """
        Export the current flow or color video

        Args:
            video: the video data of the size [H, W, C, nFrame](color), [H, W, C, nFrames, 2] (Flow)
            hole_mask: mask of unknown regions [H, W, nFrame]
            video_res_path: result directory
            video_name: result name
    """
    
    if video_type == "CIELab":
        video_RGB = vc_video_lab2rgb(video_data)
    elif video_type == "Flow":
        video_RGB = vc_video_flow2color(video_data)
    elif video_type == "JetColor":
        video_RGB = vc_video_scalar2jet(video_data)
    elif video_type == "RGB":
        video_RGB = video_data
    else:
        raise NotImplementedError

    video_RGB = vc_clamp(video_RGB, 0, 1)
    # Write the RGB video to file
    vc_export_video(video_RGB, hole_mask, video_res_path, video_name)

def vc_export_video(video_data, hole_mask, video_res_path, video_name):
    """
        Export the current color video

        Args:
            video_data: the video data of size [H, W, C, nFrames]
            hole_mask: the hole of size [H, W, nFrames]
            video_res_path: result directory
            video_name: result name
    """

    # Start exporting frames
    nFrames = video_data.shape[3]
    for i in range(nFrames):
        strImg 


def change_video_frame_rate(video_data, frame_rate):
    