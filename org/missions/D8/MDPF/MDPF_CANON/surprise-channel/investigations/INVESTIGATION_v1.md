# MDPF_CANON -- surprise channel, INVESTIGATION v1 (round 1, dell1). Append-only; rows below are validated by `.tools/surprise-row-gate.py` at commit.

```json
{
  "id": "MDPF_CANON-D1-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-09T18:54:16Z",
  "one_line": "Three data/mdpf/scripts/gold/tests/test_global_fold_flag2.py cases fail at box/dell1 before any MDPF_CANON change (carried vs measured label; 128.0 vs 120.0) -- a pre-existing red in the global fold's tests, not this project's.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D1 (routes it to the global fold's owner; last commits 0.4.0_DS_ClientPlatform 0d653d4aa3/e56eef609e/4ed8a19775)",
  "spec_asserts": "A round's regression criterion runs the gold tests and expects 0 failed.",
  "world_is": "python -m pytest data/mdpf/scripts/gold/tests -q at box/dell1 (2026-10-09 ~18:5xZ): 3 failed, 94 passed -- test_carry_within_window_carries_and_labels, test_carry_beyond_window_absent_for_real, test_carry_source_is_measured_never_interpolated. Round 1's AC2 deselects exactly these three by node id so the project's own regressions stay visible.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest data/mdpf/scripts/gold/tests -q (3 failed, 94 passed)",
      "git log -- data/mdpf/scripts/gold/tests/test_global_fold_flag2.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed at L5 by the issuer; no cell of this project owns the global fold."
}
```

```json
{
  "id": "MDPF_CANON-D1-W1-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~1",
  "surfaced_at": "2026-10-09T19:08:20Z",
  "one_line": "CN-a-1 names the composite bucket as scope_bucket['global'], but that map entry is opal-data-portal-v2; address(mdpf, global, gold, ...) puts the composite gold in opal-data-mdpf. The build uses local.mdpf_bucket (opal-data-mdpf).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-a-1 item 2: the gold Lambda's Put/Get on mdpf/global/gold/<artifact>/* is in the composite bucket 'from the module's scope_bucket for scope global, never typed'; the same item and AC1 arm 4 name that bucket opal-data-mdpf.",
  "world_is": "infra/aws/terraform/modules/opal_name/generated_locals.tf scope_bucket[\"global\"] = \"opal-data-portal-v2\"; lib/opal_naming.py address(\"mdpf\",\"global\",\"gold\",\"aum_metrics\",\"date=2026-10-08\") = s3://opal-data-mdpf/mdpf/global/gold/aum_metrics/date=2026-10-08. Following the map literally would grant the four prefixes in opal-data-portal-v2, a bucket the parquet emitter never writes. iam.tf uses the existing local.mdpf_bucket (main.tf:56, the same local the TAXSMA control grant uses at mdpf_gold_taxsma). r1_iam.py arm 4 does not read the bucket and passes either way; the bucket is not typed in the new block.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/modules/opal_name/generated_locals.tf@155ac2ce67 scope_bucket global",
      "python -c address('mdpf','global','gold','aum_metrics','date=2026-10-08')",
      "infra/aws/terraform/mdpf-pipeline/main.tf:56 mdpf_bucket"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```
