import pyaudio
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import webbrowser
import os
import winshell
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import win32com.client as wincl
from urllib.request import urlopen
import speech_recognition as sr
import pyttsx3
import datetime



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        print("Good Morning Sir !")
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        print("Good Morning Sir !")
        speak("Good Afternoon Sir !")  
  
    else:
        print("Good Morning Sir !")
        speak("Good Evening Sir !") 
  
    assname =("AI DIABETES CHECK SYSTEM")
    speak("I am your Doctor")
    speak(assname)

import speech_recognition as sr
def take():
    global text
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("Done recording")

    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="en-UK"
            )

        print("Decoded Text : {}".format(text))

    except Exception as ex:

        print(ex)

    return text


def Pregnancies():
    print("No of Pregnancies you have ???")
    speak("No of Pregnancies you have")

def Glucose():
    print("Whats your Glucose level")
    speak("Whats your Glucose level")

def BloodPressure():
    print("Enter Whats your BloodPressure")
    speak("Enter Whats your BloodPressure")

def SkinThickness():
    print("Enter your SkinThickness")
    speak("Enter your SkinThickness")

def Insulin():
    print("Enter Insulin Level")
    speak("Enter Insulin Level")

def BMI():
    print("Enter Your BMI")
    speak("Enter Your BMI")

def DiabetesPedigreeFunction():
    print("Enter Number of Diabetes Pedigree Function")
    speak("Enter Number of Diabetes Pedigree Function")

def Age():
    print("Enter Your Age")
    speak('Enter Your Age')

def badresult():
    print("You have diabetes You need to see the doctors")
    speak("You have diabetes You need to see the doctors")
    import webbrowser
    search_terms = ['diabetes doctor near me ']

    # ... construct your list of search terms ...

    for term in search_terms:
        url = "https://www.google.com.tr/search?q={}".format(term)
        webbrowser.open_new_tab(url)






