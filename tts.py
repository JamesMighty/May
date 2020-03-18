from gtts import gTTS
import string
from playsound import playsound
import unidecode

def TTS (output):
    tts = gTTS(output, lang='cs', slow=False)
    tts.save(output+'.mp3')
    playsound(output+'.mp3')
	

def text_edit (text):
    text = unidecode.unidecode(text)
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace(":", "")
    text = text.replace("<", "")
    text = text.replace(">", "")
    text = text.replace(";", "")
    return text.lower()

while True:
	inp = TTS(input("MARI>> "))
	print(inp)