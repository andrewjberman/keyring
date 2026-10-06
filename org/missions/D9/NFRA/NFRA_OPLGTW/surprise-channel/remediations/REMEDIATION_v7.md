# NFRA_OPLGTW -- surprise channel, REMEDIATION v7 -- THE SLUG (round 19)

Author: 3.0.0_SA_CVO~O. Round: v7. Fabric: site-z. Recorded: 2026-10-06T05:55:00Z. **Reader:** `1.0.0_SA_CTO~O`.

1 row, graduated by `adjudications/ADJUDICATION_v11.Z.md` C-S32. It is OPEN for the issuer. Round 19 has no L9 grade.

**Advanced in place this slug (C-S33), REMEDIATED, each on this seat's own run on CLOUD:**
- Z-W22-S10: two test files pass, 11 and 9.
- Z-W25-S3: `ts2.AC2`, with 30 concurrent export runs and 0 FileNotFoundError.

**Still OPEN from earlier slugs:**
- Z-W27-S3: the CTO's R17 per-route ruling.
- Z-W15-S41: at Andrew.
- Z-S55: the onboarding kit.
- Z-W13-S5: ARMED and moot.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-W15-S58",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "tests/test_schwab_export_stream.py::test_ogx2_ac01 is intermittent on this device on both live 37be3485db and the release tree (job_failed in the export stream): identical re-runs flip it. A baseline therefore reads 7 or 8 failing ids by chance, and a one-id release-vs-baseline difference cannot be graded as a regression or ruled out as one.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S58",
      "deliverables/0.9.0_WK_NFRA_OPLGTW~15/r19b_tests_baseline.out, r19b_tests_release.out"
    ],
    "remedy": "OPEN: the issuer cuts a cell that finds why the export-stream job fails intermittently (timing, the shared export path, or the engine deadline) and makes test_ogx2_ac01 deterministic, then removes it from any baseline; until then the baseline names it as FLAKY, not as failing.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v7"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~O
