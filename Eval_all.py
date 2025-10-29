#############################################################################
# code for paper: Sora Generateds Video with Stunning Geometical Consistency
# arxiv: https://arxiv.org/abs/
# Author: <NAME> xuanyili
# email: xuanyili.edu@gmail.com
# github: https://github.com/meteorshowers/SoraGeoEvaluate
#############################################################################
import argparse
from AutoExtraFrame import AutoExtraFrame
from PatchAutoEvaluate import PatchAutoEvaluate
from PatchDenseMatch import PatchDenseMatch
from PatchDrawMatch import PatchDrawMatch


def main():
    parser = argparse.ArgumentParser(description='Evaluate geometric consistency of generated videos')
    parser.add_argument('--output_video', type=str, required=True, 
                        help='Name of the output video folder (e.g., "yucheng")')
    parser.add_argument('--gt_video', type=str, default=None,
                        help='Name of the ground truth video folder (e.g., "gt"). Optional.')
    
    args = parser.parse_args()
    
    # Build video list
    video_list = [args.output_video]
    if args.gt_video:
        video_list.append(args.gt_video)
    
    print(f"Processing videos: {video_list}")
    
    # Run evaluation pipeline
    AutoExtraFrame(video_list)
    PatchAutoEvaluate(video_list)
    PatchDenseMatch(video_list)
    PatchDrawMatch(video_list)


if __name__ == "__main__":
    main()




