# ADVI_BDPRCE -- round 3 L8 adjudication of the existing rows (dell1)

<sweep_watermark>2026-10-14T06:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T06:20:00Z. L8 packet: 2.0.0_SA_COO~K1 msg 5442, `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)`.
Round 3 was REOPENED at @13167533b7 (msg 5446) under CTO R1 Amendment 4 (msg 5443): BP-c-2 and BP-c-3 re-run on R1.4, and neither is graded here.
59 rows swept since ADJUDICATION_v2: 10 graduate (8 ARMED, 2 INERT), held in `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BDPRCE_R3_REMEDIATION_HELD_20261014.md` until the row gate admits REMEDIATION_v3; 49 dismissed.
No L10 slug while the round is reopened; it waits for 2.0.0_SA_COO~K1's second close.

```json
[
  {
    "id": "ADVI_BDPRCE-D1-C-S38",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "Round-3 L8 compile of the existing rows (7 orders; BP-c-2 and BP-c-3 REOPENED at @13167533b7 under CTO R1 Amendment 4, msg 5443, and NOT graded here; no JUDGMENT criterion in the round). This seat's own runs on box/dell1 at 13167533b7: test_bd_price_rule 'OK 53 arms', AMENDMENT = 'R1.3'; r3_checks ruleprobe3 'per100=1 per_unit=824 unreadable=63 unit_changed=0', cap 'days=76 at_500000=15 verdict=CAP', lotproof3 'legacy_equal=true units_in_key=true folded_without_units=192 zero_fold=deferred', sentinel 'runs=14 honest=19 dishonest=2 cause=EXPORT_WINDOW_RULE deployed=true', offcanon 'lots=1859 older_canonical=310 daily=0 other=1118 unexplained=431'; test_lot_split3 'OK 10 arms'; r3_selftest 'OK 55 arms'. Live reads: canonical_prices.parquet ETag a88a7030f4506ac7e0cdb844382f9d16 (LastModified 04:03:36Z, the object REPLAY3 read); bronze/<date>/_BRONZE_COMPLETE.json present for 2026-10-12 (363 B), 10-13 (277 B), 10-14 (277 B). MOVERS3.csv effects re-summed: 90,964.77 / 358,069.96 / 103,614.55 (packet 90,964.76 / 358,069.95 / 103,614.56, rounding). Corroboration only: BEFORE_AFTER3.csv row 1647 shows SIX FLAGS served 11.41 from a Transfer In (old_price_types 'Transfer In:4') replaced by a 2025-08-04 carry of 30.805, the case Amendment 4 already rules; no new row. 59 rows swept since ADJUDICATION_v2's watermark: 10 graduate (8 ARMED, 2 INERT), 49 dismissed. The graduates are HELD in org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BDPRCE_R3_REMEDIATION_HELD_20261014.md because the row gate refuses a remediation row while BP-c-2 and BP-c-3 are non-terminal; they land as REMEDIATION_v3 at ~K1's second close. No L10 slug while the round is reopened. REMEDIATION_v1/v2 rows unchanged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Round-3 L8 compile of the existing rows (7 orders; BP-c-2 and BP-c-3 REOPENED at @13167533b7 under CTO R1 Amendment 4, msg 5443, and NOT graded here; no JUDGMENT criterion in the round). This seat's own runs on box/dell1 at 13167533b7: test_bd_price_rule 'OK 53 arms', AMENDMENT = 'R1.3'; r3_checks ruleprobe3 'per100=1 per_unit=824 unreadable=63 unit_changed=0', cap 'days=76 at_500000=15 verdict=CAP', lotproof3 'legacy_equal=true units_in_key=true folded_without_units=192 zero_fold=deferred', sentinel 'runs=14 honest=19 dishonest=2 cause=EXPORT_WINDOW_RULE deployed=true', offcanon 'lots=1859 older_canonical=310 daily=0 other=1118 unexplained=431'; test_lot_split3 'OK 10 arms'; r3_selftest 'OK 55 arms'. Live reads: canonical_prices.parquet ETag a88a7030f4506ac7e0cdb844382f9d16 (LastModified 04:03:36Z, the object REPLAY3 read); bronze/<date>/_BRONZE_COMPLETE.json present for 2026-10-12 (363 B), 10-13 (277 B), 10-14 (277 B). MOVERS3.csv effects re-summed: 90,964.77 / 358,069.96 / 103,614.55 (packet 90,964.76 / 358,069.95 / 103,614.56, rounding). Corroboration only: BEFORE_AFTER3.csv row 1647 shows SIX FLAGS served 11.41 from a Transfer In (old_price_types 'Transfer In:4') replaced by a 2025-08-04 carry of 30.805, the case Amendment 4 already rules; no new row. 59 rows swept since ADJUDICATION_v2's watermark: 10 graduate (8 ARMED, 2 INERT), 49 dismissed. The graduates are HELD in org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BDPRCE_R3_REMEDIATION_HELD_20261014.md because the row gate refuses a remediation row while BP-c-2 and BP-c-3 are non-terminal; they land as REMEDIATION_v3 at ~K1's second close. No L10 slug while the round is reopened. REMEDIATION_v1/v2 rows unchanged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO runs 2026-10-14T06:0xZ of data/black_diamond/scripts/silver/tests/test_bd_price_rule.py, deliverables/2.0.0_SA_COO~K1/round3/checks/r3_checks.py (ruleprobe3, cap, lotproof3, sentinel, offcanon), r3_selftest.py, deliverables/0.9.0_WK_ADVI_BDPRCE~23/test_lot_split3.py",
        "3.0.0_SA_CVO aws s3api head-object opal-data-bd silver/prices/canonical_prices.parquet and bronze/2026-10-1{2,3,4}/_BRONZE_COMPLETE.json",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)",
        "ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md AMENDMENT 4 @3a0ffc0946; reopen @13167533b7 (BP-c-2 pending, BP-c-3 staged)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Round-3 L8 compile of the existing rows (7 orders; BP-c-2 and BP-c-3 REOPENED at @13167533b7 under CTO R1 Amendment 4, msg 5443, and NOT graded here; no JUDGMENT criterion in the round). This seat's own runs on box/dell1 at 13167533b7: test_bd_price_rule 'OK 53 arms', AMENDMENT = 'R1.3'; r3_checks ruleprobe3 'per100=1 per_unit=824 unreadable=63 unit_changed=0', cap 'days=76 at_500000=15 verdict=CAP', lotproof3 'legacy_equal=true units_in_key=true folded_without_units=192 zero_fold=deferred', sentinel 'runs=14 honest=19 dishonest=2 cause=EXPORT_WINDOW_RULE deployed=true', offcanon 'lots=1859 older_canonical=310 daily=0 other=1118 unexplained=431'; test_lot_split3 'OK 10 arms'; r3_selftest 'OK 55 arms'. Live reads: canonical_prices.parquet ETag a88a7030f4506ac7e0cdb844382f9d16 (LastModified 04:03:36Z, the object REPLAY3 read); bronze/<date>/_BRONZE_COMPLETE.json present for 2026-10-12 (363 B), 10-13 (277 B), 10-14 (277 B). MOVERS3.csv effects re-summed: 90,964.77 / 358,069.96 / 103,614.55 (packet 90,964.76 / 358,069.95 / 103,614.56, rounding). Corroboration only: BEFORE_AFTER3.csv row 1647 shows SIX FLAGS served 11.41 from a Transfer In (old_price_types 'Transfer In:4') replaced by a 2025-08-04 carry of 30.805, the case Amendment 4 already rules; no new row. 59 rows swept since ADJUDICATION_v2's watermark: 10 graduate (8 ARMED, 2 INERT), 49 dismissed. The graduates are HELD in org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BDPRCE_R3_REMEDIATION_HELD_20261014.md because the row gate refuses a remediation row while BP-c-2 and BP-c-3 are non-terminal; they land as REMEDIATION_v3 at ~K1's second close. No L10 slug while the round is reopened. REMEDIATION_v1/v2 rows unchanged."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S39",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "Eight rows graduate ARMED (held for REMEDIATION_v3): W16-S2 BLOCKING (the 500,000-row export cap; this seat's cap run reads 15 of 76 days at 500,000) and W16-S1 (bronze unrealized keys only on Fridays) for the paging design; W17-S1 BLOCKING (the five-column key folds 192 rows) and W23-S1 (the synthetic-units zero is not evidence) until the first real export under the apply's pair reads 0 folded; W18-S4 (a header-only Monday/Tuesday transactions export completes a day; sentinels for 10-12 and 10-13 read present here) for the shared-module window fix; W20-S8 (the served canonical object is rewritten by writers not named in the round); W20-S11 (19 served Fixed Income rows and 59 no-pair assets withheld unit_unreadable; the band is the CTO's call); W20-S13 RE-SCOPED by this seat: the module's served_unit_map(pairs) returns what its caller passes, and the two round-3 callers disagree -- RULE_PROBE3 pools all pairs (per_unit 824, unreadable 63) while the replay passes one source per asset (827, 60), so ISHARES CORE U.S. AGGREGATE BOND ETF and SIX FLAGS read different units under the same module (W21-S5).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W16-S2",
      "ADVI_BDPRCE-D1-W16-S1",
      "ADVI_BDPRCE-D1-W17-S1",
      "ADVI_BDPRCE-D1-W23-S1",
      "ADVI_BDPRCE-D1-W18-S4",
      "ADVI_BDPRCE-D1-W20-S8",
      "ADVI_BDPRCE-D1-W20-S11",
      "ADVI_BDPRCE-D1-W20-S13"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Eight rows graduate ARMED (held for REMEDIATION_v3): W16-S2 BLOCKING (the 500,000-row export cap; this seat's cap run reads 15 of 76 days at 500,000) and W16-S1 (bronze unrealized keys only on Fridays) for the paging design; W17-S1 BLOCKING (the five-column key folds 192 rows) and W23-S1 (the synthetic-units zero is not evidence) until the first real export under the apply's pair reads 0 folded; W18-S4 (a header-only Monday/Tuesday transactions export completes a day; sentinels for 10-12 and 10-13 read present here) for the shared-module window fix; W20-S8 (the served canonical object is rewritten by writers not named in the round); W20-S11 (19 served Fixed Income rows and 59 no-pair assets withheld unit_unreadable; the band is the CTO's call); W20-S13 RE-SCOPED by this seat: the module's served_unit_map(pairs) returns what its caller passes, and the two round-3 callers disagree -- RULE_PROBE3 pools all pairs (per_unit 824, unreadable 63) while the replay passes one source per asset (827, 60), so ISHARES CORE U.S. AGGREGATE BOND ETF and SIX FLAGS read different units under the same module (W21-S5).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_BDPRCE-D1-W16-S2, ADVI_BDPRCE-D1-W16-S1, ADVI_BDPRCE-D1-W17-S1, ADVI_BDPRCE-D1-W23-S1, ADVI_BDPRCE-D1-W18-S4, ADVI_BDPRCE-D1-W20-S8, ADVI_BDPRCE-D1-W20-S11, ADVI_BDPRCE-D1-W20-S13",
        "deliverables/0.9.0_WK_ADVI_BDPRCE~20/RULE_PROBE3.json served_units {per100 1, per_unit 824, unreadable 63}, units_source 'one median per asset over all its pairs'",
        "deliverables/0.9.0_WK_ADVI_BDPRCE~21/REPLAY3.json served_units {per100 1, per_unit 827, unreadable 60}; unit_map_pairs.py line 10 'over the pairs of that one source'; BEFORE_AFTER3.csv ISHARES CORE U.S. AGGREGATE BOND ETF per_unit",
        "data/black_diamond/scripts/silver/bd_price_rule.py:218 served_unit_map(pairs)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated ARMED; held in org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BDPRCE_R3_REMEDIATION_HELD_20261014.md until the row gate admits REMEDIATION_v3 (every round-3 order terminal)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S40",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "Two rows graduate INERT (held for REMEDIATION_v3): W19-S2 (the newest Schwab RPS partition is 2026-07-23, yet it prices 1,118 of the 1,859 off-canonical lots; with the 431 unexplained lots, 34 of them 'nan', it is round-4 enrichment item 4) and W22-S1 (726 of 819 lots in moving assets carry a price other than the served price, so the packet's dollar effect depends on its basis; which basis is the true change in Andrew's book is the CTO's call, and it persists into the R1.4 packet).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W19-S2",
      "ADVI_BDPRCE-D1-W22-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Two rows graduate INERT (held for REMEDIATION_v3): W19-S2 (the newest Schwab RPS partition is 2026-07-23, yet it prices 1,118 of the 1,859 off-canonical lots; with the 431 unexplained lots, 34 of them 'nan', it is round-4 enrichment item 4) and W22-S1 (726 of 819 lots in moving assets carry a price other than the served price, so the packet's dollar effect depends on its basis; which basis is the true change in Andrew's book is the CTO's call, and it persists into the R1.4 packet).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_BDPRCE-D1-W19-S2, ADVI_BDPRCE-D1-W22-S1",
        "deliverables/0.9.0_WK_ADVI_BDPRCE~19/OFFCANON.json (offcanon run above)",
        "deliverables/0.9.0_WK_ADVI_BDPRCE~22/PACKET3.json dollar_effect_* fields"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated INERT; held in org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BDPRCE_R3_REMEDIATION_HELD_20261014.md."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S41",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S1 dismissed: superseded: Amendments 2 and 3 replace the coupon test with the per-row Fixed Income ratio test read in the served unit; RULE_PROBE3 par_quoted assets_scaled 8, unit_changed_assets 0, and R3_CLOSE section 1 reads the eight round-2 par rows equal to the served price (8 of 8).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S1 dismissed: superseded: Amendments 2 and 3 replace the coupon test with the per-row Fixed Income ratio test read in the served unit; RULE_PROBE3 par_quoted assets_scaled 8, unit_changed_assets 0, and R3_CLOSE section 1 reads the eight round-2 par rows equal to the served price (8 of 8).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S1",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S1 dismissed: superseded: Amendments 2 and 3 replace the coupon test with the per-row Fixed Income ratio test read in the served unit; RULE_PROBE3 par_quoted assets_scaled 8, unit_changed_assets 0, and R3_CLOSE section 1 reads the eight round-2 par rows equal to the served price (8 of 8)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S42",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S2 dismissed: superseded: the per-row test reads each row, so a name whose rows disagree on the old candidate test is no longer classed by name (Amendment 2).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S2 dismissed: superseded: the per-row test reads each row, so a name whose rows disagree on the old candidate test is no longer classed by name (Amendment 2).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S2",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S2 dismissed: superseded: the per-row test reads each row, so a name whose rows disagree on the old candidate test is no longer classed by name (Amendment 2)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S43",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S3 dismissed: Corporate Action is not a trade under Amendment 1; the module excludes and counts it UNCLASSIFIED, which withholds rather than prices.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S3 dismissed: Corporate Action is not a trade under Amendment 1; the module excludes and counts it UNCLASSIFIED, which withholds rather than prices.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S3",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S3 dismissed: Corporate Action is not a trade under Amendment 1; the module excludes and counts it UNCLASSIFIED, which withholds rather than prices."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S44",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S4 dismissed: the probe read 2026-09-16 as well (row text); the omission in the order's date list cost no count.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S4 dismissed: the probe read 2026-09-16 as well (row text); the omission in the order's date list cost no count.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S4",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S4 dismissed: the probe read 2026-09-16 as well (row text); the omission in the order's date list cost no count."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S45",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S5 dismissed: a disagreement between two round-2 variant records; variant A was not adopted and the R1.3 module supersedes both records; no current reader.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S5 dismissed: a disagreement between two round-2 variant records; variant A was not adopted and the R1.3 module supersedes both records; no current reader.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S5",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S5 dismissed: a disagreement between two round-2 variant records; variant A was not adopted and the R1.3 module supersedes both records; no current reader."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S46",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S6 dismissed: the two 0.0 Sale rows are excluded under clause 3 and counted in no_price_excluded; they never become a price.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S6 dismissed: the two 0.0 Sale rows are excluded under clause 3 and counted in no_price_excluded; they never become a price.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S6",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S6 dismissed: the two 0.0 Sale rows are excluded under clause 3 and counted in no_price_excluded; they never become a price."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S47",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S7 dismissed: the naming gate refused as built; the module now takes the field names as arguments and test_bd_price_rule reads OK 53 arms on this seat's run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S7 dismissed: the naming gate refused as built; the module now takes the field names as arguments and test_bd_price_rule reads OK 53 arms on this seat's run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S7",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S7 dismissed: the naming gate refused as built; the module now takes the field names as arguments and test_bd_price_rule reads OK 53 arms on this seat's run."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S48",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S8 dismissed: ALLSPRING CORE BOND CIT CLASS E2 is classed To Be Classified, so it keeps its price as a non-Fixed-Income row: the order's intended outcome (left alone per unit) by another path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S8 dismissed: ALLSPRING CORE BOND CIT CLASS E2 is classed To Be Classified, so it keeps its price as a non-Fixed-Income row: the order's intended outcome (left alone per unit) by another path.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S8",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S8 dismissed: ALLSPRING CORE BOND CIT CLASS E2 is classed To Be Classified, so it keeps its price as a non-Fixed-Income row: the order's intended outcome (left alone per unit) by another path."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S49",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S9 dismissed: the two funds at ratios 1.04 and 1.08 are the fixed-income-fund band case carried by W20-S11 (graduated ARMED, the CTO's band call).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S9"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S9 dismissed: the two funds at ratios 1.04 and 1.08 are the fixed-income-fund band case carried by W20-S11 (graduated ARMED, the CTO's band call).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S9",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S9 dismissed: the two funds at ratios 1.04 and 1.08 are the fixed-income-fund band case carried by W20-S11 (graduated ARMED, the CTO's band call)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S50",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S10 dismissed: superseded with W13-S2 by the per-row test of Amendment 2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S10 dismissed: superseded with W13-S2 by the per-row test of Amendment 2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S10",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S10 dismissed: superseded with W13-S2 by the per-row test of Amendment 2."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S51",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S11 dismissed: a non-Fixed-Income row keeps its price whatever the unit (W20-S12 world_is; Amendment 3: R1 changes values, never units); the residual band question is carried by W20-S11.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S11"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S11 dismissed: a non-Fixed-Income row keeps its price whatever the unit (W20-S12 world_is; Amendment 3: R1 changes values, never units); the residual band question is carried by W20-S11.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S11",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S11 dismissed: a non-Fixed-Income row keeps its price whatever the unit (W20-S12 world_is; Amendment 3: R1 changes values, never units); the residual band question is carried by W20-S11."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S52",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W13-S12 dismissed: the one out-of-scope path is the task order, edited by the issuer's own commit 544d551f1d, not by the worker.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W13-S12"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S12 dismissed: the one out-of-scope path is the task order, edited by the issuer's own commit 544d551f1d, not by the worker.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W13-S12",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S12 dismissed: the one out-of-scope path is the task order, edited by the issuer's own commit 544d551f1d, not by the worker."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S53",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W18-S1 dismissed: a log-retention correction; SENTINEL.json states the basis (14 run dates readable, 2026-09-29 and 09-30 past retention).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W18-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W18-S1 dismissed: a log-retention correction; SENTINEL.json states the basis (14 run dates readable, 2026-09-29 and 09-30 past retention).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W18-S1",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W18-S1 dismissed: a log-retention correction; SENTINEL.json states the basis (14 run dates readable, 2026-09-29 and 09-30 past retention)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S54",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W18-S2 dismissed: the grant is narrower than the commit message says and still covers the read-back; this seat reads the 10-12, 10-13 and 10-14 sentinels present.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W18-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W18-S2 dismissed: the grant is narrower than the commit message says and still covers the read-back; this seat reads the 10-12, 10-13 and 10-14 sentinels present.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W18-S2",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W18-S2 dismissed: the grant is narrower than the commit message says and still covers the read-back; this seat reads the 10-12, 10-13 and 10-14 sentinels present."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S55",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W18-S3 dismissed: 2026-09-14 and 09-15 join the sentinel-less Monday/Tuesday set; carried by W18-S4 (graduated ARMED, re-land and re-emit the Monday and Tuesday dates) and REMEDIATION_v1 W3-S2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W18-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W18-S3 dismissed: 2026-09-14 and 09-15 join the sentinel-less Monday/Tuesday set; carried by W18-S4 (graduated ARMED, re-land and re-emit the Monday and Tuesday dates) and REMEDIATION_v1 W3-S2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W18-S3",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W18-S3 dismissed: 2026-09-14 and 09-15 join the sentinel-less Monday/Tuesday set; carried by W18-S4 (graduated ARMED, re-land and re-emit the Monday and Tuesday dates) and REMEDIATION_v1 W3-S2."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S56",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W18-S5 dismissed: an order pointer corrected by the worker; SENTINEL.json window_rule cites cot_bronze_ingest.py and BD_TXN_CHUNK_DAYS=3, which W18-S4 carries.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W18-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W18-S5 dismissed: an order pointer corrected by the worker; SENTINEL.json window_rule cites cot_bronze_ingest.py and BD_TXN_CHUNK_DAYS=3, which W18-S4 carries.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W18-S5",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W18-S5 dismissed: an order pointer corrected by the worker; SENTINEL.json window_rule cites cot_bronze_ingest.py and BD_TXN_CHUNK_DAYS=3, which W18-S4 carries."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S57",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W17-S2 dismissed: a count-basis correction of round 2's record; the round-3 key decision rests on the 192-row fold (W17-S1), not on these counts.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W17-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W17-S2 dismissed: a count-basis correction of round 2's record; the round-3 key decision rests on the 192-row fold (W17-S1), not on these counts.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W17-S2",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W17-S2 dismissed: a count-basis correction of round 2's record; the round-3 key decision rests on the 192-row fold (W17-S1), not on these counts."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S58",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W17-S3 dismissed: carried by W16-S2 (graduated ARMED): the paging design cell is where slice exports are made.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W17-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W17-S3 dismissed: carried by W16-S2 (graduated ARMED): the paging design cell is where slice exports are made.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W17-S3",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W17-S3 dismissed: carried by W16-S2 (graduated ARMED): the paging design cell is where slice exports are made."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S59",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W19-S1 dismissed: the 34 'nan' lots sit inside the 431 unexplained off-canonical lots carried by W19-S2 (graduated INERT).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W19-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W19-S1 dismissed: the 34 'nan' lots sit inside the 431 unexplained off-canonical lots carried by W19-S2 (graduated INERT).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W19-S1",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W19-S1 dismissed: the 34 'nan' lots sit inside the 431 unexplained off-canonical lots carried by W19-S2 (graduated INERT)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S60",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W19-S3 dismissed: historical_prices has no asset_name and the lots no ticker, so no binding exists; the offcanon classification (310/0/1118/431) stands on this seat's run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W19-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W19-S3 dismissed: historical_prices has no asset_name and the lots no ticker, so no binding exists; the offcanon classification (310/0/1118/431) stands on this seat's run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W19-S3",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W19-S3 dismissed: historical_prices has no asset_name and the lots no ticker, so no binding exists; the offcanon classification (310/0/1118/431) stands on this seat's run."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S61",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W14-S1 dismissed: the canonical object's rewrites are carried by W20-S8 (graduated ARMED); the R1.2 replay this row qualifies is superseded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W14-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W14-S1 dismissed: the canonical object's rewrites are carried by W20-S8 (graduated ARMED); the R1.2 replay this row qualifies is superseded.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W14-S1",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W14-S1 dismissed: the canonical object's rewrites are carried by W20-S8 (graduated ARMED); the R1.2 replay this row qualifies is superseded."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S62",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W14-S2 dismissed: the seat re-fetched and verified the current objects; REPLAY3 verifies 1,928 partitions by md5 or size, and the reopened BP-c-2 re-reads them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W14-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W14-S2 dismissed: the seat re-fetched and verified the current objects; REPLAY3 verifies 1,928 partitions by md5 or size, and the reopened BP-c-2 re-reads them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W14-S2",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W14-S2 dismissed: the seat re-fetched and verified the current objects; REPLAY3 verifies 1,928 partitions by md5 or size, and the reopened BP-c-2 re-reads them."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S63",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W14-S3 dismissed: the absent 2026-10-13 partition and the late-landed 10-14 partition are the Monday/Tuesday window cause carried by W18-S4.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W14-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W14-S3 dismissed: the absent 2026-10-13 partition and the late-landed 10-14 partition are the Monday/Tuesday window cause carried by W18-S4.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W14-S3",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W14-S3 dismissed: the absent 2026-10-13 partition and the late-landed 10-14 partition are the Monday/Tuesday window cause carried by W18-S4."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S64",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W14-S4 dismissed: a scope fact: the replay fates interpolated rows on the served set only, as ordered; unserved assets serve no price.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W14-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W14-S4 dismissed: a scope fact: the replay fates interpolated rows on the served set only, as ordered; unserved assets serve no price.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W14-S4",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W14-S4 dismissed: a scope fact: the replay fates interpolated rows on the served set only, as ordered; unserved assets serve no price."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S65",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W14-S5 dismissed: ARMED, disarmed on this seat's read: RULE_PROBE3 per100_assets lists MORGAN STANLEY FIN LLC 0% 05/03/2029; BEFORE_AFTER3.csv reads it per100 with the 2026-10-05 carry at 100.0 and unit_changed 0; the 100x move cannot occur under Amendment 3, and Amendment 4 further keeps the served 115.995 against the 16-month carry.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W14-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W14-S5 dismissed: ARMED, disarmed on this seat's read: RULE_PROBE3 per100_assets lists MORGAN STANLEY FIN LLC 0% 05/03/2029; BEFORE_AFTER3.csv reads it per100 with the 2026-10-05 carry at 100.0 and unit_changed 0; the 100x move cannot occur under Amendment 3, and Amendment 4 further keeps the served 115.995 against the 16-month carry.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W14-S5",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W14-S5 dismissed: ARMED, disarmed on this seat's read: RULE_PROBE3 per100_assets lists MORGAN STANLEY FIN LLC 0% 05/03/2029; BEFORE_AFTER3.csv reads it per100 with the 2026-10-05 carry at 100.0 and unit_changed 0; the 100x move cannot occur under Amendment 3, and Amendment 4 further keeps the served 115.995 against the 16-month carry."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S66",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W14-S6 dismissed: the conservative reading (refuse the carry) withholds rather than prices; R3_CLOSE section 3 item 5 counts the 3 refused carries.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W14-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W14-S6 dismissed: the conservative reading (refuse the carry) withholds rather than prices; R3_CLOSE section 3 item 5 counts the 3 refused carries.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W14-S6",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W14-S6 dismissed: the conservative reading (refuse the carry) withholds rather than prices; R3_CLOSE section 3 item 5 counts the 3 refused carries."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S67",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W14-S7 dismissed: a count correction of the order's prose; no decision rests on it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W14-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W14-S7 dismissed: a count correction of the order's prose; no decision rests on it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W14-S7",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W14-S7 dismissed: a count correction of the order's prose; no decision rests on it."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S68",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W14-S8 dismissed: the nine-fund ratio cluster is the band case carried by W20-S11.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W14-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W14-S8 dismissed: the nine-fund ratio cluster is the band case carried by W20-S11.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W14-S8",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W14-S8 dismissed: the nine-fund ratio cluster is the band case carried by W20-S11."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S69",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W20-S1 dismissed: ARMED, superseded: the unit source moved from the lot extract to served pairs (Amendment 3 clause 1); RULE_PROBE3 reads MORGAN STANLEY per100 from trade pairs, so the missing lots no longer block a unit read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W20-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W20-S1 dismissed: ARMED, superseded: the unit source moved from the lot extract to served pairs (Amendment 3 clause 1); RULE_PROBE3 reads MORGAN STANLEY per100 from trade pairs, so the missing lots no longer block a unit read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W20-S1",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W20-S1 dismissed: ARMED, superseded: the unit source moved from the lot extract to served pairs (Amendment 3 clause 1); RULE_PROBE3 reads MORGAN STANLEY per100 from trade pairs, so the missing lots no longer block a unit read."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S70",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W20-S2 dismissed: ARMED, superseded by the served-pair source; its residual (withheld Fixed Income rows) is re-read as W20-S11, graduated ARMED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W20-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W20-S2 dismissed: ARMED, superseded by the served-pair source; its residual (withheld Fixed Income rows) is re-read as W20-S11, graduated ARMED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W20-S2",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W20-S2 dismissed: ARMED, superseded by the served-pair source; its residual (withheld Fixed Income rows) is re-read as W20-S11, graduated ARMED."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S71",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W20-S3 dismissed: the probe added 2026-09-16 and 09-17 (row text); no count was lost.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W20-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W20-S3 dismissed: the probe added 2026-09-16 and 09-17 (row text); no count was lost.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W20-S3",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W20-S3 dismissed: the probe added 2026-09-16 and 09-17 (row text); no count was lost."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S72",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W20-S4 dismissed: skipping a lot with no positive current price is required: no ratio exists for it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W20-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W20-S4 dismissed: skipping a lot with no positive current price is required: no ratio exists for it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W20-S4",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W20-S4 dismissed: skipping a lot with no positive current price is required: no ratio exists for it."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S73",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W20-S5 dismissed: ARMED, superseded: RULE_PROBE3 per100_assets = [MORGAN STANLEY FIN LLC 0% 05/03/2029], so R1.3 reads it per100, not unreadable.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W20-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W20-S5 dismissed: ARMED, superseded: RULE_PROBE3 per100_assets = [MORGAN STANLEY FIN LLC 0% 05/03/2029], so R1.3 reads it per100, not unreadable.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W20-S5",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W20-S5 dismissed: ARMED, superseded: RULE_PROBE3 per100_assets = [MORGAN STANLEY FIN LLC 0% 05/03/2029], so R1.3 reads it per100, not unreadable."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S74",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W20-S6 dismissed: ARMED, superseded: the final served-unit read is per100 1 (RULE_PROBE3 and REPLAY3), not 0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W20-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W20-S6 dismissed: ARMED, superseded: the final served-unit read is per100 1 (RULE_PROBE3 and REPLAY3), not 0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W20-S6",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W20-S6 dismissed: ARMED, superseded: the final served-unit read is per100 1 (RULE_PROBE3 and REPLAY3), not 0."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S75",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W20-S7 dismissed: a cache-path correction; the probe read the manifest paths.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W20-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W20-S7 dismissed: a cache-path correction; the probe read the manifest paths.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W20-S7",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W20-S7 dismissed: a cache-path correction; the probe read the manifest paths."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S76",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W20-S9 dismissed: ARMED, superseded by its own re-read W20-S11 (graduated ARMED).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W20-S9"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W20-S9 dismissed: ARMED, superseded by its own re-read W20-S11 (graduated ARMED).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W20-S9",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W20-S9 dismissed: ARMED, superseded by its own re-read W20-S11 (graduated ARMED)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S77",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W20-S10 dismissed: a re-read of W20-S1 after the second correction; the nine names take their units from trade and served pairs, as W20-S1's dismissal states.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W20-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W20-S10 dismissed: a re-read of W20-S1 after the second correction; the nine names take their units from trade and served pairs, as W20-S1's dismissal states.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W20-S10",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W20-S10 dismissed: a re-read of W20-S1 after the second correction; the nine names take their units from trade and served pairs, as W20-S1's dismissal states."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S78",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W20-S12 dismissed: the four between-band assets are carried by W20-S11 (the band) and W20-S13 (the pair source).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W20-S12"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W20-S12 dismissed: the four between-band assets are carried by W20-S11 (the band) and W20-S13 (the pair source).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W20-S12",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W20-S12 dismissed: the four between-band assets are carried by W20-S11 (the band) and W20-S13 (the pair source)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S79",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W21-S1 dismissed: the 1,689 vs 1,664 difference is the canonical object rewrite carried by W20-S8; REPLAY3 is keyed on the 04:03:36Z object, the same ETag this seat reads live.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W21-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W21-S1 dismissed: the 1,689 vs 1,664 difference is the canonical object rewrite carried by W20-S8; REPLAY3 is keyed on the 04:03:36Z object, the same ETag this seat reads live.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W21-S1",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W21-S1 dismissed: the 1,689 vs 1,664 difference is the canonical object rewrite carried by W20-S8; REPLAY3 is keyed on the 04:03:36Z object, the same ETag this seat reads live."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S80",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W21-S2 dismissed: the 12,070 withheld Fixed Income trade rows on 102 assets are the no-pair and band case carried by W20-S11.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W21-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W21-S2 dismissed: the 12,070 withheld Fixed Income trade rows on 102 assets are the no-pair and band case carried by W20-S11.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W21-S2",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W21-S2 dismissed: the 12,070 withheld Fixed Income trade rows on 102 assets are the no-pair and band case carried by W20-S11."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S81",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W21-S3 dismissed: the order's 214 has no stated basis; the 27 window rows carry 100.0 per100, and the par-carry hazard closes with W14-S5.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W21-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W21-S3 dismissed: the order's 214 has no stated basis; the 27 window rows carry 100.0 per100, and the par-carry hazard closes with W14-S5.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W21-S3",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W21-S3 dismissed: the order's 214 has no stated basis; the 27 window rows carry 100.0 per100, and the par-carry hazard closes with W14-S5."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S82",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W21-S4 dismissed: partition drift since the second seat's manifest; REPLAY3 re-verified 1,928 partitions and the reopened replay re-reads them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W21-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W21-S4 dismissed: partition drift since the second seat's manifest; REPLAY3 re-verified 1,928 partitions and the reopened replay re-reads them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W21-S4",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W21-S4 dismissed: partition drift since the second seat's manifest; REPLAY3 re-verified 1,928 partitions and the reopened replay re-reads them."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S83",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W21-S5 dismissed: the pooled vs one-source unit read for SIX FLAGS is the caller disagreement carried by W20-S13 (graduated ARMED).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W21-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W21-S5 dismissed: the pooled vs one-source unit read for SIX FLAGS is the caller disagreement carried by W20-S13 (graduated ARMED).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W21-S5",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W21-S5 dismissed: the pooled vs one-source unit read for SIX FLAGS is the caller disagreement carried by W20-S13 (graduated ARMED)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S84",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W22-S2 dismissed: only 15 served prices move, and the list holds all 15; BP-c-3 is re-staged under R1.4.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W22-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W22-S2 dismissed: only 15 served prices move, and the list holds all 15; BP-c-3 is re-staged under R1.4.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W22-S2",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W22-S2 dismissed: only 15 served prices move, and the list holds all 15; BP-c-3 is re-staged under R1.4."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S85",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W22-S3 dismissed: the same 34 'nan' lots as W19-S1, carried by W19-S2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W22-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W22-S3 dismissed: the same 34 'nan' lots as W19-S1, carried by W19-S2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W22-S3",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W22-S3 dismissed: the same 34 'nan' lots as W19-S1, carried by W19-S2."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S86",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W22-S4 dismissed: the interpolated-row moves are stated separately in the packet with their basis; their place in the dollar effect is carried by W22-S1 (graduated INERT).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W22-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W22-S4 dismissed: the interpolated-row moves are stated separately in the packet with their basis; their place in the dollar effect is carried by W22-S1 (graduated INERT).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W22-S4",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W22-S4 dismissed: the interpolated-row moves are stated separately in the packet with their basis; their place in the dollar effect is carried by W22-S1 (graduated INERT)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S87",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W22-S5 dismissed: the decision sentence is the worker's composition and R3_CLOSE section 2 says so; the CTO puts the packet to Andrew, and the packet is regenerated on R1.4.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W22-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W22-S5 dismissed: the decision sentence is the worker's composition and R3_CLOSE section 2 says so; the CTO puts the packet to Andrew, and the packet is regenerated on R1.4.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W22-S5",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W22-S5 dismissed: the decision sentence is the worker's composition and R3_CLOSE section 2 says so; the CTO puts the packet to Andrew, and the packet is regenerated on R1.4."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S88",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W23-S2 dismissed: test plumbing; test_lot_split3 reads OK 10 arms on this seat's run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W23-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W23-S2 dismissed: test plumbing; test_lot_split3 reads OK 10 arms on this seat's run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W23-S2",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W23-S2 dismissed: test plumbing; test_lot_split3 reads OK 10 arms on this seat's run."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S89",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T06:20:00Z",
    "one_line": "D1-W23-S3 dismissed: the legacy bytes carry _ingested_at; lotproof3 legacy_equal=true is read under the pinned clock, which the record states.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W23-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W23-S3 dismissed: the legacy bytes carry _ingested_at; lotproof3 legacy_equal=true is read under the pinned clock, which the record states.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W23-S3",
        "deliverables/2.0.0_SA_COO~K1/round3/R3_CLOSE.md @1002ff2446 (blob 63467699a7, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W23-S3 dismissed: the legacy bytes carry _ingested_at; lotproof3 legacy_equal=true is read under the pinned clock, which the record states."
  }
]
```
