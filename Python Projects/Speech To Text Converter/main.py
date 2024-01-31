import speech_recognition as sr


def record():
    speech_recognizer = sr.Recognizer()

    microphone = sr.Microphone()
    print('Speak')
    
    with microphone as sound:
        audio = speech_recognizer.listen(sound)
    
    try:
        phrase = speech_recognizer.recognize_google(audio)
        return phrase
    except sr.UnknownValueError:
        return "I couldn't understand what you said"
            
if __name__ == '__main__':
    phrase = record()
    if phrase != "I couldn't understand what you said":      
        print(f"You said '{phrase}'")
    else:
        print(phrase)