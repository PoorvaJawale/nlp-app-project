## NLP App using Google Gemini API

This is a simple NLP appliaction built in Python using object-oriented (OOP) concepts. The app interacts with the Google Gemini API to perform various natural language processing tasks such as sentiment analysis, language translation, and language detection.

## Features
 -user registration and login systems (simple in-memory database) <br>
 -sentiment analysis of input sentences <br>
 -language translation (English to Hindi) <br>
 -language detection of input text <br>
 -menu-driven interface for easy interaction <br>

## Technologies used
-python 3.12.4 <br>
-google Generative AI API (Gemini model) <br>

## Setup instructions

1. Clone the repository <br>
   ```bash
   git clone https://github.com/your-username/nlp-app-project.git
   cd nlp-app-project 
   
2. Install dependencies <br>

  Make sure you have the google.generativeai package installed: <br>
``
  pip install google-generativeai ``

3. Google API key <br>
   -replace the GOOGLE_API_KEY in the code with your own Google Generative AI API key. <br>
   -you can get an API key by signing up on the Google Cloud Console and enabling the Generative AI API. <br>

4. Run the app <br>
   ```bash
   python your_script_name.py

## Usage
-when you run the script, you will be greeted with a menu to either register or login. <br>
-after successful login, you can choose between sentiment analysis, language translation, or language detection. <br>
-follow the prompts to enter the text and get the output from the Gemini model. <br>

## Notes
-this app uses a simple dictionary to simulate a user database, which means data is not persistent and will reset every time you restart the app. <br>
-for production use, integrate with a real database and secure the API key properly. <br>
-the current implementation uses synchronous calls to the Gemini model, so expect some delay depending on API response time. <br>

## Contact
For questions or feedback, please open an issue or contact me at poorvakjawale@gmail.com
