# S1 FINDING — the attribution "89% failure" is THREE errors stacked, and the top one is a New Axis error ABOVE the one everybody is looking at

CORRECTS: org/tier1_exec/3.0.0_SA_CVO/deliverables/SPEC_kimi_call_subdivision_and_insight_strata_20260805.md -- the "89% fallback" is a COMPOSITE; ~2/3 are records no resolver can chain
STALE-MARKER: 89% of paths land in fallback labels


**Seat:** `3.0.0_SA_CVO` (SIGNAL half of the comp-tool split @7a3e7117d).
**Frame:** Andrew's denominator-error taxonomy, stated at this terminal 2026-08-05 ~1615Z —
New Axis (Case C) · Grain Shift · Semantic Redirect · Vocab Missing · Merge/Split.
**Data:** the 2026-08-05 estate report (first scheduled fire), 357 changed paths, 14 buckets.

⚠ **The taxonomy is NOT in the searchable record under those names** — `comp-grep` scanned 22,307
files; the only "Case C" hits are unrelated portal panel variants. Recorded here as Andrew stated it,
pending his confirmation of the canonical form.

## What I actually measured

| | paths |
|---|---|
| Fallback-labelled (`area:*` + `UNRESOLVED`) | **347** |
| Real canon entities (`producer:*`, `yang-*`) | **10** |
| — of which `area:governance` alone | **221** (64% of all fallback) |

Then split the 347 by top-level directory:

| top-level | paths | has a semantic vertical? |
|---|---|---|
| `org/` | 221 | **NO — by nature.** Agent logs, audit snapshots, ledgers, rulings |
| `docs/` `rcg/` `.claude/` | 22 | **NO — by nature** |
| `infra/` | 50 | **YES, should resolve** — Lambda/EC2 code |
| `.tools/` | 26 | **YES** — the comp-tool estate |
| `workflows/` | 15 | **YES** — Bloomberg / vendor-watch |
| `data/` | 8 | **YES** — pipeline scripts |
| root config (`CLAUDE.md`, `.gitignore`, `.gitmodules`, `.owned-paths.yaml`) | 4 | **NO — my own mis-class, see below** |

**⚠ CORRECTION TO MY OWN MEASUREMENT:** my first pass counted those 4 root config files as
"addressable estate artifacts." They are repo governance, no more resolvable than `org/`. **The
addressable set is ~99, not the 104 I first computed.** Recording it because a denominator I
overstated by 5% inside a finding *about* denominator errors is exactly the thing this file is about.

## The finding: THREE stacked errors, and the top one is new

**1 — NEW AXIS, at the TOP level, above the area-vs-producer problem everyone is looking at.**
**243 of 357 paths (68%) are not estate resources at all.** They are the fabric's own paperwork —
agent session logs, audit-archive snapshots, ledgers, rulings, PRDs. A "changed RESOURCES" list that
contains `org/audit/archive/.baseline` is not mis-labelling a resource; **it is asserting that a
governance record IS a resource.** That is a New Axis error one level above the `area:*` vs
`producer:*` conflation I filed this morning, and it is bigger: it is the majority of the report.

*Aggravating detail: the 221 is inflated by the fabric's own machinery. A single audit-archive
snapshot commit mints ~15 paths in one event. **The largest bucket in the daily estate report is
substantially the report-adjacent bookkeeping of the agents writing it.***

**2 — NEW AXIS again, one level down** (filed 1615Z, unchanged): `producer:*`/`yang-*` is a
**runtime-artifact** axis; `area:*` is a **filesystem-location** axis. Two axes, one field.

**3 — GRAIN SHIFT, necessarily, once (2) holds:** `area:governance` carried 221 paths / 224 commits /
17 authors; `yang-factor-tilts` carried 1 path / 1 commit / 1 author. Same field, same report, grains
three orders apart. **Semantic Redirect** is the mechanism hiding both: a path that fails to resolve
is silently demoted to a location label, and the reader cannot tell an answer from a fallback.

## Why this reframes the number I have quoted all day

**"10 of 357 chain-resolved = 89% failure" is wrong three times over.**

- 243 of those paths **should never have been in the denominator** — they have no vertical by nature.
- The addressable set is **~99 estate paths**, of which 10 resolve.
- So the real attribution gap is **~90 of ~109 addressable paths (83%)** — on a denominator **3.3×
  smaller** than the one I have been citing to four seats.

**The failure is real and roughly as severe; the SIZE of the fix is a third of what I said.** And the
target is concentrated and legible: `infra/` 50, `.tools/` 26, `workflows/` 15, `data/` 8.

## Recommendations — verification findings, NOT design

- **R-A (P0, and it is cheap):** exclude org-records from the resource axis, or give them their own
  declared axis. **Not** a resolver improvement — a scope correction. It removes 68% of the noise and
  it is the reason proposals keep landing on `area:governance`, which is *by nature* un-proposable.
- **R-B (P1):** the two-field split — a location field and a semantic-vertical field, independently
  populated, with **unresolved being an honest empty on the vertical axis** rather than a silent
  demotion to the location axis. Precedented in our own law: Rule 24's type specimen is exactly this
  shape (RCG charters v1 → v2).
- **R-C (P1):** `infra/` is the single biggest addressable win at 50 paths, and Lambda/EC2 code maps
  to producers more directly than anything else in the set. Start there, not with `data/` (8 paths).

**Not mine to build.** Attribution modelling is `1.0.0_SA_CTO~B` with CTO on the architecture gate.
This sizes the problem and names its class; it does not specify the remedy.

-- 3.0.0_SA_CVO
