import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

UPSTREAM_WORKFLOWS = [
    "audit", "seo", "script", "hook", "thumbnail", "strategy", "calendar",
    "shorts", "analyze", "repurpose", "monetize", "competitor", "metadata",
    "ideate",
]

UPSTREAM_REFERENCES = [
    "algorithm-guide.md", "analytics-guide.md", "dataforseo-integration.md",
    "monetization-guide.md", "repurposing-guide.md",
    "retention-scripting-guide.md", "seo-playbook.md", "shorts-playbook.md",
    "thumbnail-ctr-guide.md",
]

UPSTREAM_TEMPLATES = [
    "education-channel.md", "entertainment-channel.md", "tutorial-channel.md",
    "vlog-channel.md", "review-channel.md", "commentary-channel.md",
    "niche-authority-channel.md", "personal-brand-channel.md",
    "shorts-first-channel.md",
]

UPSTREAM_EXECUTION = [
    "fetch_channel_data.py", "fetch_video_analytics.py",
    "search_competitor_videos.py", "fetch_transcript.py",
    "utils/quota_tracker.py", "utils/youtube_auth.py",
]

class SkillStructureTests(unittest.TestCase):
    def test_orchestrator_routes_to_upstream_workflows(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for name in UPSTREAM_WORKFLOWS:
            with self.subTest(name=name):
                self.assertTrue((ROOT / "sub-skills" / f"{name}.md").exists())
                self.assertIn(f"sub-skills/{name}.md", skill)

    def test_upstream_reference_guides_exist(self):
        for name in UPSTREAM_REFERENCES:
            with self.subTest(name=name):
                self.assertTrue((ROOT / "references" / name).exists())

    def test_upstream_channel_templates_exist(self):
        for name in UPSTREAM_TEMPLATES:
            with self.subTest(name=name):
                self.assertTrue((ROOT / "templates" / name).exists())

    def test_upstream_execution_scripts_exist(self):
        for name in UPSTREAM_EXECUTION:
            with self.subTest(name=name):
                self.assertTrue((ROOT / "execution" / name).exists())

    def test_modules_are_nonempty(self):
        for path in (ROOT / "sub-skills").glob("*.md"):
            with self.subTest(path=path.name):
                self.assertGreater(len(path.read_text(encoding="utf-8").strip()), 100)

if __name__ == "__main__":
    unittest.main()
