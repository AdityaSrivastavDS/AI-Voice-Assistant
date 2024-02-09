# Import necessary libraries
import re
import sre_compile
from google.cloud import speech
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np
import pyttsx3

# Initialize chat string
chatStr = ""

# Function to chat with OpenAI's GPT-3 model
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Jarvis: "
    # Generate a response using GPT-3
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Speak the response
    say(response["choices"][0]["text"])
    # Add the response to the chat string
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

# Function to generate a response from OpenAI's GPT-3 model and save it to a file
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    # Generate a response using GPT-3
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    # Create a directory if it doesn't exist
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # Save the response to a file
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

# Function to convert text to speech
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to listen to a command from the user using Google Cloud Speech-to-Text
def takeCommand():
    client = speech.SpeechClient()

    with sre_compile.Microphone() as source:
        audio = re.listen(source)
        audio_content = audio.get_wav_data()

    response = client.recognize(
        config=speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        ),
        audio=speech.RecognitionAudio(content=audio_content),
    )

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))
        return result.alternatives[0].transcript

    return "Some Error Occurred. Sorry from Mihir's side."

# Main function
if __name__ == '__main__':
    print('Welcome to Mihir A.I')
    say("Mihir A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        # Open a website if the user asks to
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # Play music if the user asks to
        if "open music" in query:
            musicPath = "/path/to/your/music/file.mp3"
            os.startfile(musicPath)

        # Tell the time if the user asks for it
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        # Respond to requests to open FaceTime or Passky
        elif "open facetime".lower() in query.lower():
            say("Sorry, FaceTime is not available on Windows.")
        elif "open pass".lower() in query.lower():
            say("Sorry, Passky is not available on Windows.")

        # Generate a response using GPT-3 if the user asks a question about AI