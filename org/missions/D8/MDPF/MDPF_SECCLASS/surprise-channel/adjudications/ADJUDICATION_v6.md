# MDPF_SECCLASS -- rounds 6-8 L8/L9 adjudication

<sweep_watermark>2026-10-07T09:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-07 ~09:5xZ. L8 packet: 2.0.0_SA_COO~M1 drain-end
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/2.0.0_SA_COO~M1/DRAIN_END_R8_20261007.md` @572829ce3b (branch `coo-m1-secclass-r8`),
asked by 1.0.0_SA_CTO~DELL1 msg 108. Swept: every row of `investigations/INVESTIGATION_v1.md` after ADJUDICATION_v5's watermark
(2026-10-02T02:10Z) = 93 rows, S9 through W25-S6. Each row was read against the artifact it names (git bytes at this branch head,
read-only S3/DynamoDB/Lambda reads from dell1; the firm buckets deny this box, and the rows that needed them rest on their ledgers).
47 are dismissed by the rows below; 46 graduate in `remediations/REMEDIATION_v6.md`, with one new row C-S13. All 9 BLOCKING rows
of the window (S9, S13, S18, S19, S23, S34, W23-S4, W24-S5, W24-S8) are dismissed on a read that shows them resolved; 0 BLOCKING
remain open. Open ARMED after this compile: S46, S49 (new), and S2, W6-S2, S7 (carried, not re-read).

Packet corrections: W10-S1, W10-S5 and W12-S1, which the packet lists as armed with a dark owner, were closed DISARMED in
REMEDIATION_v4. The order files of TO-SC-e21, e35, e36 and e37 read `<status>issued` at this branch head while the packet calls
them complete; e29 is not started. The slug waits until every order of round 8 reads a terminal status.

L9: no swept order carries a JUDGMENT criterion. Trading-calendar hold (laptop CTO msg 106079): nothing here is dated before 2024.

```json
[
  {
    "id": "MDPF_SECCLASS-C-S14",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S9 (BLOCKING/ARMED) dismissed: Disarmed by S12 (the r3 rollback, ledger CLOSED); the r4 re-land (ledger secclass-bd-thread-r4-reland-m-20261002, CLOSED 2026-10-05) superseded r3, and the served 49F mix no longer drops a quarter of the firm.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S9"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Disarmed by S12 (the r3 rollback, ledger CLOSED); the r4 re-land (ledger secclass-bd-thread-r4-reland-m-20261002, CLOSED 2026-10-05) superseded r3, and the served 49F mix no longer drops a quarter of the firm.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ledger 20261002T0618Z_secclass-bd-thread-r3-rollback-m-20261002: Status CLOSED -- nothing stranded -- 20261002T083722Z; legs P/C read back the four keys to the prior VersionIds",
        "s3api get-object opal-data-bd platinum/firm/mix_summary.json (VersionId kg7oxej6.., LM 2026-10-07T05:49:01Z): data_as_of 2026-10-05, 8 classes, equity 0.7208, fixed_income 0.1894, alternatives 0.0008; MV sum 2,001,258,931.56 -- not the 75.8 pct / three-class shape S9 recorded",
        "investigation row MDPF_SECCLASS-S9 (3.0.0_SA_CVO)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by S12 (the r3 rollback, ledger CLOSED); the r4 re-land (ledger secclass-bd-thread-r4-reland-m-20261002, CLOSED 2026-10-05) superseded r3, and the served 49F mix no longer drops a quarter of the firm."
  },
  {
    "id": "MDPF_SECCLASS-C-S15",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S10 (OBSERVATION/INERT) dismissed: S10 is one instance of the class S14 measures (274 tickers on more than one CUSIP); it is carried by the graduated S14 row, whose close condition covers GLDM's 60,873.45 USD of the gold-miners fund.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S10 is one instance of the class S14 measures (274 tickers on more than one CUSIP); it is carried by the graduated S14 row, whose close condition covers GLDM's 60,873.45 USD of the gold-miners fund.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "dynamodb get-item etf-classifications GLDM (ConsistentRead): commodities / Metals, classified_by seed -- the ticker-keyed row S10 describes is unchanged",
        "investigation row MDPF_SECCLASS-S10 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S10 is one instance of the class S14 measures (274 tickers on more than one CUSIP); it is carried by the graduated S14 row, whose close condition covers GLDM's 60,873.45 USD of the gold-miners fund."
  },
  {
    "id": "MDPF_SECCLASS-C-S16",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S12 (OBSERVATION/INERT) dismissed: A disarm record for S9; its claim (rollback closed, nothing stranded) reads true in the ledger. Dismissed as the resolving row of S9.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S12"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "A disarm record for S9; its claim (rollback closed, nothing stranded) reads true in the ledger. Dismissed as the resolving row of S9.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ledger 20261002T0618Z_secclass-bd-thread-r3-rollback-m-20261002: CLOSED 20261002T083722Z, leg C copy-object of the prior VersionId on each of the four keys with ETag read-back",
        "investigation row MDPF_SECCLASS-S12 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record for S9; its claim (rollback closed, nothing stranded) reads true in the ledger. Dismissed as the resolving row of S9."
  },
  {
    "id": "MDPF_SECCLASS-C-S17",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S13 (BLOCKING/ARMED) dismissed: The repo-vs-served split S13 names is closed: the r4 re-land released the held lines under SERVE-RELEASE-ACK and the served code now equals HEAD byte for byte.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S13"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The repo-vs-served split S13 names is closed: the r4 re-land released the held lines under SERVE-RELEASE-ACK and the served code now equals HEAD byte for byte.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "md5 of HEAD bytes vs s3api head-object ETag on opal-data-bd code/gold/: C_06.client_mix_timeseries.py 0095fc95 = 0095fc95; D_03.composition_artifacts.py 84f9bf8e = 84f9bf8e; D_04.client_portal_summary.py 816a77e9 = 816a77e9; DEPLOY-SERVE-HELD count 0 in each",
        "ledger 20261002T1358Z_secclass-bd-thread-r4-reland-m-20261002: CLOSED 20261005T015653Z; leg M is the SERVE-RELEASE-ACK commit removing the four DEPLOY-SERVE-HELD lines",
        "investigation row MDPF_SECCLASS-S13 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The repo-vs-served split S13 names is closed: the r4 re-land released the held lines under SERVE-RELEASE-ACK and the served code now equals HEAD byte for byte."
  },
  {
    "id": "MDPF_SECCLASS-C-S18",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S16 (OBSERVATION/INERT) dismissed: The COO's dismissal stands: the byte change moved nothing Black Diamond gold computes. Its lesson (name the CODE_TREES shipped artifacts in every gold half) is confirmed by the 10-07 push re-shipping all three.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S16"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The COO's dismissal stands: the byte change moved nothing Black Diamond gold computes. Its lesson (name the CODE_TREES shipped artifacts in every gold half) is confirmed by the 10-07 push re-shipping all three.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api head-object opal-data-bd code/gold/lib/_shared/{etf_classifications_dynamodb,etf_classification_scheduled,etf_classification}.py: ETags 4cc11d3e / cfe898d1 / 05c924d5 equal HEAD md5, all LastModified 2026-10-07T04:15Z -- the shared artifacts move again with each gold push, as the row says",
        "investigation row MDPF_SECCLASS-S16 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The COO's dismissal stands: the byte change moved nothing Black Diamond gold computes. Its lesson (name the CODE_TREES shipped artifacts in every gold half) is confirmed by the 10-07 push re-shipping all three."
  },
  {
    "id": "MDPF_SECCLASS-C-S19",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S17 (OBSERVATION/INERT) dismissed: Superseded by Andrew's ruling: there is no multi_asset class, the table holds zero such rows, so a renderer missing from the multi_asset reader census can never meet one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S17"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Superseded by Andrew's ruling: there is no multi_asset class, the table holds zero such rows, so a renderer missing from the multi_asset reader census can never meet one.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "dynamodb scan etf-classifications (CLI auto-paginated, no LastEvaluatedKey): 3,507 rows; asset_class equity 2,785, fixed_income 679, structured 20, commodities 12, alternatives 11; multi_asset 0",
        "git log: c4dd01424a records Andrew-direct ~00:4xZ 10-07 'no multi-asset class, six classes only'; 0d9457b639 rule-B remap wrote 33 of 33 multi_asset rows to equity/fixed_income",
        "investigation row MDPF_SECCLASS-S17 (3.0.0_SA_CVO)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Superseded by Andrew's ruling: there is no multi_asset class, the table holds zero such rows, so a renderer missing from the multi_asset reader census can never meet one."
  },
  {
    "id": "MDPF_SECCLASS-C-S20",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S18 (BLOCKING/ARMED) dismissed: Restored (ledger closed) and fixed at the cause: the class cell is live and the served 10-01 cube now carries the accounts S18 saw dropped.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S18"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Restored (ledger closed) and fixed at the cause: the class cell is live and the served 10-01 cube now carries the accounts S18 saw dropped.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3 get-object + pandas, opal-data-bd gold/positions_cube: 2026-09-30 7,189 accounts, 2026-10-01 7,195, 2026-10-05 7,208 (all rewritten 2026-10-07T04:14Z) -- no drop of hundreds of accounts at 10-01",
        "13d0277249 (S18 class cell) is an ancestor of HEAD; code/gold/A_03.positions_cube.py ETag 4baf5de3 = HEAD md5, LastModified 2026-10-03T21:23Z",
        "ledger 20261003T0715Z_secclass-s18-restore-0930-m-20261003: CLOSED 20261003T124534Z",
        "investigation row MDPF_SECCLASS-S18 (3.0.0_SA_CVO)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Restored (ledger closed) and fixed at the cause: the class cell is live and the served 10-01 cube now carries the accounts S18 saw dropped."
  },
  {
    "id": "MDPF_SECCLASS-C-S21",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S19 (BLOCKING/INERT) dismissed: The mechanism S19 diagnoses (end date follows a partial delivery; the weekly-allocation confirmation is a no-op) is bypassed by the live S18 class cell; the BLOCKING condition no longer holds on the served cube.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S19"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The mechanism S19 diagnoses (end date follows a partial delivery; the weekly-allocation confirmation is a no-op) is bypassed by the live S18 class cell; the BLOCKING condition no longer holds on the served cube.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "same reads as S18: A_03 served = HEAD (4baf5de3) carrying 13d0277249, which keys carry-forward on dimension-open AND held on the reference day rather than the weekly allocation confirmation; served cube 10-01 7,195 accounts vs 7,189 on 09-30",
        "s3 list silver/allocations/2026-10: one object (2026-10-02.parquet) -- the allocation files are still weekly, so the cell, not the allocations, carries the fix",
        "investigation row MDPF_SECCLASS-S19 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The mechanism S19 diagnoses (end date follows a partial delivery; the weekly-allocation confirmation is a no-op) is bypassed by the live S18 class cell; the BLOCKING condition no longer holds on the served cube."
  },
  {
    "id": "MDPF_SECCLASS-C-S22",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S21 (OBSERVATION/INERT) dismissed: Superseded by S22, which re-counts the same fire paths (S21's notification plus the 49F dispatcher) and is graduated; no BD gold hold is in force now.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S21"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Superseded by S22, which re-counts the same fire paths (S21's notification plus the 49F dispatcher) and is graduated; no BD gold hold is in force now.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api get-bucket-notification-configuration opal-data-bd: GoldLayerPricesTrigger -> bd-gold-trigger still present (plus BronzeCompleteSilverMerge -> bd-silver-merge)",
        "investigation row MDPF_SECCLASS-S21 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Superseded by S22, which re-counts the same fire paths (S21's notification plus the 49F dispatcher) and is graduated; no BD gold hold is in force now."
  },
  {
    "id": "MDPF_SECCLASS-C-S23",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S23 (BLOCKING/ARMED) dismissed: Disarmed by S24 (re-mints before the Monday publication) and made moot by Andrew's six-classes ruling and the remap to zero multi_asset rows.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S23"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Disarmed by S24 (re-mints before the Monday publication) and made moot by Andrew's six-classes ruling and the remap to zero multi_asset rows.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ledger 20261004T1953Z_secclass-multi-asset-rows-and-remint-m-20261004: CLOSED 20261006T142745Z",
        "etf-classifications scan: multi_asset 0 of 3,507 rows (0d9457b639 remap) -- the class the producers refused no longer exists",
        "investigation row MDPF_SECCLASS-S23 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by S24 (re-mints before the Monday publication) and made moot by Andrew's six-classes ruling and the remap to zero multi_asset rows."
  },
  {
    "id": "MDPF_SECCLASS-C-S24",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S24 (OBSERVATION/INERT) dismissed: The disarm record of S23; its ledger is closed. Dismissed as S23's resolving row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S24"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The disarm record of S23; its ledger is closed. Dismissed as S23's resolving row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ledger 20261004T1953Z_secclass-multi-asset-rows-and-remint-m-20261004: Status CLOSED -- nothing stranded -- 20261006T142745Z (legs P, M ... closed)",
        "the firm buckets (opal-data-49financial, opal-data-cottonwood) were NOT read from this box (dell1 is denied on firm buckets per the packet); the re-mint VersionIds rest on the ledger only",
        "investigation row MDPF_SECCLASS-S24 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The disarm record of S23; its ledger is closed. Dismissed as S23's resolving row."
  },
  {
    "id": "MDPF_SECCLASS-C-S25",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W13-S2 (OBSERVATION/ARMED) dismissed: Resolved by 58c7dfd2b2: write() carries both fields and every live BLOOMBERG row has them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W13-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Resolved by 58c7dfd2b2: write() carries both fields and every live BLOOMBERG row has them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "etf_classification_scheduled.py:110-113 _WRITE_FIELDS now names security_bloomberg and listing_country (commit 58c7dfd2b2, TO-SC-e17 amendments 1 and 2)",
        "live scan 2026-10-07: 0 of 626 BLOOMBERG rows lack security_bloomberg or listing_country; BBG:REL:LN carries security_bloomberg 'REL LN Equity', listing_country GB",
        "investigation row MDPF_SECCLASS-W13-S2 (0.9.0_WK_MDPF_SECCLASS~13)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by 58c7dfd2b2: write() carries both fields and every live BLOOMBERG row has them."
  },
  {
    "id": "MDPF_SECCLASS-C-S26",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W13-S4 (OBSERVATION/INERT) dismissed: No functional caller of find_by_asset_class / find_by_sub_asset_class exists, so a listed BLOOMBERG row reaches no consumer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W13-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "No functional caller of find_by_asset_class / find_by_sub_asset_class exists, so a listed BLOOMBERG row reaches no consumer.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find 'find_by_(sub_)?asset_class(' --corpus default: DEF in the three etf_classifications_dynamodb.py copies and one census script; otherwise one test and two census scripts -- no functional caller",
        "_shared/etf_classifications_dynamodb.py:117-120 _drop_cusip_rows unchanged",
        "investigation row MDPF_SECCLASS-W13-S4 (0.9.0_WK_MDPF_SECCLASS~13)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No functional caller of find_by_asset_class / find_by_sub_asset_class exists, so a listed BLOOMBERG row reaches no consumer."
  },
  {
    "id": "MDPF_SECCLASS-C-S27",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S25 (OBSERVATION/INERT) dismissed: Disarm verified for W13-S2: the writer now carries both contract fields. W13-S1 (picker key) stays held behind the issuer's own rows act; its own disposition belongs to the W13-S1 row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S25"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Disarm verified for W13-S2: the writer now carries both contract fields. W13-S1 (picker key) stays held behind the issuer's own rows act; its own disposition belongs to the W13-S1 row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py:110-113 at HEAD: _WRITE_FIELDS carries security_bloomberg and listing_country (landed 58c7dfd2b2, TO-SC-e17 amendments)",
        "investigation row MDPF_SECCLASS-S25 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarm verified for W13-S2: the writer now carries both contract fields. W13-S1 (picker key) stays held behind the issuer's own rows act; its own disposition belongs to the W13-S1 row."
  },
  {
    "id": "MDPF_SECCLASS-C-S28",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W14-S1 (OBSERVATION/INERT) dismissed: Superseded: batch 259 answered the domain question; the stocks still without a row are carried by W14-S5.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W14-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Superseded: batch 259 answered the domain question; the stocks still without a row are carried by W14-S5.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "r7_fwd9_row_set.py header line 17 and FWD9_ROW_SET_20261005.tsv: OUT reasons follow batch 259 (provider Equity or empty), the question this row raised",
        "live get-item 2026-10-07: BRK/B, CRWV, EPAM, FPS, MDLN, ORI, SLDE absent; NBIS present (scheduled)",
        "investigation row MDPF_SECCLASS-W14-S1 (0.9.0_WK_MDPF_SECCLASS~14)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Superseded: batch 259 answered the domain question; the stocks still without a row are carried by W14-S5."
  },
  {
    "id": "MDPF_SECCLASS-C-S29",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W14-S2 (OBSERVATION/INERT) dismissed: Resolved by 58c7dfd2b2: the field lives in the shared writer and the wrapper is gone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W14-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Resolved by 58c7dfd2b2: the field lives in the shared writer and the wrapper is gone.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "etf_classification_scheduled.py:110-113 _WRITE_FIELDS includes security_bloomberg (58c7dfd2b2: one writer path, no table wrapper)",
        "live scan: 0 of 626 BLOOMBERG rows lack security_bloomberg",
        "investigation row MDPF_SECCLASS-W14-S2 (0.9.0_WK_MDPF_SECCLASS~14)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by 58c7dfd2b2: the field lives in the shared writer and the wrapper is gone."
  },
  {
    "id": "MDPF_SECCLASS-C-S30",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W14-S3 (OBSERVATION/INERT) dismissed: Resolved by 58c7dfd2b2 (US five-letter XX tickers OUT as money-market funds); none was written as a single-security stock.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W14-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Resolved by 58c7dfd2b2 (US five-letter XX tickers OUT as money-market funds); none was written as a single-security stock.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FWD9_ROW_SET_20261005.tsv: AGPXX, CMQXX, IJGXX read OUT 'money-market fund (US five-letter ticker ending XX), a cash equivalent'",
        "live get-item 2026-10-07: AGPXX, CMQXX, DGCXX absent from etf-classifications",
        "investigation row MDPF_SECCLASS-W14-S3 (0.9.0_WK_MDPF_SECCLASS~14)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by 58c7dfd2b2 (US five-letter XX tickers OUT as money-market funds); none was written as a single-security stock."
  },
  {
    "id": "MDPF_SECCLASS-C-S31",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W14-S4 (OBSERVATION/INERT) dismissed: Resolved: precondition (a) grades the SC-e-16 census by its verdicts (row S26 records the same).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W14-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Resolved: precondition (a) grades the SC-e-16 census by its verdicts (row S26 records the same).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "R7_CHECKS/r7_fwd9_write.py:44-45 and :82-94 grade the census by per-reader verdicts (citing W14-S4); a missing counter is not read as 0",
        "live scan: 626 BLOOMBERG rows written (updated_by rivalfunds-backfill), so the write passed the repaired precondition",
        "investigation row MDPF_SECCLASS-W14-S4 (0.9.0_WK_MDPF_SECCLASS~14)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved: precondition (a) grades the SC-e-16 census by its verdicts (row S26 records the same)."
  },
  {
    "id": "MDPF_SECCLASS-C-S32",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S26 (OBSERVATION/INERT) dismissed: W14-S4 resolved in the issuer's gate script as the row states; W14-S5 is the boundary of the ruled batch-259 rule, carried in the half.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S26"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W14-S4 resolved in the issuer's gate script as the row states; W14-S5 is the boundary of the ruled batch-259 rule, carried in the half.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_write.py:82-96 at HEAD: check_census grades readers by verdict against CLEAN_VERDICTS, reads denominator.uncensused, and does not read a missing counter as 0 (drained 58629060b0)",
        "investigation row MDPF_SECCLASS-S26 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W14-S4 resolved in the issuer's gate script as the row states; W14-S5 is the boundary of the ruled batch-259 rule, carried in the half."
  },
  {
    "id": "MDPF_SECCLASS-C-S33",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W16-S1 (OBSERVATION/INERT) dismissed: The departure is registered (rule 30 / R20 entry X13) with Andrew's permanent acknowledgement.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W16-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The departure is registered (rule 30 / R20 entry X13) with Andrew's permanent acknowledgement.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/logic/06_CONFORMANCE_LEDGER.md:147 X13: new-security-classifier reads opal-data-etfs/silver/holdings/ read-only, five columns; the acknowledgement column reads PERMANENT",
        "investigation row MDPF_SECCLASS-W16-S1 (0.9.0_WK_MDPF_SECCLASS~16)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The departure is registered (rule 30 / R20 entry X13) with Andrew's permanent acknowledgement."
  },
  {
    "id": "MDPF_SECCLASS-C-S34",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W16-S2 (OBSERVATION/INERT) dismissed: Resolved: the map row was added and the function is deployed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W16-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Resolved: the map row was added and the function is deployed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json:3 and :6360 row mdpf-secclass-new-security-lambda (W16-S2, ledger secclass-fwd10-apply-m-20261005)",
        "aws lambda get-function mdpf-secclass-new-security-lambda: Active, LastModified 2026-10-05T20:03Z",
        "investigation row MDPF_SECCLASS-W16-S2 (0.9.0_WK_MDPF_SECCLASS~16)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved: the map row was added and the function is deployed."
  },
  {
    "id": "MDPF_SECCLASS-C-S35",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W20-S2 (OBSERVATION/INERT) dismissed: Superseded: Andrew's six-class word retires multi_asset, so files without it are the target state, not a gap.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W20-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Superseded: Andrew's six-class word retires multi_asset, so files without it are the target state, not a gap.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/cot/scripts/gold/D_03.composition_artifacts.py:102-111 _ASSET_CLASS_LABELS has no multi_asset at HEAD; runners_cot/d08_cot_mix_summary.py:51 unchanged",
        "git log: a62580ef8f 'the S29 gold edits undone ... (Andrew's six-class word; CTO msg 105888)' follows 88728a728e; DECOMP_R8 SC-e-21/22/23 remove multi_asset",
        "investigation row MDPF_SECCLASS-W20-S2 (0.9.0_WK_MDPF_SECCLASS~20)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Superseded: Andrew's six-class word retires multi_asset, so files without it are the target state, not a gap."
  },
  {
    "id": "MDPF_SECCLASS-C-S36",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W20-S3 (OBSERVATION/INERT) dismissed: Order-premise drift, disclosed and worked around by the worker in round 7; the cell is closed and the census records the substitutions. No hazard.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W20-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Order-premise drift, disclosed and worked around by the worker in round 7; the cell is closed and the census records the substitutions. No hazard.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/cot/scripts/gold/runners_cot exists (d08_cot_mix_summary.py read at HEAD); data/assets/scripts/gold/runners_cot does not",
        "investigation row MDPF_SECCLASS-W20-S3 (0.9.0_WK_MDPF_SECCLASS~20)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Order-premise drift, disclosed and worked around by the worker in round 7; the cell is closed and the census records the substitutions. No hazard."
  },
  {
    "id": "MDPF_SECCLASS-C-S37",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S31 (OBSERVATION/ARMED) dismissed: The armed condition fired: BD C_06 published at 05:27Z while the table still held multi_asset rows. The source is gone (0 multi_asset rows since the 07:09Z remap) and Andrew's six-class word removed the class, so no list change is owed. The residual served shortfall is tracked under S36.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S31"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The armed condition fired: BD C_06 published at 05:27Z while the table still held multi_asset rows. The source is gone (0 multi_asset rows since the 07:09Z remap) and Andrew's six-class word removed the class, so no list change is owed. The residual served shortfall is tracked under S36.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3 opal-data-bd gold/views/firm_composition.json generated 2026-10-07T05:28:10Z data_as_of 2026-10-02: total 2,007,761,226.11, sum of 7 class market_values 2,002,269,258.95, gap 5,491,967.16; mix_daily_summary.json LastModified 2026-10-07T05:27:03Z",
        "dynamodb scan etf-classifications filter asset_class=multi_asset: Count 0 of ScannedCount 3507 (2026-10-07 ~09:5xZ)",
        "investigation row MDPF_SECCLASS-S31 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The armed condition fired: BD C_06 published at 05:27Z while the table still held multi_asset rows. The source is gone (0 multi_asset rows since the 07:09Z remap) and Andrew's six-class word removed the class, so no list change is owed. The residual served shortfall is tracked under S36."
  },
  {
    "id": "MDPF_SECCLASS-C-S38",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S33 (OBSERVATION/INERT) dismissed: The 48-vs-77 population question concerned holders of a class Andrew removed; the table holds 0 multi_asset rows, so the check it graded no longer exists.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S33"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The 48-vs-77 population question concerned holders of a class Andrew removed; the table holds 0 multi_asset rows, so the check it graded no longer exists.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "dynamodb scan etf-classifications filter asset_class=multi_asset: Count 0 of ScannedCount 3507 (2026-10-07 ~09:5xZ)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md: six classes, no multi_asset",
        "investigation row MDPF_SECCLASS-S33 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The 48-vs-77 population question concerned holders of a class Andrew removed; the table holds 0 multi_asset rows, so the check it graded no longer exists."
  },
  {
    "id": "MDPF_SECCLASS-C-S39",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S34 (BLOCKING/INERT) dismissed: BLOCKING resolved by supersession: the blocked BD multi_asset list edits are the wrong change under Andrew's six-class word, and the registry the gate enforced is the right state.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S34"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "BLOCKING resolved by supersession: the blocked BD multi_asset list edits are the wrong change under Andrew's six-class word, and the registry the gate enforced is the right state.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-constants.config.yaml:295 at HEAD: MIX_ASSET_CLASSES canonical_value without multi_asset",
        "the worktree holding the uncommitted edits is gone (C:/tmp/wk-secclass-r7-20 absent; cleanup verdict 6c72e70143 read it SUPERSEDED)",
        "dynamodb scan etf-classifications filter asset_class=multi_asset: Count 0 of ScannedCount 3507 (2026-10-07 ~09:5xZ)",
        "investigation row MDPF_SECCLASS-S34 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "BLOCKING resolved by supersession: the blocked BD multi_asset list edits are the wrong change under Andrew's six-class word, and the registry the gate enforced is the right state."
  },
  {
    "id": "MDPF_SECCLASS-C-S40",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S35 (OBSERVATION/ARMED) dismissed: Disarmed by S37: the served-code keys read at their pre-S29 bodies and the repo matches them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S35"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Disarmed by S37: the served-code keys read at their pre-S29 bodies and the repo matches them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "head-object + md5 of git HEAD 572829ce3b: opal-data-cot code/gold C_06 75135f33, lib/mix_views 8c233b0d, D_03 6f48eaf3; opal-data-bd code/gold C_06 0095fc95, lib/mix_views 2c8dbfd7 -- S3 ETag == repo HEAD md5 for 5 of 5, LastModified 2026-10-07 04:16Z; multi_asset count in each repo HEAD body 0",
        "investigation row MDPF_SECCLASS-S35 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by S37: the served-code keys read at their pre-S29 bodies and the repo matches them."
  },
  {
    "id": "MDPF_SECCLASS-C-S41",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S37 (OBSERVATION/INERT) dismissed: Verified: S3 holds the pre-S29 bodies and the repo carries 0 multi_asset in those files, which also closes the row's open repo-revert note.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S37"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Verified: S3 holds the pre-S29 bodies and the repo carries 0 multi_asset in those files, which also closes the row's open repo-revert note.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "head-object + md5 of git HEAD 572829ce3b: opal-data-cot code/gold C_06 75135f33, lib/mix_views 8c233b0d, D_03 6f48eaf3; opal-data-bd code/gold C_06 0095fc95, lib/mix_views 2c8dbfd7 -- S3 ETag == repo HEAD md5 for 5 of 5, LastModified 2026-10-07 04:16Z; multi_asset count in each repo HEAD body 0",
        "investigation row MDPF_SECCLASS-S37 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Verified: S3 holds the pre-S29 bodies and the repo carries 0 multi_asset in those files, which also closes the row's open repo-revert note."
  },
  {
    "id": "MDPF_SECCLASS-C-S42",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S38 (OBSERVATION/ARMED) dismissed: Disarmed by S40: S3 latest and repo HEAD both equal the pre-8f67065e50 body; a later push at 07:09:42Z re-uploaded the same bytes, as S40 predicted.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S38"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Disarmed by S40: S3 latest and repo HEAD both equal the pre-8f67065e50 body; a later push at 07:09:42Z re-uploaded the same bytes, as S40 predicted.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-object-versions opal-data-cot code/gold/B_01b.classify_new_securities.py: latest 68oIr2cg 2026-10-07T07:09:42Z ETag eedfd1d1 (13737 B); u_QyPqqo 06:34:58Z eedfd1d1; Hh9lWlPa 04:16:37Z 28b33a17. md5 of git show 8f67065e50^ and of HEAD 572829ce3b for the file: both eedfd1d1",
        "investigation row MDPF_SECCLASS-S38 (3.0.0_SA_CVO)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by S40: S3 latest and repo HEAD both equal the pre-8f67065e50 body; a later push at 07:09:42Z re-uploaded the same bytes, as S40 predicted."
  },
  {
    "id": "MDPF_SECCLASS-C-S43",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S39 (OBSERVATION/ARMED) dismissed: Disarmed by S40 (verified on the artifact).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S39"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Disarmed by S40 (verified on the artifact).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-object-versions opal-data-cot code/gold/B_01b.classify_new_securities.py: latest 68oIr2cg 2026-10-07T07:09:42Z ETag eedfd1d1 (13737 B); u_QyPqqo 06:34:58Z eedfd1d1; Hh9lWlPa 04:16:37Z 28b33a17. md5 of git show 8f67065e50^ and of HEAD 572829ce3b for the file: both eedfd1d1",
        "investigation row MDPF_SECCLASS-S39 (3.0.0_SA_CVO)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by S40 (verified on the artifact)."
  },
  {
    "id": "MDPF_SECCLASS-C-S44",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S40 (OBSERVATION/INERT) dismissed: Verified: the rollback holds and the repo agrees with S3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S40"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Verified: the rollback holds and the repo agrees with S3.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-object-versions opal-data-cot code/gold/B_01b.classify_new_securities.py: latest 68oIr2cg 2026-10-07T07:09:42Z ETag eedfd1d1 (13737 B); u_QyPqqo 06:34:58Z eedfd1d1; Hh9lWlPa 04:16:37Z 28b33a17. md5 of git show 8f67065e50^ and of HEAD 572829ce3b for the file: both eedfd1d1",
        "investigation row MDPF_SECCLASS-S40 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Verified: the rollback holds and the repo agrees with S3."
  },
  {
    "id": "MDPF_SECCLASS-C-S45",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S41 (OBSERVATION/INERT) dismissed: Census verified for the 5 runnable scripts read here (ETags match the row); B_01b is S40's. No live hazard.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S41"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Census verified for the 5 runnable scripts read here (ETags match the row); B_01b is S40's. No live hazard.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "head-object + md5 of git HEAD 572829ce3b: opal-data-cot code/gold C_06 75135f33, lib/mix_views 8c233b0d, D_03 6f48eaf3; opal-data-bd code/gold C_06 0095fc95, lib/mix_views 2c8dbfd7 -- S3 ETag == repo HEAD md5 for 5 of 5, LastModified 2026-10-07 04:16Z; multi_asset count in each repo HEAD body 0",
        "investigation row MDPF_SECCLASS-S41 (2.0.0_SA_COO~M)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Census verified for the 5 runnable scripts read here (ETags match the row); B_01b is S40's. No live hazard."
  },
  {
    "id": "MDPF_SECCLASS-C-S46",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S42 (OBSERVATION/INERT) dismissed: Held-count drift between DECOMP_R8 and the round-8 cut; each order inlined the re-measured value, so no worker was cut against a stale number. Nothing left to act on.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S42"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Held-count drift between DECOMP_R8 and the round-8 cut; each order inlined the re-measured value, so no worker was cut against a stale number. Nothing left to act on.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python import of _shared/etf_classification.ETF_CLASSIFICATIONS vs R9_CHECKS/MULTI_ASSET_REMAP_B_SET_20261007.tsv at 572829ce3b: keys 33, seed tickers in set 20 (row says 20; DECOMP_R8 said 19)",
        "investigation row MDPF_SECCLASS-S42 (2.0.0_SA_COO~M1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Held-count drift between DECOMP_R8 and the round-8 cut; each order inlined the re-measured value, so no worker was cut against a stale number. Nothing left to act on."
  },
  {
    "id": "MDPF_SECCLASS-C-S47",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "S43 (OBSERVATION/INERT) dismissed: Both stale 0.3.0 pins were repaired by TO-SC-e27 and TO-SC-e31 (complete); the pin tests pass at the drain head.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S43"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Both stale 0.3.0 pins were repaired by TO-SC-e27 and TO-SC-e31 (complete); the pin tests pass at the drain head.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest -q _shared/tests/test_classified_by_v2.py _shared/tests/test_model_classifier.py at 572829ce3b: 54 passed, 0 failed",
        "investigation row MDPF_SECCLASS-S43 (2.0.0_SA_COO~M1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Both stale 0.3.0 pins were repaired by TO-SC-e27 and TO-SC-e31 (complete); the pin tests pass at the drain head."
  },
  {
    "id": "MDPF_SECCLASS-C-S48",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W26-S1 (OBSERVATION/INERT) dismissed: Annotation spelling only (py39 ruff gate); name, parameter and behaviour match the order.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W26-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Annotation spelling only (py39 ruff gate); name, parameter and behaviour match the order.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "_shared/security_name.py:32 'def clean_name(name: str | None) -> str | None:'",
        "investigation row MDPF_SECCLASS-W26-S1 (0.9.0_WK_MDPF_SECCLASS~26)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Annotation spelling only (py39 ruff gate); name, parameter and behaviour match the order."
  },
  {
    "id": "MDPF_SECCLASS-C-S49",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W23-S1 (OBSERVATION/INERT) dismissed: Off-by-one line citation in the order; the census records :95 and the PRD already says 95. No effect on any deliverable.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W23-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Off-by-one line citation in the order; the census records :95 and the PRD already says 95. No effect on any deliverable.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "sed -n 95p yang-generate-positioning/lambda_function.py at 572829ce3b: 'ETF_GEOGRAPHY_MAPPING = {'",
        "investigation row MDPF_SECCLASS-W23-S1 (0.9.0_WK_MDPF_SECCLASS~23)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Off-by-one line citation in the order; the census records :95 and the PRD already says 95. No effect on any deliverable."
  },
  {
    "id": "MDPF_SECCLASS-C-S50",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W28-S1 (OBSERVATION/INERT) dismissed: Absorbed into S47's remedy (PRD manifest path corrections at the next addendum).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W28-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Absorbed into S47's remedy (PRD manifest path corrections at the next addendum).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FWD4_CENSUS_20261007.json s13_resolution maps the four S13 files to their real paths",
        "investigation row MDPF_SECCLASS-W28-S1 (0.9.0_WK_MDPF_SECCLASS~28)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Absorbed into S47's remedy (PRD manifest path corrections at the next addendum)."
  },
  {
    "id": "MDPF_SECCLASS-C-S51",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W28-S2 (OBSERVATION/INERT) dismissed: The two bounds are disclosed in the instrument's own output and the plant was found; the truncated files are data, not code.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W28-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The two bounds are disclosed in the instrument's own output and the plant was found; the truncated files are data, not code.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FWD4_CENSUS_20261007.json read_truncated_over_bytes: limit 3000000, 14 files listed; census_seconds 60.5; plant ran, found true",
        "investigation row MDPF_SECCLASS-W28-S2 (0.9.0_WK_MDPF_SECCLASS~28)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The two bounds are disclosed in the instrument's own output and the plant was found; the truncated files are data, not code."
  },
  {
    "id": "MDPF_SECCLASS-C-S52",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W28-S3 (OBSERVATION/INERT) dismissed: The extra tooling band is disclosed and printed; it keeps 60 production hits visible. A reading choice, not a defect.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W28-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The extra tooling band is disclosed and printed; it keeps 60 production hits visible. A reading choice, not a defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FWD4_CENSUS_20261007.json copies_by_band: prod 60, test 44, tooling 201",
        "investigation row MDPF_SECCLASS-W28-S3 (0.9.0_WK_MDPF_SECCLASS~28)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The extra tooling band is disclosed and printed; it keeps 60 production hits visible. A reading choice, not a defect."
  },
  {
    "id": "MDPF_SECCLASS-C-S53",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W28-S4 (OBSERVATION/INERT) dismissed: Both surfaces were scanned and reported with zero copies and a reason; nothing to act on beyond S47's path correction.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W28-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Both surfaces were scanned and reported with zero copies and a reason; nothing to act on beyond S47's path correction.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FWD4_CENSUS_20261007.json surfaces.S15 copies 0 with note (identifier kind, not a class); surfaces.S26 copies 0 with note",
        "investigation row MDPF_SECCLASS-W28-S4 (0.9.0_WK_MDPF_SECCLASS~28)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Both surfaces were scanned and reported with zero copies and a reason; nothing to act on beyond S47's path correction."
  },
  {
    "id": "MDPF_SECCLASS-C-S54",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W23-S4 (BLOCKING/INERT) dismissed: BLOCKING row resolved by the issuer's amendment 1: the order was re-ruled to a local producer build and completed with a VALID proof. The residual (served bytes unreadable by this principal) is carried by W25-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W23-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "BLOCKING row resolved by the issuer's amendment 1: the order was re-ruled to a local producer build and completed with a VALID proof. The residual (served bytes unreadable by this principal) is carried by W25-S1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-SC-e33 order file: <status>complete; AMENDMENT 1 (~09:1xZ) rules the held set from a local producer build, source marked inferred",
        "python .tools/proof-of-spec-check.py on deliverables/0.9.0_WK_MDPF_SECCLASS~23/...TO-SC-e33...proof_of_spec.json: VALID (rc=0)",
        "investigation row MDPF_SECCLASS-W23-S4 (0.9.0_WK_MDPF_SECCLASS~23)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "BLOCKING row resolved by the issuer's amendment 1: the order was re-ruled to a local producer build and completed with a VALID proof. The residual (served bytes unreadable by this principal) is carried by W25-S1."
  },
  {
    "id": "MDPF_SECCLASS-C-S55",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W24-S5 (BLOCKING/INERT) dismissed: BLOCKING row resolved by the issuer's amendment 2; AC3 re-run by this read reads ok=True. terraform validate is deferred to the safe-apply plan, which runs before any apply.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W24-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "BLOCKING row resolved by the issuer's amendment 2; AC3 re-run by this read reads ok=True. terraform validate is deferred to the safe-apply plan, which runs before any apply.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-SC-e28 AMENDMENT 2 (~09:4xZ) rules W24-S5: validate leaves AC3 and runs in the issuer's safe-apply plan",
        "python issuer_check_sc_e28_tf.py at 572829ce3b: 'SC-E28-TF ok=True fmt=clean names=5 registered=5 unregistered=[] validate=deferred-to-safe-apply'",
        "proof-of-spec-check on the e28 proof: VALID (rc=0)",
        "investigation row MDPF_SECCLASS-W24-S5 (0.9.0_WK_MDPF_SECCLASS~24)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "BLOCKING row resolved by the issuer's amendment 2; AC3 re-run by this read reads ok=True. terraform validate is deferred to the safe-apply plan, which runs before any apply."
  },
  {
    "id": "MDPF_SECCLASS-C-S56",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W24-S7 (OBSERVATION/INERT) dismissed: Superseded by TO-SC-e28 amendment 2, which grades registration through lib/opal_naming grade(); AC3 now reads ok=True.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W24-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Superseded by TO-SC-e28 amendment 2, which grades registration through lib/opal_naming grade(); AC3 now reads ok=True.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "sector-writer/main.tf:158 check \"names_are_builder_output\" present",
        "issuer_check_sc_e28_tf.py: names=5 registered=5 (amendment 2 replaced the literal-name limb with grade() CONFORMANT)",
        "investigation row MDPF_SECCLASS-W24-S7 (0.9.0_WK_MDPF_SECCLASS~24)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Superseded by TO-SC-e28 amendment 2, which grades registration through lib/opal_naming grade(); AC3 now reads ok=True."
  },
  {
    "id": "MDPF_SECCLASS-C-S57",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W24-S8 (BLOCKING/INERT) dismissed: BLOCKING row resolved by the issuer's amendment 2; the registry validates clean and AC3 reads registered=5.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W24-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "BLOCKING row resolved by the issuer's amendment 2; the registry validates clean and AC3 reads registered=5.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-SC-e28 AMENDMENT 2 rules W24-S8 ('registered' = grade() CONFORMANT, no redundant row)",
        "python lib/opal_naming.py validate at 572829ce3b: 'VALIDATE: OK 53 system row(s), 13 scope row(s), 41 warning(s)'",
        "investigation row MDPF_SECCLASS-W24-S8 (0.9.0_WK_MDPF_SECCLASS~24)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "BLOCKING row resolved by the issuer's amendment 2; the registry validates clean and AC3 reads registered=5."
  },
  {
    "id": "MDPF_SECCLASS-C-S58",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W26-S2 (OBSERVATION/INERT) dismissed: The ordered repair is done and passes; the remaining exact-set pin on classified_by is a known fragility the next cell that adds a writer value will meet in its own test run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W26-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The ordered repair is done and passes; the remaining exact-set pin on classified_by is a known fragility the next cell that adds a writer value will meet in its own test run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pytest -q test_model_classifier.py with test_classified_by_v2.py at 572829ce3b: 54 passed",
        "investigation row MDPF_SECCLASS-W26-S2 (0.9.0_WK_MDPF_SECCLASS~26)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The ordered repair is done and passes; the remaining exact-set pin on classified_by is a known fragility the next cell that adds a writer value will meet in its own test run."
  },
  {
    "id": "MDPF_SECCLASS-C-S59",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W26-S4 (OBSERVATION/INERT) dismissed: The box ruff now equals the gate pin: dell1 gate ruff is 0.15.11 since ~09:45Z (MSTR~DELL1 msg 114), confirmed by this seat; the version skew the row names no longer exists.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W26-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The box ruff now equals the gate pin: dell1 gate ruff is 0.15.11 since ~09:45Z (MSTR~DELL1 msg 114), confirmed by this seat; the version skew the row names no longer exists.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/commit-gate.sh:46 'Pinned version: 0.15.11'; python -m ruff --version on dell1 -> ruff 0.16.10",
        "python -m ruff --version and ruff --version on dell1 by 3.0.0_SA_CVO 2026-10-07 09:4xZ: both ruff 0.15.11, the gate pin (.tools/commit-gate.sh:46); 0.0.0_AB_MSTR~DELL1 msg 114 replaced the 0.16.10 binary at ~09:45Z",
        "investigation row MDPF_SECCLASS-W26-S4 (0.9.0_WK_MDPF_SECCLASS~26)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The box ruff now equals the gate pin: dell1 gate ruff is 0.15.11 since ~09:45Z (MSTR~DELL1 msg 114), confirmed by this seat; the version skew the row names no longer exists."
  },
  {
    "id": "MDPF_SECCLASS-C-S60",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T09:50:00Z",
    "one_line": "W26-S5 (OBSERVATION/INERT) dismissed: The write path the round uses adds identifier_namespace through NamespaceTable; the runner is unchanged and has no other caller this round.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W26-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The write path the round uses adds identifier_namespace through NamespaceTable; the runner is unchanged and has no other caller this round.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "classify-residual-model.py: no identifier_namespace in landing_row; old_list_reclassify_write.py:85 class NamespaceTable wraps put_item",
        "investigation row MDPF_SECCLASS-W26-S5 (0.9.0_WK_MDPF_SECCLASS~26)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The write path the round uses adds identifier_namespace through NamespaceTable; the runner is unchanged and has no other caller this round."
  }
]
```
