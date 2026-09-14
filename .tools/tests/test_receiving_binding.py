#!/usr/bin/env python3
"""FE-s-43 -- THE L7 -> L8 RECEIVING ROUTE BINDS THE GOVERNING ORDER (1.0.0_SA_CTO RULING AA @4713211d87 s.3;
row IRPT_FNTEND-W4-S14, graduated by 3.0.0_SA_CVO in C-S90).

Subject: `.tools/receiving-check.py` -- its CLI and its run_one() -- dispatching a proof-of-spec instance to
`.tools/proof-of-spec-check.py --governing-order <the order it was handed with>`.
Built 2026-09-14 by `0.9.0_WK_IRPT_FNTEND~4` on `IRPT_FNTEND.TO-FE-s-43` (decomp cell FE-s-43).

THE DEFECT. The proof route built [instance] and nothing else, and run_one returned ACCEPT on rc=0, so the receiving
verdict came from whatever order the instance's own decomp_ref.to_ref named. RULING S (FE-s-37) bound the flip path;
the receiving route stayed unbound.

EVERY ARM RUNS IN A REAL GIT INDEX ON REAL BYTES (RULING AC). A scratch repo under <WS>/.scratch/ borrows this
repository's object store (objects/info/alternates), sits at this worktree's HEAD and sparse-checks-out the paths the
tools read. The worktree's CURRENT receiving-check.py and proof-of-spec-check.py bytes are copied in. One scratch
commit returns FE-s-29 to the state before its close; a second commits FE-s-29's REAL close -- the order flipped to
complete, the instance, its PENDING-THIS-COMMIT artifact -- the shape of 6ad371c88e. That is what the CVO RECEIVES at
L8: a committed close. The two fixtures differ ONLY in the instance's to_ref bytes.
  POSITIVE CONTROL   the committed instance, received with its own order     -> ACCEPT (CLI rc 0 and run_one)
  DOCTORED to_ref    to_ref -> the committed IRPT_FNTEND.TO-FE-s-28.* order,
                     received with FE-s-29's own order                       -> HAND BACK (CLI rc 1 and run_one); the
                     binding violation names both paths and is the checker's ONLY violation
  UNBOUND            the SAME doctored instance, received with no order      -> NOT-BOUND; nothing ran
  BEFORE             the SAME doctored instance through receiving-check @%s (the cut) -> ACCEPT: the steered verdict
                     the ruling exists for, so the refusals above are the binding's
  OTHER ROUTES       each non-proof route classifies a committed example of its own artifact type and builds the same
                     argv as at the cut -- with and without an order handed over
The census of record for every battery calling either tool is FE-s-37's test_governing_binding.py (F43-AC8); this
file names proof-of-spec-check, so that census runs it too.

Scratch lives under <WS>/.scratch/fe-s-43-receiving/<pid> (a concurrent run -- the census -- owns its own) and is
removed at the end.
Run: python .tools/tests/test_receiving_binding.py
Exit 0 = every arm as expected. Exit 1 otherwise.
"""
from __future__ import annotations

import concurrent.futures as cf
import importlib.util
import json
import os
import shutil
import stat
import subprocess
import sys
import time
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WORKSPACE = TOOLS.parent
RECEIVING = TOOLS / "receiving-check.py"
CHECKER = TOOLS / "proof-of-spec-check.py"
PROJECT = "org/missions/D9/IRPT/IRPT_FNTEND"
TO_DIR = PROJECT + "/task-orders/"
SERIAL = "0.9.0_WK_IRPT_FNTEND~4"
SCRATCH = WORKSPACE / ".scratch" / "fe-s-43-receiving" / str(os.getpid())
SPARSE = (".tools", "org/standards", "org/projects", PROJECT)
PENDING = "PENDING-THIS-COMMIT"
CUT = "edac45e48c"   # the issuer's measurement of the receiving route (the order's cut)
BINDING = "governing-binding"
# One committed example per NON-PROOF route, each named here (never derived from the table under test) and each
# verified present at HEAD before it is classified.
EXAMPLES = (
    ("PRD addendum", "org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD_ADDENDUM_01.md"),
    ("step-4 PRD", PROJECT + "/prd/IRPT_FNTEND_PRD.md"),
    ("task order", None),   # FE-s-28's committed order, resolved below
    ("surprise-channel row set", PROJECT + "/surprise-channel/investigations/INVESTIGATION_v1.md"),
    ("register row", PROJECT + "/project.json"),
)
results: list = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((name, bool(ok), detail))
    return bool(ok)


def _run(cmd: list, cwd: Path, timeout: int):
    t = time.time()
    env = dict(os.environ)
    env["OPAL_AGENT_SERIAL"] = SERIAL
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


def _at_head(rel: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", "HEAD:" + rel], cwd=str(WORKSPACE),
                          capture_output=True, timeout=60).returncode == 0


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


def _close_fixture(name: str, head: str, common: str, tools: dict, fx: dict, inst_bytes: bytes) -> Path:
    """A repo in which FE-s-29's REAL close is COMMITTED on top of a commit that returns it to just before that close.
    The instance committed is `inst_bytes` (as committed, or doctored); nothing else differs between fixtures."""
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
    _sgit(repo, "commit", "-q", "--no-verify", "-m", "FE-s-29 close (battery fixture)")
    return repo


def _receiving_cli(repo: Path, tool: str, inst_rel: str, order_rel: str | None):
    """The receiving CLI from the fixture's root, paths RELATIVE to it (the receiver's natural call)."""
    cmd = [sys.executable, str(repo / ".tools" / tool), inst_rel]
    if order_rel:
        cmd += ["--governing-order", order_rel]
    return _run(cmd, repo, 400)


def _receiving_run_one(repo: Path, inst_rel: str, order_rel: str | None, tag: str):
    """run_one() called as a FUNCTION from the fixture's own receiving-check bytes, absolute paths."""
    mod = _load(repo / ".tools" / "receiving-check.py", "receiving_fe_s_43_" + tag)
    if order_rel is None:
        return mod.run_one(str(repo / inst_rel))
    return mod.run_one(str(repo / inst_rel), governing_order=str(repo / order_rel))


def _verdict_row(out: str, inst_rel: str):
    """The per-artifact verdict word the CLI printed for this instance (first token of its row)."""
    for ln in out.splitlines():
        s = ln.strip()
        if s.endswith(inst_rel) and not s.startswith("|"):
            for word in ("ACCEPT", "HAND BACK", "NOT-BOUND", "UNCHECKED"):
                if s.startswith(word):
                    return word
    return None


def _viol(body: str) -> list:
    return [ln.strip()[len("VIOLATION: "):] for ln in body.splitlines() if ln.strip().startswith("VIOLATION: ")]


def _unwrap(out: str) -> str:
    """The owning tool's output as the CLI printed it, gutters removed: a `      | ` line opens a tool line and a
    `      :   ` line continues the one above (the CLI wraps, never truncates), so a wrapped violation reads whole."""
    joined = []
    for ln in out.splitlines():
        if ln.startswith("      :   ") and joined:
            joined[-1] += " " + ln[len("      :   "):]
        elif ln.startswith("      | "):
            joined.append(ln[len("      | "):])
        else:
            joined.append(ln)
    return "\n".join(joined)


def _last(out: str) -> str:
    lines = [ln.rstrip() for ln in out.splitlines() if ln.strip()]
    return lines[-1][:160] if lines else "(no output)"


def main() -> int:
    t0 = time.time()
    shutil.rmtree(SCRATCH, onerror=_rm_ro)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    pool = cf.ThreadPoolExecutor(max_workers=8)
    try:
        # ---- the fixtures, built from REAL committed bytes ----
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
        check("premise: FE-s-29's committed order carries exactly one <status>complete</status>",
              order_bytes.count(b"<status>complete</status>") == 1)
        check("premise: FE-s-29's committed instance names its own order in to_ref",
              inst_doc.get("decomp_ref", {}).get("to_ref") == f29)
        old_ref = ('"to_ref": "%s"' % f29).encode()
        check("premise: the doctoring edits one byte span (to_ref, once)", inst_bytes.count(old_ref) == 1)
        doctored = inst_bytes.replace(old_ref, ('"to_ref": "%s"' % f28).encode())
        fx = {"order": f29, "inst": inst_rel, "order_bytes": order_bytes, "pending": pending,
              "order_pending": order_bytes.replace(b"<status>complete</status>", b"<status>pending</status>")}
        cut_bytes = _show("%s:.tools/receiving-check.py" % CUT)
        tools = {"receiving-check.py": RECEIVING.read_bytes(), "proof-of-spec-check.py": CHECKER.read_bytes(),
                 "receiving-check-at-cut.py": cut_bytes}
        ctl = _close_fixture("control", head, common, tools, fx, inst_bytes)
        doc = _close_fixture("doctored", head, common, tools, fx, doctored)
        print("FIXTURES: two real git indexes over this repository's objects at %s; FE-s-29's close committed on top "
              "(order M, instance A, %d PENDING artifact(s) A); they differ only in the instance's to_ref"
              % (head[:10], len(pending)))

        jobs = {
            "ctl-cli": pool.submit(_receiving_cli, ctl, "receiving-check.py", inst_rel, f29),
            "ctl-fn": pool.submit(_receiving_run_one, ctl, inst_rel, f29, "ctl"),
            "doc-cli": pool.submit(_receiving_cli, doc, "receiving-check.py", inst_rel, f29),
            "doc-fn": pool.submit(_receiving_run_one, doc, inst_rel, f29, "doc"),
            "unb-cli": pool.submit(_receiving_cli, doc, "receiving-check.py", inst_rel, None),
            "unb-fn": pool.submit(_receiving_run_one, doc, inst_rel, None, "unb"),
            "cut-cli": pool.submit(_receiving_cli, doc, "receiving-check-at-cut.py", inst_rel, None),
            "self": pool.submit(_run, [sys.executable, str(RECEIVING), "--self-test"], WORKSPACE, 120),
        }

        # ================================ the positive control ================================
        rc, out, secs = jobs["ctl-cli"].result()
        fv, _fl, fbody = jobs["ctl-fn"].result()
        row = _verdict_row(out, inst_rel)
        ok_ctl = rc == 0 and row == "ACCEPT" and fv == "ACCEPT" and "VALID (rc=0)" in fbody
        print("  receiving CLI, committed instance + its own order: rc=%d (%.0f s), row %s -- %s"
              % (rc, secs, row, _last(out)))
        print("  run_one(), committed instance + its own order: %s" % fv)
        print("POSITIVE CONTROL, FE-s-29 AS COMMITTED, BOUND: %s" % ("ACCEPT" if ok_ctl else "NOT ACCEPT -- see above"))
        check("POSITIVE CONTROL: the committed instance with its own order reads ACCEPT (CLI and run_one)", ok_ctl)

        # ================================ the doctored arm ================================
        rc, out, secs = jobs["doc-cli"].result()
        fv, _fl, fbody = jobs["doc-fn"].result()
        row = _verdict_row(out, inst_rel)
        fn_bind = [x for x in _viol(fbody) if x.startswith(BINDING)]
        cli_bind = [x for x in _viol(_unwrap(out)) if x.startswith(BINDING)]
        ok_doc = rc == 1 and row == "HAND BACK" and fv == "HAND BACK" and bool(fn_bind) and bool(cli_bind)
        print("  receiving CLI, to_ref -> %s, handed FE-s-29's own order: rc=%d (%.0f s), row %s"
              % (f28.rsplit("/", 1)[-1], rc, secs, row))
        print("  run_one(), the same: %s; binding violation(s) in its body: %d" % (fv, len(fn_bind)))
        print("DOCTORED to_ref, BOUND THROUGH THE RECEIVING ROUTE: %s" % (
            "HAND BACK" if ok_doc else "NOT HANDED BACK BY THE BINDING (rc=%d, row %s, run_one %s)" % (rc, row, fv)))
        check("DOCTORED to_ref: HAND BACK through the CLI AND run_one, both carrying the binding violation", ok_doc)
        both = bool(cli_bind) and f29 in cli_bind[0] and f28 in cli_bind[0] and f29 in out and f28 in out
        print("THE HAND-BACK NAMES BOTH PATHS: %s" % ("yes" if both else "no"))
        print("  the printed violation: %s" % (cli_bind[0] if cli_bind else "(none)"))
        check("the printed hand-back carries the violation naming the order handed over AND the order to_ref declared",
              both)
        only = _viol(fbody)
        ok_only = len(only) == 1 and only[0].startswith(BINDING)
        print("  the checker's violations on the doctored close: %d, binding: %d -- %s" % (
            len(only), len(fn_bind), "the binding is the ONLY violation" if ok_only
            else "; ".join(x[:120] for x in only)))
        check("the binding is the doctored close's ONLY violation (the hand-back is the binding's)", ok_only)

        # ================================ the unbound arm ================================
        rc, out, secs = jobs["unb-cli"].result()
        fv, _fl, fbody = jobs["unb-fn"].result()
        row = _verdict_row(out, inst_rel)
        steered = any(tok in out + fbody for tok in ("VALID (rc=0)", "INVALID (rc=1)", "count-bar-frame:",
                                                     "drives-frame:", "governing-binding: UNBOUND"))
        ok_unb = rc == 1 and row == "NOT-BOUND" and fv == "NOT-BOUND" and "NOT-BOUND" in out and not steered
        print("  receiving CLI, the same doctored instance, NO order: rc=%d (%.0f s), row %s -- %s"
              % (rc, secs, row, _last(out)))
        print("  run_one(), the same with no order: %s; the checker ran: %s" % (fv, "yes" if steered else "no"))
        print("UNBOUND INSTANCE THROUGH THE RECEIVING ROUTE: %s" % (
            "NOT-BOUND" if ok_unb else "NOT NOT-BOUND (rc=%d, row %s, run_one %s, checker ran %s)"
            % (rc, row, fv, steered)))
        check("UNBOUND: the doctored instance received with no order reads NOT-BOUND, never ACCEPT, and nothing ran",
              ok_unb)

        rc, out, secs = jobs["cut-cli"].result()
        row = _verdict_row(out, inst_rel)
        ok_before = rc == 0 and row == "ACCEPT"
        print("BEFORE (receiving-check @%s, the cut), the SAME doctored instance: %s (rc=%d, %.0f s) -- %s" % (
            CUT, row, rc, secs, _last(out)))
        check("BEFORE: the cut's receiving route ACCEPTS the doctored instance (the steer the ruling names)", ok_before)

        # ================================ every other route ================================
        cut_mod = _load(SCRATCH / "control" / ".tools" / "receiving-check-at-cut.py", "receiving_fe_s_43_cut")
        now_mod = _load(RECEIVING, "receiving_fe_s_43_now")
        non_proof = [lbl for _rx, lbl, tool, _a, _h in cut_mod.ROUTES if tool != "proof-of-spec-check.py"]
        same = 0
        covered = set()
        print("OTHER ROUTES: %d non-proof route(s) in the cut's table: %s" % (len(non_proof), ", ".join(non_proof)))
        for label, rel in EXAMPLES:
            rel = rel or f28
            present = _at_head(rel)
            cut_hit = cut_mod.classify(rel)
            now_hit = now_mod.classify(rel)
            now_bound = now_mod.classify(rel, governing_order=f29)
            good = present and cut_hit is not None and cut_hit[0] == label and now_hit == cut_hit and now_bound == cut_hit
            same += good
            covered.add(label if good else None)
            print("  %-4s %-26s %-24s argv %-58s cut==now %s, cut==now-with-order %s  [%s]" % (
                "SAME" if good else "DIFF", label, (now_hit or ("", "(none)"))[1], str((now_hit or ("", "", []))[2]),
                now_hit == cut_hit, now_bound == cut_hit, rel))
        all_routes = set(non_proof) <= covered and len(EXAMPLES) == len(non_proof)
        print("EVERY OTHER ROUTE UNCHANGED: %d of %d" % (same, len(non_proof)))
        check("every non-proof route classifies its committed example and builds the cut's argv, with and without an "
              "order", same == len(non_proof) and all_routes)

        rc, out, _s = jobs["self"].result()
        print("RECEIVING SELF-TEST: rc=%d -- %s" % (rc, _last(out)))
        check("receiving-check.py --self-test holds (the binding controls included)", rc == 0 and "ALL HOLD" in out)
    finally:
        pool.shutdown(wait=True)
        shutil.rmtree(SCRATCH, onerror=_rm_ro)

    failed = [r for r in results if not r[1]]
    for name, ok, detail in results:
        print("  %-4s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail[:200]) if (detail and not ok) else ""))
    print("receiving-binding battery: %d of %d arm(s) as expected (%.0f s wall)" % (
        len(results) - len(failed), len(results), time.time() - t0))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
