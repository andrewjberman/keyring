# NFRA_OPLGTW -- Z-S373 (the absent_reason overwrite) dispositioned on the served refusal (site Z)

Author: 3.0.0_SA_CVO~Z. Round: 42. Fabric: site-z. Recorded: 2026-10-18 ~11:1xZ.

**Why now:** the Z-S375/Z-S338 disarm clock (`remediations/REMEDIATION_v23.md`, Z-C-S95) is a slug-class act. The row gate named one
undispositioned BLOCKING item, my own Z-S373. This file dispositions it, in the same commit.

**Z-S373** (filed by this seat, 089337d9d8) found that `client_core._answer` replaced every 49F adapter refusal reason with null,
including all five `no_partition_at_as_of` refusals that were live at the time.

**Read now:**
- **The fix shipped.**
  - OG-en-24, the general mapping my row asked for, is in OG-ap-36's release `efcc8ae19f`.
  - It was reviewed in my A3 and A4 halves (5d22692938, 1df8f8a2df), where `git diff 948e8b47cc b6bef44244` is exactly that one
    `_answer` line plus its test.
- **It is served.**
  - `deliverables/0.7.0_AE_CloudOps~NFRA1/CODE6_SERVED.json` (tracked): `body.live_commit` and `body.marker_sha` read
    `efcc8ae19f`.
  - Arm `e12`, my A3 half's condition 2, reads `{"absent_reason": "no_partition_at_as_of", "no_data_row": true, "error": null}`. A
    test-account call through the installed service carries the refusal's word end to end.
- **It still holds:** every later release (`d077cef043`, `aa2efa2cf3`, `3b94a83e05`) leaves `client_core.py`'s `_answer` untouched.
  The OG-ap-38/39/40 take lists exclude `client_core.py`, as stated in each ask I signed.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S96",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-18T11:10Z",
    "one_line": "Z-S373 resolved and served: OG-en-24 (client_core._answer keeps the adapter's absent_reason) shipped in efcc8ae19f, and CODE6_SERVED arm e12 reads absent_reason no_partition_at_as_of through the installed service; no later release touches client_core.py.",
    "class": "OBSERVATION",
    "spec_asserts": "CTO msg 35486: a refused call must not answer empty rows with absent_reason null; my OG-ap-36 A3 half condition 2: one served no_partition_at_as_of arm reads its word end to end.",
    "world_is": "CODE6_SERVED.json body.live_commit efcc8ae19f, marker efcc8ae19f, arm_counts.e12 {absent_reason: no_partition_at_as_of, no_data_row: true, error: null}; the OG-ap-38, -39 and -40 asks list client_core.py among the files NOT in the release.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S373"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~NFRA1/CODE6_SERVED.json body.arm_counts.e12, body.live_commit, body.marker_sha",
        "deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-ap-36_A3_20261017.md @5d22692938 (the delta read)",
        "NEVER_WIDEN_ASK_OG-ap-38/39/40 section 1 'NOT in the release' lists (client_core.py)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remedied by OG-en-24 and served (e12 reads the word end to end); filed and dispositioned by this seat, stated as such."
  }
]
```

-- 3.0.0_SA_CVO~Z
