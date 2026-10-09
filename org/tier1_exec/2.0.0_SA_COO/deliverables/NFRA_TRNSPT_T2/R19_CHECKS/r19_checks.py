"""NFRA_TRNSPT round 19 -- the issuer's mechanical checks (2.0.0_SA_COO~T2). Each check: the named tests exist and the file is green.

  s8   TR19-s8-AC1   read_meeting.py and research_read.py share ONE holdout filter; a held-out row is never printed
  w7   TR19-w7-AC1   the Teams silver re-wipe tool (dry-run names every key, the mail wipe rule) + wipe-on-landing with a planted-token test
  e4   TR19-e4-AC1   a listing snapshot is stored per pull, and completeness reaches the "expired" cause from it
  i6   TR19-i6-AC1   a market-update deck lands byte-exact with its sha256, and a re-saved copy is recognised as the same deck
  q9   TR19-q9-AC1   one read-only question returns securities mentioned across meetings, mail updates and commentary drafts

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

T = "data/transcripts/scripts/tests/"
SPEC = {
    "s8": (T + "test_holdout_filter_shared.py",
           ["test_both_readers_use_one_filter", "test_held_out_row_never_printed", "test_research_read_unchanged"]),
    "w7": (T + "test_rewipe_teams_silver.py",
           ["test_dry_run_lists_every_key", "test_rewipe_uses_mail_wipe_rule", "test_wipe_on_landing_planted_token"]),
    "e4": (T + "test_listing_snapshot_expired.py",
           ["test_snapshot_written_per_pull", "test_expired_cause_reached", "test_never_recorded_still_distinct"]),
    "i6": (T + "test_market_update_intake.py",
           ["test_lands_byte_exact_with_sha256", "test_resaved_copy_recognised", "test_different_deck_not_matched"]),
    "q9": (T + "test_securities_across_sources.py",
           ["test_one_answer_three_sources", "test_counts_only_no_content", "test_quarter_bounds"]),
}


def run(key):
    path, names = SPEC[key]
    test = Path(path)
    if not test.exists():
        return False, "absent: %s" % test.as_posix()
    text = test.read_text(encoding="utf-8")
    missing = [n for n in names if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(test), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= len(names)), tail


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in SPEC:
        print("usage: r19_checks.py {%s}" % "|".join(SPEC))
        sys.exit(2)
    ok, why = run(sys.argv[1])
    print("R19-%s-%s %s" % (sys.argv[1].upper(), "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
