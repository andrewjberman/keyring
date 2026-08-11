# MDPF trigger/schedule remediation — decomposed, sequenced, and twice re-premised — 2.0.0_SA_COO

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, SCRIBE
**Date:** 2026-08-10
**Task Order:** MDPF_REMED W1–W5 (one workstream, per launcher mandate) + ad-hoc decomposition
**Status:** IN PROGRESS — all execution tracks correctly blocked; nothing applied

---

## Objective

Execute CTO's MDPF trigger/schedule diagnosis as **one** workstream, owning decomposition and
sequencing. Andrew's originating frame (via CTO, 2026-08-10): *"The 'Global' view is on August 5th,
Inflection is August 5th, and 49 and Cottonwood are both on August 6th. All of them should be on
August 7th at this point, so we need to trace the routes and identify the basis for the delay."*

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `--name "*MDPF_REMED*"` | 10 hits / 24,955 scanned — located the TO set |
| `comp-find` | `"13:00Z floor"` · `"intakes"` | **1 unrelated / 24,954** and **0 / 3,841** — the measured zeros that proved the diagnosis was not in git |
| `comp-find` | `"rebalancer_accounts"` | 64 / 24,959 (DEF=6) — landed the second producer's definition line |
| `comp-which` | *"what schedules and triggers fire the mdpf pipeline"* | routed to `comp-trigger` (near-tie surfaced, not silently guessed) |
| `comp-trigger` | `cot-bd-session-daily-et` · `ingest-mirror-cot` · `cot-rebalancer-runner-daily` · `--list` | 139 rules + 16 schedules; **`--list` is what surfaced `cron(0 6)` = the unknown producer** |
| `comp-blast` | `cot_bd_session_trigger` | **TIMED OUT at 120s**, backgrounded — did not contribute |

**What worked:** `comp-trigger --list` was decisive — it surfaced `cot-rebalancer-runner-daily` at
06:00Z, independently reaching the producer AE was hunting from the other direction. `comp-find`'s
printed denominators were load-bearing: the measured zeros are *why* I refused to reconstruct an
absent diagnosis rather than assuming I had searched badly.

**What failed:** ⛔ **`comp-trigger` reports `TF-DESIRED: not found in infra/aws/**/*.tf` for
resources that ARE Terraform-managed when the name is INTERPOLATED.** Hit **twice**:
`opal-assets-ingest-mirror-cot-daily-et` (`mirror.tf:138` — `"${local.mirror_name}-cot-daily-et"`)
and `cot-rebalancer-runner-daily`. My own literal `grep` reproduced the same false absence; only
reading the file resolved it. **Why it is more than cosmetic: "live but not in Terraform" reads as
console drift, and the natural response to console drift is a console fix — a NEVER-rule violation
reached by trusting a tool.** Positive control that discriminates: `cot-bd-session-daily-et`
(literal name) *was* found in the same run. Routed to CTO as a register row.

**Gap found:** no comp-tool answers *"which schedules feed this consumer, in fire order, with their
measured landing times"* — the exact question this workstream is. It was assembled by hand from
`comp-trigger` + CloudWatch + `list-objects-v2` across two seats.

---

## Work Completed

### 1. Refused to execute an uncommitted diagnosis
Launcher asserted the CTO diagnosis was DONE. It was not in git. Rather than reconstruct it (which
the same instruction forbade), I printed denominators and asked. CTO confirmed it existed only in
session context, committed it @087938fa61, and recorded the defect in the file's own header:
*"A DIAGNOSIS THAT IS NOT IN GIT IS NOT DONE. IT IS A CLAIM."*

### 2. Decomposition + sequencing @e1c891366a (+ addenda @fbcc6411c7, @3b6c5dcedb)
Four scopes split by **cause**, not by firm: cottonwood + 49financial are schedule-ordering;
inflection is a cross-axis gate refusal and global inherits it. Trading calendar resolved **first**
(08-08 Sat / 08-09 Sun; frontier Fri 08-07) so the lag is stated in trading days, not wall clock.

### 3. The finding that broke the proposed target shape
Source-confirmed `opal-assets-ingest-mirror/lambda_function.py:353` —
`for row in MAP + PROVENANCE_RIDERS:` iterates **all four rows unconditionally**, never consulting
the event payload; both invokers pass `input = "{}"` (`mirror.tf:155`). **The two mirror schedules
are two clocks on one all-rows function**, so the diagnosis's `-cot-daily-et` row is an
**inflection** intake, not a cottonwood one. Its §4 shape could not execute as written.

### 4. W1-5 premise corrected @2406096dde; W1-2 retired @e34422cf34
W1-5's context table was falsified (orion was *never* T+1 03:30Z). W1-2 superseded citing R-31 —
**after** verifying AE's landing commit @586d9f1d8a in git and the tree clean, not on self-report.

### 5. Killed an inferred gate while it was cheap
AE reported idling "pending CTO's GO" that nobody had issued. Surfaced it as a governance shape;
CTO answered **and ruled in the same message** (4 minutes), and issued a standing fabric rule:
**SURFACING IS DISCHARGED BY THE ACT OF SURFACING.**

---

## Decisions Made

| # | decision | ground |
|---|---|---|
| D-1 | **P0-7R OUT of scope** — decommission item, not a schedule item | R-31; NEVER#4 binds a *production* pipeline; scheduling residue = two producers on one floor. CTO confirmed by measurement, not filename |
| D-2 | **W1-2 SUPERSEDED**, code landed first, insight banked separately | CTO ruling + both carve-outs, executed in the required order |
| D-3 | Split by **grounding state**, not firm | a firm split puts the mirror in the cottonwood track, which §0 disproves |
| D-4 | **W1-5 corrected, not executed** | its landing table was measurably wrong |
| D-5 | **Mirror 100%-failure tracked separately** | not the lag cause; must not be credited to the retime |
| D-6 | **Retracted my own escalation to Andrew** | the T-1 fork dissolved at source; a dissolved fork left standing costs a decision he does not owe |

---

## Files Modified

`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_REMED_DECOMPOSITION_AND_SEQUENCE_20260810.md`
(@e1c891366a, @fbcc6411c7, @3b6c5dcedb) ·
`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/MDPF_REMED.W1-5…` (@2406096dde) ·
`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/MDPF_REMED.W1-2…` (@e34422cf34)

---

## Blockers

**None are mine, and none are manufactured.**
- **Track A** — blocked at **CTO (diagnosis)**: cottonwood's lag is unexplained again now that
  `cot-bd-session-daily-et` is known to **produce** rather than wait.
- **Track B** — blocked on **vendor-availability evidence** for SmartX. P0-2R bounds the current
  *pipeline* clock only, and says so itself.
- **Track D** — ownership call at **CTO**, delivered with the caller named.
- **Inflection / global** — CTO's thread; their `(a)`-vs-`(b)` A4-write fork remains open, so the
  morning error list is still not trustworthy as a record and nothing I sequenced rests on it.

---

## Current State

**Nothing applied. No schedule touched. That is the correct outcome of today, not a shortfall.**
Two near-misses were caught before an apply, each of which would have manufactured the defect class
this workstream exists to remove:
1. A cron built on the carried **02:00Z** anchor would have fired **~3.5h before** the data landed
   (measured 06:00:43–45Z) — a pull that runs, exits clean, and gets nothing.
2. Track A's remedy direction rested on a **consumer** premise; the job is a **producer**, so moving
   it changes when we ask a *vendor* for data at an unmeasured hour.

**Established today:** two producers write `blackdiamond/cottonwood/bronze/` in two grammars
(687 json / 368 xlsx / 1,229 denominator) — so the mirror's guard is **correct** and the estate
under it changed.

---

## Next Steps

1. **CTO** — re-derive cottonwood's cause under the producer premise; rule the bronze-prefix
   ownership question; rule whether the cot-side lever survives (it is COT-owned, not INF).
2. **`0.7.0_AE_CloudOps`** — one bounded measurement only: `forwardfill_v2/` **pre-08-06** xlsx
   history, so "the delivery moved on 08-06" becomes measured rather than inferred from a sentinel.
3. **49financial** needs a shape decision (SmartX pull move vs downstream-chain re-architecture) —
   the consumer-side lever provably cannot reach it.
4. **Register rows routed to CTO:** the interpolated-name `comp-trigger` defect (2 instances);
   *"SILVER-FRESH IS NOT GOLD-COMPLETE"*; and **"a denominator printed next to a filtered result is
   more dangerous than no denominator at all."**

---

## Correction I own

I relayed AE's *"nothing fires at 06:00Z across 139 rules"* to CTO **without re-deriving it**, and
built a three-hypothesis frame on it — in the same message warning CTO about instruments that cannot
fail. The claim was a filtered subset wearing the unfiltered denominator. AE self-caught and
quantified it (10 rules fire 05:00–07:00Z); **the relayer obligation was mine and I did not discharge
it.** Nothing was applied, and the outside-AWS caution was the right frame on evidence that did not
deserve it — but CTO should not have received it as grounded.
