"""ESTATE REPORT -- the text-input capture layer (Andrew ruling 7 + 7a; sovereign mandate).

Andrew ruling 7, VERBATIM: "every single text of user input from me into a terminal session needs to
be tracked somewhere on a day by day basis."
Andrew ruling 7a, VERBATIM: "also we need to figure out how to track all my text inputs and have that
saved somewhere."

*** THIS RUNS DEVICE-SIDE, NOT ON THE EC2 RUNNER, AND THAT IS FORCED -- NOT A PREFERENCE. ***
The transcripts live at ~/.claude/projects/ on each physical device. They are NOT in the repo and NOT
in S3. The estate-report EC2 runner clones the repo, so it STRUCTURALLY CANNOT SEE THEM. Any design
that puts capture on the runner captures nothing and produces a perfectly well-formed empty store --
the exact "looks complete, is empty" failure this whole pipeline exists to refuse.
So: this tool runs on the DEVICE, uploads to S3; the runner READS the uploaded store.
It is also why site-Z is a DECLARED GAP rather than an oversight: a second device needs this tool
running on it, and until it does, "every single text" is device-scoped and every day's manifest must
say so.

WHAT IT EXTRACTS, and the measured reason the obvious version is wrong:
Harness transcripts store turn-boundary input as `type: user`, but MID-TURN input as
`queue-operation` + `attachment` -- NEVER as `user`. Measured against ground truth on session
339beee1: Andrew sent 5 messages; 3 were mid-turn. A naive `type == "user"` extractor captures 40%
AND admits skill bodies, system reminders, task notifications and tool_results as if he had typed
them -- false negatives and false positives at once. The 3 it drops were the highest-signal messages
in that session (two architecture rulings and a standing hold).

FAIL-CLOSED PROVENANCE, one layer below ruling 6's: HUMAN / HARNESS / UNCLASSIFIED. Anything not
positively identifiable as human-typed is NEVER stored as Andrew's words. A missed nugget is absent;
a forged one is believed.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import socket
import sys
from datetime import datetime, timezone

# Markers that prove a payload is harness-generated rather than typed by a human. Substring match:
# these strings do not occur in ordinary prose, and over-matching costs a dropped message (visible,
# recoverable) while under-matching costs a FORGED QUOTE (invisible, believed).
HARNESS_MARKERS = (
    "<system-reminder>",
    "SYSTEM NOTIFICATION",
    "<task-notification>",
    "<command-name>",
    "<command-message>",
    "<local-command-stdout>",
    "Base directory for this skill:",
    "Launching skill:",
    "[Request interrupted",
    "<user-prompt-submit-hook>",
)

# A skill body is delivered wearing the user role. It is long, structured, and NOT Andrew.
SKILL_BODY_RE = re.compile(r"^#\s+\S+.*\n.*\*\*(Refreshed|Base directory)", re.S)


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def device_id() -> str:
    """Stable device label. Goes in the S3 key so a partial day is visibly partial."""
    return os.environ.get("ESTATE_DEVICE_ID") or socket.gethostname() or "unknown-device"


# HARNESS DISPLAY PREFIXES: glyphs the harness prepends to mid-turn input for rendering. Andrew did
# not type these. Kept as an explicit, enumerated list rather than a general "strip leading
# punctuation" rule -- a general rule would eventually eat a real character from a real sentence, and
# nobody would notice because the result would still read fine.
DISPLAY_PREFIXES = ("❯ ", "❯", "> ", "› ")


def _strip_display_prefix(text: str) -> str:
    t = text
    for p in DISPLAY_PREFIXES:
        if t.startswith(p):
            return t[len(p):].lstrip()
    return t


def _text_of(msg: object) -> str:
    if isinstance(msg, str):
        return msg
    if isinstance(msg, dict):
        c = msg.get("content")
        if isinstance(c, str):
            return c
        if isinstance(c, list):
            return "\n".join(
                p.get("text", "") for p in c if isinstance(p, dict) and p.get("type") == "text"
            )
    return ""


def _has_tool_result(msg: object) -> bool:
    if isinstance(msg, dict):
        c = msg.get("content")
        if isinstance(c, list):
            return any(isinstance(p, dict) and p.get("type") == "tool_result" for p in c)
    return False


def classify_text(text: str, row: dict) -> tuple[str, str]:
    """HUMAN / HARNESS / UNCLASSIFIED -- fail-closed. Returns (label, why).

    Only HUMAN is ever stored as Andrew's words. UNCLASSIFIED is retained in the store but flagged,
    so a later reader can audit what the filter was unsure about -- silently dropping the ambiguous
    class would hide the filter's own error rate, and an error rate nobody can see is one nobody
    fixes.
    """
    if _has_tool_result(row.get("message")):
        return ("HARNESS", "tool_result payload")
    t = (text or "").strip()
    if not t:
        return ("HARNESS", "empty/non-text")
    for marker in HARNESS_MARKERS:
        if marker in t:
            return ("HARNESS", "harness marker %r" % marker)
    if SKILL_BODY_RE.match(t):
        return ("HARNESS", "skill body shape")
    if t.startswith("<") and t.endswith(">") and len(t) < 200:
        return ("UNCLASSIFIED", "bare tag-like payload")
    return ("HUMAN", "no harness marker; free text")


def extract_session(path: str) -> tuple[list, dict]:
    """Union of user + queue-operation + attachment, de-duplicated, classified.

    THE UNION IS THE WHOLE POINT and it is also why de-dup is REQUIRED rather than hygiene: one
    mid-turn message appears in BOTH queue-operation and attachment, so the union that fixes the 40%
    miss GUARANTEES duplicates. Keying on a row uuid would fail -- the same utterance carries
    different ids across row types -- so the key is content-based.
    """
    rows = []
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:  # noqa: BLE001
                continue

    session_id = ""
    for r in rows:
        if r.get("sessionId"):
            session_id = str(r["sessionId"])
            break
    if not session_id:
        session_id = os.path.splitext(os.path.basename(path))[0]

    seen: dict[str, dict] = {}
    counts = {"rows_scanned": 0, "candidates": 0}
    labels = {"HUMAN": 0, "HARNESS": 0, "UNCLASSIFIED": 0}

    for r in rows:
        if r.get("type") not in ("user", "queue-operation", "attachment"):
            continue
        counts["rows_scanned"] += 1
        # A queue-operation/attachment row nests the payload in varying places; search the row for
        # any message-shaped text rather than assuming one field. Assuming a field shape is exactly
        # the defect that produced the UNRESOLVED bucket earlier in this build.
        texts = []
        m = r.get("message")
        if m is not None:
            texts.append((_text_of(m), r))
        for key in ("prompt", "text", "content", "value"):
            v = r.get(key)
            if isinstance(v, str) and v.strip():
                texts.append((v, r))
            elif isinstance(v, dict):
                tv = _text_of(v)
                if tv.strip():
                    texts.append((tv, r))
        for text, row in texts:
            if not text or not text.strip():
                continue
            counts["candidates"] += 1
            label, why = classify_text(text, row)
            labels[label] += 1
            if label == "HARNESS":
                continue
            # Whitespace-collapse ONLY for the key. NEVER case-fold, NEVER strip punctuation --
            # the stored text is EVIDENCE and must stay byte-faithful to what he typed.
            norm = " ".join(text.split())
            key = hashlib.sha256((session_id + "\x1e" + norm).encode("utf-8")).hexdigest()
            if key in seen:
                seen[key]["row_types"] = sorted(set(seen[key]["row_types"] + [r.get("type")]))
                continue
            seen[key] = {
                "dedup_key": key,
                "session_id": session_id,
                "provenance": label,
                "provenance_why": why,
                "row_types": [r.get("type")],
                "ts": r.get("timestamp") or r.get("ts"),
                # TWO FIELDS ON PURPOSE, and the distinction is load-bearing for quoting.
                # `text` is BYTE-FAITHFUL to the transcript -- it is the evidence, and it is what any
                # dispute resolves against. But the harness prefixes mid-turn input with a display
                # marker ("> ") that ANDREW DID NOT TYPE. Quoting `text` verbatim would attribute a
                # harness glyph to him -- a small forgery, but a forgery, and exactly the class ruling
                # 6's fail-closed provenance exists to refuse.
                # `text_for_quote` is the same string with ONLY known harness display prefixes
                # removed. Nothing else is normalized: no case-folding, no punctuation stripping,
                # no whitespace rewriting beyond the prefix.
                "text": text,
                "text_for_quote": _strip_display_prefix(text),
            }

    out = sorted(seen.values(), key=lambda d: (str(d.get("ts") or ""), d["dedup_key"]))
    meta = {
        "session_id": session_id,
        "source_path": path,
        "rows_scanned": counts["rows_scanned"],
        "candidate_payloads": counts["candidates"],
        "by_label": labels,
        "stored": len(out),
        "captured_at": utcnow(),
        "device": device_id(),
    }
    return out, meta


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="ESTATE REPORT device-side text-input capture")
    ap.add_argument("--project-dir", default=os.path.expanduser(
        "~/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace"))
    ap.add_argument("--session", help="single session id/file to extract (fixture mode)")
    ap.add_argument("--json", action="store_true", help="emit the extracted records as JSON")
    args = ap.parse_args(argv)

    if args.session:
        files = [p for p in glob.glob(os.path.join(args.project_dir, "*.jsonl"))
                 if args.session in os.path.basename(p)]
    else:
        files = glob.glob(os.path.join(args.project_dir, "*.jsonl"))
    if not files:
        print("NO TRANSCRIPTS FOUND under %s -- refusing to report an empty capture as a complete one"
              % args.project_dir, file=sys.stderr)
        return 2

    all_recs, metas = [], []
    for p in files:
        recs, meta = extract_session(p)
        all_recs.extend(recs)
        metas.append(meta)

    if args.json:
        print(json.dumps({"records": all_recs, "meta": metas}, indent=2))
    else:
        tot = {"HUMAN": 0, "HARNESS": 0, "UNCLASSIFIED": 0}
        for m in metas:
            for k in tot:
                tot[k] += m["by_label"][k]
        print("sessions: %d | rows scanned: %d | stored: %d"
              % (len(metas), sum(m["rows_scanned"] for m in metas), len(all_recs)))
        print("labels: %s" % tot)
    return 0


if __name__ == "__main__":
    sys.exit(main())
