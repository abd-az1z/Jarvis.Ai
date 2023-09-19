import speech_recognition as sr #for recognition of speech
import win32com.client #for speaking of speech
import webbrowser #for opening websites
import datetime #for recognizing the date and time
# import pygame #to play stored music
# import os

speaker = win32com.client.Dispatch("SAPI.SpVoice")

recognizer = sr.Recognizer()
def take_command():
    with sr.Microphone() as source:
        print("Listening..")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        recognizer.pause_threshold = 0.5
        print("Recognizing...")
        try:
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some Error Occured, Sorry from Jarvis!"

print("PyCharm")
speaker.Speak("Hello This Is Jarvis AI")

while True:
    query = take_command()
    speaker.Speak(f"{query}")
    sites = [["youtube", "http://youtube.com"], ["google", "http://google.com"], ["chatGPT", "http://chatgpt.com"], ["artificial", "https://bard.google.com/"], ["wikipedia", "http://wikipedia.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            speaker.Speak(f"Opening {site[0]} Sir.....")
            webbrowser.open(site[1])
    # if "Open Music" in query:
    #     music_file_path = "C:\\Users\\mohda\\OneDrive\\Desktop\\Movies\\Musics\\Tera Chehra.mp3"
    #     speaker.Speak("Opening Music Sir...")
    #     os.system(f"open{music_file_path}")
    if "time" in query:
        # strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        # speaker.Speak(f"Sir the time is{strfTime}")
        hour = datetime.datetime.now().strftime("%H")
        mins = datetime.datetime.now().strftime("%M")
        speaker.Speak(f"Sir the time is{hour} bajhkay {mins} minutes")
