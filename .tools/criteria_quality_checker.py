#!/usr/bin/env python3
"""criteria_quality_checker.py -- AMGT_RESAPP round 12, cell AMGT-rk-9 (criteria repair at
the issuer). Andrew-direct via the round-11 slug's obligation 5, cut as a cell because it is
graded rather than promised: an issuer's criteria can carry shapes that CANNOT FAIL, and no
product surface can deliver a remedy to that -- only a checker over the issuer's own text can.

REFUSES a criterion carrying one of FIVE shapes, over either object:
  (a) a PROOF-OF-SPEC instance (JSON, schema org/standards/PROOF_OF_SPEC.schema.json)
      whose acceptance[] rows are ALREADY EXECUTED (output_evidence, denominator, status); or
  (b) a TASK-ORDER .md file whose <proof_of_spec> block carries <criterion id=".."
      cell_refs=".."><invocation>..</invocation><expect>..</expect></criterion> elements,
      PRE-EXECUTION (no output_evidence yet -- the only evidence of shape is the issuer's
      own invocation and expect text).

Each shape is a HEURISTIC over the criterion's own text. A criterion this checker does not
flag is ADMITTED, never CERTIFIED -- this tool proves the presence of a named defect shape,
not the absence of every possible one.

FIVE SHAPES (verbatim from AMGT-rk-9's DELIVER list):
  1. ZERO-COLLECTED   -- a test-suite-shaped criterion whose printed/expected collected
                          count is 0 (or a denominator reading "0 of 0").
  2. RC-SWALLOWED     -- a piped test/build runner whose own exit status is never read
                          (no `pipefail`, no `PIPESTATUS` capture, anywhere in the invocation).
  3. GRAIN-MISMATCH   -- a pre/before census and a post/after census IN THE SAME ORDER that
                          resolve their count with a DIFFERENT instrument (tool).
  4. INEXACT-CAPTURE  -- a criterion asserting a specific captured/saved file by a filename
                          carrying a glob wildcard (*, ?, [ ) instead of an exact name.
  5. NO-TIMEOUT       -- a command/live_read/test_suite criterion whose invocation carries
                          no literal `timeout <N>` bound at all.

USAGE:
  python criteria_quality_checker.py --self-test
      Runs FIVE SEALED PLANTED MUTANTS (one per shape above, synthetic, embedded in this
      file -- never read from the estate) plus ONE CLEAN CONTROL, and prints, for each,
      REFUSED or ADMITTED. Prints the counts as its denominator. rc 0 always: this is the
      checker reporting on ITSELF, graded by the caller against "5 refusals, >=1 admission".

  python criteria_quality_checker.py <order.md-or-instance.json> [more ...]
      Scans each file. A .json file is read as a PROOF-OF-SPEC instance (acceptance[]
      rows). Anything else is read as text and its <proof_of_spec> block's <criterion>
      elements are extracted. Prints "orders-scanned <N>" (the denominator) then, per
      file, ADMIT or REFUSE <criterion-id>: <SHAPE> <reason> for every flagged criterion.
      rc 0 (a refusal is a REPORTED finding about the issuer's own bar, never a tool
      failure -- see AMGT-rk-9 AC3); rc 2 on a usage/read error.

NON-APPLICATION, stated once rather than per-shape: this tool reads TEXT. It cannot know
that a criterion's collected count really will be nonzero at run time, only that the
issuer's own words do or do not carry the zero-collection shape; a criterion that passes
every shape here can still fail for reasons outside this cell's remit.
"""
import glob
import json
import re
import sys

RUNNER_RE = re.compile(
    r"\b(pytest|py\.test|python -m pytest|python -m unittest|unittest discover|"
    r"bun test|npm test|npm run test|yarn test|jest|go test|mocha)\b"
)
TIMEOUT_RE = re.compile(r"\btimeout\s+\d+\b")
ZERO_COLLECT_PATTERNS = [
    re.compile(r"\bcollected\s+0\b", re.I),
    re.compile(r"\b0\s+passed\b", re.I),
    re.compile(r"\bran\s+0\s+test", re.I),
    re.compile(r"\b0\s+selected\b", re.I),
    re.compile(r"\bno\s+tests?\s+ran\b", re.I),
    re.compile(r"\b0\s+of\s+0\b", re.I),
]
PRE_RE = re.compile(r"\b(pre-?census|before|prior to|-before\b)", re.I)
POST_RE = re.compile(r"\b(post-?census|after|-after\b)", re.I)
INSTRUMENT_RE = re.compile(
    r"\b(git ls-files|git ls-tree|git log|find|comp-find|aws s3 ls|aws s3api|"
    r"apigatewayv2 get-routes|ls -[a-zA-Z]*|wc -l|du -s)\b"
)
CAPTURE_CONTEXT_RE = re.compile(
    # captur\w* deliberately EXCLUDES the `capture_output=True` subprocess.run() kwarg, which is
    # unrelated boilerplate present in most of this estate's own invocations and would otherwise
    # false-fire this shape on every criterion that merely calls subprocess.run near a wildcard.
    r"\b(captur(?!e_output)\w*|saved? to|written to|the file|output file|copy(?:ied)? (?:both|the))\b",
    re.I,
)
FILE_TOKEN_RE = re.compile(r"[\w./\-*?\[\]]+\.(?:json|txt|log|py|md|csv)\b")
CRITERION_RE = re.compile(
    r'<criterion\s+id="([^"]+)"[^>]*>\s*<invocation>(.*?)</invocation>\s*'
    r"<expect>(.*?)</expect>\s*</criterion>",
    re.S,
)


def _norm(c):
    """Normalize a criterion dict from either source into the common field set this
    checker reads: id, method, invocation, expect, verbatim, output_evidence, denominator."""
    return {
        "id": c.get("id") or c.get("criterion_id") or "?",
        "method": c.get("method") or "command",
        "invocation": c.get("invocation") or "",
        "expect": c.get("expect") or "",
        "verbatim": c.get("verbatim") or c.get("criterion_verbatim") or "",
        "output_evidence": c.get("output_evidence") or "",
        "denominator": c.get("denominator") or "",
    }


def load_criteria_from_json(path):
    inst = json.loads(open(path, encoding="utf-8").read())
    return [_norm(row) for row in inst.get("acceptance", [])]


def load_criteria_from_order(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r"<proof_of_spec>(.*?)</proof_of_spec>", text, re.S)
    scope = m.group(1) if m else text
    out = []
    for cm in CRITERION_RE.finditer(scope):
        out.append(_norm({"id": cm.group(1), "invocation": cm.group(2), "expect": cm.group(3)}))
    return out


def load_criteria(path):
    if path.endswith(".json"):
        return load_criteria_from_json(path)
    return load_criteria_from_order(path)


# ---------------------------------------------------------------- the five shapes


def shape1_zero_collected(c):
    is_suite = c["method"] == "test_suite" or bool(RUNNER_RE.search(c["invocation"]))
    if not is_suite:
        return None
    blob = " ".join([c["output_evidence"], c["expect"], c["denominator"]])
    for pat in ZERO_COLLECT_PATTERNS:
        if pat.search(blob):
            return f"ZERO-COLLECTED: test-suite-shaped criterion reads '{pat.pattern}' -- {blob.strip()[:140]}"
    return None


def shape2_rc_swallowed(c):
    inv = c["invocation"]
    if not RUNNER_RE.search(inv):
        return None
    for seg in re.split(r"(?:;|&&)", inv):
        if RUNNER_RE.search(seg) and "|" in seg:
            if "pipefail" in inv or "PIPESTATUS" in inv:
                return None
            return f"RC-SWALLOWED: runner piped without pipefail/PIPESTATUS -- '{seg.strip()[:140]}'"
    return None


def shape3_grain_mismatch(criteria):
    """Runs over the WHOLE set of criteria in one order/instance (not one at a time):
    the shape is a relationship BETWEEN two rows, never a property of either alone."""
    flags = {}
    pre_rows = [c for c in criteria if PRE_RE.search(c["invocation"] + " " + c["expect"] + " " + c["verbatim"])]
    post_rows = [c for c in criteria if POST_RE.search(c["invocation"] + " " + c["expect"] + " " + c["verbatim"])]
    for p in pre_rows:
        pm = INSTRUMENT_RE.search(p["invocation"])
        if not pm:
            continue
        for q in post_rows:
            if q["id"] == p["id"]:
                continue
            qm = INSTRUMENT_RE.search(q["invocation"])
            if not qm:
                continue
            if pm.group(1) != qm.group(1):
                flags[p["id"]] = (
                    f"GRAIN-MISMATCH: pre-census instrument '{pm.group(1)}' vs "
                    f"post-census '{qm.group(1)}' in {q['id']}"
                )
                flags[q["id"]] = (
                    f"GRAIN-MISMATCH: post-census instrument '{qm.group(1)}' vs "
                    f"pre-census '{pm.group(1)}' in {p['id']}"
                )
    return flags


def shape4_inexact_capture(c):
    blob = c["invocation"] + " " + c["expect"] + " " + c["verbatim"]
    for tok in FILE_TOKEN_RE.findall(blob):
        if any(ch in tok for ch in "*?[]") and CAPTURE_CONTEXT_RE.search(blob):
            return f"INEXACT-CAPTURE: captured file asserted by wildcard token '{tok}'"
    return None


def shape5_no_timeout(c):
    if not c["invocation"].strip():
        return None
    if TIMEOUT_RE.search(c["invocation"]):
        return None
    return "NO-TIMEOUT: invocation carries no literal `timeout <N>` bound"


def evaluate(criteria):
    """Returns {criterion_id: [reason, ...]} for every flagged criterion."""
    flags = {}
    for c in criteria:
        reasons = []
        for fn in (shape1_zero_collected, shape2_rc_swallowed, shape4_inexact_capture, shape5_no_timeout):
            r = fn(c)
            if r:
                reasons.append(r)
        if reasons:
            flags.setdefault(c["id"], []).extend(reasons)
    for cid, reason in shape3_grain_mismatch(criteria).items():
        flags.setdefault(cid, []).append(reason)
    return flags


# ---------------------------------------------------------------- self-test (sealed planted mutants)


def _mk(id_, invocation="", expect="", verbatim="", method="command", output_evidence="", denominator=""):
    return _norm(
        {
            "id": id_,
            "invocation": invocation,
            "expect": expect,
            "verbatim": verbatim,
            "method": method,
            "output_evidence": output_evidence,
            "denominator": denominator,
        }
    )


def _self_test():
    results = []

    # SHAPE 1 mutant: a test-suite criterion whose own denominator reads "0 of 0" --
    # exactly round 11's "suite over an empty collection" defect this cell exists to catch.
    m1 = _mk(
        "MUT-1",
        invocation="python -m pytest tests/test_planted_mutant_empty.py -q",
        method="test_suite",
        output_evidence="collected 0 items\n============ no tests ran in 0.01s ============",
        denominator="0 of 0 tests collected",
    )
    flagged = evaluate([m1])
    results.append(("shape1-zero-collected", "MUT-1", bool(flagged.get("MUT-1"))))

    # SHAPE 2 mutant: pytest piped into tee with NO pipefail/PIPESTATUS -- the rc a caller
    # reads is tee's, never pytest's.
    m2 = _mk(
        "MUT-2",
        invocation="pytest tests/test_real.py -q | tee .scratch/out.log; echo rc=$?",
    )
    flagged = evaluate([m2])
    results.append(("shape2-rc-swallowed", "MUT-2", bool(flagged.get("MUT-2"))))

    # SHAPE 3 mutant: a pre-census on `git ls-files` (tracked-only) paired with a post-census
    # on `find` (every file) in the SAME order -- the W20-S1 grain-mismatch class.
    m3a = _mk(
        "MUT-3-PRE",
        invocation="git ls-files org/x | wc -l",
        expect="routes-before N",
        verbatim="pre-census file count",
    )
    m3b = _mk(
        "MUT-3-POST",
        invocation="find org/x -type f | wc -l",
        expect="routes-after N",
        verbatim="post-census file count",
    )
    flagged = evaluate([m3a, m3b])
    results.append(("shape3-grain-mismatch", "MUT-3-PRE/POST", bool(flagged.get("MUT-3-PRE")) and bool(flagged.get("MUT-3-POST"))))

    # SHAPE 4 mutant: the criterion claims a specific captured output file but locates it
    # by a glob wildcard, so the file it actually reads is never provably the one named.
    m4 = _mk(
        "MUT-4",
        invocation="cat .scratch/result_*.json",
        expect="the captured output file result_007.json contains status ok",
        verbatim="the output file .scratch/result_*.json was saved to disk",
    )
    flagged = evaluate([m4])
    results.append(("shape4-inexact-capture", "MUT-4", bool(flagged.get("MUT-4"))))

    # SHAPE 5 mutant: an unbounded invocation, no timeout of any duration.
    m5 = _mk(
        "MUT-5",
        invocation="python -m pytest tests/test_real.py -q",
    )
    flagged = evaluate([m5])
    results.append(("shape5-no-timeout", "MUT-5", bool(flagged.get("MUT-5"))))

    # CLEAN CONTROL: an honest criterion carrying NONE of the five shapes -- bounded,
    # rc genuinely read, nonzero collected count, one exact filename, no pre/post pairing.
    control = _mk(
        "CTRL-1",
        invocation="timeout 90 python -m pytest tests/test_real.py -q > .scratch/ctrl.log 2>&1; echo rc=$?",
        method="test_suite",
        output_evidence="rc=0\ncollected 12 items\n12 passed in 0.44s",
        denominator="12 of 12 tests collected and passed",
        verbatim="the exact file .scratch/ctrl.log was captured",
    )
    flagged = evaluate([control])
    results.append(("clean-control", "CTRL-1", bool(flagged.get("CTRL-1"))))

    refused = 0
    admitted = 0
    print("SELF-TEST -- five sealed planted mutants (one per shape) plus one clean control:")
    for shape_name, mid, was_flagged in results:
        if mid == "CTRL-1":
            verdict = "ADMITTED" if not was_flagged else "REFUSED (WRONG -- control should be clean)"
            if not was_flagged:
                admitted += 1
        else:
            verdict = "REFUSED" if was_flagged else "ADMITTED (WRONG -- mutant should be refused)"
            if was_flagged:
                refused += 1
        print(f"  {shape_name:24s} {mid:14s} -> {verdict}")
    print(f"DENOMINATOR: mutants-refused {refused} of 5; controls-admitted {admitted} of 1")
    if refused == 5 and admitted == 1:
        print("SELF-TEST RESULT: DISCRIMINATES (5 of 5 mutants refused, 1 of 1 control admitted)")
    else:
        print("SELF-TEST RESULT: DOES NOT DISCRIMINATE -- see counts above")
    return 0


# ---------------------------------------------------------------- main


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        return _self_test()
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        print("USAGE-ERROR (rc=2): expected one or more <order.md|instance.json> paths")
        return 2
    files = []
    for a in args:
        files.extend(sorted(glob.glob(a))) if any(ch in a for ch in "*?[") else files.append(a)
    print(f"orders-scanned {len(files)}")
    any_refusal = False
    for f in files:
        try:
            criteria = load_criteria(f)
        except Exception as exc:  # noqa: BLE001
            print(f"  READ-ERROR {f}: {exc}")
            continue
        flags = evaluate(criteria)
        if not flags:
            print(f"  ADMIT {f} ({len(criteria)} criteria, 0 flagged)")
            continue
        any_refusal = True
        print(f"  REFUSE {f} ({len(criteria)} criteria, {len(flags)} flagged)")
        for cid in sorted(flags):
            for reason in flags[cid]:
                print(f"    {cid}: {reason}")
    print(f"VERDICT: {'REFUSALS PRESENT' if any_refusal else 'ALL ADMITTED'} across {len(files)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
