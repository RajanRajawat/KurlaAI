**KurlaAI – Mumbai's Tapori Voice Assistant**
KurlaAI is a fun, voice-activated virtual assistant inspired by Mumbai’s street-smart tapori vibes. Built with Python, this AI bot uses speech recognition, text-to-speech, and generative AI to interact like a true Kurla boy – unfiltered, local, and hilarious.

**Features**
-Voice Interaction: Talk to KurlaAI using your microphone
-AI Chat Responses: Uses kluster.ai API (Llama 3.1) for smart but tapori-style answers
-Web Commands:
-Open YouTube, Instagram, Reddit, LinkedIn – opens directly in browser
-Play Music: Say Play Kurla or any configured keyword to play linked songs
-Exit: Say Bye Bantai to stop the bot



**availableCommands:**

"Bantai" : "Launch Command",
"bye bantai" : "Exit Command",
"Play Kurla" : "Will Play Kurla Song on Browser",
"Play Bandra" : "Will Play Bandra Song on Browser",
"Open Instagram" : "Will Open Instagram on Browser",
"Open YouTube" : "Will Open Youtube on Browser",
"Open LinkedIn" : "Will Open LinkedIn on Browser",
"Open Reddit" : "Will Open Reddit on Browser",  
"Work with AI API too" : 'kluster.ai API Used'


**Tech Stack** 
'speech_recognition' – Converts your voice to text
'pyttsx3' – Speaks like a Kurla bhai
'webbrowser' – Opens links
'openai' – Uses KlusterAI’s hosted Llama model
'musiclib' – Local module for song keyword-to-link mapping

**How to Run**
1. Clone the repo
2. Install dependencies:
-pip install speechrecognition pyttsx3 openai
3. Add your own musiclib.py with song keyword mappings
4. Run it:
-python kurla_ai.py

**Note**
-Uses KlusterAI public key. Replace with your own API key if needed.
-Tested on Windows (some parts like pyttsx3 might behave differently on Mac/Linux).
