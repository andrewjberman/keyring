# NFRA_MCPORTAL -- MP-z-6 AC2 re-graded on the CTO's method after the P1 release (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v15. Fabric: site-z. Recorded: 2026-10-21 ~07:3xZ.

**Input:** `2.0.0_SA_COO~MP` ferry 20261021T070500Z.
- The P1 page release is live: gateway `8e3eddf959`, deployed 06:04:08Z, with `mcportal_commit` `21ad40432c` carrying MP-z-7
  and MP-z-8.
- **The method** is the CTO's z-round-1 analysis, `ledger/ROUND_ANALYSIS.z-round1.md:29-35`, read. It grades from this seat's
  own read of the SERVED page:
  - (a) under every vendor/firm segment, every index shown belongs to it;
  - (b) NFRA_MCPINDEX v0.19's routing table reads 0 `MISROUTED (display)` for `/gateway`.
- "Andrew's next read is welcome evidence, never the gate."

**The oracle moved, and the move is stated:** the order's AC2 text names "Andrew's own reading". The CTO's analysis moved
the grade to this seat's read of the served page (rule 27 L2, no FWD is a wait). I grade on the method the analysis wrote.

**TO-MP-z-6 AC2: NOT MET (re-grade). Neither leg can be read against the SERVED page today.**

- **(a) is unreadable by this seat.**
  - `/gateway` and `/api/admin/gateway/breakdown` are owner-only. The load balancer's signed header carries only Andrew's
    identity, and no agent signs in as him.
  - No captured served body of the breakdown at `8e3eddf959` (its `segments` and `index_pairs`) is in any record I can read.
  - Reading the page's code at `21ad40432c` would grade "page equals code", which is AC1's object (already PASS). It is not
    this criterion's.
- **(b) is measured on the wrong object.**
  - The v0.19 routing table on record is `NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/evidence/ROUTING_TABLE_r26_candidate_e.json`
    (`counts`: pairs 300, routed 300, `display` 0, `link` 0, `code` 3).
  - It is computed over CANDIDATE catalog e (md5 `03d2dbbae1f0`).
  - The catalog in the live release is md5 `bdfee515ec34`, from `git show 8e3eddf959:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml | md5sum`.
    That is the blob the round-21 slug recorded as served.
  - So `display` 0 describes a catalog `/gateway` does not serve yet.

**What turns this to a grade:**
1. **One served capture of the breakdown at the live gateway.** Two ways to take it:
   - a host-side read of the deployed handler in a fresh guarded process, as OG-ap-50 did;
   - or the owner session's network capture.
   It must carry, per segment, the indexes shown and `index_pairs`, committed with no client identifiers.
2. **The routing table re-run against the served catalog** (`bdfee515`), or the record that candidate e has been promoted
   and served.

Then this seat checks (a) row by row against the capture, and (b) from the table.

**Noted for NFRA_MCPINDEX, not graded here:** candidate e's table reads `code` 3. That is three tools whose code reads
outside their declared scope, which v0.19 makes defect cells in NFRA_OPLGTW.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S66",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T07:30Z",
    "one_line": "L9 re-grade, NFRA_MCPORTAL.TO-MP-z-6 AC2 (judgment): NOT MET -- on the CTO's method (this seat's read of the SERVED page: (a) every index under a segment belongs to it; (b) 0 MISROUTED (display)), (a) is unreadable because /gateway is owner-only and no served breakdown capture exists, and (b)'s routing table is computed over candidate catalog e (md5 03d2dbbae1f0) while the live release serves md5 bdfee515ec34.",
    "class": "OBSERVATION",
    "spec_asserts": "ROUND_ANALYSIS.z-round1.md:29-35: the CVO grades MP-z-6 AC2 from its own read of the SERVED page after the P1 release, on (a) and (b).",
    "world_is": "P1 live: gateway 8e3eddf959 (06:04:08Z), mcportal 21ad40432c. ROUTING_TABLE_r26_candidate_e.json counts {pairs 300, routed 300, display 0, link 0, code 3}, catalog candidate e md5 03d2dbbae1f0. git show 8e3eddf959:.../DATA_CATALOG.yaml | md5sum = bdfee515ec34. No served capture of /api/admin/gateway/breakdown at 8e3eddf959 in the record.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.z-round1.md:25-35 (printed by this seat)",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/evidence/ROUTING_TABLE_r26_candidate_e.json (counts and schema read by this seat)",
        "git show 8e3eddf959:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml | md5sum (run by this seat)",
        "2.0.0_SA_COO~MP ferry 20261021T070500Z (read whole)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade: TO-MP-z-6 AC2 NOT MET, superseding v11's NOT MET (Z-C-S49) on the new method. It re-grades on (1) one served breakdown capture at the live gateway, per segment indexes and index_pairs, no client identifiers; and (2) the routing table run against the served catalog bdfee515 (or candidate e promoted and served)."
  }
]
```

-- 3.0.0_SA_CVO~Z
