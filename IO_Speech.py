# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Tue Oct 24 12:26:50 2017

@author: ebgaspar
"""

import os

from time import ctime
#import time

#import pyttsx
import speech_recognition as sr
from gtts import gTTS

 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='pt')
    tts.save("d:/hello.mp3")
    os.system("\"c:/Program Files (x86)/Windows Media Player/wmplayer.exe\" /play /Close d:/hello.mp3")

#def speak( audioString ) :
#    engine = pyttsx.init()
#    engine.say( audioString )
#    engine.runAndWait()    
 
def listenUser():
    r = sr.Recognizer()
    r.energy_threshold = 5500

    with sr.Microphone( 1 ) as source:
        print( "Fale" )
        speak( "Fale" )
        audio = r.listen( source )
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google( audio, language="pt-Br" )
        print( "Entrada : " + data )
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def answerUser( data ):
    if "Como vai" in data :
        speak( 'Estou bem' )
 
    if "Que horas são" in data :
        speak( ctime() )
        
    if "sair" in data :
        speak( 'Adeus' )
        raise SystemExit
 
def main( ):
    # initialization
#    time.sleep(2)
    speak("Olá, o que posso fazer por você?")
    while True:
        data = listenUser()
        answerUser( data )
        
if __name__== "__main__":
  main()        

