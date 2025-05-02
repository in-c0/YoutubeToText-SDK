# YT2Text(YouTube-to-Text) SDK

> A minimal client for the hosted YouTube-to-Text transcription API.

[![PyPI version](https://img.shields.io/pypi/v/youtubetotext-sdk)](https://pypi.org/project/youtubetotext-sdk/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Features
- Simple, lightweight wrapper written in Python
- Supports fetching transcripts with language fallbacks  
- Handles HTTP errors and returns JSON responses  

## Installation
```bash
pip install youtubetotext-sdk
```

## Quickstart
```python
from youtubetotext.client import YouTubeToText

client = YouTubeToText(api_key="YOUR_API_KEY")
response = client.transcript("VIDEO_ID", lang="es,fr")
for segment in response["segments"]:
    print(segment["text"])
```

## API Reference
`YouTubeToText.transcript(video_id: str, lang: str = None) -> dict`

- **video_id**: YouTube video identifier (e.g. `4t2714aREe0`)  
- **lang**: Optional comma‑separated ISO language codes (`en`, `ko,ja`, etc.)  
- **Returns**: A dictionary with the following keys:
  - `source` (str): Which backend provided the transcript (`youtube-transcript-api`, `yt-dlp`, `whisper-cpp`)
  - `language` (str): Human‑readable language (e.g. "English")
  - `language_code` (str): ISO code (e.g. `en`)
  - `is_generated` (bool): Whether the transcript was auto‑generated
  - `segments` (List[dict]): List of segment objects:
    - `start` (float): Start time in seconds
    - `duration` (float): Duration in seconds
    - `text` (str): Transcript text

Full API docs at: https://youtubetotext.com/

## Configuration
Set your API key via the `YTT_API_KEY` environment variable:

```bash
export YTT_API_KEY="your_api_key"
```

## Examples
See `examples/python_example.py` and `examples/js_example.js` in this repo.

## Contributing
Bug reports and pull requests are welcome at https://github.com/in-c0/youtubetotext-sdk.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
