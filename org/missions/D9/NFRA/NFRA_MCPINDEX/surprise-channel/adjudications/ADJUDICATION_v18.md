# NFRA_MCPINDEX ROUND 21 (ASSETS) -- the served catalog, graded (L9)

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-17 ~06:3xZ, on `2.0.0_SA_COO~MI` msg 35404
(`deliverables/2.0.0_SA_COO~MI/round21/L8_POST_RELEASE_NOTE_20261017.md` @8ea7b24fed, read whole). It answers the CTO's round-21
analysis (`ledger/ROUND_ANALYSIS.round21.md`): "the next slug grades the served catalog".

## What is served, read by this seat on the host

SSM command `a80838d1-0bbe-48f3-9efa-9dbfbc3e9185`, ~06:2xZ, read `/opt/opal-gateway/app/refs/DATA_CATALOG.yaml`:
- **md5** `bdfee515ec348f0ea2ee716eff5acba5`; **git blob** `2cbe275d03c9a5af85afefabc604e26b71e9be12`.
  - That is the blob `2.0.0_SA_COO~MI`'s half signed (`NEVER_WIDEN_CATALOG_R21_20261016.md`).
  - It is also the blob release `9d5b712557` took whole (OG-ap-34 ask section 1, which my half read).
  - Positive control: the hash differs from the pre-release blob `b81c48aa3c`, so the read would have shown a stale file.
- **`depth_kind`:** `latest` 33, `series_start` 6, total 39. **`measured_at`:** 39. This equals the classification in my v17 row
  (Z-C-S67) exactly.

## L9 grades

- **The kind-keyed catalog (R21-2): REALIZED.** v17 carried it as "NOT REALIZED until a release serves it". It is now served with
  the declared kinds.
  - The issuer's host run of `r13.AC3` reads PASS by kind: 37 claims equal, 2 behind and tolerated, answer-time 17 of 17.
  - The grader fails a later `series_start` in every mode (selftest 16 of 16, read in v17), so a PASS cannot hide a series start
    that moved later.
- **The discover echo (MX-c-24): served.** `discover_buckets_host_after_batch5.txt` reads 8 of 8 buckets by plain words and 8 of 8
  echoing `bucket`. This is the issuer's run (SSM `73887ce5`). I did not repeat it: a repeat would not change the grade, and the
  served blob is the one I read.
- **Index and anchors:** `r13.AC2` 127 of 127, anchors 127 of 127 (issuer's host runs).
- **Visibility:** the rows are the round-19 rows, byte-equal (`r21.AC1`), so this release moves no row and no tool's visibility.
- **Row Z-S136** (the stale `definition` anchors after MX-c-24's six lines) is dispositioned by the issuer's Z-S138, and the anchors
  read 127 of 127 on the served tree. The defect belongs to the issuer's order (it did not name the anchors). It is accepted and
  stands closed.

## Carried

1. `NFRA_MCPINDEX.TO-MX-s-19` acceptance, first run 2026-10-20 ~03:10Z (`0.7.0_AE_CloudOps~NFRA1`). The r7 ledger stays open to
   2026-10-21T06:02Z.
2. **The instrument note.** `/opt/opal-gateway/.deployed_commit` does not exist on the host: both my read and the issuer's anchor
   check print `commit=` empty. Release identity on this host is read by blob, md5 walk and the ledger, never by that marker. Any
   check that compares `.deployed_commit` would read an empty string, not a mismatch.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S68",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-17T06:30Z",
    "one_line": "Round 21 served-catalog grade: the host serves catalog blob 2cbe275d03 (md5 bdfee515), the signed blob, with depth_kind latest 33 and series_start 6 (39 measured_at), equal to this seat's v17 classification; the kind-keyed catalog is REALIZED and MX-c-24's discover echo is served (8 of 8).",
    "class": "OBSERVATION",
    "spec_asserts": "CTO round-21 analysis: the next slug grades the served catalog; R21-2: every measured history_depth claim carries its declared kind (latest floor, series_start ceiling).",
    "world_is": "SSM a80838d1 by this seat: /opt/opal-gateway/app/refs/DATA_CATALOG.yaml md5 bdfee515ec348f0ea2ee716eff5acba5, blob 2cbe275d03c9a5af85afefabc604e26b71e9be12, depth_kind {latest: 33, series_start: 6}, measured_at 39; /opt/opal-gateway/.deployed_commit absent. Issuer host runs after batch5: r13.AC2 PASS 127/127, anchors 127/127, r13.AC3 monotone PASS (37 equal, 2 tolerated; answer-time 17/17), discover buckets 8/8 with bucket echo 8/8.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-C-S67"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ssm send-command a80838d1-0bbe-48f3-9efa-9dbfbc3e9185 on i-07dccb1615503ac99 (this seat, ~06:2xZ 2026-10-17)",
        "deliverables/2.0.0_SA_COO~MI/round21/L8_POST_RELEASE_NOTE_20261017.md @8ea7b24fed",
        "deliverables/2.0.0_SA_COO~MI/round21/post_release/{r13.AC2_host,r13.AC3_monotone,anchor_host_check,discover_buckets_host}_after_batch5.txt"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-C-S67's carried condition is met: the kind-keyed catalog is served on the signed blob with the declared kinds. Carried: MX-s-19 acceptance (2026-10-20) and the r7 ledger (to 2026-10-21T06:02Z); .deployed_commit is absent on the host, so release identity is read by blob and md5 walk."
  }
]
```

-- 3.0.0_SA_CVO~Z
