# NFRA_OPLGTW -- adjudication v14 (site Z): round 22's L8 (OG-ga-1, the S41 grant)

Author: `3.0.0_SA_CVO~O`. Written 2026-10-06T19:23:00Z. Trigger: `2.0.0_SA_COO~O` msg 30243 (round 22 TERMINAL, 1 of 1:
OG-ga-1 FAILED on AC2; drained @926120bf18).

**Terminality.** The one round-22 order is terminal (`<status>failed</status>`, issuer re-grade @5d36cd195c). It carries
no judgment criterion, so this round has no L9 grade. This seat re-ran all three criteria at CLOUD: ga1.AC1 PASS
(operations `describe, download_filtered, list, query`; other dimensions and principals unchanged), ga1.AC2 FAIL
(held-only no; ssm Success; digest yes), ga1.AC3 PASS (entry files 1; sentinel no).

**Census.** `comp-surprise --project NFRA_OPLGTW` before this file: 370 investigation items, 37 adjudication rows, 80
remediation rows; 4 OPEN, 1 ARMED (Z-W28-S1). This file adjudicates the 4:
- **GRADUATED (2), C-S38:** Z-W28-S1 (to the CTO), Z-W28-S2 (to the issuer).
- **DISMISSED_WITH_REASON (2), C-S39:** Z-W28-S3; Z-S59, the issuer's adjudication of Z-W28-S1, carried whole by
  S1's remediation row.
- **C-S40** records the in-place advance of Z-W15-S41 to REMEDIATED.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S38",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T19:23:00Z",
    "one_line": "Round 22 L8: 2 rows GRADUATE OPEN -- the held set admits a blank cusip, so 23 blank-cusip dim_asset rows pass C3 on the query and download paths alike (Z-W28-S1, to the CTO, with the issuer's Z-S59 findings); the operator-command order form printed master ids to a worker's stdout (Z-W28-S2, to the issuer).",
    "class": "OBSERVATION",
    "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
    "world_is": "Z-W28-S1/Z-S59: infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py:341 builds position_cusips = frozenset(row[0] for row in pos_rows) with no blank filter; the query path (:656-660) and the download/export path (:939-946) both take the held set from the one helper _asset_holdings and pass it to sem.qualify_asset_plan. The real-holder download (GA1_DOWNLOAD.json: synthetic_principal false, grant_source store, granted_accounts 7477) returned 2173 rows = 2150 held CUSIPs + 23 blank-cusip rows; distinct 2151 = 2150 + 1 blank, so the 22 duplicates are the blank rows; on-host GA1_DIAG reads nonblank_unheld_rows=0, held_cusips_missing_from_download=0. git diff --name-only 2c27f3a795 CLOUD -- infra/aws/ec2/opal-gateway/app is empty, so this is the live rule. The grant added an operation, not a row: the hazard of the ACT is disarmed by Z-S59, while the 23 rows remain served on both paths until the CTO rules. Z-W28-S2: prepare()/activate print the scope diff keyed by master id; the worker saw two account-number-shaped ids on stdout once; no committed file carries them.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W28-S1",
      "NFRA_OPLGTW-Z-W28-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py:341, :656-660, :939-946 (read at CLOUD ~19:2xZ)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~28/GA1_DOWNLOAD.json (held_check {returned 2173, distinct_returned 2151, held_cusips_in_dim_position 2150, unheld_returned 23}; ssm dca27ce0-6fdf-4304-bf61-44c74f5e69a3)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~28/GA1_PROBE_AFTER_final.out (GA1_DIAG blank_cusip_rows=23 nonblank_unheld_rows=0 duplicate_rows=22)",
        "deliverables/2.0.0_SA_COO~O/r22/checks/ga1.AC2.sh re-run by this seat: RESULT: FAIL exit=1",
        "git diff --name-only 2c27f3a795 CLOUD -- infra/aws/ec2/opal-gateway/app (0 paths)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S39",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T19:23:00Z",
    "one_line": "Round 22 L8: 2 rows are DISMISSED_WITH_REASON -- Z-W28-S3 (served_release is the manifest's deployed_commit, as every earlier release record carried it, and it matches live's app tree) and Z-S59 (the issuer's adjudication of Z-W28-S1, whose findings S1's remediation row carries whole).",
    "class": "OBSERVATION",
    "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
    "world_is": "GA1_DOWNLOAD.json body.served_release is 2c27f3a7958de0aa644374cdd08fc188a27e9e3f, the EC2_MANIFEST opal-gateway deployed_commit, inside the host-printed digest. The RL6-RL8 verify scripts passed it the same way. The gateway app tree at CLOUD equals 2c27f3a795 (empty diff), and Z-W15-S47's lineage ruling stands.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W28-S3",
      "NFRA_OPLGTW-Z-S59"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_OPLGTW~28/GA1_DOWNLOAD.json body.served_release",
        "git diff --name-only 2c27f3a795 CLOUD -- infra/aws/ec2/opal-gateway/app (0 paths)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S3: consistent with every prior release record; the release md5 proof belongs to the deploy orders' verify, not to a grant order that ships no bytes. Z-S59: an adjudicating row, not a second defect; its disarm (19:11Z), its cause read (integration.py:341, :656-660, :939-946) and its fix candidate are carried by remediations/REMEDIATION_v9.md#NFRA_OPLGTW-Z-W28-S1."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S40",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T19:23:00Z",
    "one_line": "Round 22 L8: Z-W15-S41 advanced in place to REMEDIATED -- FWD-4 is now exercised by the real holder (grant_revision 3, download OK); the C3 gap the download exposed is carried by Z-W28-S1, not by S41.",
    "class": "OBSERVATION",
    "spec_asserts": "The CVO advances remediation clocks in place only on its own corroborating read; S41's remedy: on Andrew's grant word, the grant write takes the post-act read of a real download under C3.",
    "world_is": "Andrew's word: org/tier1_exec/2.0.0_SA_COO~O/deliverables/ANDREW_DIRECT_20261006_181xZ_S41_DOWNLOAD_FILTERED_GRANT_YES.md @ca460bf9fe. ga1.AC1 re-run by this seat: 1 in-force dim_asset grant, carrying download_filtered, revision advanced, nothing else moved. The post-act read ran: a real-holder download from the store (no synthetic principal) returned OK with every held CUSIP. S41's mechanism (no real principal can open FWD-4) no longer holds. The 23 blank-cusip rows predate the grant and are graduated separately (C-S38).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~O/r22/checks/ga1.AC1.sh re-run by this seat: RESULT: PASS exit=0",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~28/GA1_DOWNLOAD.json (dim_asset_download OK, synthetic_principal false, grant_source store)",
        "remediations/REMEDIATION_v5.md#NFRA_OPLGTW-Z-W15-S41"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
