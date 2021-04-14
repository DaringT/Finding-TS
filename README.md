# Finding Timestamps

## About
Finding_TS is a proof of concept and is far from perfect. It uses OpenCV (cv2) to get the average light in a frame. It is slow and It times triggers in low light scenes. Even with its flaws, it's nice to not watch every episode just for Chapter Timestamps.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [opencv-python](https://pypi.org/project/opencv-python/). 

```
pip install opencv-python
```

## Usage

```python 
from flagging_TS import get_dark_frames
# If you want to turn it into a chapter file;
# I have a list() to chapter file (make_txt & make_xml) functions in 
# ChapterCleaner script.

chapter_ts_list = get_dark_frames(input_video_file)

print(chapter_ts_list)
```

## Contributing
I am open to improvements. For changes please open an issue to discuss what you would like to change.
