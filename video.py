from moviepy.editor import *
# from moviepy.config import change_settings

# change_settings({"IMAGEMAGICK_BINARY": "/usr/local/bin/convert"})
clip = VideoFileClip("videoplayback.mp4")
clip.audio.write_audiofile("theaudio1.mp3")
duration = clip.duration 
print(duration)
# Make the text. Many more options are available.
# txt_clip = (TextClip("My Holidays 2013",fontsize=70,color='white')
#              .set_position('center')
#              .set_duration(10))

# result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
# result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...
# clip.audio.write_audiofile("theaudio.mp3")
