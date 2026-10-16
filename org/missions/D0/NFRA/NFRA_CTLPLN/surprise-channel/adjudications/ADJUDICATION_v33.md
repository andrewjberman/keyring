# NFRA_CTLPLN: CVO L8/L9 at the round-29 close -- FWD-8, FWD-25, FWD-7 graded (2026-10-16)

<sweep_watermark>2026-10-16T16:00Z</sweep_watermark>

L8/L9 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109700 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND29.md`
@1f141a032b). Six tree orders, all complete; no judgment criterion on the orders.

**Result:**
- **FWD-8 REALIZED** (C-S99): from 12:12Z (round 29's issuance) to this read, 74 integrator merges, 0 conflicted. In that
  window the laptop ran round 29 through (12:12Z to 15:4xZ) and dell2 ran IRPT_DASHBD round 132 F-SHIP through (issued
  12:37Z, slugged 15:02Z, analysed 15:04Z). The one-writer call-file layout is live on every box (`LAYOUT` = 2 on HEAD,
  `origin/box/dell1`, `dell2`, `sitez` and `origin/CLOUD`).
- **FWD-25 REALIZED** (C-S100): all eight kinds started and asked what they are (six in round 28; MSTR and WORKER this
  round), and the seat-rules exercise stops a forbidden act for every kind (60 of 60 probes, at least 4 per kind).
- **FWD-7 stays ADVANCED** (C-S101): the CTO's round-28 rulings settle the classes and the placement tool now fails loud,
  but the shared `lambda-source-map.json` is still one file until stage 2 lands. A new reader of it on dell2 appeared after
  the census, so the census no longer reconciles (C-S102, ARMED for the CTO's stage-2 decision).
- Not re-graded (no new act): FWD-11 (C-S90, your choice pending), FWD-4, FWD-12, FWD-22.
- Tally: 13 REALIZED (1, 3, 5, 8, 15, 16, 17, 18, 19, 23, 24, 25, 28), 11 ADVANCED, 0 GATED, 1 PARKED (9), 3 MOVED (13, 20,
  26); denominator 28 (C-S105).
- Rows: 23 round-29 rows dismissed (C-S104); W137-S1 and W137-S3 close in place; W143-S1 ruled (C-S103).

**Criterion re-runs in the main tree (this seat, 15:5xZ):** 12 of 14 pass as the issuer read them (`CROSSBOX-SELFTEST 40/40`,
`CROSSBOX-TEST 76/76`, `APPLY-GATES-TEST 100/100`, `SOURCEMAP-SELFTEST 9/9`, `PLACEMENT-LOUD 7/7`, placement self-test 7/7,
`SEAT-RULES ... probes_pass=60 probes_fail=0 ok=True`, `SEAT-RULES-VALIDATE problems=0`, `SEAT-RULES-TEST 26/26`,
`GRADE-OF-RECORD 8/8`, `GRADE-NOT-A-MENTION 7/7`, `ROUND-CLOSE-SELFTEST 30/30`). **Two read differently now, both from state
that moved after the merge, not from a product defect:**
- `CROSSBOX-SPLIT arms=12/13`: arm (f) compares the base reader with the new one over the LIVE call folder, and the folder
  now holds the first layout-2 call (`XB-20261016T142512Z-6441.json` and its `.dell1.json` answer), which the base reader
  cannot read the same way; `differing=3` (the two lists and that call's status). It passed at the merge, before any layout-2
  call existed. The arm should compare `crossbox/1` files only (C-S104, W-class observation; no fix cut here).
- `SOURCEMAP-CENSUS ... other=1 ok=False`: one file the census does not class,
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p170_filled_reader.py` (line 32 names the map
  path), committed on dell2 after the census (C-S102).
Running two of these criteria rewrote tracked files (the census markdown, and in round 28 the FWD-7 overlap table); this seat
restored both to HEAD. That class is already rows W140-S3, W141-S3 and W144-S4.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S99",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:00Z",
  "one_line": "FWD-8 graded REALIZED: two boxes each ran one full round in parallel (laptop NFRA_CTLPLN round 29, 12:12Z-15:4xZ; dell2 IRPT_DASHBD round 132 F-SHIP, 12:37Z-15:04Z) and box-sync read 74 integrator merges with 0 conflicts over the whole span; the crossbox call file, the only file that conflicted before, now has one writer per box on every box.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-8 DONE WHEN: two boxes working in parallel through one full round each, with no merge conflict on a shared file. ACCEPT: shared lists have one writer. C-S93's missing act: one writer per call file per box, then a window with zero conflicts.",
  "world_is": "python .tools/box-sync-conflicts.py --since 2026-10-16T12:12:00Z at 15:5xZ: merges=74 conflicted_merges=0 paths=0; --since 14:24:00Z (the switch): merges=26 conflicted_merges=0. Round 29 issuance 833181d311 at 12:12:00Z; IRPT_DASHBD round 132 issue 44db9f7b62 12:37:25Z, CVO slug 8d1e88436a 15:02:19Z, CTO analysis 0791af7d64 15:04Z (all on origin). org/devices/crossbox/LAYOUT reads 2 on HEAD and on origin/box/dell1, dell2, sitez and CLOUD (committed 911c4273dc, 14:24:04Z). The first layout-2 call 6441 is two files, XB-...-6441.json (laptop) and XB-...-6441.dell1.json (dell1). The span from 12:12Z to 14:24Z ran on layout 1 and also read zero conflicts; the mechanism that keeps it at zero is the layout-2 one-writer rule.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python .tools/box-sync-conflicts.py --since 2026-10-16T12:12:00Z and --since 2026-10-16T14:24:00Z, 2026-10-16T15:5xZ",
    "git show <ref>:org/devices/crossbox/LAYOUT for HEAD, origin/box/dell1, origin/box/dell2, origin/box/sitez, origin/CLOUD",
    "git log origin/CLOUD --grep 'IRPT_DASHBD round 132' (issue 44db9f7b62, slug 8d1e88436a)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S100",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:00Z",
  "one_line": "FWD-25 graded REALIZED: one seat of each of the eight kinds was started and asked what it is (CTO, COO, CVO, CRO, CLOUDOPS, TIER2 in round 28; MSTR and WORKER this round), and the seat-rules exercise tries a forbidden act under each kind and a tool stops it: 60 of 60 probes, every kind covered.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-25 DONE WHEN: one seat of each kind started on a box and asked what it is, and one forbidden act per kind tried and stopped or flagged by a tool. ACCEPT: across how code moves, how cloud changes are made, and how seats work.",
  "world_is": "Seat start: FWD25_SEAT_START_ANSWERS_20261016.md (0.0.0_AB_MSTR; six kinds, plus 0.0.0_AB_MSTR~FW answering at line 80) and FWD25_WORKER_KIND_ANSWER_20261016.md (a worker subagent, 0 tool calls, naming what it is and is not). Forbidden acts: python .tools/seat-rules-check.py exercise at 15:5xZ: rules=47 pairs_covered=24/24 probes_pass=60 probes_fail=0 probes_unread=0 ok=True; by serial kind MSTR 9, CTO 11, COO 5, CVO 7, CRO 5, CLOUDOPS 4, TIER2 5, WORKER 5 (9 more carry no serial); the three domains GITOPS, AWSDEVOPS and WORKFLOW each appear (for example a rebase on CLOUD denied by the PreToolUse hook; an apply by any non-CloudOps kind REFUSED by APPLY-WHO; MSTR's tier-2 write denied). Limits, stated: a probe drives the gate under the kind's serial, not the started seat making the attempt itself; the MSTR lane was started with its loops banned in the hint; needs_andrew=2 rows remain his.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python .tools/seat-rules-check.py exercise, 2026-10-16T15:5xZ (probe lines counted by serial prefix)",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.0.0_AB_MSTR/FWD25_SEAT_START_ANSWERS_20261016.md",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/FWD25_WORKER_KIND_ANSWER_20261016.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S101",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:00Z",
  "one_line": "FWD-7 graded ADVANCED: the CTO ruled the classes (directory-prefix is NOT-SAME-FILE; record-terraform-deploy.sh has one owner, 0.7.0_AE_CloudOps; lambda-source-map.json is not a carrier and splits per function) and the placement tool now fails loud, but the map is still one file written by projects on three boxes until stage 2 lands.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-7 ACCEPT: two projects on different boxes change different files.",
  "world_is": "PLACEMENT-LOUD 7/7 and the placement self-test 7/7 here. The map split is stage 2 (PROPOSED_LAYOUT_AND_MIGRATION.md, the CTO's decision, packet section 6). The record-terraform-deploy.sh owner ruling's effect on the placement read was not re-read here.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python .tools/tests/test_round29_placement_loud.py and python .tools/placement-check.py --self-test, 2026-10-16T15:5xZ",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND29.md sections 4 and 6"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard; stage 2 is the CTO's decision."
 },
 {
  "id": "NFRA_CTLPLN-C-S102",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:00Z",
  "one_line": "The lambda-source-map consumer census no longer reconciles: a reader committed on dell2 after the census (IRPT_DASHBD r149 p170_filled_reader.py) names the map path in a shape the census does not class, so SOURCEMAP-CENSUS reads other=1 ok=False; a stage-2 split cut on the round-29 census would miss it.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO",
  "spec_asserts": "The census is the list of every consumer the stage-2 split must move (CT-bb-1; W140-S2: four live readers degrade silently when the map is absent). Disarms when the stage-2 migration cell re-runs the census at its cut and reads other=0 ok=True, with every reader it names moved in the same commit.",
  "world_is": "python .../0.9.0_WK_NFRA_CTLPLN~140/source_map_census.py at 15:5xZ: files=2534 grep_files=2534 reconciled=True map_functions=240 classes=read_whole:175,read_one:0,write:6,test:21,doc:2331,other:1 ok=False; the OTHER file is org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p170_filled_reader.py, line 32 SOURCE_MAP = \"infra/aws/lambda/ci/lambda-source-map.json\". At the merge the census read 2528 files, other=0. The run rewrote the tracked census markdown; this seat restored it to HEAD.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/source_map_census.py, 2026-10-16T15:5xZ (the diff of LAMBDA_SOURCE_MAP_CONSUMER_CENSUS.md it wrote, then restored)"
   ]
  },
  "disposition": "UNDER_INVESTIGATION"
 },
 {
  "id": "NFRA_CTLPLN-C-S103",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:00Z",
  "one_line": "Ruling on W143-S1 (owed to this seat): a NOT MET grade of record is a grade, so round-close-check is right to count it in graded=; what is missing is that the count hides it. The ROUND-CLOSE line should also print not_met=<n>, so a MAY-CLOSE with a failed judgment criterion cannot read as clean. The verdict rule is unchanged: the CTO's analysis answers a NOT MET.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W143-S1"
  ],
  "spec_asserts": "Spine L9: judgment criteria are graded at L9 and never self-graded; L10 goes to the CTO after every order is terminal, and the CTO answers with an addendum or a recut.",
  "world_is": "W143-S1: round-close-check reads a grade of record of NOT MET as GRADED; the verdict is set only by ungraded and self-graded counts. A NOT MET grade still reaches the CTO in the CVO's slug and adjudication, so nothing is lost today; the risk is a reader of the one ROUND-CLOSE line alone.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md row NFRA_CTLPLN-W143-S1",
    "python .tools/round-close-check.py --selftest -> 30/30, 2026-10-16T15:5xZ"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Ruled: counting is correct; the not_met field is an enrichment candidate for the CTO's list, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S104",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:00Z",
  "one_line": "Round-29 rows W139-S1..S4, W140-S1..S5, W141-S1..S3, W142-S1..S4, W143-S2 and W144-S1..S5 dismissed with reason; W137-S1 closes on CT-bc-1 (the placement tool fails loud) and W137-S3 on the CTO's round-28 ruling (directory-prefix is NOT-SAME-FILE); CROSSBOX-SPLIT arm (f) ages with the live call folder.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W137-S1",
   "NFRA_CTLPLN-W137-S3",
   "NFRA_CTLPLN-W139-S1",
   "NFRA_CTLPLN-W139-S2",
   "NFRA_CTLPLN-W139-S3",
   "NFRA_CTLPLN-W139-S4",
   "NFRA_CTLPLN-W140-S1",
   "NFRA_CTLPLN-W140-S2",
   "NFRA_CTLPLN-W140-S3",
   "NFRA_CTLPLN-W140-S4",
   "NFRA_CTLPLN-W140-S5",
   "NFRA_CTLPLN-W141-S1",
   "NFRA_CTLPLN-W141-S2",
   "NFRA_CTLPLN-W141-S3",
   "NFRA_CTLPLN-W142-S1",
   "NFRA_CTLPLN-W142-S2",
   "NFRA_CTLPLN-W142-S3",
   "NFRA_CTLPLN-W142-S4",
   "NFRA_CTLPLN-W143-S2",
   "NFRA_CTLPLN-W144-S1",
   "NFRA_CTLPLN-W144-S2",
   "NFRA_CTLPLN-W144-S3",
   "NFRA_CTLPLN-W144-S4",
   "NFRA_CTLPLN-W144-S5"
  ],
  "spec_asserts": "Every row a round mints is dispositioned before its L10; an ARMED row closes on its done-when or its owner's ruling.",
  "world_is": "All 23 round-29 rows are INERT. W139-S1, W142-S4: the base crossbox suite was red; 76/76 here. W139-S2, W141-S2, W142-S2, W143-S2: sparse-tree readings; this seat's reads are in the main tree. W139-S3, W139-S4: a fixture gap (repaired, APPLY-GATES 100/100 here) and a stale comment outside the cell. W140-S1..S5: map facts the stage-2 decision reads (C-S102 adds the missed reader); W140-S2 and W140-S4 bear on stage 2. W141-S1, W141-S3, W144-S4: criteria that rewrite tracked files (seen here too, restored). W142-S1, W142-S3: the order's assumptions, ruled in its amendments. W144-S1..S3 (BLOCKING, INERT): the two withdrawn grade rules; the final rule's sweep changed no reading (GRADE-NOT-A-MENTION 7/7 here). W144-S5: five source-only changes at equal dates, recorded. W137-S1: PLACEMENT-LOUD 7/7 (a missing org/missions now exits 3). W137-S3: closed by the CTO's ruling. Arm (f) of test_round29_crossbox_split.py reads the live folder and fails once a layout-2 call exists (differing=3 here); it should compare crossbox/1 files only.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "the criterion re-runs in this record's header, 2026-10-16T15:5xZ",
    "python .tools/tests/test_round29_crossbox_split.py (arm f detail) and the schema read of every org/devices/crossbox/*.json (2 files not crossbox/1)",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND29.md sections 4 and 5"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Each row is resolved in the round, ruled, or a recorded state; the arm-(f) aging and the tracked-file rewrites are enrichment candidates."
 },
 {
  "id": "NFRA_CTLPLN-C-S105",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:00Z",
  "one_line": "FWD delta after round 29: 11 -> 13 REALIZED (FWD-8, FWD-25), 13 -> 11 ADVANCED, 0 GATED, 1 PARKED, 3 MOVED; denominator 28.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 DONE WHEN and ACCEPT per outcome.",
  "world_is": "C-S99 to C-S101. FWD-11 waits on the CTO's choice (C-S90). FWD-4, FWD-12 and FWD-22 were not re-read this round.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this record's C-S99 to C-S101",
    "adjudications/ADJUDICATION_v32.md C-S98 (the table entering the round)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade delta, not a hazard."
 }
]
```
