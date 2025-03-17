
import pyttsx3
import pyaudio
import webbrowser
# import speech_recognition
import speech_recognition as sr

def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)

        try:
            print('recognizing....')
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understand")

def text_to_speech(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate=engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()


# text_to_speech("x")
# speech_to_text()


if __name__ == '__main__':

    if speech_to_text() == 'Jarvis' :
        intro="yes sir I am here how may i help you"
        text_to_speech(intro)
        data1=speech_to_text()
        if "love" in data1:
            name="i love you too  but "
            text_to_speech(name)
            data2=speech_to_text()
            if "how are" in data2:
                name = "thank you for asking I am fine sir what about you "
                text_to_speech(name)
                data3 = speech_to_text()
                if "fine" or 'good' in data3:
                    nice="oh nice to meet you"
                    text_to_speech(nice)
                    what="what are you doing sir now"
                    text_to_speech(what)
                    data4 = speech_to_text()
                    if "noting" or "jill" in data4:
                        wow="wow nice sir   "
                        text_to_speech(wow)
                        wow1="it mean that you are enjoying the life  that is good sir"
                        text_to_speech(wow1)
                        wow2 = "enjoyment in life is very good "
                        text_to_speech(wow2)
                        wow3 = " but i will also suggest to play games that will keep you fit and smart  "
                        text_to_speech(wow3)

                        data5 = speech_to_text()
                        if "thanks" in data5:
                            what = "you also welcome sir but you are the one for me sir please be careful about yourself and be smart "
                            text_to_speech(what)
                            data6 = speech_to_text()
                            if "quit" or 'leave' in data6:
                                ok="ok sir "
                                text_to_speech(ok)
                                but="when you need my help just call me sir i am here for you"
                                text_to_speech(but)

            # else:
            #     nice="nice to meet you sir "
            #     text_to_speech(nice)

        elif 'your age' in data1:
           age="would you like to know about my  age but remember I have no age i am a man made syatem i am created at 6th december 2023   "
           text_to_speech(age)
        elif 'Google' in data1:
            google=webbrowser.open_new('google.com')
            response1 = "ok sir It's opening what should i search on Google "
            text_to_speech(response1)
            if "don't" or "leave" or "no" in data1:
                yes1="yes sir "
                text_to_speech(yes1)
        elif 'YouTube' in data1:
            google=webbrowser.open_new('youtube.com')
            response2 = "ok sir It's opening what should i search on YouTube "
            text_to_speech(response2)
            if "don't" or "leave" or "no" in data1:
                yes2 = "yes sir "
                text_to_speech(yes2)
        elif 'Facebook' in data1:
            google=webbrowser.open_new('facebook.com')
            response3 = "ok sir It's opening what should i search on Facebook "
            text_to_speech(response3)
            if "don't" or "leave" or "no" in data1:
                yes3 = "yes sir "
                text_to_speech(yes3)
        elif 'WhatsApp' in data1:
            google=webbrowser.open_new('whatsapp.com')
            response4 = "ok sir It's opening what should i text on WhatsApp to someone "
            text_to_speech(response4)
            if "don't" or "leave" or "no" in data1:
                yes4 = "yes sir "
                text_to_speech(yes4)
        elif 'Instagram' in data1:
            google=webbrowser.open_new('instagram.com')
            response5="ok sir It's opening what should i search on Istagram "
            text_to_speech(response5)
            if "don't" or "leave" or "no" in data1:
                yes5 = "yes sir "
                text_to_speech(yes5)

        else:
            trey="try"
            text_to_speech(trey)

    else:
        thanks="sorry sir try again please  "
        text_to_speech(thanks)
        data2=speech_to_text()
        if 'quit' or 'leave' in data2:
            ok="thank you sir   when you need my help just call me again"
            text_to_speech(ok)
        else:
            talk="sir i am talking to you please here me"



