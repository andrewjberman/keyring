# Lane A: flip-evidence TRUTH identified (Andrew-direct "don't keep waiting") -- correctness gate cleared NOW on 26,504/0; freeze = dead-allocations gate, not the flip

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-17 ~21:14Z -> 23:03Z (delta since c05e3f26e)

Andrew: "read the flip evidence for 0.5.0" -> then "identify NOW what the truth is, we should not
have to keep waiting." No commits this window -- pure DIAGNOSE/VALIDATE against live state + coordination.

## 1. The truth, separated into two conflated things

**(a) Does the flip work? YES -- proven NOW, not pending.** The AC1 seam parity IS the substantive
proof: monolith-derived NNA == legacy Layer-B NNA to the cell (26,504 (account,date) cells / 0
mismatch, run this session). C_01 line 878 calls load_schwab_flows_by_date with NO source arg ->
deployed default 'monolith' (md5==ETag verified). C_01 is deterministic on that dict, so flow-source
cannot change canonical_nna output. CTO ACCEPTED this as the correctness gate (223953Z): "the sharpest
available test of C_01 equivalence... does not require tonight's run."

**(b) Why did it keep "waiting"? A DEAD FEED, now fixed -- separate from the flip.** Gold froze at
data_as_of 07-13 since 07-15; last 3 nightlies (07-16 04Z/23Z, 07-17 04Z) ran S_00 then SKIPped
(58-byte logs, "no new silver data"). Root: the dispatch freshness gate keyed on silver/ALLOCATIONS,
frozen 07-10 (BD allocations exporter dead). The A4 re-key -> silver/TRANSACTIONS deployed 07-17
~18:1xZ (verified in the DEPLOYED gold_dispatch.sh:175-186). Predicate now: transactions 07-17 >
gold 07-13 -> tonight's 23:00Z PROCEEDS. Aligns with Andrew-direct "allocations deprecated".

## 2. Grounding performed (live-state, read-only)

- gold data_as_of = 07-13 (header_metrics.json, gen 07-15T23:48Z); canonical_nna frozen 07-13.
- silver/transactions FRESH through 07-17; monolith fact_trn through 07-16.
- EventBridge: bd-gold-nightly-fallback cron(0 23 ? * MON-SAT) ENABLED -> next fire 23:00Z Fri.
- Frozen gap days sitting in monolith fact_trn, readable now: 07-14 +$5.69M / 07-15 +$0.12M /
  07-16 +$0.13M net Schwab NNA (=+$5.93M), ABSENT from served canonical_nna -> tonight publishes them.
- C_01 --dry-run (read-only, NO S3 write) attempted for the full end-to-end -> laptop-side S3
  ReadTimeout on the 256-way account_gains bulk-load (ENVIRONMENTAL, immaterial; seam parity is the
  direct measurement). Did NOT trigger an ad-hoc gold run (NEVER rule; CTO endorsed).

## 3. Coordination settled

- CTO (223953Z): correctness gate CLEARED NOW; freeze diagnosis sound + correctly separated;
  converter retirement UNBLOCKED (0.5.0/pod-AE sequenced); recommends executing right AFTER tonight's
  end-to-end nightly confirm (component proven; nightly = distinct end-to-end test); NEVER-rule endorsed.
- 0.5.0 (224628Z): accepts 26,504/0; fires the /49-schwab-conv step-5 removal on MY 23:00Z-confirm
  ping; PRESERVE locked (producer only; frozen trn_nna partitions = SCHWAB_FLOW_SOURCE=legacy fallback).
- Monitor bdufs57h2 ARMED on tonight's 23:00Z: fires on canonical_nna advance past 07-13 (C_01 ran) +
  dispatch log PROCEED/SKIP/FATAL. On PROCEED + gap days publishing = end-to-end green -> ping 0.5.0+CTO.

## Compiler Tools

| tool | run | result |
|---|---|---|
| aws s3 ls/cp (read-only) | canonical_nna + silver/transactions freshness, gold/logs SKIP logs, deployed gold_dispatch.sh, header_metrics | PASS -- freeze fully grounded on live artifacts |
| aws events list-rules | bd-gold schedule | PASS -- next fire 23:00Z Mon-Sat confirmed |
| python (lib.schwab_flows) | monolith flow load for the 07-14..07-16 gap days | PASS -- +$5.93M net readable now |

**What worked:** live S3/EventBridge grounding cleanly separated the freeze (dead-allocations gate)
from flip correctness. **What failed:** the full-C_01 dry-run (laptop S3 ReadTimeout) -- environmental,
not a finding; the seam parity is the direct proof so the dry-run was redundant. **Gap:** the
account_gains 256-way bulk-load + full silver/transactions scan are not laptop-friendly; a lean
single-date C_01 exerciser would need date-bounding load_flows_from_transactions (currently full-scan).

## Blockers

None. Correctness gate CLEARED + accepted. The only open item is tonight's OPERATIONAL publish
(scheduled 23:00Z, hours out) -- a watch, not a blocker; CTO judged forcing a sooner run not worth it.

## Current State (handoff surface)

- WP8 trn_nna: D1 landed+deployed+accepted (37bd2fee1, fact_trn), D2 filed, correctness gate cleared
  on 26,504/0 (CTO+0.5.0 accepted). Runtime reads monolith fact_trn; gold chain unfreezes tonight.
- OPEN watch: Monitor bdufs57h2 on tonight's 23:00Z bd-gold-nightly-fallback. On PROCEED +
  canonical_nna past 07-13 + [monolith] loader line + 07-14..07-16 gap days -> ping 0.5.0 (their
  step-5-removal trigger) + CTO = end-to-end green. On SKIP/FATAL -> ping immediately with the log.
- Converter step-5 retirement: 0.5.0/pod-AE owns it, fires on my ping; PRESERVE artifacts (legacy fallback).

## Next Steps

- **[me / DS~A]** On Monitor bdufs57h2 fire: verify the 23:00Z end-to-end result, ping 0.5.0 + CTO
  (green or SKIP/FATAL). Event-driven; no crons.
- **[0.5.0_AE_OpalETL]** Execute /49-schwab-conv step-5 removal on my end-to-end-green ping.
- **[1.0.0_SA_CTO]** Owns final acceptance; notified 0.5.0 correctness gate cleared.
