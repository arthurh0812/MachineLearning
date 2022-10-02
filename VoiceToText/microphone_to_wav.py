import wave
import pyaudio
import sys

# one kilobyte (1024 frames)
CHUNK = 1024
# Int16 format
FORMAT = pyaudio.paInt16
# 2 channels (2 simultaneous sounds)
CHANNELS = 2
# frame rate per second (standard frame frate)
RATE = 44100
# number of seconds to record
DURATION = 5
# default wav filename
OUTPUT_FILENAME = "sound.wav"

# 1. check if filename.wav is passed as runtime argument; if so, then use it as output filename
if len(sys.argv) > 1:
    OUTPUT_FILENAME = sys.argv[1]

# 2. create a pyaudio.PyAudio object and stream that will read the microphone data according to
# configuration
pa = pyaudio.PyAudio()

pa_stream = pa.open(
    rate=RATE,
    format=FORMAT,
    channels=CHANNELS,
    input=True,
    frames_per_buffer=CHUNK
)

frames = []

chunks_per_second = RATE/CHUNK
# 3. write to the wav file using the PyAudio stream that reads the data from the microphone
for i in range(0, int(chunks_per_second*DURATION)):
    data = pa_stream.read(num_frames=CHUNK)
    frames.append(data)

# 4. stop and close the input stream and terminate PyAudio object streaming
pa_stream.stop_stream()
pa_stream.close()
pa.terminate()

# 5. open the wav file (writing mode) and write the frames to it
wav_file = wave.open(OUTPUT_FILENAME, mode="w")
wav_file.setnchannels(CHANNELS)
wav_file.setframerate(RATE)
wav_file.setsampwidth(pa.get_sample_size(FORMAT))
wav_file.writeframes(b''.join(frames))

# 6. close the wav file writing process
wav_file.close()
