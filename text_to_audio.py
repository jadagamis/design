import pyttsx3
engine = pyttsx3.init()
text = input("Convert this text to audio: ")
name = input("The file will be called: ")
engine.say(text)
engine.runAndWait()
engine.save_to_file(text, f"{name}.mp3")
engine.runAndWait()