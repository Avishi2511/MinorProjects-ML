from moviepy.editor import *

video = VideoFileClip("C:/Users/hp/Desktop/ML_Lab_Projects/sampleVideo.mp4")
audio = video.audio
audio.write_audiofile("C:/Users/hp/Desktop/ML_Lab_Projects/outputAudio.mp3")

audio.close()
video.close()