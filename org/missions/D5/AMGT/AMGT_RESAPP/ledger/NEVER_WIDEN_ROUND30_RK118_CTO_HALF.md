# AMGT_RESAPP round 30 -- never-widen pair, `AMGT-rk-118` (L-FIL, the Lenovo filings battery) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`. **Status: SIGNED**, 2026-09-22 ~19:4xZ, against the live reads below.

The COO half is `ledger/NEVER_WIDEN_ROUND30_RK118_COO_HALF.md`, signed at the round-30 issuance @`bf5c280e48`. The
order acts on neither half alone, and it CHAINS behind `rk-121` (the crosswalk-identity seed fix), without which the
crawl would start with zero seeds. **Authority:** Andrew's Lenovo trial word @`cd0cca7f46`; PRD v0.23 s.12 stage 3;
this seat's rulings msg 24257 (issuer-site route; the HKEX regulator route has no registry row) and msg 24353 (EDGAR
by CIK is a finding, not a violation, if it now resolves).

## LIVE PRE-ACT READS (this seat's own instrument, ~19:4xZ, read-only)

| surface | value |
|---|---|
| `amgt/harvest/state/filing_attempt/security_key=992_HK_Equity/` | **1** -- `UNRESOLVED-SOURCE.json` |
| `filings/v1/992_HK_Equity/` | **1** |
| `sec/harvest/bronze/` | **0** objects, estate-wide |
| `issuer-site/harvest/bronze/document/` | **0** objects, estate-wide |

## BLAST RADIUS -- what the act MAY move

1. **`sec/harvest/bronze/company_tickers/<date>/`** -- 0 -> 1 estate-wide if step 1 runs. Immutable, one fetch per UTC
   day by rk-98's rule.
2. **`sec/harvest/bronze/filing/...`** -- a document only if step 2 (EDGAR by CIK 932477) fetches one. Immutable.
   **If EDGAR resolves, that IS the route**; my issuer-site ruling bound the HKEX regulator route, never EDGAR.
3. **`issuer-site/harvest/bronze/document/...`** -- one object per step-4 CANDIDATE the crawl checks, not only the
   winner (rk-98's ruled behaviour). Immutable. Crawl cap: **40 pages**.
4. **SERVED: Lenovo's `filing_attempt` key** -- write-once, and it refuses an overwrite by contract. An UNCHANGED
   outcome is SKIP-HELD and writes nothing; a CHANGED outcome is CHANGED-HELD, writes nothing, and the run exits
   non-zero (rk-105). **So this act can only ADD where nothing exists.**
5. **SERVED: `filings/v1/992_HK_Equity/...` and its `filing_source` silver** -- only on a RESOLVED outcome.
6. **The served Thesis tab for Lenovo.** With no drafting document, the adapter serves the `filing_attempt` reason
   (`scoped_amgt.py:1954-1981` at `:2052-2055`). **If this run RESOLVES, the tab still serves the OLD unresolved
   reason** until the superseding reader cell lands (this seat's carried item, round 29). That is disclosed, expected,
   and not a rollback trigger.
7. **Egress: public sources only** -- SEC EDGAR and the issuer's own site. **No vendor word is spent**: no Bloomberg,
   no Lusha, no Seeking Alpha, no model call.

**Nothing else moves:** no other security; no Bloomberg surface; no model block; no management, peers or posture
object; no code; no portal artifact.

## ROLLBACK, per key -- no delete in any branch

- **`filing_attempt`:** write-once and overwrite-refusing, so there is nothing to undo. A wrong outcome is superseded
  ONLY by the reader cell this seat carried -- never by a delete and never by an overwrite.
- **`filings/v1` and the `filing_source` silver:** on a wrong RESOLVED outcome, the rollback publishes a corrected
  object under the same newest-wins rule the reader uses; the prior object is left in place.
- **Bronze (ticker table, filing, issuer documents):** immutable and additive; a superseded object is LEFT and
  recorded.
- **Triggers:** any second security touched; a crawl beyond 40 pages; any vendor call; a `filing_attempt` overwrite
  attempt that does not refuse.

**SIGNED -- `1.0.0_SA_CTO~Z`.**
