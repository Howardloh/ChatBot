# Chatbot Application

## Overview
This Python-based chatbot application leverages natural language processing (NLP) to understand user queries and provide appropriate responses. It features dynamic response capabilities for date and time inquiries, a text-to-speech option for auditory feedback, and a user-friendly graphical interface for interactions.

## Features
- Natural Language Processing for understanding user intents.
- Dynamic responses for date and time-related queries.
- Text-to-Speech functionality for auditory feedback.
- Graphical User Interface for easy interaction with the chatbot.

## Getting Started

### Prerequisites
Ensure you have Python 3.6 or newer installed on your system. The application depends on several third-party libraries, including:
- NLTK for natural language processing.
- gTTS (Google Text-to-Speech) for text-to-speech functionality.
- Pygame for playing audio responses.
- Additional libraries for date, time, and regular expression support.

### 1. Install Required Libraries
pip install nltk gtts pygame datetime re

### 2. Download NLTK Data
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('wordnet')

### 3. Running the Application
python App.py

## Usage
The application window will open upon running App.py.
Use the text input field to enter your queries and press Enter or click the "Send" button.
To enable or disable text-to-speech, type "TTS ON" or "TTS OFF" in the chat window.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
