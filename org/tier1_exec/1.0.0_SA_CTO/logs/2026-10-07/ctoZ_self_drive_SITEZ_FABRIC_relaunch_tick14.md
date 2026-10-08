# /self-drive SITEZ fabric (relaunch) -- tick 14, 2026-10-07 ~20:50Z -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 13's log (author time 2026-10-07T15:56:44-04:00 by `git log`) to ~21:0xZ. Cadence 60m, cron `12f228ad`.
**state: ARMED**

## Measurements

- Sequence (`.tools/sequence-check.py --project`, 5 of 5 read): AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP NEEDS-SLOT=1 each;
  DSGN_AMGTV1 and ETFS_RIVALS none. No DRIFT, no WAITING. Unchanged.
- Inbox: 0 files unread in the folder; 1 broker message at this tick's read, acked (31385).
- Origin CLOUD `f797fc2df1` (ls-remote). Not run this tick: `directives-check`, `active-commitments`.

## Andrew-direct this hour

- ~20:4xZ at the `4.0.0_SA_CRO~Z` terminal: rivalfunds needs 365 days of history per security and per tracked fund, kept by the
  ingestion sequence; the analysis comes to this seat to place in ETFS_RIVALS with `2.0.0_SA_COO~RV`. Record in
  `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/` (named in PRD ADDENDUM G).
- CLAUDE.md rule 32 (SEAT ROLES) read on origin CLOUD at `6257c5e1b6` (relay 31354).

## Calls ruled since tick 13

| call | ruling | carrier |
|---|---|---|
| ETFS_RIVALS, the 365-day history (CRO~Z 31385) | PRD v0.19, ADDENDUM G, new outcome FWD-24 with four contracts; the reader census comes before any year of closes is written | `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`, this commit |
| AMGT_CORPUS, the 25 gained passages graded 23 of 25 (`3.0.0_SA_CVO~Z` 31350) | a repair cell; then on 31380 the rule this seat named is WITHDRAWN and AMENDMENT 5's narrow rule taken; six mid-sentence values served as they are, named | msgs 31351 to 31353, 31382 to 31384 |
| AMGT_HARVST gold rebuild #8 (`2.0.0_SA_COO~H` 31373) | CTO half SIGNED, three conditions; runs BEFORE bb-18's apply (31379) | `deliverables/CTO_HALF_AMGT_HARVST_GOLD_REBUILD8_20261007.md` @201121c305 |

Governance forks at the CVO: 0. Design forks at the CRO: 0.

## Corrections to this seat's own acts

- Msg 31352 named a rule ("end at the last sentence end") that drops about 14 whole bullet points on the 950 fields and leaves
  Nike unfixed. Found by `2.0.0_SA_COO~X` reading every dropped tail before the write. Withdrawn (31382).

## Acts landed and notices (others')

- R36's acceptance read: the first rivalfunds record on the audit lake keeps `day` and `route` with `bytes`, 18:55:34Z (31372).
- Cross-box notice: no untargeted apply of `infra/aws/terraform/opal-assets` until 2026-10-08 06:20Z (31364). No act in this
  scope applies that root.
- NFRA_OPLGTW r28: 3 tests red on the release tree; re-cut before any half is asked (31372).

## Scope state (register read, 5 of 5)

All five `status: active`, `dep_stage: EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.

## Acts only Andrew can do (cited)

- His word on whether "no fetch on any box" covers an AWS host at deploy (the word is his; asked ~17:4xZ).
- His word that the smoke on port 5174 is finished (asked ~16:4xZ).
- DSGN_AMGTV1 FWD-1's signed-in walk and the PROD promote of `4b167888` (CLAUDE.md Portal: PROD gated).
- Stated to him, not waited on: ADDENDUM G reads his ~20:4xZ words as a standing Bloomberg request of closes for rivalfunds
  securities (CLAUDE.md, vendor use by his word); one word from him reverses it.

## Compiler Tools

- `sequence-check.py` x5; `prd-signoff.py status ETFS_RIVALS`; native Read and Grep; `s3api list-objects-v2` (inspection).
