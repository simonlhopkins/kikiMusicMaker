
import moviepy
import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip

if len(sys.argv) != 3:
    print("run command like this\npython3 main.py <audio clip name> <start time>")
#change this number to determine where the music will start on the audio clip
startTime =int(sys.argv[2]);

#set the name of the audio file here
audio_background = AudioFileClip(str(sys.argv[1]))
intro = VideoFileClip("kikipt1.mp4")
silentKiki = VideoFileClip("kikipt2.mp4")
startTime = min(startTime, audio_background.duration - silentKiki.duration)
trimmedAudio = audio_background.subclip(startTime, startTime + silentKiki.duration)

final_audio = CompositeAudioClip([silentKiki.audio, trimmedAudio])
final_clip = silentKiki.set_audio(final_audio)
returnClip = concatenate_videoclips([intro, final_clip])
returnClip.write_videofile("final.mp4")


 #  _
 # | |
 # | | _____   _____
 # | |/ _ \ \ / / _ \
 # | | (_) \ V /  __/_
 # |_|\___/ \_/ \___( )
 #     (_)          |/
 #  ___ _ _ __ ___   ___  _ __
 # / __| | '_ ` _ \ / _ \| '_ \
 # \__ \ | | | | | | (_) | | | |
 # |___/_|_| |_| |_|\___/|_| |_|
 #
