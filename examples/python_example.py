from youtubetotext.client import YouTubeToText

def main():
    client = YouTubeToText(api_key="YOUR_API_KEY")
    res = client.transcript("qT6hMn8vFZo", lang="en")
    for seg in res["segments"]:
        print(f"{seg['start']:>6.2f}s – {seg['text']}")

if __name__ == "__main__":
    main()
