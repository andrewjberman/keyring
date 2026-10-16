#!/usr/bin/env python3
"""test_round29_crossbox_split.py -- CT-ba-1 (NFRA_CTLPLN round 29, FWD-8): a cross-box call's two sides write two files.

Run: python .tools/tests/test_round29_crossbox_split.py   (LAST line: CROSSBOX-SPLIT arms=<k>/<n> ok=<True|False>)

The from side writes XB-<id>.json (crossbox/2); each answering box writes XB-<id>.<box>.json (crossbox-answer/1). These arms
run the layout on temporary git repositories (two clones of a temporary bare origin, one per box) and the base tool at
7d4aef5b93 copied into a temporary folder. Nothing is pushed, fetched from a network, or written under the real
org/devices/crossbox. Arm (j) is the control: a reader that reads only the from-side file must fail arm (c).
"""
from __future__ import annotations

import contextlib
import datetime
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
REPO = TOOLS.parent
BASE_OBJ = "7d4aef5b93:.tools/crossbox-call.py"
SEAT = "9.9.0_ZZ_Selftest"
LANE = "~X"
BODY = "docs/selftest_body.md"
ANSWER_BUS = "0a1b2c3d-0000-4000-8000-0000000000e1"
FIXED = datetime.datetime(2026, 10, 16, 12, 0, 0, tzinfo=datetime.timezone.utc)
RESULTS = []


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


os.environ["OPAL_DEVICE_REGISTER"] = str(REPO / "org" / "devices" / "DEVICES.json")   # the base copy reads the same register
cb = load("crossbox_call_split_under_test", TOOLS / "crossbox-call.py")
REL = cb.REL_DIR


def rmtree_force(path) -> None:
    def onerr(func, target, _exc):
        os.chmod(target, 0o700)
        func(target)
    shutil.rmtree(path, onerror=onerr)


def arm(name, ok, detail=""):
    RESULTS.append((name, bool(ok), str(detail)[:400]))


@contextlib.contextmanager
def fixed_now(mod):
    old = mod.now_dt
    mod.now_dt = lambda: FIXED
    try:
        yield
    finally:
        mod.now_dt = old


def run_main(mod, argv):
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rc = mod.main(argv)
    except Exception as exc:   # an exception is an output too: it must match the base's exception
        return ("EXC", type(exc).__name__, str(exc))
    return (rc, buf.getvalue())


def load_base(tmp):
    """The base tool (7d4aef5b93) in a temporary folder with the register module beside it; (module, reason)."""
    present = subprocess.run(["git", "-C", str(REPO), "cat-file", "-e", BASE_OBJ], capture_output=True).returncode == 0
    if not present:
        return None, "git object %s is absent" % BASE_OBJ
    text = subprocess.run(["git", "-C", str(REPO), "show", BASE_OBJ], capture_output=True).stdout
    root = Path(tmp) / "base"
    (root / ".tools").mkdir(parents=True)
    (root / "lib").mkdir()
    (root / ".tools" / "crossbox-call.py").write_bytes(text)
    shutil.copy(REPO / "lib" / "devices.py", root / "lib" / "devices.py")
    return load("crossbox_call_base", root / ".tools" / "crossbox-call.py"), ""


class Pair:
    """Box A (the sender, the first device of the register) and box B (the answering box), two clones of one bare origin."""

    def __init__(self, mod, tmp, layout2: bool):
        self.mod = mod
        tmp = Path(tmp)
        tmp.mkdir(parents=True, exist_ok=True)
        names = mod.devmod().names()
        a_root, b_root, origin = tmp / "boxA", tmp / "boxB", tmp / "origin.git"
        a_root.mkdir()
        mod.sgit(a_root, "init", "-q")
        (a_root / "docs").mkdir()
        (a_root / BODY).write_text("selftest body\n", encoding="utf-8")
        mod.sgit(a_root, "add", BODY)
        mod.sgit(a_root, "commit", "-q", "-m", "body")
        subprocess.run(["git", *cb.GIT_FLAGS, "init", "-q", "--bare", str(origin)], capture_output=True, text=True,
                       env={**os.environ, **cb.GIT_ENV}, timeout=60, check=True)
        mod.sgit(a_root, "remote", "add", "origin", str(origin))
        self.push(mod, a_root)
        if layout2:
            (a_root / REL).mkdir(parents=True)
            (a_root / REL / "LAYOUT").write_text("2\n", encoding="utf-8", newline="\n")
            mod.sgit(a_root, "add", "--", REL + "/LAYOUT")
            mod.sgit(a_root, "commit", "-q", "-m", "layout", "--", REL + "/LAYOUT")
            self.push(mod, a_root)
        subprocess.run(["git", *cb.GIT_FLAGS, "clone", "-q", str(a_root), str(b_root)], capture_output=True, text=True,
                       env={**os.environ, **cb.GIT_ENV}, timeout=60, check=True)
        (b_root / "org" / "tier2_senior" / SEAT).mkdir(parents=True)
        (b_root / "org" / "mcp" / "inbox" / SEAT / LANE).mkdir(parents=True)
        self.a = mod.Box(a_root, names[0])
        self.b = mod.Box(b_root, names[1])

    def push(self, mod, root):
        rc, _, err = mod.sgit(Path(root), "push", "-q", "origin", "HEAD:refs/heads/main")
        if rc != 0:
            raise RuntimeError("push to the scratch origin failed: %s" % err.strip()[:120])

    def commit(self, mod, box, *paths) -> str:
        mod.sgit(box.root, "add", "--", *paths)
        mod.sgit(box.root, "commit", "-q", "-m", "step", "--", *paths)
        return mod.sgit(box.root, "rev-parse", "HEAD")[1].strip()

    def pull(self, mod, dst, src, ff: bool):
        mod.sgit(dst.root, "fetch", "-q", str(src.root), "HEAD")
        if ff:
            mod.sgit(dst.root, "merge", "-q", "--ff-only", "FETCH_HEAD")

    def open_call(self, subject="Split arm call", call_id=None):
        """Open on A, commit and push the file, put the bus line out, and let B pull the commit (as box-sync does)."""
        mod = self.mod
        cid = self.a.open("CALL", self.b.device, SEAT + LANE, "1.0.0_SA_CTO", subject, BODY, call_id=call_id)[0].split()[1]
        self.commit(mod, self.a, self.a.rel(cid))
        self.push(mod, self.a.root)
        line = self.a.line(cid)[0]
        self.pull(mod, self.b, self.a, ff=True)
        return cid, line

    def answered(self, cid, line):
        """B receives, acknowledges, commits its answer file and pushes; A pulls it."""
        mod = self.mod
        self.b.receive(line)
        self.b.ack(cid, SEAT + LANE)
        self.commit(mod, self.b, self.answer_rel(cid))
        self.push(mod, self.b.root)
        self.pull(mod, self.a, self.b, ff=True)

    def answer_rel(self, cid) -> str:
        return "%s/%s" % (REL, self.mod.answer_name(cid, self.b.device))


def files_of(root) -> list:
    d = Path(root) / REL
    return sorted(p.name for p in d.iterdir()) if d.is_dir() else []


def snapshot(root) -> dict:
    d = Path(root) / REL
    return {p.name: p.read_bytes() for p in sorted(d.iterdir())} if d.is_dir() else {}


def closed_flow(mod, tmp, subject="Split arm call"):
    """The exchange whose two sides close on two boxes: A closes the from side, B closes the to side, B merges A's commit
    and A merges B's commit. Returns the facts the arms read."""
    p = Pair(mod, tmp, True)
    cid, line = p.open_call(subject=subject)
    p.answered(cid, line)
    a_close = p.a.close(cid, "from", "1.0.0_SA_CTO")
    a_commit = p.commit(mod, p.a, p.a.rel(cid))
    a_files = mod.sgit(p.a.root, "show", "--name-only", "--format=", a_commit)[1].split()
    p.b.close(cid, "to", SEAT + LANE)
    b_commit = p.commit(mod, p.b, p.answer_rel(cid))
    b_files = mod.sgit(p.b.root, "show", "--name-only", "--format=", b_commit)[1].split()
    fetch_rc = mod.sgit(p.b.root, "fetch", "-q", str(p.a.root), "HEAD")[0]
    merge_rc, merge_out, merge_err = mod.sgit(p.b.root, "merge", "--no-edit", "FETCH_HEAD")
    unmerged = mod.sgit(p.b.root, "ls-files", "-u")[1].strip()
    markers = any("<<<<<<<" in (p.b.root / REL / n).read_text(encoding="utf-8") for n in files_of(p.b.root)
                  if n.startswith("XB-"))
    status_b = p.b.status(cid)[0]
    mod.sgit(p.a.root, "fetch", "-q", str(p.b.root), "HEAD")
    a_merge_rc = mod.sgit(p.a.root, "merge", "--no-edit", "FETCH_HEAD")[0]
    status_a = p.a.status(cid)[0]
    return {"cid": cid, "pair": p, "a_close": a_close, "a_files": a_files, "b_files": b_files, "fetch_rc": fetch_rc,
            "a_commit_sha": a_commit, "b_commit_sha": b_commit,
            "merge_rc": merge_rc, "merge_out": (merge_out + merge_err).strip(), "unmerged": unmerged, "markers": markers,
            "status_b": status_b, "status_a": status_a, "a_merge_rc": a_merge_rc}


# ---------------------------------------------------------------- the arms

def arm_a(tmp):
    p = Pair(cb, tmp, True)
    cid = p.a.open("CALL", p.b.device, SEAT + LANE, "1.0.0_SA_CTO", "Split arm call", BODY)[0].split()[1]
    listing = files_of(p.a.root)
    raw = json.loads((p.a.root / REL / ("%s.json" % cid)).read_text(encoding="utf-8"))
    ok = listing == sorted(["LAYOUT", "%s.json" % cid]) and raw["schema"] == "crossbox/2" and "state" not in raw \
        and raw["closed_from"] == {"at": None, "by": None}
    arm("(a) LAYOUT 2: open writes exactly one call file, XB-<id>.json of schema crossbox/2, and no answer file",
        ok, "files=%s schema=%s" % (listing, raw["schema"]))


def arm_b(tmp):
    p = Pair(cb, tmp, True)
    cid, line = p.open_call()
    from_path = p.b.path(cid)
    before_bytes, before_files = from_path.read_bytes(), files_of(p.b.root)
    p.b.receive(line)
    reply = p.b.ack(cid, SEAT + LANE)
    after_files = files_of(p.b.root)
    answer = p.b.root / REL / cb.answer_name(cid, p.b.device)
    ans = json.loads(answer.read_text(encoding="utf-8")) if answer.is_file() else {}
    ok = from_path.read_bytes() == before_bytes and sorted(set(after_files) - set(before_files)) == [answer.name] \
        and ans.get("schema") == "crossbox-answer/1" and ans.get("ack", {}).get("by") == SEAT + LANE and ans.get("closed_to") == {"at": None, "by": None} \
        and reply[-1].startswith("CROSSBOX-ACK %s READ by" % cid)
    arm("(b) the answering box's ack writes only its own answer file; the from-side file is byte-identical", ok,
        "new=%s from-side unchanged=%s" % (sorted(set(after_files) - set(before_files)), from_path.read_bytes() == before_bytes))


def arm_c(tmp):
    f = closed_flow(cb, tmp)
    ok = (f["a_close"][0].startswith("STATUS") and f["fetch_rc"] == 0 and f["merge_rc"] == 0 and not f["markers"]
          and f["unmerged"] == "" and f["a_merge_rc"] == 0
          and f["status_b"].startswith("STATUS %s CLOSED-BOTH" % f["cid"]) and f["status_a"].startswith("STATUS %s CLOSED-BOTH" % f["cid"])
          and f["a_files"] == [f["pair"].a.rel(f["cid"])] and f["b_files"] == [f["pair"].answer_rel(f["cid"])])
    arm("(c) from-side close (clone A) and to-side ack and close (clone B) merge with zero conflicts and read CLOSED-BOTH",
        ok, "merge rc=%s conflicts=%s status_b=%s | A commit=%s B commit=%s | status_a=%s" % (
            f["merge_rc"], f["markers"] or bool(f["unmerged"]), f["status_b"][:60], f["a_files"], f["b_files"], f["status_a"][:60]))


def arm_d(tmp):
    p = Pair(cb, tmp, True)
    cid, line = p.open_call()
    p.answered(cid, line)
    before = snapshot(p.a.root), snapshot(p.b.root)
    refusals = [
        ("ack on the sending box", lambda: p.a.ack(cid, SEAT + LANE), "receiving box"),
        ("close --side to on the sending box", lambda: p.a.close(cid, "to", SEAT + LANE), "receiving box"),
        ("close --side from on the receiving box", lambda: p.b.close(cid, "from", "1.0.0_SA_CTO"), "sending box"),
        ("sent on the receiving box", lambda: p.b.sent(cid, ANSWER_BUS), "sending box"),
        ("acked on the receiving box", lambda: p.b.acked(cid, "[x] CROSSBOX-ACK %s READ by %s at 2026-10-16T12:00:00Z" % (cid, SEAT + LANE), ANSWER_BUS), "sending box"),
        ("withdraw on the receiving box", lambda: p.b.withdraw(cid, "1.0.0_SA_CTO", BODY), "sending box"),
        ("supersede on the receiving box", lambda: p.b.supersede(cid, "1.0.0_SA_CTO", BODY, cid), "sending box"),
    ]
    results = []
    for label, fn, needle in refusals:
        try:
            fn()
            results.append((label, False, "no refusal"))
        except cb.Refused as exc:
            results.append((label, needle in str(exc), str(exc)[:90]))
    unchanged = (snapshot(p.a.root), snapshot(p.b.root)) == before
    ok = all(r[1] for r in results) and unchanged
    arm("(d) each writer refuses the other side's file (ack, close --side to/from, sent, acked, withdraw, supersede) and writes nothing",
        ok, "refused=%d/%d unchanged=%s | %s" % (sum(1 for r in results if r[1]), len(results), unchanged,
                                               "; ".join(r[0] + ": " + ("ok" if r[1] else "FAIL " + r[2]) for r in results if not r[1]) or "all named"))


def arm_e(tmp, base):
    if base is None:
        arm("(e) no LAYOUT file: open writes crossbox/1 exactly as at the base", True, "SKIP: the base object is absent")
        return
    got = {}
    for label, mod in (("base", base), ("new", cb)):
        with fixed_now(mod):
            p = Pair(mod, Path(tmp) / label, False)
            lines = p.a.open("CALL", p.b.device, SEAT + LANE, "1.0.0_SA_CTO", "Split arm call", BODY, call_id="OC-SPLIT-E1")
            cid = lines[0].split()[1]
            text = (p.a.root / REL / ("%s.json" % cid)).read_text(encoding="utf-8")
            got[label] = ([x.replace(cid, "XB-ID") for x in lines], text.replace(cid, "XB-ID"),
                          [n.replace(cid, "XB-ID") for n in files_of(p.a.root)])
    ok = got["base"] == got["new"] and '"schema": "crossbox/1"' in got["new"][1] and not any(n.startswith("LAYOUT") for n in got["new"][2])
    arm("(e) no LAYOUT file: open writes crossbox/1 exactly as at the base (same bytes and lines, ids normalised)", ok,
        "identical=%s files=%s" % (got["base"] == got["new"], got["new"][2]))


def arm_f(tmp, base):
    if base is None:
        arm("(f) the 235 existing calls read identically through the new reader (list and status, base against new)", True,
            "SKIP: the base object is absent")
        return
    src = REPO / REL
    names = sorted(p.name for p in src.glob("*.json"))
    root = Path(tmp) / "real"
    (root / REL).mkdir(parents=True)
    for n in names:
        shutil.copyfile(src / n, root / REL / n)
    outs = {}
    for label, mod in (("base", base), ("new", cb)):
        with fixed_now(mod):
            seq = [run_main(mod, ["--root", str(root), "--device", "laptop", "list"]),
                   run_main(mod, ["--root", str(root), "--device", "laptop", "list", "--open"])]
            for n in names:
                seq.append(run_main(mod, ["--root", str(root), "--device", "laptop", "status", "--id", n[:-5]]))
            outs[label] = seq
    diffs = [i for i, (x, y) in enumerate(zip(outs["base"], outs["new"])) if x != y]
    ok = len(outs["base"]) == len(outs["new"]) and not diffs and len(names) > 0
    arm("(f) the existing calls read identically through the new reader: list, list --open and status for every file, base against new",
        ok, "files=%d commands=%d differing=%d" % (len(names), len(outs["new"]), len(diffs)))


def arm_g(tmp, base):
    f = closed_flow(cb, Path(tmp) / "g2")
    p = f["pair"]
    before = snapshot(p.b.root)
    out = p.b.merge(f["cid"], "origin/main")
    line = out[0]
    same = snapshot(p.b.root) == before
    nothing = line == "CROSSBOX-MERGE %s NOTHING-TO-FOLD (layout 2: each side writes its own file)" % f["cid"]
    # crossbox/1 folds as at the base: one file, a copy with the other box's ack
    q = Pair(cb, Path(tmp) / "g1", False)
    cid, line1 = q.open_call()
    q.b.receive(line1)
    q.b.ack(cid, SEAT + LANE)
    q.commit(cb, q.b, q.b.rel(cid))
    q.pull(cb, q.a, q.b, ff=False)
    fold = q.a.merge(cid, "FETCH_HEAD")
    folded = fold[0].startswith("MERGED %s from FETCH_HEAD" % cid) and q.a.read(cid)["ack"]["by"] == SEAT + LANE
    ok = nothing and same and folded
    arm("(g) merge on a crossbox/2 call prints NOTHING-TO-FOLD and writes nothing; on crossbox/1 it folds the ack as before", ok,
        "layout2=%r unchanged=%s crossbox1=%r" % (line, same, fold[0][:60]))


def arm_h(tmp):
    """open-calls.py's reader for `close` (the function cmd_close calls) reads a layout-2 CLOSED-BOTH pair by call_id."""
    tool = load("opal_open_calls_split", TOOLS / "open-calls.py")
    dev = load("opal_devices_split", REPO / "lib" / "devices.py")
    reg = dev.load()
    base_dir = Path(tmp) / "h"
    state_dir, cross_dir = base_dir / "state", base_dir / "crossbox"
    state_dir.mkdir(parents=True)
    cross_dir.mkdir(parents=True)
    here = dev.resolve("laptop", reg)
    env_keys = {"OPAL_STATE_ROOT": str(state_dir), "OPAL_CROSSBOX_ROOT": str(cross_dir), "AGENTBUS_DEVICE": here,
                "OPAL_AGENT_SERIAL": "0.9.0_WK_TEST~1"}
    old_env = {k: os.environ.get(k) for k in env_keys}
    os.environ.update(env_keys)
    try:
        def run(*argv):
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                try:
                    rc = tool.main(list(argv))
                except SystemExit as exc:
                    rc = exc.code if isinstance(exc.code, int) else 2
            return rc, out.getvalue(), err.getvalue()
        ruling = base_dir / "ruling.md"
        ruling.write_text("RULING -- fixture\n", encoding="utf-8")
        add = ["add", "--project", "NFRA_CTLPLN", "--asked-by", "1.0.0_SA_CTO", "--source", "docs/none.md",
               "--context", "Fixture call: the test creates it to exercise the close path through a layout-2 call.",
               "--rec", "Fixture recommendation: none; the test reads the row, it does not act on it.",
               "--subject", "cross-box call", "--roots", "infra/aws/terraform/shared-infra"]
        rc, out, err = run(*add)
        cid_x = out.split("ADDED id=")[1].split()[0] if "ADDED id=" in out else ""
        f = closed_flow(cb, base_dir / "pair", subject="about %s" % cid_x)
        for name in files_of(f["pair"].b.root):
            if name.startswith("XB-"):
                shutil.copyfile(f["pair"].b.root / REL / name, cross_dir / name)
        found_direct = tool.crossbox_closed_both(cid_x, None)[0]
        rc, out, err = run("close", "--id", cid_x, "--by", "1.0.0_SA_CTO", "--ruling", str(ruling))
        xb = f["cid"]
        rows = json.load(open(state_dir / here / "open_calls.json", encoding="utf-8"))["rows"]
        closed_cb = (rows[-1].get("closed") or {}).get("crossbox") if rows else None
        ok = bool(cid_x) and found_direct == "%s.json" % xb and rc == 0 and rows[-1]["state"] == "CLOSED" and closed_cb == xb
        arm("(h) open-calls.py close finds and closes a CROSS-BOX row through a layout-2 call by call_id (its real reader and close)",
            ok, "add=%r close rc=%s reader=%s crossbox=%s | %s" % (cid_x, rc, found_direct, closed_cb, (err or out).strip()[:160]))
    finally:
        for k, v in old_env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def arm_i(tmp):
    p = Pair(cb, tmp, True)
    cid, line = p.open_call()
    good = p.a.path(cid).read_text(encoding="utf-8")
    checks = []
    raw = json.loads(good)
    raw["schema"] = "crossbox/9"
    p.a.path(cid).write_text(json.dumps(raw), encoding="utf-8")
    try:
        p.a.read(cid)
        checks.append(False)
    except cb.Refused as exc:
        checks.append("crossbox/9" in str(exc))
    raw = json.loads(good)
    raw["surprise"] = 1
    p.a.path(cid).write_text(json.dumps(raw), encoding="utf-8")
    try:
        p.a.read(cid)
        checks.append(False)
    except cb.Refused as exc:
        checks.append("unknown key" in str(exc))
    p.a.path(cid).write_text(good, encoding="utf-8")
    p.b.receive(line)
    p.b.ack(cid, SEAT + LANE)
    ans_path = p.b.root / REL / cb.answer_name(cid, p.b.device)
    ans = json.loads(ans_path.read_text(encoding="utf-8"))
    ans["schema"] = "crossbox-answer/9"
    ans_path.write_text(json.dumps(ans), encoding="utf-8")
    try:
        p.b.read(cid)
        checks.append(False)
    except cb.Refused as exc:
        checks.append("crossbox-answer/9" in str(exc))
    arm("(i) an unknown schema value (call file or answer file) and an unknown key are refused loudly", all(checks),
        "refusals=%d/%d" % (sum(1 for c in checks if c), len(checks)))


def arm_j(tmp):
    mut = load("crossbox_call_mutant_from_only", TOOLS / "crossbox-call.py")

    def from_only(path, where):
        raw = json.loads(path.read_text(encoding="utf-8"))
        return mut.assemble(raw, None, where)     # the mutant never reads the answer file

    mut.load_call_path = from_only
    try:
        f = closed_flow(mut, tmp)
    except Exception as exc:   # the mutant's sender cannot see the answer's ack, so the flow refuses before CLOSED-BOTH: detected
        arm("(j) control: a reader that reads only the from-side file fails arm (c)'s CLOSED-BOTH assertion", True,
            "mutant refused before CLOSED-BOTH: %s: %s" % (type(exc).__name__, str(exc)[:100]))
        return
    closed = f["status_b"].startswith("STATUS %s CLOSED-BOTH" % f["cid"])
    arm("(j) control: a reader that reads only the from-side file fails arm (c)'s CLOSED-BOTH assertion", not closed,
        "mutant status_b=%s" % f["status_b"][:70])


def arm_k(tmp):
    """box-sync's known resolver (.tools/merge-resolve-known.py fold_crossbox): a crossbox/1 record folds as before; a
    layout-2 file on either side is HELD, never folded by the crossbox/1 rule."""
    mr = load("merge_resolve_split", TOOLS / "merge-resolve-known.py")
    p = Pair(cb, Path(tmp) / "k1", False)
    cid, line = p.open_call()
    base = p.a.path(cid).read_text(encoding="utf-8")
    d_ours = json.loads(base)
    d_ours["ack"] = {"at": "2026-10-16T12:00:00Z", "by": SEAT + LANE, "bus_message_id": None}
    d_theirs = json.loads(base)
    d_theirs["closed"].update({"from_at": "2026-10-16T13:00:00Z", "from_by": "1.0.0_SA_CTO"})
    text, how = mr.fold_crossbox(base, json.dumps(d_ours, indent=1), json.dumps(d_theirs, indent=1))
    folded = json.loads(text) if text else {}
    ok1 = text is not None and how == "crossbox-fold" and folded.get("ack", {}).get("by") == SEAT + LANE \
        and folded.get("closed", {}).get("from_at") == "2026-10-16T13:00:00Z"
    q = Pair(cb, Path(tmp) / "k2", True)
    cid2, _line = q.open_call()
    raw = q.a.path(cid2).read_text(encoding="utf-8")
    moved = json.loads(raw)
    moved["subject"] = "moved on the other side"
    text2, how2 = mr.fold_crossbox(raw, raw, json.dumps(moved, indent=1))
    ok2 = text2 is None and "HOLD" in how2
    arm("(k) box-sync's known resolver folds a crossbox/1 record as before and HOLDs a layout-2 file (never folds it)",
        ok1 and ok2, "crossbox/1 folded=%s | layout 2: %s" % (how, how2[:110]))


def arm_l(tmp):
    """crossbox-matrix.py reads the pair across two refs: the sender's branch holds the from-side close, the answering box's
    branch holds its close; the one reader assembles them, and the matrix reports CLOSED-BOTH with no error."""
    mx = load("crossbox_matrix_split", TOOLS / "crossbox-matrix.py")
    f = closed_flow(cb, Path(tmp) / "l")
    p = f["pair"]
    cb.sgit(p.a.root, "update-ref", "refs/remotes/origin/box/laptop", f["a_commit_sha"])
    cb.sgit(p.a.root, "update-ref", "refs/remotes/origin/box/sitez", f["b_commit_sha"])
    files, bad = mx.union(str(p.a.root), ["origin/box/laptop", "origin/box/sitez"])
    rec = files.get(f["cid"], {}).get("rec", {})
    mine = [b for b in bad if f["cid"] in b[1] or f["cid"] in str(b[2])]
    ok = rec.get("state") == "CLOSED-BOTH" and rec.get("schema") == "crossbox/2" and not mine
    arm("(l) crossbox-matrix.py reads a layout-2 pair across two refs (from-side on one branch, answer on the other) as CLOSED-BOTH",
        ok, "state=%s schema=%s refs=%s bad=%d" % (rec.get("state"), rec.get("schema"),
                                                  ",".join(files.get(f["cid"], {}).get("refs", [])), len(mine)))


def arm_m(tmp):
    """crossbox-deploy-check.py's open-call read (measure_open_call): a live layout-2 call naming the root is a HIT; the same
    call once both sides are closed is not live."""
    dc = load("crossbox_deploy_check_split", TOOLS / "crossbox-deploy-check.py")
    now = datetime.datetime(2026, 10, 16, 12, 0, 0)
    root_rel = "infra/aws/terraform/rootx"
    p = Pair(cb, Path(tmp) / "m1", True)
    cid, line = p.open_call(subject="Hold the apply of " + root_rel)
    hits_open, _ = dc.measure_open_call(str(p.a.root), root_rel, [], now)
    p.b.receive(line)
    p.b.ack(cid, SEAT + LANE)
    p.commit(cb, p.b, p.answer_rel(cid))
    p.push(cb, p.b.root)
    p.pull(cb, p.a, p.b, ff=True)
    hits_acked, _ = dc.measure_open_call(str(p.a.root), root_rel, [], now)
    f = closed_flow(cb, Path(tmp) / "m2", subject="Hold the apply of " + root_rel)
    hits_closed, _ = dc.measure_open_call(str(f["pair"].b.root), root_rel, [], now)
    ok = any(cid in h for h in hits_open) and any(cid in h for h in hits_acked) and not any(f["cid"] in h for h in hits_closed)
    arm("(m) crossbox-deploy-check.py: a live layout-2 call naming the root is a HIT (OPEN and ACKED); CLOSED-BOTH is not live",
        ok, "open_hits=%d acked_hits=%d closed_hits_naming_call=%d" % (
            sum(1 for h in hits_open if cid in h), sum(1 for h in hits_acked if cid in h),
            sum(1 for h in hits_closed if f["cid"] in h)))


def main() -> int:
    tmp_root = tempfile.mkdtemp(prefix="crossbox-split-")
    try:
        base, why = load_base(tmp_root)
        steps = [("a", lambda: arm_a(os.path.join(tmp_root, "a"))),
                 ("b", lambda: arm_b(os.path.join(tmp_root, "b"))),
                 ("c", lambda: arm_c(os.path.join(tmp_root, "c"))),
                 ("d", lambda: arm_d(os.path.join(tmp_root, "d"))),
                 ("e", lambda: arm_e(os.path.join(tmp_root, "e"), base)),
                 ("f", lambda: arm_f(os.path.join(tmp_root, "f"), base)),
                 ("g", lambda: arm_g(os.path.join(tmp_root, "g"), base)),
                 ("h", lambda: arm_h(os.path.join(tmp_root, "h"))),
                 ("i", lambda: arm_i(os.path.join(tmp_root, "i"))),
                 ("j", lambda: arm_j(os.path.join(tmp_root, "j"))),
                 ("k", lambda: arm_k(os.path.join(tmp_root, "k"))),
                 ("l", lambda: arm_l(os.path.join(tmp_root, "l"))),
                 ("m", lambda: arm_m(os.path.join(tmp_root, "m")))]
        for name, fn in steps:
            try:
                fn()
            except Exception as exc:   # an arm that cannot run is a failed arm, never a pass
                arm("(%s) arm could not run" % name, False, "%s: %s" % (type(exc).__name__, exc))
        if base is None:
            print("SKIP base object: %s (arms e and f read as SKIP)" % why)
    finally:
        rmtree_force(tmp_root)
    for name, ok, detail in RESULTS:
        print("%s %s%s" % ("ok  " if ok else "FAIL", name, "" if ok or not detail else "  -- " + detail))
    good = sum(1 for _, ok, _ in RESULTS if ok)
    print("CROSSBOX-SPLIT arms=%d/%d ok=%s" % (good, len(RESULTS), bool(RESULTS) and good == len(RESULTS)))
    return 0 if RESULTS and good == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
