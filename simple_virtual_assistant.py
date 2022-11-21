import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Friday Sir. Please tell me vishal sir how me I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query


# It's our main function(so don't touch it, if you can't know anything).
if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #  In this section program run the query from the web browser.
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open datacamp' in query:
            webbrowser.open("datacamp.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsappweb.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open amazone' in query:
            webbrowser.open("amazone.com")

        elif 'open moviesverse' in query:
            webbrowser.open("moviesverse.com")

        elif 'open wordpress' in query:
            webbrowser.open("wordpress.com")

        elif 'open telegram' in query:
            webbrowser.open("telegram.com")

        elif 'open tailwindcss' in query:
            webbrowser.open("tailwindcss.com")

        elif 'open taliblocks' in query:
            webbrowser.open("taliblocks.com")

        elif 'open font' in query:
            webbrowser.open("font.com")

        elif 'open google duo' in query:
            webbrowser.open("googleduo.com")

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com")

        elif 'open mxplayer' in query:
            webbrowser.open("mxplayer.com")

        elif 'open snapdeal' in query:
            webbrowser.open("snapdeal.com")

        elif 'open datacamp' in query:
            webbrowser.open("datacamp.com")

        elif 'open codechef' in query:
            webbrowser.open("codechef.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # In this section program using the path of the query from the computer.
        elif 'open code' in query:
            codepath = "C:\\Users\\suman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open nodejs' in query:
            nodejspath = "C:\\Program Files\\nodejs\\node.exe"
            os.startfile(nodejspath)

        elif 'open notepad' in query:
            notepadpath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(notepadpath)

        elif 'open google chrome' in query:
            googlechromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(googlechromepath)

        elif 'open word' in query:
            wordpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordpath)

        elif 'open publisher' in query:
            publisherpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\MSPUB.EXE"
            os.startfile(publisherpath)

        # It's a simple calculator, only four operation are work (add, subtract, multiply, and divide).
        elif 'calculate the value' in query:
            def add(x,y):
                return x + y
            def subtract(x,y):
                return x - y
            def multiply(x,y):
                return x * y
            def divide(x,y):
                return x / y

            # Select the any operation for your calculation
            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            while (True):
                mic = input("Whether your microphone is working or not? (yes/no): ")
                print('enter your choice: ')
                speak('enter your choice: ')
                if (mic == "yes"):
                    choice = takeCommand()
                else:
                    choice = input("enter you choice: ")

                if choice in ('1', '2', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))
                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))
                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))
                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))

                    speak("Let's do next calculation? (Yes or no): ")
                    next_calculation = input("Let's do next calculation? (yes/no): ")
                    if next_calculation == "no":
                        break
                    else:
                        print("Invalid syntax")