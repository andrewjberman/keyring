# ETFS_GUARDRAIL -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~B` at the L6 issuance (a seat row; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a worker's row is `ETFS_GUARDRAIL-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `ETFS_GUARDRAIL-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`ETFS_GUARDRAIL-C-S<k>`. **Append-only during the round.** Never edit an existing row.
**Round 1 task orders:** 14, one per cell of `../../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.1.1, on three worker
slots (`0.9.0_WK_ETFS_GUARDRAIL~1`, `~2`, `~3`).

```json
[
  {
    "id": "ETFS_GUARDRAIL-S1",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-04T19:05:00Z",
    "one_line": "EG-s-4: PRD s.7.4 homes the classifier in the ETFS layer and s.7.2 S4 binds its discriminator as 'read upstream partition + count priced' -- but the ETFS layer holds ZERO firm-bucket grants by explicit NEVER#1 design (reporter role: opal-data-etfs/* + the artifact prefix only; aggregation reader: daily/* + config/* only). L5 delegates the discriminator to the firm-scoped producers as a non-writing PROBE (EG-s-1/EG-s-2) and to the relied-on inf producer's own invoke answer; the classifier stays etfs-only and returns UNKNOWN where no probe answers; the one IAM change is an invoke grant on the reporter role (EG-s-7). No firm prefix is opened. Carried for the CTO's L10 read; not a spec edit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/etfs-reports/iam.tf:24-59 @291551ca2f -- the reporter instance role's policy: ReadEtfsAggregation (s3:GetObject opal-data-etfs/*), ListEtfsAggregation, WriteReports (platinum/reports/* only), PullRendererArtifact (opal-313476888478-lambda-artifacts/ec2/etfs-reports/*); no statement names opal-data-assets, opal-data-inf, opal-data-cot or opal-data-bd",
        "infra/aws/terraform/shared-infra/etfs-aggregation-iam.tf:1-60 @291551ca2f -- the AVGCAP reader role scoped to opal-data-etfs/daily/* + config/* with the header comment 'ZERO firm-bucket grants (NEVER#1: the metric layer never reads opal-data-inf / opal-data-cot / opal-data-schwab)'",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/prd/ETFS_GUARDRAIL_PRD.md s.7.2 row S4 and s.7.4 @4e30d6b635 -- the bound 'Discriminator = read upstream partition + count priced' and the home 'data/etfs/scripts/coverage/classifier.py ... importable by the renderer'; s.7.4's own clause 'These are step-4 PROPOSALS ... a decomp finding may overturn any of them'",
        "infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py:98-144 @291551ca2f and infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py:68-95 -- each owned producer already performs the discriminator on its own firm's partition (head_object on the date= partition; priced / rows count) under its own least-privilege role"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD s.7.2 S4 bound: 'Discriminator = read upstream partition + count priced'; s.7.4: 'S4 classifier -> data/etfs/scripts/coverage/classifier.py. One home, importable by the renderer.' Read together: the classifier, running in the ETFS layer on the reporter box, reads the three firms' upstream silver partitions.",
    "world_is": "The ETFS layer's principals (etfs-reports-reporter-role; etfs-avgcap-reader-role) hold no grant on any firm prefix, by a design that names NEVER#1 as its reason. Granting the reporter role s3 reads on blackdiamond/cottonwood/*, schwab/08242234/* and orion/inflection/* in opal-data-assets would mint the cross-firm reader that design refused. The producers already hold exactly the per-firm read the discriminator needs.",
    "notes": "L5/L6 resolution (decomposition v0.1.1 s.6a): probe mode on EG-s-1/EG-s-2; the inf producer's own invoke answer for Inflection; EG-s-4 etfs-only with an injected probe and UNKNOWN as an honest value; EG-s-7 holds the invoke and the one IAM Sid (lambda:InvokeFunction on three producer ARNs, reporter role, ledgered). If the CTO's L10 read prefers a data grant instead, that is a PRD addendum at L4 and the cells re-cut; nothing in this round opens a firm prefix. Disarm needs nothing: INERT, an OBSERVATION for the record."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S1",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-04T20:15:45Z",
    "one_line": "EG-s-3 AC1 bound 'the source's own battery is green at HEAD' is FALSE: test_catchup_scan.py crashes at import (KeyError: ASSETS_BUCKET) before it ever calls the real _catchup_missing_dates -- it was landed against the PRE-repoint shape and nobody re-vendored it across the 2026-08-02/03 repoint.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/test_catchup_scan.py@5376ecaa8b -- sets os.environ INF_BUCKET/HOLDINGS_PREFIX (not ASSETS_BUCKET/FACT_POSITIONS_PREFIX/META_DEDUP_PREFIX/CONFIG_KEY/OUTPUT_PREFIX/PARTNER) and calls lf._catchup_missing_dates(universe=[...], skip_date=...) with two kwargs against a real signature that takes three positional args (universe, all_dates, skip_date); it also monkeypatches lf._holdings_key_for/_holdings_exists/_compute_and_write_slice(src_key, universe), names lambda_function.py does not define at HEAD",
        "python -m pytest infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/test_catchup_scan.py -q run this turn @5376ecaa8b -- rc=2, '1 error during collection', KeyError: 'ASSETS_BUCKET' raised importing lambda_function.py:77, i.e. the module under test never finishes loading and _catchup_missing_dates is never invoked",
        "git log -1 --format=%H\\ %ad --date=iso 288bfe8378 -- (2026-08-01 15:50:34 -0400, test landed) vs 001a73530a -- (2026-08-03 18:01:50 -0400, 'complete the stranded COMMIT leg of the half-landed inf-etf deploy': introduces ASSETS_BUCKET/FACT_POSITIONS_PREFIX/META_DEDUP_PREFIX + dedup_core.py, i.e. the repoint the test predates and was never updated across",
        "infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py:74-84,271-295@5376ecaa8b -- the live env-var names and the live _catchup_missing_dates(universe, all_dates, skip_date) signature, both incompatible with the test's stubs and call"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO EG-s-3 THE CELL: 'Its own battery test_catchup_scan.py drives the REAL _catchup_missing_dates() unmodified with the S3 collaborators stubbed -- both arms (a hole found; nothing found) required.' Acceptance S3-AC1: 'the source's own battery is green at HEAD, both arms (record N passed).'",
    "world_is": "The battery does not run: it fails at module-import collection (rc=2, KeyError: 'ASSETS_BUCKET') before _catchup_missing_dates is ever called, because it stubs env vars and helper names from the PORT SOURCE's pre-2026-08-02/03-repoint shape. It has been dead since 001a73530a (2026-08-03), ~32 days, silently -- a regression in the real catch-up sweep since then would have gone uncaught by this fixture, which is precisely the failure mode INF_ETF_OWNERSHIP_SCHEDULED_FLOOR AC4p2 built it to catch.",
    "disarm_owner": "3.0.0_SA_CVO (routes the re-vendor: this order's bound is READ the port source and run its battery, not edit it -- 'PORT SOURCE. Relied on, NOT owned -- do not modify to suit the port'; fixing test_catchup_scan.py against the repointed shape is outside EG-s-3's write lane and outside this project's ownership of inf-pipeline)",
    "notes": "S3-AC1 is graded FAIL by output this turn (rc=2, not 'passed'); the TO's other four criteria (S3-AC2..AC5) are unaffected -- the port contract in the deliverable is built from a direct read of lambda_function.py's live bytes, not from the broken test's assumptions."
  }
]
```
