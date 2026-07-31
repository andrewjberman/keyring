#!/usr/bin/env python3
"""FIXTURE 1 for .tools/estate-capture.py -- a REGRESSION detector, not a smoke test.

WHY THIS EXISTS (the defect it replaces):
    Fixture 1 was previously a manual run against a LIVE transcript path. It recorded
    "467 rows / 8 stored"; the same command reads 498/10 today -- because the file kept
    being appended after the measuring window closed. A FIXTURE PINNED TO A LIVE PATH
    CANNOT DETECT A REGRESSION: a changed count is indistinguishable from a grown corpus,
    so the only two outcomes are "matches" (luck) and "differs" (uninformative).
    Found by 0.7.0_AE_CloudOps~B; fix approved by 3.0.0_SA_CVO 20260731T135324Z.

THE THREE PROPERTIES THAT MAKE IT A DETECTOR:
    1. THE CORPUS IS PINNED BY SHA256, not by path. If the bytes are not the bytes that
       were verified, this REFUSES TO RUN rather than reporting against a different corpus.
       A count assertion over an unpinned corpus is what failed before.
    2. ASSERTIONS ARE ENUMERATED BY dedup_key, NEVER BY COUNT. "10 stored" passes while
       storing ten wrong things. Each expected utterance is named and checked individually,
       and the report says WHICH one went missing -- a count can only say "not 10".
    3. THE DENOMINATOR AND THE SHA ARE PRINTED IN THE OUTPUT ITSELF, so a reader sees what
       it ran against instead of trusting the number.

PROVENANCE OF THE EXPECTED SET -- read this before editing the list:
    The ten dedup_keys below were verified by `0.7.0_AE_CloudOps~B` on 2026-07-31, for BOTH
    precision (all 10 stored records read in full; all human-typed; zero harness leakage) AND
    recall (every user/queue-operation/attachment row re-classified straight from the JSONL;
    the 4 distinct non-empty dropped payloads enumerated and all 4 confirmed harness --
    3 `<task-notification>`, 1 `Base directory for this skill:`). No Andrew utterance dropped.

    ~B established this FRESH rather than inheriting it, and the reason is load-bearing:
    the predecessor ~B session (339beee1) hand-verified 7 utterances, but a LATER ~B session
    is a different witness. PROVENANCE ATTACHES TO A SESSION, NOT TO A SERIAL -- a log
    inherits the claim without inheriting the evidence. Re-reading the stored list would have
    been a copy wearing a verification's clothes, perfectly correlated with what it checks.
    That is also why 0.7.0_AE_CloudOps~A (who wired this) did NOT re-derive the list: the
    executor of the mechanics must not be the source of the ground truth.

    THEREFORE: do not "refresh" this list by re-running the extractor and pasting its output.
    That would make the fixture assert whatever the code currently does -- a test that can
    never fail. A change here needs a fresh human verification, attributed and dated.

NOTE ON KEY #7: it is Andrew's RULING 8 verbatim -- the day-first layout instruction the whole
    storage contract derives from. If this fixture ever stops asserting that key, the pipeline
    has lost the ruling that defines it.

CORPUS LOCATION -- and an OPEN question this file does not decide:
    The pinned corpus is a frozen copy under `.runtmp/` (gitignored), NOT committed.
    *** THIS IS RATIFIED, NOT AN OPEN DEVIATION. DO NOT "TIDY" IT INTO THE REPO. ***
    It began as a deviation NARROWER than CVO's "byte-pinned repo copy" and CVO RATIFIED it at
    20260731T142338Z, explicitly superseding their own instruction: the sha pin gives the
    integrity that instruction wanted without the residence it wrongly specified.
    The reason: the transcript is 3.7 MB of Andrew's verbatim words, and the RETENTION RULING
    covering his own words is an OPEN item at Andrew (0.7.0_AE_CloudOps~B log 2026-07-31,
    blocker 2). Committing it would publish that content to the GitHub remote ahead of the
    ruling -- and, as ~B put it, you can move a file INTO a repo later; you cannot unpublish it
    from a remote. A CORPUS_PATH edit is reversible; a push is not.
    WHAT IS COMMITTED HERE IS ONLY: the harness, the sha256 pin, and ten sha256 dedup_keys --
    all irreversible hashes, zero prose.
    THE COST, stated plainly rather than hidden: a fresh clone CANNOT run this fixture, because
    the corpus is local-only. That is the price of not pre-empting the retention ruling, and it
    resolves the moment Andrew rules -- at which point the frozen copy moves in-repo and only
    CORPUS_PATH changes.

ASCII-ONLY OUTPUT: the corpus contains harness display glyphs (e.g. U+276F). Printing record
    text on a cp1252 console raises UnicodeEncodeError -- so this reports KEYS and never echoes
    corpus prose. (CLAUDE.md: no non-ASCII in anything that runs.)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS_PATH = os.path.join(REPO, ".runtmp", "estate-capture-fixtures", "fixture1_339beee1.jsonl")
CAPTURE_TOOL = os.path.join(REPO, ".tools", "estate-capture.py")

# The pin. Verified identical by ~B (live read) and ~A (frozen copy) on 2026-07-31.
PINNED_SHA256 = "44013ceef632dea4d3084662e3b161a112e71392c9be2e14f027301e44ec997a"
PINNED_BYTES = 3706827
SOURCE_SESSION = "339beee1-469a-40df-8f2f-4dfff3d57ddf"

# dedup_key -> short ASCII label. Verified by 0.7.0_AE_CloudOps~B, 2026-07-31. See docstring.
EXPECTED: dict[str, str] = {
    "a829f4716ae365ce4ef5434045603d76f87179ba0a7ea3521dda8e119f44332d": "01 lane-B launcher paste",
    "570e83a715577a695916835728b03cc254f211fe9da329d6eba356b6c11ee2fd": "02 follow startup, await instruction",
    "707e38e7bf1236325cc02bf9172bed87481aa8742bba5a6181c4ef8c575f2096": "03 EC2 autostart idea",
    "cb7f682e1c954de6414902aaa54817c68bed73bb15d0e63dee28fd86a4b3097b": "04 >900s long-run case",
    "69da8ee6aed53ed9c99d4fa4c91b266c9afa4bc32c31642a7c99e985d202491c": "05 build the attribution bridge",
    "f04cea9a5e19643068c26e090d2441444e12510bae97142829129800b872fc02": "06 same bucket where kimi tracks",
    "8e9a9e03e7fde7c21351cb90e3a7b5e8034f187e9e4a93ea7d3086a27d091d7b": "07 RULING 8 -- day-first subfolders",
    "ee3d6af72c4abc3c1df7514360c3c696b0e3b61005e719b82e91523a9cdbd00a": "08 keep going, work is important",
    "34c28bc668a0790a82837a806fd3de83888bf5d8397eacd94e1a9e7faf03b4f6": "09 andrew deliverable reference",
    "802fa5502746e4184b88b8bd04dde0c992a9e2f73f6d98a2db0370229dcad303": "10 ok /log",
}


def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="estate-capture fixture 1 (sha-pinned, key-enumerated)")
    ap.add_argument("--corpus", default=CORPUS_PATH)
    args = ap.parse_args(argv)

    print("=== FIXTURE 1 -- estate-capture.py regression detector ===")
    print("  source session : %s" % SOURCE_SESSION)
    print("  corpus path    : %s" % args.corpus)

    if not os.path.exists(args.corpus):
        print("  RESULT: CANNOT RUN -- corpus absent at the path above.")
        print("  This is NOT a pass and NOT a failure of the capture tool. The corpus is a")
        print("  local-only frozen copy (see module docstring: retention ruling pending).")
        print("  Re-freeze it from the source session transcript, then re-run.")
        return 3

    actual_bytes = os.path.getsize(args.corpus)
    actual_sha = sha256_of(args.corpus)
    print("  bytes          : %d (pinned %d)" % (actual_bytes, PINNED_BYTES))
    print("  sha256         : %s" % actual_sha)
    print("  pinned sha256  : %s" % PINNED_SHA256)

    if actual_sha != PINNED_SHA256:
        print("")
        print("  RESULT: REFUSING TO RUN -- CORPUS SHA MISMATCH.")
        print("  The bytes are not the bytes that were verified. Any verdict from here would")
        print("  describe a DIFFERENT corpus, which is precisely the defect this fixture exists")
        print("  to close -- a changed count over an unpinned corpus cannot distinguish a")
        print("  regression from a grown file. Do NOT re-pin to make this pass: re-pinning")
        print("  silently adopts whatever the corpus became. Establish what changed first.")
        return 2

    print("  corpus PINNED and INTACT.")
    print("")

    proc = subprocess.run(
        [sys.executable, CAPTURE_TOOL,
         "--project-dir", os.path.dirname(args.corpus),
         "--session", os.path.splitext(os.path.basename(args.corpus))[0],
         "--json"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if proc.returncode != 0:
        print("  RESULT: CAPTURE TOOL FAILED rc=%d" % proc.returncode)
        print((proc.stderr or "")[:2000])
        return 1

    payload = json.loads(proc.stdout)
    records = payload.get("records", [])
    metas = payload.get("meta", []) or []
    scanned = sum(int(m.get("scanned") or m.get("rows_scanned") or 0) for m in metas) if metas else -1

    got = {r["dedup_key"] for r in records}

    print("  DENOMINATOR: rows scanned %s | records stored %d | expected keys %d"
          % (scanned if scanned >= 0 else "n/a", len(records), len(EXPECTED)))
    print("")
    print("  PER-KEY (enumerated -- a count cannot say WHICH one went missing):")
    missing = []
    for key, label in EXPECTED.items():
        present = key in got
        print("    [%s] %s  %s" % ("OK " if present else "MISS", key[:16], label))
        if not present:
            missing.append((key, label))

    extra = sorted(got - set(EXPECTED))
    if extra:
        print("")
        print("  EXTRA keys stored but NOT in the verified set (%d):" % len(extra))
        for key in extra:
            print("    [NEW ] %s" % key[:16])
        print("    An extra is NOT automatically a defect -- it may be a real utterance the")
        print("    verified set predates. It needs a fresh human verification before being")
        print("    added, never an auto-refresh of the expected list.")

    print("")
    print("  WHAT THIS FIXTURE DOES **NOT** COVER -- read before treating a PASS as assurance:")
    print("    This is ONE SESSION (%s). A green result here is evidence about" % SOURCE_SESSION[:8])
    print("    THIS SAMPLE, never about the corpus. It detects a REGRESSION in the ten utterances")
    print("    named above; it is structurally blind to any defect class ABSENT from this session.")
    print("    MEASURED INSTANCE, not a hypothetical: 213 forged quotes (130 local-command-caveat")
    print("    preambles, 83 compaction preambles, 2 missed skill bodies = 5.9% of a 3,628-record")
    print("    corpus) sat misclassified as human speech THE ENTIRE TIME fixture 1 was passing --")
    print("    because session %s contained none of those classes. The fixture was" % SOURCE_SESSION[:8])
    print("    green and the corpus was wrong, simultaneously, and neither fact disproved the other.")
    print("    CORPUS-WIDE precision/recall is a SEPARATE measurement over all sessions. Do not")
    print("    substitute this PASS for it. (Class found + fixed by 0.7.0_AE_CloudOps~B, 2026-07-31.)")
    print("")
    if missing:
        print("  RESULT: FAIL -- %d of %d verified utterances NOT captured." % (len(missing), len(EXPECTED)))
        for key, label in missing:
            print("    MISSING %s (%s)" % (label, key[:16]))
        return 1
    if extra:
        print("  RESULT: PASS WITH EXTRAS -- all %d verified utterances captured; %d unverified extra(s)."
              % (len(EXPECTED), len(extra)))
        return 0
    print("  RESULT: PASS -- all %d verified utterances captured, no extras." % len(EXPECTED))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
