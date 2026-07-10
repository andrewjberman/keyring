"""NFRA_TOOLCHECK.P4 -- negative-control fixture for `comp-surface-check`.

Owner: 0.4.0_DS_ClientPlatform~B (graph-engine charge, TO 05b2a2c1c section 8).
Lane:  NFRA_TOOLCHECK_P4 (.owned-paths.yaml) -- org/modules/graph/tests/**

P4 section 4 acceptance: THREE rails, or the tool is not verified.
  R1 NEGATIVE  an input the tool MUST go RED on.   Stored here. CI asserts it REDs.
  R3 POSITIVE  a healthy input it must stay GREEN on.
  R2 VARIANCE  the control on the control -- demonstrate the RECORDER can produce
               the other verdict at all. R1's RED is evidence only because R3 is GREEN
               from the same recorder.

VERDICT ON THE TOOL      : WORKS (discriminating). rc=2 + CRITICAL on a SEV1 surface;
                           rc=0 + OK on a file in no surface.
VERDICT ON THE GATE      : the safe-commit wiring CANNOT BLOCK, BY CONSTRUCTION.
                           `safe-commit.sh:417-418` runs it `--mode advisory`, pipes to
                           `sed`, and appends `|| true` -- THREE independent exit-code
                           maskings -- and never branches on the verdict at all.

THE TRAP THIS FIXTURE EXISTS TO CATCH (test_the_obvious_repair_is_invisible):
    A maintainer "fixes" the gate by flipping `--mode advisory` -> `--mode blocking`.
    Behaviour is IDENTICAL: the pipe still replaces rc with sed's, and `|| true` eats
    what is left. The CRITICAL line prints either way, so the repair LOOKS successful.
    Only `set -o pipefail` + an actual branch on rc restores the signal.

    An assertion that has never failed has never been tested.
    Never-fires and always-fires are the same defect.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

# tests/ -> graph/ -> modules/ -> org/ -> <repo root>.  parents[4], not [3].
# Asserted, not assumed: a wrong root makes every assertion below fail on a missing
# file rather than silently pass, but a wrong root that HAPPENED to resolve would
# make this whole fixture vacuous.
REPO = Path(__file__).resolve().parents[4]
TOOL = REPO / ".tools" / "comp-surface-check"
assert TOOL.is_file(), f"repo root misresolved: {REPO} has no .tools/comp-surface-check"

# A member of SEV1 surfaces model_portfolios.headline + model_portfolios.benchmark
# per org/modules/graph/critical-surfaces.yaml. The SHARPEST input the gate should
# catch, not the most obvious one: this single path alarms at SEV1 via two surfaces.
SEV1_PATH = "portal/src/pages/ModelPortfolios.tsx"

# A path in no critical surface. Deliberately a file this fixture's own author owns,
# so the positive control cannot silently start alarming when someone edits the repo.
BENIGN_PATH = "org/tier2_senior/0.4.0_DS_ClientPlatform/prompt.md"


def _find_bash() -> str:
    """NEVER resolve `bash` by NAME.

    On Windows, `subprocess(["bash", ...])` uses CreateProcess, which searches
    System32 before PATH and finds WSL's `bash.exe` -- while `shutil.which("bash")`
    returns Git Bash. The two disagree. WSL then fails with
    `execvpe(/bin/bash): No such file or directory` and returns rc=1.

    THAT IS WHY EVERY ASSERTION BELOW CHECKS `rc == 2` AND THE VERDICT TEXT, NEVER
    MERELY `rc != 0`. A broken interpreter is also non-zero: this fixture's R1
    negative control PASSED under WSL, on a tool that never ran. It is
    `comp-tagauthz`'s defect (P4 section 6) -- a gate that fails for the wrong
    reason is indistinguishable, at the console, from a gate that works.
    """
    for cand in ("/bin/bash",
                 r"C:\Program Files\Git\bin\bash.exe",
                 r"C:\Program Files\Git\usr\bin\bash.exe"):
        if not Path(cand).is_file():
            continue
        # POSITIVE CONTROL ON THE INTERPRETER: prove it executes and propagates rc
        # before we trust any rc it reports for the tool under test.
        probe = subprocess.run([cand, "-c", "exit 7"], capture_output=True)
        if probe.returncode == 7:
            return cand
    raise RuntimeError("no bash that executes and propagates an exit code")


BASH = _find_bash()


def _run(mode: str, path: str) -> tuple[int, str]:
    """Invoke the tool directly. NO PIPE -- a pipe would replace rc with the last
    stage's, which is the very defect under test."""
    p = subprocess.run(
        [BASH, str(TOOL), "check", "--mode", mode, "--file", path],
        capture_output=True, text=True, cwd=str(REPO),
    )
    return p.returncode, p.stdout + p.stderr


# --------------------------------------------------------------------------
# R1 -- NEGATIVE CONTROL. The deliverable. This MUST go RED.
# --------------------------------------------------------------------------
def test_R1_negative_sev1_surface_must_red() -> None:
    """The NAMED SURFACE is the load-bearing assertion, not `rc` and not the prose.

    `rc == 2` is NOT the specific red: argparse exits 2 on a USAGE ERROR, so a
    malformed invocation returns exactly the tool's RED code on ANY input, benign
    or not (see test_rc2_is_ambiguous_usage_error_vs_red). And `"CRITICAL" in out`
    is a word in the wrapper prose. Only the named surface is the property.
    """
    rc, out = _run("blocking", SEV1_PATH)
    assert rc == 2, f"expected rc=2, got {rc}\n{out}"
    assert "CRITICAL" in out, f"no CRITICAL verdict emitted\n{out}"
    assert "SEV1" in out, f"no SEV1 severity emitted\n{out}"
    # THE PROPERTY. Survives a usage error, a broken interpreter, and a reworded banner.
    assert "model_portfolios.headline" in out, f"SEV1 surface not named\n{out}"
    assert "model_portfolios.benchmark" in out, f"2nd SEV1 surface not named\n{out}"


def test_rc2_is_ambiguous_usage_error_vs_red() -> None:
    """`rc=2` IS THE TOOL'S RED **AND** ARGPARSE'S USAGE-ERROR CODE. They collide.

    Found by 1.0.0_SA_CTO (031807Z), whose first exercise passed a POSITIONAL path
    instead of `--file` and got rc=2 on a SEV1 path -- and, because he ran his
    positive control, rc=2 on a benign path too. A usage error is also non-zero,
    and here it is not merely non-zero: IT IS THE EXACT RED CODE.

    So `assert rc == 2` alone is UNDISCRIMINATING between a verdict and a typo.
    This test pins the collision so nobody weakens R1 back down to the rc check.
    """
    # positional path (the malformed call) -- argparse usage error, on BOTH inputs
    bad_sev = subprocess.run([BASH, str(TOOL), "check", "--mode", "blocking", SEV1_PATH],
                             capture_output=True, text=True, cwd=str(REPO))
    bad_ben = subprocess.run([BASH, str(TOOL), "check", "--mode", "blocking", BENIGN_PATH],
                             capture_output=True, text=True, cwd=str(REPO))

    assert bad_sev.returncode == 2 and bad_ben.returncode == 2, (
        "premise changed: a positional path no longer produces argparse's rc=2. "
        f"sev={bad_sev.returncode} benign={bad_ben.returncode}"
    )
    # ...and rc=2 here means NOTHING about surfaces. The named-surface assertion is
    # what separates a verdict from a typo. Neither malformed run names a surface.
    for r in (bad_sev, bad_ben):
        blob = r.stdout + r.stderr
        assert "model_portfolios.headline" not in blob, (
            "a usage error named a surface -- the discriminator is broken"
        )
        assert "CRITICAL" not in blob, "a usage error emitted CRITICAL"


# --------------------------------------------------------------------------
# R3 -- POSITIVE CONTROL. A healthy input must stay GREEN.
# --------------------------------------------------------------------------
def test_R3_positive_benign_file_must_stay_green() -> None:
    rc, out = _run("blocking", BENIGN_PATH)
    assert rc == 0, f"benign file did not stay GREEN. rc={rc}\n{out}"
    assert "CRITICAL" not in out, f"benign file emitted CRITICAL\n{out}"
    assert "OK:" in out, f"no OK verdict emitted\n{out}"


# --------------------------------------------------------------------------
# R2 -- VARIANCE. THE CONTROL ON THE CONTROL.
# R1's rc=2 is evidence only if this recorder can also produce rc=0. It can.
# Without this, an always-fires gate is indistinguishable from a working one.
# --------------------------------------------------------------------------
def test_R2_variance_recorder_emits_both_verdicts() -> None:
    rc_red, _ = _run("blocking", SEV1_PATH)
    rc_green, _ = _run("blocking", BENIGN_PATH)
    assert {rc_red, rc_green} == {2, 0}, (
        f"recorder is UNDISCRIMINATING: red={rc_red} green={rc_green}. "
        "An instrument's zero is evidence only after you have seen it produce a one."
    )


# --------------------------------------------------------------------------
# THE GATE, not the tool. Documents the live defect + guards the invisible repair.
# --------------------------------------------------------------------------
def test_advisory_mode_computes_CRITICAL_then_returns_zero() -> None:
    """MASK 1. safe-commit.sh:417 uses --mode advisory. The SEV1 CRITICAL is
    computed and printed; rc is 0. The verdict exists and is not acted on."""
    rc, out = _run("advisory", SEV1_PATH)
    assert "CRITICAL" in out, "advisory should still COMPUTE the SEV1 verdict"
    assert rc == 0, (
        f"advisory returned rc={rc}. If this now REDs, safe-commit's gate semantics "
        "changed -- re-derive the wiring before relaxing this assertion."
    )


def test_the_obvious_repair_is_invisible() -> None:
    """MASK 2 + 3, and the reason this fixture exists.

    Flipping advisory->blocking does NOT make the gate block, because
    `cmd | sed` yields sed's rc and `|| true` eats the remainder. A maintainer
    who flips the mode sees the CRITICAL line print and concludes the gate works.

    Positive control: pipefail restores rc=2, proving the verdict was there and
    the WIRING discards it -- not the tool.
    """
    shape = f'"{BASH}" "{TOOL}" check --mode blocking --file {SEV1_PATH} 2>&1 | sed "s/^/x/" >/dev/null'

    masked = subprocess.run([BASH, "-c", f"{shape} || true"], cwd=str(REPO))
    assert masked.returncode == 0, "expected the safe-commit pipeline shape to mask rc"

    piped = subprocess.run([BASH, "-c", shape], cwd=str(REPO))
    assert piped.returncode == 0, "expected the bare pipe to mask rc (sed's status wins)"

    # POSITIVE CONTROL on this very assertion: the RED is retrievable.
    # Without this line, `masked.returncode == 0` would also pass if the tool were
    # simply broken and never emitted anything. Put the control on the RETRIEVAL.
    restored = subprocess.run([BASH, "-c", f"set -o pipefail; {shape}"], cwd=str(REPO))
    assert restored.returncode == 2, (
        f"pipefail did not restore the RED (rc={restored.returncode}). "
        "If this fails, the tool stopped REDding and test_R1 is the real signal."
    )


def test_safe_commit_does_not_branch_on_the_verdict() -> None:
    """The gate never reads rc: no `if`, no capture, no exit. Even with pipefail
    and blocking mode, nothing consumes the verdict. Guard against a silent rewire."""
    src = (REPO / ".tools" / "safe-commit.sh").read_text(encoding="utf-8", errors="replace")
    assert "comp-surface-check check --mode advisory" in src, (
        "safe-commit's surface-check invocation changed -- re-verify the gate wiring "
        "and this fixture's premises before editing this assertion."
    )
    assert "| sed 's/^/  [surface-check] /' || true" in src, (
        "the masking pipeline changed -- if the gate now blocks, update the P4 verdict."
    )
