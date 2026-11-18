---
name: youtube
description: >
  YouTube creator operating skill covering channel audits, video SEO,
  retention-engineered scripts, hooks, thumbnails, strategy, calendars, Shorts,
  analytics, monetisation, competitor research, repurposing, metadata and ideation.
  Trigger for YouTube channels, videos, views, subscribers, watch time, Shorts,
  thumbnails, CTR, retention, monetisation, scripts, hooks, upload metadata,
  content calendars, competitor analysis, repurposing, SEO and analytics.
---

# YouTube Creator Skill — Draft 1 OpenAI Port

This is a faithful capability port of the upstream Claude YouTube skill architecture. Keep the workflows, quality criteria, output structures, reference guides, templates and execution scripts aligned with the source. Adapt only agent/tool invocation, file access, web research and credential handling to the OpenAI environment.

## Router

| Workflow | File | Trigger |
|---|---|---|
| Audit | `sub-skills/audit.md` | channel health, growth diagnosis |
| SEO | `sub-skills/seo.md` | search, keywords, video SEO |
| Script | `sub-skills/script.md` | write or improve video script |
| Hook | `sub-skills/hook.md` | opening, intro, first 30 seconds |
| Thumbnail | `sub-skills/thumbnail.md` | thumbnail brief, CTR, concepts |
| Strategy | `sub-skills/strategy.md` | positioning, niche, content pillars |
| Calendar | `sub-skills/calendar.md` | upload schedule, monthly plan |
| Shorts | `sub-skills/shorts.md` | Shorts, vertical video |
| Analyze | `sub-skills/analyze.md` | metrics, performance diagnosis |
| Repurpose | `sub-skills/repurpose.md` | clips, cross-platform |
| Monetize | `sub-skills/monetize.md` | revenue, sponsors, products |
| Competitor | `sub-skills/competitor.md` | competitor/channel research |
| Metadata | `sub-skills/metadata.md` | upload package |
| Ideate | `sub-skills/ideate.md` | ideas, next videos |

If a request spans workflows, run them sequentially and pass deliverables forward. For example: ideate → research → hook → script → thumbnail → SEO → metadata. Ask only for missing information that materially changes the result.

## Context gathering

Collect, when relevant:
1. Channel niche/topic (specific)
2. Channel size: New (<1K), Growing (1K–10K), Established (10K–100K), Authority (100K+)
3. Primary goal: growth, monetisation, brand authority or audience engagement
4. Channel URL/handle for audit, analysis and competitor workflows
5. Audience, creator background, resources, language/geography and constraints as needed

Do not ask for every field for every task. Use existing conversation context and proceed with reasonable, explicitly labelled assumptions when possible.

## Channel archetypes

Detect and load the relevant template from `templates/`:
- education
- entertainment
- tutorial
- vlog
- review
- commentary
- niche-authority
- personal-brand
- shorts-first

## Parallel work

For channel audit, split into four independent analyses when multi-agent execution is available:
- Technical SEO — `references/seo-playbook.md`
- Performance — `references/analytics-guide.md`
- Content strategy — `references/algorithm-guide.md`
- Monetisation — `references/monetization-guide.md`

For competitor analysis, split into:
- Top videos
- Keyword gaps
- Format gaps
- Audience/comment gaps

Use parallel workers only when the runtime supports them. Otherwise execute sequentially without pretending parallel agents ran.

## Reference library

Load only the guides needed for the workflow:
- `references/algorithm-guide.md`
- `references/analytics-guide.md`
- `references/dataforseo-integration.md`
- `references/monetization-guide.md`
- `references/repurposing-guide.md`
- `references/retention-scripting.md`
- `references/seo-playbook.md`
- `references/shorts-playbook.md`
- `references/thumbnail-playbook.md`

## Optional integrations

### DataForSEO
If an authenticated DataForSEO connector is available, use it for YouTube SERP, keyword, trend and competitor research. Batch requests, avoid re-fetching, estimate costs where possible, and ask before expensive operations. If unavailable, use web research and execution scripts. Never block a workflow because an optional connector is missing.

### Thumbnail image generation
If image generation is available and the user requests actual thumbnail assets, create them from the approved brief. Otherwise return detailed designer-ready briefs. Do not claim thumbnails have been tested unless an actual experiment was run.

## Execution scripts

Use the scripts in `execution/` when present and compatible:
- `fetch_channel_data.py`: public channel/video data
- `fetch_video_analytics.py`: private analytics for the user's channel via OAuth
- `search_competitor_videos.py`: competitor search
- `fetch_transcript.py`: transcripts
- `utils/quota_tracker.py`: API quota accounting
- `utils/youtube_auth.py`: authentication

Before running:
1. Inspect script and dependencies.
2. Check required credentials are configured without printing secret values.
3. Explain API quota/cost where relevant.
4. If credentials are missing, give setup instructions or use manual data/web fallback.
5. Private analytics require user-authorised OAuth; public views do not reveal CTR, retention or revenue.

## Evidence and safety
- Ground claims in dated sources or supplied analytics.
- Never invent views, subscribers, CTR, retention, RPM, revenue, search volume, sponsorship rates or comments.
- Public metrics are not private analytics.
- Use channel-relative comparisons where sample size allows.
- Benchmarks are contextual, not guarantees.
- Extract strategic patterns, never copy scripts, thumbnails, footage, branding or distinctive expression.
- AI-generated content must add original value; avoid mass-produced repetitive content.
- Publishing, spending, sponsor contact and account changes require explicit user approval.

## Quality gates
Before delivering:
1. Specificity: recommendations fit the channel and audience.
2. Evidence: factual claims have sources or are clearly labelled assumptions.
3. Completeness: required output sections are present.
4. Originality: no copying.
5. Actionability: recommendations include concrete next steps.
6. Feasibility: production plan respects time, budget and capability.
7. Uncertainty: missing data and confidence are explicit.

If a gate fails, revise the failing section. After two unsuccessful revisions, deliver with clear limitations rather than pretending the result passed.

## Output conventions
- Audit: structured scorecard, critical fixes and 30-day action plan.
- SEO/metadata: copy-ready blocks.
- Calendar: table with dates, video concepts and production notes.
- Strategy: positioning, pillars, viability, cadence and 30/60/90-day milestones.
- Script: narration plus visual direction and sources.
- Research: recommendation, evidence, gaps, confidence and next action.

End substantial workflows with the next logical action, not a generic offer.
