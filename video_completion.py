# coding=utf8
import sys
from TemporallyCoherent. import vc_init_opt


def video_completion(video_name):
    """
        Main function for video completion

        Args:
            video_name: the video filename
    """

    # Initalization algorithm parameters 
    opt = vc_init_opt(video_name)

    # load video, hole and flow data
    # Start and end frame
    frame_ind = FrameInd(start=1, end=5)

    # Load input video and holeMask
    video_color, hole_mask, load_flag = vc_load_input_data()

    

if __name__ == "__main__":
    video_name = sys.argv[1]

    video_completion(video_name)