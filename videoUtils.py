import os
import pdb
import math
import subprocess
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips

class Video:
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path
        self.file = VideoFileClip(path)
    
    def width(self):
        return float(self.file.w)
    
    def height(self):
        return float(self.file.h)
    
    def duration(self):
        return self.file.duration
    
    def resize(self, newsize=None, height=None, width=None, apply_to_mask=True):
        self.file = self.file.resize(newsize=newsize, height=height, width=width, apply_to_mask=apply_to_mask)

def download_videos(subs, dirname="downloads"):
    script_path = os.path.join("bulk-downloader-for-reddit", "script.py")
    for sub in subs:
        cmd  = "python " + script_path
        cmd += " --directory " + dirname
        cmd += " --subreddit " + sub["name"]
        cmd += " --sort " + sub["sort"]
        cmd += " --time " + sub["time"] 
        cmd += " --limit " + str(sub["limit"])
        cmd += " --skip images gifs self"
        cmd += " --quit"
        # cmd += " --no-dupes"        # TODO: optional
        subprocess.run(cmd)

def find_valid_mp4_videos(subs, dirname="downloads", additional_valid_streams=False):
    if additional_valid_streams:
        from pymediainfo import MediaInfo
    
    # Collect all *.mp4 files
    videos = []
    for sub in subs:
        for filename in os.listdir(os.path.join(dirname, sub["name"])):
            if filename.endswith(".mp4"):
                path = os.path.join(dirname, sub["name"], filename)
                try:
                    video = Video(filename, path)
                    videos.append(video)
                except:
                    print("Could not find the video at the path:" + path)
            elif additional_valid_streams and filename.endswith("video"):
                # reddit-bulk-downloader sometimes returns videos
                # with no extensions, whose name end with "video"
                path = os.path.join(dirname, sub["name"], filename)
                fileInfo = MediaInfo.parse(path)
                for track in fileInfo.tracks:
                    if track.track_type == "Video":
                        video = Video(filename, path)
                        videos.append(video)
    return videos

def split_into_compilations(total_time, videos, max_length, max_subsets=10):

    # Limit number of compilations
    if total_time[-1] > max_length * max_subsets:
        stop_ind = np.where(total_time == total_time[total_time <= max_length * max_subsets].max())[0] + 1 # include extra video for flooring later
        videos = videos[:int(stop_ind[0] + 1)]
        total_time = total_time[:int(stop_ind[0] + 1)]

    # Have at least one compilations
    n_compilations = max(1, math.floor(total_time[-1] / max_length))

    # Split videos evenly across compilations
    compilations = [[] for n in range(n_compilations)]
    for i in range(len(compilations)):
        compilations[i] = videos[i::n_compilations]

    return compilations
