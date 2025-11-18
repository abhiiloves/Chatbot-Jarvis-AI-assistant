import random
import pyttsx3
import webbrowser
import datetime
import time
import wikipedia

def Speak(Text):
  engine = pyttsx3.init("sapi5")
  voices = engine.getProperty('voices')
  engine.setProperty('voices', voices[0].id)
  engine.setProperty('rate',170)
  engine.say(Text)
  engine.runAndWait()

class SimpleAIBrain:
    def __init__(self):
        self.responses = {
            'greetings': ['Hello! Sir, I am ready to assist you.', 'Hi sir, I am ready to assist you.', 'Hello Sir, I am ready to assist you.'],
            'weather': ['The weather is nice today.', 'It looks like rain.'],
            'my friends name' : ['vikas kumar, kushagra', 'pradeep'],
            ' what is google': [' Google is a search engine that allows users to search for information on the World Wide Web.'],
            'your owner' : [ 'Abhii.. Abhishek', 'Bhanu Pratap Singh'],
            'how are you' : ['I am fine, thank you for asking'],
            'hello jarvis how are you' : ['Hello, I am fine. Thank you for asking'],
            'hello' : ['Hello Sir, I am ready to assist you.'],
            'thank you jarvis': [ 'welcome! Sir'],
            'youtube' : ['opening youtube', 'Opening the youtube'],
            'introduce' : ['I am a computer program chatbot AI that can understand and respond to human speech.I was created by Abhii AbhishIek . I am named after the character Jarvis from the Iron Man movies.'],
            'who was created you':['Jarvis was created by Abhii AbhishIek, a student at the NGF College of Engineering and Technology, Palwal. I am a computer program chatbot AI that can understand and respond to human speech.I am named after the character Jarvis from the Iron Man movies.'],
            'results' : ['anythings else Sirr'],
            'shopping': ['Amazon'],
            'doing' : ['Nothing Sir, I am ready to asist you.'],
            'default': ['I am not sure how to respond to that.']
        }
 
    def process_input(self, user_input):
        user_input = user_input.lower()

        if any(greeting in user_input for greeting in ['hello', 'hi', 'hey']):
            return self.get_response('greetings')
        elif 'wikipedia' in user_input:
            Speak('Searching Wikipedia....')
            query = user_input.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            Speak('According to Wikipedia')
            Speak(results)
            return self.get_response('results')
        elif 'weather' in user_input:
            return self.get_response('weather')
        elif 'what are you doing' in user_input:
            return self.get_response('doing')
        elif 'thank you' in user_input:
            return self.get_response('thank you jarvis') 
        elif 'about you' in user_input:
            return self.get_response('introduce')
        elif 'introduce yourself' in user_input:
            return self.get_response('introduce')
        elif 'who are you' in user_input:
            return self.get_response('introduce')
        elif 'created you' in user_input:
            return self.get_response('who was created you')
        elif 'vikas' in user_input:
            return self.get_response('vikas')
        elif 'my friends name' in user_input:
            return self.get_response('my friends name')
        elif 'friends name' in user_input:
            return self.get_response('my friends name')
        elif 'friends' in user_input:
            return self.get_response('my friends name')
        elif 'sapna' in user_input:
            return self.get_response('sapna')
        elif 'your god' in user_input:
            return self.get_response('your owner')
        elif 'who am i' in user_input:
            return self.get_response('your owner')
        elif 'google' in user_input:
            return self.get_response(' what is google')
        elif 'tell me about the google' in user_input:
            return self.get_response(' what is google')
        elif 'google' in user_input:
            return self.get_response(' what is google') 
        elif 'how' in user_input:
            return  self.get_response('how are you')
        elif 'how are you' in user_input:
            return self.get_response('how are you')
        elif 'start jarvis' in user_input:
            return self.get_response('hello')
        elif 'open youtube' in user_input:
            url = "https://www.youtube.com"
            webbrowser.open(url)
            print("Opening YouTube...")
            return self.get_response('youtube')
        elif 'open amazon' in user_input:
            url = "https://www.amazon.com"
            webbrowser.open(url)
            print("Opening Amazon...")
            return self.get_response('shopping')
        elif 'open filpkart' in user_input:
            url = "https://www.flipkart.com"
            webbrowser.open(url)
            print("Opening Flipkart...")
            return self.get_response('shoping')
        else:
            return self.get_response('default')

    def get_response(self, category):
        responses = self.responses.get(category, self.responses['default'])
        return random.choice(responses)


def main():
    ai_brain = SimpleAIBrain()
    print("Jarvis: Hello! I'm your AI. You can start chatting with me. Type 'exit' to end the conversation.")
    Speak(" Hello! I'm your AI. You can start chatting with me. Type 'exit' to end the conversation")
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            Speak("Goodbye!Sirr")
            break

        ai_response = ai_brain.process_input(user_input)
        print(f"Jarvis: {ai_response}")
        Speak(ai_response)

if __name__ == "__main__":
    main()

