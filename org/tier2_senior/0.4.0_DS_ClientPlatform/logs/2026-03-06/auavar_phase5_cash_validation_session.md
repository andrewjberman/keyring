# ADVI_AUAVAR Phase 5 — Cash Validation & Segment E Resolution
**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-06
**Session start:** ~20:30
**Session end:** ~23:00

---

## Context

Continued from Phase 4 session (`auavar_session_complete.md`). Phase 4 closed with two
open COO decisions: D2 BKF forward-fill (~$6.6M) and "cash-only/new accounts" (~$34.1M).
Phase 5 was initiated to validate the cash-only/new accounts bucket before any inclusion
decision, driven by COO preference to include cash in AUA figures if rigidly validated.

---

## Work Performed

### 1. Cash-Only Account Diagnostic Design and Execution

Wrote `diag_cash_only_accounts.py` (commit `fb71afa4`) — five-section diagnostic profiling
the ~354 "cash-only/new" accounts:
- Section 2: account type composition (non-investment type leak check)
- Section 3: BD cash_market_value vs account_market_value split
- Section 4: multi-date value stability (10 consecutive dates)
- Section 5: NNA flow event check (deposit/withdrawal/transfer history)

**DT results (commit `00f96478`):**

| Check | Result |
|---|---|
| S2: no non-investment types | FAIL — 119 accounts (Insurance 99, TermLife 15, Annuity 4, CreditCard 1) |
| S3: cash_market_value present | PASS — account_market_value is the carrier ($91.5M vs $878K cash MV) |
| S4: MV stable | PASS — 0.21% variation, 411 accounts unchanged for 10 dates |
| S5: flow events < 10% | WARN — 389/411 = 94.6% have flow history |

**Key findings:**
- The 119 non-investment accounts are the same Segment A population already excluded
  from the gold layer (+1 new, vs 118 from AUAVAR Phase 1)
- `account_market_value` is the value carrier — these are NOT cash-holding accounts
- 94.6% of accounts have real deposit/withdrawal/transfer history — not new or pre-deployment
- The "cash-only" label was a mischaracterization from Phase 2

---

### 2. ACAT Confirmation Diagnostic

Wrote `diag_acat_confirmation.py` (commit `bb794d8b`) to determine WHY 292 activity-gap
accounts had flow history but no recent position transactions. Tested three hypotheses:
ACAT/in-kind transfer origin, buy-and-hold (old records), pipeline parsing gap.

**DT v1 results (commit `c05dafb7`):** MIXED verdict

| Bucket | Count | AUA | Fix path |
|---|---|---|---|
| OLD_POS | 327 | $31.5M | BKF fix (91b1918a) |
| FLOW_ONLY | 215 | $36.4M | Positions seed feed (AE scope) |
| UNKNOWN | 161 | $16.5M | Inspection needed |
| NO_HISTORY | 12 | $4.7M | Accept gap |

**Key finding:** No ACAT transaction label exists in the dataset. BD calls incoming position
transfers "Transfer In" (non-zero units). $91.5M in `account_market_value` confirms these are
real securities, not cash.

---

### 3. UNKNOWN Bucket Inspection

Wrote `diag_unknown_txn_types.py` (commit `0991adbf`) to inspect transaction type labels for
the 161 UNKNOWN accounts and determine if they were misclassified or a genuine new bucket.

**DT results (commit `88bab51b`):** PATTERN EXTENSION verdict

Missed labels: Sale (1,219 rows), Transfer In (3,549 rows), Cash Withdrawal (12,709),
Cash Deposit (3,946), Expense (440), Management Fee (343), Transfer Out (101).

**Critical finding:** Checked Script 02 `BUY_TYPES`/`SELL_TYPES` constants (lines 63–72).
Both `Transfer In` and `Sale` are already in Script 02's type sets — the pipeline was
processing these correctly. The pattern gap was only in the diagnostic scripts, not production.

---

### 4. Pattern Extension and v2 Re-run

Updated `diag_acat_confirmation.py` (commit `5dd75c6d`):
- Added `sale`, `transfer.?in`, `transfer.?out` to `POSITION_BROAD_PATTERN`
- Added unit-based reclassification: FLOW label with non-zero units → POSITION
- Applied consistently to both Section 1 target derivation and Section 2 classification

**DT v2 results (commit `7c6a1527`):** BUY-AND-HOLD verdict (83%)

| Metric | v1 | v2 (extended) |
|---|---|---|
| Activity-gap target | 715 / $89.1M | 465 / $33.2M |
| OLD_POS | 327 / $31.5M | 386 / $26.8M |
| FLOW_ONLY | 215 / $36.4M | 1 / $3 |
| UNKNOWN | 161 / $16.5M | 66 / $1.7M |

**Critical finding:** 250 accounts exited the gap entirely at Section 1 — they have
recent position transactions (`Sale`, `Transfer In`) already recognized by Script 02.
FLOW_ONLY collapsed from $36.4M to $3 — the positions seed feed AE scope is eliminated.

---

### 5. Variance Memo Update

Updated `docs/briefs/data-scientist-auavar-variance-memo.md` (commit `ef401956`):
- Segment E recharacterized: "buy-and-hold accounts" replacing "cash-only/new accounts"
- D2 section updated: BKF fix scope extended to cover 386 OLD_POS accounts
- Positions seed feed recommendation removed (FLOW_ONLY = $3)
- Accuracy scenarios updated: post-rebuild 99.1% non-cash
- Phase 5 diagnostic artifacts added to artifacts table

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Positions seed feed scope eliminated | FLOW_ONLY collapsed from $36.4M to $3 after correct pattern matching |
| Segment E recharacterized as buy-and-hold, not cash-only | account_market_value is the carrier; 94.6% have flow history; old position records confirmed |
| No new AE engineering required | Deployed BKF fix (91b1918a) covers the full OLD_POS population on next rebuild |

---

## Final Gap Attribution (Phase 5 Complete)

| Segment | Net Contribution | Status |
|---|---|---|
| Non-investment products (119 accts) | +$59.5M | Structural exclusion, correct |
| Liability accounts (26 accts) | -$3.5M | Structural exclusion, correct |
| Cash in gold cube | -$23.2M | Convention difference, documented |
| D1: ACT settlement lag (164 accts) | +$7.4M BD / ~$16K real | Convention difference, not a bug |
| D2 + Segment E BKF/OLD_POS (386 + 233 accts) | +$26.8M–$33M | Fix deployed, pending rebuild |
| Cash-only / NO_HISTORY (12 accts) | +$4.7M | Accept gap |
| UNKNOWN residual (66 accts) | +$1.7M | Low priority, likely covered by rebuild |
| Pricing/timing spread | -$4.3M | Normal variance |
| Rounding / set overlap | ~-$3.1M | Normal |
| **TOTAL** | **+$73.6M** | |

---

## Accuracy Scenarios

| Scenario | Gold Non-Cash AUA | vs BD Inv-Only ($1,571.6M) | Accuracy |
|---|---|---|---|
| Current (non-cash) | $1,530.7M | -$40.9M | 97.4% |
| Current (gross, incl. cash) | $1,553.9M | -$17.7M | 98.9% |
| Post-rebuild (non-cash, BKF active) | ~$1,557.5M | -$14.1M | **99.1%** |

---

## Open Items (COO gate only)

| Item | Owner | Action |
|---|---|---|
| Authorize cube rebuild | COO/Andrew | Activates 91b1918a, recovers ~$26.8M–$33M |
| UNKNOWN residual (66 accts, $1.7M) | DS | Low priority; verify after rebuild |
| H4-B structural accounts (4 accts, $15K) | DS | Low priority, manual inspection |
| Trade-date vs settlement-date wiki doc | DS | Backlog |

---

## Files Modified

| File | Change | Commit |
|---|---|---|
| `data/black_diamond/scripts/diagnostics/diag_cash_only_accounts.py` | New — Phase 5 section 1 | `fb71afa4` |
| `data/black_diamond/scripts/diagnostics/diag_acat_confirmation.py` | New, then extended patterns | `bb794d8b`, `5dd75c6d` |
| `data/black_diamond/scripts/diagnostics/diag_unknown_txn_types.py` | New — UNKNOWN inspection | `0991adbf` |
| `docs/briefs/data-scientist-auavar-variance-memo.md` | Phase 5 update — Segment E, scenarios, artifacts | `ef401956` |

---

## Status

**COMPLETE — DS work done. One COO decision remaining: authorize cube rebuild.**
