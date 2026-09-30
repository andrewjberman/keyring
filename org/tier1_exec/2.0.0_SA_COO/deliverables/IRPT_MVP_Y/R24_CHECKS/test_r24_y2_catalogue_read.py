"""R24 ~Y cell IB-yr-242 check: a sibling scoped GET serves the comparison catalogue, named or verbatim.

Why (walk-2 W2-04/W2-05, CTO 103026 placed it here; shape ruled at 103038; source ruled at 103035). The composer
documents its own gap: `GenerateComposer.tsx:20-25` -- ResolvedScope v1 "carries no catalogue of selectable
comparisons", so the control takes an OPAQUE KEY and prints 'Comparison {n}', and `composer.ts:187-204` refuses only
the cap and duplicates with no existence check.

The shape was measured before it was asked. `_contracts/ResolvedScope.schema.json` is `additionalProperties: false`
with 12 properties and 9 required, so the catalogue cannot be added to it quietly. CTO 103038 ruled shape **B**: a
SIBLING scoped GET, leaving ResolvedScope at v1, under the existing `/api/scoped/investor-reporting/` family behind
the same authz guard and tenant check, with its own new `_contracts` schema (v1, `additionalProperties: false`).

CTO 103035 ruled the source: the model catalogue plus etf-classifications, and **no substitution to bd-securities**
("Andrew is retiring bd-securities, so a new reader of it is the fork he named"). A ticker neither source names
**shows its ticker verbatim, never a positional label**. That degrade path is the point of AC3: ~M's census measured
etf_classifications at 285 items covering about one ticker in five, so MOST entries take the verbatim path and it
must not look like a bug.

Run from the repo root:
    python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y2_catalogue_read.py::<test>

- route_registered_under_the_scoped_family: the new GET is in the entry's ROUTES and under the existing family.
                                            FAILS at the base -- no such route.
- catalogue_contract_is_closed:             the new `_contracts` schema exists, is v1 and closed, and a built payload
                                            validates against it. FAILS at the base -- no such schema.
- unnamed_ticker_is_verbatim:                a ticker in neither source carries its TICKER and no positional label.
                                            FAILS at the base -- no builder.
- existing_surface_unchanged:                CONTROL. The POST analysis route still maps to `analysis-requests`, and
                                            ResolvedScope still has its 12 closed properties. PASSES at the base and
                                            must keep passing -- ResolvedScope staying v1 IS the ruling.

Each test that needs the NEW module imports it INSIDE the test, never at module scope, so the control stays runnable
while the cell is unbuilt. (An earlier battery in this round imported at module scope and took its own control down
with it, which makes a red criterion unreadable.)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
IR = ROOT / "infra/aws/lambda/investor-reporting"
GEN = IR / "ycharts/generate"
CONTRACTS = IR / "_contracts"
sys.path[:0] = [str(GEN), str(IR / "_scope"), str(IR / "_authz"), str(IR / "ops"), str(IR / "intake")]

FAMILY = "/api/scoped/investor-reporting/"
# the name the order tells the worker to create; the battery holds it so the cell cannot drift
MODULE = "comparison_catalogue"
SCHEMA = CONTRACTS / "ComparisonCatalogue.schema.json"


def test_route_registered_under_the_scoped_family():
    """The catalogue is served by a GET inside the existing scoped family (CTO 103038)."""
    import entry as generate_entry

    routes = dict(generate_entry.ROUTES)
    gets = {k: v for k, v in routes.items() if k.startswith("GET ") and FAMILY in k}
    assert gets, ("no GET route under %s is registered; ROUTES holds %r. CTO 103038 ruled a sibling scoped GET, so "
                  "the catalogue needs its own route key here and in the published routes.json." % (FAMILY, routes))
    for key in gets:
        assert "catalog" in key.lower() or "comparison" in key.lower(), (
            "the new GET does not look like the catalogue read: %r" % key)


def test_catalogue_contract_is_closed():
    """The new contract exists, is v1, is closed, and the builder's payload validates against it."""
    assert SCHEMA.exists(), (
        "%s does not exist. CTO 103038: the route 'gets its own new _contracts schema (v1, additionalProperties "
        "false)', and the portal validates against it." % SCHEMA.name)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert schema.get("additionalProperties") is False, "the new contract must be closed"

    import jsonschema
    mod = __import__(MODULE)
    payload = mod.build_catalogue(tenant="cottonwood")
    jsonschema.Draft202012Validator(schema).validate(payload)


def test_unnamed_ticker_is_verbatim():
    """A ticker neither source names carries its TICKER verbatim, never a positional label (CTO 103035)."""
    mod = __import__(MODULE)
    unknown = "ZZZZTESTTICKER"
    entry = mod.entry_for_ticker(unknown, tenant="cottonwood")
    text = json.dumps(entry)
    assert unknown in text, (
        "a ticker neither the model catalogue nor etf-classifications names must show its ticker VERBATIM; "
        "the entry was %r" % entry)
    lowered = text.lower()
    for positional in ("comparison 1", "comparison 2", "comparison {", "unnamed", "not supplied", "unavailable"):
        assert positional not in lowered, (
            "the unnamed entry carries a positional or placeholder label %r, which is the defect W2-04 exists to "
            "fix: %r" % (positional, entry))


def test_existing_surface_unchanged():
    """CONTROL: the POST analysis route is untouched and ResolvedScope stays v1 with its 12 closed properties."""
    import entry as generate_entry

    assert generate_entry.ROUTES.get("POST /api/scoped/investor-reporting/analysis") == "analysis-requests", \
        "the existing analysis POST route changed: %r" % generate_entry.ROUTES

    resolved = json.loads((CONTRACTS / "ResolvedScope.schema.json").read_text(encoding="utf-8"))
    assert resolved.get("additionalProperties") is False, "ResolvedScope stopped being closed"
    assert len(resolved["properties"]) == 12, (
        "ResolvedScope gained or lost a property (%d now). CTO 103038 ruled it stays v1 -- the catalogue rides a "
        "SIBLING read, not this contract." % len(resolved["properties"]))
    assert "comparison_catalogue" not in resolved["properties"], \
        "the catalogue was added to ResolvedScope; 103038 ruled shape B precisely to avoid that"
