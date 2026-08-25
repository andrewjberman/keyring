# ADVI_PERFRP TO-R1-DS delivered in full: 18 cells, 14 criteria, and six findings that were true-but-wrong-framed — 0.4.0_DS_ClientPlatform~G

**Serial:** 0.4.0_DS_ClientPlatform~G
**Date:** 2026-08-24 ~21:1xZ - 2026-08-25 ~04:2xZ
**TO:** ADVI_PERFRP.TO-R1-DS (issuer 2.0.0_SA_COO; decomp @1ce9b2d6bc, CVO cert @62598c1bfb)
**Archetype:** BUILD + MEASURE

---

## Objective

Deliver the DS half of ADVI_PERFRP round 1: the column audit, the per-client projection
contract, the projection runner cells b-2..b-7, the emitter half of c-1, and the producer
halves of inv-2/3/5/6. One project, one lane, spec frozen mid-round.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-find | `comp-find 'def link_returns'` | PASS | 1 hit / 26,292 files. AC11's one-definition oracle. |
| comp-find | `comp-find 'def rollup'` then `'def rollup('` | WARN | Unanchored returned **8** (rollup_roles / rollup_defects / rollup_exit / rollup_by_tool) — the Rule-21 substring-overcount hazard. Anchored returned 2; I disclosed the second (a class method in the graph module) rather than quoting 1. |
| comp-find | `comp-find -i 'custodian'` | PASS | 10 hits across 87 files, **all prose, zero data fields** — the measured absence AC7's sentinel rests on. |
| comp-find | `comp-find -i 'co-extensive'` | PASS | Found the retracted claim on **four** surfaces when CVO had named one. |
| comp-find | `comp-find -i 'contract_version' data/assets/scripts/gold/runners_49f/` | PASS | 0 -> 9 hits across 87 files; DE~D's own start-condition oracle. |
| comp-pipescript | `comp-pipescript io <module> --pipeline bd` | SKIPPED (no domain) | "Unknown script" for every module I added. **Positive control `io C_02 --pipeline bd` returned a full 5-read / 2-write manifest**, so the tool works and the gap is DOMAIN: its subject is registered stage scripts with S3 I/O; these are library modules with zero I/O. Recorded as a gap, never as a PASS. |
| commit-gate.sh | before every commit | BLOCKED x3, all fixed | Two F401 unused imports, one E702. One F401 was informative: it flagged the in-process `main()` import left over after I moved AC12's rc measurement to a real subprocess. |
| safe-commit msg-verify | `-F <msgfile>` | PASS on every commit from 09ac3a9996 | The built-in Andrew ordered; MATCH with byte length each time. Made the manual checker comparison moot at the tool layer. |
| comp-system | `comp-system` | PASS | Regenerated 06_current_state when the gate blocked the proof instance; staged in the same commit. |
| proof-of-spec-check | positional, 14 criteria | **VALID, rc=0, violations=0** | Runs 1-3 were NOT clean (2 crashes on schema shape, then 6 real violations). Reported in sequence. |

---

## Work Completed

### 1. PRF-a-1 column audit + two addenda I wrote against my own work
`N = 56 = M 46 + K 10`, self-checking (rc=1 if the arithmetic fails). Then **I corrected it
twice**: `MAPPED` collapsed FULL-history and SHALLOW-history sources (8 of 13 serve NO contract
period), and COO's Ruling 2 discriminator resolved each shallow source as RECOVERABLE (5),
STRUCTURALLY-ABSENT (1), UNDETERMINED (1), N/A (1).

### 2. PRF-b-1 the contract, v0.1.0 -> v0.5.0
RATIFIED vs PROPOSED **machine-readable** per DE~D's requirement. Five bumps, each announced
directly to the live consumer rather than only by commit. Carries the absent-column list, the
history floor, recoverability, allocation semantics, period semantics, and the twr shape
declaration.

### 3. PRF-a-2 — proving my own acceptance criterion vacuous, then building the one that works
Six mutants over the gains identity, **all six passed including total garbage**. Built the
component tie-out instead: the core's `fees_tax` covers **9.65%** of the contract's fee buckets,
a $41.4M gap, because management fees carry `sb_cd='FC'` which is not in `SB_FEES_TAX`.

### 4. PRF-a-3 / b-3 / a-5 / a-6 — classification, allocation, book, roster
97.72% of MV classified with the residue named as two states. Additivity exact at every level
(6,141/6,141 accounts within a cent). Book membership **ties exactly** to the live leaderboard
(146/146 advisors, 146/146 counts). Roster emits 866 known-not-held rows in two never-collapsed
populations.

### 5. PRF-b-2 / b-5 / b-7 / inv-5 / c-1 — the production modules
The ONE rollup law and geometric link; the transactions paged key with a strict PII allowlist;
the firm argument contract with a real path pin; the 11 emitter families and the never-blend
guard. Every module imported by its exercise, never re-typed.

### 6. PRF-a-4 / b-4 Gain/Loss, delivered LAST
Census first — which is what caught that `fact_upn` IS `fact_uln` at position grain.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| SI is NOT `max` | They coincide today, which is the argument FOR the rule: an alias passes every test runnable now and breaks silently when STITCH lands. Guarded structurally (`SI_WINDOW_START_ASSERTED`), not by a note. |
| Allowlist, never denylist, for served transactions | A denylist fails OPEN on the next upstream schema change, and the failure mode is publishing a client's bank routing number. |
| bmv/emv sourced from `canonical_valuation`, not twr_daily's own columns | 530/530 partitions vs 523/529 — and twr's native columns vanish on exactly the 6 partitions where a consumer most needs them. |
| Custodian emits `UNAVAILABLE-NO-SOURCE` | No source exists. The TO's own "(Fidelity / position-only)" described the BD dashboard's column. A plausible value being available is what makes it dangerous. |
| Did not invent an insurance discriminator | The surface does not exist yet. A marker for an unpublished schema is a guess encoded as a guard. |

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Projection contract (the b-1 data contract) | `data/assets/scripts/gold/runners_49f/perfrp_contract.py` | DE~D (renderer), AE~G (publisher) |

---

## Files Modified

6 production modules under `data/assets/scripts/gold/runners_49f/` (contract, rollup,
transactions, firm_pin, book, emitters) and 14 exercise/audit artifacts under this lane's
deliverables, plus the proof-of-spec instance. **22 commits, all committed, all LOCAL riding
integration** — verified on 0 remote branches by `git branch -r --contains`, never assumed.

---

## Blockers

None at this seat. Two items are owned elsewhere and named: the twr_daily BMV remedy (DS~H,
now the critical path per Andrew ~04:1xZ) and an insurance discriminator for `dim_account_xref`
(routed to COO).

---

## What I got wrong, and how each was caught

This belongs in the log because the pattern is the finding, not the individual slips.

1. **Read a 5-partition tail as the whole twr_daily series.** 529 partitions exist. The full
   denominator corrected it before anything was quoted.
2. **Summed `flow_ledger.signed_amount` for a fee comparison** — a field the core never reads,
   on a table it does not use. Income came back exactly $0.00 and I nearly reported it.
   Withdrawn entirely and re-derived from `dim_transaction`.
3. **Differenced two populations** (450 vs 530 dates) and charged the gap for dates merely absent.
4. **Scored source coverage by partition COUNT** against a day threshold — the wrong test; a
   source can hold 250 partitions inside one month. It made `dim_account_xref` read as serving
   QTD and YTD.
5. **Annotated `transaction_detail_description` as "the custodian's type text" without reading
   its values.** It is the SECURITY NAME. DE~D built a render proposal on my wrong comment,
   having correctly diffed the committed ref. A wrong reason on a right decision is still a defect.
6. **Claimed 4 new checks in a commit message that contained none** — a scripted edit missed its
   anchor and I read the unchanged 17/17 as confirmation. A count that does not move is exactly
   as green as one that does.
7. **Landed a disarm on one surface while three others still carried the retracted claim**,
   including the machine-readable `BLOCK_STATUS` a consumer reads programmatically — and wrote a
   pointer that pointed at the wrong section *inside* that correction.
8. **Printed "TRUE RC=0" while the checker had crashed**, because I piped it through `tail`.
9. **Reported "24 commits" twice without measuring.** The anchored count was 21.
10. **The `%`-comma format slip four times.** Fixed mechanically with a regex sweep after the
    fourth, which is what I should have done after the second.

**The pattern:** every substantive one was a FRAME error, not an arithmetic error — the number
was right about something, just not the thing asked. And the three biggest were caught only
because they produced an **absurd** figure rather than a plausible one (99.76% residual; ~92%
unclassified; $0.00 income). A two-grain sum landing at 1.02x would have shipped.

---

## Current State

TO-R1-DS COMPLETE. All 18 cells discharged; proof instance VALID rc=0 @672e622680 with
alignment 14/14 forward-1, 18/18 forward-2, 18/18 backward. Three criteria carry a
`status_reason` qualifying what their PASS means, because a bare PASS would mislead a certifier.

Nothing is published. Andrew's ~04:0xZ word made publishing part of "build it out" with the
promote act still held, under his condition that PERFRP keys publish only after the emitters are
wired and the first emission is READ. His ~04:1xZ word set the gate at "actually works on the
backend side" — Rule 22a's BEHAVIOR layer in his own words.

---

## Next Steps

1. **CVO cert** on the proof instance — ready now.
2. **AE~G** wires the publisher; my first emission is their start condition.
3. **DS~H's twr D-1 remedy** is the critical path to a publish; my 66739 finding is what surfaced
   it, and my `link_returns` was hardened for the mixed partitions it will create.
4. **Open at CTO:** the FIGURE_STATE enum (PROPOSED, with its Rule-24 record and token census).
