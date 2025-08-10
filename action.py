import datetime
import speak
import webbrowser
import os

# Paths to installed apps
APP_PATHS = {
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "spotify": "spotify",
    "visual studio code": r"C:\Users\srija\AppData\Local\Programs\Microsoft VS Code\Code.exe"
}

# ---------- HELPERS ----------
def open_app(app_name):
    try:
        path = APP_PATHS.get(app_name.lower())
        if path:
            os.startfile(path)
            speak.speak(f"Opening {app_name}")
            return f"Opening {app_name}"
        else:
            speak.speak(f"Sorry, I don't know where {app_name} is installed.")
            return f"Sorry, I don't know where {app_name} is installed."
    except Exception as e:
        speak.speak(f"Failed to open {app_name}")
        return f"Error opening {app_name}: {str(e)}"

# ---------- MAIN ACTION ----------
def Action(send):
    data_btn = send.lower().strip()

    # DATE & TIME
    if data_btn == "time":
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak.speak(f"The current time is {current_time}")
        return current_time

    if data_btn == "date":
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        speak.speak(f"Today's date is {today}")
        return today

    # GOOGLE
    if data_btn.startswith("open google"):
        webbrowser.open("https://www.google.com")
        speak.speak("Google open")
        return "Google open"

    # YOUTUBE
    if data_btn.startswith("open youtube"):
        webbrowser.open("https://www.youtube.com")
        speak.speak("YouTube open")
        return "YouTube open"

    # SPOTIFY
    if data_btn.startswith("open spotify"):
        webbrowser.open("https://open.spotify.com")
        speak.speak("Spotify open")
        return "Spotify open"

    # PLAY
    if data_btn.startswith("play "):
        query = data_btn.replace("play ", "").strip()

        if "on spotify" in query:
            query = query.replace("on spotify", "").strip()
            webbrowser.open(f"https://open.spotify.com/search/{query}")
            speak.speak(f"Playing {query} on Spotify")
            return f"Playing {query} on Spotify"

        if "on youtube" in query:
            query = query.replace("on youtube", "").strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            speak.speak(f"Playing {query} on YouTube")
            return f"Playing {query} on YouTube"

        if "anime" in query:
            anime_name = query.replace("anime", "").strip()
            webbrowser.open(f"https://hianime.to/search?keyword={anime_name}")
            speak.speak(f"Searching {anime_name} on HiAnime")
            return f"Searching {anime_name} on HiAnime"

        # Default play on YouTube
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        speak.speak(f"Playing {query} on YouTube")
        return f"Playing {query} on YouTube"

    # SEARCH
    if data_btn.startswith("search "):
        query = data_btn.replace("search ", "").strip()

        if "on youtube" in query:
            query = query.replace("on youtube", "").strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            speak.speak(f"Searching {query} on YouTube")
            return f"Searching {query} on YouTube"

        if "anime" in query:
            anime_name = query.replace("anime", "").strip()
            webbrowser.open(f"https://hianime.to/search?keyword={anime_name}")
            speak.speak(f"Searching {anime_name} on HiAnime")
            return f"Searching {anime_name} on HiAnime"

        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak.speak(f"Searching {query} on Google")
        return f"Searching {query} on Google"

    # OPEN LOCAL APPS
    if data_btn.startswith("open "):
        app_name = data_btn.replace("open ", "").strip()
        return open_app(app_name)

    # RESPONSES
    if "what is your name" in data_btn:
        speak.speak("my name is zoro")
        return "my name is zoro"
    elif "hello" in data_btn or "hi" in data_btn or "hey" in data_btn:
        speak.speak("Hey How I can help you!")
        return "Hey How I can help you!"
    elif "how are you" in data_btn:
        speak.speak("I am doing great these days")
        return "I am doing great these days"
    elif "thanks" in data_btn or "thank you" in data_btn:
        speak.speak("It's my pleasure to stay with you")
        return "It's my pleasure to stay with you"
    elif "good morning" in data_btn:
        speak.speak("Good morning, I think you might need some help")
        return "Good morning, I think you might need some help"
    elif "shutdown" in data_btn or "quit" in data_btn:
        speak.speak("ok")
        return "ok"
    else:
        speak.speak("I'm not able to understand!")
        return "I'm not able to understand!"
