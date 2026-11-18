import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PY = sys.executable

def run_script(path, *args):
    return subprocess.run([PY, str(ROOT / path), *args], cwd=ROOT,
                          text=True, capture_output=True, check=False)

class SmokeTests(unittest.TestCase):
    def test_hookscore_json(self):
        r = run_script("scripts/yt-script/hookscore.py", "--hook",
                       "You could lose $500 if you ignore this warning", "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)
        self.assertEqual(len(data), 1)
        self.assertIn("verdict", data[0])
        self.assertIn("properties", data[0])

    def test_title_json(self):
        r = run_script("scripts/yt-package/title.py", "--title",
                       "How I saved $500 in 30 days", "--thumb", "THE COST", "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)
        self.assertEqual(len(data), 1)
        self.assertIn("score", data[0])
        self.assertIn("issues", data[0])

    def test_swipe_json_and_thin_channel(self):
        payload = [
            {"channel":"Alpha","title":f"Video {i}","views":v,"url":"https://example.com"}
            for i,v in enumerate([100,100,100,400],1)
        ] + [{"channel":"Small","title":"One","views":10}]
        with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8") as f:
            json.dump(payload, f); f.flush()
            r = run_script("scripts/yt-viral/swipe.py", f.name, "--min", "1", "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)
        self.assertEqual(len(data["outliers"]), 1)
        self.assertEqual(data["outliers"][0]["multiple"], 4.0)
        self.assertEqual(data["skipped_thin_channels"], [["Small", 1]])

    def test_retention_csv(self):
        rows = "position,retention\n" + "\n".join(f"{i*10},{100-i*5}" for i in range(10))
        with tempfile.NamedTemporaryFile("w", suffix=".csv", encoding="utf-8") as f:
            f.write(rows); f.flush()
            r = run_script("scripts/yt-retention/retention.py", f.name, "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)
        self.assertEqual(data["points"], 10)
        self.assertIn("hook_leak", data)

    def test_deadair_whisper_json_array(self):
        cues = [{"start":0,"end":1,"text":"Hello there"},
                {"start":2,"end":2.2,"text":"um"},
                {"start":3,"end":4,"text":"Hello there"}]
        with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8") as f:
            json.dump(cues, f); f.flush()
            r = run_script("scripts/yt-edit/deadair.py", f.name, "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)
        self.assertGreaterEqual(len(data["cuts"]), 1)
        self.assertEqual(data["duration"], 4)

    def test_chapters_srt(self):
        srt = "\n".join(
            f"{i+1}\n00:00:{i*12:02d},000 --> 00:00:{i*12+10:02d},000\n"
            f"Topic {i} explains a different important concept.\n"
            for i in range(6)
        )
        with tempfile.NamedTemporaryFile("w", suffix=".srt", encoding="utf-8") as f:
            f.write(srt); f.flush()
            r = run_script("scripts/yt-chapters/chapters.py", f.name, "--target", "3", "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)
        self.assertGreaterEqual(len(data["chapters"]), 3)
        self.assertEqual(data["chapters"][0]["start"], 0)

if __name__ == "__main__":
    unittest.main()
