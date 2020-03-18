import unidecode
import string
from gtts import gTTS
from playsound import playsound

def any_common(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return True 
    else: 
        return False

def TTS (output):
    tts = gTTS(output, lang='cs', slow=False)
    tts.save(output)
    playsound(output)

def ofline_TTS (output):
    playsound(output)

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