# 4.0.0_SA_CRO -- Script I/O S-layer DESIGNED then DISSOLVED by Andrew's one-sentence question; eight-layer C/D field anatomy landed in the ontology home (2026-08-07 01:00Z -> 03:00Z)

**archetype:** EXPLORE
**secondary_archetypes:** DIAGNOSE, SCRIBE, COORDINATE

## Window

01:00Z -> 03:00Z. Prior log: `2026-08-06/bundle_ferry_closeout_and_standdown_1615-2000Z.md`.
New engagement, Andrew-direct, with `3.0.0_SA_CVO~C` (review + exercise) and `1.0.0_SA_CTO~D`
(architecture), CRO driving per Andrew's word at the CTO~D terminal.

## What happened

**1. Commissioned:** design a "script io" ontological layer -- line-level inputs/outputs for
field-level dependency and flow, Python + React/JS -- as the precursor to project coherence, of which
`ATOM_DECOMP` is the base. Mid-engagement correction, VERBATIM: *"we probably need to enhance this
somehwat with more classifications than simply input and output. need to figure out how to reconcile
this layer with D1 and C1."*

**2. Three revisions, each falsified by a different seat.**
- **REV 1** (@72279a7c2): S0 = SITES / S1 = BINDINGS (rejecting his input/output split as non-MECE
  under Rule 24), five axes, aggregating to C1 and witnessing D1.
- **REV 2** (@785ed481f): I bounded the denominator REV 1 admitted it had left open. It contained
  `recognizer_sdk` -- a wired FrontEnd SDK with capability tiers. **My §6 had specified BUILDING
  language adapters where an abstraction already existed.** Also corrected my own "75 first-party AST
  users" to **56** (the 75 included vendored Lambda-layer deps -- a `denominator_grain` defect
  committed inside a spec citing `denominator_grain`).
- **REV 3** (@2d40590fa): CVO~C falsified axis independence -- **Axis 3 was a META-axis over Axes
  1/2/5**, and already landed as `Coverage`. Axis 1 failed the intent test **I wrote for it**. And
  the unknown-unknown: **grain is observer-relative and I had asserted it as observer-independent.**

**3. ANDREW'S QUESTION DISSOLVED ALL OF IT.** *"Since it's all about data flow anyway... wouldn't
that sit at D1 anyway? What is in D1?"* I measured instead of answering from my own spec. **A live
`FLOWS_TO` edge carries `srcField`/`dstField`/`kind`/`rename`/`condition`/`via` (a FILE:LINE)/
`resolution` (the METHOD).** Seven capabilities specified, **seven already live** -- including the
`observer` field I had ADDED in REV 3, which `resolution` already was. **The layer was never
net-new.** Disposition: `SCRIPT_IO_S_LAYER_DISPOSITION_20260807.md` @118fb1585, amended @7280b1790.

**4. Root cause, and it is a law-surface finding:** I ran BUILD LADDER rung 2 against **EXTRACTION**
twice (it caught `recognizer_sdk` the second time) and **NEVER against the ONTOLOGY SLOT.**
**THE BUILD LADDER APPLIES TO SCHEMA, NOT ONLY TO CODE.** CTO~D raised it separately with my
co-sign (@611f0e18b).

**5. Side product that outlived the engagement:** `infra/system/ontology/LAYER_FIELD_ANATOMY.md`
(@015877662 -> @47d00a4e5) -- all **eight** layers (5 C-rungs + 3 D-rails) with purpose, field shape,
calculation, and up/down dependencies, every figure vintage-stamped and command-derivable.
**Andrew caught the banner reading "SEVEN" while listing eight items beside the word.**

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-kuzu` | ~12 queries: schema, node/edge census, layer distribution, props inspection, falsifiers | PASS + **decisive** | The `props` read is what killed the S-layer. Its own 0-rows warning ("an unmodeled class or wrong-pattern query returns 0 identically") is what made me negative-control every zero |
| `comp-which` | A.3 exercise + "inputs/outputs of a gold script at column level" | PASS | routed correctly to `comp-pipescript io`; forwarder EXERCISED (banner produced), not merely name-resolved |
| `comp-grep` | prior-art sweep for `script_io` | PASS | found `test_script_io_ast.py` + `_extract_script_io`, which set up the whole rung-2 finding |
| `comp-estate --layers` / `--definitions` | canonical C0-C4 + D1-D3 ladder and term registry | PASS | the authority for the anatomy file |
| `to-check.py --all` | own TOs + CVO~C + CTO~D | PASS | 0 rows all three -- confirmed no competing work before driving |
| `safe-commit.sh` | 9 commits, all `-F` | PASS | risk-reflex HOLD fired on `prompt.md` and correctly sent me to a memory citation |
| `audit-archive-invoker` | startup A.2 | PASS | rc=0, 0 findings, snapshot not-due |
| **GAP** | `comp-claimlink` | UNRESOLVED | 96 of 97 comp-tools resolve bare; this one does not (known -- CVO~B placed it minimally to unwedge the coverage gate 2026-08-06) |

**What worked:** measuring instead of answering from the spec, every time. The five moments that
mattered were all a query, not an argument -- the `props` read, the portal-only falsifier, the
`PROP_PASSES` census, the header count, and the positive control on `/c` at startup.
**What failed:** nine corrections, mine and others'. **Every one had the same shape -- the
measurement was real and the thing it was evidence OF was not what was claimed.**
**Gap found:** `edge.layer != node.layer` -- `WHERE e.layer='portal'` returns 0 while 4,453 portal
field edges exist. Recorded in the anatomy file; no owner routed (it is a producer convention, not a
defect I can attribute).

## MCP traffic

**OUT:** CVO~C x6 (review request, stop-read, REV 2/3 notices, attack brief, stand-down + close);
CTO~D x6 (ACK, arch call, deciding-measurement result, retraction ACK, disposition, close); MSTR x2
(prefix advisory + follow-up); CVO~B x3 (ACK, correction, vintage close).
**IN:** CVO~C x7 (ACK, review, retraction, exercise, attack-4, locus census, close); CTO~D x8
(live, §7 read, addendum, retraction, arch ruling, converged, correction, RAVC close); CVO~B x3.

## Blockers

**None at me.** Two items sit at **Andrew** and neither blocks anyone: **(a)** the held-out fence
scope -- now sharpened to a **directory-listing collision** (ADVI sorts alphabetically FIRST in
`portal/src/api/endpoints/`, so any systematic audit of the portal template hits held-out surfaces
**by construction**; and the live C3 `EmergentSystem`'s constituents are ADVI surfaces); **(b)**
placement into `projects/ATOM_DECOMP/` which is lane `TIER0_MSTR`.

## Current State (zero-context handoff)

- **S-layer: DISSOLVED.** No new rung, no `S0`/`S1`, no `sits_inside:`, no naming act. The real work
  is **populating D1 field grain on the `aws`/`pipeline` substrates** -- a pure BUILD, and it has
  **left the CRO lane**: PRD -> `1.0.0_SA_CTO~D` (sequenced BEHIND their 3-week-old COMPLEARN P3a
  ruling, on my advice), TOs -> COO, verification -> `3.0.0_SA_CVO~C`.
- **`SCRIPT_IO_ONTOLOGY_SPEC_20260806.md` is HISTORY, not a design** -- REV 3 frozen under a
  superseding banner; the disposition supersedes it.
- **Four defects the build inherits, declared:** no locus on `PROP_PASSES` (0/1382; field-flow locus
  **41%**, not 100%); 9-of-14 locus precision where present; `condition` on 4.8% against an exact
  count; `row` grain unpopulated estate-wide and likely FORCED by Python extraction (largest cost).
  Offsetting: D1's own LIVE claims audit **3 of 4 clear**.
- **Andrew's stop-condition is NOT self-assessed as met.** The Script I/O *question* is closed and
  exercised; the *capability* is unbuilt, so "meshed into our system" is not true yet. **Proceeding
  to `atom_decomp` is his call, deliberately not inferred.**
- **`/loop` 10m armed** -- cron `57624188` (`4,14,24,34,44,54`), session-only, 7-day expiry.
