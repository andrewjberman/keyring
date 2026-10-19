# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 169 (2026-10-19 11:29Z to 12:2xZ)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Bloomberg: Smart App Control (0.0.0_AB_MSTR~Z msg 35951, acked)

- **Finding:** Smart App Control is set to ENFORCE.
  - It blocks cma's unsigned `ffiutils.cp311` pyd per file instance. The byte-identical PY_AWS copy loads.
  - It flipped between the 10-18 07:03 and 10-19 07:01 local runs. The cause is not determined.
- **RULED: no in-place preload of the PY_AWS blpapi into cma.**
  - That would get around a code-integrity control.
  - It would also break the two-interpreter rule (READ_HERE section 3).
- **Remaining question:** the models (PKL) leg waits on a sanctioned route: a signed or reputable build, or Andrew's word on Smart
  App Control.
  - Asked 0.0.3_BG_BBGTerminal whether that leg's data is backfillable.
  - If it is current-day only, Smart App Control goes on Andrew's act list. Turning it off cannot be undone, which makes it his act.

## Surprise rows

**Filed by 3.0.0_SA_CVO~Z** (msg 35954, acked), @5012389f79:
- Z-S17, ARMED, mine;
- Z-S18, ARMED, 0.0.0_AB_MSTR~Z's;
- Z-S19, INERT, mine.

**My ruling row Z-S20 @b2e304e0f5:**
- **Z-S17:** every DAPI-precondition failure path, including the UNVERIFIED skip, reaches the landing legs.
  - The precondition is measured under cma and the legs run under PY_AWS. A cma DOWN is not evidence the legs would fail.
  - The costs are not symmetric: one non-zero leg line, against a current-day-only capture lost for good.
  - Constraints on the edit: `set PY_AWS` (:139) stays ahead of `:etf_leg` (the Z-S248 class), and the wrapper rc stays 50 so the
    backstop still fires.
  - Z-S17 stays ARMED until 0.0.3_BG_BBGTerminal lands the edit before the 2026-10-20 11:00Z run, with a forced-failure dry-run.
- **Z-S19:** no script change. Both leg scripts default run_class to adhoc. A hand recovery leaves `ETF_RUN_CLASS` unset.
- **dapi_check:** naming an import failure IMPORT-BLOCKED rather than DOWN is ruled the BBG seat's.
- **Z-S18:** relayed to 0.0.0_AB_MSTR~Z for the CVO, which the L8 gate bars from sending it. My rec: once Z-S17 lands, Z-S18 costs
  only the models leg.

**Filed by me: NFRA_OPLGTW Z-S405 (INERT), @fc62ea3ae6.**
- This session's opalgateway MCP connect got HTTP 429 `{"error":"rate_limited","scope":"identity"}`.
- It is evidence for OG-ev-13's 24 h lake re-read: the refusal should appear in the audit lake (OG-en-10).
- disarm_owner is 2.0.0_SA_COO~O.

## Box state

- Commit free 25,528 MB; 8 claude.exe alive.

## Open calls

- 0 forks.
- 6 open `act` rows, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew), 5b35, 2ac2, and a485 (superseded by 2ac2).
- **Owed to me:**
  - the round-46 slug, which carries the Z-S404 design call: should the audit lake store a hashed principal id?
  - OG-cd-3 Phase B, so I can grade CT1-CT4;
  - OG-ev-13, due no earlier than 2026-10-20 07:45Z.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| sed / grep (scheduled_daily_pull.cmd) | the precondition branch and run_class sets | :115 goto :prune; :139 set PY_AWS; :246/:297 scheduled |
| comp-find run_class | the scripts' default label | 6 hits in 7 files; default adhoc |
| surprise-row-gate (safe-commit) | Z-S20 | first REFUSED (surfaced_at not a time); fixed; OK |
