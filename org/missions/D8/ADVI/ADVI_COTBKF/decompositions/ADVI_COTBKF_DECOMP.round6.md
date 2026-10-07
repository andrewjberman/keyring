# ADVI_COTBKF decomposition -- ROUND 6 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~09:4xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-5 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_5_20261007.md` @21843491cd section 3 (E3 issued
on its un-park, no new analysis) and its re-ruling msg 264 (S13 confirmed; E3's CTO half signed on two conditions: (1) S14 fixed -- the
`commonwealth/cottonwood/bronze/crm/` PATH held back in any bucket, tested in both buckets; (2) the plan's source list prints 0 crm keys).

**Rule 24.** Domain: the three items of the round-5 analysis section 3 (E2, E5, E3). Subtraction at the cut:
- **E5:** DONE by the issuer's act, ledger `advi-cotbkf-r5-crosswalk-apply-20261007` CLOSED 1/1 @98652475d8. No cell.
- **E2:** HELD (laptop ruling A; `calendar_source()` on dell2 = `NYSE/hardcoded-fallback-2024-2027`, read 09:2xZ). No cell.
- **E3:** the CTO half's two conditions are code in `commonwealth_documents.py`: one cell, `CB-f-1`. The apply stays the issuer's act after
  its drain.

## Measured constraints (dell2, 09:3xZ-09:4xZ)

1. `restricted_prefix()` (`commonwealth_documents.py:80-83`) = `address(SOURCE, SCOPE, "bronze", "crm", ...)` less the partition =
   `s3://opal-data-assets/commonwealth/cottonwood/bronze/crm/`. Register X15 (`infra/logic/06_CONFORMANCE_LEDGER.md:149`): the restricted
   prefix is `commonwealth/cottonwood/bronze/crm/` in **`opal-data-cottonwood`**, the key being `opal_naming.key("commonwealth",
   "cottonwood", "bronze", "crm", ...)`; `address()` has no route to the firm bucket for bronze. Row S14.
2. The plan today: `DOCUMENTS-PLAN unique=11119 ... held_restricted=0 writable=11119` (no source-key count).
3. `-k "restricted and any_bucket"` selects 0 of 11 tests at the base.

## The cell

| cell | what | serves | risk | slot |
|---|---|---|---|---|
| `CB-f-1` | the hold-back matches the restricted KEY PATH in any bucket (built from `opal_naming.key()`), tested in both buckets; the plan prints `crm_source_keys=<n>`, the count of planned SOURCE keys under that path | FWD-5 (E3's CTO conditions); row S14 | LOCAL | `0.9.0_WK_ADVI_COTBKF~20` |

**Write set:** `data/assets/scripts/silver/commonwealth_documents.py`, `data/assets/scripts/silver/tests/test_commonwealth_documents.py`,
the deliverables folder, the investigation file. **Fan-out:** `1 of 1 chains, cap 8`.

## The issuer's act after the drain

E3 `commonwealth_documents.py --apply` under the never-widen pair (COO half section 1 row E3, given after the drain; CTO half msg 264), one
ledger entry; read back by count and a sample of SHA-256s; one statement and one tax form opened for the CVO (CB4d5-AC3).
