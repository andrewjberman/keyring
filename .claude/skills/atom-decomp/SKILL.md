---
name: atom-decomp
description: Run the ATOM_DECOMP method on a named system, pipeline or estate surface: the entity-by-field rectangle, every cell {value, status, evidence}, fan-out until dry, certified with a sealed planted mutant. Use on `/atom-decomp <subject>`, "decompose X", "establish SSOT on X", or before a refactor, migration or decommission where deployed truth must be proven.
---

# /atom-decomp — ad-hoc invocation of the atomic-decomposition method

**THE METHOD LIVES IN ITS PACKAGE; THIS SKILL IS THE INVOCATION FRAME.** Never restate the method
from memory — read the canonical entrypoint and follow it:

> `projects/ATOM_DECOMP/skill/atomic-decomposition/SKILL.md`

That file carries the 14 rules (read-only start, state separation, denominators-with-instruments,
tool-failure-is-coverage-limitation, count-parity-is-not-identity-parity, ...) and the Rule-14
STRUCTURED-SSOT protocol: schema-generated rectangle → owner's DOMAIN BAR before measurement →
status-missioned fan-out (verify MEASURED / fill UNMEASURED / kill-or-promote INFERRED / challenge
NOT_MEASURABLE) → iterate UNTIL DRY → certify with the sealed-mutant protocol
(`rectangle.final.certified.json`, PASS / PASS-WITH-REFUSAL / VOID, certifier ≠ author). This shim
adds the estate frame:

## Step 0 — Scope the run

- **Subject:** one named system/surface per run (a pipeline, a Lambda family, a serving route, a
  bucket grammar…). No subject given → ask; Rule 2 (pin identity/environment/scope/denominator/
  consumer boundary) cannot start without it.
- **Posture:** read-only unless mutation is explicitly authorized (package Rule 1). An ad-hoc run
  is a legitimate QA/truth-establishment instrument; its artifacts are never production evidence
  and it changes nothing without its own authorization.
- **Grounding law applies on top:** live/served state for WHAT, source+graph for WHY; comp-tools
  first per the estate rail (`comp-which` routes the question).

## Step 1 — Execute per the package entrypoint

Follow the package SKILL.md and its references (`ledger_schemas.json`,
`ssot_establishment.schema.json`, `ssot_mission_rubrics.json`) verbatim. Fan-out agents return the
declared patch shape and merge ONLY through the validator; certification is signed by the standing
certifier seat, never the author; VOIDs accumulate in the run directory with their post-mortems and
are never overwritten.

## Step 2 — Land at the run home

```
workflows/atom_decomposition/runs/<subject>/<UTC-stamp>/     run.json + rectangle.c0.json +
                                                             patches/ + rectangle.final.json +
                                                             certification.json
```
(the layout `workflows/atom_decomposition/README.md` legislates; `run_id = <subject>__<stamp>`;
`run.json` carries the hole-census trajectory + the METHOD VINTAGE — which package commit ran).
Then recompile the view: `python workflows/atom_decomposition/compile_manifest.py` (the run ledger
+ `runs/INDEX.json` regenerate; `--check` must read CURRENT before you cite the manifest).

## Step 3 — Route, never repair

Findings are characterize-not-fix: a discovered defect on an owner's surface ROUTES to that owner
(via COO per standing dispatch); the run's deliverable is the certified rectangle, not landed
fixes. Rule 24 binds any enum/array/predicate the run authors or adopts.

## Cross-references

- Workflow home (compile-on-view manifest + run ledger): `workflows/atom_decomposition/README.md`
- Package (the portable unit): `projects/ATOM_DECOMP/**` per its `PACKAGE_MANIFEST.json`
- Sibling: `/atom-layer0` — conceptual-base atomicity + resolution contracts; use THAT skill for
  concepts, this one for deployed-system truth.
