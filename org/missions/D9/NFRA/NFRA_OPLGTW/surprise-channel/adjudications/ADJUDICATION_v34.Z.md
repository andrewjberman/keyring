# NFRA_OPLGTW -- OG-ap-28 live: Z-S292 closed on the served read; AC3 held for an answer body (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v34. Fabric: site-z. Recorded: 2026-10-16 ~18:5xZ.
**Input:** `2.0.0_SA_COO~O` msg 35186 (acked). `deliverables/0.7.0_AE_CloudOps~Z/CODE2_SERVED.json` @59598f83c3, read for its `live_commit`,
`arms`, `arm_counts`, `limits` and `e4_regrade`. `live_commit` `bf9d23b518`, live since 17:57Z.

## Z-S292: CLOSED on the served read

My OG-ap-28 half set the condition: a master_admin stand-in call per live tool with rows above 0 through the dedicated role,
and a non-admin call refused with 0 reads. The `e12_bd49f_live` arm records exactly that:
- **Rows per tool:** `client_get_holdings` 34, `client_get_transactions` 2, `client_get_allocation` 7, `client_get_fees` 2.
- **Where they come from:** all four read bucket `opal-data-bd` from its newest dated file, through
  `gateway-49f-blackdiamond-live-read-role` (`e12_dedicated_role_on_all_four: true`).
- **The non-admin arm:** refused, with `e12_non_admin_s3_client_requests: 0`.
- **One expected extra read:** `client_get_allocation` also reads the assets-copy profile through the 49f role. That read is
  within that role's own two prefixes (OG-ap-24), so it is no widening.

The 49F live tools serve, on the dedicated role, to master_admin only. **Z-S292 is REMEDIATED** (Z-C-S81).

## AC3 of NFRA_OPLGTW.TO-OG-ap-28: NOT MEASURED until an answer body is read

**What AC3 asks:** do the first 49F Black Diamond live answers, and the unit, currency and floor fields, read as an analyst
would want? That means the data date stated, figures with units, and nothing merged across firms, graded on a real
master_admin call.

**What is on record:** `CODE2_SERVED.json` holds booleans and counts per arm.
- The `e4` re-grade shows `weight_unit` `fraction` and `currency_basis` `source_absent`, with `currency` null, on the 49F
  and SmartX rows.
- The 49F source carries no currency column.
- No answer body is on record. A field's value set is not a reading of an answer.

**This seat's instrument** (the opalgateway MCP on this box) has been down since ~09:0xZ (429). So AC3 closes on the same
route as round 37's OG-ev-1. The applier captures, from the live release, one projected body per 49F live tool for a single
account (holdings, transactions, allocation, fees), plus one news `coverage_floor` answer and one chatter answer with
`trading_days_behind_t1`.

**One instrument correction for that capture.** OG-ev-1's scrub hyphenated every run of 8 or more digits and comma-formatted
large numbers (`ev1_answer_bodies.py:42-67`, my v30 caution). That rewrites CUSIPs and figures, and figures with units are
exactly what AC3 reads. Mask account and person identifiers by key as before, but leave numeric values and security
identifiers as served, so the record shows the served bytes.

## Rows

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S81",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T18:50Z",
    "one_line": "Z-S292 REMEDIATED on the served read of release bf9d23b518: the four 49F live tools return rows (34/2/7/2) from opal-data-bd's newest dated file through gateway-49f-blackdiamond-live-read-role, and a non-admin is refused with 0 S3 requests; NFRA_OPLGTW.TO-OG-ap-28 AC3 is NOT MEASURED, because no answer body is on record (the capture should leave numbers and security ids unscrubbed).",
    "class": "OBSERVATION",
    "spec_asserts": "Z-S292's close (my OG-ap-28 half, condition 1): one master_admin call per live tool with rows above 0 through the dedicated role, and one non-admin call refused with 0 reads, on the served release.",
    "world_is": "CODE2_SERVED.json @59598f83c3, live_commit bf9d23b518: arm e12_bd49f_live true; e12_rows_per_tool holdings 34, transactions 2, allocation 7, fees 2; e12_all_four_bucket_opal_data_bd true; e12_all_four_newest_dated_file true; e12_dedicated_role_on_all_four true; e12_non_admin_refused true with 0 S3 client requests; e4 re-grade: weight_unit fraction, currency_basis source_absent, currency null on BD49F and SmartX. No answer body in the record.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S292"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~Z/CODE2_SERVED.json @59598f83c3 (arms, arm_counts, e4_regrade, limits)",
        "deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-ap-28_20261016.md @ffc2045889 (the condition)",
        "deliverables/0.7.0_AE_CloudOps~Z/ev1_answer_bodies.py:42-67 (the scrub that rewrites digits)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Z-S292 is closed by this row. It stays UNDER_INVESTIGATION only for TO-OG-ap-28 AC3, which closes on one real-call answer body per 49F live tool (plus one news floor and one chatter lag answer) read by this seat, captured with numbers and security ids left as served."
  }
]
```

-- 3.0.0_SA_CVO~Z
