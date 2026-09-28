# NFRA_MCPINDEX ROUND 2 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~O`. **Written:** 2026-09-28T15:00:22Z. **Terminality:** every order is terminal. `2.0.0_SA_COO~O`
closed the last one @4ce47993e4 on Andrew's word ('close out each project's round so the CVO can slug'): MX-s-10
PHASE A is issuer-graded (A6 @471c840a0a), and PHASE B re-cuts after this slug.

Input: `investigations/INVESTIGATION_v1.md`, 93 rows, 42 undispositioned (41, plus Z-S47 at 13:48Z). This seat
re-measured every remedy it marks REMEDIATED.

Carried and not re-graded: the C-S13 remediation row (REMEDIATION_v1) still reads OPEN. Its bar is re-measured here:
silver/bd_assets_dim.parquet is current (VersionId kittUyy..., 12:22:57Z), with 12,141 unique asset_ids and 1,184
null or blank cusip (9.75%). The row is append-only, so the flip is the round-3 analysis's.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S22",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T15:00:22Z",
    "one_line": "Round 2 L8: 22 rows DISMISSED_WITH_REASON -- issuer disarm records whose targets are already terminal, method records of workers, and blockers the issuer re-routed or ruled inside its own decomposition. None carries a residual hazard.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Records: Z-S2 and Z-S7 are the issuer's disarm records for W3-S11 and W2-S7, both already terminal via Z-S14. Re-routed or ruled: Z-S30 was ruled by MX-s-4 A5 @fc2001d2a6 (option (c): step 1 left the order, the REST pull became the CTO design cell, built as MX-s-9/MX-s-6); Z-S45 was ruled by MX-s-10 A5 @64bb58d8b8 (no new policy, the ARN added to the existing AdditionalPermissions statement), and that grant is LIVE (re-read below). Worker method records, each measured and stated in its own row: Z-W1-S1, -S2, -S4, -S5 (MX-c-5 probe conform, graded at MXC5-AC4); Z-W2-S3 (latest_value carries its claim held/absent), -S4 (no-egress.invalid), -S6 (query_v0 named as the next call); Z-W2-S9 (the real-ask population is thin: 3 of 27 target a dataset -- a stated limit, not a defect); Z-W3-S5 (tool_prefix read only by summary()); Z-W3-S9 (a stale worker base, read at CLOUD); Z-W3-S13 (7 portal_* source files removed, recoverable from 6345d36f04); Z-W4-S1 (rep ids through INF_E_00's join, 0 of 787 outside the allowlist). Resolved in round: Z-W3-S2 (the catalog was regenerated @bc0cde67f0, 3 emitted, 0 refused); Z-W3-S6 (portal_index is in the tree @bc0cde67f0 under the R-3 legacy-read waiver); Z-W3-S8 (the etfs entry left scope with Z-S2's cut to 3 mdpf tools). Carried as constraints on a later cell, not defects today: Z-W1-S3 (a cell that adds the `tools` manifest must add catalog refs in the same commit or the integration de-registers); Z-W1-S6 (the 49-name denominator excludes 5 registered tools, all SAFE today); Z-W2-S5 (the discover tools' catalog ref is not an entity id).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#(each id above)",
        "commits fc2001d2a6, 64bb58d8b8, bc0cde67f0, 2c25c4c831",
        "aws iam get-role-policy bd-exporter-ec2-role AdditionalPermissions, read by this seat 2026-09-28, before 14:56Z: carries blackdiamond/49f/session"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S2",
      "NFRA_MCPINDEX-Z-S7",
      "NFRA_MCPINDEX-Z-S30",
      "NFRA_MCPINDEX-Z-S45",
      "NFRA_MCPINDEX-Z-W1-S1",
      "NFRA_MCPINDEX-Z-W1-S2",
      "NFRA_MCPINDEX-Z-W1-S3",
      "NFRA_MCPINDEX-Z-W1-S4",
      "NFRA_MCPINDEX-Z-W1-S5",
      "NFRA_MCPINDEX-Z-W1-S6",
      "NFRA_MCPINDEX-Z-W2-S3",
      "NFRA_MCPINDEX-Z-W2-S4",
      "NFRA_MCPINDEX-Z-W2-S5",
      "NFRA_MCPINDEX-Z-W2-S6",
      "NFRA_MCPINDEX-Z-W2-S9",
      "NFRA_MCPINDEX-Z-W3-S2",
      "NFRA_MCPINDEX-Z-W3-S5",
      "NFRA_MCPINDEX-Z-W3-S6",
      "NFRA_MCPINDEX-Z-W3-S8",
      "NFRA_MCPINDEX-Z-W3-S9",
      "NFRA_MCPINDEX-Z-W3-S13",
      "NFRA_MCPINDEX-Z-W4-S1"
    ],
    "dismissal_reason": "Each row is a record, a ruled or re-routed blocker whose act completed, or a constraint carried to the enrichment list by the slug; none holds a hazard a remediation row would own."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S23",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T15:00:22Z",
    "one_line": "Round 2 L8: 8 rows GRADUATED and REMEDIATED inside the round, each re-read by this seat: the recorder's encoding, the asset-dim dependency closure, the 49F session grant, the Z-S46 regression, and the two gateway wiring gaps (factory registration and data_entitlement class) for opal_discover and portal_index.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Z-S12: record-terraform-deploy.sh:259 now reads `open(source_map_path, encoding='utf-8')` (@981d0e931c). Z-S43: the document @0ff972bc38 stages the producer tree with lib/silver_ids.py, lib/trading_calendar.py and the MX-s-11 generated pin, and step 2 ran to DELTA=0 (ssm:0626f927). Z-S44: the live role policy AdditionalPermissions carries blackdiamond/49f/session. Z-S46: the S3 versions of silver/bd_assets_dim.parquet read 06:22:06 a218b3dd, 12:04:24 83ae55e0 (the regression), 12:08:43 a218b3dd (restored), 12:22:57 a33f5eef (step 2), and the document refuses the bare path (rc 92). The consumers of the 4m19s window are NOT measured, as the row itself states. Z-W2-S1 and Z-W3-S3: registry.py:60-61 registers portal_index and opal_discover. Z-W2-S2 and Z-W3-S1: data_entitlement.py:114-115 classifies the 3 mdpf portal tools and both discover tools.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/record-terraform-deploy.sh:259",
        "infra/aws/ssm/opal-bd-asset-dim-download.json@0ff972bc38",
        "s3api list-object-versions opal-data-bd silver/bd_assets_dim.parquet, read by this seat 12:5xZ",
        "infra/aws/ec2/opal-gateway/app/integrations/registry.py:60-61; infra/aws/ec2/opal-gateway/app/data_entitlement.py:114-115"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S12",
      "NFRA_MCPINDEX-Z-S43",
      "NFRA_MCPINDEX-Z-S44",
      "NFRA_MCPINDEX-Z-S46",
      "NFRA_MCPINDEX-Z-W2-S1",
      "NFRA_MCPINDEX-Z-W2-S2",
      "NFRA_MCPINDEX-Z-W3-S1",
      "NFRA_MCPINDEX-Z-W3-S3"
    ]
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S24",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T15:00:22Z",
    "one_line": "Round 2 L8: 12 rows GRADUATED and OPEN. Two hold the live Black Diamond credential (Z-S29, Z-S31), two hold the unscheduled asset dim and the false-success fees producer that MX-s-10 PHASE B retires (Z-S42, Z-S47), and eight are standing code or tooling defects.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Z-S31, RE-MEASURED by this seat with the row's own detector and without reading Secrets Manager or printing any value: over 42,435 tracked text files, the live fingerprint (len 11, sha256 prefix 161ff0eb3831) occurs 6 times in 6 files AT HEAD. Four are shell scripts that carry it as the DEFAULT of BD_PASSWORD (bd-exporter/src/stepwise/run-daily-downloads.sh, run-backfill.sh, run-allocation-backfill.sh, historical-backfill-2014-2020.sh); two are docs (bd-exporter/docs/PARALLEL_BACKFILL.md, terraform/QUICK_COMMANDS.md). A shape-regex positive control matched. So the value-out-of-tracked-files half is NOT met, and a working-tree count of 0 reported elsewhere does not hold for this fingerprint. The superseded Z-S29 value (7c3755be9e80) reads 0. Z-S29 stays open on rotation, which is Andrew's act; the history is unpurged. Z-S42 and Z-S47: PHASE A built the REST document; PHASE B (the DEFAULT switch and the fees-leg retirement, signed @73e884bbbb) re-cuts after this slug. Still present at HEAD: Z-S22 (record-terraform-deploy.sh:218 hardcodes /c/Users/AndrewBerman/.bun/bin/bun); Z-S24 (convert_assets_to_silver.py:153 `dtype == object`, latent on pandas 3); Z-W5-S1 (commit_gate_lib.sh stages a present path with git add -f, so a --cached removal cannot commit); Z-W7-S2 (the CHANGELOG writer is still a temp Node script, record-terraform-deploy.sh:570). Z-W4-S2: gold/canonical/lots_unrealized and lots_realized still end at 2026-07-23 (read today). Z-W2-S8 (discover routing: 0 of 3 dataset asks route first), Z-W3-S4 (portal rows sit under a silver-dataset header, 4 mdpf objects with 2 rows) and Z-W3-S12 (pytest_named misreads capsys.disabled output) have no fixing commit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's scan: git ls-files (45,152), 42,435 text files scanned, tokens of shape [A-Z][a-z]{7}[0-9]{3} hashed, 6 hits at HEAD bytes; no value printed or stored",
        "infra/aws/lambda/ci/record-terraform-deploy.sh:218, :570; data/black_diamond/scripts/silver/convert_assets_to_silver.py:153; .tools/commit_gate_lib.sh:95-110",
        "s3api list-objects-v2 opal-data-bd gold/canonical/lots_unrealized/ and lots_realized/: newest 2026-07-23.parquet",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_MCPINDEX_MX-s-10_NEVER_WIDEN_SECOND_HALF_20260928.md@73e884bbbb"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S22",
      "NFRA_MCPINDEX-Z-S24",
      "NFRA_MCPINDEX-Z-S29",
      "NFRA_MCPINDEX-Z-S31",
      "NFRA_MCPINDEX-Z-S42",
      "NFRA_MCPINDEX-Z-S47",
      "NFRA_MCPINDEX-Z-W2-S8",
      "NFRA_MCPINDEX-Z-W3-S4",
      "NFRA_MCPINDEX-Z-W3-S12",
      "NFRA_MCPINDEX-Z-W4-S2",
      "NFRA_MCPINDEX-Z-W5-S1",
      "NFRA_MCPINDEX-Z-W7-S2"
    ]
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S25",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T15:00:22Z",
    "one_line": "L9 grade, MX-s-4 AC4 (judgment, WORLD): PASS with one limit. The asset-dim wrapper reports a failed run as SSM Failed, re-read here live on both the real failure and the planted ordering probe.",
    "class": "OBSERVATION",
    "spec_asserts": "AC4: the wrapper reports a failed download or merge as a non-zero exit (SSM Failed); show a real or planted failure's SSM status.",
    "world_is": "This seat's own live reads. ssm get-command-invocation 9ba8d9c9 (opal-bd-asset-dim-download, 2026-09-26T23:32:14Z) returns Status Failed, ResponseCode 1, and its output carries 'Asset-dim pipeline failed'. The same failure under the prior document had recorded Success. e77e84c7 (AWS-RunShellScript carrying the live v3 lines, 2026-09-27T22:15:03Z) returns Failed rc 1, with 'Shutting down' printed BEFORE the error line, so the shutdown is armed before the exit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws ssm get-command-invocation --command-id 9ba8d9c9-6759-4a4c-a1ac-d571abcde94f and e77e84c7-6e1f-4772-9dae-d00dc52b9965, instance i-0e6f6dc014fdcf1cd, read by this seat 2026-09-28, before 14:56Z",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/NFRA_MCPINDEX.TO-MX-s-4.bd-asset-dim-login.proof_of_spec.json@81c13ee0f9 (proof-of-spec-check VALID rc=0 on this seat's run)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "MXS4-AC4",
        "instance": "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/NFRA_MCPINDEX.TO-MX-s-4.bd-asset-dim-login.proof_of_spec.json@81c13ee0f9",
        "verdict": "PASS",
        "reason": "A real failure under the new document reads SSM Failed rc 1 where the identical failure under the old one read Success. That discriminates, and it is the organic case. Limit: the exit-after-shutdown ORDERING is proven only by a planted probe that ran the document's lines under AWS-RunShellScript, not by a fire of the named document itself. The MX-s-10 document @0ff972bc38 keeps that same order (shutdown armed before the failure exit), read here. The fees document has no exit at all (Z-S47), which is outside AC4."
      }
    ]
  }
]
```

-- 3.0.0_SA_CVO~O
