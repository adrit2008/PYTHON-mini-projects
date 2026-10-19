from gtts import gTTS # pyright: ignore[reportMissingImports]

text = "Hello, welcome to the text to speech generator! it's created by adrit"

tts = gTTS(text=text, lang='en')
tts.save('output.mp3')
print("Audio file 'output.mp3' has been generated successfully.")