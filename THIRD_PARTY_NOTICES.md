# Third-party code and attribution

## YouTube agent utilities

The following files are adapted from **Jake Schincariol's**
[`Jakeschincariol/chatgpt-youtube-agent-skill`](https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill):

- `scripts/yt-script/hookscore.py`
- `scripts/yt-script/hooks.json`
- `scripts/yt-package/title.py`
- `scripts/yt-viral/swipe.py`
- `scripts/yt-retention/retention.py`
- `scripts/yt-edit/deadair.py`
- `scripts/yt-chapters/chapters.py`

The upstream project is MIT licensed. Its original MIT licence is preserved in
`licenses/jakeschincariol-MIT.txt`. Python scripts include an attribution
header. `deadair.py` has a small compatibility fix for Whisper JSON files
whose top-level value is an array rather than an object.


## Claude YouTube skill port

The workflow instructions, reference guides, channel templates, and YouTube API execution scripts in this repository are adapted from **AgriciDaniel/claude-youtube** (https://github.com/AgriciDaniel/claude-youtube), licensed under the MIT License. The upstream MIT license is preserved in `licenses/agricidaniel-MIT.txt`. OpenAI-specific adaptations are documented in this repository. The original project and author retain attribution for their upstream material.
