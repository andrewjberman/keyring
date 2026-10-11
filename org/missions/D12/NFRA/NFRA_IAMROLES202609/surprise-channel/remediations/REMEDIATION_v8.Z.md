# NFRA_IAMROLES202609 -- surprise channel, REMEDIATION v8 (site Z) -- THE ROUND-8 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-11 ~18:3xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 8: 2 of 2 complete, proofs VALID (`ledger/COMPLETION_REPORT.round8.json @be0536cad9`).

**L9** (`ADJUDICATION_v1.md`):
- **y-1 AC4 FAIL, narrow** (C-S42): the inbox check's fallback is year-pinned to 2026; one token fixes it, and it is
  INERT until 2027-01-01.
- **y-2 AC4 PASS** (C-S43): this seat exercised the sweep's uncontrolled FOREIGN arm (403 on two foreign names) and re-read
  all 7 ABSENT names at 404.

**For the analysis:**
1. Six ABSENT names carry live Allows that nobody decided (5 with write): ajb-workflow, opal-data-portal-s3,
   opal-data-schwab, opal-data-smartx-v2, opal-market-update, and opal-data-smartx (read only). These are round-9
   narrowing candidates.
2. `opal-data-schwab` reads 404, yet the `/49-schwab-conv` skill's description still names `s3://opal-data-schwab` as its
   sync target. Confirm the pipeline's real target before narrowing.
3. The sweep skipped three wildcard grants (`opal*`, `opal-*`, `opal-data-*`). `opal-data-*` grants on any future bucket
   by that prefix, a squatting class that `head-bucket` cannot classify.
4. The R20 bridge is carried (retire it when dell1's FWD-8 is in box/sitez).

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S42",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "/cloud-ops 18a's fallback limb counts unread mail with find -name '2026*.md', so from 2027-01-01 every waiting message is excluded; its line then equals an empty inbox's (unread=0 state_markers=3) and the check reads CLEAN",
    "evidence": [
      "ADJUDICATION_v1.md Z-C-S42: a planted 2027 message reads unread=0 state_markers=3, the same line the live empty inbox prints; the grammar form reads unread=1"
    ],
    "remedy": "Replace '2026*.md' with the filename grammar '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]T*.md' in both find calls, and add a planted-message control to the rule. One line in .claude/skills/cloud-ops/SKILL.md. INERT until 2027-01-01, and only on the broker-unreachable path.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S43",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "opal-market-data-v2 was deleted on Andrew's ruling (2026-07-30) and is tombstoned, but its Terraform declaration and one live Allow with write still name it; anyone who recreates the name inherits that grant",
    "evidence": [
      "Z-S43; DEAD_BUCKET_SWEEP.md section 4 (the 1 of 6 tombstones whose grant was not cleaned up); head-bucket 404 at ~18:2xZ"
    ],
    "remedy": "Remove the declaration (TF-debt A7) and the Allow in one never-widen pair; safe-apply already refuses the recreate.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v8"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
