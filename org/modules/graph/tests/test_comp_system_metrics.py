"""comp-system live-metrics refresher (2026-07-14, Andrew-direct: comp-system should refresh
tool counts / state / anything that would actually go stale, not just the one doc).

WHAT THIS PROVES:
  1. compute_metrics() grounds the real scalars against their ONE authoritative source (the tool
     counts read from the manifest + ledger yaml, not scraped prose).
  2. the managed-region refresher CORRECTS a drifted span (the whole point) -- exercised against a
     deliberately-stale fixture doc, not just asserted.
  3. it is SAFE: it rewrites ONLY the text between the <!--cs:NAME--> markers, never the surrounding
     prose; an UNKNOWN metric is REFUSED (the existing number is preserved, the drift reported) --
     the no-fabrication invariant, so the refresher can never stamp UNKNOWN-VINTAGE over a real count.
  4. an unknown metric name is reported, not silently applied.

    python org/modules/graph/tests/test_comp_system_metrics.py
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import comp_system as cs  # noqa: E402

PASS = 0
FAIL = 0


def check(name: str, got, want) -> None:
    global PASS, FAIL
    if got == want:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}: got {got!r}, want {want!r}")


print("== compute_metrics grounds the real scalars ==")
mets = cs.compute_metrics()
check("tools_index_count is a positive int (read from manifest yaml, not prose)",
      isinstance(mets["tools_index_count"]["value"], int) and mets["tools_index_count"]["value"] > 0, True)
check("ledger_union_count is a positive int (tools+meta_tools)",
      isinstance(mets["ledger_union_count"]["value"], int) and mets["ledger_union_count"]["value"] > 0, True)
check("ledger_union >= tools_index (union of tools+meta is the larger set)",
      mets["ledger_union_count"]["value"] >= mets["tools_index_count"]["value"], True)
check("every metric carries {value,source,vintage}",
      all(set(v.keys()) == {"value", "source", "vintage"} for v in mets.values()), True)

# ---------------------------------------------------------------------------
# The refresher, exercised against a fixture doc in a temp dir (never the real tree).
# ---------------------------------------------------------------------------
print("== refresher CORRECTS a drifted span (the core behavior) ==")
live_ti = mets["tools_index_count"]["value"]
STALE = 37  # the exact stale number the real 03_comp_tools.md carried before this landed
assert live_ti != STALE, "test needs the live count to differ from the stale fixture value"

tmp = tempfile.mkdtemp(prefix="cs_metrics_test_")
prose_before = "The routed surface. Section 10 is the health overlay. See LD-0208."
doc = (f"# 03 fixture\n\n"
       f"{prose_before}\n\n"
       f"<!--cs:tools_index_count-->{STALE}<!--/cs--> tools in the manifest; "
       f"the delta = meta/enforcement.\n")
fixture = os.path.join(tmp, "03_fixture.md")
Path(fixture).write_text(doc, encoding="utf-8")

# Point the refresher at the temp dir.
_orig_dir = cs._MANAGED_DOCS_DIR
cs._MANAGED_DOCS_DIR = tmp
try:
    # report-only first: it should SEE the drift and touch nothing on disk.
    changes, problems = cs.refresh_managed_regions(mets, write=False)
    check("report-only run detects the drift", (("03_fixture.md", "tools_index_count", str(STALE), str(live_ti)) in changes), True)
    check("report-only run wrote NOTHING to disk", Path(fixture).read_text(encoding="utf-8"), doc)

    # write: it should correct the span to the live value.
    changes, problems = cs.refresh_managed_regions(mets, write=True)
    after = Path(fixture).read_text(encoding="utf-8")
    check("write corrected the span to the live count",
          f"<!--cs:tools_index_count-->{live_ti}<!--/cs-->" in after, True)
    check("the stale number is gone", f">{STALE}<!--/cs-->" not in after, True)
    check("surrounding prose is UNTOUCHED (only the span changed)", prose_before in after, True)

    # idempotent: a second write is a no-op.
    changes2, _ = cs.refresh_managed_regions(mets, write=True)
    check("second run is a no-op (idempotent)", changes2, [])

    print("== SAFE: UNKNOWN metric is refused, real number preserved ==")
    Path(fixture).write_text(
        "keep <!--cs:tools_index_count-->99<!--/cs--> here\n", encoding="utf-8")
    poisoned = dict(mets)
    poisoned["tools_index_count"] = cs._metric(cs.UNKNOWN, "forced", cs.UNKNOWN)
    ch, pb = cs.refresh_managed_regions(poisoned, write=True)
    after = Path(fixture).read_text(encoding="utf-8")
    check("UNKNOWN metric did NOT overwrite the existing number", ">99<!--/cs-->" in after, True)
    check("the UNKNOWN overwrite was reported as a problem",
          any(p[1] == "tools_index_count" for p in pb), True)

    print("== unknown metric NAME is reported, not applied ==")
    Path(fixture).write_text("x <!--cs:no_such_metric-->5<!--/cs--> y\n", encoding="utf-8")
    ch, pb = cs.refresh_managed_regions(mets, write=True)
    check("unknown metric name reported as a problem",
          any(p[1] == "no_such_metric" and "no such metric" in p[2] for p in pb), True)
    check("unknown-name span left unchanged", ">5<!--/cs-->" in Path(fixture).read_text(encoding="utf-8"), True)
finally:
    cs._MANAGED_DOCS_DIR = _orig_dir
    for f in Path(tmp).glob("*"):
        f.unlink()
    os.rmdir(tmp)

print(f"\n{PASS} passed, {FAIL} failed")

# GUARDED 2026-07-22 (0.8.0_AE_CloudComp). This is a standalone SCRIPT (see the docstring's
# `python org/modules/graph/tests/test_comp_system_metrics.py`) that lives in tests/ with a `test_`
# prefix, so pytest COLLECTS it and executes this module body at import. A bare module-level
# sys.exit() raises SystemExit during COLLECTION, which pytest reports as INTERNALERROR and which
# ABORTS THE ENTIRE COLLECTION -- so `pytest org/modules/graph/tests/` ran ZERO tests (not "some
# tests", zero) from 2026-07-14 until this guard landed, in CI and locally.
#
# The whole suite was dark, including test_sovereign_held_no_drift.py -- the anti-drift guard that
# had CORRECTLY gone red on a re-introduced sovereign-hold literal and whose RED nobody could see.
# comp-tool-tests.yml's own header warns that "a committed regression test that no gate ever runs"
# is the trap it exists to close; the gate was running, the suite was not. A green-looking gate over
# an empty collection is the same failure shape as a guard whose broad paths are dead.
#
# If FAIL is non-zero the script still exits 1 when run directly; under pytest it stays inert.
# FOLLOW-UP (not done here, not mine to redesign): convert these checks into real pytest functions
# so they are ASSERTED by the suite rather than merely importable by it.
if __name__ == "__main__":
    sys.exit(1 if FAIL else 0)
