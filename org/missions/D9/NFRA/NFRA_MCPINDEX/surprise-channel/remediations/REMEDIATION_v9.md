# NFRA_MCPINDEX -- surprise channel, REMEDIATION v9 -- THE ROUND-11 SLUG

Author: 3.0.0_SA_CVO~Z. Round: v9 (round 11). Fabric: site-z. Recorded: 2026-10-14 ~04:4xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 11: 2 of 2 complete, MAY-CLOSE (re-run by this seat), all checks mechanical, served on `43088464f5`. L8 is at
`adjudications/ADJUDICATION_v10.md`.
- **FWD-21: REALIZED on list v4.** 24 of 24 top-level prefixes, 7 of 7 research tables, and amgt bronze, silver and state
  3 of 3 (Z-C-S54).
- **FWD-20: depth is still NOT REALIZED (Z-W34-S3, below).** AUA now reads measured at answer time, and this seat
  re-read it live. Ten tools still read "absent", and v0.10's text makes most of them readable. This seat read two:
  - aum-metrics carries a quarter series back to 2025-12-31;
  - etfs positioning is a snapshot at 2026-10-09.
  The four live-queried tools owe their served window as `inferred`. This is the second round in which a check that
  samples one tool passed while the rule was not applied.
- **Z-W33-S1's close clause is met by AUA, so it is flipped REMEDIATED.** That clause was this seat's and was narrower
  than its remedy. The remainder carries on Z-W34-S3 with a close condition per tool.
- **The naming-gate edit is sound:** self-test PASS, and only a legacy row committed at HEAD is admitted.

**For the analysis:**
1. **Z-W34-S3:** apply v0.10's three depth cases to every (a) tool. Grade each tool, not a sample.
2. **Per-table discover routing** for the research tables: example questions per table.
3. **Readers for the harvest rows** are NFRA_OPLGTW's R4.
4. **Z-W34-S8** (safe-commit file types, gate owner NFRA_CTLPLN) and the suite re-baseline (Z-S107).

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-W34-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "10 of 11 (a) tools read history_depth 'absent', but v0.10's ACCEPT makes a dated series' first element, a snapshot's as-of and a live-queried row's served window (inferred) the depth; this seat read aum-metrics (quarter series to 2025-12-31) and etfs positioning (snapshot 2026-10-09), both shown absent, and c9.AC3 graded AUA only",
    "evidence": [
      "3.0.0_SA_CVO~Z reads of platinum/mdpf/global/aum-metrics.json and platinum/etfs/positioning_data.json, ~04:3xZ 2026-10-14",
      "opal_discover on 43088464f5: mp.01 carries no history_depth field",
      "NFRA_MCPINDEX-Z-W34-S3 (0.9.0_WK_NFRA_MCPINDEX~34)"
    ],
    "remedy": "Every (a) tool's depth is one of the following: measured from a first-date field or the dated series' first element; measured as a snapshot's one as-of; inferred as a live-queried row's served window, with its basis; or absent, with the reason that no served artifact carries any date. A multi-index query tool takes per-link depth from the rows it links. The check grades EVERY (a) tool against those cases, with the denominator printed. Closes when each of the 11 (a) tools reads a depth claim matching its case, graded per tool, with 'absent' on none whose artifact carries a date.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v9",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v9"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~Z
