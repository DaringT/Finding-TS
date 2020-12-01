import cv2
import numpy as np
import time
import os
from TS import TS
from tqdm import tqdm


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def frames_to_secs(input_frame_num, fps):
    # Python Program to Convert seconds
    # into hours, minutes and seconds
    secs = input_frame_num / fps
    return convert(secs)


def get_file_data(f):
    import re
    f = os.path.basename(f)
    ep_seires, ep_se, ep_title = f.split(" - ")
    match = re.match(r"[S|s](\d\d?)[E|e](\d\d?)", ep_se)
    seasion_num, ep_num = match.groups()
    return ep_seires, seasion_num, ep_num


def remove_duplicates(input_list):
    print('Removing Duplicates from list')
    cleaned_list = list(set(input_list))
    return sorted(cleaned_list)


def get_dark_frames(input_loc):
    """Function to extract frames from input video file
    and save them as timestamps in an output directory.
    Args:
        input_loc: Input video file path.
    Returns:
        list: Found Timestamps
    """

    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", video_length)
    count = 0

    old_found_TS = ""
    # Start converting the video
    black = num_of_frames = 0
    found_TS_list = []

    with tqdm(total=video_length, dynamic_ncols=True, desc="Finding Timestamps... ") as prbar:
        while cap.isOpened():

            # Extract the frame
            ret, frame = cap.read()
            num_of_frames = num_of_frames + 1
            # print(num_of_frames)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if np.average(gray) < 7:
                # Write the results back to output location.
                black = black + 1
                found_TS = frames_to_secs(num_of_frames, fps=fps)
                # print("Found_TS:", found_TS)
                found_TS_list.append(found_TS)

            count = count + 1
            # If there are no more frames left
            if count > video_length - 1:
                prbar.update(-1)

                # Log the time again
                time_end = time.time()
                # Release the feed
                cap.release()
                # print("Found_TS:",TS)
                print("It took %d seconds forconversion." %
                      (time_end - time_start))
                print(f"black frames:{black}")
                print("video_length:", video_length)

                try:
                    print(get_file_data(input_loc))
                except Exception:
                    print("There was no TV-Show data.")

                return remove_duplicates(found_TS_list)
            else:
                prbar.update(1)

if __name__ == '__main__':
    # input_file = "C:\\Users\\Daren\\Videos\\Testing_Video_files\\testmp4.mp4"
    input_file  = r"C:\Users\Daren\Videos\Little_House_in_the_Parie\S1\D1 S1\Little_House_in_the_Parie - s01e01 - A Harvest of Friends.mkv"
    output_file = "C:\\Users\\Daren\\Videos\\Testing_Video_files\\"
    print(get_dark_frames(input_file))
