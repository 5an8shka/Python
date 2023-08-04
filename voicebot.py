#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SpeechRecognition


# In[2]:


pip install pyttsx3 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:



pip install pipwin


# In[4]:


pip install PyAudio


# In[11]:


pip install wikipedia


# In[10]:


pip install pyowm


# In[9]:


pip install youtube-dl


# In[8]:


pip install python-vlc


# In[6]:


pip install beautifulsoup4


# In[ ]:


import speech_recognition as sr #provides ability to listen spoken words and identify them
import sys  #used to access those variables and functions which interact strongly with intrepeter
import re   #provides regular expression support
import webbrowser  #provides a high-level interface to allow displaying web-based documents to users
import requests   #allows to send http requests in python
from pyowm import OWM  #to access weather data of different locations
from urllib.request import urlopen  #for fetching urls
from bs4 import BeautifulSoup as soup  #bs4: pulling data from html and xml files||
#beautifulsoup:makes it easy to scrape information from web pages
import wikipedia  #makes it easy to access data from wikipedia
from time import strftime  #time: provide ways to represent time||
#strftime:format date objects and present them in readable form 
import pyttsx3  #text to speech conversion library



def response(audio):  #function to convert text to speech
    "speaks audio passed as argument"
    print(audio)
    engine = pyttsx3.init()
    engine.getProperty('rate')  #getting speech rate from pyttsx3  
    engine.setProperty('rate', 150)  # default speech rate is 200; here it is 150
    engine.getProperty('volume')   #getting volume from pyttsx3
    engine.setProperty('volume',2.0)  #default volume is 1.0
    engine.say(audio)  #say is used to speak the audio argument
    engine.runAndWait()  #blocks furthur execution till speaking of audio argument is done
    
    
      
def myCommand():  #function to recognize the command
    r = sr.Recognizer() #new object is created from speechrecognition
    with sr.Microphone() as source: #new object from speechrecoginition which represents the source of audio input(microsoft)
        response('Say something...')  #calls sofiaResponse function to prompt user to speak
        r.pause_threshold = 1   #The pause threshold is the amount of time in seconds of non-speaking audio to consider the end of a phrase or sentence here it is 1 sec
        r.adjust_for_ambient_noise(source, duration=1)  # adjusts the recognizer's sensitivity to background noise by analyzing a short sample of audio from the microphone
        audio = r.listen(source)  #captures the audio input from the microphone using the listen()
    try:  #use google recognizer to convert the captured audio to text using Google's speech recognition API and convert them into lowercase and display
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError: #if speech recognition not successful then error is raised and the function prints a message to the console and then calls itself recursively to prompt the user to try again
        print('....')
        command = myCommand();
    return command  #the function returns the recognized command as a string



def assistant(command):
        
        
        
        
        
        if 'open whatsapp' in command:
            reg_ex = re.search('open whatsapp (.*)', command) #search for extra text user as given along with the required one like phone no. or contact
            url = 'https://web.whatsapp.com/' 
            if reg_ex:   #check whether the regex search was successful or not
                recipient = reg_ex.group(1)  #initialized by the extra text added by user
                url = url + 'send?phone=' + recipient  #extra text added to the url if any
            webbrowser.open(url)
            response('WhatsApp has been opened for you.')

        
        
                
        elif 'bye' in command:
            response('bye bye Have a nice day')
            sys.exit()  #to exit the voicebot
        
        
        
        
        elif 'open' in command:
            reg_ex = re.search('open (.+)', command) #to search extra text added by the  user
            if reg_ex: #after search is successful this code will be executed
                domain = reg_ex.group(1) #the extra text said by user is saved in domain
                print(domain)  #printing the extra text said by user
                url = 'https://www.' + domain  #creating url for the same
                webbrowser.open(url)
                response('The website you have requested has been opened for you .')
            else:
                pass  #if nothing is mentioned by the user then it will pass
        
        
        
        
        elif 'hello' in command:
            day_time = int(strftime('%H'))  #to get the current time
            if day_time < 12:
                response('Hello . Good morning')
            elif 12 <= day_time < 18:
                response('Hello . Good afternoon')
            else:
                response('Hello . Good evening')
         
        
        
            
        elif 'help me' in command:
            print("""
             You can use these commands and I'll help you out:
        1. Say Hello
        2. Open xyz.com
        3. news for today
        4. time : Current system time
        5.tell me a joke
        6. tell me about xyz
        7. open whatsapp
        8.bye to exit
        """)
        
        
        
        
        elif 'joke' in command:
            res = requests.get(
                'https://icanhazdadjoke.com/',  #to get jokes from specific url which is joke API and returns in JSON format(a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications )
                headers={"Accept":"application/json"}) # to specify that the program is requesting JSON data.
            if res.status_code == requests.codes.ok: #checks if the response from the API is successful
                response(str(res.json()['joke'])) #extracts the joke text from the JSON response and passes it to the response() to be spoken by the bot
            else:
                response('oops!I ran out of jokes')
            
            
            
            
        elif 'news for today' in command:
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url) #to open the url from previous line
                xml_page=Client.read() #reads the content of the RSS feed from client
                Client.close() #closes client
                soup_page=soup(xml_page,"xml") #use beautiful soup to get data from webpage
                news_list=soup_page.findAll("item") #lists contents from rss feed
                for news in news_list[:5]:  #will read top 5 news feed
                    response(news.title.text.encode('utf-8')) #.encode('utf-8') is common format to convert web info into text
            except Exception as e: # to catch if there is any error
                   print(e)     #to print the error
                
                
            
        elif 'time' in command:
            import datetime  
            now = datetime.datetime.now()
            response('Current time is %d hours %d minutes' % (now.hour, now.minute))
        
        
        
        elif 'tell me about' in command:
            reg_ex = re.search('tell me about (.*)', command) #to search the info entered by user
            try:
                if reg_ex:
                    topic = reg_ex.group(1) # to store the text by the user
                    ny = wikipedia.page(topic) #to fing the info from wikipidea
                    response(ny.content[:500].encode('utf-8'))  # to display the response
            except Exception as e: #if the topic is not on wikipidea then exception occurs
                    print(e)
                    response(e)
                
                
                
response('Hi buddy,I am JOJO, your personal voice assistant, how can I help you.')
while True:
    assistant(myCommand())
    
    

    


# In[ ]:




