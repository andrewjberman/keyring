from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "codex-inbox-monitor.py"


class CodexInboxMonitorTest(unittest.TestCase):
    def run_until(
        self, inbox: Path, events: int, repeat_seconds: float = 15.0
    ) -> subprocess.Popen[str]:
        return subprocess.Popen(
            [
                sys.executable,
                "-u",
                str(SCRIPT),
                "--inbox",
                str(inbox),
                "--poll-seconds",
                "0.01",
                "--repeat-seconds",
                str(repeat_seconds),
                "--max-events",
                str(events),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def test_existing_root_markdown_is_emitted_but_not_consumed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            inbox = Path(raw)
            unread = inbox / "message.md"
            unread.write_text("synthetic", encoding="utf-8")

            proc = self.run_until(inbox, 1)
            stdout, stderr = proc.communicate(timeout=3)

            self.assertEqual(proc.returncode, 0, stderr)
            self.assertEqual(stdout, "[HARD-NUDGE] message.md\n")
            self.assertTrue(unread.is_file())
            self.assertEqual(unread.read_text(encoding="utf-8"), "synthetic")

    def test_only_root_level_markdown_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            inbox = Path(raw)
            (inbox / "read").mkdir()
            (inbox / "read" / "already-read.md").write_text("read", encoding="utf-8")
            (inbox / "ignore.txt").write_text("text", encoding="utf-8")
            target = inbox / "new.MD"
            target.write_text("peer", encoding="utf-8")

            proc = self.run_until(inbox, 1)
            stdout, stderr = proc.communicate(timeout=3)

            self.assertEqual(proc.returncode, 0, stderr)
            self.assertEqual(stdout, "[HARD-NUDGE] new.MD\n")
            self.assertTrue(target.is_file())
            self.assertTrue((inbox / "read" / "already-read.md").is_file())

    def test_unread_markdown_repeats_without_being_consumed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            inbox = Path(raw)
            unread = inbox / "still-unread.md"
            unread.write_text("pending", encoding="utf-8")

            proc = self.run_until(inbox, 2, repeat_seconds=0.03)
            stdout, stderr = proc.communicate(timeout=3)

            self.assertEqual(proc.returncode, 0, stderr)
            self.assertEqual(
                stdout,
                "[HARD-NUDGE] still-unread.md\n"
                "[HARD-NUDGE] still-unread.md\n",
            )
            self.assertTrue(unread.is_file())
            self.assertEqual(unread.read_text(encoding="utf-8"), "pending")


if __name__ == "__main__":
    unittest.main()
