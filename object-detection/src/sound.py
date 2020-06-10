from gtts import gTTS 
from playsound import playsound
import os
class tts:
    def txt(self,msg):
        mytext = msg 
        language = 'en'
      
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
        myobj = gTTS(text=mytext, lang=language, slow=False) 
    # Saving the converted audio in a mp3 file named  
        myobj.save("speak.mp3") 
      
    # Playing the converted file 
        playsound("./speak.mp3")

        if os.path.exists("speak.mp3"):
            os.remove("speak.mp3")