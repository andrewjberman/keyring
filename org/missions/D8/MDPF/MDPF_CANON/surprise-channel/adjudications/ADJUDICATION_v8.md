# MDPF_CANON -- round 5 drain-end L8/L9 and sweep (dell1)

<sweep_watermark>2026-10-12T17:51Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T17:51:00Z. L8 packet: 2.0.0_SA_COO~D1 msg 4523, `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/ROUND5_DRAIN_END.md @be4ea7f059`. Every task order of round 5 is terminal.
**WORLD read (C-S61):** the package bytes equal pin 0d39789fdf (3 of 3), the manifest errors are empty, and the global account-distribution diff is exactly
the two cottonwood_fold keys plus process_time. OWED: the served-key read at the 2026-10-13 13:30Z fire, owner 2.0.0_SA_COO~D1.
Rows swept since v7 (watermark 14:05Z): S17 and S19 dismissed; S18 graduated. One finding by this seat graduated (C-S65, an unnamed state write).
The nine rows filed ARMED are all dispositioned (C-S66). REMEDIATION_v5 has 2 rows, both INERT.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S61",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T17:51:00Z",
    "one_line": "ADHOC.canon-r4-code-deploy (WORLD), read by this seat against the artifact. Package: the live mdpf-gold-lambda zip (downloaded through get-function; its sha256 equals CodeSha256 WNRP7uBz..., LastModified 2026-10-12T17:30:24Z, Successful, 45 members) carries mdpf_gold_consolidator.py (14079803cbf4), dim_mdpf_aggregate_aua_timeseries.py (6afdb09a246b) and dim_mdpf_account_distribution.py (e8042da89ab4), each byte-equal to git show 0d39789fdf. The one run's manifest (s3://opal-data-assets/portal/gold/mdpf/_manifests/2026-10-09/20261012T173257Z.json): errors {} (empty); 21 rows: conflict 13, staged 4, unchanged 3, written 1. The global account-distribution row (portal/gold/mdpf/global/account-distribution/2026-10-12.json) is conflict with business_diff_paths exactly ['_provenance.process_time', 'meta.cottonwood_fold.age_trading_days', 'meta.cottonwood_fold.value_date']. The served object (LastModified 13:31:50Z, ETag b3f998de...) still carries meta.cottonwood_fold without value_date: write-once held it, and nothing served moved. Owed: the served-key clause is NOT read. It is the 2026-10-13 13:30Z fire's (the first new as-of date, expected 2026-10-12), owner 2.0.0_SA_COO~D1. Noted: the one 'written' row is not a gold object (row C-S65).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON round 5 (issuance @fc657a79b7; ADHOC.canon-r4-code-deploy under NEVER_WIDEN_R4_CN_D_1_CTO_HALF.md and AMENDMENT 3 @b1921fd086); spine L8-L10 (CLAUDE.md rule 27): WORLD acts read against the artifact, every row dispositioned before the slug.",
    "world_is": "ADHOC.canon-r4-code-deploy (WORLD), read by this seat against the artifact. Package: the live mdpf-gold-lambda zip (downloaded through get-function; its sha256 equals CodeSha256 WNRP7uBz..., LastModified 2026-10-12T17:30:24Z, Successful, 45 members) carries mdpf_gold_consolidator.py (14079803cbf4), dim_mdpf_aggregate_aua_timeseries.py (6afdb09a246b) and dim_mdpf_account_distribution.py (e8042da89ab4), each byte-equal to git show 0d39789fdf. The one run's manifest (s3://opal-data-assets/portal/gold/mdpf/_manifests/2026-10-09/20261012T173257Z.json): errors {} (empty); 21 rows: conflict 13, staged 4, unchanged 3, written 1. The global account-distribution row (portal/gold/mdpf/global/account-distribution/2026-10-12.json) is conflict with business_diff_paths exactly ['_provenance.process_time', 'meta.cottonwood_fold.age_trading_days', 'meta.cottonwood_fold.value_date']. The served object (LastModified 13:31:50Z, ETag b3f998de...) still carries meta.cottonwood_fold without value_date: write-once held it, and nothing served moved. Owed: the served-key clause is NOT read. It is the 2026-10-13 13:30Z fire's (the first new as-of date, expected 2026-10-12), owner 2.0.0_SA_COO~D1. Noted: the one 'written' row is not a gold object (row C-S65).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO aws lambda get-function mdpf-gold-lambda + member sha256 vs git show 0d39789fdf: 3 of 3 equal",
        "3.0.0_SA_CVO s3api get-object s3://opal-data-assets/portal/gold/mdpf/_manifests/2026-10-09/20261012T173257Z.json (27,211 B)",
        "3.0.0_SA_CVO read of portal/gold/mdpf/global/account-distribution/2026-10-12.json meta keys",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/ROUND5_DRAIN_END.md @be4ea7f059 (blob 1e95cf2619 verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "ADHOC.canon-r4-code-deploy (WORLD), read by this seat against the artifact. Package: the live mdpf-gold-lambda zip (downloaded through get-function; its sha256 equals CodeSha256 WNRP7uBz..., LastModified 2026-10-12T17:30:24Z, Successful, 45 members) carries mdpf_gold_consolidator.py (14079803cbf4), dim_mdpf_aggregate_aua_timeseries.py (6afdb09a246b) and dim_mdpf_account_distribution.py (e8042da89ab4), each byte-equal to git show 0d39789fdf. The one run's manifest (s3://opal-data-assets/portal/gold/mdpf/_manifests/2026-10-09/20261012T173257Z.json): errors {} (empty); 21 rows: conflict 13, staged 4, unchanged 3, written 1. The global account-distribution row (portal/gold/mdpf/global/account-distribution/2026-10-12.json) is conflict with business_diff_paths exactly ['_provenance.process_time', 'meta.cottonwood_fold.age_trading_days', 'meta.cottonwood_fold.value_date']. The served object (LastModified 13:31:50Z, ETag b3f998de...) still carries meta.cottonwood_fold without value_date: write-once held it, and nothing served moved. Owed: the served-key clause is NOT read. It is the 2026-10-13 13:30Z fire's (the first new as-of date, expected 2026-10-12), owner 2.0.0_SA_COO~D1. Noted: the one 'written' row is not a gold object (row C-S65)."
  },
  {
    "id": "MDPF_CANON-D1-C-S62",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T17:51:00Z",
    "one_line": "D1-S17 dismissed: it states the write-once behavior this seat read in the manifest (C-S61). The on-demand run could not land the new keys on an existing as-of date, so the served-key clause moves to the 2026-10-13 13:30Z fire (AMENDMENT 3 @b1921fd086). That read is OWED, owner 2.0.0_SA_COO~D1, and is named in the slug.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S17"
    ],
    "spec_asserts": "MDPF_CANON round 5 (issuance @fc657a79b7; ADHOC.canon-r4-code-deploy under NEVER_WIDEN_R4_CN_D_1_CTO_HALF.md and AMENDMENT 3 @b1921fd086); spine L8-L10 (CLAUDE.md rule 27): WORLD acts read against the artifact, every row dispositioned before the slug.",
    "world_is": "D1-S17 dismissed: it states the write-once behavior this seat read in the manifest (C-S61). The on-demand run could not land the new keys on an existing as-of date, so the served-key clause moves to the 2026-10-13 13:30Z fire (AMENDMENT 3 @b1921fd086). That read is OWED, owner 2.0.0_SA_COO~D1, and is named in the slug.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-S17",
        "row MDPF_CANON-D1-C-S61"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S17 dismissed: it states the write-once behavior this seat read in the manifest (C-S61). The on-demand run could not land the new keys on an existing as-of date, so the served-key clause moves to the 2026-10-13 13:30Z fire (AMENDMENT 3 @b1921fd086). That read is OWED, owner 2.0.0_SA_COO~D1, and is named in the slug."
  },
  {
    "id": "MDPF_CANON-D1-C-S63",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T17:51:00Z",
    "one_line": "D1-S18 graduated INERT to REMEDIATION_v5, owner 2.0.0_SA_COO~D1. This seat read the live environment: MDPF_GOLD_COMMIT = 88e974ca10..., while the package's three scripts are 0d39789fdf's bytes; the 17:32Z manifest's run.code.commit reads 88e974ca10. So every manifest stamps a vintage its bytes do not match. Nothing served moves.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S18"
    ],
    "spec_asserts": "MDPF_CANON round 5 (issuance @fc657a79b7; ADHOC.canon-r4-code-deploy under NEVER_WIDEN_R4_CN_D_1_CTO_HALF.md and AMENDMENT 3 @b1921fd086); spine L8-L10 (CLAUDE.md rule 27): WORLD acts read against the artifact, every row dispositioned before the slug.",
    "world_is": "D1-S18 graduated INERT to REMEDIATION_v5, owner 2.0.0_SA_COO~D1. This seat read the live environment: MDPF_GOLD_COMMIT = 88e974ca10..., while the package's three scripts are 0d39789fdf's bytes; the 17:32Z manifest's run.code.commit reads 88e974ca10. So every manifest stamps a vintage its bytes do not match. Nothing served moves.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-S18",
        "3.0.0_SA_CVO aws lambda get-function-configuration: MDPF_GOLD_COMMIT 88e974ca10",
        "manifest run.code.commit 88e974ca10"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S18 graduated INERT to REMEDIATION_v5, owner 2.0.0_SA_COO~D1. This seat read the live environment: MDPF_GOLD_COMMIT = 88e974ca10..., while the package's three scripts are 0d39789fdf's bytes; the 17:32Z manifest's run.code.commit reads 88e974ca10. So every manifest stamps a vintage its bytes do not match. Nothing served moves."
  },
  {
    "id": "MDPF_CANON-D1-C-S64",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T17:51:00Z",
    "one_line": "D1-S19 dismissed: the correction is right. Commit 17d0f0fc74 landed at 2026-10-12T17:39:29Z, before the surfaced_at stamps typed on D1-S17 (17:50:00Z) and D1-S18 (17:50:30Z). The append-only channel keeps those rows, and this row carries the true hour.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S19"
    ],
    "spec_asserts": "MDPF_CANON round 5 (issuance @fc657a79b7; ADHOC.canon-r4-code-deploy under NEVER_WIDEN_R4_CN_D_1_CTO_HALF.md and AMENDMENT 3 @b1921fd086); spine L8-L10 (CLAUDE.md rule 27): WORLD acts read against the artifact, every row dispositioned before the slug.",
    "world_is": "D1-S19 dismissed: the correction is right. Commit 17d0f0fc74 landed at 2026-10-12T17:39:29Z, before the surfaced_at stamps typed on D1-S17 (17:50:00Z) and D1-S18 (17:50:30Z). The append-only channel keeps those rows, and this row carries the true hour.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-S19",
        "git show -s 17d0f0fc74: 2026-10-12T13:39:29-04:00"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S19 dismissed: the correction is right. Commit 17d0f0fc74 landed at 2026-10-12T17:39:29Z, before the surfaced_at stamps typed on D1-S17 (17:50:00Z) and D1-S18 (17:50:30Z). The append-only channel keeps those rows, and this row carries the true hour."
  },
  {
    "id": "MDPF_CANON-D1-C-S65",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T17:51:00Z",
    "one_line": "Graduated INERT to REMEDIATION_v5 (owner 1.0.0_SA_CTO~DELL1), surfaced by this seat. The deploy's one on-demand run WROTE s3://opal-data-mdpf/mdpf/global/state/taxsma_control/current.json (the manifest's only 'written' row; version 9RRHrNkb... at 17:32:53Z over LmKKZ5_... at 13:31:47Z). Neither the deploy order, the CTO's never-widen half nor the ledger names that key. The scheduled fire writes it every run; this seat compared the two versions: only process_time moved, freshness CURRENT and run_result COMPLETE in both, and the rollback is the prior VersionId. Harmless here, but it is a write outside the sign-off's stated blast radius on the manual path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON round 5 (issuance @fc657a79b7; ADHOC.canon-r4-code-deploy under NEVER_WIDEN_R4_CN_D_1_CTO_HALF.md and AMENDMENT 3 @b1921fd086); spine L8-L10 (CLAUDE.md rule 27): WORLD acts read against the artifact, every row dispositioned before the slug.",
    "world_is": "Graduated INERT to REMEDIATION_v5 (owner 1.0.0_SA_CTO~DELL1), surfaced by this seat. The deploy's one on-demand run WROTE s3://opal-data-mdpf/mdpf/global/state/taxsma_control/current.json (the manifest's only 'written' row; version 9RRHrNkb... at 17:32:53Z over LmKKZ5_... at 13:31:47Z). Neither the deploy order, the CTO's never-widen half nor the ledger names that key. The scheduled fire writes it every run; this seat compared the two versions: only process_time moved, freshness CURRENT and run_result COMPLETE in both, and the rollback is the prior VersionId. Harmless here, but it is a write outside the sign-off's stated blast radius on the manual path.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO manifest s3://opal-data-assets/portal/gold/mdpf/_manifests/2026-10-09/20261012T173257Z.json: written 1 = taxsma_control/current.json",
        "3.0.0_SA_CVO s3api list-object-versions + get-object of the two latest versions",
        "data/mdpf/scripts/gold/mdpf_gold_consolidator.py:1216 (the key's builder)",
        "grep of ADHOC.canon-r4-code-deploy.md, NEVER_WIDEN_R4_CN_D_1_CTO_HALF.md and the deploy ledger: 0 mentions"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Graduated INERT to REMEDIATION_v5 (owner 1.0.0_SA_CTO~DELL1), surfaced by this seat. The deploy's one on-demand run WROTE s3://opal-data-mdpf/mdpf/global/state/taxsma_control/current.json (the manifest's only 'written' row; version 9RRHrNkb... at 17:32:53Z over LmKKZ5_... at 13:31:47Z). Neither the deploy order, the CTO's never-widen half nor the ledger names that key. The scheduled fire writes it every run; this seat compared the two versions: only process_time moved, freshness CURRENT and run_result COMPLETE in both, and the rollback is the prior VersionId. Harmless here, but it is a write outside the sign-off's stated blast radius on the manual path."
  },
  {
    "id": "MDPF_CANON-D1-C-S66",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T17:51:00Z",
    "one_line": "The packet's nine rows filed ARMED are all dispositioned, read by this seat. D1-S3, S4, S5 and S6 were dismissed and disarmed at ADJUDICATION_v1 (C-S5..C-S8). W8-S2 is CLOSED_UNREMEDIATED (ACCEPTED_BY_RULING) and W8-S3 REMEDIATED, both disarmed (REMEDIATION_v3). W8-S5 and W9-S7 are disarmed and OPEN: W8-S5 to the round-6 fold's read-back, W9-S7 to the code/ sync WORLD window of the 8 runner members, not claimed here. W13-S1 was dismissed at ADJUDICATION_v4 (C-S48). None holds the slug. Open after this round: W8-S4 (closes on the 10-13 served-key read), W8-S5, W9-S7, and the D1-S18 and C-S65 rows here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON round 5 (issuance @fc657a79b7; ADHOC.canon-r4-code-deploy under NEVER_WIDEN_R4_CN_D_1_CTO_HALF.md and AMENDMENT 3 @b1921fd086); spine L8-L10 (CLAUDE.md rule 27): WORLD acts read against the artifact, every row dispositioned before the slug.",
    "world_is": "The packet's nine rows filed ARMED are all dispositioned, read by this seat. D1-S3, S4, S5 and S6 were dismissed and disarmed at ADJUDICATION_v1 (C-S5..C-S8). W8-S2 is CLOSED_UNREMEDIATED (ACCEPTED_BY_RULING) and W8-S3 REMEDIATED, both disarmed (REMEDIATION_v3). W8-S5 and W9-S7 are disarmed and OPEN: W8-S5 to the round-6 fold's read-back, W9-S7 to the code/ sync WORLD window of the 8 runner members, not claimed here. W13-S1 was dismissed at ADJUDICATION_v4 (C-S48). None holds the slug. Open after this round: W8-S4 (closes on the 10-13 served-key read), W8-S5, W9-S7, and the D1-S18 and C-S65 rows here.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ADJUDICATION_v1 C-S5..C-S8; ADJUDICATION_v4 C-S48",
        "remediations/REMEDIATION_v3.md (W8-S2, W8-S3, W8-S5, W9-S7 clocks)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The packet's nine rows filed ARMED are all dispositioned, read by this seat. D1-S3, S4, S5 and S6 were dismissed and disarmed at ADJUDICATION_v1 (C-S5..C-S8). W8-S2 is CLOSED_UNREMEDIATED (ACCEPTED_BY_RULING) and W8-S3 REMEDIATED, both disarmed (REMEDIATION_v3). W8-S5 and W9-S7 are disarmed and OPEN: W8-S5 to the round-6 fold's read-back, W9-S7 to the code/ sync WORLD window of the 8 runner members, not claimed here. W13-S1 was dismissed at ADJUDICATION_v4 (C-S48). None holds the slug. Open after this round: W8-S4 (closes on the 10-13 served-key read), W8-S5, W9-S7, and the D1-S18 and C-S65 rows here."
  }
]
```
