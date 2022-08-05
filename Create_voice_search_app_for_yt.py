import speech_recognition as sr
import pyaudio
import pywhatkit
import time

def question_en():
    print(' ')
    print('Do you want to search something verbally?')
    troad = input('Type "yt" to search from youtube and "go" to search from google. :')
    if troad.lower() == 'yt':
        get_audio_yt()
    elif troad.lower() == 'go':
        get_audio_go()
    else:
        print('Please enter valid command.')
        mainbody()


def question():
    print(' ')
    print('Sesli arama ile size yardımcı olabiliriz.')
    yol = input('Youtubeden bir şeyler aramak için "yt", Googleden bir şeyler aratmak için "go" yazınız.')
    if yol.lower() == 'yt' :
        get_audio_yt_tr()
    elif yol.lower() == 'go':
        get_audio_go_tr()
    else:
        print('Düzgün değerler giriniz.')
        mainbody_tr()


def get_audio_yt():
    recorder= sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        audio = recorder.listen(source)
    
    text = recorder.recognize_google(audio)
    print(f'You said: {text}')
    pywhatkit.playonyt(text)
    mainbody()


def get_audio_go():
    recorder= sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        audio = recorder.listen(source)
    
    text = recorder.recognize_google(audio)
    print(f'You said: {text}')
    pywhatkit.search(text)
    mainbody()


def get_audio_yt_tr():
    recorder= sr.Recognizer()
    with sr.Microphone() as source:
        print('Bir şeyler söyleyin...')
        audio = recorder.listen(source)
    
    text = recorder.recognize_google(audio, language='tr-TR')
    print(f'Aranılan: {text}')
    pywhatkit.playonyt(text)
    mainbody_tr()


def get_audio_go_tr():
    recorder= sr.Recognizer()
    with sr.Microphone() as source:
        print('Bir şeyler söyleyin...')
        audio = recorder.listen(source)
    
    text = recorder.recognize_google(audio, language='tr-TR')
    print(f'Aranılan: {text}')
    pywhatkit.search(text)
    mainbody_tr()


def mainbody():
    mainbodyi = input('If you wanna continue app enter "yes" or you wanna quit please enter "no". ')
    if mainbodyi.lower() == 'yes':
        troad = input('Type "yt" to search from youtube and "go" to search from google. :')
        if troad.lower() == 'yt':
            get_audio_yt()
        elif troad.lower() == 'go':
            get_audio_go()
        else:
            print('Please enter valid command.')
            question_en()
    elif mainbodyi.lower() == "no":
        print('Quiting...')
        time.sleep(1.5)
        print('Thanks for using my app')
        exit()
    else:
        print('Please enter valid command.')
        mainbody()


def mainbody_tr():
    mainbodyi = input('Eğer devam etmek istiyorsanız "evet", programı sonlandırmak için "hayır" yazınız. ')
    if mainbodyi.lower() == 'evet':
        troad = input('Youtubeden bir şeyler aramak için "yt", Googleden bir şeyler aratmak için "go" yazınız.')
        if troad.lower() == 'yt':
            get_audio_yt_tr()
        elif troad.lower() == 'go':
            get_audio_go_tr()
        else:
            print('Lütfen düzgün değerler giriniz')
            question()
    elif mainbodyi.lower() == "hayır":
        print('Çıkış yapılıyor...')
        time.sleep(1.5)
        print('Uygulamamı kullandığınız için çok teşekkür ederim.')
        exit()
    else:
        print('Lütfen düzgün değerler giriniz.')
        mainbody_tr()




print('Welcome/Hoşgeldiniz.')
body = input('Type "en" to continue in English./Ingilizce devam etmek için "en" yazarak devam ediniz.')
if body.lower() == 'en':
    name = input('Your name ? : ')
    print('Welcome ' + name.capitalize())
    time.sleep(1)
    print('How can i help you ?')
    time.sleep(1)
    print('Do you want to search something verbally?')
    time.sleep(1)
    troad = input('Type "yt" to search from youtube and "go" to search from google. :')
    if troad.lower() == 'yt':
        get_audio_yt()
    elif troad.lower() == 'go':
        get_audio_go()
    else:
        print('Please enter valid command.')
        time.sleep(2)
        question_en()
else:
    isim = input('Isminiz ? : ')
    print('Hoşgeldin ' + isim.capitalize())
    time.sleep(1)
    print('Size nasıl yardımcı olabilirim ?')
    time.sleep(1)
    print('Sesli arama ile size yardımcı olabiliriz.')
    time.sleep(1)
    yol = input('Youtubeden bir şeyler aramak için "yt", Googleden bir şeyler aratmak için "go" yazınız. ')
    if yol.lower() == 'yt' :
        get_audio_yt_tr()
    elif yol.lower() == 'go':
        get_audio_go_tr()
    else:
        print('Düzgün değerler giriniz.')
        time.sleep(2)
        question()