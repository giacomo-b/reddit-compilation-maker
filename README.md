# Reddit Compilation Maker

Reddit Compilation Maker is a Python tool created to automatically create compilations from subreddits content. Can be used to synthesize the trending videos into compilations, automate content generation for social media, and much more.

## Requirements

This program relies on [`bulk-downloader-for-reddit`](https://github.com/aliparlakci/bulk-downloader-for-reddit), which in turn needs `ffmpeg` to work correctly.

You also need `numpy` and `moviepy`.

### Installing `ffmpeg`
* On **Linux**: run `sudo apt install ffmpeg`
* On **Windows**:
    * Download the installer from [here](https://www.gyan.dev/ffmpeg/builds/) or [here](https://github.com/BtbN/FFmpeg-Builds/releases) and run it
    * Add `ffmpeg` to your `Path`:
        * Go to [Environment Variables](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/)
        * Select `Path` -> Edit -> New and add `C:\FFmpeg\bin` (or wherever you installed `ffmpeg` at the previous step)
* On **MacOS**:
    * Install [Homebrew](https://brew.sh/)
    * Run `brew install ffmpeg`

### Installing `numpy` and `moviepy`
Run `python -m pip install numpy moviepy`

## How to use

### Selecting the target subreddits for your compilations
Just edit `settings.py` to include all the subreddits you want. To make the script more flexible, `topics` allows to keep track of multiple topics. This means that the final output will mix videos from all the subreddits provided for each topic.

Each `topics` element is a dictionary with the following format:
```python
{
    "name": "MyTopic",
    "subreddits": [ {"name":  "first-sub", "sort": "top", "time":  "week", "limit": 10},
                    {"name": "second-sub", "sort": "hot", "time": "month", "limit": 20} ],
    "MAX_CLIP_TIME":    60.0,  # seconds
    "MAX_SUBCLIP_TIME": 20.0,  # seconds
}
```

In the example above, the script will generate a compilation "MyTopic" containing videos from "first-sub" and "second-sub" (add as many as you wish).

The videos will be selected by taking the first 10 and 20 posts of each subreddit, sorted by "top of the last week" in the first case and "hot in the last month" in the second case.

Videos longer than `MAX_SUBCLIP_TIME` will be discarded, and a single compilation won't be longer than `MAX_CLIP_TIME`. If the total duration of the videos is longer than `MAX_CLIP_TIME`, multiple compilations are generated.

Feel free to add as many compilation topics as you want by populating `topics` with more dictionaries in `settings.py`.

### Running the script
Run `python main.py` from the command line.

### Additional options

#### About `sort` and `time`
These options are taken from the original [`bulk-downloader-for-reddit`](https://github.com/aliparlakci/bulk-downloader-for-reddit) repo:

* `sort`: accepts `hot`, `top`, `new`, `rising`, `controversial` and `relevance`
* `time`: accepts `hour`, `day`, `week`, `month`, `year` and `all`

#### Videos order inside the compilation
Note that videos are currently being sorted by order inside each compilation video. This suited my use case, but you can change it in `main.py`.