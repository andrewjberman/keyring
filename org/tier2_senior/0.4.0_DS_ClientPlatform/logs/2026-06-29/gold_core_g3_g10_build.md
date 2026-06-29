# DS Session Log -- canonical GOLD-CORE G3-G10 BUILT + ACCEPTED IN FULL

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE
**serial:** 0.4.0_DS_ClientPlatform | **date:** 2026-06-29 | **window:** session start (~12:54Z) -> ~13:28Z | **TO:** DATA_ANALYTICS.GOLD-CORE

---

## Summary

The Monday-first task, done. Built the **canonical GOLD analytics CORE (G3-G10)** -- 8 new
gold tables on the complete 17-fact + 5-dim silver -- each committed, materialized to
`opal-data-bd/canonical/schwab/gold/{table}/date=2026-06-24/` (parallel/NOT-served, AES256,
canonical/schwab firm-separated), and INDEPENDENTLY boto3-verified. RAVC'd in 3 batches
(G3-6 / G7-8 / G9-10); **all three batches COO-ACCEPTED -> GOLD-CORE G3-G10 COMPLETE in full.**
Pre-GO'd Friday; formal TO + GO arrived this session (COO bfe4c0910 / GO 12:54Z).

## Work done

| # | gold table | commit | rows | sharp structural check |
|---|---|---|---|---|
| G3 | canonical_lots | a3d295652 | 252,508 | per-lot Schwab-native, NO FIFO (ULN OPEN + RLD CLOSED union); unrealized_gl $74.86M reconciles to MV-basis within $1,286 |
| G4 | account_performance | 17483c572 | 17,932 | account-grain return timeseries, 3 windows; flow-neutral investment_return |
| G5 | client_performance | 39ea0e927 | 8,839 | relationship-grain; returns RE-computed on summed bmv (not averaged) |
| G6 | canonical_nna | 8080d6cbc | 17,932 | per-account NNA; nna_total==cash+in_kind EXACT $0.0000 |
| G7 | client_tax_liability | 0e80042f8 | 2,325 | DO-BETTER: ACTUAL 1099-DIV boxes ($315,856 div tax) + real ULT lot basis ($158.68M) |
| G8 | realized_gains | 97ee6b48f | 521,065 | DO-BETTER: all 6 realized facts grounded -> non-overlapping RLU+RLW+RLD, 6-tuple dedup |
| G9 | firm_composition | 891685f8f | 3,224 | dim_asset Schwab-DERIVED class (no DDB/regex); total MV ties 06-24 snapshot exactly |
| G10 | portal_aggregates | 0d8c72dd7 | 3 | firm rollup of G5/G7/G9; NOT wired to portal (never-widen gated) |

Housekeeping: TO flipped complete + 08_GOLD_SCOPE.md marked core DONE (40ca7aa56).

## Key diagnostic wins (the grounding that held)

- **G7 ULT-vs-ULN distinction.** ULT's unrealized ($158.68M) is ~2x ULN's ($74.86M). Rather
  than ship a silently-wrong tax surface, I ground-truthed it: ULT is a DISTINCT Schwab form
  (tax/cost-basis-reporting view, 2,095 covered accts, $911M MV) -- verified ULT's own
  `unrealized` column = $158.68M (not a column mis-map). The tax view is the CORRECT basis for
  a tax-liability table. The scope's source-mapping was right; the magnitude needed grounding.
- **G8 the double-count trap, caught before shipping.** "6 realized-lot facts" are NOT 6
  independent windows -- empirically grounding close_event_id overlap showed RLY/RTY/RTU are
  superseded / tax-form-DUPLICATE vintages (RLY 99%-subset of RLW; RTY==RLY, RTU==RLU at 100%).
  A naive union would have ~doubled realized GL. Canonical series = RLU(2025 full) + RLW(2026
  YTD) + RLD(daily), deduped.
- **G8 the non-unique "natural key", caught.** The doc calls (close_event_id, close_open_event_id)
  the realized-lot key -- but it is NOT unique in the cumulative facts: distinct lots share it
  (25 RLU / 20 RLW, different qty/GL). Deduping on it dropped real lots. Fixed to a 6-tuple lot
  key (account,cusip,both event-ids,qty,gl) that preserves distinct lots while collapsing only
  true cross-fact dups (996 RLD-in-RLW). 2025 total then reconciled to RLU exactly.
- **Cross-stack tie-out (the trust anchor).** G9 composition total = G4 06-24 EMV = G10 06-24
  AUA = $1,591,227,965; G10 06-18 AUA = $1,631,357,904.10 = the documented served AUA. Internally
  consistent, nothing dropped -- COO independently S3-verified all 8 (NEVER#7).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-pipescript io | build_gold_canonical_lots.py | ran (Unknown script) | new parallel script not yet in the pipescript registry -- expected for a brand-new canonical-tree gold script; column-gap check done manually vs live silver schemas |
| comp-to | DATA_ANALYTICS.GOLD-CORE... | OK | race-free per-session TO_ID set |
| ds-commit-gate | all 8 build_gold_*.py | PASS | py_compile + ds-precommit-check + ruff py39 clean on every script (caught the G9 validate boolean-index bug pre-commit via dry-run) |
| comp-validate | build_gold_canonical_lots.py --artifact ... | NO_CONFIG | brand-new parallel tables have no validate config; gave structural+boto3 evidence instead of a false SAFE (per protocol) -- same for all 8 |
| safe-commit | x9 commits | PASS | surface-check clean, author-line correct, lane-scoped |
| boto3 (direct S3) | read-back of every materialized artifact | PASS | live-artifact grounding: head_object (AES256/size) + read-back (rows/cols/sums) for own-change verify (F5), plus the ULT/ULN + 6-realized-fact overlap diagnostics |

**What worked:** live boto3 grounding caught the G7 ULT magnitude question + the G8 double-count
trap + the non-unique key BEFORE shipping -- the discipline that makes the canonical layer
trustworthy. **What failed:** none material (one G9 validate bug, caught by dry-run pre-commit).
**Gap found:** new canonical-tree gold scripts aren't in the comp-pipescript registry yet (io
returns "Unknown script") -- a registry-coverage follow-on if these graduate to dispatch-run.

Compiler-tools-log line appended.

## Blockers

None. GOLD-CORE complete + accepted.

## Next Steps

- **[2.0.0_SA_COO]** surfacing G11-G13 (advisor/partner extension) + the 2 boundary gaps
  (canonical-history-start; Schwab-only-$1.63B vs firm-wide-union) to Andrew; if GO'd, dispatches
  the extension as a fresh TO.
- **[0.4.0_DS_ClientPlatform]** HELD on G11-G13 pending Andrew GO (do NOT build unilaterally).
  Other open line: COTETL retry-net trio still awaits 0.7.0_AE's EventBridge TF pair-window;
  DATA_ANALYTICS A3 engine design still gated on CTO A3 D1/D2 rulings. Event-hold / next queue item.
- **[Andrew]** GO/no-go on G11-G13 + the 2 boundary gaps (history-start, Schwab-only-vs-union).
