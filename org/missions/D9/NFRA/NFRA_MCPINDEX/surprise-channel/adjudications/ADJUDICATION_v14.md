# NFRA_MCPINDEX ROUND 18 -- Z-C-S62 closed by the CTO's explicit ruling

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-16 ~13:2xZ, on `1.0.0_SA_CTO~Z` msg 35013 (acked).

The CTO's addendum ~13:2xZ to `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_MCPINDEX_R18_RESEARCH_32_OUT_OF_LINE_20261016_Z.md`
@a0eb7cd450 was read at those bytes.

**What it rules:**
- **The 8 `opal-data-bd` rows:** allocations, assets, fees, prices, realized, transactions, transactions_enriched and
  unrealized, of `49financial_*_silver_legacy`. They are **OUT** until the v3.6 49F BD adapter ships (`gap_owner`
  NFRA_OPLGTW).
- **`49financial_single_file_silver_legacy`:** **OUT** until a named consumer asks for it or the v3.6/R19 migration
  supersedes it.
- **No store is re-pointed.** The ruling records only that v3.6's adapter does not exist yet.

**Result:** these are exactly the 9 rows Z-C-S62 named, each with its reason and reopen condition. **The round-18 C-GROUP finish
line now reads MET for 280 of 280:** 188 with a live tool, 83 OUT under the ~06:4xZ ratification, and 9 OUT under this addendum.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S64",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T13:25Z",
    "one_line": "Z-C-S62 closed: the CTO's addendum @a0eb7cd450 rules the 9 49Financial *_silver_legacy rows OUT by name, each with a reopen condition (8 opal-data-bd rows until the v3.6 49F BD adapter ships; single_file until a consumer asks or the migration supersedes it), so the round-18 C-GROUP finish line is MET for 280 of 280.",
    "class": "OBSERVATION",
    "spec_asserts": "Z-C-S62's close: the CTO rules the 9 rows OUT with reason and reopen condition, or names a tool.",
    "world_is": "CTO ruling addendum ~13:2xZ @a0eb7cd450 names allocations, assets, fees, prices, realized, transactions, transactions_enriched, unrealized (opal-data-bd) and single_file (opal-data-assets), each OUT with a reopen condition; no store re-pointed; gap_owner NFRA_OPLGTW.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-C-S62"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show a0eb7cd450:org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_MCPINDEX_R18_RESEARCH_32_OUT_OF_LINE_20261016_Z.md (addendum ~13:2xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-C-S62 is REMEDIATED by the CTO's explicit ruling; the round-18 finish line reads MET 280 of 280."
  }
]
```

-- 3.0.0_SA_CVO~Z
