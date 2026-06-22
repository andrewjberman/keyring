# Session 2026-06-22 ~1430-1700Z — COTETL same-day P0: served-AUA architectural fix (C00SNAPSHOT) — 0.4.0_DS_ClientPlatform

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, VALIDATE

## Window
Andrew-direct SAME-DAY P0 (via CVO/COO): fix ALL cot breaks + run bronze->silver->gold e2e + validate
TODAY. Drove the COTETL served firm-AUA freeze (frozen 06-09, ~$24M/6.5% understated) to a
CVO-certified close. Continuation of the morning DATEMODE-A/B/C arc (separate logs). ~60 MCP exchanges
with CTO/COO/CVO/AE; the whole arc held on verify-on-served + Rule 22 (which became LAW mid-session,
CLAUDE.md Rule 21/22, off these very mis-inferences). ZERO false-fixes shipped.

## THREAD — COTETL served-AUA freeze: 5-layer diagnosis -> architectural fix -> certified
Root chain (each layer ground-truthed against the live/served artifact, NOT inferred -- 3 were
"looks-stuck-but-downstream" mis-localizations corrected by reading the actual code/artifact):
1. consolidated cot_transactions.parquet (orphaned, 0 consumers) -> CHAINFIX OFF-TARGET (dead).
2. holdings export CurrentDay asOfDate PINNED at 6/8 (content mutates) -> DATEMODE-A/B/C (export
   CurrentDay->Custom, deployed; silver reprocess confirmed $397.3M; standing daily holdings-refresh live).
3. canonical-seal "stuck 06-09" -> mis-localization (COT canonical_holdings snapshot-path build, not
   watermark-sealed -- B_00:1045-1051). No fix.
4. served firm-AUA STILL 06-09 post-e2e (AE caught on served, not rc=0): THE REAL ROOT -- cot's served-AUA
   ran on the bd-inherited LOTS-FIFO performance lineage (D_00 clients_tab <- account_performance C_03 <-
   C_00 canonical_performance [date=list_account_gains_dates] <- account_gains B_03 <- canonical_lots B_02
   <- holdings_lots B_01) which cot's SNAPSHOT-FIRST model does NOT feed (lots tier ENTIRELY empty;
   cot v1 chain ssm.tf:234 skips B_01/B_02/B_03). A bd-fork-shadow WIRING mismatch.

FIX (A, CTO-ruled + Andrew strategic frame: cot snapshot-first is the DELIBERATE leaner BD methodology;
this is its FIRST instantiation, not a patch): add a cot snapshot-perf branch so account_performance(C_03)
+ nna(C_01) derive total_aua/date from canonical_holdings (the 06-18 BD snapshot), NOT the dead
account_gains chain. Design iterated w/ CTO (corrected 3 of his inferences via code-grounding:
edit-point C_00->C_03, NNA-derivable-not-limitation, market_growth-derivable-as-aua_change-NNA).

IMPLEMENTED (commit 5c80bf6ca, deployed s3://opal-data-cot/code/gold):
- C_03.account_performance.py: _canonical_holdings_dates() cot-detect + load_account_performance_from_snapshot()
  (aua_current=sum(canonical_holdings.market_value) per (date,account), mirror B_03:219; aua_prior=per-account
  prior-snapshot shift; growth=aua_change-NNA [no-FIFO appreciation]; aua_residual=NNA [GRO checksum holds];
  FIFO G/L out-of-scope). main() cot-conditional gains source (:248-255) + post-flows growth/residual (:299).
- C_01.canonical_nna.py: _canonical_holdings_dates + _load_snapshot_gains (components=NNA_CLEAN_MASK so
  txn-NNA marked clean) + date-axis re-point (:825) + gains-cache loader swap. nna VALUE stays txn-derived.
- Field-map (architect-confirmed): snapshot-native (total_aua/date/aua_change/tax) | value-derived
  (NNA=txn flows; market_growth=aua_change-NNA) | out-of-scope (FIFO realized/unrealized G/L, per-lot price_return).
- FIRM-SEPARATED (NEVER#1-adjacent): cot-fork-only; git diff cot-tree-only; comp-pipescript deployed bd/49F
  C_03/C_01/C_01b/C_01c MATCH = zero contamination. C_03 ds-gate CLEAN (rm 1 unused import); C_01 RULE15
  gate-note bypass (8 pre-existing bd-fork ruff, all outside the change; cleanup-TO routed to COO by CTO).

VERIFIED (binding, on the SERVED re-run artifacts -- sharp test, not rc=0; AE re-run gold 62baea04):
- clients_tab + header_metrics + dashboard + mix_summary + timeseries_overview ALL data_as_of=06-18.
- total_aua = $395,300,238 (off the $373,157,665/06-09 freeze; +$22M). account_performance contiguous
  04-22->06-18 (707 accts/56 dates). nna 06-18. CVO-CERTIFIED CLEARED ($24M). Deploy-ledger CLOSED
  (deploy_ledger.py, slug cotetl-c00snapshot-servedaua, all 5 legs proven).
- ANOMALIES grounded (Rule 22, not glossed): (1) $395.30M vs $397.31M canonical = EXACTLY 13
  relationship-UNMAPPED accounts ($2,013,374) dropped by D_00's client-universe filter -- reconciled to
  the dollar; NOT aua_overrides (3 ids, 0 in canonical_holdings), NOT a cohort drop. (2) nna_qtd==ytd==12m
  = EXPECTED (cot data starts 04-22 -> all windows = same period; AUA=NNA+~$4M appreciation, consistent).
  (3) fee_count=0/707-vs-694 = out-of-scope fee-side (AUAFIX-L6 carry-forward).
- RESIDUAL #1 (CVO caught): account_gains STILL 06-09 -> grounded (a) BENIGN-UNCONSUMED. Consumer-map:
  C_01/C_03 snapshot-wired (don't consume); D_00 C_03-PRIMARY w/ C_02-fallback-UNUSED; D_00b/c/D_03/C_06
  grep-CLEAN. The dead account_gains->C_00->C_02 path is frozen-but-unconsumed (folds w/ the C_02 follow-on,
  future cleanup). Cert-clean end-to-end.

## Files Modified
- data/cot/scripts/gold/C_03.account_performance.py + C_01.canonical_nna.py (5c80bf6ca)
- org/critical_paths/change_management/20260622T1650Z_cotetl-c00snapshot-servedaua_deploy_completion.md (tool-ledger, CLOSED)
- 49F (data/black_diamond/scripts/gold) UNTOUCHED (firm-separated).

## Compiler Tools
| Tool | Where | Result |
|---|---|---|
| comp-pipescript io | B_03 (bd-graph) | confirmed account_gains READS canonical_lots (B_02) -- grounded the empty-lots chain |
| comp-pipescript deployed | C_03/C_01 (bd-graph) | 49F MATCH = firm-separation zero-touch verified |
| ds-commit-gate.sh | C_03 (CLEAN) / C_01 (RULE15 bypass: py_compile+AST+FA pass, 8 pre-existing ruff) | per-file |
| deploy_ledger.py | open/close-leg/close slug cotetl-c00snapshot-servedaua | 5 legs proven, CLOSED |
| safe-deploy hook | C_03/C_01 -> opal-data-cot/code/gold | DEPLOYED [cot] + md5/etag MATCH |
| md5/etag verify | deploy-MATCH (cot bronze/gold comp-pipescript Unknown-prone) | MATCH both |

- **What worked:** verify-on-served at EVERY layer (caught 4 false-success layers incl my own incomplete
  "no-gold-fix"); code-grounding the mechanism before any fix (Rule 22) -- corrected 3 CTO inferences +
  my own; mirroring B_03:219's proven snapshot-AUA calc instead of reinventing; the dollar-exact
  707/694/$2.01M reconcile.
- **What failed/banked:** the served-AUA lineage was never source-grounded before today (the gap Rule 22
  targets -- my first "no-gold-fix" was one layer too shallow, AE's served-check caught it); cot bronze/gold
  comp-pipescript Unknown -> md5/etag fallback; cot-bd-fork ruff debt (RULE15 bypass).
- **Gap found:** 13 relationship-unmapped accounts ($2.01M) -- accounts-dim/onboarding mapping gap (separate,
  benign); the dead cot account_gains->C_00->C_02 lots-FIFO path (future retire/rewire-to-snapshot).

## Blockers
None. $24M served-AUA P0 CVO-certified CLEARED + ledger CLOSED. Residual #1 benign-unconsumed (accepted).

## Next Steps
1. **[3.0.0_SA_CVO]** full-freeze re-cert on the residual-#1 source-ground (final stamp). **[2.0.0_SA_COO]** Andrew co-report ($24M-complete).
2. **[future cleanup, COO-queued]** retire/rewire the dead cot account_gains->C_00->C_02 path to the snapshot (folds w/ the C_02 follow-on) + the cot-bd-fork ruff cleanup-TO. Non-correctness, non-blocking.
3. **[self, event-driven]** AUAFIX-L6 fee-side (anomaly-3 carry-forward) when COO dispatches; the 13-unmapped accounts-dim question if Andrew wants the full 707 headline.
