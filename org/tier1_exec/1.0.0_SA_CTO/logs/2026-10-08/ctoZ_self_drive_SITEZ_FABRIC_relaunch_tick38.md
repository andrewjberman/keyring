# /self-drive SITEZ fabric (relaunch) -- tick 38, 2026-10-08 ~21:3xZ to ~21:5xZ -- `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 37's log @713ae4ebba to this tick. Cron `812ad509`, hourly at :17 local.
**state: ARMED**

## Measurements

- Sequence (5 of 5 read): all PLACED, no DRIFT. **NEEDS-SLOT on AMGT_CORPUS, AMGT_HARVST and AMGT_RESAPP was a carrier gap, not
  startup:** their tree rows never carried `coo_lane`, though `seats.coo` names `2.0.0_SA_COO~X`, `~H` and `~Z`. This seat writes the
  tree-row carriers (Rule 27 L3) and added the field; the re-read shows all three at `flags=-`.
- Register: 5 of 5 `active`, `EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.
- Inbox: 6 delivered since tick 37 (32017, 32025, 32026, 32031, 32033, plus 32005 before it), all READ-acked.

## Calls ruled and acts taken

| call | ruling | carrier |
|---|---|---|
| ETFS_RIVALS round-28 slug (`3.0.0_SA_CVO~RV` 32017) | ADDENDUM 7: R31 ask the aw-1 deploy pair now, J1 reads the 10-09 13:00Z sweep, no ad-hoc served run; R32 remediation `round` = task-order round from the next slug; round 29 cuts nothing | `ledger/ROUND_ANALYSIS.round22.md` @0820f6b0b7; msgs 32023, 32024 |
| AMGT_HARVST round 74 (`2.0.0_SA_COO~H` 32025): a clause added to R30 inside the decomposition, so an exact match on the stored alias also counts | accepted, no reply owed: it keeps "eBay" on a lower-case stored alias, which R30 alone would have dropped | -- |
| Three tree rows missing `coo_lane` | written: CORPUS `~X`, HARVST `~H`, RESAPP `~Z` | this commit |
| DSGN_AMGTV1 rounds 51-52 analysis (owed since tick 35) | written: SAUX-37 to 40 MET; F1 to F5 ruled; round 53 waits on AMGT_RESAPP round 79 serving | `ledger/ROUND_ANALYSIS.round51.md`, this commit |
| NFRA_TRNSPT fabric field (`0.0.0_AB_MSTR~Z` 32031) | not this fabric's: routed MSTR to MSTR to `1.0.0_SA_CTO` and `1.0.0_SA_CTO~DELL2`, with the REC set fabric dell2 | msg 21:48:48Z |
| Port 5174: `2.0.0_SA_COO~X` returned it (32026); this seat restored Andrew's smoke server (portal DEV `a3ab197f`, HTTP 200); `2.0.0_SA_COO~Z` then asked for it for AMGT_RESAPP cc-8 (32033) | stopped the smoke server; 0 listeners read; given to cc-8. The smoke server goes back only when no project walk is waiting | msg 21:50:33Z |

Design forks at the CRO: 0. Governance forks at the CVO: 0.

## Owed by this seat (carried)

The ETFS_RIVALS PRD's C-OWED-GRAIN amendment (R13), and G.2's citation of his card 5. The CTO half of the aw-1 deploy pair, when the
COO half arrives. The AMGT_HARVST R30 grade read.

## Acts only Andrew can do (cited)

- DSGN_AMGTV1 FWD-1: his own signed-in walk on PROD (his login).
- A Barron's sign-in (his, "any time").

## Compiler Tools

- `sequence-check.py --project` x5, run as one call per project inside one Bash call (~3 min). It found the carrier gap; the re-read
  after the write confirms it closed.
- `git cat-file -t` on the six hashes cited in the DSGN analysis: 6 of 6 resolve.
