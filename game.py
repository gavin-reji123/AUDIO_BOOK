import pyttsx3 as py
import PyPDF2
import speech_recognition as sr
import pyaudio



#phase 1

def u():
   print("enter the page number to read using phase 1 (type) :")
   a=int(input(" "))
   a-=1
   page=read.getPage(a)
   question=str(input("which voice (m/f):"))
   answer="m"
   if question == answer :
       txt=page.extractText()
       speaker.say(txt)
       speaker.runAndWait()
   else:
       voices=speaker.getProperty('voices')
       speaker.setProperty('voice',voices[1].id)
       txt = page.extractText()
       speaker.say(txt)
       speaker.runAndWait()


#phase 2

def j():
   r = sr.Recognizer()
   with sr.Microphone() as source: 
     r.adjust_for_ambient_noise(source, duration=3)
     print("which page to be read using phase 2(speak the number)")
     audio=r.listen(source,timeout=5)
     print("please wait.....")
     b=int(r.recognize_google(audio))
     b-=1
     page = read.getPage(b)
   question = str(input("which voice (m/f):"))
   answer = "m"
   if question == answer:
       txt=page.extractText()
       speaker.say(txt)
       speaker.runAndWait()
   else:
      voices = speaker.getProperty('voices')
      speaker.setProperty('voice', voices[1].id)
      txt = page.extractText()
      speaker.say(txt)
      speaker.runAndWait()



#phase 3

def  k():
   print("enter the page number to read phase 3(type):")
   a=int(input("  "))
   question = str(input("which voice (m/f):"))
   answer = "m"
   for i in range(1,a):
     page=read.getPage(i)
     if question == answer:
        txt=page.extractText()
        speaker.say(txt)
        speaker.runAndWait()
     else:
         voices = speaker.getProperty('voices')
         speaker.setProperty('voice', voices[1].id)
         txt = page.extractText()
         speaker.say(txt)
         speaker.runAndWait()


b = open('oop.pdf','rb')
read=PyPDF2.PdfFileReader(b)
c= read.numPages
print("\n")
print("total number of pages :")
print(c)
speaker =py.init()
print("CHOOSE FROM 1 TO 3 :")
print("1)phase 1\n2)phase 2 \n3)phase 3")
d=input("enter the number :")
if(d=="1"):
    u()
if(d=="2"):
    j()
if(d=="3"):
    k()


print("Create by : \n\t GAVIN REJI \n\t AKSHAT SAHANI \n\t BITAN PAUL \n\t GIRESH ")
print("THANK YOU !!!! :)")