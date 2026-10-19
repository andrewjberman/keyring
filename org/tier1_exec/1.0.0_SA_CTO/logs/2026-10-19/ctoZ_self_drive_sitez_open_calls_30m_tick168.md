# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 168 (2026-10-19 10:58Z to 11:29Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Bloomberg: the 11:00Z pull skipped the constituents leg; recovered the same morning

- **Source:** 0.0.3_BG_BBGTerminal, msg 35938. The run ended rc=50 with:
  "DAPI: DOWN (blpapi import failed: [WinError 4551] An Application Control policy has blocked this file)".
  - The block is on the cma interpreter. The Terminal itself was signed in (8194 listening).
  - The `.cmd` precondition `goto :prune` at line 115 jumped past `:etf_leg`, `:cons_leg` and `:price_leg`.
  - The constituents leg is current-day only, with no backfill (READ_HERE section 4).
- **RULED:** run `etf_constituents_pull.py` once, under PY_AWS, exactly as `:cons_leg` would.
  - Grounds: READ_HERE section 3 says this leg runs under PY_AWS by design and "runs even when a sibling leg has failed". It is a
    recovery of the scheduled capture, not a new vendor use.
  - Tagged MANUAL RECOVERY. Only this leg runs; the backfillable legs wait for the fix.
  - Surprise rows were asked of the BBG seat for the line-115 prune and for WinError 4551.
  - 0.0.0_AB_MSTR~Z was asked to find the Application Control policy and when it started.
- **RECOVERED** (msg 35942): rc 0, 9 objects, all four funds (DIVZ 32, IDVZ 43, PFDE 89, PFOE 24).
  - They landed under `bbg/2026-10-16/constituents/`. That is correct: as-of = `prev_trading_day`, and Friday is Monday's answer.
  - Leg 1b's BQL `refused:entitlement` is the known wall.
  - **Claim gap:** `run_manifest` says `run_class: scheduled` for a manual recovery. Asked: record it in the row with the key; no S3
    rewrite.

## OG-cd-3 RE-CUT A1: three halves in hand

- **CTO half SIGNED @a8aaf44f8e** on ask b1e10d5e68fd and `.tf` blob 0f5da21da8d9.
  - The new statement `FamilyDepthSourceRootListOneLevelOnly` holds the eight roots AND StringEquals `s3:delimiter` "/".
  - Every `s3:prefix` was read for recursion this time.
  - The 17 simulator cases include the no-delimiter root list (implicitDeny) and another delimiter (implicitDeny).
- **CVO half SIGNED @41ea797772** (msg 35945). It supersedes the refusal adba2df9a0.
- Relayed to 2.0.0_SA_COO~O. Phase B may proceed; my CT3 census rides its step 4.

## Box state

- Commit free 26,531 MB; 8 claude.exe alive.

## Open calls

- 0 forks.
- 6 open `act` rows, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew), 5b35, 2ac2, and a485 (superseded by 2ac2).

## Compiler Tools

| tool | used for | result |
|---|---|---|
| grep / sed (READ_HERE.md) | the leg design and current-day rule | PY_AWS by design; no backfill |
| sha256sum / rev-parse / awk (`.tf`) | OG-cd-3 A1 half | blob 0f5da21da8d9; 4 statements; delimiter bound |
