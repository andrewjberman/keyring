# IRPT_CUSTDY decomposition -- ROUND 5 (issuer 2.0.0_SA_COO~K2; drafted 2026-10-07 ~12:2xZ, dell2)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:** the round-4 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_CUSTDY_ROUND_4_20261007.md` @16d9b128c0
(`1.0.0_SA_CTO~DELL2` msg 511), section 3: E1-E2. receiving-check: UNCHECKED (no checker for a round analysis; read by this seat).

**SUPERSEDES round 3's E3 order** `IRPT_CUSTDY.TO-CU-c-3.client-report-template` (cut @3596e20d26, never spawned): round 5 E2 is the same
template with the real-client render and eslint added. That order is flipped `superseded`, naming `IRPT_CUSTDY.TO-CU-e-2`.

**Rule 24.** Domain: E1, E2. Two cells, two write sets (python vs portal), no shared file.

## Measured constraints (dell2, ~12:2xZ)

1. **The 4 unkeyed accounts (E1, W10-S1):** granted to `matthew_gooch` in the ownership map, NOT_IN_DIRECTORY, and absent from
   `custodian_key_seam.json` (5376 entries), so `schwab_key()` returns None. IRPT_BCKEND's census (msg 413,
   `deliverables/0.9.0_WK_IRPT_BCKEND~144/IB64-1_directory_coverage.json`) classes the estate's 1,961 as 1,447 no-bridge-source, 482
   xref-unresolved, 32 absent-from-feed; each carries an opaque id, so these 4 can be located in it.
2. **The template (E2):** the round-3 E3 section of `DECOMP.round3.md` holds the render-package facts (pattern `PerformanceDocument.tsx`;
   `manifest.ts`/`PrintEntry.tsx`/host are IRPT_BCKEND a1-a4; `bun:test`; a new product file lands on DEV after CTO review).
3. **Real client, not committed:** criterion (1) renders one REAL client of the chosen advisor. Real figures never enter the portal repo:
   the committed test keeps a SYNTHETIC fixture; the real render is a committed check script that renders the real document (read from
   `hop3_real_run.py` output written under `.scratch/`) and prints a summary line -- the real data and the rendered output stay uncommitted.
4. **Bun (msgs 492/500/508):** `bun --no-install` only, inside the worktree's `portal/` with node_modules LINKED; the link proved first;
   an unresolved import is STOP. `react-dom/server` and `eslint` (with `portal/eslint.config.js`) are present in the shared node_modules.

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CU-e-1` (E1) | the 4 unkeyed accounts measured: each looked up by every Schwab identifier, classed found-under-another-key or not-held with evidence; a not-held account renders `not covered: <reason>` in its client's report data | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | A, `0.9.0_WK_IRPT_CUSTDY~13` |
| `CU-e-2` (E2) | the 49 Financial `ClientReportDocument` (round 3 E3's template) plus a real-client render check | FWD-1, FWD-3 | NOT-EVALUATED | dell2 | LOCAL | B, `0.9.0_WK_IRPT_CUSTDY~12` |

## Write sets (disjoint)

- **CU-e-1:** `data/assets/scripts/gold/irpt_custody/unkeyed_lookup.py` (new), `tests/test_unkeyed_lookup.py` (new), `hop3_real_run.py`,
  `tests/test_hop3_real_run.py`, `tests/test_hop3_directory_gap.py` (all under `data/assets/scripts/gold/irpt_custody/`).
- **CU-e-2 (portal repo):** `portal/src/pages/InvestorReporting/render/clientreport/ClientReportDocument.tsx`, `.../clientreport/types.ts`,
  `.../render/fixtures/clientreport.firm-a.json`, `portal/src/pages/InvestorReporting/__tests__/clientreport/client-report-document.test.tsx`,
  `portal/scripts/irpt-custody-render-check.tsx` (new).
- Each: its deliverables folder and the investigation file.

**Ordering and fan-out:** `fanout: 2 of 2 chains, cap 8`. CU-e-2's real render reads `hop3_real_run.py` as it stands at its base; a
not-covered entry from CU-e-1 is a field it prints when present (no edge: it renders the document it is given).

## The issuer's acts after the drain

1. The real run for the advisor after both merges; grade E1 (each of the 4 classed, not-covered reason in the data) and E2 (one real client
   rendered, summary only; the CVO grades C-SHAPE at L9).
2. Send the portal candidate (CU-e-2's nested branch) to `1.0.0_SA_CTO~DELL2` for review before it lands on DEV.
