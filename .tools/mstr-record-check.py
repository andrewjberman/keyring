#!/usr/bin/env python3
"""mstr-record-check.py -- list anything in a fabric manager's day that looks like a project ruling, for a REVIEWER to judge
(NFRA_CTLPLN workstream SEATS, cell CT-s-4; contract C-SEATS clause 3; rule R-WORKFLOW-20).

Andrew's word (2026-10-07): "MSTR whole purpose is not business logic/project reasoning, they are infrastructure
managers". A manager's acts are merges, pulls, pushes, integration, spawn, kill, unstick and the bid; a question of substance
goes to its CTO by a file. This tool LISTS; it grades nothing and refuses nothing: the counts are the finding and the
reviewer grades them. It writes nothing, sends nothing, and needs no switch file.

    python .tools/mstr-record-check.py --serial <manager serial> --since <UTC> [--until <UTC>] [--repo <dir>] [--mcp-dir <dir>]
    python .tools/mstr-record-check.py --selftest

<UTC> is YYYY-MM-DD, YYYY-MM-DDTHH:MM or YYYY-MM-DDTHH:MM:SS with an optional trailing Z; --until defaults to now.
The serial is matched EXACTLY (0.0.0_AB_MSTR is not 0.0.0_AB_MSTR~Z).

LIMB 1, COMMITS. Commits by that author on any branch inside the window (git log --all --author "^<serial> <", anchored).
  A commit touching a path whose lane is a project's specification (prd/), decomposition (decompositions/), task order
  (task-orders/), adjudication (surprise-channel/adjudications/) or remediation (surprise-channel/remediations/) is listed.
  Those are the TREE_* lanes of .owned-paths.yaml; most are already refused to a manager at commit. A MERGE is exempt from
  lane checks, so for a merge commit a path is listed only when its content at the merge is on NONE of the merge's parents
  (the manager wrote it in the merge itself); a merge that only brings a parent's content is an ordinary manager act.
LIMB 2, MESSAGES. Messages the broker holds as SENT by that serial inside the window: <mcp-dir>/broker.db (opened read-only),
  and <mcp-dir>/message_archive/messages_*.jsonl when the window starts before the database's earliest message. Listed when
  the subject begins RULING, DECISION or ADJUDICATION, or when the subject or first body line carries a project code (a token naming a project row) AND
  opens as an answer (Re / Answer / Yes / No / Ruled / Decided / Approved / Refused / Accepted) AND names none of merge,
  push, pull, spawn, kill, unstick, bid, drain, integrate (a merge notice or a spawn notice is an ordinary manager act).
  If neither the database nor an archive can be read the limb is UNREAD and said so; it is never a zero.
BLIND: a ruling the manager spoke or pasted that is in no file; a message the broker never stored (the cross-device bus holds
only a pointer); a ruling worded without any of the cues above; a message sent as a different serial.

LAST line: MSTR-RECORD serial=<s> window=<h>h commits=<n> ruling_paths=<a> messages=<m> ruling_shaped=<b> unread_limbs=<u> ok=<True|False>
  (ok=True when every limb was read; the counts are the finding.)
--selftest LAST line: MSTR-RECORD-SELFTEST cases=<k>/<n> ok=<True|False>
Exit: 0 done (ok=True), 1 ok=False, 2 usage.
"""
from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import re
import sqlite3
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)

RULING_PATH = re.compile(r"^org/missions/[^/]+/[^/]+/[^/]+/(prd|decompositions|task-orders|surprise-channel/adjudications|"
                         r"surprise-channel/remediations)/")
SUBJECT_RULING = re.compile(r"^[\s\[\(]*(RULING|DECISION|ADJUDICATION)\b", re.I)
PROJECT_CODE = re.compile(r"(?<![A-Za-z0-9_])[A-Z][A-Z0-9]{1,7}_[A-Z][A-Z0-9]{2,11}(?![A-Za-z0-9_])")
ANSWER_CUE = re.compile(r"^[\s\[\(]*(re\b|answer|yes\b|no\b|ruled|decided|approved|refused|accepted|the answer)", re.I)
INFRA_WORD = re.compile(r"\b(merge[sd]?|merging|push(ed)?|pull(ed)?|spawn(ed)?|kill(ed)?|unstick|bid|drain(ed)?|integrate|"
                        r"integration)\b", re.I)


def clean_env() -> dict:
    return {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}


def main_root() -> str:
    """The main worktree: the broker's files are untracked and live only there."""
    try:
        common = subprocess.run(["git", "-C", ROOT, "rev-parse", "--path-format=absolute", "--git-common-dir"],
                                capture_output=True, text=True, check=True, env=clean_env()).stdout.strip()
        return os.path.dirname(common)
    except (OSError, subprocess.SubprocessError):
        return ROOT


def parse_utc(text: str) -> datetime.datetime:
    raw = text.strip()
    if raw.endswith("Z") or raw.endswith("z"):
        raw = raw[:-1]
    when = datetime.datetime.fromisoformat(raw)
    return when.replace(tzinfo=datetime.timezone.utc) if when.tzinfo is None else when.astimezone(datetime.timezone.utc)


def git(repo: str, *args: str) -> str:
    res = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True, encoding="utf-8", errors="replace",
                         timeout=110, env=clean_env())
    if res.returncode != 0:
        raise RuntimeError("git %s: rc=%d %s" % (" ".join(args[:3]), res.returncode, res.stderr.strip()[:200]))
    return res.stdout


# ---------------------------------------------------------------- limb 1: commits

def author_pattern(serial: str) -> str:
    return "^" + re.escape(serial) + " <"


def merge_novel_paths(repo: str, sha: str, parents: list) -> list:
    """Paths the merge changed whose blob at the merge is on none of its parents."""
    changed = set()
    for parent in parents:
        for name in git(repo, "diff-tree", "-r", "--name-only", "--no-commit-id", parent, sha).splitlines():
            if RULING_PATH.match(name):
                changed.add(name)
    if not changed:
        return []
    asks = []
    for name in sorted(changed):
        for rev in [sha] + parents:
            asks.append("%s:%s" % (rev, name))
    res = subprocess.run(["git", "-C", repo, "cat-file", "--batch-check"], input="\n".join(asks) + "\n", capture_output=True,
                         text=True, encoding="utf-8", errors="replace", timeout=110, env=clean_env())
    if res.returncode != 0:
        raise RuntimeError("git cat-file rc=%d %s" % (res.returncode, res.stderr.strip()[:200]))
    out = res.stdout.splitlines()
    if len(out) != len(asks):
        raise RuntimeError("git cat-file answered %d of %d" % (len(out), len(asks)))
    blobs, at = {}, 0
    for name in sorted(changed):
        blobs[name] = out[at:at + 1 + len(parents)]
        at += 1 + len(parents)
    novel = []
    for name in sorted(changed):
        ids = [None if row.endswith(" missing") else row.split()[0] for row in blobs[name]]
        if ids[0] is not None and ids[0] not in ids[1:]:
            novel.append(name)
    return novel


def read_commits(repo: str, serial: str, start: datetime.datetime, end: datetime.datetime) -> tuple:
    """(commits in window, listed rows). Raises RuntimeError when git cannot be read."""
    log = git(repo, "log", "--all", "--author=" + author_pattern(serial), "--format=%H%x09%P%x09%ct%x09%s")
    total, listed = 0, []
    for line in log.splitlines():
        sha, parents, epoch, subject = (line.split("\t", 3) + ["", "", "", ""])[:4]
        if not epoch.isdigit():
            continue
        when = datetime.datetime.fromtimestamp(int(epoch), datetime.timezone.utc)
        if not (start <= when <= end):
            continue
        total += 1
        plist = parents.split()
        if len(plist) > 1:
            for name in merge_novel_paths(repo, sha, plist):
                listed.append((sha[:10], when, subject, name, "MERGE wrote content found on no parent, in a project-lane path"))
            continue
        for name in git(repo, "diff-tree", "-r", "--name-only", "--no-commit-id", "--root", sha).splitlines():
            if RULING_PATH.match(name):
                listed.append((sha[:10], when, subject, name, "commit touches a project specification/decomposition/"
                               "task-order/adjudication/remediation path"))
    return total, listed


# ---------------------------------------------------------------- limb 2: messages

def first_line(body: str) -> str:
    for part in (body or "").splitlines():
        if part.strip():
            return part.strip()[:300]
    return ""


def project_codes(repo: str) -> set:
    """Project codes that name a project row (org/missions/D*/*/<CODE>/project.json) in the repository read."""
    return {os.path.basename(os.path.dirname(p)) for p in
            glob.glob(os.path.join(glob.escape(repo), "org", "missions", "D*", "*", "*", "project.json"))}


def shape_reason(subject: str, body: str, known: set):
    """Why a sent message is ruling-shaped, or None. A token counts as a project code only when it names a project row."""
    if SUBJECT_RULING.match(subject or ""):
        return "subject begins RULING/DECISION/ADJUDICATION"
    head = first_line(body)
    text = (subject or "") + "\n" + head
    codes = [c for c in PROJECT_CODE.findall(text) if c in known]
    if codes and (ANSWER_CUE.match(subject or "") or ANSWER_CUE.match(head)) and not INFRA_WORD.search(text):
        return "answers a question about project code %s and is not a merge/push/spawn/kill/unstick/bid act" % codes[0]
    return None


def to_epoch(text: str):
    try:
        return parse_utc(str(text)).timestamp()
    except ValueError:
        return None


def read_messages(mcp: str, serial: str, start: datetime.datetime, end: datetime.datetime):
    """(rows, earliest_db_epoch) or None when no source could be read. rows: (id, sent_at, to, subject, body)."""
    rows, seen_db, earliest = {}, False, None
    db = os.path.join(mcp, "broker.db")
    if os.path.isfile(db):
        try:
            con = sqlite3.connect("file:" + db.replace("\\", "/") + "?mode=ro", uri=True, timeout=20)
            try:
                earliest = con.execute("select min(sent_at) from messages").fetchone()[0]
                for mid, sent, dest, subject, body in con.execute(
                        "select id, sent_at, to_serial, subject, body from messages where from_serial = ?", (serial,)):
                    ep = to_epoch(sent)
                    if ep is not None and start.timestamp() <= ep <= end.timestamp():
                        rows[mid] = (mid, sent, dest, subject, body)
                seen_db = True
            finally:
                con.close()
        except sqlite3.Error:
            seen_db = False
    if not seen_db:
        return None
    early_ep = to_epoch(earliest) if earliest else None
    if early_ep is None or start.timestamp() < early_ep:
        needle = '"from_serial": "%s"' % serial
        for path in sorted(glob.glob(os.path.join(mcp, "message_archive", "messages_*.jsonl"))):
            try:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    for raw in fh:
                        if needle not in raw:
                            continue
                        try:
                            msg = json.loads(raw)
                        except ValueError:
                            continue
                        ep = to_epoch(msg.get("sent_at", ""))
                        if msg.get("from_serial") == serial and ep is not None and start.timestamp() <= ep <= end.timestamp():
                            rows.setdefault(msg.get("id"), (msg.get("id"), msg.get("sent_at"), msg.get("to_serial", ""),
                                                           msg.get("subject", ""), msg.get("body", "")))
            except OSError:
                continue
    return list(rows.values())


# ---------------------------------------------------------------- the run

def run(serial: str, start: datetime.datetime, end: datetime.datetime, repo: str, mcp: str, out=print) -> dict:
    unread = 0
    commits, listed = 0, []
    try:
        commits, listed = read_commits(repo, serial, start, end)
    except (RuntimeError, OSError, subprocess.SubprocessError) as exc:
        unread += 1
        out("UNREAD limb COMMITS: %s" % exc)
    for sha, when, subject, name, why in listed:
        out("COMMIT %s %s | %s | %s | %s" % (sha, when.strftime("%Y-%m-%dT%H:%MZ"), subject[:70], name, why))
    msgs = read_messages(mcp, serial, start, end)
    sent, shaped = 0, []
    if msgs is None:
        unread += 1
        out("UNREAD limb MESSAGES: no readable broker.db or message_archive under %s. Zero is NOT claimed." % mcp)
    else:
        sent = len(msgs)
        known = project_codes(repo)
        for mid, when, dest, subject, body in sorted(msgs, key=lambda r: str(r[1])):
            why = shape_reason(subject, body, known)
            if why:
                shaped.append(mid)
                out("MESSAGE %s %s to=%s | %s | %s" % (mid, str(when)[:16], dest, (subject or "")[:80], why))
    hours = (end - start).total_seconds() / 3600.0
    line = "MSTR-RECORD serial=%s window=%.4gh commits=%d ruling_paths=%d messages=%d ruling_shaped=%d unread_limbs=%d ok=%s" % (
        serial, hours, commits, len(listed), sent, len(shaped), unread, unread == 0)
    return {"line": line, "listed": listed, "shaped": shaped, "commits": commits, "messages": sent, "unread": unread}


# ---------------------------------------------------------------- the selftest

def _git_fix(repo: str, *args: str, author: str = "", when: str = "2026-10-05T12:00:00+0000") -> str:
    env = clean_env()
    env.update({"GIT_COMMITTER_NAME": "fixture", "GIT_COMMITTER_EMAIL": "fixture@opal.agent", "GIT_COMMITTER_DATE": when,
                "GIT_AUTHOR_DATE": when, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull})
    if author:
        env.update({"GIT_AUTHOR_NAME": author, "GIT_AUTHOR_EMAIL": author + "@opal.agent"})
    res = subprocess.run(["git", "-C", repo, "-c", "commit.gpgsign=false", "-c", "core.autocrlf=false"] + list(args),
                         capture_output=True, text=True, env=env, timeout=60)
    if res.returncode != 0 and "conflict" not in (res.stdout + res.stderr).lower():
        raise RuntimeError("fixture git %s rc=%d %s" % (args[:2], res.returncode, res.stderr.strip()[:200]))
    return res.stdout.strip()


def _write(repo: str, rel: str, text: str) -> None:
    path = os.path.join(repo, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def build_fixture(base: str) -> dict:
    mgr, other = "0.0.0_AB_MSTR", "0.0.0_AB_MSTR~Z"
    repo, mcp = os.path.join(base, "repo"), os.path.join(base, "mcp")
    os.makedirs(repo)
    os.makedirs(mcp)
    decomp = "org/missions/D0/TST/TST_ONE/decompositions/TST_ONE_DECOMP.md"
    to_path = "org/missions/D0/TST/TST_ONE/task-orders/TST_ONE.TO-1.md"
    _git_fix(repo, "init", "-q", "-b", "main")
    _write(repo, "README.md", "base\n")
    _write(repo, "org/missions/D0/TST/TST_ONE/project.json", "{}\n")
    _write(repo, decomp, "line1\nline2\nline3\n")
    _git_fix(repo, "add", "-A")
    _git_fix(repo, "commit", "-q", "-m", "base", author="seed")
    _git_fix(repo, "checkout", "-q", "-b", "worker")
    _write(repo, to_path, "worker order\n")
    _write(repo, decomp, "line1\nworker line2\nline3\n")
    _git_fix(repo, "add", "-A")
    _git_fix(repo, "commit", "-q", "-m", "worker work", author="0.9.0_WK_TST_ONE~1", when="2026-10-05T10:00:00+0000")
    _git_fix(repo, "checkout", "-q", "main")
    # C1: a manager commit to a decomposition, inside the window
    _write(repo, decomp, "line1\nline2\nmanager line3\n")
    _git_fix(repo, "add", "-A")
    _git_fix(repo, "commit", "-q", "-m", "mstr edits the decomposition", author=mgr, when="2026-10-05T11:00:00+0000")
    # C2: a manager commit to an ordinary tool, inside the window
    _write(repo, ".tools/infra.py", "x = 1\n")
    _git_fix(repo, "add", "-A")
    _git_fix(repo, "commit", "-q", "-m", "mstr infra tool", author=mgr, when="2026-10-05T11:30:00+0000")
    # C3: a lane of the manager (a different serial) commits to a decomposition: the exact serial does not match
    _write(repo, decomp, "line1\nline2\nlane line3\n")
    _git_fix(repo, "add", "-A")
    _git_fix(repo, "commit", "-q", "-m", "lane edits", author=other, when="2026-10-05T11:40:00+0000")
    # C4: the manager's MERGE of the worker branch; line2 conflicts, the manager resolves it with NEW content
    _git_fix(repo, "merge", "--no-ff", "-q", "-m", "merge worker", "worker", author=mgr, when="2026-10-05T12:00:00+0000")
    if not os.path.isfile(os.path.join(repo, ".git", "MERGE_HEAD")):
        raise RuntimeError("fixture: the first merge did not stop on its conflict")
    _write(repo, decomp, "line1\nmanager-resolved line2\nlane line3\n")
    _git_fix(repo, "add", "-A")
    _git_fix(repo, "commit", "-q", "--no-edit", "-m", "merge worker (resolved)", author=mgr, when="2026-10-05T12:00:00+0000")
    # C5: a clean merge that only brings a parent's content (a second worker branch adding a new task order)
    _git_fix(repo, "checkout", "-q", "-b", "worker2", "main")
    _write(repo, "org/missions/D0/TST/TST_ONE/task-orders/TST_ONE.TO-2.md", "order two\n")
    _git_fix(repo, "add", "-A")
    _git_fix(repo, "commit", "-q", "-m", "worker2 work", author="0.9.0_WK_TST_ONE~2", when="2026-10-05T13:00:00+0000")
    _git_fix(repo, "checkout", "-q", "main")
    _write(repo, "README.md", "base\nmain moved\n")
    _git_fix(repo, "add", "-A")
    _git_fix(repo, "commit", "-q", "-m", "mstr readme", author=mgr, when="2026-10-05T13:10:00+0000")
    _git_fix(repo, "merge", "--no-ff", "-q", "-m", "merge worker2", "worker2", author=mgr, when="2026-10-05T13:20:00+0000")
    # C6: a manager commit to a decomposition OUTSIDE the window
    _write(repo, decomp, "line1\nline2\nold line3\n")
    _git_fix(repo, "add", "-A")
    _git_fix(repo, "commit", "-q", "-m", "mstr old edit", author=mgr, when="2026-09-01T11:00:00+0000")
    con = sqlite3.connect(os.path.join(mcp, "broker.db"))
    con.execute("create table messages (id integer primary key, from_serial text, to_serial text, subject text, body text, "
                "sent_at text)")
    rows = [
        (1, mgr, "1.0.0_SA_CTO", "RULING on TST_ONE round 2: ship it", "Ruled: the cell passes.", "2026-10-05T12:00:00+00:00"),
        (2, mgr, "1.0.0_SA_CTO", "merged 4 worker branches to CLOUD", "Merged and pushed. Nothing else.", "2026-10-05T12:05:00+00:00"),
        (3, mgr, "2.0.0_SA_COO~C", "spawned 2.0.0_SA_COO~C", "Spawned after the pre-flight read clean.", "2026-10-05T12:10:00+00:00"),
        (4, mgr, "1.0.0_SA_CTO", "Re 77: question", "Yes, TST_ONE should use the narrower schema.", "2026-10-05T12:15:00+00:00"),
        (5, other, "1.0.0_SA_CTO", "RULING from the lane", "not this serial", "2026-10-05T12:20:00+00:00"),
        (6, mgr, "1.0.0_SA_CTO", "DECISION old", "outside the window", "2026-09-01T12:00:00+00:00"),
        (7, mgr, "1.0.0_SA_CTO", "Re 80: the bid", "Yes, TST_ONE bid is placed and pushed.", "2026-10-05T12:25:00+00:00"),
        (8, mgr, "1.0.0_SA_CTO", "Re 90: arms", "Yes, LIVE_ARMS says so.", "2026-10-05T12:30:00+00:00"),
    ]
    con.executemany("insert into messages values (?,?,?,?,?,?)", rows)
    con.commit()
    con.close()
    return {"repo": repo, "mcp": mcp, "mgr": mgr, "decomp": decomp}


def selftest() -> int:
    results = []

    def case(name: str, ok: bool, detail: str = "") -> None:
        results.append(ok)
        print("%s %s%s" % ("PASS" if ok else "FAIL", name, "" if ok else " -- " + detail))

    start, end = parse_utc("2026-10-05T00:00:00Z"), parse_utc("2026-10-06T00:00:00Z")
    with tempfile.TemporaryDirectory(prefix="mstr-record-selftest-") as base:
        fx = build_fixture(base)
        lines = []
        res = run(fx["mgr"], start, end, fx["repo"], fx["mcp"], out=lines.append)
        text = "\n".join(lines)
        paths = [(row[2], row[3]) for row in res["listed"]]
        case("a manager commit to a decomposition is listed",
             any(s == "mstr edits the decomposition" and p == fx["decomp"] for s, p in paths), text)
        case("a manager commit to an ordinary tool is not listed", not any(".tools/infra.py" in p for _, p in paths), text)
        case("a lane's commit to a decomposition is not the manager's (exact serial)",
             not any(s == "lane edits" for s, _ in paths), text)
        case("a merge that wrote new content in a project-lane path is listed",
             any(s.startswith("merge worker (resolved)") and p == fx["decomp"] for s, p in paths), text)
        case("a merge that only brings a parent's content is not listed",
             not any(s == "merge worker2" for s, _ in paths) and not any("TO-2" in p for _, p in paths), text)
        case("a commit outside the window is not counted or listed", not any(s == "mstr old edit" for s, _ in paths)
             and res["commits"] == 5, "commits=%d\n%s" % (res["commits"], text))
        case("a message with a RULING subject is listed", 1 in res["shaped"], text)
        case("a merge notice is not listed", 2 not in res["shaped"], text)
        case("a spawn notice is not listed", 3 not in res["shaped"], text)
        case("an answer about a project code is listed", 4 in res["shaped"], text)
        case("a bid notice naming a project code is not listed", 7 not in res["shaped"], text)
        case("a token that names no project row is not a project code", 8 not in res["shaped"], text)
        case("another serial's RULING and an out-of-window DECISION are not counted",
             5 not in res["shaped"] and 6 not in res["shaped"] and res["messages"] == 6, "messages=%d" % res["messages"])
        case("the final line carries every count and ok=True",
             res["line"].endswith("unread_limbs=0 ok=True") and "ruling_shaped=2" in res["line"] and
             "ruling_paths=2" in res["line"], res["line"])
        gone = run(fx["mgr"], start, end, fx["repo"], os.path.join(base, "no-such-mcp"), out=lambda _t: None)
        case("an unreadable message source is UNREAD and the run is not ok, never a zero",
             gone["unread"] == 1 and gone["line"].endswith("ok=False") and "messages=0" in gone["line"], gone["line"])
        broken = run(fx["mgr"], start, end, os.path.join(base, "no-such-repo"), fx["mcp"], out=lambda _t: None)
        case("an unreadable repository is UNREAD and the run is not ok", broken["unread"] == 1 and broken["line"].endswith("ok=False"),
             broken["line"])
    good = sum(1 for r in results if r)
    print("MSTR-RECORD-SELFTEST cases=%d/%d ok=%s" % (good, len(results), good == len(results)))
    return 0 if good == len(results) else 1


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(prog="mstr-record-check.py", description=__doc__.split("\n")[0])
    ap.add_argument("--serial")
    ap.add_argument("--since")
    ap.add_argument("--until")
    ap.add_argument("--repo", help="repository to read (default: the main worktree)")
    ap.add_argument("--mcp-dir", help="the broker's directory (default: <main worktree>/org/mcp)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.serial or not args.since:
        print("usage: mstr-record-check.py --serial <manager serial> --since <UTC> [--until <UTC>] | --selftest",
              file=sys.stderr)
        return 2
    try:
        start = parse_utc(args.since)
        end = parse_utc(args.until) if args.until else datetime.datetime.now(datetime.timezone.utc)
    except ValueError as exc:
        print("ERROR: unreadable time (%s)" % exc, file=sys.stderr)
        return 2
    if end < start:
        print("ERROR: --until is before --since", file=sys.stderr)
        return 2
    root = main_root()
    repo = args.repo or root
    mcp = args.mcp_dir or os.path.join(root, "org", "mcp")
    print("MSTR-RECORD read | serial %s | %s to %s | repo %s | broker %s" % (
        args.serial, start.strftime("%Y-%m-%dT%H:%M:%SZ"), end.strftime("%Y-%m-%dT%H:%M:%SZ"), repo, mcp))
    res = run(args.serial, start, end, repo, mcp)
    print(res["line"])
    return 0 if res["unread"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
