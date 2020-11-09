import os
import sys
import pdb
import time
import numpy as np
from operator import itemgetter
from moviepy.editor import VideoFileClip, concatenate_videoclips
from videoUtils import Video, download_videos, find_valid_mp4_videos, split_into_compilations

from settings import topics

download = True
export   = True

DOWNLOAD_DIR  = "downloads"
EXPORT_DIR   = "youtube"

if download and not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

for topic in topics:
    if download:
        print("\n\nInitializing downloads for topic " + topic["name"] + "...\n\n")
        download_videos(topic["subreddits"], dirname=DOWNLOAD_DIR)
    
    if export:
        print("\n\nInitializing YouTube postprocessing for topic " + topic["name"] + "...\n\n")
        videos = find_valid_mp4_videos(topic["subreddits"], dirname=DOWNLOAD_DIR)

        # Resize
        for video in videos:
            ratio = video.width() / video.height()
            video.resize(width=1920) if ratio > (16.0 / 9) else video.resize(height=1080)

        # Remove videos that are too long
        duration = [video.duration() for video in videos]
        duration, videos = map(list, zip(*[(d, v) for (d, v) in zip(duration, videos) if d <= topic["MAX_SUBCLIP_TIME"]]))

        # Sort videos by duration
        duration, videos = map(list, zip(*sorted(zip(duration, videos), key=itemgetter(0))))

        # Cumulative duration
        cum_time = np.cumsum(duration)

        compilations = split_into_compilations(cum_time, videos, max_length=topic["MAX_CLIP_TIME"], max_subsets=3)

        print("\n\nGenerating YouTube compilations for topic " + topic["name"] + "...\n\n")

        if not os.path.exists(EXPORT_DIR):
            os.makedirs(EXPORT_DIR)

        for n, compilation in enumerate(compilations):                        
            output_video = concatenate_videoclips([video.file for video in compilation], method="compose")
            video_name = topic["name"] + "_" + str(n + 1) + ".mp4"
            video_path = os.path.join(EXPORT_DIR, video_name)
            output_video.write_videofile(video_path, audio=True, threads=8)
        
        print("\n\nDone with YouTube topic " + topic["name"] + ".\n\n\n")