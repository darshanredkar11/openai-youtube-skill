# OpenAI YouTube Business Operator

A lean, evidence-led skill for researching and operating a YouTube channel as a business. It combines a practical GPT/Codex workflow with six reusable, dependency-free Python utilities.

**Goal:** choose a commercially sensible niche, find a differentiated audience promise, produce useful videos consistently, and learn from real analytics — without building another SaaS platform.

## What is included

- `SKILL.md` — the end-to-end operating playbook.
- `references/research-and-scoring.md` — niche validation rubric and evidence standards.
- `templates/` — niche scorecard, video brief, creator voice profile and experiment log.
- `scripts/` — hook scoring, title/thumbnail linting, channel-relative outlier analysis, retention diagnostics, dead-air EDL and chapter drafts.
- `THIRD_PARTY_NOTICES.md` — attribution and upstream licence information.

## Install (Codex)

Clone this repository, then copy the skill into your Codex skills directory:

```bash
git clone https://github.com/darshanredkar11/openai-youtube-skill.git
mkdir -p ~/.codex/skills/youtube-business-operator
cp -R openai-youtube-skill/SKILL.md openai-youtube-skill/scripts \
  openai-youtube-skill/references openai-youtube-skill/templates \
  ~/.codex/skills/youtube-business-operator/
```

Start a new Codex session and ask it to validate a niche, audit a channel, plan a video or diagnose retention. The skill can also be used as a repository-level instruction reference by an OpenAI-compatible agent that supports `SKILL.md`.

## Run the utilities

Python 3 standard library only; no pip packages are required.

```bash
python3 scripts/yt-script/hookscore.py --hook "Your candidate opening line"
python3 scripts/yt-package/title.py --title "A specific video title" --thumb "THE RESULT"
python3 scripts/yt-viral/swipe.py samples.json --min 2.0 --json
python3 scripts/yt-retention/retention.py retention.csv --duration 600 --json
python3 scripts/yt-edit/deadair.py transcript.srt --json
python3 scripts/yt-chapters/chapters.py transcript.srt --target 7 --json
```

For `swipe.py`, provide at least four videos per channel for a meaningful within-channel median. Input format:

```json
[
  {"channel":"Example Channel","title":"Video title","views":412000,"url":"https://youtube.com/watch?v=example","duration":613}
]
```

## Principles

- Research current evidence; don't invent metrics or revenue.
- Use public competitor information; don't access private accounts.
- Compare videos to their own channel baseline, not just raw views.
- Treat scoring scripts as diagnostic heuristics, not predictions.
- Build original, useful content; do not copy scripts or footage.
- Keep publishing, purchases and external outreach behind explicit human approval.

## Licence

Original playbook, templates and documentation are MIT licensed. Reused code from Jake Schincariol's `chatgpt-youtube-agent-skill` remains under its upstream MIT licence; see `THIRD_PARTY_NOTICES.md` and `licenses/jakeschincariol-MIT.txt`.
