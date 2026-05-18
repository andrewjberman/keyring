# Session — Schwab<->BD fuzzy-join live-path verification

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-18
**Source:** COO routing task, surfaced by MDPF_ASSETS.011 (DS Base SmartX per-account
membership probe, brief `292d2ef84`). Low urgency.
**Workspace CLOUD commit:** (this log) pending

---

## Task

MDPF_ASSETS.011 proved the Schwab<->BD account relationship is DETERMINISTIC — Schwab
`account_id` (10-digit zero-padded) `lstrip('0')` == BD `original_account_number`
(8-digit), live-verified 73/76. It flagged that the archived
`build_schwab_bd_account_mapping.py` joins by FUZZY matching instead (market value
±1% + name Levenshtein). COO ask: confirm no fuzzy Schwab<->BD account-join variant is
wired into any LIVE pipeline path.

## Finding — CONFIRMED: no fuzzy account-join is live

| # | Item | Verdict |
|---|------|---------|
| 1 | `archive/integration/build_schwab_bd_account_mapping.py` (MV±1% + Levenshtein account matcher) | DEAD — archived; zero dispatch/chain/Lambda/producer references; Jan-2026 logs record it produced "0 matches" even when last run |
| 2 | `scripts/bronze/build_schwab_bd_account_xref.py` (LIVE bronze producer) | Account join is DETERMINISTIC — `acct10` = `lstrip('0')` on both sides (L119/L185, merged L227). Exactly the proven key. |
| 3 | `build_schwab_bd_account_xref.py` `last_name_fuzzy_lookup` (L207-222) | Fuzzy, but ATTRIBUTION-only — resolves architect/relationship_id for Schwab-ONLY accounts (no BD counterpart). NOT an account-to-account join; zero double-counting risk. |
| 4 | `scripts/diagnostics/_schwab_bd_match_v2/v3.py`, `_schwab_bd_account_match.py` | Ad-hoc diagnostics — underscore-prefixed, "Run on EC2" manual headers, no pipeline wiring |
| 5 | `infra/aws/lambda/**` fuzzy-join grep | Only false positives (openai SDK `text_similarity_grader` in news layer). No Schwab<->BD join in any Lambda. |

The live Schwab<->BD account relationship uses the deterministic `lstrip('0')` key. The
archived fuzzy matcher is dead. The one piece of live fuzzy logic
(`build_schwab_bd_account_xref.py` last-name attribution fallback) is not an account
join — flagged to COO as a separate, lower-severity item if a review is wanted, but it
is NOT the fragile fuzzy account-join MDPF_ASSETS.011 raised.

## Resolution

- No fix TO needed for the account join — COO's "confirm back, no action" branch.
- Full evidence report sent to COO `20260518T190120Z`.

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-blast build_schwab_bd_account_xref` | No graph nodes — bronze scripts aren't in the portal/gold-centric compiler graph |
| `comp-blast build_schwab_bd_account_mapping` | No graph nodes — archived script not in graph |
| `Grep` (repo-wide, non-archive) | Operative tool — script-name + output-artifact + diagnostics references enumerated; confirmed no live dispatch/chain/Lambda wiring |

comp-blast had no coverage here (bronze + archived scripts are outside the graph);
repo-wide grep across `data/*/scripts/`, `infra/aws/lambda/`, dispatch/chain configs
was the operative verification.

## Current State

| Item | Status |
|------|--------|
| Schwab<->BD fuzzy-join verification | COMPLETE — confirmed no fuzzy account-join live; report to COO |
| ADVI_BIWNDW.001 | Code-accepted; visual pass routed to Andrew; flips complete on COO relay |
| ADVI_INFGRO.005/.006 | HELD — INFGRO.009 clean re-run + DS~C AC5 |
| Watcher | LIVE |

## Next Steps

- [COO] Verification closed back — no action on the account join. Optional: decide
  whether the live last-name attribution fallback in `build_schwab_bd_account_xref.py`
  warrants a separate review (lower severity; not a double-counting risk).
- [DE] Standing by for the BIWNDW.001 visual-pass relay + the INFGRO.009 re-run.
