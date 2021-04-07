import speech_recognition as sr
import webbrowser as web


def main():
    path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say website's name...")
        audio = r.listen(source)
        print("Recognizing now...")

        try:
            dest = (r.recognize_google(audio))
            print(f"You have said:\n{dest}")
            web.get(path).open(dest)

        except Exception as e:
            print(f"Error : {str(e)}")

if __name__ == '__main__':
    main()  