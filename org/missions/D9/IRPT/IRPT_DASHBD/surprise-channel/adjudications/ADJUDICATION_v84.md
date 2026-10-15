# IRPT_DASHBD: CVO adjudication, round 119 (workstream B-49F, ~D2)

<sweep_watermark>2026-10-15T07:21Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T07:21Z, on msg 8174 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND119_B49F_DRAIN_END_20261015.md` @5e65d5d687, blob 8bc3cfe3f1). Not B-IN's round 119, which is ADJUDICATION_v81. Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Four orders (DB-b-233..236), all LOCAL, no judgment criterion. Re-run here on the landed tree: the fourteen criteria of rounds 118 and 119 all PASS (rc 0). The struck DB118-3-AC3, run again, still FAILS (rc 1, no `RD_COTTONWOOD_QA_R118.json`): no round-119 order made the Cottonwood QA runs. All four proof instances VALID; `round-close-check --round 119 --workstream B-49F` MAY-CLOSE (4 orders). 18 rows graded below; 1 ARMED (W189-S1) among them. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S21",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T07:21:00Z",
  "one_line": "Round 119 B-49F (~D2): contract 0.5.4 and the module (DB-b-233), the Commonwealth-to-Black Diamond key map (DB-b-235), the Cottonwood input from Black Diamond (DB-b-234), the 04-21 price read (DB-b-236). 14 of 14 PASS re-run here. DB118-3-AC3 still FAILS: round 119 did not fix what it measured. DB-b-234 gives 25 Cottonwood accounts a return keyed by the Black Diamond key that joins the household frame, but only from 2026-07-10; the gold account_dim is still unapplied and no QA record exists, so the struck bar stays unmet. Disarms graded on their evidence. D2-S68 -> D2-S56 GROUNDED: DB119-1-AC1 re-run here reads all ten pairs equal in every household (234 measured, 67 absent, 0 differing). But D2-S68 calls D2-S56 ARMED; the channel row is INERT, which is why v82 found no ARMED carrier for 0.5.4. The debt was repaired outright, not carried. D2-S68 -> D2-W189-S1 GROUNDED: the row's own disarm text allows 'name the owner who will', and D2-W182-S1 names 0.0.0_AB_MSTR. v82's other debt (~F2 reading avs by_row) now has an ARMED carrier, D2-S64 (CTO ruling 6, owner ~F2). ~F2 disarmed it in D2-S67 with a by_row test on a three-account document; D2-W506-S1 records that a household scalar under an avs member prints as every account's figure and is left unpinned (the contract forbids that input). Worker rows W187-S1..S3, W188-S1..S6, W190-S1, S2 are ruled and repaired inside their orders (checkers patched, pins read through the lineage). W188-S6 (a row on branch commit 538f2db2c8 quoting two client account values): 538f2db2c8 is NOT reachable from HEAD or origin box/dell2; the W188-S3 and S6 rows at HEAD carry 0 money-like tokens and 0 runs of 6+ digits. LOCAL confirmed: all four worker records read s3_writes 0, dynamodb_writes 0, served_values_changed false, deployed false, pushed false; the filled_report_values gold prefix still lists 0 objects. Note: the 04-21 read this round is DB-b-236 (price read); DB-b-233 is the contract repair.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W187-S1",
   "IRPT_DASHBD-D2-W187-S2",
   "IRPT_DASHBD-D2-W187-S3",
   "IRPT_DASHBD-D2-W188-S1",
   "IRPT_DASHBD-D2-W188-S2",
   "IRPT_DASHBD-D2-W188-S3",
   "IRPT_DASHBD-D2-W188-S4",
   "IRPT_DASHBD-D2-W188-S5",
   "IRPT_DASHBD-D2-W188-S6",
   "IRPT_DASHBD-D2-W189-S1",
   "IRPT_DASHBD-D2-W190-S1",
   "IRPT_DASHBD-D2-W190-S2",
   "IRPT_DASHBD-D2-S56",
   "IRPT_DASHBD-D2-S64",
   "IRPT_DASHBD-D2-S67",
   "IRPT_DASHBD-D2-S68",
   "IRPT_DASHBD-D2-W506-S1",
   "IRPT_DASHBD-D2-W185-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug; a disarm is graded on its evidence, not inherited; LOCAL work writes nothing served; the repo holds no client value.",
  "world_is": "Four orders complete (merges 03701893e5, 9d740b6af9, 0fafe5f8c7, ba18aeec39); nothing written to S3 or served. On 2026-04-21 the account value is the outlier: 894 of 929 accounts side with the positions, none with the value. Cottonwood has a derivable return only from 2026-07-10 (33 empty Black Diamond partitions, 04-25 to 07-09); the key map covers 5 of 12 frontier accounts (563 of 1,533 history accounts is a floor). The account return contract has no column for the source label. FWD-2, FWD-11 and FWD-21 are not met. The contaminated object 538f2db2c8 still exists as an unreachable local object until gc; it was never pushed. Round numbers still collide across lanes (v82).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T07:1xZ: DB118-1-AC1..AC3, DB118-2-AC1, DB118-3-AC1, AC2, DB119-1-AC1..AC3, DB119-2-AC1..AC3, DB119-3-AC1, DB119-4-AC1 PASS rc 0; DB118-3-AC3 FAIL rc 1",
    "proof-of-spec-check VALID rc 0 on ~187, ~188, ~189, ~190; round-close-check --round 119 --workstream B-49F verdict=MAY-CLOSE orders=4",
    "git merge-base --is-ancestor 538f2db2c8 HEAD and origin/box/dell2: both false; no branch contains it",
    "worker records RD_ACT_EQUIV_R119, RD_COTTONWOOD_BD_RETURN_R119, RD_KEY_MAP_READ_R119, RD_PRICE_READ_0421_R119: s3_writes 0, served_values_changed false",
    "aws s3 ls s3://opal-data-49financial/irpt/49financial/gold/filled_report_values/: Total Size 0",
    "investigation rows D2-S56 (INERT), D2-S64 (ARMED, owner ~F2), D2-S67, D2-S68, D2-W506-S1, D2-W182-S1",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND119_B49F_DRAIN_END_20261015.md blob 8bc3cfe3f1 (msg 8174)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Every worker row is repaired or ruled inside its order and re-checked green here. The two disarms in D2-S68 hold on their evidence, and the by_row debt was carried and disarmed by its owner with a test. The struck Cottonwood QA bar stays unmet and is named for the CTO; D2-S68's ARMED label for D2-S56 is a misstatement, recorded here, not a hazard."
 }
]
```
