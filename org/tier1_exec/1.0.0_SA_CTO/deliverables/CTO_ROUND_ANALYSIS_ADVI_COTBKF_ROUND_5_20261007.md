# ADVI_COTBKF -- ROUND ANALYSIS, round 5

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~09:1xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. This answers `3.0.0_SA_CVO`'s slug (msg 241):
REMEDIATION_v3 @521f5aaab8. 5 rows: 2 dismissed, 3 OPEN. ARMED after: S9 and S12 (both BLOCKING), and W12-S1.
Round 5's issued orders: CB-e-1 (calendar refusal), CB-e-3 (documents hold the restricted prefix back) and CB-e-4 (the C-RESTRICTED
write-in), all `complete` (this seat's read of `<status>`). E2's apply and E5 were not issued: their gates are below.

## 1. Outcome state -- 2 of 9 REALIZED (unchanged)

FWD-1 and FWD-9 hold from round 4's analysis (@e363a194ed). No outcome turned this round. Round 5 made the scripts safe to run
(a fallback calendar now refuses instead of computing wrong) and staged the writes. Every write that remains is behind an act
dell2 cannot perform.

## 2. Rulings on the open rows

| row | ruling | un-parks when |
|---|---|---|
| S9 (BLOCKING) | Stands. No links `--apply` from a box whose calendar does not cover 2013 onward | the laptop's fix B lands on dell2: the bring-up kit carries `pandas_market_calendars` (NFRA_CTLPLN v0.14 C-KIT-PYTHON). Then E2 runs, and S9 disarms when the applied run reproduces the laptop deliverable row for row |
| S12 (BLOCKING) | **RULED (b) for both E5 and E3** (msg to `~C2` 09:06Z). No laptop apply: one project, one box (C-PLACEMENT), and Andrew took this project off the laptop's COO lane. The exact silver prefixes are asked for in NFRA_CTLPLN round 4's fence census (relay 09:06Z) | NFRA_CTLPLN round 4 admits the dell2 user to write those prefixes. Do not probe PutObject before then |
| W19-S1 | The laptop's (`org/devices/role_request.py` admits no user principal). Routed with the E4 write-in (relay 09:06Z) | the laptop changes the writer, or creates the role by hand from the write-in |

## 3. The ENRICHMENT LIST -- round 6

**No issuance this round.** Every cuttable item is behind one of the three un-park conditions above, and no other outcome has a
cell that avoids both the fenced bucket and pre-2024 dates. `~C2` holds the scripts at 9fea452b9d and the drafted never-widen pairs.
On each un-park, `~C2` issues the matching item the same tick, without a new analysis:

| on | issue | criteria (carried from round 4's E2, E3, E5) |
|---|---|---|
| fix B on dell2 | E2: the links and the census on the covering calendar, then the links applied | round 4 analysis E2 (1)-(3) |
| round 4 write grant | E5: the crosswalk applied | round 4 analysis E5 (1)-(2) |
| round 4 write grant | E3: the unique documents and the documents table applied, the restricted prefix held back | round 4 analysis E3 (1)-(3) |

## 4. Reachability

All 7 open outcomes are REACHABLE, but not by dell2's own work: each waits on a laptop act (fix B, the round 4 grant, the role).
None waits on Andrew. While these acts are pending, the ADVI_COTBKF lane is idle, and that is the honest state.

-- 1.0.0_SA_CTO~DELL2
