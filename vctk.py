import ffmpeg
import random

import os
import subprocess

#
# Return the length in seconds (float) of a media (audio/video)
#
def get_media_length(path):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

#
# Get a random segment of a video, of length "segment_len"
#
def get_random_segment(input_file: str, segment_len: float):
    video_len = get_media_length(input_file)
    if video_len < segment_len:
        raise ValueError("Requested segment length is longer than the provided video")
    
    start_point = random.randint(0, int(video_len - segment_len))
    end_point = start_point + segment_len

    video = ffmpeg.input(input_file)

    return (
        video
        .trim(start=start_point, end=end_point)
        .setpts('PTS-STARTPTS')
    )


#
# Generate a background video that's spliced together from a bunch of other videos (b-roll, minecraft, etc..)
# No one file is guaranteed to be selected, A segment_len interval is chosen from a random video and added to 
# the output. the start and endpoints are random. The final video will be an amalgamation of random clips cut together.
# Width and height determine the dimensions of the final video, all videos will be scaled to this.
#
def gen_bg_spliced_video(input_file_list: None | list = None,
                         input_file_dir: None | str = None,
                         video_len: float = 10.0,
                         segment_len: float = 5.0,
                         width: None | int = None,
                         height: None | int = None):
    
    if input_file_list == None:
        if input_file_dir == None:
            raise ValueError("Must specify either input file list or input file directory")
        input_file_list = [os.path.join(input_file_dir, file) for file in os.listdir(input_file_dir)]
    
    # determine the length and number of segments to use
    segment_lengths = [segment_len] * int(video_len // segment_len)
    if (video_len // segment_len) < (video_len / segment_len):
        segment_lengths.append(video_len % segment_len)


    # create an ffmpeg stream for each segment
    segment_streams = []
    for s in segment_lengths:
        stream = get_random_segment(random.choice(input_file_list), s)

        if width != None or height != None:
            if width == None:
                width = -1
            elif heigh == None:
                height = -1
            stream = stream.filter('scale', width, height)

        segment_streams.append(
            stream            
        )
    
    if len(segment_streams) == 1:
        return segment_streams[0]
    else:
        return (
            ffmpeg.concat(*segment_streams)
        )
        