# OpenAI YouTube Skill

An OpenAI-compatible port of **[Claude YouTube by AgriciDaniel](https://github.com/AgriciDaniel/claude-youtube)**, a comprehensive YouTube creator skill. Draft 1 focuses on reproducing the upstream workflows, guides, channel templates, and execution utilities before introducing new capabilities.

## Draft 1 scope

The port contains the same core architecture:

- **14 workflows:** audit, SEO, script, hook, thumbnail, strategy, calendar, Shorts, analytics, repurpose, monetize, competitor, metadata, ideate
- **9 reference guides:** algorithm, analytics, DataForSEO, monetization, repurposing, retention scripting, SEO, Shorts, thumbnails
- **9 channel templates:** education, entertainment, tutorial, vlog, review, commentary, niche authority, personal brand, Shorts-first
- **6 YouTube API execution scripts:** channel data, video analytics, competitor search, transcript retrieval, quota tracking, authentication

The OpenAI adaptation changes tool/runtime assumptions where necessary. It does not intentionally redesign the workflows.

## Repository layout

```
SKILL.md
sub-skills/
  audit.md
  seo.md
  script.md
  hook.md
  thumbnail.md
  strategy.md
  calendar.md
  shorts.md
  analyze.md
  repurpose.md
  monetize.md
  competitor.md
  metadata.md
  ideate.md
references/
  algorithm-guide.md
  analytics-guide.md
  dataforseo-integration.md
  monetization-guide.md
  repurposing-guide.md
  retention-scripting-guide.md
  seo-playbook.md
  shorts-playbook.md
  thumbnail-ctr-guide.md
templates/
  education-channel.md
  entertainment-channel.md
  tutorial-channel.md
  vlog-channel.md
  review-channel.md
  commentary-channel.md
  niche-authority-channel.md
  personal-brand-channel.md
  shorts-first-channel.md
execution/
  fetch_channel_data.py
  fetch_video_analytics.py
  search_competitor_videos.py
  fetch_transcript.py
  utils/
    quota_tracker.py
    youtube_auth.py
scripts/
  # Existing independent creator utilities
```

## Install

### Codex

Clone the repository and install the skill in your Codex skills directory:

```bash
git clone https://github.com/darshanredkar11/openai-youtube-skill.git
mkdir -p ~/.codex/skills/youtube
cp -R openai-youtube-skill/SKILL.md \
  openai-youtube-skill/sub-skills \
  openai-youtube-skill/references \
  openai-youtube-skill/templates \
  openai-youtube-skill/execution \
  ~/.codex/skills/youtube/
```

Restart or open a new Codex session so the skill can be discovered.

### Other OpenAI-compatible skill runtimes

This repository uses the standard `SKILL.md` format. Install the directory into the skill location supported by your agent/runtime and ensure it can read the companion `sub-skills/`, `references/`, `templates/`, and `execution/` directories.

## Use it

Ask naturally; the skill routes requests to the appropriate workflow.

| Workflow | Example |
|---|---|
| Audit | `Audit my YouTube channel: https://youtube.com/@example` |
| SEO | `Create an SEO package for my video about Java virtual threads` |
| Script | `Write a retention-focused script about building an MCP server` |
| Hook | `Give me five hooks for this video` |
| Thumbnail | `Create thumbnail concepts for this topic` |
| Strategy | `Build a 90-day channel strategy for my niche` |
| Calendar | `Plan my content calendar for next month` |
| Shorts | `Turn this topic into a Shorts production package` |
| Analyze | `Analyze these YouTube Studio metrics` |
| Repurpose | `Repurpose this video across platforms` |
| Monetize | `Build a monetization strategy for my channel` |
| Competitor | `Analyze these competing channels` |
| Metadata | `Prepare my complete upload metadata package` |
| Ideate | `Give me ten ranked video ideas for my channel` |

Multi-workflow tasks can chain sequentially—for example, ideation → research → hook → script → thumbnail → SEO → metadata—with prior outputs passed into the next stage.

The skill uses available context and asks for missing information only when it materially affects the task.

## Optional YouTube API configuration

The skill can work with manually supplied channel/video data and public web research. API credentials are optional for automated data collection.

### YouTube Data API v3

1. Create a project in Google Cloud Console.
2. Enable YouTube Data API v3.
3. Create an API key.
4. Configure it as an environment variable:

```bash
export YOUTUBE_API_KEY="your-api-key"
```

Do not commit credentials to Git.

### OAuth for private channel analytics

The analytics script requires OAuth authorization for the channel/account whose private analytics are being accessed. Follow the script's setup instructions and grant only the required permissions. Public channel data cannot reveal private CTR, retention, revenue or traffic-source analytics.

## Optional research integrations

### DataForSEO

When an authenticated DataForSEO MCP integration is available, workflows can use YouTube SERP, keyword, trend and competitor research. The skill should batch requests, avoid redundant calls, disclose estimated costs where possible and fall back to web research when the integration is unavailable.

See `references/dataforseo-integration.md`.

### Thumbnail generation

When image generation is available and the user requests actual image assets, the thumbnail workflow can use an image-generation tool. Otherwise it produces designer-ready briefs and variants. It does not claim A/B test results unless a real experiment was run.

## Python execution utilities

The execution scripts use Python. Inspect each script's help and requirements before use.

```bash
python3 execution/fetch_channel_data.py --help
python3 execution/fetch_video_analytics.py --help
python3 execution/search_competitor_videos.py --help
python3 execution/fetch_transcript.py --help
```

The quota tracker and authentication utilities are shared support modules under `execution/utils/`.

The repository also contains independent utilities under `scripts/` for hook scoring, title/thumbnail checks, channel-relative video outlier analysis, retention diagnostics, dead-air editing and chapter generation. These are separate from the upstream six-script API integration.

## Testing

Run the repository tests:

```bash
python -m unittest discover -s tests -v
```

The GitHub Actions workflow runs the Python test suite across supported Python versions.

Tests check repository structure and utility behavior. They do not substitute for end-to-end validation of every AI workflow, external API integration, OAuth flow or optional MCP connector.

## Evidence and operating principles

- Do not invent channel metrics, search volume, CTR, retention, RPM, revenue or sponsorship rates.
- Distinguish public data from private analytics.
- Use dated sources for changing platform guidance.
- Treat benchmarks as contextual indicators—not guarantees.
- Analyze competitor patterns; do not copy scripts, thumbnails, footage or distinctive branding.
- Publishing, spending, sponsor outreach and account changes require explicit approval.
- Mark assumptions, data gaps and confidence.

## Upstream and licensing

This project ports the workflow instructions, references, templates and execution scripts from [AgriciDaniel/claude-youtube](https://github.com/AgriciDaniel/claude-youtube), which is MIT licensed. Upstream attribution and license are preserved in `THIRD_PARTY_NOTICES.md` and `licenses/agricidaniel-MIT.txt`.

The existing creator utilities adapted from [Jakeschincariol/chatgpt-youtube-agent-skill](https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill) retain their separate MIT attribution and license.

## Draft status

**Draft 1 — Faithful port.** The priority is capability parity and functional validation. Improvements, new workflows, architectural changes and additional integrations belong in a subsequent draft after this baseline is tested.

## License

See `LICENSE` and `THIRD_PARTY_NOTICES.md` for project and upstream licensing details.
