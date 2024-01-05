# Speech Translation Application

This Python application provides a simple Graphical User Interface (GUI) for speech translation using Google Translate and text-to-speech conversion.

## Features

- Allows users to select input and output languages for translation.
- Utilizes speech recognition to initiate translation by recognizing the word 'hello'.
- Translates spoken sentences using Google Translate.
- Converts translated text into speech and plays it back.

## Requirements

- Python 3.x
- Required Python libraries: tkinter, googletrans, speech_recognition, gtts

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the necessary Python libraries using pip:
    ```
    pip install googletrans==4.0.0-rc1 SpeechRecognition gtts
    ```
3. Clone or download this repository to your local machine.

## Usage

1. Run the Python script (`code.py`).
2. The GUI window will appear, allowing you to:
    - Select input and output languages.
    - Click on the 'Translate' button to start the translation process.
3. To initiate the translation, say 'hello' when prompted.
4. Speak the sentence you want to translate.
5. The translated text will be displayed in the output text box, and the translated speech will be played back.

## Code Structure

- `code.py`: Contains the main Python script with the GUI and translation functionalities.
- `README.md`: This file, providing information about the application.

## Notes

- This is a basic implementation and may have limitations in recognizing speech accurately in all environments.
- Ensure a stable internet connection for Google Translate functionality.
- The application provides a starting point and can be extended for more features and error handling.

---

Feel free to adjust and expand this README file according to the specific requirements or additional details about the application.
