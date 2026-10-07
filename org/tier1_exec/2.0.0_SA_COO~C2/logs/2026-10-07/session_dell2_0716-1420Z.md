# ADVI_COTBKF carried from the laptop to dell2 and driven from round 4 to round 11 -- 2.0.0_SA_COO~C2

**Date:** 2026-10-07
**Task Order:** ADVI_COTBKF rounds 4-11 (issuer); /canonical-drive ADVI_COTBKF
**Status:** IN PROGRESS (project parked on two external gates; 5 of 9 FWD REALIZED)

---

## Objective

Seated by `0.0.0_AB_MSTR~DELL2` as successor of `2.0.0_SA_COO~C` (moved to NFRA_CTLPLN only, Andrew-direct ~06:1xZ) to carry ADVI_COTBKF
on dell2 (placement ruling ~06:2xZ), picking it up mid-round with /canonical-flow and driving it under /canonical-drive (Andrew-direct
~07:16Z, "they should have /canonical-drive on their respective projects"; LIVE_ARMS DELL2 block @3e5ce43ebb, class CHOSEN).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "open a change-management deploy ledger entry with legs"` | FAIL | no curated rule; found `.tools/deploy_ledger.py` by a native Grep for its log string |
| comp-estate | `--resource 'commonwealth/cottonwood/silver/{crosswalk,documents,account_links}'` | PASS | SUBJECT_ABSENT_FROM_CORPUS over 135 chains: the reader census for three never-widen halves |
| comp-find | `comp-find 'marketdata' ... --files` piped to tail | SKIPPED | the rail refused a piped census; used native Grep on the registry instead |
| proof-of-spec-check | every drained instance, in the worker worktree, with the criterion list | PASS | 12 orders, all VALID before merge |
| safe-merge | every drain | PASS | caught 6 append-only channel conflicts (resolved base + both appends); refused cleanly while peers' merges were open |
| surprise-row-gate | via safe-commit | PASS | refused a row whose fabric did not match its D2 coordinate; caught at commit, fixed |

**What worked:** safe-merge's `--continue` limb for append conflicts; the row gate's coordinate check; the proof checker in the worker worktree.
**What failed:** `comp-which` had no route for the deploy ledger; the Bash rail blocked text that merely quoted `aws s3 ls`.
**Gap found:** none new beyond the two above.

---

## Work Completed

### 1. Pickup and round 4 (laptop worker branches drained on dell2)
/canonical-flow: L7, round 4 (issuance b699efa196) with worker branches 12-16 laptop-only. Asked MSTR to push them; drained ~13 c8fe590f77,
~14 aa23c85ee3, ~15 85d8b5f20f (TF, not applied), ~16 2040c2db3f; re-dispatched CB-d-1 (no laptop work) to a fresh ~12, drained 642222e85f.
Packet 29479eeb61.

### 2. The calendar hazard (S9 / W12-S1)
Measured the cause independently (S10 3dd25927f2: the 2024-2027 fallback; 1,450 of 1,450 rows equal under pre-2024 holidays). Round 5
(407326a599): CB-e-1 calendar refusal, CB-e-3 restricted hold-back, CB-e-4 write-in. After the laptop fix (0a73ed06a0): E2 links applied
(1,450 rows = laptop deliverable, every column), disarming S9 (D2-S16) and W12-S1 (S17).

### 3. Applies from dell2, each under a never-widen pair and a closed ledger
E5 crosswalk 98652475d8; E3 documents (11,119, first mint) and E2 links 3c39c9f4ae. S12's fence premise was wrong (S13: the applies write
opal-data-assets); corrected before any apply.

### 4. Rounds 6-11
CB-f-1 restricted path in any bucket; CB-g-1/2/3 price-store scanner, FWD-8 read, FWD-6 page; CB-h-1 repeat count + per-kind page; CB-i-1
RETURNS line; CB-j-1 marketdata (BARRED, 49financial alias); CB-k-1 price-need FILE for MDPF_SECHIST (4,545 securities / 8,091,310 days,
amended from the issuer's 2,914 error, D2-S21).

### 5. FWD-1 thread re-trace (D2-S22)
Both 2026-10-06 traces reproduce on today's applied data; 5 extra rows on D49141617 are C-SILVER-restored repeats.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Drain the laptop's round-4 branches rather than re-dispatch | a project moves between rounds, never mid-round; their work was finished |
| Struck E3-r7 (re-apply to 1,415,137) by REC to the CTO | PRD v0.4 C-SILVER keeps every delivered record; the CTO agreed (msg 393) |
| Refused msg 456's 49F/INF census half | CTO ruling 1 and the CLAUDE.md cross-firm NEVER; the CTO struck it (msg 485) |
| Amended CB-k-1 to 4,545 securities | 2,914 and 8,091,310 are two sets; MDPF_SECHIST needs every uncovered day |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round{5..11}.md` | round decompositions | Yes |
| `org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-{e,f,g,h,i,j,k}-*.md` | 12 orders | Yes |
| `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/*` | packets r4-r11, never-widen halves, checks, probes | Yes |
| `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md` | rows S7-S20, D2-S21, D2-S22 | Yes, except D2-S22 (held for MSTR's merge window) |

---

## Blockers

- FWD-3: MDPF_SECHIST's price loads on dell1 (Yahoo has Andrew's word, 13:2xZ; Bloomberg awaits his word on card A).
- FWD-2 CRM half, FWD-4, FWD-7: the laptop C-RESTRICTED apply (statements-only halves, COO AMENDMENT 2 e297665fdb), then the CRM landing.

---

## Current State

ADVI_COTBKF on dell2: rounds 4-11 drained, every proof VALID, 0 ARMED rows of this seat, 5 of 9 FWD REALIZED (FWD-1, 5, 6, 8, 9). The
project is parked on two external gates (above), each with a pre-named cut; the price-need FILE for MDPF_SECHIST is
`deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv` @50a35d3ada. /canonical-drive runs every 30 minutes (cron 17,47).

---

## Next Steps

1. **Close row W6-S5** (superseded by CB-d-1's registry reads) -- record hygiene.
2. **Pre-draft the FWD-3 daily-returns cut** -- issue the tick MDPF_SECHIST announces a price load.
3. **[Andrew] Bloomberg pull, card A** -- 1,319 securities, 2,317,534 security-days, about 20 days paced.
