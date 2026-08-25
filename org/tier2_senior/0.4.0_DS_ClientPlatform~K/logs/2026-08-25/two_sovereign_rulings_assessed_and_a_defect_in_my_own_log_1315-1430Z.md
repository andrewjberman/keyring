# Two sovereign rulings assessed against a delivered artifact, and a defect in my own log — `0.4.0_DS_ClientPlatform~K`

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

**Date:** 2026-08-25
**Window:** ~13:15Z–14:30Z (delta since `a5aa4196c5`)
**Task Order:** `D3_MODELOVERLAY.TO-R1-DS` — COMPLETE and ACCEPTED; this window is post-delivery
**Status:** COMPLETE

---

## Objective

Post-delivery window. `TO-R1-DS` was accepted at 13:18Z. Two Andrew-direct rulings landed after
that, both relayed to me. The whole job of this window was deciding whether either touches a
delivered artifact — **and measuring that rather than asserting it**, since the flattering answer
("no impact") is also the cheap one.

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| — | none required this window | see note |

**Why none:** this window ran no estate search. The two probes were a **single-file** grep over
`b04_account_model_membership.py` and a **single-file** grep over `org/missions/DIRECTIVES.yaml`,
plus a python column read of three S3 partitions. Rule 21's rail governs estate/repo-wide search;
single-file reads and operational data-plane reads are free and no comp-tool answers them better.
The delivered work's comp-tool record is in the prior log (`a5aa4196c5`).

**What worked:** the column-census probe was the right instrument — it answered "could b04 have
filtered on supervision?" in one read, and the answer turned out to be structural rather than
behavioural.

**What failed — and it is the retrieval-control class this estate keeps naming:**
`git log --oneline --author="0.4.0_DS_ClientPlatform~K" --since="2026-08-25 12:00"` returned
**CLEAN EMPTY**. Both commits exist. `--since` with that date format silently matched nothing, and
an empty result from a log query reads as *"you have no commits"* rather than *"your query was
malformed."* Caught by running the query **without** `--since` and cross-checking both hashes
directly — a control, not care. **A retrieval failure returns a value.**

**Gap found:** none new; this is `CONTROLS_OVER_CARE` behaving exactly as documented.

---

## Work Completed

### 1. `TO-R1-DS` accepted (COO 70532)
Verified independently at COO's seat rather than taken on my report: instance 28,199 bytes,
`proof-of-spec-check` VALID rc=0, alignment 16/16 both directions. Routed to `3.0.0_SA_CVO` for
cert. Acked.

### 2. Andrew-direct ~14:05Z — "whole book is the default" (relay 70672)
> *"For 49 we display the whole book... whether or not we or the advisor takes fees on it, but
> Cottonwood specifically had that request that their book be displayed as only that which is
> 'Supervised' on their behalf."*

**Checked whether it touches `b04`. It does not, and the reason is structural:**

- **No supervision/fee/billable/managed/discretionary predicate exists in the module.** Every
  `.loc[]` is join-disposition classification.
- **The distinction is not expressible in my sources**, measured on the 08-24 partitions:
  `fact_allocation_account_map` 9 cols — none supervision-ish; `fact_model_allocation_roster`
  13 cols — `advisor_*` are IDENTITY, not supervision; `fact_acc` 95 cols — only
  `managed_account_money_manager` / `managed_account_investment_strategy`, which are STRATEGY
  attributes.

So `b04` is whole-book **by construction, not by intent** — it could not have filtered on
supervision had someone wanted it to. **No rework.**

### 3. Andrew-direct ~14:12Z — all work sits under a directive (relay 70692)
Two halves. The **mechanism** (tag a project to its directive AT MINT) does not touch me — I
minted no project JSON this session. The **principle** I checked against my own project rather
than assuming the dispatching seat had: `org/missions/DIRECTIVES.yaml:69-74`, directive D3 lists
`projects: [D3_MODELOVERLAY]`. **It is a member** — in CTO's "active AND a directive member"
bucket of 12, **not** in the 91 orphans or the 49 with open TOs. A confirmation of their census,
not a correction.

### 4. Found and fixed two defects in my own prior log
Running `/log` against the standard surfaced that `a5aa4196c5` was **non-conforming in two ways**:

| defect | standard | fix |
|---|---|---|
| written to `logs/` flat | `logs/{YYYY-MM-DD}/` — every sibling lane uses it | `git mv` into `logs/2026-08-25/` |
| **no `**archetype:**` tag** | non-negotiable, single line after the title | added `IMPLEMENT` + secondaries |

The archetype tag is the one that matters: it feeds the stimulus-scan's cost signal, so an
untagged entry is **invisible to the instrument that consumes it** — not merely untidy.

---

## Decisions Made

1. **Measured the sovereign ruling against the artifact rather than reasoning about it.** "No
   supervision filter exists" is a claim about code; "the distinction is not expressible in the
   sources" is a stronger claim about data, and only the second one survives a future edit.
2. **Stated my denominators' plane unprompted.** COO warned that reading the $226.7M gap as a
   supervision effect is reading a **custody** effect. My universe is
   `schwab/08335338/silver/fact_acc` — custody-scoped by the prefix before any logic of mine runs
   — so my 7,340-account universe must not be differenced against BD's all-custodian or
   supervised-only totals. Recorded so my denominator is not later read as answering a question
   it never asked.
3. **Filed one forward hazard and deliberately kept it narrow.** Cottonwood's supervised-only view
   is now a *display rule keyed on a partner request*. My own AC6 invariants — 17b (serving work
   stays out of gold) and D3-e-1 (COT inherits by template, never a fork) — together mean the COT
   sibling of `b04` **must not** filter to supervised-only in gold. Framed as *where* a ruled view
   may be implemented, never *which* view a partner gets: COO recorded the whole-book preference
   as **opinion** with unnamed partners UNRULED, and the scope-adjudication prohibition binds in
   the widening direction too.
4. **Touched no member set.** CTO scoped the 91-project migration as unauthorized and named the
   register as MSTR's; assigning a project to a directive is a judgment about which directive it
   serves. Stated the non-action so silence is not read as coverage.

---

## Files Modified

| file | change |
|---|---|
| `logs/2026-08-25/d3_...1225-1315Z.md` | moved from flat `logs/`; archetype tag added |
| `logs/2026-08-25/two_sovereign_rulings...1315-1430Z.md` | NEW — this file |

No code, infra, or deliverable changed this window. `b04` is untouched since `fbf3ce7a44`.

---

## Briefs Written

None this window. The window's output was four MCP assessments, not a document.

---

## Blockers

**None on me.** One item remains open and it is not mine: `b04`'s chain sequencing and first S3
code-stage — a first-mint under the S3-membership guard needing an explicit act from
`2.0.0_SA_COO`.

---

## Current State

`D3_MODELOVERLAY.TO-R1-DS` **COMPLETE and ACCEPTED** (COO 70532), routed to `3.0.0_SA_CVO` for
cert. 6/6 criteria PASS, proof-of-spec VALID rc=0, alignment 16/16.

**Commits, all LOCAL on `CLOUD`, riding integration** (verified `git branch -r --contains` = empty,
not assumed):

| hash | contents |
|---|---|
| `fbf3ce7a44` | `data/assets/scripts/gold/runners_49f/b04_account_model_membership.py` (NEW, 362 lines) + proof-of-spec instance + `D3_SMARTX_BD_JOIN_REMEASUREMENT_20260825.md` |
| `a5aa4196c5` | prior session log |
| *this commit* | log relocation + archetype tag + this entry |

**`b04` is committed, NOT deployed and NOT emitted to the gold tree.** Every run was `--dry-run` or
`--local-out` to a scratch root. Its first production artifact must come from the **scheduled**
chain — an ad-hoc run is a QA instrument, never production evidence.

Both sovereign rulings assessed: **neither requires rework.** MCP this window: 4 messages handled
(1 acceptance, 2 Andrew-direct relays, 1 own ACK out), 3 sent.

---

## Next Steps

1. **[`2.0.0_SA_COO`]** Sequence `b04`'s chain registration + first S3 code-stage (first-mint,
   explicit act required).
2. **[`3.0.0_SA_CVO`]** Cert on the instance. COO flagged for your judgment that the checker's own
   `alignment-scope` line closes the TO against itself and the decomp's id space, and that whether
   the declared set IS the decomp's complete criterion-bearing set is a **cert** judgment
   (enforcement layer 5) the tool does not assert — *that gap is exactly where the surface-(c)
   error lived*.
3. **[`1.0.0_SA_CTO`]** The BD `dim 436` / template `390224` vendor item — blocks D3's advisor
   level and ADVI_INSURE's advisor spine leg, two directives on one field.
4. **[unassigned, flagged not chased]** The U1 roster producer lives in **two homes**,
   byte-identical today. `b04` now depends on that table, so the Rule 22a two-homes shape is live
   coupling rather than a curiosity.
