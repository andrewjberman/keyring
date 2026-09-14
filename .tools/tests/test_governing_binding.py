#!/usr/bin/env python3
"""FE-s-37 -- THE GOVERNING ORDER IS THE ORDER BEING FLIPPED (1.0.0_SA_CTO RULING S @942e4ff992 s.2; row S61).

Subject: `.tools/to-pipeline-gate.py` check_complete_flip() -> `.tools/proof-of-spec-check.py --governing-order`.
Built 2026-09-14 by `0.9.0_WK_IRPT_FNTEND~4` on `IRPT_FNTEND.TO-FE-s-37` (decomp cell FE-s-37).

THE DEFECT (3.0.0_SA_CVO, row IRPT_FNTEND-S61). check_complete_flip ran the checker on the instance ALONE, and the
checker read its governing order from the instance's own decomp_ref.to_ref. FE-s-29's instance with to_ref pointed at
the real round-4 order TO-FE-s-28 moved the count-bar and drives limbs to ANNOUNCE/LEGACY, and nothing named it.

EVERY FLIP ARM RUNS IN A REAL GIT INDEX ON REAL BYTES. A scratch repo under <WS>/.scratch/ borrows this repository's
object store (objects/info/alternates), sits at this worktree's HEAD and sparse-checks-out the paths the two tools
read -- so the ruling pins and every order's ADD COMMIT resolve exactly as they do here. The worktree's CURRENT gate
and checker bytes are copied in (the change under test, committed or not). One scratch commit returns FE-s-29 to the
state before its close (order <status>pending</status>; the instance and its PENDING-THIS-COMMIT artifacts absent);
the arm then stages FE-s-29's REAL close -- the order flipped to complete (M), the instance (A), each PENDING artifact
(A) -- the shape of commit 6ad371c88e, so the replay raises no PENDING sentinel of its own (the false violation S61
names for a copy).
  POSITIVE CONTROL  the instance exactly as committed -> the gate CLI admits the flip (rc 0); check_complete_flip [].
  DOCTORED to_ref   to_ref -> the committed IRPT_FNTEND.TO-FE-s-28.* order -> the gate CLI refuses (rc 1) through
                    check_complete_flip, the refusal carries the binding violation naming BOTH paths, and it is the
                    checker's ONLY violation.
  DOCTORED to_id    to_id -> FE-s-28's own <to_id> (to_ref as committed) -> refused the same way.
  BEFORE            the SAME doctored flip under the tools S61 measured (checker @9e6ed6c236, gate @8aa00e60fb) ->
                    ADMITTED. So the refusal above is the binding's, and S61's "inferred" flip is now exercised.
  FRAMES            the checker CLI called exactly as check_complete_flip calls it (bound) and as a bare seat run
                    calls it (unbound), in the same index: limb 1 (the placeholders reader), limb 2 (count-bar) and
                    limb 3 (drives) frames printed; bound runs read the FLIPPED order's boundary (NEW); the unbound
                    doctored run reproduces S61 (FE-s-28, LEGACY).
THE COMMITTED CORPUS. Every tracked IRPT_FNTEND instance, through the checker CLI UNBOUND and BOUND to its own order:
same rc, same violations, no binding violation. And the binding's cross-check alone over every tracked estate order
that has an instance beside it where check_complete_flip looks (denominator printed).
THE WHOLE-SUITE CENSUS OF RECORD (F37-AC8). Every file under .tools/tests/ that names either tool is run once. This
file is the census RUNNER and is excluded from its own census, by name (running it inside itself would recurse).

Everything runs through ONE pool of 8 workers, longest battery first (test_seeded_limb, 359 s alone at the cut).
Scratch lives under <WS>/.scratch/fe-s-37-binding and is removed at the end.
Run: python .tools/tests/test_governing_binding.py
Exit 0 = every arm as expected. Exit 1 otherwise.
"""
from __future__ import annotations

import concurrent.futures as cf
import glob
import importlib.util
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import time
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WORKSPACE = TOOLS.parent
TESTS = TOOLS / "tests"
GATE = TOOLS / "to-pipeline-gate.py"
CHECKER = TOOLS / "proof-of-spec-check.py"
PROJECT = "org/missions/D9/IRPT/IRPT_FNTEND"
TO_DIR = PROJECT + "/task-orders/"
SERIAL = "0.9.0_WK_IRPT_FNTEND~4"
SCRATCH = WORKSPACE / ".scratch" / "fe-s-37-binding"
SPARSE = (".tools", "org/standards", "org/projects", PROJECT)
PENDING = "PENDING-THIS-COMMIT"
S61_CHECKER_PIN = "9e6ed6c236"   # the checker vintage row S61 measured
S61_GATE_PIN = "8aa00e60fb"      # the gate vintage row S61 measured
TO_ID_TAG_RE = re.compile(r"<to_id>\s*([^<\s]+)\s*</to_id>")
results: list = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((name, bool(ok), detail))
    return bool(ok)


def _run(cmd: list, cwd: Path, timeout: int, env=None):
    t = time.time()
    try:
        out = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=timeout, env=env)
        return out.returncode, (out.stdout or "") + (out.stderr or ""), time.time() - t
    except subprocess.TimeoutExpired:
        return 124, "TIMEOUT after %d s" % timeout, time.time() - t


def _ws_git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=str(WORKSPACE), capture_output=True, text=True, encoding="utf-8",
                         errors="replace", timeout=120)
    if out.returncode != 0:
        raise RuntimeError("git %s rc=%d: %s" % (" ".join(args[:2]), out.returncode, out.stderr.strip()[:200]))
    return out.stdout


def _show(spec: str) -> bytes:
    out = subprocess.run(["git", "show", spec], cwd=str(WORKSPACE), capture_output=True, timeout=120)
    if out.returncode != 0:
        raise RuntimeError("git show %s rc=%d" % (spec, out.returncode))
    return out.stdout


def _order(stem: str) -> str:
    hits = [p for p in _ws_git("ls-files", "--", TO_DIR).splitlines()
            if p.rsplit("/", 1)[-1].startswith("IRPT_FNTEND.TO-%s." % stem)]
    if len(hits) != 1:
        raise RuntimeError("expected one committed order for %s, found %d" % (stem, len(hits)))
    return hits[0]


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _rm_ro(func, path, _exc):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:  # noqa: BLE001 -- a scratch leftover is not a verdict
        pass


# ---- the scratch repo: a REAL git index over this repository's objects ----------------------------------------

def _sgit(repo: Path, *args: str) -> str:
    out = subprocess.run(["git", "-c", "core.autocrlf=false", "-c", "core.hooksPath=" + str(repo / ".git" / "nohooks"),
                          *args], cwd=str(repo), capture_output=True, text=True, encoding="utf-8", errors="replace",
                         timeout=180)
    if out.returncode != 0:
        raise RuntimeError("scratch git %s rc=%d: %s" % (" ".join(args[:2]), out.returncode, out.stderr.strip()[:200]))
    return out.stdout


def _repo(name: str, head: str, common: str, tools: dict) -> Path:
    repo = SCRATCH / name
    repo.mkdir(parents=True)
    _sgit(repo, "init", "-q", "-b", "main")
    for k, val in (("core.autocrlf", "false"), ("user.name", "battery"), ("user.email", "battery@opal.agent")):
        _sgit(repo, "config", k, val)
    (repo / ".git" / "objects" / "info").mkdir(parents=True, exist_ok=True)
    # write_bytes, never write_text: text mode on Windows writes CRLF and git then reads the path as `objects\r`
    (repo / ".git" / "objects" / "info" / "alternates").write_bytes((common + "/objects\n").encode("utf-8"))
    _sgit(repo, "update-ref", "refs/heads/main", head)
    _sgit(repo, "sparse-checkout", "set", "--cone", *SPARSE)
    _sgit(repo, "read-tree", "-mu", "HEAD")
    for fname, data in tools.items():
        (repo / ".tools" / fname).write_bytes(data)
    return repo


def _flip_fixture(name, head, common, tools, fx, inst_bytes) -> tuple:
    """A repo in which FE-s-29 stands just before its close, with its REAL close staged. Returns (repo, staged)."""
    repo = _repo(name, head, common, tools)
    order_rel, inst_rel = fx["order"], fx["inst"]
    (repo / order_rel).write_bytes(fx["order_pending"])
    _sgit(repo, "rm", "-q", "--", inst_rel, *fx["pending"])
    _sgit(repo, "add", "--", order_rel)
    _sgit(repo, "commit", "-q", "--no-verify", "-m", "FE-s-29 before its close (battery fixture)")
    (repo / order_rel).write_bytes(fx["order_bytes"])
    (repo / inst_rel).write_bytes(inst_bytes)
    for p, data in fx["pending"].items():
        (repo / p).write_bytes(data)
    _sgit(repo, "add", "--", order_rel, inst_rel, *fx["pending"])
    staged = {}
    for ln in _sgit(repo, "diff", "--cached", "--name-status").splitlines():
        if ln.strip():
            staged[ln.split("\t")[-1]] = ln.split("\t")[0]
    return repo, staged


def _gate_cli(repo: Path, paths: list):
    env = dict(os.environ)
    env["OPAL_AGENT_SERIAL"] = SERIAL
    env.pop("STAGED", None)
    return _run([sys.executable, str(repo / ".tools" / "to-pipeline-gate.py"), *paths], repo, 400, env)


def _ccf_direct(repo: Path, order_rel: str, tag: str):
    """check_complete_flip called as a FUNCTION, from the scratch repo's own gate bytes."""
    t = time.time()
    mod = _load(repo / ".tools" / "to-pipeline-gate.py", "gate_fe_s_37_" + tag)
    return mod.check_complete_flip(str(repo), order_rel), time.time() - t


def _checker_cli(root: Path, inst_rel: str, bound: str | None):
    """The checker CLI. Bound, exactly the argv check_complete_flip builds (instance, --governing-order, order)."""
    cmd = [sys.executable, str(root / ".tools" / "proof-of-spec-check.py"), str(root / inst_rel)]
    if bound:
        cmd += ["--governing-order", bound]
    return _run(cmd, root, 400)


def _viol(out: str) -> list:
    return [ln.strip()[len("VIOLATION: "):] for ln in out.splitlines() if ln.strip().startswith("VIOLATION: ")]


def _frame(out: str, prefix: str):
    return next((ln.strip() for ln in out.splitlines() if ln.strip().startswith(prefix)), None)


def _last(out: str) -> str:
    lines = [ln.rstrip() for ln in out.splitlines() if ln.strip()]
    return lines[-1][:150] if lines else "(no output)"


# ---- the corpus and the census domains -------------------------------------------------------------------------

def _irpt_corpus() -> list:
    rows = []
    for ip in sorted(p for p in _ws_git("ls-files", "--", PROJECT + "/deliverables/").splitlines()
                     if p.endswith(".proof_of_spec.json")):
        own = TO_DIR + ip.rsplit("/", 1)[-1][:-len(".proof_of_spec.json")] + ".md"
        rows.append((ip, own))
    return rows


def _batteries():
    me = Path(__file__).resolve()
    pat = re.compile(r"proof[-_]of[-_]spec[-_]check|to[-_]pipeline[-_]gate")
    files = sorted(p for p in TESTS.rglob("*.py") if "__pycache__" not in p.parts)
    named = [p for p in files if pat.search(p.read_text(encoding="utf-8", errors="replace"))]
    run = [p for p in named if p.resolve() != me]
    # longest first (measured at the cut), so the pool's tail is not one 359 s battery started last
    run.sort(key=lambda p: (p.name != "test_seeded_limb.py", p.name))
    return files, named, run


def _estate_binding_census():
    """The binding cross-check ALONE, in-process, over every tracked order that has an instance where
    check_complete_flip looks for one (the same search, both roots)."""
    posc = _load(CHECKER, "posc_fe_s_37")
    gate = _load(GATE, "gate_fe_s_37_census")
    tracked = _ws_git("ls-files").splitlines()
    orders = [p for p in tracked if gate.TO_PATH_RE.search(p)]
    n_with, refused, unreadable = 0, [], 0
    for rel in orders:
        stem = rel.rsplit("/", 1)[-1].rsplit(".md", 1)[0]
        names = (stem + ".proof_of_spec.json", stem + "_PROOF_OF_SPEC.json")
        to_dir = rel.rsplit("/", 1)[0]
        if to_dir.endswith("/task-orders"):
            cands = [c for n in names for c in glob.glob(os.path.join(str(WORKSPACE), to_dir[:-len("/task-orders")],
                                                                     "deliverables", "*", n))]
        else:
            cands = [os.path.join(str(WORKSPACE), to_dir.replace("task_orders", "deliverables"), n) for n in names]
        inst = next((c for c in cands if os.path.isfile(c)), None)
        if inst is None:
            continue
        n_with += 1
        try:
            with open(inst, "r", encoding="utf-8") as fh:
                doc = json.load(fh)
        except Exception:  # noqa: BLE001
            unreadable += 1
            continue
        v, _f = posc.governing_binding_check(doc, rel)
        if v:
            refused.append((rel, v[0][:220]))
    return len(orders), n_with, refused, unreadable


def main() -> int:
    t0 = time.time()
    shutil.rmtree(SCRATCH, onerror=_rm_ro)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    pool = cf.ThreadPoolExecutor(max_workers=8)
    try:
        # ---- 1. the whole-suite census is submitted FIRST: it is the long pole ----
        files, named, run = _batteries()
        bat_futs = [(p, pool.submit(_run, [sys.executable, str(p)], WORKSPACE, 560)) for p in run]

        # ---- 2. the flip fixtures, built from REAL committed bytes ----
        head = _ws_git("rev-parse", "HEAD").strip()
        common = _ws_git("rev-parse", "--path-format=absolute", "--git-common-dir").strip()
        f29, f28 = _order("FE-s-29"), _order("FE-s-28")
        stem29 = f29.rsplit("/", 1)[-1][:-3]
        inst_rel = "%s/deliverables/%s/%s.proof_of_spec.json" % (PROJECT, SERIAL, stem29)
        order_bytes = _show("HEAD:" + f29)
        inst_bytes = _show("HEAD:" + inst_rel)
        inst_doc = json.loads(inst_bytes.decode("utf-8"))
        pending = {a["path_or_key"]: _show("HEAD:" + a["path_or_key"]) for a in inst_doc.get("artifacts_produced", [])
                   if a.get("commit_or_etag") == PENDING and a.get("kind") != "s3_object"}
        f28_id = TO_ID_TAG_RE.search(_show("HEAD:" + f28).decode("utf-8", "replace")).group(1)
        n_status = order_bytes.count(b"<status>complete</status>")
        check("premise: FE-s-29's committed order carries exactly one <status>complete</status>", n_status == 1)
        check("premise: FE-s-29's committed instance names its own order in to_ref",
              inst_doc.get("decomp_ref", {}).get("to_ref") == f29)
        old_ref = ('"to_ref": "%s"' % f29).encode()
        old_id = ('"to_id": "%s"' % inst_doc.get("to_id")).encode()
        check("premise: the doctoring edits one byte span each (to_ref once, to_id once)",
              inst_bytes.count(old_ref) == 1 and inst_bytes.count(old_id) == 1)
        doctored_ref = inst_bytes.replace(old_ref, ('"to_ref": "%s"' % f28).encode())
        doctored_id = inst_bytes.replace(old_id, ('"to_id": "%s"' % f28_id).encode())
        fx = {"order": f29, "inst": inst_rel, "order_bytes": order_bytes, "pending": pending,
              "order_pending": order_bytes.replace(b"<status>complete</status>", b"<status>pending</status>")}
        now = {"to-pipeline-gate.py": GATE.read_bytes(), "proof-of-spec-check.py": CHECKER.read_bytes()}
        before = {"to-pipeline-gate.py": _show("%s:.tools/to-pipeline-gate.py" % S61_GATE_PIN),
                  "proof-of-spec-check.py": _show("%s:.tools/proof-of-spec-check.py" % S61_CHECKER_PIN)}
        flip_paths = [f29, inst_rel, *pending]
        arms = {}
        for tag, tools, ib in (("control", now, inst_bytes), ("doctored-ref", now, doctored_ref),
                               ("doctored-id", now, doctored_id), ("before", before, doctored_ref)):
            arms[tag] = _flip_fixture(tag, head, common, tools, fx, ib)
        jobs = {
            ("control", "gate"): pool.submit(_gate_cli, arms["control"][0], flip_paths),
            ("control", "ccf"): pool.submit(_ccf_direct, arms["control"][0], f29, "control"),
            ("control", "bound"): pool.submit(_checker_cli, arms["control"][0], inst_rel, f29),
            ("doctored-ref", "gate"): pool.submit(_gate_cli, arms["doctored-ref"][0], flip_paths),
            ("doctored-ref", "ccf"): pool.submit(_ccf_direct, arms["doctored-ref"][0], f29, "doctored"),
            ("doctored-ref", "bound"): pool.submit(_checker_cli, arms["doctored-ref"][0], inst_rel, f29),
            ("doctored-ref", "unbound"): pool.submit(_checker_cli, arms["doctored-ref"][0], inst_rel, None),
            ("doctored-id", "gate"): pool.submit(_gate_cli, arms["doctored-id"][0], flip_paths),
            ("before", "gate"): pool.submit(_gate_cli, arms["before"][0], flip_paths),
        }

        # ---- 3. the committed corpus, unbound and bound ----
        corpus = _irpt_corpus()
        cor_futs = [(ip, own, pool.submit(_checker_cli, WORKSPACE, ip, None), pool.submit(_checker_cli, WORKSPACE, ip, own))
                    for ip, own in corpus]
        estate = _estate_binding_census()

        # ================================ the flip path ================================
        want = {f29: "M", inst_rel: "A", **{p: "A" for p in pending}}
        print("FLIP FIXTURE: a real git index over this repository's objects at %s; FE-s-29's close staged as %s "
              "(%d PENDING artifact(s) staged with it)" % (head[:10], ", ".join("%s %s" % (s, p.rsplit("/", 1)[-1])
                                                             for p, s in sorted(arms["control"][1].items())), len(pending)))
        for tag in arms:
            check("fixture %s: the index stages exactly the real close (order M, instance and PENDING artifacts A)" % tag,
                  arms[tag][1] == want, str(arms[tag][1]))

        rc, out, secs = jobs[("control", "gate")].result()
        ccf, _s = jobs[("control", "ccf")].result()
        brc, bout, _s2 = jobs[("control", "bound")].result()
        ok_ctl = rc == 0 and "NOT VALID" not in out and ccf == [] and brc == 0 and "VALID (rc=0)" in bout
        print("  gate CLI on the committed close: rc=%d (%.0f s) -- %s" % (rc, secs, _last(out)))
        print("  check_complete_flip() on the committed close: %d refusal line(s)" % len(ccf))
        print("POSITIVE CONTROL, FE-s-29 AS COMMITTED: %s" % ("VALID (gate rc=0; check_complete_flip []; the bound "
                                                           "checker reads VALID)" if ok_ctl else "REFUSED -- see above"))
        check("POSITIVE CONTROL: the committed close is admitted through the flip path", ok_ctl)

        rc, out, secs = jobs[("doctored-ref", "gate")].result()
        ccf, _s = jobs[("doctored-ref", "ccf")].result()
        brc, bout, _s2 = jobs[("doctored-ref", "bound")].result()
        urc, uout, _s3 = jobs[("doctored-ref", "unbound")].result()
        gate_bind = [ln.strip() for ln in out.splitlines() if "governing-binding" in ln]
        ccf_bind = [x for x in ccf if "governing-binding" in x]
        only = _viol(bout)
        ok_ref = rc == 1 and bool(gate_bind) and bool(ccf_bind)
        print("  gate CLI on the doctored close (to_ref -> %s): rc=%d (%.0f s)" % (f28.rsplit("/", 1)[-1], rc, secs))
        for ln in out.splitlines():
            if ln.strip().startswith(f29 + ":"):
                print("    gate refusal: %s" % ln.strip()[:900])
        print("  check_complete_flip() on the doctored close: %d refusal line(s), %d carry the binding violation"
              % (len(ccf), len(ccf_bind)))
        print("DOCTORED to_ref THROUGH THE FLIP PATH: %s" % (
            "REFUSED (gate CLI rc=1 and check_complete_flip() both carry the binding violation)" if ok_ref
            else "NOT REFUSED BY THE BINDING (rc=%d)" % rc))
        check("DOCTORED to_ref: refused by the gate CLI AND by check_complete_flip(), both carrying the binding", ok_ref)
        both = bool(ccf_bind) and f29 in ccf_bind[0] and f28 in ccf_bind[0]
        print("THE REFUSAL NAMES BOTH PATHS: %s" % ("yes" if both else "no"))
        print("  the violation: %s" % (ccf_bind[0].split("instance VIOLATION: ", 1)[-1] if ccf_bind else "(none)"))
        check("the binding violation names the flipped order's path AND the path to_ref declared", both)
        ok_only = len(only) == 1 and "governing-binding" in only[0]
        print("  the bound checker's violations on the doctored close: %d, binding: %d -- %s" % (
            len(only), sum("governing-binding" in x for x in only),
            "the binding is the ONLY violation (no PENDING sentinel: the replay staged the result file)" if ok_only
            else "; ".join(x[:120] for x in only)))
        check("the binding is the doctored close's ONLY violation (a real close raises no PENDING sentinel)", ok_only)

        lim1 = _frame(bout, "invocation-frame:")
        lim1b = _frame(bout, "invocation-alignment")
        ok_l1 = bool(lim1) and f29 in lim1
        if ok_l1:
            print("LIMB 1 FRAME ON THE DOCTORED ARM: %s" % lim1)
            print("  %s" % (lim1b or "(no invocation-alignment line)"))
        else:
            print("LIMB 1 FRAME ABSENT ON THE DOCTORED ARM (or it read another order): %s" % lim1)
        check("limb 1's frame is printed on the doctored arm and reads the flipped order", ok_l1)

        frames = []
        for tag, text in (("bound, as committed", jobs[("control", "bound")].result()[1]), ("bound, doctored", bout)):
            for limb, prefix in (("limb 2 count-bar", "count-bar-frame:"), ("limb 3 drives", "drives-frame:")):
                fr = _frame(text, prefix) or ""
                good = f29 in fr and "-> NEW" in fr and "mode ENFORCE" in fr and f28 not in fr
                frames.append(good)
                print("  %-4s %s, %s: %s" % ("NEW" if good else "NOT", tag, limb, fr[:400]))
        print("LIMBS 2 AND 3 READ THE FLIPPED ORDER'S BOUNDARY: %d of %d" % (sum(frames), len(frames)))
        check("limbs 2 and 3 read ENFORCE/NEW from the flipped order on the bound and the doctored run", all(frames))
        contrast = []
        for limb, prefix in (("limb 2 count-bar", "count-bar-frame:"), ("limb 3 drives", "drives-frame:")):
            fr = _frame(uout, prefix) or ""
            legacy = f28 in fr and "-> LEGACY" in fr and "ANNOUNCE" in fr
            contrast.append(legacy)
            print("  %-6s unbound, doctored, %s: %s" % ("LEGACY" if legacy else "other", limb, fr[:400]))
        unb = _frame(uout, "governing-binding:") or ""
        print("  unbound doctored run (a seat's bare CLI, S61 reproduced): limbs 2 and 3 read the to_ref order LEGACY "
              "%d of %d; rc=%d; its frame: %s" % (sum(contrast), len(contrast), urc, unb[:200]))
        check("the unbound doctored run still reads the to_ref order (S61 reproduced) and SAYS it is unbound",
              all(contrast) and unb.startswith("governing-binding: UNBOUND"))

        rc, out, secs = jobs[("doctored-id", "gate")].result()
        id_bind = [ln.strip() for ln in out.splitlines() if "governing-binding" in ln and "to_id" in ln]
        ok_id = rc == 1 and bool(id_bind)
        print("DOCTORED to_id THROUGH THE FLIP PATH (to_id -> %s, to_ref as committed): %s" % (
            f28_id, "REFUSED (rc=1)" if ok_id else "NOT REFUSED BY THE BINDING (rc=%d)" % rc))
        if id_bind:
            print("  %s" % id_bind[0][:700])
        check("DOCTORED to_id: refused through the gate CLI by the binding", ok_id)

        rc, out, secs = jobs[("before", "gate")].result()
        ok_before = rc == 0
        print("BEFORE (checker @%s, gate @%s -- the vintages S61 measured), the SAME doctored close: %s -- %s" % (
            S61_CHECKER_PIN, S61_GATE_PIN, "ADMITTED (rc=0)" if ok_before else "rc=%d" % rc, _last(out)))
        check("BEFORE: the same doctored close is ADMITTED by the tools S61 measured (the refusal is the binding's)",
              ok_before)

        # ================================ the committed corpus ================================
        n_same = n_nobind = n_frames = 0
        print("COMMITTED IRPT_FNTEND INSTANCES, UNBOUND vs BOUND TO THEIR OWN ORDER (%d tracked):" % len(corpus))
        n_own = 0
        for ip, own, fu, fb in cor_futs:
            try:
                tr = json.loads((WORKSPACE / ip).read_text(encoding="utf-8")).get("decomp_ref", {}).get("to_ref")
            except Exception:  # noqa: BLE001
                tr = None
            n_own += tr == own
            u, b = fu.result(), fb.result()
            same = u[0] == b[0] and sorted(_viol(u[1])) == sorted(_viol(b[1]))
            nobind = not any("governing-binding" in x for x in _viol(b[1]))
            fr_ok = "governing-binding: BOUND" in b[1] and "governing-binding: UNBOUND" in u[1]
            n_same += same
            n_nobind += nobind
            n_frames += fr_ok
            print("  %-4s %-62s unbound rc=%d bound rc=%d violations %d/%d%s" % (
                "OK" if same and nobind and fr_ok else "DIFF", ip.rsplit("/", 1)[-1][:62], u[0], b[0],
                len(_viol(u[1])), len(_viol(b[1])), "" if nobind else " BINDING-REFUSED"))
        print("CORPUS: %d of %d name their own order in to_ref; bound == unbound (rc and violations) %d of %d; refused "
              "by the binding %d of %d; each run prints its binding frame %d of %d"
              % (n_own, len(corpus), n_same, len(corpus), len(corpus) - n_nobind, len(corpus), n_frames, len(corpus)))
        check("every committed IRPT_FNTEND instance reads the same bound and unbound, and the binding refuses none",
              n_same == len(corpus) and n_nobind == len(corpus) and n_frames == len(corpus) and len(corpus) > 0)
        n_orders, n_with, refused, unreadable = estate
        print("ESTATE: the binding's cross-check over every tracked order with an instance where check_complete_flip "
              "looks: refused %d of %d (%d tracked orders scanned; %d instance(s) unreadable as JSON)"
              % (len(refused), n_with, n_orders, unreadable))
        for rel, why in refused[:10]:
            print("  REFUSED %s -- %s" % (rel, why))
        check("the binding refuses no committed estate instance whose fields name its own order", not refused)

        # ================================ the whole-suite census ================================
        green = 0
        print("CENSUS DOMAIN: %d .py file(s) under .tools/tests/; %d name proof-of-spec-check or to-pipeline-gate; "
              "%d run (this file, the census runner, excluded by name)" % (len(files), len(named), len(run)))
        for p, fut in bat_futs:
            rc, out, secs = fut.result()
            green += rc == 0
            print("  %-5s rc=%-3d %4.0f s  %-44s %s" % ("GREEN" if rc == 0 else "RED", rc, secs, p.name, _last(out)))
        print("EVERY .tools BATTERY THAT CALLS EITHER TOOL: %d of %d green" % (green, len(run)))
        check("every battery that calls either tool is green with the change applied", green == len(run) and run)
    finally:
        pool.shutdown(wait=True)
        shutil.rmtree(SCRATCH, onerror=_rm_ro)

    failed = [r for r in results if not r[1]]
    for name, ok, detail in results:
        print("  %-4s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail[:200]) if (detail and not ok) else ""))
    print("governing-binding battery: %d of %d arm(s) as expected (%.0f s wall)" % (
        len(results) - len(failed), len(results), time.time() - t0))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
