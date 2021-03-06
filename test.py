import ffmpeg

input = ffmpeg.input('osaka-vid.mp4')
audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
video = input.video.hflip()
out = ffmpeg.output(audio, video, 'out.mp4')
print(out)