#!/usr/bin/env python3
"""crossbox-matrix.py -- the directed matrix of cross-box files across every box branch (NFRA_CTLPLN FWD-3, FWD-22; cell CT-t-2).

A cross-box call is a file org/devices/crossbox/<id>.json (schema crossbox/1, written by .tools/crossbox-call.py). Each box
writes its own copy on its own branch, so ONE branch's folder is never the whole picture. This tool is READ-ONLY: it unions
the folder over origin/box/*, origin/CLOUD and the working tree, reading each ref through `git show <ref>:<path>`, then
prints, for every directed pair of distinct boxes in the device register, the newest file with its state, whether `ack` is
set, `ack.bus_message_id` and its age. A pair with no file reads NONE.

  python .tools/crossbox-matrix.py [--fetch] [--since <UTC>] [--root <repo>]
  python .tools/crossbox-matrix.py --selftest

The same `id` on several refs is ONE file; the most advanced state wins (OPEN < ACKED < CLOSED-BOTH), and every ref that
carries it is printed. A file that cannot be read or fails the crossbox/1 shape is listed UNREADABLE and is not counted. A
file naming a box the register does not hold is listed UNREGISTERED and is not counted. Boxes and the pair count come from
the register through lib/devices.py; nothing here types a box name.

`acked` counts pairs whose newest file has `ack` set (a CLOSED-BOTH file always has one, so closed_both <= acked).
A message carried on the bus with no file is invisible to this tool (BLIND).

LAST line: CROSSBOX-MATRIX pairs=<n> with_file=<a> acked=<b> closed_both=<c> none=<d>
Selftest LAST line: CROSSBOX-MATRIX-SELFTEST cases=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "lib"))
import devices  # noqa: E402

# the ONE reader of the call files (CT-ba-1): a crossbox/2 call is read as the from-side file with its answer file
_spec = importlib.util.spec_from_file_location("crossbox_call_reader_matrix", ROOT / ".tools" / "crossbox-call.py")
CALLS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CALLS)

FOLDER = "org/devices/crossbox"
SCHEMA = "crossbox/1"
SCHEMA2 = "crossbox/2"
RANK = {"OPEN": 0, "ACKED": 1, "CLOSED-BOTH": 2}
WORKTREE = "worktree"


def git(root, *args, check=False):
    p = subprocess.run(["git", "-C", str(root)] + list(args), capture_output=True)
    if check and p.returncode != 0:
        raise RuntimeError("git %s rc=%d: %s" % (" ".join(args), p.returncode, p.stderr.decode("utf-8", "replace").strip()))
    return p


def box_refs(root):
    """origin/box/* and origin/CLOUD, as they stand locally (run --fetch first for the live picture)."""
    out = git(root, "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/box", "refs/remotes/origin/CLOUD")
    refs = sorted(r for r in out.stdout.decode("utf-8", "replace").split() if r)
    # `git for-each-ref refs/remotes/origin/CLOUD` can also match origin/CLOUD/* sub-refs; keep the exact trunk only.
    return [r for r in refs if r == "origin/CLOUD" or r.startswith("origin/box/")]


def shape(rec):
    """(record, None) or (None, reason). The record as the one reader folds it (crossbox/1, or crossbox/2 assembled): the keys
    the matrix reads must be present and typed."""
    if not isinstance(rec, dict):
        return None, "not a JSON object"
    if rec.get("schema") not in (SCHEMA, SCHEMA2):
        return None, "schema is %r, not %r or %r" % (rec.get("schema"), SCHEMA, SCHEMA2)
    for k in ("id", "from_device", "to_device"):
        if not isinstance(rec.get(k), str) or not rec[k]:
            return None, "key %s missing or not a string" % k
    if rec.get("state") not in RANK:
        return None, "state %r not in %s" % (rec.get("state"), sorted(RANK))
    return rec, None


def _advance(text) -> tuple:
    """How far an answer file's copy has gone: a closed answer is the most advanced, an acked one next, a bare one least."""
    try:
        doc = json.loads(text)
    except ValueError:
        return (0,)
    if not isinstance(doc, dict):
        return (0,)
    if (doc.get("closed_to") or {}).get("at"):
        return (2,)
    return (1,) if doc.get("ack") else (0,)


def read_sources(root, refs):
    """Yield (source, path, text-or-None) for every crossbox file on every ref and in the working tree."""
    for ref in refs:
        ls = git(root, "ls-tree", "-r", "--name-only", ref, "--", FOLDER + "/")
        if ls.returncode != 0:
            yield ref, FOLDER, None
            continue
        for path in ls.stdout.decode("utf-8", "replace").split("\n"):
            path = path.strip()
            if not path.endswith(".json"):
                continue
            show = git(root, "show", "%s:%s" % (ref, path))
            if show.returncode != 0:
                yield ref, path, None
                continue
            try:
                yield ref, path, show.stdout.decode("utf-8")
            except UnicodeDecodeError:
                yield ref, path, None
    wt = pathlib.Path(root) / FOLDER
    if wt.is_dir():
        for f in sorted(wt.glob("*.json")):
            try:
                yield WORKTREE, FOLDER + "/" + f.name, f.read_bytes().decode("utf-8")
            except (OSError, UnicodeDecodeError):
                yield WORKTREE, FOLDER + "/" + f.name, None


def union(root, refs):
    """({id: {rec, refs}}, [unreadable (source, path, reason)]). One entry per id; the most advanced state wins."""
    files, bad = {}, []
    by_source = {}   # source -> {file name: text}: each source's folder is folded by the one reader, call by call
    for source, path, text in read_sources(root, refs):
        if text is None:
            bad.append((source, path, "unreadable from this source"))
            continue
        by_source.setdefault(source, {})[path.rsplit("/", 1)[-1]] = text
    # a layout-2 call can span refs: the sender's branch holds the from-side file, the answering box's branch its answer file.
    # So every answer file is offered to every source's fold (the most advanced copy of a name wins), and an answer that a
    # source does not hold is not that source's error.
    answers = {}
    for texts in by_source.values():
        for name, text in texts.items():
            if CALLS.ANSWER_RE.fullmatch(name) and (name not in answers or _advance(text) > _advance(answers[name])):
                answers[name] = text
    entries = []
    for source, texts in by_source.items():
        full = dict(answers)
        full.update(texts)
        for name, doc, err in CALLS.fold_texts(full):
            if err is not None and CALLS.ANSWER_RE.fullmatch(name) and name not in texts:
                continue
            entries.append((source, name, doc, err))
    for source, name, doc, err in entries:
        if err is not None:
            bad.append((source, FOLDER + "/" + name, err))
            continue
        rec, why = shape(doc)
        if rec is None:
            bad.append((source, FOLDER + "/" + name, why))
            continue
        cur = files.get(rec["id"])
        if cur is None:
            files[rec["id"]] = {"rec": rec, "refs": [source]}
            continue
        cur["refs"].append(source)
        old = cur["rec"]
        key = (RANK[rec["state"]], 1 if rec.get("ack") else 0)
        if key > (RANK[old["state"]], 1 if old.get("ack") else 0):
            cur["rec"] = rec
    return files, bad


def parse_utc(s):
    if not isinstance(s, str):
        return None
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
    except ValueError:
        return None


def age_text(opened, now):
    t = parse_utc(opened)
    if t is None:
        return "age-unknown"
    secs = int((now - t).total_seconds())
    if secs < 0:
        return "future"
    d, rem = divmod(secs, 86400)
    h, rem = divmod(rem, 3600)
    return "%dd%02dh%02dm" % (d, h, rem // 60)


def build(root, refs, reg, since=None):
    """The matrix as data: pairs {(from, to): record-or-None}, files, unreadable, unregistered, skipped."""
    names = devices.names(reg)
    files, bad = union(root, refs)
    pairs = {(a, b): None for a in names for b in names if a != b}
    unregistered, skipped = [], []
    cutoff = parse_utc(since) if since else None
    for fid, ent in sorted(files.items()):
        rec = ent["rec"]
        if cutoff is not None:
            opened = parse_utc(rec.get("opened_at"))
            if opened is None or opened < cutoff:
                skipped.append(fid)
                continue
        a, b = devices.resolve(rec["from_device"], reg), devices.resolve(rec["to_device"], reg)
        if a is None or b is None or a == b:
            unregistered.append((fid, rec["from_device"], rec["to_device"]))
            continue
        cur = pairs[(a, b)]
        mine = (rec.get("opened_at") or "", fid)
        if cur is None or mine > (cur["rec"].get("opened_at") or "", cur["id"]):
            pairs[(a, b)] = {"id": fid, "rec": rec, "refs": ent["refs"]}
    return {"pairs": pairs, "files": files, "bad": bad, "unregistered": unregistered, "skipped": skipped}


def counts(m):
    got = [v for v in m["pairs"].values() if v is not None]
    return {
        "pairs": len(m["pairs"]),
        "with_file": len(got),
        "acked": sum(1 for v in got if v["rec"].get("ack")),
        "closed_both": sum(1 for v in got if v["rec"]["state"] == "CLOSED-BOTH"),
        "none": len(m["pairs"]) - len(got),
    }


def render(m, now, refs):
    lines = ["SOURCES %s" % ", ".join(list(refs) + [WORKTREE])]
    for fid, ent in sorted(m["files"].items()):
        r = ent["rec"]
        lines.append("FILE %s %s->%s state=%s refs=%s" % (fid, r["from_device"], r["to_device"], r["state"], ",".join(ent["refs"])))
    for source, path, why in m["bad"]:
        lines.append("UNREADABLE %s:%s -- %s" % (source, path, why))
    for fid, a, b in m["unregistered"]:
        lines.append("UNREGISTERED %s %s->%s (not a pair of distinct registered boxes; not counted)" % (fid, a, b))
    if m["skipped"]:
        lines.append("SKIPPED-BY-SINCE %d file(s)" % len(m["skipped"]))
    for (a, b), v in m["pairs"].items():
        if v is None:
            lines.append("PAIR %s->%s NONE" % (a, b))
            continue
        r = v["rec"]
        ack = r.get("ack")
        bus = ack.get("bus_message_id") if isinstance(ack, dict) else None
        lines.append("PAIR %s->%s newest=%s state=%s ack=%s ack.bus_message_id=%s age=%s" % (
            a, b, v["id"], r["state"], "set" if ack else "unset", bus or "-", age_text(r.get("opened_at"), now)))
    c = counts(m)
    lines.append("CROSSBOX-MATRIX pairs=%d with_file=%d acked=%d closed_both=%d none=%d" % (
        c["pairs"], c["with_file"], c["acked"], c["closed_both"], c["none"]))
    return lines


# ---------------------------------------------------------------- selftest

def _xb(fid, a, b, state, ack=False, opened="2026-10-09T01:00:00Z"):
    return {"schema": SCHEMA, "id": fid, "kind": "CALL", "from_device": a, "to_device": b, "opened_at": opened,
            "state": state, "sent": {"at": opened, "bus_message_id": "m-" + fid},
            "ack": {"at": opened, "by": "s", "bus_message_id": "ack-" + fid} if ack else None}


def _fixture(tmp, ref_files, wt_files=None):
    """A temp git repo with one commit per ref (refs/remotes/<ref>) carrying {filename: text} under the crossbox folder."""
    root = pathlib.Path(tmp)
    git(root, "init", "-q", check=True)
    for n, (ref, files) in enumerate(sorted(ref_files.items())):
        d = root / FOLDER
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.json"):
            old.unlink()
        for name, text in files.items():
            (d / name).write_text(text, encoding="utf-8")
        git(root, "add", "-A", check=True)
        git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "c%d" % n, check=True)
        sha = git(root, "rev-parse", "HEAD", check=True).stdout.decode().strip()
        git(root, "update-ref", "refs/remotes/" + ref, sha, check=True)
    d = root / FOLDER
    if d.exists():
        for old in d.glob("*.json"):
            old.unlink()
    for name, text in (wt_files or {}).items():
        d.mkdir(parents=True, exist_ok=True)
        (d / name).write_text(text, encoding="utf-8")
    return root


def _reg(names):
    return {"devices": [{"name": n, "aliases": [], "inbound_queue": "q-" + n} for n in names]}


def selftest():
    results = []
    now = datetime.datetime(2026, 10, 9, 2, 0, 0, tzinfo=datetime.timezone.utc)

    def case(name, ok, detail=""):
        results.append(ok)
        print("%s %s %s" % ("PASS" if ok else "FAIL", name, detail))

    def dump(rec):
        return json.dumps(rec)

    # 1 and 2: the same id on two refs counts once at its most advanced state; a pair with no file reads NONE.
    with tempfile.TemporaryDirectory() as tmp:
        f_open = _xb("XB-1", "alpha", "beta", "OPEN")
        f_done = _xb("XB-1", "alpha", "beta", "CLOSED-BOTH", ack=True)
        root = _fixture(tmp, {"origin/box/alpha": {"XB-1.json": dump(f_open)},
                              "origin/box/beta": {"XB-1.json": dump(f_done)}})
        refs = box_refs(root)
        m = build(root, refs, _reg(["alpha", "beta", "gamma"]))
        c = counts(m)
        v = m["pairs"][("alpha", "beta")]
        case("same-id-on-two-refs-counts-once", c["with_file"] == 1 and v["rec"]["state"] == "CLOSED-BOTH"
             and sorted(v["refs"]) == ["origin/box/alpha", "origin/box/beta"], "counts=%s refs=%s" % (c, v["refs"]))
        case("pair-with-no-file-reads-NONE", c["pairs"] == 6 and c["none"] == 5 and m["pairs"][("beta", "alpha")] is None
             and any(ln == "PAIR beta->alpha NONE" for ln in render(m, now, refs)), "counts=%s" % c)
        case("closed-both-implies-acked", c["acked"] == 1 and c["closed_both"] == 1, "counts=%s" % c)

    # 3: a malformed file is listed UNREADABLE and not counted (broken JSON, wrong schema, and a bad state).
    with tempfile.TemporaryDirectory() as tmp:
        bad_state = _xb("XB-4", "alpha", "beta", "WHATEVER")
        wrong = dict(_xb("XB-5", "alpha", "beta", "OPEN"), schema="other/9")
        root = _fixture(tmp, {"origin/box/alpha": {"XB-3.json": "{not json", "XB-4.json": dump(bad_state), "XB-5.json": dump(wrong),
                                                    "XB-6.json": dump(_xb("XB-6", "alpha", "beta", "OPEN"))}})
        refs = box_refs(root)
        m = build(root, refs, _reg(["alpha", "beta"]))
        c = counts(m)
        lines = render(m, now, refs)
        case("malformed-file-listed-UNREADABLE-not-counted",
             len(m["bad"]) == 3 and c["with_file"] == 1 and sum(1 for ln in lines if ln.startswith("UNREADABLE")) == 3,
             "bad=%d counts=%s" % (len(m["bad"]), c))

    # 4: a fifth box added to a fixture register makes 20 pairs with no code edit; four boxes make 12.
    with tempfile.TemporaryDirectory() as tmp:
        root = _fixture(tmp, {"origin/box/alpha": {}})
        refs = box_refs(root)
        n4 = counts(build(root, refs, _reg(["a", "b", "c", "d"])))["pairs"]
        n5 = counts(build(root, refs, _reg(["a", "b", "c", "d", "e"])))["pairs"]
        case("fifth-box-makes-20-pairs-no-code-edit", n4 == 12 and n5 == 20, "four=%d five=%d" % (n4, n5))

    # 5: a file only in the working tree is read, and the newest file of a pair wins by opened_at.
    with tempfile.TemporaryDirectory() as tmp:
        old = _xb("XB-7", "alpha", "beta", "CLOSED-BOTH", ack=True, opened="2026-10-09T00:00:00Z")
        new = _xb("XB-8", "alpha", "beta", "OPEN", opened="2026-10-09T01:30:00Z")
        root = _fixture(tmp, {"origin/CLOUD": {"XB-7.json": dump(old)}}, wt_files={"XB-8.json": dump(new)})
        refs = box_refs(root)
        m = build(root, refs, _reg(["alpha", "beta"]))
        v = m["pairs"][("alpha", "beta")]
        case("worktree-read-and-newest-wins", v["id"] == "XB-8" and v["refs"] == [WORKTREE] and "origin/CLOUD" in refs
             and any("age=0d00h30m" in ln for ln in render(m, now, refs)), "newest=%s refs=%s" % (v["id"], v["refs"]))

    # 6: --since drops older files; a file naming a box outside the register is UNREGISTERED and not counted.
    with tempfile.TemporaryDirectory() as tmp:
        a = _xb("XB-9", "alpha", "beta", "OPEN", opened="2026-10-01T00:00:00Z")
        b = _xb("XB-10", "alpha", "zeta", "OPEN", opened="2026-10-09T00:00:00Z")
        root = _fixture(tmp, {"origin/box/alpha": {"XB-9.json": dump(a), "XB-10.json": dump(b)}})
        refs = box_refs(root)
        m = build(root, refs, _reg(["alpha", "beta"]), since="2026-10-05T00:00:00Z")
        c = counts(m)
        case("since-and-unregistered", m["skipped"] == ["XB-9"] and len(m["unregistered"]) == 1 and c["with_file"] == 0,
             "skipped=%s unregistered=%d counts=%s" % (m["skipped"], len(m["unregistered"]), c))

    ok = all(results)
    print("CROSSBOX-MATRIX-SELFTEST cases=%d/%d ok=%s" % (sum(results), len(results), ok))
    return 0 if ok else 1


# ---------------------------------------------------------------- main

def main(argv):
    ap = argparse.ArgumentParser(description="4x4 directed matrix of cross-box files across every box branch (read-only)")
    ap.add_argument("--fetch", action="store_true", help="git fetch origin first (reads only the remote)")
    ap.add_argument("--since", help="only files opened at or after this UTC time (YYYY-MM-DDTHH:MM:SSZ)")
    ap.add_argument("--root", default=str(ROOT), help="repository to read (default: the one this script lives in)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.since and parse_utc(args.since) is None:
        print("ERROR: --since must be YYYY-MM-DDTHH:MM:SSZ, got %r" % args.since)
        return 2
    try:
        reg = devices.load()
    except devices.RegisterError as exc:
        print(exc)
        return 3
    if args.fetch:
        p = git(args.root, "fetch", "origin", "--quiet")
        if p.returncode != 0:
            print("WARN: git fetch origin rc=%d (%s); the refs below are as last fetched" % (
                p.returncode, p.stderr.decode("utf-8", "replace").strip()))
        else:
            print("OK: git fetch origin rc=0")
    refs = box_refs(args.root)
    if not refs:
        print("WARN: no origin/box/* or origin/CLOUD ref found; the matrix reads the working tree only")
    m = build(args.root, refs, reg, since=args.since)
    for ln in render(m, datetime.datetime.now(datetime.timezone.utc), refs):
        print(ln)
    return 0


if __name__ == "__main__":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    sys.exit(main(sys.argv[1:]))
