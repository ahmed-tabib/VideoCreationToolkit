import vctk
import ffmpeg

output_params = {
    "y": None,
    "c:v": "hevc_nvenc",
    "pix_fmt": "yuv420p",
}

image = ffmpeg.input('C:\\Users\\ahmed\\Desktop\\methodology-diagram.png')
video = ffmpeg.input('test.mp4')

#overlayed = vctk.add_image(image, video, start=1.0, end=5.0, width=680, height=680, x='min((W-w)/2,-w+(t-1)*1500)')
overlayed = vctk.add_image(image, video, start=1.0, end=5.0, width=680, height=680, x='min((W-w)/2,-w+(t-1)*1500)')

( 
    overlayed
    .output('test2.mp4', **output_params)
    .run()
)