# NFRA_CTLPLN: CVO L8 dispositions at the round-9 drain (2026-10-12)

L8 by `3.0.0_SA_CVO~L` (laptop), on 2.0.0_SA_COO~C msg 108534. HEAD e08f8332a9.

`round-close-check --round 9` reads 2 of 2 judgments graded (C-S16 and C-S17, carried), proof_bad 0, MAY-CLOSE. Two gating
items were undispositioned:
- **S9112 GRADUATED** (C-S34; row in `remediations/REMEDIATION_v3.md`). It stays ARMED and its disarm is Andrew's.
- **W70-S1 DISMISSED** (C-S35).

All 66 gating items are now dispositioned. The round's OBSERVATION/INERT rows (W70-S2, W70-S3, W71-S1..S3, D1-S11) gate
nothing. They are noted, not dispositioned.

<sweep_watermark>2026-10-12T12:35Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S34",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T12:35Z",
    "one_line": "S9112 GRADUATED: the data proxy's log group still holds refresh_token and device_trust cookies logged before the CT-w-10 fix; retention is 14 days; the purge and the token invalidation are Andrew's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "No credential material is kept in a function's logs.",
    "world_is": "CT-w-10 (@e08f8332a9) is live; the issuer read 27 post-apply events with Bearer 0, JWT 0, cookie 0. That stops new lines and leaves the old ones. This seat read the group's metadata only (no event): /aws/lambda/opal-portal-data-proxy retentionInDays 14, storedBytes 212029. The pre-apply events therefore age out by about 2026-10-26. Until then the refresh tokens (7-day expiry) and device-trust tokens (30-day window) in them are treated as live, as the row says, since no value was tested.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.md row S9112 (0.7.0_AE_CloudOps~U7)",
        ".tools/aws logs describe-log-groups --log-group-name-prefix /aws/lambda/opal-portal-data-proxy, 2026-10-12 ~12:3xZ",
        "2.0.0_SA_COO~C msg 108534"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-S9112"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_CTLPLN-C-S35",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T12:35Z",
    "one_line": "W70-S1 resolved by AMENDMENT 1 of CT-w-8: 49financial had no comment at base 2ed4373d, so three firm rows carry a note and CTw8-AC2 expects 3; the issuer re-ran it and closed the order.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "W70-S1 (BLOCKING): CTw8-AC2 expected four notes; three exist.",
    "world_is": "TO-CT-w-8 AMENDMENT 1 (issuer, ~11:1xZ) rules that the premise was wrong: 38 comment lines across three firms (inflection 4, cottonwood 11, demo 23), equal to the old literal's 38. CTw8-AC2 now reads `grep -c '\"note\"' ... expect 3`. The order is complete @2a978fab00 with AC2 re-run to 3, suites 96/16/5, proof VALID.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-w-8.firm-pages-note-field-and-comments.md lines 9, 46-47, 55",
        "git show -s 2a978fab00"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W70-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The issuer amended the expectation to the measured truth and the order closed on it."
  }
]
```
