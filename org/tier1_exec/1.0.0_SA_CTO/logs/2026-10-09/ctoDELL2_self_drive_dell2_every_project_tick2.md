# /self-drive EVERY dell2 project (11, 30m) -- tick 2 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_034xZ_SELF_DRIVE_30M_EVERY_DELL2_PROJECT_AND_DISCRETION_ON_THREE_ACTS.md` @35fabf20c8
**Tick:** 2 (04:48Z), plus the event-driven work since tick 1 @08ececfa5e. **state: ARMED** | cron c17cb1c7

## Andrew's words since tick 1 (each through the CRO, recorded by it)

- **~04:4xZ:** "Go with your recs on both consolidation calls". This confirms CTO ruling @ca5f74553d (record @c41f11fb70).
- **~04:4xZ-05:1xZ:** the security swap method; "I do not think we actually need YCHARTS for anything"; prices yfinance-first, Bloomberg only if
  necessary; the DASHBD engine ported for overlays (record @9ae5d353d1).
- **~04:4xZ (laptop law edit d92d08c448):** pushes need no word, except a PROD push of a client-facing page.

## Acts

| Act | Record |
|---|---|
| IRPT_ANLREQ PRD v0.1, then v0.2 (CRO R1-R3: C-ABSORB, security swap, 14-row coverage). **ADMITTED** (CVO and CRO). Then v0.3 (C-SWAP, C-PRICES, FWD-7 no YCharts); both halves re-asked | @5dd6c2422b, @97ef783e9a, @1251f44685 |
| IRPT consolidation: the ruling, confirmed by Andrew. IRPT_CUSTDY closed as superseded_by IRPT_DASHBD after the ~K2 handover. LIVE_ARMS updated | @ca5f74553d, @ddc720db66, @d016a98794 |
| IRPT_DASHBD v0.9: CUSTDY FWD-1..9 absorbed as FWD-12..20. **ADMITTED** (CVO msg 2484). Quote-placement fix | @d1813f3204, @e8f96f579c |
| CTO halves: SA-k-1 firm clamp (its condition was met: no ticket leaves Alyssa's view); svc-custody-statement mint (the reader ARN is a laptop act) | @fbe4b3585d, @53fa699974 |
| Rulings: IRPT_DASHBD R35 ROLLBACK; YCDGEN round 6, CVO grades the two FAILs (graded MET, msg 2495); NFRA_TRNSPT round 18's commentary cell issues under IRPT_ANLREQ; COTBKF round 27 cap back to 0.5; ~P2 builds H1 as DESIRED Terraform for IRPT_ANLREQ, plus release packets | messages, and @be3a9999fc |
| Cross-box items routed via MSTR: data_refresh admission fix (site Z owns it); round-close-check fallback (MERGED @ee22806754 on the laptop); SECCLASS designated-proxy table (dell1) | messages |

## Scope (denominator 11)

- IRPT_CUSTDY is `closed`, superseded_by IRPT_DASHBD. It stays in the denominator, and is not removed.
- ADVI_BILLING (`~B2`) and NFRA_OPSWKF (`~O2`) were seated by MSTR (msg 2409), so they are REACHABLE now.
- IRPT_ANLREQ is at PRD (v0.3 re-sign owed).
- The other 7 are EXECUTING, ROUND_CLOSE or PRD as read.

## Completion test

NOT DONE: 0 of 11 complete. IRPT_CUSTDY is `closed`, superseded, which is not `complete`. **11 REACHABLE, 0 UNREACHABLE.**

## Acts only Andrew can do

- A PROD push of a client-facing page (law edit d92d08c448). The open case is the Performance client statement print page (CU-g-6, row 0347).
- FWD-8's accepted tolerance for the Black Diamond tie-out. It is not cited as an act, so this is a call carried to the merged project's analysis.

## Compiler Tools

`prd-signoff.py status`; `missions-tree-index.py`; release-census.py; `git patch-id`; opal-users-v2 and opal-tickets scans (counts only);
safe-commit.sh.
