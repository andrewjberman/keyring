# IRPT_DASHBD: CVO adjudication, round 118 (workstream B-49F, ~D2)

<sweep_watermark>2026-10-15T05:33Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T05:33Z, on msg 8091 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND118_B_DRAIN_END_20261015.md` @402e68a4a0, blob 86435ae810). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Round 113 of this workstream is already stamped in ADJUDICATION_v73 (packet blob 2ca9a39ff5) and is not re-stamped here. No judgment criterion; all three orders LOCAL. Re-run here on the landed tree: DB118-1-AC1..AC3, DB118-2-AC1, DB118-3-AC1 and AC2, 6 of 6 PASS (rc 0); the three proof instances VALID; `round-close-check --round 118 --workstream B` MAY-CLOSE (3 orders). **The struck criterion DB118-3-AC3, run anyway, FAILS** (rc 1: no `RD_COTTONWOOD_QA_R118.json`): Amendment 2 (@3cc4e81178) removed a bar the round did not meet. Its commit names its gate limb ("none graded: an amendment of the issuer's own order that removes a criterion"). 9 worker rows and 2 issuer disposition rows graded below; 1 ARMED (W185-S8) among them. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S19",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T05:33:00Z",
  "one_line": "Round 118 B-49F (~D2): hop 1's filled_report_values gold (DB-b-230), the flow-guard READ (DB-b-231), the Cottonwood reader (DB-b-232). 6 of 6 live criteria PASS re-run here. The STRUCK DB118-3-AC3, run anyway, FAILS: Amendment 2 removed a failing bar. The amendment names its gate limb (none graded) and its ground holds: zero overlap between the Cottonwood household key and the return table's key, so no QA run could be made, and the reader refused correctly. The Cottonwood QA is deferred, not met. LOCAL confirmed: the filled_report_values gold prefix derived by lib/opal_naming address() for 49 Financial LISTs 0 objects (positive control: the sibling account_return_daily prefix lists 570 lines); the record says s3_writes 0, deployed false, served_values_changed false; the QA parquet is private (sha256 2256d6b5 equals the record). Flow guard: 2026-04-21's 943 GRADED_DISAGREED rows are 941 VALUE, 2 FLOW_AND_VALUE, 0 FLOW (recounted from the gold by the checker). Issuer dispositions graded, not inherited: D2-S56 on W185-S1/S2 GROUNDED (recounted here from the private QA table: act.* 402 of 402 absent, hold.net_gain_* 125 of 125 absent), but the fix (contract 0.5.4) is only promised for the next issuance and no ARMED row holds it, so nothing stops the table being scheduled before it lands; W185-S3's ruling binds ~F2's reader and render to read the 16 avs members by_row, carried only in an ~D2 row ~F2 is not told of; W185-S4, S5 accepted. D2-S62 on W185-S6..S9 GROUNDED: S6 superseded by S9; S7 repaired in the module (AC3 21 tests pass); S8 (ARMED, owner ~D2) DISARMED, test_empty_lot_source_is_absent_not_zero exists (tests/test_filled_report_values.py:285) and passes in AC3's run; S9 a data fact carried to the CTO.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W185-S1",
   "IRPT_DASHBD-D2-W185-S2",
   "IRPT_DASHBD-D2-W185-S3",
   "IRPT_DASHBD-D2-W185-S4",
   "IRPT_DASHBD-D2-W185-S5",
   "IRPT_DASHBD-D2-W185-S6",
   "IRPT_DASHBD-D2-W185-S7",
   "IRPT_DASHBD-D2-W185-S8",
   "IRPT_DASHBD-D2-W185-S9",
   "IRPT_DASHBD-D2-S56",
   "IRPT_DASHBD-D2-S62"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug; an issuer amendment states which gate limb graded it; LOCAL work writes nothing served.",
  "world_is": "Three orders complete (DB-b-231 merged 524ba1f162, DB-b-230 00a48e7d7e, DB-b-232 17e300d554); nothing written to S3 or served. FWD-2, FWD-11, FWD-21 not met. Cottonwood cannot yield a household report: no join key between its household key and its return table (12 accounts at the frontier), and no applied account_dim. Two carried debts sit only in INERT rows: contract 0.5.4 (S56) and ~F2 reading avs by_row (W185-S3). Round numbers collide across IRPT_DASHBD lanes, so a round number alone no longer names a round. Measured from the packet filenames under each COO lane's deliverables folder: 114 under ~I2 (ROUND114_BIN) and ~F2 (L8_PACKET_R114_F); 115 under ~I2 (ROUND115_BIN), ~F2 (L8_PACKET_R115_F) and ~C2 (NEVER_WIDEN_DB-c-5_R115, a sign-off half, not a drain packet); 118 under ~D2 (ROUND118_B) and ~I2 (ROUND118_BIN). Adjudication titles must carry the workstream.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T05:2xZ: DB118-1-AC1..AC3, DB118-2-AC1, DB118-3-AC1, AC2 PASS rc 0; DB118-3-AC3 FAIL rc 1 (no RD_COTTONWOOD_QA_R118.json); proof-of-spec-check VALID rc 0 on all three instances; round-close-check --round 118 --workstream B verdict=MAY-CLOSE orders=3",
    "git show 3cc4e81178 (Amendment 2; 'Gate limb: none graded')",
    "aws s3 ls of s3://opal-data-49financial/irpt/49financial/gold/filled_report_values/ (address() output): 0 objects; positive control account_return_daily/: 570 lines",
    "private QA parquet sha256 2256d6b5... equals RD_FILLED_REPORT_VALUES_R118.json; recount act.* 402/402 absent, hold.net_gain_* 125/125 absent",
    "data/assets/scripts/gold/irpt_reporting/tests/test_filled_report_values.py:285",
    "investigation rows D2-W185-S1..S9, D2-S56, D2-S62",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND118_B_DRAIN_END_20261015.md blob 86435ae810 (msg 8091)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Every worker row is dispositioned by the issuer on grounds this seat re-checked. The one ARMED row is disarmed with a test that exists and passes; the BLOCKING Cottonwood rows are repaired or are data facts carried to the CTO. Two debts are named above for the CTO: the contract 0.5.4 repair and ~F2's by_row read have no ARMED carrier. The struck AC3 is recorded as a failing bar removed, not met."
 }
]
```
