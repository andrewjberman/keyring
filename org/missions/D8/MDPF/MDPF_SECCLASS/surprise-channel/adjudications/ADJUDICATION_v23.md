# MDPF_SECCLASS -- round 24 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-14T12:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T12:20:00Z. L8 packet: 2.0.0_SA_COO~M1 msg 5504, `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R24_20261014.md` @d4286aab30 (blob a94611849e56, verified).
18 orders, 14 complete (proof_ok 14), e57e61 held outside the verdict. round-close-check --round 24: MAY-CLOSE.

**L9:** FWD-1's Black Diamond half REALIZED on live served pages, on the class-path reading stated in D1-C-S21. FWD-2..17 not re-graded.

**L10:** precondition met (D1-C-S24). **Rows:** 22 of 22 since v22's watermark: 2 graduated, 20 dismissed; this seat's D1-S39 graduated. D1-W83-S5's clock closed in REMEDIATION_v12.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S21",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T12:20:00Z",
    "one_line": "ROUND 24 L9: FWD-1 Black Diamond half REALIZED -- on live served pages GLD and PHYS read commodities and VXX structured/Hedge, every class from etf-classifications, 0 unclassified on the three client pages; round 19's 23 placeable securities are placed (residue 4 tickers the list has no row for).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_SECCLASS PRD FWD-1 (lines 27-35): DONE WHEN 'one live run of the Black Diamond chain for the latest day, traced from the shared list to the page the advisor reads'; ACCEPT 'for a real Black Diamond client, gold funds such as GLD and PHYS read as commodities and VXX reads as a hedge, the same as Positioning shows them; the trace shows every class on that page came from the one shared list, and the old Black Diamond copy of the list was never consulted at any step'. Re-read condition: CTO round-19 analysis 'When item 1's leg G reads MET and item 2 has named its cause, FWD-1's Black Diamond half is read again for REALIZED.'",
    "world_is": "ROUND 24 L9, FWD-1 BLACK DIAMOND HALF: REALIZED, on this seat's reads 2026-10-14 ~11:55Z-12:15Z. Packet @d4286aab30 (blob a94611849e56, verified). The re-read condition holds: e91 leg G closed MET 10-13 (packet); D1-S27's cause is named (share rounding; its acceptability stays open with 1.0.0_SA_CTO~DELL1). THE LIVE RUN: the 10-13 23:00Z and 10-14 04:00Z fires wrote the served client pages at 05:47Z-05:48Z; composition data_as_of 2026-10-09, the latest holdings_lots partition (gold/timeseries/holdings_lots/2026-10-09.parquet, VersionId FeCuiFKCthXAItpjYR.6AL8GFdo8uf_3). THE CODE ON THE PATH: e97_shipped_check E97-SHIPPED ok=True (C_06 f847d8d1, D_04 43a5d613 equal the repo); sc_r20_served_reach D_04, D_03 and C_06 each ok=True controls 3/3; the served lib/etf_classifier.py equals 20150348a5 by content (md5 e714dc50; HEAD differs only by DB-b-181, row D1-S39) and lib/_shared/etf_classifications_dynamodb.py equals the repo (md5 4cc11d3e); the classifier opens etf-classifications only. REAL CLIENTS (the largest open holder of each ticker in the lots): z08373330 GLD commodities/Metals; z0893406 PHYS commodities/Metals; z08327149 VXX structured/Hedge -- each with class_source etf-classifications, equal to the shared list's own row (VXX get-item: structured / Hedge). Every top holding on the three pages reads class_source etf-classifications (16, 15 and 22 of 16, 15, 22), unclassified count 0 on each. 'Reads as a hedge' is met as sub-class Hedge under class structured, which is how the one list holds VXX. 'The same as Positioning': PRD line 236 states the two Positioning surfaces read the same etf-classifications table; this seat did not render Positioning. ROUND 19's DEFECT: re-running the served classifier bytes over all 3,760 open securities of the 10-09 lots against the live list: 3,690 placed by etf-classifications, 69 non-cash unclassified for $2,693,553.95 (the served composition counts 65 for $2,686,197.19; the $7,357 gap is this seat's finer ticker+name+cusip grouping). Of the 69, only 4 carry a ticker (HPI, CUBE, GLPI, PCEF; $63,967.82) and the list has no ticker, NAME:: or CUSIP row for them -- unclassified by right, against round 19's 23 placeable securities ($966,285). STATED READING: 'never consulted at any step' is read on the class path the trace walks. The BD chain still runs B_01b (writes new securities into bd-securities) and E_18 (reads it); neither puts a class on any page. Their retirement is FWD-4/FWD-5's open work. If the CTO reads 'any step' as any step of the chain run, this grade is NOT REALIZED until FWD-5.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python R23_CHECKS/e97_shipped_check.py: E97-SHIPPED ok=True",
        "3.0.0_SA_CVO python R20_CHECKS/sc_r20_served_reach.py D_04 | D_03 | C_06: ok=True controls=3/3 each",
        "3.0.0_SA_CVO s3api get-object opal-data-49financial advi/49financial/platinum/clients/{z08327149,z08373330,z0893406}/composition.json (LastModified 2026-10-14T05:47:54Z-05:48:02Z)",
        "3.0.0_SA_CVO dynamodb get-item etf-classifications VXX: structured / Hedge",
        "3.0.0_SA_CVO served-bytes classifier (lib/etf_classifier.py VersionId 0jhXHH7axm_H934t5s5gVDVNJ6Y_WqI., _shared VersionId uV1e3F_RKieARDaz9M7bq3qMYLRwgLG2) over the 10-09 lots: 3,760 securities, 69 unclassified $2,693,553.95",
        "3.0.0_SA_CVO s3api get-object platinum/firm/mix_summary.json VersionId FlO7ql.PVFj4mwe4aUpA3KIcRgy9dZPR: composition unclassified count 65, $2,686,197.19",
        "git grep bd-securities over data/black_diamond/scripts/gold/: D_03, D_04, C_06 0 hits; B_01b, E_18 use it"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record: FWD-1's Black Diamond half REALIZED on the class-path reading, stated."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S22",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T12:20:00Z",
    "one_line": "GRADUATED to REMEDIATION_v14: D1-S36 (ARMED, re-base in round 25), D1-S37 (C_06 key order, sorted-keys change unbuilt), D1-S39 (undeployed DB-b-181 rides the next BD lib deploy).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-S36",
      "MDPF_SECCLASS-D1-S37",
      "MDPF_SECCLASS-D1-S39"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED to REMEDIATION_v14: D1-S36 (ARMED: the e97 bars and advisors clauses fail against the Oct-12 baselines because an AUA restatement landed before the fire; CTO call 1108 re-bases them as a class in round 25) -> 1.0.0_SA_CTO~DELL1. D1-S37 (INERT: C_06 writes mix_daily_summary.json byte-nondeterministically with identical content; DELTA=0 read as canonical-JSON equality by XA-a304; the sorted-keys change is not built) -> 2.0.0_SA_COO~M1 under its own never-widen pair. D1-S39 (INERT: the undeployed DB-b-181 classifier change rides the next BD gold lib deploy) -> 2.0.0_SA_COO~M1: any pair that ships code/gold/lib/ names DB-b-181's radius, or the deploy pins the served classifier.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_SECCLASS-D1-S36, MDPF_SECCLASS-D1-S37, MDPF_SECCLASS-D1-S39",
        "packet sections 'Leg Q' and 'Not shown'"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S23",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T12:20:00Z",
    "one_line": "DISMISSED 20 round-24 rows (2 BLOCKING resolved in the round, the rest instrument and criterion notes), each with its own reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W88-S1",
      "MDPF_SECCLASS-D1-W88-S2",
      "MDPF_SECCLASS-D1-W88-S3",
      "MDPF_SECCLASS-D1-W88-S4",
      "MDPF_SECCLASS-D1-W88-S5",
      "MDPF_SECCLASS-D1-W88-S6",
      "MDPF_SECCLASS-D1-W88-S7",
      "MDPF_SECCLASS-D1-S33",
      "MDPF_SECCLASS-D1-W89-S1",
      "MDPF_SECCLASS-D1-W89-S2",
      "MDPF_SECCLASS-D1-W89-S3",
      "MDPF_SECCLASS-D1-W89-S4",
      "MDPF_SECCLASS-D1-W89-S5",
      "MDPF_SECCLASS-D1-W89-S6",
      "MDPF_SECCLASS-D1-W89-S7",
      "MDPF_SECCLASS-D1-W90-S1",
      "MDPF_SECCLASS-D1-W90-S2",
      "MDPF_SECCLASS-D1-S34",
      "MDPF_SECCLASS-D1-S35",
      "MDPF_SECCLASS-D1-S38"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "DISMISSED, 20 rows: D1-W88-S1: Instrument choice inside the criterion's own dates; TO-SC-e99 completed under amendment 2. D1-W88-S2: BLOCKING, resolved: amendment 2 (@c68cb7c25a) re-stated in_range; TO-SC-e99 complete, proof OK. D1-W88-S3: Criterion-vs-would-be note; the served key was graded as the instrument reads it. D1-W88-S4: Scope note on bars.json; the graded figures are the committed ones. D1-W88-S5: Instrument scope (a broad prefix); the e91 read was narrowed; no served defect. D1-W88-S6: The e91 fall vs bound question; e91 leg G closed MET 10-13 (packet), and the e97 re-derive governs the window. D1-W88-S7: Negative-control magnitude; the selftest uses tolerance + $1. D1-S33: The eight unnamed dates were re-derived by the e97 rolling re-derive (restated_through present); D1-S36 carries the remaining baseline question. D1-W89-S1: Negative control moved to bound + $251; selftest passes. D1-W89-S2: Reading question with no live divergence at this fire. D1-W89-S3: Measured: bare e91 on the canonical default needs --fire-start (this seat saw the same line). D1-W89-S4: Temp-file read method; read-only. D1-W89-S5: Print-volume choice; not a defect. D1-W89-S6: Denominators differ by destination as measured; no effect on the expectation. D1-W89-S7: Proof path follows the serial; the ~89 instance is the graded one. D1-W90-S1: BLOCKING ARMED, resolved: the issuer's amendment changed the sibling test to the CTO's ruling; this seat ran test_holdings_snapshot.py at HEAD: 30 passed. D1-W90-S2: Stale docstring premise; the issuer's call inside its grant. D1-S34: The record of D1-W90-S1's resolution. D1-S35: Corrected by its author in D1-S36. D1-S38: The record of D1-W83-S5's disarm; REMEDIATION_v12's clock closed here.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the investigation rows named",
        "3.0.0_SA_CVO pytest data/assets/scripts/gold/investor_reporting/tests/test_holdings_snapshot.py: 30 passed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "DISMISSED, 20 rows: D1-W88-S1: Instrument choice inside the criterion's own dates; TO-SC-e99 completed under amendment 2. D1-W88-S2: BLOCKING, resolved: amendment 2 (@c68cb7c25a) re-stated in_range; TO-SC-e99 complete, proof OK. D1-W88-S3: Criterion-vs-would-be note; the served key was graded as the instrument reads it. D1-W88-S4: Scope note on bars.json; the graded figures are the committed ones. D1-W88-S5: Instrument scope (a broad prefix); the e91 read was narrowed; no served defect. D1-W88-S6: The e91 fall vs bound question; e91 leg G closed MET 10-13 (packet), and the e97 re-derive governs the window. D1-W88-S7: Negative-control magnitude; the selftest uses tolerance + $1. D1-S33: The eight unnamed dates were re-derived by the e97 rolling re-derive (restated_through present); D1-S36 carries the remaining baseline question. D1-W89-S1: Negative control moved to bound + $251; selftest passes. D1-W89-S2: Reading question with no live divergence at this fire. D1-W89-S3: Measured: bare e91 on the canonical default needs --fire-start (this seat saw the same line). D1-W89-S4: Temp-file read method; read-only. D1-W89-S5: Print-volume choice; not a defect. D1-W89-S6: Denominators differ by destination as measured; no effect on the expectation. D1-W89-S7: Proof path follows the serial; the ~89 instance is the graded one. D1-W90-S1: BLOCKING ARMED, resolved: the issuer's amendment changed the sibling test to the CTO's ruling; this seat ran test_holdings_snapshot.py at HEAD: 30 passed. D1-W90-S2: Stale docstring premise; the issuer's call inside its grant. D1-S34: The record of D1-W90-S1's resolution. D1-S35: Corrected by its author in D1-S36. D1-S38: The record of D1-W83-S5's disarm; REMEDIATION_v12's clock closed here."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S24",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T12:20:00Z",
    "one_line": "L10 PRECONDITION MET: round 24 MAY-CLOSE (14 of 14 complete with proofs, e57e61 held); 22 of 22 rows since the watermark dispositioned; D1-W83-S5 clock closed; FWD-1 BD half REALIZED; FWD-2..17 not re-graded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W83-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L10 PRECONDITION MET. round-close-check --project MDPF_SECCLASS --round 24 on this seat: orders=18, 14 complete, proof_ok 14, TO-DEPLOY-e57e61 outside the verdict on its stated hold (the L3 read waits on a scheduled run that plans US stocks), verdict MAY-CLOSE. Every investigation row after ADJUDICATION_v22's watermark (2026-10-12T14:05Z) is dispositioned: 22 of 22 (C-S22 graduates 2, C-S23 dismisses 20), plus this seat's D1-S39 (graduated). Remediation clock closed: D1-W83-S5 (REMEDIATION_v12) DISARMED on XA-a304 and REMEDIATED by the shipped rolling re-derive. Kept open: D1-S27 (v10, the ~$128 share-rounding acceptability, 1.0.0_SA_CTO~DELL1), D1-W78-S1 (v11, cause untraced). THE BOARD: FWD-1's Black Diamond half REALIZED (C-S21). FWD-2 to FWD-17 are not re-graded by this seat: the packet prints each as its last recorded word, all older than round 20, none REALIZED, and this seat ran nothing that moves them. Note for FWD-2/13: SC-e-100 restored multi_asset in the frozen v1 HoldingsSnapshot copies, the same schema family as W38-S6; not read here.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/round-close-check.py --project MDPF_SECCLASS --round 24: MAY-CLOSE",
        "this file's rows C-S21..C-S23",
        "remediations/REMEDIATION_v12.md D1-W83-S5 clock"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The L10 record."
  }
]
```
