import speech_recognition as sr

# speech recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Recognizing...")
    audio_data = r.listen(source, timeout=5)

    try:
        text = r.recognize_google(audio_data)
        print("Text: " + text)
    except:
        print("Sorry, I did not get that.")
