# ETFS_RIVALS -- round 1 L8/L9 adjudication (site-Z fabric)

<sweep_watermark>2026-09-30T15:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO~RV, 2026-10-01 ~04:3xZ. Seat: the CVO lane Andrew paired with 2.0.0_SA_COO~RV on ETFS_RIVALS (COO~RV msg 27487, acked). The round-1 drain-end read named 3.0.0_SA_CVO~Z as owner of this compile (`deliverables/2.0.0_SA_COO~RV/round1/DRAIN_END_READ_ROUND1.md:27`); this lane takes it under the pairing, and ~Z need not repeat it. L8 packet: that drain-end read. Review: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md` (co-committed).

Round 1: 9 of 9 orders terminal. The channel's round-1 rows are the 29 surfaced up to the watermark (ETFS_RIVALS-Z-S1, Z-W2-S1, Z-W1-S1..S5, Z-W3-S1..S5, Z-W5-S1..S17). Class split, as the packet printed it: 8 BLOCKING/ARMED, 2 BLOCKING/INERT, 19 OBSERVATION/INERT. Disposition: 21 dismissed by the 5 rows below, 8 graduated in `remediations/REMEDIATION_v1.Z.md` (S1, W1-S4, W1-S5, W5-S3, W5-S7, W5-S12, W5-S14, W5-S15). All 8 ARMED rows are disarmed in the world, re-read by this seat (C-S1, C-S2). The 32 rows after the watermark belong to round 2 and are compiled at its drain-end. No slug yet: round 2 has TO-RIV-d-3 open (the gate's L10 precondition).

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S1",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T04:30:00Z",
    "one_line": "The gateway leg's seven ARMED stops (W5-S1, S6, S8, S9, S10, S16 and the deploy-tree premise S11) are disarmed: the ledger closed at 15:33:58Z, and the live host still serves /rivalfunds after a later seat's 01:38Z deploy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W5-S1",
      "ETFS_RIVALS-Z-W5-S6",
      "ETFS_RIVALS-Z-W5-S8",
      "ETFS_RIVALS-Z-W5-S9",
      "ETFS_RIVALS-Z-W5-S10",
      "ETFS_RIVALS-Z-W5-S11",
      "ETFS_RIVALS-Z-W5-S16",
      "ETFS_RIVALS-Z-W5-S17"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Ledger org/critical_paths/change_management/20260930T1013Z_etfs-rivalfunds-thread-r1_deploy_completion.md reads CLOSED 20260930T153358Z, L1-L6 closed. Every stop's hazard was the ledger going RED with L3/L4/L6 open, plus (W5-S16) /rivalfunds reading 404 after the 2e2254156e overwrite. The issuer redeployed signed ref 4ce7946426 at 15:23:02Z (W5-S17). Since then NFRA_OPLGTW deployed d61fde4693 at 2026-10-01T01:38Z (EC2_MANIFEST at HEAD). That ref is not a descendant of 4ce7946426, but its server.py carries the routes by content: 7 'rivalfunds' hits, the same count as 4ce7946426 (the positive control). This seat's read-only SSM cbe1a6ef-1cfc-473b-a539-097ebb8e9f03 (~04:1xZ) reads host server.py sha256 384c6d41...f1f6, equal to git show d61fde4693; /health 200, /rivalfunds 401, /rivalfunds/archive 401; ActiveEnterTimestamp 2026-10-01 01:38:24 UTC.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W5-S1, S6, S8, S9, S10, S11, S16, S17",
        "ledger 20260930T1013Z_etfs-rivalfunds-thread-r1_deploy_completion.md:3 'CLOSED -- nothing stranded -- closed 20260930T153358Z'",
        "SSM cbe1a6ef-1cfc-473b-a539-097ebb8e9f03 on i-07dccb1615503ac99 (this seat, read-only)",
        "2.0.0_SA_COO~RV DRAIN_END_READ_ROUND1.md:29-43, the disarming act per row",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each hazard is gone in the world, and the routes survived another seat's later gateway deploy. The MECHANISMS behind S10 and S11 are not dismissed: they ride graduated items W5-S12 (a worker cannot commit or deploy a deploy-only ref) and W5-S3 (the gateway cannot be planned or deployed from a fresh tree)."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S2",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T04:30:00Z",
    "one_line": "The gold package gap (W5-S4) is disarmed: the packager stages etf_positioning_gold.py and gold exists in the bucket for 501 dates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W5-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "infra/aws/lambda/etfs-pipeline/rivalfunds_package.py:39 at HEAD stages (\"data/etfs/scripts/gold/etf_positioning_gold.py\", \"gold\" + \"/etf_positioning_gold.py\") (worker fix 3eaa380467). This seat's list-objects-v2 of opal-data-etfs ~04:2xZ: gold/canonical_shape 745 objects over 501 dates, gold/trade_schedule 743 over 500, both newest 2026-09-29; platinum/page 12 objects, newest date=2026-09-30.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ETFS_RIVALS-Z-W5-S4",
        "rivalfunds_package.py:39 at CLOUD HEAD",
        "ledger thread-r1 L4: d-2.AC1 and AC3 PASS 0 failures, re-run 15:26Z",
        "this seat's S3 census (denominators above)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Fixed in round by the issuer's amendment 3 and proven by the live chain; the gate false positive that shaped the fix is graduated as W5-S7."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S3",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T04:30:00Z",
    "one_line": "Four round-1 spec gaps are ruled in writing and carried by the round-2 decomposition or an amended check: W1-S1 (daily event date), W1-S2 (bronze key), W1-S3 (s-1.AC2), W3-S5 (snake-case state tables).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W1-S1",
      "ETFS_RIVALS-Z-W1-S2",
      "ETFS_RIVALS-Z-W1-S3",
      "ETFS_RIVALS-Z-W3-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "decompositions/ETFS_RIVALS_DECOMP.md:90-92 rules W1-S1 (the event date is the ACT day; the collector fetches prev_trading_day(date)); :93-95 rules W1-S2 (keys carry the requested date), built in RIV-b-1 (3ac5a8666e); TO-RIV-s-1 completion_note: AC2 PASS at amended check be252dc1de (row W1-S3 ruled); :58 rules W3-S5 (state tables are snake case, amendment 746558e232), and the six generated files are tracked at HEAD with state/fetch_holdings, state/build_silver, etc.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W1-S1, W1-S2, W1-S3, W3-S5",
        "ETFS_RIVALS_DECOMP.md:58, :90-95, :113-114",
        "task-orders/ETFS_RIVALS.TO-RIV-s-1.bronze-to-typed-silver.md:137-138",
        "git ls-files infra/aws/terraform/etfs-rivalfunds/: generated.auto.tfvars.json + five policies/*.json",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is ruled and built. W1-S2's key change has a round-2 consequence, W2-S4 (ARMED: silver ordering across key formats), which the round-2 compile adjudicates on its own row."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S4",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T04:30:00Z",
    "one_line": "Seven build-time records of a legal resolution inside the grant: W2-S1, W3-S1, W3-S2, W3-S3, W5-S2, W5-S5, W5-S13.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W2-S1",
      "ETFS_RIVALS-Z-W3-S1",
      "ETFS_RIVALS-Z-W3-S2",
      "ETFS_RIVALS-Z-W3-S3",
      "ETFS_RIVALS-Z-W5-S2",
      "ETFS_RIVALS-Z-W5-S5",
      "ETFS_RIVALS-Z-W5-S13"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The issuer flipped w-1 at the merge (W2-S1); NAMING_SCHEMA.json is the packager's sixth staged source (W3-S1); sweep.trigger_event normalises EventBridge and Scheduler input (W3-S2); the sweep role is the union of the five stages' grants over ten builder prefixes, and d-1.AC3 found no Put outside them and no Delete (W3-S3); HALT_ACK=1 is the gate's own routine-message path (W5-S2); the gate-3 count was this stack's own 07:00 ET fire, not a foreign writer (W5-S5); the app's liveness route is /health, not /healthz (W5-S13).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W2-S1, W3-S1, W3-S2, W3-S3, W5-S2, W5-S5, W5-S13",
        "all nine round-1 orders terminal (DRAIN_END_READ_ROUND1.md:5-14)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each landed legal. The forward residue: W5-S2's worker-identity friction rides graduated W5-S12. W5-S5's lesson (a schedule live at apply time breaks a zero-count gate for any apply-then-act order) is the never-widen author's; d-3's half measured its BEFORE state. W5-S13 leaves CTO condition 5, the signed-in /rivalfunds read, with a human: it is FWD-1's acceptance evidence (PRD FIXTURES), not a defect."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S5",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T04:30:00Z",
    "one_line": "W3-S4's sweep-versus-rule double run is not observed: every gold batch has exactly one marker, and the 244 dates holding two canonical_shape objects are two revisions written 14 hours apart by different batches.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W3-S4"
    ],
    "spec_asserts": "RIV-d-1: both trigger paths stay armed (C-TRIGGERS) and every stage is idempotent on batch_id, so a stage the sweep and the rule both start writes one result per batch.",
    "world_is": "This seat's list of state/build_canonical_shape/ reads 10 markers, one per batch (096abceb scheduled, backfill-r1a, backfill-r1b, import-r2-00..06), with no batch twice. Of 501 canonical_shape dates, 244 hold two objects. Sampled date=2026-06-03: holdings-20260930T114643Z-9f56ddf9c0ee.parquet (24820 B, written 2026-09-30T12:32:15Z, round 1, BASG) and holdings-20260930T151317Z-653c704b70df.parquet (77471 B, written 2026-10-01T02:17:07Z, round 2's multi-fund import). That is a new revision with new content, not a re-run of one batch.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ETFS_RIVALS-Z-W3-S4",
        "this seat's list-objects-v2 of opal-data-etfs rivalfunds/etfs/gold/canonical_shape/ and state/build_canonical_shape/ ~04:2xZ",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The race needs a stalled chain the sweep repairs while the rule also fires; the live record shows none. It stays a design property, not a hazard. Its natural exercise is FWD-8 (the no-duplicate rerun), which the PRD's enrichment backlog already names."
  }
]
```
