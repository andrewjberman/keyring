# ETFS_RIVALS -- round 5 L8/L9 adjudication, part A (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-02 ~05:25Z, relaunched on Andrew-direct ~04:57Z
(`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261002_045xZ_RV_TEAM_ETFS_RIVALS_ADJUDICATION_AND_EGRESS_TONIGHT.md`).

**Scope:** every investigation row on CLOUD at ccde3fa12f that is surfaced after the round-4 watermark (2026-10-01T22:40Z).
That is 128 rows minus the 121 compiled in rounds 1-4, so 7 rows. This document carries NO `<sweep_watermark>` element
on purpose. Four rows surfaced earlier (W5-S29..S32, 01:31Z-01:54Z) sit on the undrained branch `wk-rivals5-5` (RIV-s-6).
A time cut would claim them, and this compile has not read them as served. They are compiled in part B, with the
round-5 slug, after that branch drains.

**Round state at this compile:** 35 of 45 orders terminal. COO~RV moved ETFS_RIVALS to a FAST lease from 05:08Z
(`org/mcp/drive-mode.log` line 56, msg 28219). The A1 orders become the lease's next-list. `wk-rivals5-2` (m-2, l-1) and
`wk-rivals5-5` (s-6) are held and drain after the morning legs. No slug goes out before every order is terminal, so S13
stays open here and graduates in part B.

**Disposition of the 7 rows:**
- 6 are dismissed by C-S17 and C-S18 below.
- S13 (BLOCKING, INERT) stays UNDER_INVESTIGATION. The f-4 mechanism is built, but the shipped config still holds BASG
  to 0.23. The timing of the config change is a call, and it went to `4.0.0_SA_CRO~RV`.

**Clock advances in the same commit:** six earlier remediation rows advance in place.
- W4-S9 is REMEDIATED in code by RIV-b-2 @a5c6cf991c. Its disarm stays ARMED with COO~RV until the code is deployed and
  one real marker batch above 45 dates completes on the Lambda.
- Five more are REMEDIATED and closed by the round-4 analysis (`ledger/ROUND_ANALYSIS.round4.md`):
  - W4-S7 (ruling 8);
  - W4-S14 (ruling 9);
  - W5-S12 (ruling 10);
  - S2 (ruling 12, the interim lock);
  - W5-S15 (ruling 11). Both refs are tagged: `git tag --points-at 288fa78c93` and `093fc247c6` each print a tag.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S17",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-02T05:25:00Z",
    "one_line": "Four round-5 rows are closed at HEAD: W3-S18 (ARMED, 4 red RIV-h-4 tests) is repaired by the amendment and fix that W3-S19 records, W3-S17's page clause is built by RIV-f-4 and its config file ships in every stage zip, and W4-S17's reading of the manifest word matches ruling 7.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W3-S18",
      "ETFS_RIVALS-Z-W3-S19",
      "ETFS_RIVALS-Z-W3-S17",
      "ETFS_RIVALS-Z-W4-S17"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W3-S18/S19: amendment a84ad1ad3b added test_r5h4_id_change_identifier_relation.py to RIV-h-6's paths, and fix 7faba49a91 changed the five expectations to CLEAN. This seat ran `python -m pytest rivalfunds/tests -q` at CLOUD ccde3fa12f and read 342 passed, 2 skipped, 0 failed, so the ARMED hazard (a red suite) is gone. W3-S17: render.py:170-179 `refused()` renders a REFUSED G6 row as 'not inferred: the window was refused', and publish_page.py:338-354 never drops it or shows it as an empty window (RIV-f-4 e69e51cd39). The second clause is closed by construction: infra/aws/lambda/etfs-pipeline/rivalfunds_package.py:33 stages the whole data/etfs/scripts/rivalfunds directory into every stage Lambda, and :41 ignores only __pycache__, *.pyc, tests and .pytest_cache. So guardrails_config.json, which gold_trade_schedule.refusal_limits() reads (:438), ships in every zip. W4-S17: publish_page.py:550 is `\"published\" if ctx[\"n_updated\"] else \"not-updated\"`. Ruling 7 says the word means 'page published', and FWD-9 says failed figures never publish. A page with no fund updated publishes no figures.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W3-S18, W3-S19, W3-S17, W4-S17",
        "this seat's `python -m pytest rivalfunds/tests -q` at CLOUD ccde3fa12f: 342 passed, 2 skipped",
        "data/etfs/scripts/rivalfunds/render.py:170-179, publish_page.py:338-354, :550 at HEAD",
        "infra/aws/lambda/etfs-pipeline/rivalfunds_package.py:33, :41, :71 at HEAD",
        "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md:47 (ruling 7)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Repaired in round, or matches the ruling. The refused-window display is in code only. Nothing serves a refused window until the G5/G6 replay (round 6), and that replay is where it gets its first real proof."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S18",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-02T05:25:00Z",
    "one_line": "Two round-5 build choices are recorded as built: W1-S40 (the G1 cursor is a `.cursor` object no marker reader or trigger sees) and W3-S16 (hop-9 (a)'s identifier-event limb is built and dormant, because no served source names an identifier event).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W1-S40",
      "ETFS_RIVALS-Z-W3-S16"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W1-S40: markers.py:52-53 names the cursor `<marker stem>.cursor`. Every lister of that prefix filters on `.json`: markers.py:28, sweep.py:255 and gold_holdings_coverage.py:284. The five EventBridge rules in infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json bind state/build_bloomberg_silver/, build_silver/, fetch_bloomberg/, fetch_holdings/ and build_trade_schedule/, and none binds state/build_canonical_shape/. The canonical-shape role already holds Put and Get on state/build_canonical_shape/* (policies/rivalfunds-build-canonical-shape-lambda.json, PutGetOwnPrefixes). W3-S16: gold_trade_schedule.py:119 IDENTIFIER_EVENT_TYPES and :359-368 identifier_events() need an event row with `counterpart_security_id`. enrichment_bloomberg.py:119 map_event_type maps Bloomberg dividend types only, so the limb returns no pair on served data. The crosswalk and CUSIP-equality limbs still fire.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W1-S40, W3-S16",
        "data/etfs/scripts/rivalfunds/markers.py:28, :52-70; sweep.py:255; gold_holdings_coverage.py:284 at HEAD",
        "infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json `rules` (5 prefixes) and policies/rivalfunds-build-canonical-shape-lambda.json at HEAD",
        "data/etfs/scripts/rivalfunds/gold_trade_schedule.py:119, :359-368; enrichment_bloomberg.py:119 at HEAD"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Built as the order and ruling allow. W1-S40 gets its first served proof on the first real PARTIAL G1 run after b-2 deploys (W4-S9's disarm). W3-S16's dormant limb rides with W3-S12 (round 6: probe whether a Bloomberg field names the related security). Until then a shared CUSIP-6 never pairs on served data, and that is the safe direction."
  }
]
```

-- 3.0.0_SA_CVO~RV
