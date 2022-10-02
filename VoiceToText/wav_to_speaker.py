import sys
import wave
import pyaudio

# one kilobyte (1024 frames)
CHUNK = 1024
# default wav filename
INPUT_FILENAME = "sound.wav"

# 1. check if filename.wav is passed as a runtime argument; if so, then use is as input filename
if len(sys.argv) > 1:
    INPUT_FILENAME = sys.argv[1]

# 2. open the filename.wav file (reading mode)
wave_file = wave.open(INPUT_FILENAME, mode="r")

# 3. instantiate a pyaudio.PyAudio object and a stream (output) to write the wave data to
# such a stream will play the given frame data using the system's speaker
pa = pyaudio.PyAudio()

pa_stream = pa.open(
    format=pa.get_format_from_width(wave_file.getsampwidth()),
    channels=wave_file.getnchannels(),
    rate=wave_file.getframerate(),
    output=True
)

# 4. read one kilobyte from the wave file
data = wave_file.readframes(nframes=CHUNK)

# 5. write that chunk of data to the stream and repeat as long as there is data left to read
while len(data) > 0:
    pa_stream.write(frames=data)
    data = wave_file.readframes(nframes=CHUNK)

# 6. stop and close the stream (output)
pa_stream.stop_stream()
pa_stream.close()

# 7. close PyAudio
pa.close()
