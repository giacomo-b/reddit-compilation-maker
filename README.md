# Reddit Compilation Maker

Reddit Compilation Maker is a Python tool created to make compilations out of user-specified subreddits content.

## Requirements

This program relies on [`bulk-downloader-for-reddit`](https://github.com/aliparlakci/bulk-downloader-for-reddit), which needs `ffmpeg` to work correctly.
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

### 