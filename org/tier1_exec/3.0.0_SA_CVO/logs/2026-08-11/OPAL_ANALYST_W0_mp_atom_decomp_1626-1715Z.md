# OPAL_ANALYST W0 — Model Portfolios atom_decomp first run + delegated semantics pass
**archetype:** MIXED (VALIDATE-primary, with TRACE and DIAGNOSE)

**Agent:** `3.0.0_SA_CVO~Z` (site Z) · **Window:** 2026-08-11 16:26–17:15Z
**Authority:** Andrew-direct ~1020Z at the MSTR~Z terminal · **TO:** `OPAL_ANALYST.W0` @a438a40793
**Commit:** `cb4d65486f` (+ this window's follow-up) · **Certifier:** `1.0.0_SA_CTO~Z` (pending)

## What happened

Session opened on a sovereign GO, not a TO: Andrew delegated the semantics he would have written
and ordered this seat to run atom_decomp on Model Portfolios itself *"so that we validate every
little thing."* Startup (`/watcher`, registration, `org/XXX.md` 1b) then straight into the run.

**Delivered:**
- **The run** — `workflows/atom_decomposition/runs/portal-page-portfolios/20260811T1640Z/`.
  16 censused MP items × 10 fields across 3 declared planes = 160 cells. `c0` born UNMEASURED →
  c1 FILL → c2 VERIFY → c3/c4 convergence. **Final: 158 MEASURED, 2 NOT_MEASURABLE, 0 validator
  violations, status DRY.**
- **The semantic pass** — Andrew's 6-question block answered for all 16 in his stead, as MEASURED
  cells with per-cell evidence, provenance `CVO-DELEGATED`. 3 SERVE / 6 SERVE-WITH-CAVEAT / 7 DENY.
- **10 findings**, including a live user-facing defect.
- **The method read** (C10) — 6 defects in atom_decomp itself, with fixes, for CTO~Z before W1.
- **`OPAL_ANALYST.W0_PROOF_OF_SPEC.json`** — validator-clean, 10 acceptance rows, 0 violations.

## Findings (detail in the findings deliverable)

**F-1 is the one that matters today:** `PipelineProgress.tsx:432` renders
`<Link to="/model-portfolios">View Portfolios</Link>`. That route does not exist (`/portfolios`,
`App.tsx:408`), and `App.tsx:470`'s catch-all silently redirects to `/market` — so the button
labelled *View Portfolios* delivers Market Overview, with no error, and the sibling button above it
goes to `/market` on purpose. Admin-only page. Routed to CTO~Z; I author no portal code.

Then: `json/portfolios/**` (5 keys) absent from the census denominator → **487 keys, not 482**;
a live accessor fetching a key that does not exist; two artifacts frozen since 2026-06-01 behind a
`state: live` row; the vintage-field zoo measured at 8 forms, not 3; one artifact carrying two
as-of dates four days apart; and one deliberate **NON-FINDING** (`peer_performance` is healthy on
its own month-end cadence) recorded because a bar that only ever produces findings is not a bar.

## What I got wrong, and how it was caught

Worth more than the findings, because it is about the instrument rather than the estate.

1. **Cycle 1 came out 160/160 MEASURED — and that was the smell.** Re-reading it against my own
   domain bar found two cells whose *value* was "unresolved" while their *status* said MEASURED: a
   hole wearing a measured label, invisible in the hole census, which is the one instrument whose
   job is seeing holes. Downgraded to `NOT_MEASURABLE` with the discriminator named. Self-caught.
2. **Two producer cells were grounded on ABSENCE** ("no publish stamp, therefore no writer") —
   Rule 6 says absence is a coverage limitation, not a mechanism. Re-grounded at source on the
   publisher's own `SERVE_ROOT` scope.
3. **My own hand-counts were wrong twice**, caught by machine-checking the cycle-3 sweep against
   the rectangle instead of reciting it: a `decommission` substring match read 5 candidates where
   there are 2 (three were *negative* uses of the word), and a verdict tally read 4
   SERVE-WITH-CAVEAT where the machine count is 6. The second propagated back as a correction to
   the findings deliverable. **An undiscriminating matcher and an uncounted denominator — the same
   two classes this run kept finding in other people's evidence, arriving in mine.**
4. **DRY was not claimed when it was not earned.** First commit went out at status `OPEN` saying so
   explicitly; DRY came afterwards from actually running two zero-change cycles under *different*
   lenses (constraint sweep, then entity-row sweep), each emitting a `changes:[]` patch with a
   populated `unchanged_examined` so the no-op is an artifact rather than an assertion.

## Governance

- **Rule 14(e) author/certifier collision surfaced, not resolved unilaterally.** Andrew ordered the
  fabric's certifier to AUTHOR; the method forbids the author certifying. Surfaced same-turn with a
  recommendation, MSTR~Z ruled (163153Z) CTO~Z signs W0, adopted into PRD v1.1 §9.4. **No hold, no
  manufactured gate** — I proceeded and authored while the ruling was in flight.
- **Two Plane-C serve verdicts ride to Andrew as one confirm.** Widening is his by design; my
  delegation covers semantics, not widening — reading it wider would use his own delegation to
  erase his own control. Nothing is held on it.
- **Rule 24 self-check on my own field axis is recorded as FAILING postulate (iv)**, with the
  non-moving values named: "CVO authors the semantics" delivers Planes A and B entirely and
  structurally cannot deliver Plane C's widening subset.
- **Mutant planted, sealed and committed at plant time** so the disclosure cannot be retrofitted
  after the certifier's pass. `rectangle.final.json` is **not consumable SSOT** until the c3
  correction lands.
- **SYSPARITY:** `comp-system --check` reads GATE 06 STALE. Reported to MSTR~Z rather than
  self-authorized (the remedy rewrites tracked files on a shared tree mid-flight); ruled to fold in
  after certification, announced one turn ahead. **Zero crons armed** (LD-0175).

## Compiler Tools

| tool | invocation | result / what it decided |
|---|---|---|
| `ssot_validate` | `rectangle` ×3, `patch` ×4 | 0 violations at every stage; every merge went through the validator, so no hand-edited rectangle exists in this run |
| `comp-estate` | `comp-estate model-portfolios` | 8 chains; named the producer Lambdas + the yang S3-manifest trigger topology, which grounded the T-1 vintage semantics. **Topology only** — its freshness claims measured STALE vs live (2026-06-15 vs 2026-08-11) |
| `comp-find` | `_smartx_model`, `PUBLISH_MAP`, `platinum/mdpf`, publisher name | Source-confirmed the `_smartx` producer as an **operator-run script**, not a schedule (the mechanism behind F-4); source-confirmed the publisher's `SERVE_ROOT` scope, upgrading a producer cell off an absence inference |
| `comp-routes` | `comp-routes rewrites` | `/api/general/mdpf/ → platinum/mdpf/`. **DESIRED-plane only** by its own disclosure — never allowed to carry the verdict alone; paired with live successor freshness |
| `comp-system` | `comp-system --check` | GATE 06 STALE (181→183 fingerprint drift). Reported, not self-remedied |
| `aws s3` | `ls --recursive` ×6 prefixes, `cp` to stdout ×14 | 487 keys, **auto-paginated and counted client-side** (never `--query length()`, never `--no-paginate`); 14/14 fetched+parsed with the probe printing its own denominator; every ABSENT verdict positive-controlled in a **separate invocation** |
| `grep` (consumed end) | per-accessor over `portal/src` | 9/16 entities established zero-consumer at the **consumed** end (Rule 12) — changed verdicts producer-side reasoning would have got wrong |
| `proof-of-spec-check` | `<instance> C1..C10` | `acceptance rows=10 | violations=0 | VALID` |
| `comp-which` rail | one `# rail-checked:` override, audited | reading a python dict literal inside one named Lambda file; no comp-tool returns a source-level output-key map |

## Blockers

**NONE at me.** Armed on triggers, all owned: CTO~Z's certification verdict → I land the c3
mutant-correction patch and `rectangle.final.certified.json` same-turn, and C8 flips from
`UNCOMPUTABLE` to PASS (or the pass is reported VOID and re-run). Andrew's two one-line widening
confirms → the last 2 of 16 catalog rows. MSTR~Z's word on the SYSPARITY regenerate → fold in and
announce. W1 semantics arrive from 0.5.0 page by page; I named the output shape so they can build
to it rather than hand me something to reshape.

— `3.0.0_SA_CVO~Z`
