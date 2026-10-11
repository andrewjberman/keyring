# MDPF_CANON -- round 2 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-11T02:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T02:25:00Z. L8 packet: 2.0.0_SA_COO~D1 msg 3275, `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/ROUND2_CLOSE.md` @8f550419f6. Risk WORLD. 4 of 4 orders complete.

**L9:** CN-b-1 AC3 MET; CN-b-2 AC3 NOT MET (the basis says minimum firm count 2; global carries 12 single-firm by_model entries, 6 at 3 or fewer accounts, and two single-firm series); CN-b-3 AC3 MET; CN-b-4 AC3 MET.
Carried: CN-a-2 AC3 stays NOT MET and FWD-1 PARTIAL on the 2026-10-10 13:30Z fire (D1-S9); FWD-3 not REALIZED (C-S12).
Rows: D1-W7-S1, D1-W5-S1, D1-W4-S1 dismissed. D1-S8 graduated INERT; D1-S9 graduated BLOCKING; C-S12 graduated. All three go to `remediations/REMEDIATION_v2.md`.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S11",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:25:00Z",
    "one_line": "MDPF_CANON.TO-CN-b-1 AC3 MET: the census lists or excludes with a reason every live reader and writer this seat's own unscoped read finds. Over tracked code and config in infra/, data/, lib/, .tools/ and .claude/ (md, jsonl, log and the ontology census excluded), the served key json/portfolios/aum-timeseries is named in 22 files and the census cites all 22; mdpf/bronze 2 of 2; gold/mdpf_revamp 36 of 40; portal/gold/mdpf 20 of 22. The 6 uncited files hold no reader or writer outside a row the census already carries: a docstring (build_dim_model_portfolio.py:37), two script-FILENAME hits of the class the census excludes by reason (mdpf_name_discovery.py:84, the gold Lambda BUILD_MANIFEST.json:155), two CHANGELOG.json files (history), and EC2_MANIFEST.json:482, which names the portal/gold/mdpf/_code/ accrual bundle the census's _code row already rules live. The denominator is printed and reconciled to IV.2 (47 config cells against the floor of 50, disclosed as a citation grouping); INSTRUMENT names what the name census cannot see. The one unseen limb, the portal front end, is closed by row D1-S8, which this seat re-read at portal c96efe17: the readers of the stale key sit only in src/api (portal-proxy.ts:338-345, endpoints/aum.ts:322-328 and :447-449), and no page calls them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD v2.10 @fa51c1f544 (round 2: M1, M5, M7/FWD-3, W1-S1); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-b-1 AC3 MET: the census lists or excludes with a reason every live reader and writer this seat's own unscoped read finds. Over tracked code and config in infra/, data/, lib/, .tools/ and .claude/ (md, jsonl, log and the ontology census excluded), the served key json/portfolios/aum-timeseries is named in 22 files and the census cites all 22; mdpf/bronze 2 of 2; gold/mdpf_revamp 36 of 40; portal/gold/mdpf 20 of 22. The 6 uncited files hold no reader or writer outside a row the census already carries: a docstring (build_dim_model_portfolio.py:37), two script-FILENAME hits of the class the census excludes by reason (mdpf_name_discovery.py:84, the gold Lambda BUILD_MANIFEST.json:155), two CHANGELOG.json files (history), and EC2_MANIFEST.json:482, which names the portal/gold/mdpf/_code/ accrual bundle the census's _code row already rules live. The denominator is printed and reconciled to IV.2 (47 config cells against the floor of 50, disclosed as a citation grouping); INSTRUMENT names what the name census cannot see. The one unseen limb, the portal front end, is closed by row D1-S8, which this seat re-read at portal c96efe17: the readers of the stale key sit only in src/api (portal-proxy.ts:338-345, endpoints/aum.ts:322-328 and :447-449), and no page calls them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO git grep -l -I -F per surface string over infra data lib .tools .claude at box/dell1 9dee79a23a, each file checked for a citation in deliverables/0.9.0_WK_MDPF_CANON~4/READER_CENSUS.md: 22/22, 2/2, 36/40, 20/22",
        "3.0.0_SA_CVO git grep -n getAUMTimeSeries|getModelTimeSeries|aum-timeseries in portal/src at c96efe17: calls only inside src/api; pages/ModelPortfolios.tsx hits are comments (:347, :418, :563-569)",
        "r2_checks.py census 4 of 4 arms (this seat's run at HEAD)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: a judgment criterion graded by a seat that did none of the work."
  },
  {
    "id": "MDPF_CANON-D1-C-S12",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:25:00Z",
    "one_line": "MDPF_CANON.TO-CN-b-2 AC3 NOT MET: the paragraph exists and is pointed at by the ledger X2 row, but its minimum firm count is ASSERTED, not read from what the producer emits. X2_GLOBAL_BASIS.md says 'Minimum firm count: 2 ... no non-null figure combines fewer than 2 firms' and 'the finest account-level fact is an integer count'. The producer's own global output says otherwise. (1) On 2026-10-08 the global aggregate-aua-timeseries by_model carries 18 models with a value. 12 of them are held at exactly ONE firm, and global's model_value equals that firm's value in 12 of 12. Six of those 12 carry account_count 3 or fewer, so a global entry is one or two accounts' holding value under a model name. (2) non_model_aua is 49financial's alone and inflection_non_model_aua inflection's alone (dim_mdpf_aggregate_aua_timeseries.py:2434-2435), each non-zero on 484 of 493 dates. The summed headline series (model_aua, opal_aggregate_aua, partner custody) do need 2 or 3 firms, as the basis reads from :2399-2429. FWD-3's ACCEPT ('reveals nothing about any single firm's clients') is therefore not met by the written reason. No account identifier is present; what is present is single-firm, small-count values.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD v2.10 @fa51c1f544 (round 2: M1, M5, M7/FWD-3, W1-S1); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-b-2 AC3 NOT MET: the paragraph exists and is pointed at by the ledger X2 row, but its minimum firm count is ASSERTED, not read from what the producer emits. X2_GLOBAL_BASIS.md says 'Minimum firm count: 2 ... no non-null figure combines fewer than 2 firms' and 'the finest account-level fact is an integer count'. The producer's own global output says otherwise. (1) On 2026-10-08 the global aggregate-aua-timeseries by_model carries 18 models with a value. 12 of them are held at exactly ONE firm, and global's model_value equals that firm's value in 12 of 12. Six of those 12 carry account_count 3 or fewer, so a global entry is one or two accounts' holding value under a model name. (2) non_model_aua is 49financial's alone and inflection_non_model_aua inflection's alone (dim_mdpf_aggregate_aua_timeseries.py:2434-2435), each non-zero on 484 of 493 dates. The summed headline series (model_aua, opal_aggregate_aua, partner custody) do need 2 or 3 firms, as the basis reads from :2399-2429. FWD-3's ACCEPT ('reveals nothing about any single firm's clients') is therefore not met by the written reason. No account identifier is present; what is present is single-firm, small-count values.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO s3api get-object opal-data-assets portal/gold/mdpf/{global,49financial,inflection,cottonwood}/aggregate-aua-timeseries/2026-10-08.json (700334/457692/119028/505692 B), by_model model_value compared per model on the last date: single-firm 12, equal to the firm's value 12, account_count<=3 in 6; 2-firm 1; 3-firm 5 (counts only, no figure printed)",
        "data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:2399-2400 (_sum2), :2420-2429 (model_aua branches), :2434-2435 (non_model = nm49 only; inf_non_model = nminf only)",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~5/X2_GLOBAL_BASIS.md sections 'Minimum firm count' and 'Why no per-firm or per-account row survives'",
        "PRD v2.10 FWD-3 ACCEPT (lines 124-133) and DEC-7 (line 285)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Graduated to REMEDIATION_v2: the basis's owner rewrites the minimum firm count per field family from the producer's output and states the single-firm, small-count by_model entries, or the CTO rules what X2 may carry. Andrew's X2 grant rests on the written basis."
  },
  {
    "id": "MDPF_CANON-D1-C-S13",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:25:00Z",
    "one_line": "MDPF_CANON.TO-CN-b-3 AC3 MET: the publisher runs on python3.11 and serves leaves whose data-bearing values equal what it served before. Live: Runtime python3.11, one layer pandas-pyarrow-requests-layer:1, CodeSha256 pj+Jat96...EJA= (equal to the pre-apply sha the deploy record states). The producer's DELTA=0 (125,721 values across 18 leaves; 444 archive keys byte-identical) is corroborated on this seat's own read of the ORGANIC 2026-10-10 13:50Z scheduled run on python3.11: three served leaves (global aum-metrics, cottonwood aggregate-aua-timeseries, 49financial account-distribution) compared value by value with the gold JSON each was published from -- 36,272 of 36,272 values equal in value and type, 0 keys on one side only, _provenance excluded. The run logged OK on every leaf, with no error.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD v2.10 @fa51c1f544 (round 2: M1, M5, M7/FWD-3, W1-S1); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-b-3 AC3 MET: the publisher runs on python3.11 and serves leaves whose data-bearing values equal what it served before. Live: Runtime python3.11, one layer pandas-pyarrow-requests-layer:1, CodeSha256 pj+Jat96...EJA= (equal to the pre-apply sha the deploy record states). The producer's DELTA=0 (125,721 values across 18 leaves; 444 archive keys byte-identical) is corroborated on this seat's own read of the ORGANIC 2026-10-10 13:50Z scheduled run on python3.11: three served leaves (global aum-metrics, cottonwood aggregate-aua-timeseries, 49financial account-distribution) compared value by value with the gold JSON each was published from -- 36,272 of 36,272 values equal in value and type, 0 keys on one side only, _provenance excluded. The run logged OK on every leaf, with no error.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO lambda get-function-configuration opal-assets-mdpf-portal-publisher: python3.11, layer arn ...:layer:pandas-pyarrow-requests-layer:1, CodeSha256 pj+Jat96t5dijB+0SQF918S1pi3AZBs1eQNvMXLYEJA=, LastModified 2026-10-09T22:21:52Z",
        "3.0.0_SA_CVO get-object of the three platinum/mdpf leaves (LastModified 2026-10-10T13:50:50-52Z) and their gold sources; flattened compare 190/190, 35618/35618, 464/464, 0 diffs",
        "/aws/lambda/opal-assets-mdpf-portal-publisher 2026-10-10T13:50Z: 'OK: published' per leaf",
        "org/critical_paths/change_management/20261009T2216Z_mdpf-canon-r2-publisher-layer-and-builder-grant-dell1-20261009_deploy_completion.md L3, L4, L5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: a judgment criterion graded by a seat that did none of the work."
  },
  {
    "id": "MDPF_CANON-D1-C-S14",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:25:00Z",
    "one_line": "MDPF_CANON.TO-CN-b-4 AC3 MET: the composite grant on builder output renders a policy identical to the live one. Source iam.tf:1590-1625 takes every composite ARN from module.mdpf_scope_buckets.scope_bucket[\"mdpf\"], which the builder module maps to opal-data-mdpf (modules/opal_name/generated_locals.tf:74). The live mdpf-gold-writer-assume-policy reads the same three statements: the three role ARNs; Put/Get on exactly the four opal-data-mdpf mdpf/global/gold/<artifact>/* keys; ListBucket on arn:aws:s3:::opal-data-mdpf. So the producer's targeted plan rc=0 'No changes' (target resolved, 5 no-ops in the planfile) agrees with this seat's hand render. For the CTO: scope_bucket[\"global\"] still reads opal-data-portal-v2 (:70), so a consumer that keys the composite by 'global' gets the platinum bucket (packet note on W1-S1).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD v2.10 @fa51c1f544 (round 2: M1, M5, M7/FWD-3, W1-S1); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-b-4 AC3 MET: the composite grant on builder output renders a policy identical to the live one. Source iam.tf:1590-1625 takes every composite ARN from module.mdpf_scope_buckets.scope_bucket[\"mdpf\"], which the builder module maps to opal-data-mdpf (modules/opal_name/generated_locals.tf:74). The live mdpf-gold-writer-assume-policy reads the same three statements: the three role ARNs; Put/Get on exactly the four opal-data-mdpf mdpf/global/gold/<artifact>/* keys; ListBucket on arn:aws:s3:::opal-data-mdpf. So the producer's targeted plan rc=0 'No changes' (target resolved, 5 no-ops in the planfile) agrees with this seat's hand render. For the CTO: scope_bucket[\"global\"] still reads opal-data-portal-v2 (:70), so a consumer that keys the composite by 'global' gets the platinum bucket (packet note on W1-S1).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO iam get-role-policy mdpf-gold-lambda-role / mdpf-gold-writer-assume-policy: Sids GoldWriterAssumeScopedRoles, GoldCompositePutGet, GoldCompositeListScoped with the resources above",
        "infra/aws/terraform/mdpf-pipeline/iam.tf:1586-1625 at 9dee79a23a; infra/aws/terraform/modules/opal_name/generated_locals.tf:70,74",
        "r2_checks.py builder 3 of 3 and r1_iam.py 6 of 6 (this seat's run at HEAD)",
        "deploy completion record L1 (plan -detailed-exitcode rc=0 with the three-way control)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: a judgment criterion graded by a seat that did none of the work."
  },
  {
    "id": "MDPF_CANON-D1-C-S15",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:25:00Z",
    "one_line": "D1-W7-S1 dismissed: the issuer's ARN scanner defect was fixed in the issuer's own checks (@8a4ef42ee6, an HCL-aware scanner in r2_checks.py and r1_iam.py). At HEAD this seat reads builder 3 of 3 and r1_iam 6 of 6.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W7-S1"
    ],
    "spec_asserts": "MDPF_CANON PRD v2.10 @fa51c1f544 (round 2: M1, M5, M7/FWD-3, W1-S1); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-W7-S1 dismissed: the issuer's ARN scanner defect was fixed in the issuer's own checks (@8a4ef42ee6, an HCL-aware scanner in r2_checks.py and r1_iam.py). At HEAD this seat reads builder 3 of 3 and r1_iam 6 of 6.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W7-S1",
        "git show 8a4ef42ee6",
        "3.0.0_SA_CVO r2_checks.py builder / r1_iam.py at 9dee79a23a"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W7-S1 dismissed: fixed in the issuer's checks @8a4ef42ee6; both read green at HEAD."
  },
  {
    "id": "MDPF_CANON-D1-C-S16",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:25:00Z",
    "one_line": "D1-W5-S1 dismissed: AMENDMENT 1 (@6f0b43bb0f) moved both documents to their authors' serial folders. PRD v2.10 (@fa51c1f544) records the paths, and the ledger X2 row cites deliverables/0.9.0_WK_MDPF_CANON~5/X2_GLOBAL_BASIS.md. This seat reads basis 3 of 3 and census 4 of 4 at HEAD. The basis's content is graded separately (C-S12).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W5-S1"
    ],
    "spec_asserts": "MDPF_CANON PRD v2.10 @fa51c1f544 (round 2: M1, M5, M7/FWD-3, W1-S1); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-W5-S1 dismissed: AMENDMENT 1 (@6f0b43bb0f) moved both documents to their authors' serial folders. PRD v2.10 (@fa51c1f544) records the paths, and the ledger X2 row cites deliverables/0.9.0_WK_MDPF_CANON~5/X2_GLOBAL_BASIS.md. This seat reads basis 3 of 3 and census 4 of 4 at HEAD. The basis's content is graded separately (C-S12).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W5-S1",
        "git show 6f0b43bb0f",
        "infra/logic/06_CONFORMANCE_LEDGER.md:136",
        "3.0.0_SA_CVO r2_checks.py basis / census at 9dee79a23a"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W5-S1 dismissed: the path conflict is resolved by AMENDMENT 1 and PRD v2.10, and both checks read green at HEAD."
  },
  {
    "id": "MDPF_CANON-D1-C-S17",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:25:00Z",
    "one_line": "D1-W4-S1 dismissed: the unseen portal limb is seen in D1-S8, which this seat re-read at portal c96efe17 (readers only in src/api, no page caller).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W4-S1"
    ],
    "spec_asserts": "MDPF_CANON PRD v2.10 @fa51c1f544 (round 2: M1, M5, M7/FWD-3, W1-S1); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-W4-S1 dismissed: the unseen portal limb is seen in D1-S8, which this seat re-read at portal c96efe17 (readers only in src/api, no page caller).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_CANON-D1-W4-S1, -D1-S8",
        "3.0.0_SA_CVO git grep in portal/src at c96efe17"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W4-S1 dismissed: closed by D1-S8, confirmed on this seat's own portal read."
  },
  {
    "id": "MDPF_CANON-D1-C-S18",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:25:00Z",
    "one_line": "D1-S8 confirmed and graduated INERT: json/portfolios/aum-timeseries.json has dead readers in portal/src/api and no live page caller at c96efe17. Removing them is a portal-repo act at the served key's retirement in the PRD's arc, not a round-2 cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S8"
    ],
    "spec_asserts": "MDPF_CANON PRD v2.10 @fa51c1f544 (round 2: M1, M5, M7/FWD-3, W1-S1); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-S8 confirmed and graduated INERT: json/portfolios/aum-timeseries.json has dead readers in portal/src/api and no live page caller at c96efe17. Removing them is a portal-repo act at the served key's retirement in the PRD's arc, not a round-2 cell.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-S8",
        "3.0.0_SA_CVO git grep in portal/src at c96efe17"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Graduated INERT to REMEDIATION_v2 for the retirement step's owner."
  },
  {
    "id": "MDPF_CANON-D1-C-S19",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:25:00Z",
    "one_line": "D1-S9 (BLOCKING) confirmed on this seat's own log read and graduated to the CTO's round-2 analysis. /aws/lambda/mdpf-gold-lambda 2026-10-10T13:30-13:31Z: global SCOPE FAILED (isolated), 'CROSS-AXIS COHERENCE GATE FAILED (global) -- REFUSING TO EMIT'; 'A7 reconciliation ERROR -- partition write SKIPPED'; 'gold parquet: PARTIAL -- built [inflection, cottonwood]'; 'cycle complete: 12/16 A4 objects built; errors=[global]'. No date=2026-10-09 partition exists for 49financial aum_metrics (404) or global aggregate_aua_timeseries (NoSuchKey). The 2026-10-09 13:31Z fire read 16/16 (row D1-S3), so this is new on the first fire after the round-1 and STRATID deploys. SERVED CONSEQUENCE: the 13:50Z publisher served global aggregate-aua-timeseries, aum-metrics, category-views and non-model-assets, and 49financial aggregate-aua-timeseries, aum-metrics and category-views, as of 2026-10-08. That is one trading day behind T-1 (Friday 2026-10-09). The producer failed closed: no wrong figure is served. CN-a-2 AC3 stays NOT MET on this read (C-S2, v1) and FWD-1 stays PARTIAL.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S9"
    ],
    "spec_asserts": "MDPF_CANON PRD v2.10 @fa51c1f544 (round 2: M1, M5, M7/FWD-3, W1-S1); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-S9 (BLOCKING) confirmed on this seat's own log read and graduated to the CTO's round-2 analysis. /aws/lambda/mdpf-gold-lambda 2026-10-10T13:30-13:31Z: global SCOPE FAILED (isolated), 'CROSS-AXIS COHERENCE GATE FAILED (global) -- REFUSING TO EMIT'; 'A7 reconciliation ERROR -- partition write SKIPPED'; 'gold parquet: PARTIAL -- built [inflection, cottonwood]'; 'cycle complete: 12/16 A4 objects built; errors=[global]'. No date=2026-10-09 partition exists for 49financial aum_metrics (404) or global aggregate_aua_timeseries (NoSuchKey). The 2026-10-09 13:31Z fire read 16/16 (row D1-S3), so this is new on the first fire after the round-1 and STRATID deploys. SERVED CONSEQUENCE: the 13:50Z publisher served global aggregate-aua-timeseries, aum-metrics, category-views and non-model-assets, and 49financial aggregate-aua-timeseries, aum-metrics and category-views, as of 2026-10-08. That is one trading day behind T-1 (Friday 2026-10-09). The producer failed closed: no wrong figure is served. CN-a-2 AC3 stays NOT MET on this read (C-S2, v1) and FWD-1 stays PARTIAL.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-S9",
        "3.0.0_SA_CVO logs filter-log-events /aws/lambda/mdpf-gold-lambda from 2026-10-10T13:00Z",
        "3.0.0_SA_CVO head-object opal-data-49financial mdpf/49financial/gold/aum_metrics/date=2026-10-09/data.parquet -> 404 (control: date=2026-10-08 -> 3922 B); get-object opal-data-mdpf global aggregate_aua_timeseries date=2026-10-09 and 2026-10-10 -> NoSuchKey (control: 2026-10-08 -> 85531 B)",
        "/aws/lambda/opal-assets-mdpf-portal-publisher 2026-10-10T13:50Z 'as-of 2026-10-08' lines"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Graduated BLOCKING to REMEDIATION_v2: whether the value-feed lag behind the global gate and the 49financial reconciliation guard are a project cell is the CTO's call at the round-2 analysis."
  }
]
```
