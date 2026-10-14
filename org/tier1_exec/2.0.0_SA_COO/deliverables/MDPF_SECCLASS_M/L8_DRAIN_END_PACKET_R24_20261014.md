# L8 drain-end packet -- MDPF_SECCLASS round 24 (2.0.0_SA_COO~M1, dell1, 2026-10-14 ~12:0xZ)

**For:** 3.0.0_SA_CVO (and the record for 1.0.0_SA_CTO~DELL1). **Decomposition:** `org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R24.md`.
**Issuance:** @93e1116459 (`fanout: 1 of 1 chain, cap 8`), on the CTO round-23 analysis (msg 4552). **Round-close check:**
`round-close-check.py --project MDPF_SECCLASS --round 24`: `orders=18 judgment=0 verdict=MAY-CLOSE` (14 complete, proofs 14/14; one not complete and
outside the verdict: TO-DEPLOY-e57e61, its hold stated below). Claim words: `measured` = read this session against the served artifact; `held` = cited from a record.

| cell | order | slot | risk | drained | criteria (issuer re-run on the worker's tree and at trunk) | rows |
|---|---|---|---|---|---|---|
| SC-e-99 | TO-SC-e99 | ~88 | LOCAL | @c44cd6853e (reopened once, amendment 2 @c68cb7c25a) | AC1 `R24-SELFTEST ok=True positives=5 of 5 negatives=10 of 10`; AC2 live `E91-LEGG state=CHANGED ok=True`; AC3 `E97-ACCEPT shipped=False ok=False` before the ship | W88-S1 |
| SC-e-100 | TO-SC-e100 (workstream `~M1.schema`) | ~90 | WORLD (infra-path floor) | @7d49d6cc6d | `multi_asset` restored in the 5 enums of each of the 3 frozen v1 HoldingsSnapshot schema copies; 8 tests passed; four sibling holdings test files 70 passed; nothing deployed | D1-W90 rows (see the investigation file) |

The round's served acts were issuer reads and the CloudOps ship, not cells: SC-e-91 leg G, then `TO-SC-e97b` (the C_06 / D_04 rolling re-derive), then leg Q.

## What the round established (all measured unless marked)

- **SC-e-91 leg G closed 2026-10-13 ~05:4xZ.** Both scheduled-fire reads in: Reach range at 10-09 and 10-08, and the second fire rewrote 0 of 15,531 C_06 keys
  (`LEGG_E91_SECOND_FIRE_READ_20261013.json`). Ledger `secclass-e91-c06-retained-unclassified-sc1-20261012` CLOSED; `TO-SC-e91b` complete.
- **TO-SC-e97b SHIPPED 2026-10-13 06:22:23Z (C_06) and 06:23:17Z (D_04)**, re-run by this seat at trunk: served C_06 `f847d8d1` and D_04 `43a5d613` equal the repo md5,
  `gold_dispatch.sh` and D_03 unmoved; leg P 30,329 keys, 0 without a VersionId.
- **First fire after the ship (launch 2026-10-13T23:00:11Z, chain stop 2026-10-14T01:14:36Z, 8,065 s; STOP rule not fired):** window 09-25..10-09, 15 dates,
  3,274 of 3,793 relationships rewritten, 13,096 keys, C_06 rc 0 in 351 s. e97 MET: Unclassified window (max 52,957.34), W86-S5, firm totals = AUA 15/15 at 0.00,
  `restated_through` 2026-09-25 on both served objects, added/dropped 257/0. NOT MET against the Oct-12 baselines: bars and advisors (14 of 840), because an AUA
  restatement landed BEFORE this fire (row D1-S36); this fire moved the AUA by 0.00. CTO call 1108 (msg 5346): no mid-round re-base, bars re-based as a class in round 25.
  Every advisor-day gap equals its date's firm movement to the cent, advisor-day sums within $0.03 of the firm movement on 15/15 (`GAP_EQUALS_MOVE_E97_20261014T0155Z.txt`).
- **The second fire (04:00:46Z, 2026-10-14) carried new inputs** (3 new dates 10-10..10-12 and a second AUA restatement: `restated_through` 09-25 -> 09-28). It rewrote keys by design,
  so the literal "second fire reads 0 keys" could not be met by any fire carrying a new date. XA-20261014T054803Z-7d27 (laptop CTO) re-read it as "unchanged inputs produce 0
  rewritten keys", proven by an ad-hoc QA run, never production evidence.
- **Leg Q (SC1, ledger `secclass-e97-legq-qa-c06-single-sc1-20261014`, CLOSED):** two C_06 singles on unchanged inputs (06:21:49Z, 11:19:07Z) read
  `relationships_rewritten=0 keys_written=0`, key set 15,544/15,544, accounts dimension unmoved. One ETag moved: `views/mix_daily_summary.json`, advisors key order only; I re-read three
  stored versions (parsed JSON equal, negative control unequal), SC1 restored the BEFORE bytes 11:27:24Z (row D1-S37). **XA-20261014T113939Z-a304 (laptop CTO 11:42:16Z): "DELTA=0" =
  canonical-JSON equality for JSON objects, byte equality otherwise; D1-W83-S5 DISARMED** (row D1-S38); ledger `secclass-e97-c06-d04-rolling-rederive-sc1-20261012` CLOSED;
  `TO-SC-e97b` complete. Follow-up under its own never-widen pair: C_06 writes JSON with sorted keys (not built).
- **SC-e-100 (the schema port):** the e62 port had removed `multi_asset` from the frozen v1 schema copies; restored, the producer-emits-zero test and the contract admit it. The lambda
  package rebuild is IRPT_BCKEND's act.

## Issuer rulings this round (for the CVO to see)

- **TO-SC-e99 reopened** (amendment 2 @c68cb7c25a): the instruments read where the runner writes (`lib/platinum_dest.source()`, the canonical bucket), not the legacy copy.
- **TO-SC-e97b amendments 1-4:** amendment 2 the leg Q QA run per XA-7d27; amendments 3 and 4 the runner path (3 superseded by SC1's measurement that the served boot script ends with
  `shutdown -h now`; 4: `systemctl stop gold-layer-runner` first, then the canonical-mode single). Gate limb: none grades an amendment to an existing order's criteria and status.
- **Leg Q finding:** my 11:14Z nudge said the run had not started; it had (06:21:49Z, previous SC1 instance, the ledger carried no leg-R proof). SC1's 11:19Z single is a duplicate inside the authorized sequence.

## e57e61 (stated, as the round-23 analysis asked)

`TO-DEPLOY-e57e61` (FWD-10 producer apply, `~SD`) was APPLIED and proven 2026-10-08. Its remaining leg is the L3 verification, which waits on a scheduled new-security run that plans US stocks.
Hold condition: that run. Not cancelled (the apply is live; the leg only reads). Outside the verdict until it releases.

## Rows at this packet

D1-S33 (eight unnamed dates moved by the first e91 fire), D1-S35 and D1-S36 (the first post-ship fire and its correction), D1-S37 (C_06 byte-nondeterministic, content-idempotent), D1-S38 (D1-W83-S5 disarmed).
**D1-W83-S5 is DISARMED.** Still open: D1-S27 (owner's acceptability ruling on the ~$128 share-rounding difference), D1-W78-S1 (INERT, cause untraced).

## Not shown

Production-fire idempotence (leg Q is an ad-hoc QA property); that no consumer keys on `mix_daily_summary.json`'s ETag; the bars and advisors clauses graded on re-based expected values (round 25);
the Q3/September bars restated is MET only as `restated_through` present, not as a class-level re-base. The client-facing Black Diamond Mix restated-history push waits on Andrew's word.

## The 17-FWD board (owed by the PIVOT DIRECTION, O7)

PENDING: the board is compiled from recorded states with citations and added to this packet in a following commit. No FWD is claimed REALIZED by this packet.
