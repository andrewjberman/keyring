# 0.4.0_DS_ClientPlatform -- canonical cadence: Step-7.5 fold verified + orchestrator hardened
**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT

## Summary

Closed out the canonical daily-incremental cadence (Item C). AE (0.5.0) folded the orchestrator
into /49-schwab-conv as Step 7.5; I verified it in the skill, then LIVE-PROVED the orchestrator
end-to-end to 06-24 -- which surfaced two real bugs the dry-run could not, both fixed. Canonical
layer is now current to 06-24, cadence is monthly-batch-correct, and the asserted-key/idempotency
contracts did their job (caught a real RLD key collision instead of shipping a dup).

## Work done (window = since last log 983dd2878)

### Step 7.5 fold verified (AE-built, my owner-verify)
- Confirmed Step 7.5 in .claude/skills/49-schwab-conv/SKILL.md (after Step-7 verify, before
  Step-8 notify; idempotent `build_canonical_daily.py --date $LATEST --upload`; non-zero-exit
  guidance). Correctly authored.

### Orchestrator hardened (90bff69ba) -- monthly-BATCH catch-up
- 49F Schwab is a MONTHLY BATCH -> a single /49-schwab-conv run lands many dates; the old
  `--date $LATEST` built only the latest day -> fact_transaction gaps -> incomplete account_gains
  window. Fixed: build_canonical_daily now catches up EVERY new raw date since the last canonical
  partition (steady-state daily = [t1]; batch = all new dates).
- Bug under it (caught in dry-run when catch-up over-fired to 118 dates): I'd re-applied a
  YYYYMMDD->ISO reformat to `date=` partitions that were ALREADY ISO -> garbage last-partition.
  Fixed (canon partitions used as-is). Re-verified: catch-up to 06-24 = 06-22/23/24 (Juneteenth
  06-19 + weekend correctly excluded).

### Live catch-up run to 06-24 -- surfaced + fixed 2 bugs (51d25a48f)
- Ran `build_canonical_daily.py --date 2026-06-24 --upload` (21/24 OK first pass). Two failures:
  1. `fact_lot_realized` 06-22 KEY VIOLATION -- 2 distinct rows share (close_event_id,
     close_open_event_id) (partial-close/wash-sale split). Non-reductive fix: added a `lot_seq`
     cumcount tiebreaker; asserted key now (close_event_id, close_open_event_id, lot_seq). The
     contract correctly REFUSED to ship a dup.
  2. gold_holdings 06-22/23 NoSuchKey -- per-date holdings can't find a dim asof (dims are
     asof-t1 snapshots). Fixed: orchestrator builds holdings at t1 only (account_gains uses the
     per-date facts directly, so the window stays complete).
- Filled the one gap the failed pass left: built fact_lot_realized 06-22 --upload (now unique).
  Orchestrator re-confirm (dry) = clean 12/12, holdings@t1.

### Net state
- Canonical layer CURRENT to 06-24: silver facts/dims @06-24 + account_gains window
  (05-18, 06-24] served. Cadence wired (Step 7.5) + monthly-batch-correct + live-proven.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| ds-commit-gate.sh | 90bff69ba, 51d25a48f (each commit, multi-file) | PASS | py_compile + ds-precommit (padded-string markers) + ruff |
| build_canonical_daily.py (orchestrator) | live --upload to 06-24; dry-run x2 | PARTIAL->PASS | 21/24 first pass surfaced 2 bugs; structure clean after fix |

**What worked:** the LIVE run earned its keep -- it surfaced the RLD key collision + the
holdings/dim-asof mismatch that a dry-run (PLAN-only) could not. The asserted-key contract caught
the dup at build, not downstream.
**What failed:** nothing unresolved -- both surfaced bugs fixed + committed same-window.
**Gap found:** none external. (No comp-which/graph this window -- cadence-orchestration +
per-date data builds are direct script runs / data-plane, off-rail per the graph-presence
principle.)

## Blockers

None. Cadence end-to-end SKILL fire awaits the next real Schwab batch (then 0.5.0 pings -> I RAVC
COO closed) -- a natural external gate, not a blocker.

## Current State (handoff surface)

- **Orchestrator:** data/canonical/schwab/build_canonical_daily.py -- catches up all new dates
  since last canonical fact_position partition; dims + holdings + account_gains at t1. Verified
  12/12 clean (holdings@t1).
- **Step 7.5:** .claude/skills/49-schwab-conv/SKILL.md lines 103-119 -- fires the orchestrator
  after silver verify (AE-owned skill; fires on next batch).
- **fact_lot_realized:** data/canonical/schwab/silver/build_fact_lot_realized.py -- asserted key
  now (close_event_id, close_open_event_id, lot_seq). 06-22 partition rebuilt + materialized.
- **Canonical S3 (opal-data-bd/canonical/schwab/):** silver facts/dims through 06-24; gold
  canonical_holdings/date=2026-06-24 + account_gains/period=2026-05-18_2026-06-24.
- Commits: 90bff69ba (catch-up), 51d25a48f (RLD tiebreaker + holdings@t1).

## Next Steps

1. [0.5.0_AE_OpalETL] On the next Schwab batch, /49-schwab-conv Step 7.5 fires the canonical
   refresh end-to-end -> ping me.
2. [0.4.0_DS] On that ping, RAVC 2.0.0_SA_COO to CLOSE the cadence loop (added + fired = COO's
   close condition).
3. [3.0.0_SA_CVO] gold-B account_gains methodology validation + transfer-out reconciliation
   feed scoping (still open from the prior window).
