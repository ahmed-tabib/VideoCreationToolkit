import vctk
import ffmpeg

output_params = {
    "y": None,
    "shortest": None,
    "c:v": "hevc_nvenc",
    "c:a": "copy",
    "pix_fmt": "yuv420p",
}

audio = ffmpeg.input('D:\dev\QuizVideoGen\media\\timer.mp3')
video = vctk.gen_bg_spliced_video(input_file_dir='D:\\dev\\QuizVideoGen\\media\\bg', video_len=54.2, segment_len=3.0)

print(ffmpeg.output(audio, video, 'test.mp4', **output_params).compile())

( 
    ffmpeg
    .output(audio, video, 'test.mp4', **output_params)
    .run()
)