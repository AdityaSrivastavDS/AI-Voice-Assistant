# Mihir A.I - Voice Assistant

![Project Logo](https://drive.google.com/file/d/17GZZL4qVyZwonMOfLyUSl8-S6Yz-Ahff/view?usp=sharing)

## Overview

Mihir A.I is a Python-based voice assistant that integrates various functionalities, including speech recognition, natural language processing with OpenAI's GPT-3, web browsing, and task automation. The assistant enables users to interact through voice commands and responds using both pre-defined actions and intelligent chat capabilities.

## Features

- **Speech Recognition:** Utilizes Google Cloud Speech-to-Text for interpreting user voice commands.
- **OpenAI Integration:** Incorporates OpenAI's GPT-3 model for intelligent conversations and responses.
- **Web Browsing:** Opens specified websites based on user commands.
- **Task Automation:** Performs actions like opening music files, providing the current time, and responding to specific queries.

## Getting Started

Follow these instructions to set up and run Mihir A.I on your local machine.

### Prerequisites

- Python 3.x
- Install required packages: `pip install -r requirements.txt`
- Set up Google Cloud Speech-to-Text and obtain API credentials.
- Obtain OpenAI GPT-3 API key.

### Configuration

1. Create a `config.py` file with your API keys:

   ```python
   # config.py

   # Google Cloud Speech-to-Text API key
   google_api_key = 'your_google_api_key_here'

   # OpenAI GPT-3 API key
   apikey = 'your_openai_api_key_here'

2.Adjust other configurations in the code, such as website URLs, music file path, etc.

## Usage

- **1.**Run the voice assistant: python voice_assistant.py
- **2.**Mihir A.I will start listening for your commands.

## Functionalities

- **Chat with OpenAI's GPT-3**
- **The assistant engages in intelligent conversations using OpenAI's GPT-3. The chat history is stored for context.**

•python
- **Copy code**
- **chat("How are you?")**
- **Web Browsing**

### Open specified websites with commands like:

- **"Open YouTube"**
- **"Open Wikipedia"**
- **"Open Google"**
- **Task Automation**
- **Play music: "Open music"**
- **Get the current time: "What's the time?"**
- **Intelligent Responses**


### Ask questions related to AI:

- **python**
- **Copy code**
- **ai("What is the impact of artificial intelligence on society?")**
- **Responses are saved to the "Openai" directory.**

## Contributing

•Contributions are welcome! Please follow the contribution guidelines to contribute to this project.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to Google Cloud and OpenAI for their powerful APIs.
