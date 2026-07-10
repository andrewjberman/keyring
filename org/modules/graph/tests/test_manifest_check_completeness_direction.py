"""NFRA_TOOLCHECK.P4 -- three-rail verification of `comp-manifest-check`.

Owner: 0.4.0_DS_ClientPlatform~B (graph-engine charge, TO 05b2a2c1c section 8).
Lane:  NFRA_TOOLCHECK_P4 -- org/modules/graph/tests/**

VERDICTS (two subjects, two answers -- a tool is not one thing):

  `check` / `selfcheck`  -> WORKS. It ships its OWN R1 and R3: cmd_selfcheck asserts the
                           B + C anti-pattern categories are FOUND, >=1 ERROR-class, AND that
                           the benign line yields exactly 0 false positives. The first tool in
                           P4 found already carrying a negative control. Credit where due.

  `completeness` family  -> UNDISCRIMINATING WITH RESPECT TO THE PROPERTY IN ITS NAME.
                           routable + existence + placement + self-routes ALL take their
                           denominator FROM `tools_index`. They assert index -> disk and
                           index -> routable. NOTHING asserts disk -> index.

                           A COMPLETENESS CHECK WHOSE DENOMINATOR IS THE CATALOG CANNOT
                           DETECT AN INCOMPLETE CATALOG. Its verdict is invariant under the
                           truth it is named for.

                           Exercised: 19 comp-* invokables sit on disk unregistered --
                           including `comp-which` (the router), `comp-surface-check` (the SEV1
                           gate), `comp-grep`/`comp-glob` (the Rule-21 defaults), and
                           `comp-manifest-check` ITSELF. `completeness` prints
                           "PASS ... over 42 registered tool(s)" and exits 0.

TWO SUPPORTING DEFECTS, source-confirmed:

  1. `manifest_check_cli.py:472`  `_targets, unreachable, _uncatalogued, exempted = rc.check()`
     The engine RETURNS an `uncatalogued` set and the gate binds it to a DISCARD NAME.
     But do not mis-state the mechanism (I nearly did): that variable is NOT the 19.
     `comp-routable-check:114`  `uncatalogued = sorted(routable_ids - tools_index)` -- it is
     capability-provider-minus-index, and it is currently EMPTY. So the slot is both
     misnamed AND discarded, and neither fact alone is the finding.

  2. `comp-routable-check:57`  `EXCLUDE = {"comp-grep", "comp-glob", "comp-which"}`
     `:96`                     `targets = tools_index - EXCLUDE`
     |targets| == |tools_index| == 42. THE EXCLUSION HAS NEVER EXCLUDED ANYTHING, because
     none of the three is in `tools_index`. It was written, with a justifying comment, by an
     author who assumed the router was in the router's index. A set operation whose result is
     invariant under its own operand.

WHEN THE FAMILY IS MADE BIDIRECTIONAL, `test_completeness_is_blind_to_an_incomplete_catalog`
MUST GO RED. That is the acceptance signal, not a regression. Invert it then.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[4]
TOOL = REPO / ".tools" / "comp-manifest-check"
MANIFEST = REPO / "org" / "modules" / "graph" / "graph-call-manifest.yaml"
assert TOOL.is_file(), f"repo root misresolved: {REPO}"

# manifest_check_cli lives beside this tests/ dir, in the graph module.
sys.path.insert(0, str(REPO / "org" / "modules" / "graph"))


def _find_bash() -> str:
    """Never resolve `bash` by NAME: on Windows subprocess finds WSL's bash while
    shutil.which finds Git Bash. Positive-control the interpreter before trusting any
    rc it reports. See test_surface_check_negative_control for the incident."""
    for cand in ("/bin/bash",
                 r"C:\Program Files\Git\bin\bash.exe",
                 r"C:\Program Files\Git\usr\bin\bash.exe"):
        if Path(cand).is_file() and subprocess.run([cand, "-c", "exit 7"],
                                                   capture_output=True).returncode == 7:
            return cand
    raise RuntimeError("no bash that executes and propagates an exit code")


BASH = _find_bash()


def _run(*args: str) -> tuple[int, str]:
    p = subprocess.run([BASH, str(TOOL), *args],
                       capture_output=True, text=True, cwd=str(REPO))
    return p.returncode, p.stdout + p.stderr


def _index() -> set[str]:
    return set(yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))["tools_index"])


def _disk_comp_tools() -> set[str]:
    return {p.name for p in (REPO / ".tools").iterdir()
            if p.is_file() and p.name.startswith("comp-") and p.suffix == ""}


# --------------------------------------------------------------------------
# The anti-pattern detector: it carries its own R1 + R3. Verify BOTH fire.
# --------------------------------------------------------------------------
def test_R1_selfcheck_detects_the_synthetic_antipatterns() -> None:
    rc, out = _run("selfcheck")
    assert rc == 0, f"selfcheck FAILED\n{out}"
    assert "B_rebuild_when_query" in out, f"category B not detected\n{out}"
    assert "C_adhoc_reimplementation" in out, f"category C not detected\n{out}"
    assert "[ERROR]" in out, f"no ERROR-class finding\n{out}"
    # its embedded POSITIVE control: the benign line must yield 0 false positives
    assert "0 false-positive" in out, f"selfcheck lost its false-positive control\n{out}"


ANTIPATTERN = 'dag = build_firm_gold_dag(firm="bd")\n'
BENIGN = "total = sum([1, 2, 3])\n"


def _probe(body: str, name: str) -> tuple[int, str]:
    """Write a probe at the REPO ROOT -- NOT under this tests/ dir.

    `org/modules/graph/` is an `exempt_path_substring`, so a probe written beside this
    file is SILENTLY NOT SCANNED and returns rc=0 with zero output. My first draft did
    exactly that and read the silence as 'no findings'. The gate cannot tell you it did
    not look; the fixture must place its own input where the gate actually looks.
    """
    p = REPO / name
    p.write_text(body, encoding="utf-8")
    try:
        return _run("check", "--mode", "blocking", "--file", p.name)
    finally:
        p.unlink(missing_ok=True)


def test_R1_check_reds_on_a_real_antipattern_in_blocking_mode() -> None:
    """A file that re-implements a manifest-covered use-case MUST RED under --mode blocking."""
    rc, out = _probe(ANTIPATTERN, "_p4_probe_antipattern.py")
    # assert the PROPERTY, not merely non-zero: argparse also exits non-zero (rc=2),
    # and a silent exemption exits ZERO. Neither is a verdict.
    assert "C_adhoc_reimplementation" in out, f"anti-pattern not named\n{out}"
    assert "[ERROR]" in out, f"not ERROR-class\n{out}"
    assert rc == 1, f"blocking mode did not RED with rc=1. rc={rc}\n{out}"


def test_R3_positive_check_stays_green_on_a_clean_file() -> None:
    rc, out = _probe(BENIGN, "_p4_probe_clean.py")
    assert rc == 0, f"clean file did not stay GREEN. rc={rc}\n{out}"
    assert "[ERROR]" not in out, f"clean file produced an ERROR finding\n{out}"


def test_silent_exemption_is_byte_identical_to_a_clean_scan() -> None:
    """LIVE. An EXEMPT file carrying a live ERROR and a SCANNED file that is clean
    produce the SAME rc and the SAME (empty) output. The gate never says it skipped.

    That is the night's law in a third subsystem: an instrument that is MUTE on the
    branch that matters. `A predicate that cannot NAME what it excluded has not
    enumerated a universe` (CTO, ratified 024421Z) -- here, what it excluded is a file
    with a real defect in it.
    """
    exempt = REPO / "org" / "modules" / "graph" / "tests" / "_p4_probe_exempt.py"
    exempt.write_text(ANTIPATTERN, encoding="utf-8")
    try:
        rc_exempt, out_exempt = _run(
            "check", "--mode", "blocking",
            "--file", exempt.relative_to(REPO).as_posix())
    finally:
        exempt.unlink(missing_ok=True)

    rc_clean, out_clean = _probe(BENIGN, "_p4_probe_clean2.py")

    # POSITIVE CONTROL: the same bytes at the repo root DO red. So the silence below
    # is the exemption, not an impotent detector.
    rc_red, out_red = _probe(ANTIPATTERN, "_p4_probe_control.py")
    assert rc_red == 1 and "[ERROR]" in out_red, "detector cannot fire; this test proves nothing"

    assert (rc_exempt, out_exempt.strip()) == (rc_clean, out_clean.strip()), (
        "exempt-with-a-defect and scanned-and-clean are no longer identical -- "
        "the gate may have learned to announce its skips. Good. Invert this test."
    )


def test_exemption_matches_a_SUBSTRING_not_a_path_component() -> None:
    """LATENT (0 offenders in the tree today, verified with `git ls-files`).

    `is_exempt` does `if sub in rel`, so `docs/` matches `mydocs/` and `oldocs/`.
    A directory named `oldocs` anywhere silently disables the graph anti-pattern gate
    for everything beneath it -- including a gold script.

    Identical species to `grep -iE 'iam'` matching `black_diamond` (1.0.0_SA_CTO,
    031807Z, which staged a 49F file under the sovereign prohibition):
    SUBSTRING STANDING IN FOR PATH-COMPONENT.
    """
    import manifest_check_cli as m  # noqa: PLC0415

    cfg = m.load_config()
    # POSITIVE CONTROL: a real gold script is scanned.
    assert not m.is_exempt(Path("data/inf/scripts/gold/x.py"), cfg)
    # POSITIVE CONTROL: the graph module is exempt, as intended.
    assert m.is_exempt(Path("org/modules/graph/foo.py"), cfg)
    # THE DEFECT: `oldocs` is not `docs`, and neither is `mydocs`.
    assert m.is_exempt(Path("data/inf/scripts/gold/oldocs/run.py"), cfg), (
        "substring exemption fixed -- rewrite this test as a component check"
    )
    assert m.is_exempt(Path("infra/aws/lambda/mydocs/handler.py"), cfg)


def test_R2_variance_the_detector_emits_both_verdicts() -> None:
    """R1's RED is evidence only because R3 is GREEN from the same recorder."""
    rc_red, _ = _run("selfcheck")
    rc_green, out_green = _run("completeness")
    assert (rc_red, rc_green) == (0, 0)
    # the detector's variance is proven by R1/R3 above; this pins that `completeness`
    # is a DIFFERENT subject with a DIFFERENT verdict, measured separately.
    assert "PASS" in out_green


# --------------------------------------------------------------------------
# THE FINDING. `completeness` cannot see an incomplete catalog.
# --------------------------------------------------------------------------
def test_completeness_is_blind_to_an_incomplete_catalog() -> None:
    """Pins the live defect. MUST GO RED when the family is made bidirectional --
    that failure is the acceptance signal for the fix, not a regression."""
    unregistered = _disk_comp_tools() - _index()

    assert unregistered, "premise changed: every on-disk comp-* tool is now registered"
    assert "comp-manifest-check" in unregistered, (
        "the validator is now in its own catalog -- re-derive this test"
    )
    assert "comp-which" in unregistered, "the router is now indexed by the router"
    assert "comp-surface-check" in unregistered, "the SEV1 gate is now registered"

    rc, out = _run("completeness")
    assert rc == 0 and "PASS" in out, (
        f"completeness now REDs (rc={rc}). If it learned the disk->index direction, "
        "INVERT this test: that is the fix landing, not a break.\n" + out
    )
    # ...and it says so out loud, in its own denominator.
    assert f"{len(_index())} registered tool" in out, (
        f"completeness no longer reports its denominator as the catalog\n{out}"
    )


def test_the_routable_EXCLUDE_set_has_never_excluded_anything() -> None:
    """`comp-routable-check:96` computes `targets = tools_index - EXCLUDE` where
    EXCLUDE = {comp-grep, comp-glob, comp-which}. None is in tools_index, so the
    subtraction is a no-op: a set operation invariant under its own operand."""
    exclude = {"comp-grep", "comp-glob", "comp-which"}
    idx = _index()
    assert not (exclude & idx), (
        "EXCLUDE now intersects tools_index -- the subtraction finally does something; "
        "re-derive comp-routable-check's target count."
    )
    rc, out = _run("routable")
    assert rc == 0 and f"{len(idx)} registered tool" in out, (
        f"routable's denominator is no longer |tools_index|={len(idx)}\n{out}"
    )
