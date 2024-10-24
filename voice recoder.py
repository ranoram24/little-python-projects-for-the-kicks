import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import os

folder_path = "C:/Users/ranor/Desktop/on the side py projects/recording messeges"
# Sample frequency
freq = 44100

#how long the recording in seconds
duration = 2

#start recording and waiting for it to finish
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)


sd.wait()

#naming the file and make sure there are no duplicates in the folder or replacement by name 
i = 1
file_name = f"recording{i}.wav"


while os.path.exists(os.path.join(folder_path, file_name)):
    i += 1
    file_name = f"recording{i}.wav"
#writing the recording to a wav file and saving it
wv.write(os.path.join(folder_path, file_name), recording, freq, sampwidth=2)
