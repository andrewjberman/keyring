# W4c-1 certification + W4b tranche 2 — CVO~Z session, part 2
**archetype:** MIXED (VALIDATE + IMPLEMENT)

**Agent:** `3.0.0_SA_CVO~Z` · **Window:** 2026-08-12 17:45–18:10Z
**Commits:** `7bc094ac5c` (certification) · `5e5b707e52` (tranche 2 + guard repair 2)
**Prior part:** `CVOZ_W4b_semantics_tranche1_and_guard_repair_1701-1745Z.md`

## W4c-1 `/ticket-center` — CERTIFIED

First real packet of the session. Preempted W5 prep and W4b authoring by standing rule, ACKed in the
same turn, read `WCERT_PREDECLARATION.md` before the rectangle so the author's §2 could not install my
framing ahead of the evidence. **`MUTANT_SEALED.md` unopened** — and stated in the certification
rather than implied, with the note that its `atime` advanced because of **my own `ls`**, which is
itself proof atime is not a seal oracle.

**Plant caught: `tc.01.consumer_set` = "2 call sites"; truth is 1.** Falsified four independent ways
— source (`:97` is `setTickets(...)`, a state setter), the cell's own declared K2/K8 "per CALL SITE"
instrument, sibling `tc.02` scoring the identical shape as 1, and `tc.01`'s own `invocation_surface`
reading 1. Fifth tell: the cited `:97-98` range reaches into **tc.02's** data flow. Denominator:
`comp-find 'listTickets'` = 3 hits (definition + import + one call); K2/K8 excludes two by name.
**Hypothesis recorded to the author before opening either of their self-reports.**

**It is a good plant because it reads as the MORE careful answer** — real line numbers, a principled
rationale — so a verifier who rewards thoroughness reads 2 as diligent and 1 as lazy.

**Headline attacked hardest, as asked, and it SURVIVES.** Downloaded the deployed package
independently; zip sha256 matched the cited hash exactly. Enumerated every conditional and every
actor-field use: all five uses are stamps, zero conditionals put `actor[...]` on either side of a
comparison. **The near-counter-example I checked and rejected:** `:136-139` compares an assignee — but
to a **caller-supplied query parameter**, not the caller's identity. **What my read adds:**
`list_tickets` applies **no firm filter either**; firm is stamped at creation and never read back as a
predicate. That strengthens the finding CTO~Z routes to Andrew. No route invoked, no cross-firm read.

**Method amendment adjudicated — all three artifacts present** ((a) lint exercised with misfires on
the record, (b) `UI STATES EXERCISED: 0` declared, (c) coverage disclaimer verbatim). No undeclared
intersection region; my pre-declared refusal condition did not trigger.

**§3 separated as the author asked:** scope defence on `tc.06.vintage_grain` UPHELD, expression
DEFICIENT. Neither laundered the other. Their own denominator correction accepted after checking the
reasoning: 24/24 locators lack a component token but only **1** owes one, because 23 are reason-class
KIND where naming a component would invent a locus for a property that does not apply.

## W4b — 48 of 210 delivered

Denominator moved **174 → 210** (c8 amended the entity set 29 → 35), exactly the floor-not-total
caveat filed at 1740Z. Join re-run against `c10`: **ready runway 30 → 96 cells.**

**Tranche 2 (30 cells, 5 entities).** The finding is in `advi.11`: **one page serves two firm AUA
totals.** `header_metrics.total.aua` = 1,911,578,939.87 against four independent siblings at
1,778,539,360.83 — +$133,039,579.04, +7.480%, same firm, same `data_as_of`. **And the artifact
disagrees with itself:** its own `by_architect.aua_pct` values are computed against the *sibling*
total (Travis Penfield 23.4% checks against 1.7785B, not against its own 1.9116B). Producer not read;
no cause asserted. Separately, `by_architect` covers ~81% while carrying an `Unresolved` row — it
**looks** exhaustive and is not.

`advi.05` recorded as an entity with **no artifact and a live consumer**; disposition BROKEN-CONSUMER
and deliberately not a recommendation, since abandoned-producer and vestigial-consumer are
indistinguishable here and take opposite actions.

## Reconciliation with AE~Z — resolved in my favour, and the disclosure mattered more than the finding

Their c9 labelled `advi.01/03/08` ARTIFACT-ABSENT under a declared bd bound; I had called the same
zeros false absences. **The measurement was right and the LABEL was wrong** — a cell reading
ARTIFACT-ABSENT is true-under-its-bound and false to any reader who does not carry the bound, and the
bound lived in the commit message. They retracted four cells `@5d6657564d`.

**I held the evidence that would have settled it and declined to send it**, because its authorization
was under CTO~Z adjudication. That was not a hypothetical courtesy: they had **already built** a c10
draft settling all four cells off their own cross-firm reads and discarded it uncommitted on receiving
my message. **And the correction needed no cross-firm read at all** — the accessor names carried the
firm scoping in our own repo. *The probe I was not authorized to run was also the probe I did not
need.*

Their sharpening, which binds my own join: **`advi.04`'s accessor is `getClientDirectory`, with no
`Inflection` tell** — so the cheap grep fix corrects three rows, leaves the fourth wrong, and looks
systematic while doing it.

## The guard, repaired a SECOND time

The completeness limb scored against `fillable` = every UNMEASURED cell, which includes Plane-A cells
the author has not reached — so it demanded I fill the author's plane, **the exact violation the other
two limbs forbid.** >> **Tranche 1 passed only because I had selected the entities whose Plane-A was
complete, making `fillable` coincide with my six fields. The selection criterion that made the first
payload easy is what hid the defect.** << Fixed as `entitled = fillable & axis_bc`, with four checks:
tranche 2 clean, tranche 1 no regression, and **both** control directions still firing.

Two defects in my own guard in two hours, both found by *using* it, both invisible to the payload
before.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` (content) | `listTickets` in `portal/src` | DENOMINATOR 3 of 403 — the plant's falsifying count |
| `comp-find` (content) | `NMNC`, `field_planes`, `planes_B_C_certifier` | definition-site grounding; my guard is the only code reader of either key |
| `semantics_payload_guard.py` | tranche 2 × c10, + 4 controls | caught its own defect; repaired and re-verified both directions |
| `aws lambda get-function` + `curl` | deployed package of `opal-ticket-api` | sha256 matched the author's citation exactly; 273 lines |
| `aws s3api get-object` (FULL files) | 3 bd platinum artifacts | the AUA disagreement — range reads had produced unparseable truncated JSON |
| `aws s3 ls --recursive` | `platinum/firm/`, materialised | 15 keys, counted client-side |
| `safe-commit.sh` | ×2, lane author, `-F` | `7bc094ac5c`, `5e5b707e52`, risk-reflex CLEAN both |

**Instrument note:** my first range reads (`bytes=0-1300`) produced truncated JSON that failed to
parse. Had it parsed, I would have quoted a number from a partial artifact — a denominator with no
frame. Re-read as full files before any figure above was recorded.

## Blockers

**NONE self-blocking.** 78 cells remain behind the bd/inf firm-status question at Andrew — surfaced,
recorded UNMEASURED with component named, never `NOT_MEASURABLE`. 96-cell runway in front of it.

— `3.0.0_SA_CVO~Z`
