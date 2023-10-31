import speech_recognition as sr
import pyttsx3
import subprocess

# This class is responsible for listening for and executing voice commands.
class SpeechRecognition:

    # The constructor initializes the recognizer, microphone, and engine objects.
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()

    # This function listens for a voice command and returns the recognized text.
    def listen(self):
        with self.microphone as source:
            # Adjust the recognizer for the ambient noise level.
            self.recognizer.adjust_for_ambient_noise(source)
            # Listen for a voice command.
            audio = self.recognizer.listen(source)

        try:
            # Recognize the voice command using Google's speech recognition API.
            text = self.recognizer.recognize_google(audio)
            # Return the recognized text.
            return text
        except sr.UnknownValueError:
            # If the recognizer is unable to understand the voice command, return None.
            return None

    # This function executes the specified voice command.
    def execute_command(self, text):
        # TODO: Add more voice commands here
        # Open Firefox.
        if text == "open firefox":
            subprocess.run(["firefox"])
        # Open Chrome.
        elif text == "open chrome":
            subprocess.run(["chromium"])
        # Open Visual Studio Code.
        elif text == "open vscode":
            subprocess.run(["code"])
        # Open the terminal.
        elif text == "open terminal":
            subprocess.run(["gnome-terminal"])
        # If the command is not recognized, say so.
        else:
            self.engine.say("I don't understand that command.")
            self.engine.runAndWait()

    # This function starts the speech recognition loop.
    def start(self):
        while True:
            # Listen for a voice command.
            text = self.listen()
            # If the command is not None, execute it.
            if text is not None:
                self.execute_command(text)


# Start the speech recognition loop.
if __name__ == "__main__":
    speech_recognition = SpeechRecognition()
    speech_recognition.start()