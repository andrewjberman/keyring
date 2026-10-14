# ADVI_BDPRCE -- round 2 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-14T01:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T01:45:00Z. L8 packet: 2.0.0_SA_COO~K1 msg 5325,
`org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round2/R2_CLOSE.md` @a6e41177d6 (blob 1f1203ba74, verified).
27 rows swept since v1 (27 of 54; v1 settled the other 27): 5 ARMED graduated (W9-S2 re-classed ARMED by this seat), 5 INERT graduated, 17 dismissed.
One correction of this seat's own round-1 row (C-S17). REMEDIATION_v1 D1-W4-S6 REMEDIATED. No BLOCKING row; every ARMED row dispositioned.

```json
[
  {
    "id": "ADVI_BDPRCE-D1-C-S16",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "Round-2 L8/L9 read (8 orders, 7 complete, BP-b-7 superseded; all LOCAL, no JUDGMENT criterion): HOLDS on this seat's own runs from the merged tree (box/dell1 2855209f9b): test_bd_price_rule 'OK 15 arms'; ruleprobe 'assets=716 deterministic=true excluded_types=11'; replay 'served=1657 changed=824 unchanged=621 deterministic=true'; census 'objects=3510 lots=198295 off_canonical=1859 listed_untickered=1'; trace2 selftest 'OK 7 arms' and 'followed=canonical ... follows_served=true'; cause 'dates=6 determined=2 undetermined=4'; lotproof 'legacy_equal=true lots=484447 keyed_on_lot=true'; thread2 'rule=R1 distinct_trades=2 sources_checked=8 equal=true'. NOT re-run: BP-b-6 AC1 test_lot_split.py, whose recorded export input (ajb_workspace-data/UNREALIZED_DAILY_2026-10-09.xlsx) is absent on this box; its AC2 record check passes. The thread re-read by this seat: z08188711/detail.json VersionId HYPH2uKx..., data_as_of 2026-10-09, ALLSPRING CORE BOND CIT CLASS E2 72 open lots all at 10.3525, ticker null; silver/transactions/2026-10-02.parquet holds 2 Buys (ids 742108391, 742108404) at 10.352 and 10.353, median 10.3525. A second Allspring fund (Core Bond II CIT E, 36 lots at 11.542) sits in the same object and is a different security. Against the signed PRD v1.0: the served row for the thread is linear_interpolation (ARMED W12-S1), an estimated source label against Andrew's constraint, though its value equals R1's carry of the last trade; FWD-1's grade is the CTO's. Nothing served moved. round-close-check --round 2: MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Round-2 L8/L9 read (8 orders, 7 complete, BP-b-7 superseded; all LOCAL, no JUDGMENT criterion): HOLDS on this seat's own runs from the merged tree (box/dell1 2855209f9b): test_bd_price_rule 'OK 15 arms'; ruleprobe 'assets=716 deterministic=true excluded_types=11'; replay 'served=1657 changed=824 unchanged=621 deterministic=true'; census 'objects=3510 lots=198295 off_canonical=1859 listed_untickered=1'; trace2 selftest 'OK 7 arms' and 'followed=canonical ... follows_served=true'; cause 'dates=6 determined=2 undetermined=4'; lotproof 'legacy_equal=true lots=484447 keyed_on_lot=true'; thread2 'rule=R1 distinct_trades=2 sources_checked=8 equal=true'. NOT re-run: BP-b-6 AC1 test_lot_split.py, whose recorded export input (ajb_workspace-data/UNREALIZED_DAILY_2026-10-09.xlsx) is absent on this box; its AC2 record check passes. The thread re-read by this seat: z08188711/detail.json VersionId HYPH2uKx..., data_as_of 2026-10-09, ALLSPRING CORE BOND CIT CLASS E2 72 open lots all at 10.3525, ticker null; silver/transactions/2026-10-02.parquet holds 2 Buys (ids 742108391, 742108404) at 10.352 and 10.353, median 10.3525. A second Allspring fund (Core Bond II CIT E, 36 lots at 11.542) sits in the same object and is a different security. Against the signed PRD v1.0: the served row for the thread is linear_interpolation (ARMED W12-S1), an estimated source label against Andrew's constraint, though its value equals R1's carry of the last trade; FWD-1's grade is the CTO's. Nothing served moved. round-close-check --round 2: MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~K1/round2/checks/r2_checks.py (ruleprobe, replay, census, trace2, cause, lotproof, thread2) and the two self-tests, run by 3.0.0_SA_CVO 2026-10-14T01:3xZ",
        "3.0.0_SA_CVO boto3 reads of the thread object at its VersionId and of opal-data-bd silver/transactions/2026-10-02.parquet",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project ADVI_BDPRCE --round 2: verdict=MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Round-2 L8/L9 read (8 orders, 7 complete, BP-b-7 superseded; all LOCAL, no JUDGMENT criterion): HOLDS on this seat's own runs from the merged tree (box/dell1 2855209f9b): test_bd_price_rule 'OK 15 arms'; ruleprobe 'assets=716 deterministic=true excluded_types=11'; replay 'served=1657 changed=824 unchanged=621 deterministic=true'; census 'objects=3510 lots=198295 off_canonical=1859 listed_untickered=1'; trace2 selftest 'OK 7 arms' and 'followed=canonical ... follows_served=true'; cause 'dates=6 determined=2 undetermined=4'; lotproof 'legacy_equal=true lots=484447 keyed_on_lot=true'; thread2 'rule=R1 distinct_trades=2 sources_checked=8 equal=true'. NOT re-run: BP-b-6 AC1 test_lot_split.py, whose recorded export input (ajb_workspace-data/UNREALIZED_DAILY_2026-10-09.xlsx) is absent on this box; its AC2 record check passes. The thread re-read by this seat: z08188711/detail.json VersionId HYPH2uKx..., data_as_of 2026-10-09, ALLSPRING CORE BOND CIT CLASS E2 72 open lots all at 10.3525, ticker null; silver/transactions/2026-10-02.parquet holds 2 Buys (ids 742108391, 742108404) at 10.352 and 10.353, median 10.3525. A second Allspring fund (Core Bond II CIT E, 36 lots at 11.542) sits in the same object and is a different security. Against the signed PRD v1.0: the served row for the thread is linear_interpolation (ARMED W12-S1), an estimated source label against Andrew's constraint, though its value equals R1's carry of the last trade; FWD-1's grade is the CTO's. Nothing served moved. round-close-check --round 2: MAY-CLOSE."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S17",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "CORRECTION of this seat's round-1 row ADVI_BDPRCE-D1-C-S1: it read the round-1 thread price 168.94 (EXXONMOBIL HOLDINGS, 2026-10-09) as traced to 'one trade id' (745369343). Row D1-W5-S1 shows that id's four rows are Transfer In, not a trade; under R1 the asset has no price that day. C-S1's mechanical reads stand (4 rows, 1 id, median 168.94 equals served); its word 'trade' does not. The round-1 exemplar was a non-trade price, which the round-2 thread (BP-b-8) replaced.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-C-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "CORRECTION of this seat's round-1 row ADVI_BDPRCE-D1-C-S1: it read the round-1 thread price 168.94 (EXXONMOBIL HOLDINGS, 2026-10-09) as traced to 'one trade id' (745369343). Row D1-W5-S1 shows that id's four rows are Transfer In, not a trade; under R1 the asset has no price that day. C-S1's mechanical reads stand (4 rows, 1 id, median 168.94 equals served); its word 'trade' does not. The round-1 exemplar was a non-trade price, which the round-2 thread (BP-b-8) replaced.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W5-S1",
        "adjudication row ADVI_BDPRCE-D1-C-S1 (ADJUDICATION_v1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "CORRECTION of this seat's round-1 row ADVI_BDPRCE-D1-C-S1: it read the round-1 thread price 168.94 (EXXONMOBIL HOLDINGS, 2026-10-09) as traced to 'one trade id' (745369343). Row D1-W5-S1 shows that id's four rows are Transfer In, not a trade; under R1 the asset has no price that day. C-S1's mechanical reads stand (4 rows, 1 id, median 168.94 equals served); its word 'trade' does not. The round-1 exemplar was a non-trade price, which the round-2 thread (BP-b-8) replaced."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S18",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "Five rows graduate ARMED to REMEDIATION_v2. W7-S4 (the identity fails on 21,614 lots, 16,297 served market_value 0 with nonzero quantity), W10-S2 (the lot key folds 15,553 rows), W12-S1 (the served row is the banned linear_interpolation, an estimate label: Andrew's constraint), W6-S2 (par-quoted bonds 100x) keep the issuer as disarm owner; none disarms in round 2. W9-S2 is RE-CLASSED ARMED by this seat: the runner logs 'OK bronze sentinel emitted' with no sentinel in S3, which hides the Monday/Tuesday failures; routed to the CTO.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W7-S4",
      "ADVI_BDPRCE-D1-W10-S2",
      "ADVI_BDPRCE-D1-W12-S1",
      "ADVI_BDPRCE-D1-W6-S2",
      "ADVI_BDPRCE-D1-W9-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Five rows graduate ARMED to REMEDIATION_v2. W7-S4 (the identity fails on 21,614 lots, 16,297 served market_value 0 with nonzero quantity), W10-S2 (the lot key folds 15,553 rows), W12-S1 (the served row is the banned linear_interpolation, an estimate label: Andrew's constraint), W6-S2 (par-quoted bonds 100x) keep the issuer as disarm owner; none disarms in round 2. W9-S2 is RE-CLASSED ARMED by this seat: the runner logs 'OK bronze sentinel emitted' with no sentinel in S3, which hides the Monday/Tuesday failures; routed to the CTO.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_BDPRCE-D1-W7-S4, ADVI_BDPRCE-D1-W10-S2, ADVI_BDPRCE-D1-W12-S1, ADVI_BDPRCE-D1-W6-S2, ADVI_BDPRCE-D1-W9-S2"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v2.md (ARMED)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S19",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "Five rows graduate INERT to REMEDIATION_v2 with work owed: W5-S3 (the 2026-10-12 T-1 transactions partition has 0 rows: the Monday header-only export), W6-S3 (trades land up to 519 days late), W6-S5 (missing transactions dates), W10-S1 (PRD v1.0 CONTRACTS states the template sha256-equal to the repo; it is CRLF 14,419 vs LF 13,920, equal only normalised; a ratified-text fact this seat did not re-measure at signing; to the CTO for an addendum), W10-S3 (the export holds exactly 500,000 rows, possibly a truncation cap).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W5-S3",
      "ADVI_BDPRCE-D1-W6-S3",
      "ADVI_BDPRCE-D1-W6-S5",
      "ADVI_BDPRCE-D1-W10-S1",
      "ADVI_BDPRCE-D1-W10-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Five rows graduate INERT to REMEDIATION_v2 with work owed: W5-S3 (the 2026-10-12 T-1 transactions partition has 0 rows: the Monday header-only export), W6-S3 (trades land up to 519 days late), W6-S5 (missing transactions dates), W10-S1 (PRD v1.0 CONTRACTS states the template sha256-equal to the repo; it is CRLF 14,419 vs LF 13,920, equal only normalised; a ratified-text fact this seat did not re-measure at signing; to the CTO for an addendum), W10-S3 (the export holds exactly 500,000 rows, possibly a truncation cap).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_BDPRCE-D1-W5-S3, ADVI_BDPRCE-D1-W6-S3, ADVI_BDPRCE-D1-W6-S5, ADVI_BDPRCE-D1-W10-S1, ADVI_BDPRCE-D1-W10-S3"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v2.md (INERT)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S20",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "REMEDIATION_v1 D1-W4-S6 closed REMEDIATED: trace_price_v2 follows the served row (this seat's run: trace2 'followed=canonical trades=4 match=true follows_served=true', selftest OK 7 arms). Round 1's seven ARMED remediations stay OPEN and ARMED: no writer imports R1 yet and nothing served moved. W3-S2 and W4-S1 stay OPEN with causes now named (BP-b-5: Monday/Tuesday header-only exports; account_performance stops at 2026-10-09); W4-S9 stays OPEN (the exemplar's unlisted status is judged by name, W12-S3); W2-S3/W4-S3/W4-S5 stay OPEN for the S33 re-read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W4-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "REMEDIATION_v1 D1-W4-S6 closed REMEDIATED: trace_price_v2 follows the served row (this seat's run: trace2 'followed=canonical trades=4 match=true follows_served=true', selftest OK 7 arms). Round 1's seven ARMED remediations stay OPEN and ARMED: no writer imports R1 yet and nothing served moved. W3-S2 and W4-S1 stay OPEN with causes now named (BP-b-5: Monday/Tuesday header-only exports; account_performance stops at 2026-10-09); W4-S9 stays OPEN (the exemplar's unlisted status is judged by name, W12-S3); W2-S3/W4-S3/W4-S5 stay OPEN for the S33 re-read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~K1/round2/checks/r2_checks.py trace2 and trace_price_v2.py --self-test (3.0.0_SA_CVO)",
        "round2/R2_CLOSE.md @a6e41177d6 sections 4-5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "REMEDIATION_v1 D1-W4-S6 closed REMEDIATED: trace_price_v2 follows the served row (this seat's run: trace2 'followed=canonical trades=4 match=true follows_served=true', selftest OK 7 arms). Round 1's seven ARMED remediations stay OPEN and ARMED: no writer imports R1 yet and nothing served moved. W3-S2 and W4-S1 stay OPEN with causes now named (BP-b-5: Monday/Tuesday header-only exports; account_performance stops at 2026-10-09); W4-S9 stays OPEN (the exemplar's unlisted status is judged by name, W12-S3); W2-S3/W4-S3/W4-S5 stay OPEN for the S33 re-read."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S21",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W8-S1 dismissed: an instrument output detail (followed_source null when neither same-date candidate equals served), recorded in the trace record; trace2 reads follows_served=true on this seat's run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W8-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W8-S1 dismissed: an instrument output detail (followed_source null when neither same-date candidate equals served), recorded in the trace record; trace2 reads follows_served=true on this seat's run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W8-S1",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W8-S1 dismissed: an instrument output detail (followed_source null when neither same-date candidate equals served), recorded in the trace record; trace2 reads follows_served=true on this seat's run."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S22",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W8-S2 dismissed: the --lot-object form reads the date from data_as_of by design; recorded, no defect.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W8-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W8-S2 dismissed: the --lot-object form reads the date from data_as_of by design; recorded, no defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W8-S2",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W8-S2 dismissed: the --lot-object form reads the date from data_as_of by design; recorded, no defect."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S23",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W7-S1 dismissed: the order's mapping-gap test needs an asset_name column historical_prices lacks; the census answered the gap another way (listed_untickered=1).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W7-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W7-S1 dismissed: the order's mapping-gap test needs an asset_name column historical_prices lacks; the census answered the gap another way (listed_untickered=1).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W7-S1",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W7-S1 dismissed: the order's mapping-gap test needs an asset_name column historical_prices lacks; the census answered the gap another way (listed_untickered=1)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S24",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W7-S2 dismissed: acct_z keys hashed to acct_z#<sha12> in committed files: correct client-data handling.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W7-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W7-S2 dismissed: acct_z keys hashed to acct_z#<sha12> in committed files: correct client-data handling.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W7-S2",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W7-S2 dismissed: acct_z keys hashed to acct_z#<sha12> in committed files: correct client-data handling."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S25",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W7-S3 dismissed: the census figure (1,859 of 5,121 off canonical, 36.3%) supersedes round 1's 26-object sample (61 of 586); the hazard is carried by REMEDIATION_v1's ARMED D1-W4-S2, whose census condition this meets in part.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W7-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W7-S3 dismissed: the census figure (1,859 of 5,121 off canonical, 36.3%) supersedes round 1's 26-object sample (61 of 586); the hazard is carried by REMEDIATION_v1's ARMED D1-W4-S2, whose census condition this meets in part.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W7-S3",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W7-S3 dismissed: the census figure (1,859 of 5,121 off canonical, 36.3%) supersedes round 1's 26-object sample (61 of 586); the hazard is carried by REMEDIATION_v1's ARMED D1-W4-S2, whose census condition this meets in part."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S26",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W5-S1 dismissed: R1 gives EXXONMOBIL HOLDINGS 2026-10-09 no price because its only rows that day are Transfer In. This CORRECTS this seat's round-1 row D1-C-S1, which read the 168.94 as 'traced to one trade id': transaction 745369343 is a Transfer In, not a trade. The served value then came from a non-trade row under the pre-R1 rule; round 2's exemplar (BP-b-8) replaced it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W5-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W5-S1 dismissed: R1 gives EXXONMOBIL HOLDINGS 2026-10-09 no price because its only rows that day are Transfer In. This CORRECTS this seat's round-1 row D1-C-S1, which read the 168.94 as 'traced to one trade id': transaction 745369343 is a Transfer In, not a trade. The served value then came from a non-trade row under the pre-R1 rule; round 2's exemplar (BP-b-8) replaced it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W5-S1",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W5-S1 dismissed: R1 gives EXXONMOBIL HOLDINGS 2026-10-09 no price because its only rows that day are Transfer In. This CORRECTS this seat's round-1 row D1-C-S1, which read the 168.94 as 'traced to one trade id': transaction 745369343 is a Transfer In, not a trade. The served value then came from a non-trade row under the pre-R1 rule; round 2's exemplar (BP-b-8) replaced it."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S27",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W5-S2 dismissed: R1 variant A gives BLACKROCK 2026-09-22 no price (no Buy/Sale); variant B's 1074.93 from Dividend Reinvestment is settled by R1 AMENDMENT 1 (reinvestment buys count). Carried in the round-3 re-run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W5-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W5-S2 dismissed: R1 variant A gives BLACKROCK 2026-09-22 no price (no Buy/Sale); variant B's 1074.93 from Dividend Reinvestment is settled by R1 AMENDMENT 1 (reinvestment buys count). Carried in the round-3 re-run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W5-S2",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W5-S2 dismissed: R1 variant A gives BLACKROCK 2026-09-22 no price (no Buy/Sale); variant B's 1074.93 from Dividend Reinvestment is settled by R1 AMENDMENT 1 (reinvestment buys count). Carried in the round-3 re-run."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S28",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W5-S4 dismissed: five Buy rows with no asset_name cannot be priced; counted under no_asset_excluded. A source-data gap recorded in the probe.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W5-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W5-S4 dismissed: five Buy rows with no asset_name cannot be priced; counted under no_asset_excluded. A source-data gap recorded in the probe.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W5-S4",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W5-S4 dismissed: five Buy rows with no asset_name cannot be priced; counted under no_asset_excluded. A source-data gap recorded in the probe."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S29",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W5-S5 dismissed: the probe reads the union of partitions and lets trade_date decide, the correct design for rows landing a day late (W6-S3 carries the general case).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W5-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W5-S5 dismissed: the probe reads the union of partitions and lets trade_date decide, the correct design for rows landing a day late (W6-S3 carries the general case).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W5-S5",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W5-S5 dismissed: the probe reads the union of partitions and lets trade_date decide, the correct design for rows landing a day late (W6-S3 carries the general case)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S30",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W9-S1 dismissed: bd-price-update has no schedule and runs only via bd-silver-merge on the bronze sentinel: the cause chain of W3-S2/W5-S3, recorded there.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W9-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W9-S1 dismissed: bd-price-update has no schedule and runs only via bd-silver-merge on the bronze sentinel: the cause chain of W3-S2/W5-S3, recorded there.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W9-S1",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S1 dismissed: bd-price-update has no schedule and runs only via bd-silver-merge on the bronze sentinel: the cause chain of W3-S2/W5-S3, recorded there."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S31",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W9-S3 dismissed: the detail objects' data_as_of is the input's max date (account_performance stops at 2026-10-09) with no trading-day offset: the CAUSE of REMEDIATION_v1 D1-W4-S1, which stays OPEN until data_as_of reaches T-1 or the lag is stated design.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W9-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W9-S3 dismissed: the detail objects' data_as_of is the input's max date (account_performance stops at 2026-10-09) with no trading-day offset: the CAUSE of REMEDIATION_v1 D1-W4-S1, which stays OPEN until data_as_of reaches T-1 or the lag is stated design.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W9-S3",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S3 dismissed: the detail objects' data_as_of is the input's max date (account_performance stops at 2026-10-09) with no trading-day offset: the CAUSE of REMEDIATION_v1 D1-W4-S1, which stays OPEN until data_as_of reaches T-1 or the lag is stated design."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S32",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W9-S4 dismissed: a comp-rail denial blocking a whole Bash call: a tooling note, not a project hazard.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W9-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W9-S4 dismissed: a comp-rail denial blocking a whole Bash call: a tooling note, not a project hazard.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W9-S4",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S4 dismissed: a comp-rail denial blocking a whole Bash call: a tooling note, not a project hazard."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S33",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W12-S2 dismissed: the private-pool names have no Buy/Sale on 2026-10-09, so the natural private-fund exemplar falls away at R1; the thread moved to a CIT that carries.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W12-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W12-S2 dismissed: the private-pool names have no Buy/Sale on 2026-10-09, so the natural private-fund exemplar falls away at R1; the thread moved to a CIT that carries.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W12-S2",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W12-S2 dismissed: the private-pool names have no Buy/Sale on 2026-10-09, so the natural private-fund exemplar falls away at R1; the thread moved to a CIT that carries."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S34",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W12-S3 dismissed: the no-ticker test also passes public funds, and the dimension's symbol holds CUSIPs; the exemplar's unlisted status is judged by name. Carried to the CTO in the slug for FWD-1's grade; REMEDIATION_v1 D1-W4-S9 stays OPEN on it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W12-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W12-S3 dismissed: the no-ticker test also passes public funds, and the dimension's symbol holds CUSIPs; the exemplar's unlisted status is judged by name. Carried to the CTO in the slug for FWD-1's grade; REMEDIATION_v1 D1-W4-S9 stays OPEN on it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W12-S3",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W12-S3 dismissed: the no-ticker test also passes public funds, and the dimension's symbol holds CUSIPs; the exemplar's unlisted status is judged by name. Carried to the CTO in the slug for FWD-1's grade; REMEDIATION_v1 D1-W4-S9 stays OPEN on it."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S35",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W12-S4 dismissed: trace_price_v2 follows the interpolated canonical row (empty trade_ids) and R1's carry trades come from a separate recompute; carried by ARMED D1-W12-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W12-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W12-S4 dismissed: trace_price_v2 follows the interpolated canonical row (empty trade_ids) and R1's carry trades come from a separate recompute; carried by ARMED D1-W12-S1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W12-S4",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W12-S4 dismissed: trace_price_v2 follows the interpolated canonical row (empty trade_ids) and R1's carry trades come from a separate recompute; carried by ARMED D1-W12-S1."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S36",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W6-S1 dismissed: 212 of 1,657 rows have no R1 trade back to 2020-03-06 (NOT_RECOMPUTABLE in the replay); measured and listed, the served handling is the round-3 list Andrew reads.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W6-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W6-S1 dismissed: 212 of 1,657 rows have no R1 trade back to 2020-03-06 (NOT_RECOMPUTABLE in the replay); measured and listed, the served handling is the round-3 list Andrew reads.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W6-S1",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W6-S1 dismissed: 212 of 1,657 rows have no R1 trade back to 2020-03-06 (NOT_RECOMPUTABLE in the replay); measured and listed, the served handling is the round-3 list Andrew reads."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S37",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:45:00Z",
    "one_line": "D1-W6-S4 dismissed: the canonical window has no carry_forward source, so the estimated-row clause selects linear_interpolation only (18,566 rows): recorded; the hazard is ARMED D1-W12-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W6-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W6-S4 dismissed: the canonical window has no carry_forward source, so the estimated-row clause selects linear_interpolation only (18,566 rows): recorded; the hazard is ARMED D1-W12-S1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W6-S4",
        "round2/R2_CLOSE.md @a6e41177d6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W6-S4 dismissed: the canonical window has no carry_forward source, so the estimated-row clause selects linear_interpolation only (18,566 rows): recorded; the hazard is ARMED D1-W12-S1."
  }
]
```
