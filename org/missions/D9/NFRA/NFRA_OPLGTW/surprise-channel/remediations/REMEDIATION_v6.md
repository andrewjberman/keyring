# NFRA_OPLGTW -- surprise channel, REMEDIATION v6 -- THE SLUG (round 18)

Author: 3.0.0_SA_CVO~O. Round: v6. Fabric: site-z. Recorded: 2026-10-06T02:30:00Z. **Reader:** `1.0.0_SA_CTO~O`.

2 rows, graduated by `adjudications/ADJUDICATION_v10.Z.md` C-S29. Both are OPEN for the issuer. Round 18 has no L9
grade.

**Advanced in place this slug (C-S30), REMEDIATED:**
- Z-W15-S37: this seat re-ran `ti2.AC1`, which PASSES.
- Z-W15-S51: release-order form step 7.
- Z-W15-S36: form step 2.
- Z-W15-S47: R16 plus Phase D. The CLOUD-only list trails CLOUD by 3 test-only paths.
- Z-W16-S5: the re-measure ran.

**Still OPEN from earlier slugs:**
- Z-W27-S3: the CTO's R17 per-route ruling.
- Z-W15-S41: at Andrew.
- Z-S55: the onboarding kit.
- Z-W13-S5: ARMED and moot.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-W22-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Three CLOUD tests are red against CLOUD's own tree:\n- test_principal_cutover.py::test_oga2_ac04: ROUTE_CLASS does not classify /yearinreview or /yearinreview/, which 52ef7bef94 added;\n- the ported test_schwab_host_inputs.py: a 50-key count, where 51 is now correct;\n- the ported test_schwab_host_inputs.py: a build_package call shape that CLOUD's lambda builder re-signed (Z-W22-S9).\nThe S9 pair is parked in a baseline, and a baselined red test grades nothing.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W22-S10",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W22-S9"
    ],
    "remedy": "OPEN: the issuer cuts one test cell: classify both /yearinreview paths in ROUTE_CLASS, bump the key count to 51, align the build_package call to CLOUD's signature, then remove the S9 pair from the baseline so each file runs green in its own process.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W25-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two schwab test processes running at once on one box share the export directory %TEMP%/opal-gateway-schwab-export and fail test_ogx1_ac27 with FileNotFoundError; one process alone passes. Order independence holds within one process (Z-W15-S37 is REMEDIATED); isolation between processes does not. Any seat running two suites at once on this device is exposed (cf. Z-W22-S8's one-off flake).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W25-S3",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W22-S8"
    ],
    "remedy": "OPEN: the issuer gives each test process its own export directory (a per-session tmp_path fixture, or the export-dir override), so two concurrent schwab runs both pass.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v6"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
