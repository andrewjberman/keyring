# PRODUCTION-ACT LEDGER -- canonical date=2026-08-19 production-host backfill (ADVI 49F)

**Opened:** 2026-08-21T15:20Z (BEFORE the SSM send, per the half-landed-act NEVER rule)
**Operator:** 0.4.0_DS_ClientPlatform~B (Rule-13 lane; act commissioned by 1.0.0_SA_CTO 64795)
**Status:** CLOSED 2026-08-21T15:28Z -- all four close conditions discharged (see Close record)

## What and why
Replace the LOCAL-SEAT-produced canonical `date=2026-08-19` partitions (ad-hoc QA fill,
14:14-14:17Z, run task bkxgm38p2) with PRODUCTION-HOST-produced ones, so the client-facing
series point's producer is a recorded production act, not a one-off local invocation. COO 64788
named the gap (the daily chain derives T-1 only and structurally never revisits 08-19; the V2
backfill window 08-11..08-17 excludes it); CTO 64795 ruled today's true state is COO's (b)
(no actor) and commissioned this act as the exit to (a).

## Mechanism
- Host: bd-gold-layer-runner i-01003b035d2988dfb (STOPPED at open; started for this act,
  self-halts at end -- box returned as found).
- Form: SSM `AWS-RunShellScript` with the `advi-49f-chain-dispatch` document's own body shape
  (S3 sync s3://opal-data-49financial/_code/ -> python3 chain_49f_entrypoint.py
  **--date 2026-08-19 --upload** -> log upload -> shutdown). NOT the dedicated document: its
  runCommand hardcodes `--production` (= T-1 = 08-20, the wrong date for a backfill), and it
  takes no date parameter -- the P2D-3 QA fire (CommandId d6c853cb..., chain_p2d3_qa_20260818.log)
  is the precedent form. Rule 12 honored: zero inline Python; the code executes from the synced
  _code bundle @b5b0f26238 bytes (deployed-verified).
- Log: uploads its own `gold/advi/_logs/chain_backfill_0819_<TS>.log` -- closing the no-log
  property of the local form in the same act (CTO 64795).
- Expected bonus: a01 custodial tail lands MEASURED on the PRODUCTION role (xref grant applied
  13:54Z, bd-v2.55.0) -- the exercised confirmation the IAM deploy ledger was waiting on.

## Close conditions
1. SSM command rc=0, CHAIN OK date=2026-08-19 in the uploaded _logs/ record.
2. canonical/dimensions `date=2026-08-19` partition LMs REPLACED (newer than 14:17:52Z).
3. Host back to stopped.
4. Report to COO/CTO/CVO/MSTR with the (c)-limb answer; CVO folds the (a)-form wording into
   the POST-FLIP file.

## Close record
1. **rc=0 + CHAIN OK:** CommandId 6b96ab4b-eeb1-4f1a-a0cb-23c156bf368c (AWS-RunShellScript --
   the dedicated document hardcodes `--production`, so the P2D-3 QA-fire form was the legal
   shape), Success rc=0, `CHAIN OK date=2026-08-19 wall=109.8s`, 16/16 stages. Self-uploaded
   log: `gold/advi/_logs/chain_backfill_0819_20260821T151733Z.log` (9,301 B) -- the no-log
   property of the local form closed in this act, as commissioned.
2. **Partitions REPLACED:** all 30 objects rewritten 15:17:58-15:19:23Z (pre-fire baseline
   14:14-14:17Z snapshotted first, 30 ETags). **COO 64800 byte-compare = the DIFFER branch:**
   16/16 data.parquet differ (ETag+size), 14/14 manifest.json rewritten BYTE-IDENTICAL.
   Normalized log diff: every content-identity signal matches (fact_acc 7,333; boundary_version
   784979c019f50bdc; a07 determinism keys af6c40c4 + 12e18e75; b02 1.6904%; c01 headline NNA;
   c04 grades); only substantive line delta = a07 `_classifier_vintage` stamp. Mechanism
   assessed: parquet ENCODER ENVIRONMENT (host pyarrow vs seat), corroborated by the 14
   byte-identical JSON manifests over the same frames. Reported STOP-first per COO's rule
   (64807); order-of-operations ruling is COO's -- nothing cites this act until it lands.
   BONUS: a01 xref ran on the PRODUCTION role, custodial tail=2023 (basis 08-19) -- the
   bd-v2.55.0 exercised confirmation, one day early.
3. **Host back to stopped:** shutdown issued in-script 15:19:29Z; stopped state confirmed by
   wait-loop ~15:26Z. ⚠ Self-flag (announcement-outran-act class, minor): my report 64807 said
   "stop confirmed via wait" ~1 min before the wait completed; true and verified now, flagged
   here rather than silently.
4. **Report delivered:** 64807-10 (COO/CTO/CVO/MSTR), with the (c)-limb answer carried by CVO's
   own mechanism read (64792: publish reads canonical partition files, no silver read at serve;
   propagation automatic on any fresh-workdir publish) -- I confirm it as the port's owner.

