import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class SkillStructureTests(unittest.TestCase):
    def test_orchestrator_routes_to_all_modules(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        required = [
            "audit", "seo", "script", "hook", "thumbnail", "strategy",
            "calendar", "shorts", "analyze", "repurpose", "monetize",
            "competitor", "metadata", "ideate", "research", "trend",
        ]
        for name in required:
            with self.subTest(name=name):
                self.assertTrue((ROOT / "sub-skills" / f"{name}.md").exists())
                self.assertIn(f"sub-skills/{name}.md", skill)

    def test_reference_guides_exist(self):
        required = [
            "algorithm-and-growth.md", "retention-scripting.md", "seo-playbook.md",
            "thumbnail-playbook.md", "analytics-guide.md", "monetization-guide.md",
            "repurposing-guide.md",
        ]
        for name in required:
            with self.subTest(name=name):
                self.assertTrue((ROOT / "references" / name).exists())

    def test_modules_are_nonempty(self):
        for path in (ROOT / "sub-skills").glob("*.md"):
            with self.subTest(path=path.name):
                self.assertGreater(len(path.read_text(encoding="utf-8").strip()), 100)

if __name__ == "__main__":
    unittest.main()
