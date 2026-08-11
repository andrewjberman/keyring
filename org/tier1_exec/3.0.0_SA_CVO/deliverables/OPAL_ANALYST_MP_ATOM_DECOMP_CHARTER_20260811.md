# OPAL_ANALYST — Model Portfolios atom_decomp: CHARTER + DOMAIN BAR

**Run:** `opal-analyst-model-portfolios__20260811T1640Z`
**Author:** `3.0.0_SA_CVO~Z` · **Certifier:** `1.0.0_SA_CTO~Z` (ruled 2026-08-11 163153Z, MSTR~Z discretion under LD-0090, surfaced to Andrew)
**Method:** `projects/ATOM_DECOMP/skill/atomic-decomposition/SKILL.md` Rules 1–14
**Authority:** Andrew-direct 2026-08-11 ~1020Z at the MSTR~Z terminal, VERBATIM (record: `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/ANDREW_DIRECT_20260811_OPAL_ANALYST_ATOMDECOMP_PROGRAM.md`):

> *"CVO~Z validates and provides the relevant semantics that I would have done, I think it's
> fairly obvious what they'd be, and for the first run only on "Model Portfolios" i want CVO~Z
> to run atom_decomp on that so that we validate every little thing."*

---

## §1 — Objective and the decision it enables

**Objective:** establish the Model Portfolios vertical's served-artifact SSOT as a certified
rectangle — every censused MP artifact × a field set that joins its **measured serving state** to
its **ratified semantics** — so that (a) every little thing is validated, and (b) the semantic
layer Andrew would have authored exists as MEASURED cells with evidence rather than as prose.

**Decisions this enables, named:**
1. `DATA_CATALOG` **v0.2** MP rows can be built (PRD §8.2 declares it will consume exactly
   `semantics:` / `census_ref:` / `vintage_field:` / `vintage_grain:` — this run produces all four).
2. The OPAL_ANALYST serve/deny posture per MP artifact becomes explicit rather than implicit in a
   channel allowlist.
3. The disposition of the nine **served-but-unrendered / frozen** items (the residue plane) gets a
   named verdict instead of remaining an open census section.
4. It calibrates the method itself: this is the FIRST run under the delegated-semantics model, and
   the steady-state loop (0.5.0 authors page-by-page → CVO~Z supplies semantics) is scored on it.

**Authority / mutation mode:** READ-ONLY on all estate state (Rule 1 — no mutation is authorized by
the sovereign word above, and none is required). Writes are confined to this run's own artifacts
under `workflows/atom_decomposition/runs/` and this deliverable set.

## §2 — Identity, scope, denominator, boundaries (G0)

- **System identity:** the Model Portfolios vertical of the Opal portal as SERVED — route
  `/model-portfolios`, its four locations, and every S3 object under the MP thread.
- **Environment:** PROD serving surface (`opal-data-portal-v2`), portal DEV tree at the SITEZ
  submodule pointer.
- **Entity denominator:** the **16 censused MP items** of `ARTIFACT_CENSUS_MP.yaml` @0c1dae3da —
  7 visually rendered + 9 served-but-unrendered/frozen. That census states its own denominator as
  **482 keys** under the vertical, collapsed to 16 entries by two declared rules (scope-family
  dedup — one canonical entry per `{scope}`-parameterized type; and prefix-collapse for the
  `_manifests/**`, `archive/**`, `json/mdpf/**` families). **This run inherits that denominator and
  is bounded by it**: an artifact absent from the census is absent here, and §6 states how that
  boundary is probed rather than assumed.
- **Consumer boundary:** the portal frontend (`portal/src`) and `portal_lookup.py`'s channel map.
  Anything consuming these keys outside those two surfaces is OUT of scope and named as external.
- **Exclusions with reasons:** Pod-2, Macro and News verticals (separately censused; News is
  deliberately last per the ruled vertical order). Non-MP platinum scopes are IN via scope_family.

## §3 — THE DOMAIN BAR (Rule 14b — stated BEFORE any measurement)

The bar declares, in advance, what counts as **expected variance** versus a **finding**, so that a
surprising number cannot be retro-fitted into either. Three planes, each with its own bar, because
they do not share one:

### Plane A — MEASURED FACT cells (`producer`, `serving_state`, `consumer_set`, `vintage_grain`)
| | |
|---|---|
| **Expected variance** | Census prose and my live read differing in *wording*, *byte counts*, *LastModified*, or a vintage date advancing since 2026-08-10. A vintage that is stale in wall-clock but current on the **trading-day frontier** is HEALTHY, not a finding (CLAUDE.md NEVER#1 — `peer_performance` is month-end by design; MDPF platinum is T-1). |
| **A FINDING** | A census claim that is FALSE at the live artifact or at source: a producer that does not write the key; a `state: live` on a key with no live object; a `consumer_evidence: zero callers` contradicted by a real caller; a declared `vintage_field` absent from the object. |
| **Instrument** | Live S3 / `portal_lookup` reads for artifact state; **source reads** of `portal/src` and the publisher for producer/consumer. A census row is a MAP, never the territory (Rule 22). |

### Plane B — RATIFIED SEMANTIC cells (`canonical_name`, `business_meaning`, `vintage_semantics`, `disposition`, `notes`)
| | |
|---|---|
| **Expected variance** | Reasonable wording differences; a business meaning that is terse. These are *authored under delegation*, so their evidence class is DECISION, not DATA — and that is correct, not a weakness. |
| **A FINDING** | A semantic claim that contradicts a Plane-A cell (e.g. calling an artifact the source of a figure the portal does not read from it), or a `vintage_semantics` that misstates the grain the artifact actually carries. **Semantics that cannot be stated without inventing a fact are NOT_MEASURABLE, never guessed.** |
| **Authority** | Andrew-delegated 2026-08-11 (the verbatim above). Cells carry `CVO-DELEGATED` provenance, never "Andrew said". |

### Plane C — `analyst_serve_verdict` — DECLARED SEPARATELY BECAUSE ITS STABILITY FRAME FAILS
| | |
|---|---|
| **Expected variance** | A SERVE verdict on an artifact **already** inside the approved `BUCKET_ALLOWLIST` / `REQUEST_CATALOG` / the ruled `json/capital-markets` add — that is describing an existing entitlement, which is delegated semantics. |
| **A FINDING / AN ESCALATION** | A SERVE verdict that would **widen** serving beyond what Andrew has already approved. **Widening is Andrew-only by design** (PRD §4.4, and §8.2's capital-markets precedent, where an *already-approved* row's channel add was still ridden to him as a one-line confirm). |
| **Disposition** | I answer Q4 for all 16 — that is the delegation and I execute it in full. The subset whose answer would widen is marked `CVO-RECOMMENDED — RIDES TO ANDREW` and listed in one block for a single confirm. **This is not a gate I am manufacturing** (no-gates law, 2026-08-06): it is the existing widening mechanism, and I neither hold the run nor hold any other seat's work on it. |

### Why the bar is three planes and not one — a Rule 24 self-check on my own field axis
Rule 24 binds **every labeled axis at authoring time**, including this rectangle's field set.
Scored honestly against the four postulates:

- **(i) MECE** — pass. Ten fields, no overlap; `notes` is Andrew's own catch-all (Q6) and is
  scoped to "anything else on this item", not a second meaning column.
- **(ii) SAME GRAIN** — pass. Every field is a property of ONE served artifact.
- **(iii) INTENT COHERENCE** — **would FAIL as one axis**, and the three planes are the remedy, not
  a disclaimer: fact and judgment on one axis is exactly the mix the postulate forbids. Declaring
  `plane` per field discharges it — each plane serves one intent and carries one evidence class.
- **(iv) STATE COHERENCE** — **FAILS on Plane C, and I am naming which values do not move**, which
  is what the postulate asks for. The obvious remedy (I measure and author) delivers Planes A and B
  **entirely** and **structurally cannot deliver Plane C's widening subset** — no amount of my work
  ratifies a widening. A plan that reads "CVO authors the semantics" therefore silently covers
  9/10ths of its own axis. That residue is a one-line sovereign confirm, not a work item, and it is
  surfaced at delivery rather than discovered later.

### Standing bar on the run as a whole
- **Until DRY, never to a count** (Rule 14d): iterate until consecutive cycles produce zero status
  changes. A cell count is not a stop condition.
- **A cell that is not MEASURED is never cited as fact** (Rule 14f).
- **Coverage limitation ≠ absence** (Rule 6): a tool that fails reduces coverage and is recorded
  as `NOT_MEASURABLE` with the reason, never as a clean negative.
- **Count parity is not identity parity** (Rule 10): the 16-vs-482 collapse is verified by
  *membership*, not by re-deriving the same total.

## §4 — Method boundaries, declared not discovered

1. **Population is DIRECT, not by status-missioned fan-out.** Rule 14(c) prescribes a fan-out of
   sub-agents; `org/XXX.md` bans the Task/Explore agents outright ("do the work directly"), and
   Andrew's word puts *me* on this run so that every little thing is validated. I therefore
   populate every cell myself and cite per-cell evidence. **Recorded as a method boundary in
   `run.json`, not omitted** — the cost is that no cell gets an independent second author before
   the verify pass, which is precisely what CTO~Z's certification pass exists to cover.
2. **P0–P12 is not run in full.** This is a served-artifact SSOT run over an already-censused
   vertical, not a migration. Phases whose omission cannot affect the conclusion (migration waves,
   cutover, drain) are omitted **as declared boundaries** — nothing here authorizes a deletion, and
   Rule 9 is untouched because nothing is deleted.
3. **The census is INHERITED as the entity denominator but NOT as evidence.** Every Plane-A cell is
   re-grounded on the live artifact or at source. Where my read and the census disagree, the
   disagreement is the finding and both are recorded (Rule: retain the contradiction record).

## §5 — Gates in force

`G0 Scope` — discharged by §§1–4 above (identity, authority, mode, denominator, boundaries, bar).
`G1 Current state` / `G2 Reconciliation` — worked by the run.
`G3`–`G7` — **NOT APPLICABLE and declared so**: no target contract change, no migration wave, no
cutover, no cleanup, no deletion is proposed by this run. A disposition cell reading
`decommission` is a **recommendation entering the normal route**, never an authorization — Rule 9
stands and nothing retires before its replacement is verified.

## §6 — Known questions carried into the run

1. Does the 482→16 collapse hide a served key with no census row? (Probed by membership, not total.)
2. Are the nine `unrendered` rows still unrendered at today's portal HEAD, or has a consumer
   appeared since 2026-08-10?
3. Do the three measured `vintage_field` variants (`data_as_of`, `_provenance.source_vintages`/
   `as_of_last`, `as_of`) hold across all 16, or is there a fourth?
4. Is `json/yang/volatility_data.json` (a 180-byte 2026-01-14 orphan) genuinely unreferenced?

---

*Domain bar fixed at 2026-08-11T16:40Z, BEFORE any measurement in this run. Any later amendment to
this section is itself recorded as a finding, with its reason — a bar moved after seeing the data
is not a bar.*
