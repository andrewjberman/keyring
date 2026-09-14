#!/usr/bin/env python3
"""GATE (ix) -- the OUTPUT-VOCABULARY limb of .tools/to-pipeline-gate.py: a criterion whose bar its named tool can
never print is refused when a new task order is committed.

Subject: `_output_vocabulary_violations()` and the L6 gate CLI that calls it, built 2026-09-13 by
`0.9.0_WK_IRPT_FNTEND~4` on `IRPT_FNTEND.TO-FE-s-36` (decomp cell FE-s-36; 1.0.0_SA_CTO ruling N; row S55).

EVERY ARM IS A REAL SHAPE, READ BY `git show` AT A NAMED COMMIT, STAGED AS A NEWLY ADDED ORDER IN A REAL GIT INDEX,
AND GRADED BY THE GATE'S OWN CLI -- never a string this battery chose, and never the limb's rule re-derived here.

THE REAL INDEX. Each fixture is a throwaway repository whose object store BORROWS the workspace's (git alternates;
nothing is written to the workspace) and whose HEAD and index are the commit FIXTURE_BASE -- the commit on which
round 5's wave B was seated, so every round-5 order and every tool they name is in it exactly as it was at the cut.
The orders under test are placed beside the real ones under a ZZZ_TWIN name and `git add`-ed, so `git diff --cached`
reports them as ADDED (A) -- the only scope the limb grades. The limb reads each named tool from that index.

  F28-AC6 AS ISSUED       IRPT_FNTEND.TO-FE-s-28 @b6062ad2a2 -- F28-AC6 expects `0 fail` from
                          test_proof_of_spec_alignment.py, which never prints it (:458-460). REFUSED, naming F28-AC6,
                          and no other criterion of that order is refused by this limb.
  F28-AC6 AS RE-CUT       the same order @9ab6043728 (`BATTERY PASS`): ADMITTED -- the one-line delta flips the verdict,
                          and every other refusal line of the two runs is byte-identical, so the delta is the bar.
  A RUNNER'S VOCABULARY   two real committed criteria -- `bun test <one existing file>` with `0 fail`, and `bun test
                          <dirs>` with `(?<![0-9])0 fail` (no committed criterion joins the two) -- the single file present
                          in the pinned portal commit: ADMITTED (not refused; counted as a runner's vocabulary). The
                          SAME words are refused on a python battery above.
  TARGET ABSENT           IRPT_FNTEND.TO-FE-s-36 @FIXTURE_BASE: its battery (this file) did not exist at the cut, so its
                          criteria are ANNOUNCED, not refused; control: with this file staged, the absence note goes.
  REAL ROUND-5 ORDERS     FE-s-29 .. FE-s-36 @FIXTURE_BASE, 8 files, each staged as ADDED in one gate run: 0 refused by
                          this limb, with the limb's own per-order tally printed as the denominator.

Run: python .tools/tests/test_output_vocabulary.py      Exit 0 = every arm as expected.
"""
from __future__ import annotations

import difflib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WORKSPACE = TOOLS.parent
GATE = TOOLS / "to-pipeline-gate.py"
TO_DIR = "org/missions/D9/IRPT/IRPT_FNTEND/task-orders"
F28 = TO_DIR + "/IRPT_FNTEND.TO-FE-s-28.mandatory-placeholders.md"
F36 = TO_DIR + "/IRPT_FNTEND.TO-FE-s-36.output-vocabulary.md"
AS_ISSUED, AS_RECUT = "b6062ad2a2", "9ab6043728"
FIXTURE_BASE = "0a74710f33"    # CLOUD at the wave-B seating commit: round 5 as cut, FE-s-29 drained, no FE-s-36 battery
ROUND5 = ["checker-limbs", "availability-gate", "export-under-the-gate", "holdings-under-the-gate", "fixture-reach",
          "business-date-label", "envelope-refusal", "output-vocabulary"]
SELF_REL = ".tools/tests/test_output_vocabulary.py"

PASS, FAIL = "PASS", "FAIL"
results: list = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, PASS if ok else FAIL, detail))


def _git(cwd, *args, binary=False):
    return subprocess.run(["git", "-c", "core.autocrlf=false", *args], cwd=str(cwd), capture_output=True,
                          text=not binary, encoding=None if binary else "utf-8",
                          errors=None if binary else "replace", timeout=180)


def _show(ref: str, rel: str) -> str:
    out = _git(WORKSPACE, "show", "%s:%s" % (ref, rel))
    if out.returncode != 0 or not out.stdout:
        raise RuntimeError("git show %s:%s failed (rc=%d): %s" % (ref, rel, out.returncode, out.stderr.strip()[:200]))
    return out.stdout


def _fixture(tmp: Path, name: str) -> Path:
    """A real repository: the workspace's objects borrowed, HEAD and index = FIXTURE_BASE, no checkout."""
    repo = tmp / name
    repo.mkdir(parents=True)
    _git(repo, "init", "-q")
    common = _git(WORKSPACE, "rev-parse", "--path-format=absolute", "--git-common-dir").stdout.strip()
    # write_bytes, never write_text: on Windows text mode writes CRLF and git then reads the path as `objects\r`.
    (repo / ".git" / "objects" / "info" / "alternates").write_bytes((common + "/objects\n").encode("utf-8"))
    sha = _git(WORKSPACE, "rev-parse", FIXTURE_BASE + "^{commit}").stdout.strip()
    for args in (("update-ref", "HEAD", sha), ("read-tree", "HEAD")):
        r = _git(repo, *args)
        if r.returncode != 0:
            raise RuntimeError("fixture %s: git %s failed: %s" % (name, " ".join(args), r.stderr.strip()[:200]))
    return repo


def _stage(repo: Path, rel: str, text: str) -> None:
    dst = repo / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(dst, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    r = _git(repo, "add", "--", rel)
    if r.returncode != 0:
        raise RuntimeError("git add %s failed: %s" % (rel, r.stderr.strip()[:200]))


def _twin(rel: str, tag: str) -> str:
    return rel.rsplit("/", 1)[0] + "/ZZZ_TWIN_" + tag + "." + rel.rsplit("/", 1)[1]


def _run_gate(repo: Path, rels: list):
    env = dict(os.environ)
    env["OPAL_AGENT_SERIAL"] = "2.0.0_SA_COO"   # the issuer seat, so GATE (iv) is not the story
    env.pop("STAGED", None)
    out = subprocess.run([sys.executable, str(GATE), *rels], cwd=str(repo), capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=240, env=env)
    return out.returncode, (out.stdout or "") + (out.stderr or "")


def _ov_refusals(output: str) -> list:
    """This limb's refusal lines: the gate indents each violation by four spaces."""
    return [ln.strip() for ln in output.splitlines() if ln.startswith("    ") and "-- OUTPUT-VOCABULARY:" in ln]


def _other_refusals(output: str) -> list:
    return sorted(ln.strip() for ln in output.splitlines()
                  if ln.startswith("    ") and "-- OUTPUT-VOCABULARY:" not in ln)


def _tally(output: str, rel: str):
    """The limb's own per-order tally note for `rel`, or None when the limb did not run on it."""
    for ln in output.splitlines():
        if ("NOTE: OUTPUT-VOCABULARY: %s --" % rel) in ln:
            m = re.search(r"(\d+) mechanical criteria: (\d+) evaluated and admitted, (\d+) refused, (\d+) announced, "
                          r"(\d+) not evaluated \(a runner's vocabulary\), (\d+) not evaluated", ln)
            if m:
                return dict(zip(("mech", "admitted", "refused", "announced", "runner", "other"), map(int, m.groups())))
    return None


def _portal_gitdir():
    """The portal repository's git dir, DERIVED: the main worktree (the parent of the common git dir) carries the
    portal checkout, a gitlink with its own repository. None when it cannot be read."""
    common = Path(_git(WORKSPACE, "rev-parse", "--path-format=absolute", "--git-common-dir").stdout.strip())
    out = _git(common.parent / "portal", "rev-parse", "--absolute-git-dir")
    return out.stdout.strip() if out.returncode == 0 and out.stdout.strip() else None


def _runner_specimens():
    """REAL committed criteria whose output is bun's, every target confirmed in the portal commit FIXTURE_BASE pins:
    (a) `bun test <one .test.ts file>` with a `0 fail` bar, the anchored form preferred, its file PRESENT in the portal
    commit FIXTURE_BASE pins; (b) `bun test <dirs...>` with the anchored `(?<![0-9])0 fail`. MEASURED: every (b) in the
    corpus is a round-5 order naming a directory its own worker writes, so (b) is taken with its presence COUNTED, not
    required. Returns ([(order_rel, cid, targets, bar, n_present)], n_single_anchored, n_orders)."""
    block = re.compile(r"<criterion\b([^>]*?)(?<!/)>(.*?)</criterion>", re.S)
    # One `git grep` at FIXTURE_BASE names the candidate orders; a per-file `git show` over all 359 cost minutes here.
    hits = _git(WORKSPACE, "grep", "-l", "-F", "-e", "0 fail</expect>", FIXTURE_BASE, "--", "org/missions").stdout
    files = [ln.split(":", 1)[1] for ln in hits.splitlines()
             if ":" in ln and re.search(r"/task-orders/[^/]+\.md$", ln.split(":", 1)[1])]
    pin = _git(WORKSPACE, "ls-tree", FIXTURE_BASE, "portal").stdout.split()
    pg = _portal_gitdir()
    single, multi, n_sa = None, None, 0
    for rel in sorted(files):
        for m in block.finditer(_show(FIXTURE_BASE, rel)):
            inv = re.search(r"<invocation>(.*?)</invocation>", m.group(2), re.S)
            exp = re.search(r"<expect>(.*?)</expect>", m.group(2), re.S)
            if not (inv and exp and "0 fail" in exp.group(1)):
                continue
            mm = re.match(r"^cd <WS>/portal && timeout \d+ \S*bun test (\S+(?: \S+)*)$", inv.group(1).strip())
            if not mm:
                continue
            targets, bar = mm.group(1).split(), exp.group(1)
            one = len(targets) == 1 and re.search(r"\.test\.tsx?$", targets[0]) is not None
            anch = bar.startswith("(?<![0-9])")
            n_sa += one and anch
            if one and not (single is None or (anch and not single[3].startswith("(?<![0-9])"))):
                continue
            if not one and (multi is not None or not anch):
                continue
            n_present = sum(1 for x in targets if pg and len(pin) >= 3 and subprocess.run(
                ["git", "--git-dir", pg, "cat-file", "-e", "%s:%s" % (pin[2], x.rstrip("/"))],
                capture_output=True, timeout=60).returncode == 0)
            if one and n_present != 1:
                continue
            rec = (rel, re.search(r'id="([^"]*)"', m.group(1)).group(1), targets, bar, n_present)
            if one:
                single = rec
            else:
                multi = rec
    return [x for x in (single, multi) if x], n_sa, len(files)


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="ov-battery-"))
    lines = {}
    try:
        issued, recut = _show(AS_ISSUED, F28), _show(AS_RECUT, F28)
        delta = [ln for ln in difflib.unified_diff(issued.splitlines(), recut.splitlines(), lineterm="", n=0)
                 if ln[:1] in "+-" and not ln.startswith(("+++", "---"))]
        # MEASURED on the two real vintages: they differ in TWO line pairs -- F28-AC6's criterion and the record's
        # <status> line (blocked -> pending). The status line is not a criterion and this limb never reads it.
        crit_delta = [ln for ln in delta if "<criterion" in ln]
        rest = [ln for ln in delta if "<criterion" not in ln]
        check("real shapes: FE-s-28 @%s and @%s differ in exactly ONE criterion line, F28-AC6's (the only other "
              "change is the <status> line)" % (AS_ISSUED, AS_RECUT),
              len(crit_delta) == 2 and all('id="F28-AC6"' in ln for ln in crit_delta)
              and all(ln[1:].lstrip().startswith("<status>") for ln in rest), " | ".join(delta)[:300])

        # ---- F36-AC2: F28-AC6 AS ISSUED, staged ADDED, through the CLI.
        twin = _twin(F28, "OV")
        repo_i = _fixture(tmp, "issued")
        _stage(repo_i, twin, issued)
        rc_i, out_i = _run_gate(repo_i, [twin])
        ov_i = _ov_refusals(out_i)
        refused_ac6 = [ln for ln in ov_i if "criterion F28-AC6 --" in ln and twin in ln]
        check("AS ISSUED: F28-AC6 refused by this limb, naming the criterion and the tool",
              bool(refused_ac6) and "test_proof_of_spec_alignment.py" in refused_ac6[0], (ov_i or ["no line"])[0][:300])
        check("AS ISSUED: no OTHER criterion of FE-s-28 is refused by this limb", len(ov_i) == 1,
              "%d OUTPUT-VOCABULARY refusal line(s)" % len(ov_i))
        check("AS ISSUED: the gate's exit code is a refusal (rc=1)", rc_i == 1, "rc=%d" % rc_i)

        # ---- F36-AC3: F28-AC6 AS RE-CUT, same twin path, a fresh index.
        repo_r = _fixture(tmp, "recut")
        _stage(repo_r, twin, recut)
        rc_r, out_r = _run_gate(repo_r, [twin])
        ov_r, tal_r = _ov_refusals(out_r), _tally(out_r, twin)
        check("AS RE-CUT: this limb refuses nothing", not ov_r, " | ".join(ov_r)[:300])
        check("AS RE-CUT: F28-AC6 was EVALUATED and admitted (the tally counts it), not skipped",
              bool(tal_r) and tal_r["admitted"] >= 1 and tal_r["refused"] == 0, repr(tal_r))
        check("DELTA ATTRIBUTION: every other refusal line is byte-identical across the two runs",
              _other_refusals(out_i) == _other_refusals(out_r),
              "issued=%d other line(s), re-cut=%d" % (len(_other_refusals(out_i)), len(_other_refusals(out_r))))
        ok2 = bool(refused_ac6) and len(ov_i) == 1 and rc_i == 1
        ok3 = not ov_r and bool(tal_r) and tal_r["admitted"] >= 1
        lines["AC2"] = ("F28-AC6 AS ISSUED: REFUSED (bar `0 fail`, tool .tools/tests/test_proof_of_spec_alignment.py, "
                        "order bytes @b6062ad2a2 staged as ADDED; the only OUTPUT-VOCABULARY refusal of the order; rc=%d)"
                        % rc_i) if ok2 else "F28-AC6 AS ISSUED: NOT AS SPECIFIED -- see the FAIL lines"
        lines["AC3"] = ("F28-AC6 AS RE-CUT: ADMITTED (bar `BATTERY PASS`, order bytes @9ab6043728, the same twin path; "
                        "evaluated, 0 refused by this limb, every other refusal line byte-identical)"
                        ) if ok3 else "F28-AC6 AS RE-CUT: NOT AS SPECIFIED -- see the FAIL lines"

        # ---- F36-AC4: a runner's own vocabulary. MEASURED at FIXTURE_BASE: no committed criterion is the face's exact
        # shape (the anchored bar on ONE file) -- single-file criteria carry a bare `0 fail`, the anchored bar sits on
        # multi-directory runs. Both real shapes are graded; neither is a string this battery chose.
        specs, n_sa, n_ord = _runner_specimens()
        check("runner specimens: a real single-file `bun test` criterion (its file present in the pinned portal commit) "
              "and a real anchored-bar `bun test` criterion", len(specs) == 2,
              repr([(s[1], s[2]) for s in specs])[:300])
        ok4, described = len(specs) == 2, []
        for rel, cid, targets, bar, n_present in specs:
            rtwin = _twin(rel, "OV")
            repo_b = _fixture(tmp, "runner-" + cid)
            _stage(repo_b, rtwin, _show(FIXTURE_BASE, rel))
            _rc_b, out_b = _run_gate(repo_b, [rtwin])
            hit = [ln for ln in _ov_refusals(out_b) if ("criterion %s --" % cid) in ln]
            tal_b = _tally(out_b, rtwin)
            what = targets[0] if len(targets) == 1 else "%d test directories, %d of them present at the pin" % (
                len(targets), n_present)
            check("RUNNER: %s (`bun test %s`, bar `%s`) is not refused by this limb" % (cid, what, bar), not hit,
                  (hit or [""])[0][:300])
            check("RUNNER: the limb ran on %s and counted its criteria as a runner's vocabulary" % rel.rsplit("/", 1)[-1],
                  bool(tal_b) and tal_b["runner"] >= 1, repr(tal_b))
            ok4 = ok4 and not hit and bool(tal_b) and tal_b["runner"] >= 1
            described.append("%s: `bun test %s`, bar `%s`" % (cid, what, bar))
        lines["AC4"] = ("A RUNNER'S OWN VOCABULARY: ADMITTED (%s; the file present in the portal commit the workspace "
                        "pins for the single file; the same `0 fail` words are refused on a python battery above; single-file criteria with "
                        "the anchored bar at %s: %d across %d orders carrying a `0 fail` bar)"
                        % ("; ".join(described), FIXTURE_BASE, n_sa, n_ord)) if ok4 else \
            "A RUNNER'S OWN VOCABULARY: NOT AS SPECIFIED -- see the FAIL lines"

        # ---- F36-AC5: the target absent at the cut, then present.
        f36_twin = _twin(F36, "OV")
        f36_text = _show(FIXTURE_BASE, F36)
        repo_a = _fixture(tmp, "absent")
        _stage(repo_a, f36_twin, f36_text)
        _rc_a, out_a = _run_gate(repo_a, [f36_twin])
        absent_ids = sorted(set(re.findall(r"criterion (F36-AC\d+) -- TARGET ABSENT AT THE CUT", out_a)))
        ov_a = _ov_refusals(out_a)
        check("ABSENT: the criteria naming this battery are ANNOUNCED as absent at the cut", len(absent_ids) == 5,
              "announced: %s" % ", ".join(absent_ids))
        check("ABSENT: none of them is refused", not ov_a, " | ".join(ov_a)[:300])
        repo_p = _fixture(tmp, "present")
        _stage(repo_p, SELF_REL, Path(__file__).read_text(encoding="utf-8"))
        _stage(repo_p, f36_twin, f36_text)
        _rc_p, out_p = _run_gate(repo_p, [f36_twin, SELF_REL])
        check("ABSENT CONTROL: with this battery staged, no criterion is announced as absent (the note keys on the index)",
              "TARGET ABSENT AT THE CUT" not in out_p and _tally(out_p, f36_twin) is not None)
        ok5 = len(absent_ids) == 5 and not ov_a and "TARGET ABSENT AT THE CUT" not in out_p
        lines["AC5"] = ("TARGET ABSENT AT THE CUT: ANNOUNCED, NOT REFUSED (%d of %d criteria of FE-s-36 @%s name %s, "
                        "absent from that index; control: staged, the absence note is gone)"
                        % (len(absent_ids), 5, FIXTURE_BASE, SELF_REL)) if ok5 else \
            "TARGET ABSENT AT THE CUT: NOT AS SPECIFIED -- see the FAIL lines"

        # ---- F36-AC6: the round-5 orders already on CLOUD, each staged ADDED, one gate run.
        r5 = []
        for p in _git(WORKSPACE, "ls-tree", "--name-only", FIXTURE_BASE, TO_DIR + "/").stdout.splitlines():
            if any(p.endswith("." + s + ".md") for s in ROUND5) and re.search(r"FE-s-(29|3[0-6])\.", p):
                r5.append(p)
        repo_5 = _fixture(tmp, "round5")
        twins, n_crit = [], 0
        for p in sorted(r5):
            text = _show(FIXTURE_BASE, p)
            n_crit += len(re.findall(r"<criterion\b", text))
            twins.append(_twin(p, "OV"))
            _stage(repo_5, twins[-1], text)
        _rc_5, out_5 = _run_gate(repo_5, twins)
        ov_5 = _ov_refusals(out_5)
        tallies = [_tally(out_5, t) for t in twins]
        check("ROUND 5: 8 orders read at %s" % FIXTURE_BASE, len(r5) == 8, ", ".join(x.rsplit("/", 1)[-1] for x in r5))
        check("ROUND 5: the limb ran on every order (a tally note for each)", all(tallies), repr(tallies)[:300])
        for ln in ov_5:
            check("ROUND 5: refused -- a ROW names this criterion: " + ln[:160], False, ln[:300])
        s = {k: sum(t[k] for t in tallies if t) for k in ("mech", "admitted", "refused", "announced", "runner", "other")}
        ok6 = len(r5) == 8 and all(tallies)
        lines["AC6"] = ("REAL ROUND-5 ORDERS: %d REFUSED (%d orders, %d criteria, %d mechanical: %d evaluated and admitted, "
                        "%d announced, %d a runner's vocabulary, %d not one python program's output)"
                        % (len(ov_5), len(r5), n_crit, s["mech"], s["admitted"], s["announced"], s["runner"], s["other"])
                        ) if ok6 else "REAL ROUND-5 ORDERS: NOT AS SPECIFIED -- see the FAIL lines"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    for k in ("AC2", "AC3", "AC4", "AC5", "AC6"):
        print(lines.get(k, "%s: NOT REACHED" % k))
    return _report()


def _report() -> int:
    width = max(len(n) for n, _, _ in results)
    for name, verdict, detail in results:
        line = "  %-4s %s" % (verdict, name.ljust(width))
        if verdict == FAIL and detail:
            line += "   <- " + detail[:300]
        print(line)
    failed = [r for r in results if r[1] == FAIL]
    print("\noutput-vocabulary battery: %d/%d arms as expected" % (len(results) - len(failed), len(results)))
    if failed:
        print("BATTERY FAILED -- the limb does not behave as specified.")
        return 1
    print("BATTERY PASS -- the F28-AC6 shape is refused, its re-cut admitted, a runner's words and an absent target are "
          "never refused, and round 5 is untouched.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
