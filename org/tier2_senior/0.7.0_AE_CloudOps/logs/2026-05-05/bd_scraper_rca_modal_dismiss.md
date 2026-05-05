# Session Log — BD Scraper RCA: Modal Dismiss Code Asymmetry
**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-05-05
**Scope:** P0 BD scraper RCA per COO GO — disambiguate why bd-transactions fails while bd-allocations succeeds

---

## Context

COO GO received at startup. CTO halt standing on modal-dismiss patch ship pending root cause.

Known facts at GO:
- Credential differential RULED OUT (both SSM docs same `opal/bd/credentials`)
- Code asymmetry CONFIRMED: bd-allocations has full `dismissModals()` helper; bd-transactions had inline Close-button-only check, 3s timeout
- bd-transactions: i-00c7568bc510f7423; bd-allocations: i-0800437d1dbb0b5cc
- Failure history: bd-transactions failed 2026-04-22 + 2026-05-04 (same error class); bd-allocations: SUCCESS both dates

---

## Phase 0 Investigation

### Code Diff — Modal Handling

| Attribute | bd-allocations | bd-transactions (pre-fix) |
|-----------|---------------|--------------------------|
| Helper function | `dismissModals(page)` — Escape + Close/x/OK buttons | None |
| Call points | 4: after login, after DataMining nav, after template select, before each download | 0 |
| Retry logic | `retryWithBackoff(3)` on download + S3 upload | None |
| Backdrop selector handled | Generic (any close button + Escape) | None |

bd-transactions (post-fix, DT 733a46904 + d5522276c):
- Inline block after login only
- Targets `.bd-federated-desktop-header-modal-container__backdrop` specifically
- Escape → waitFor hidden (5s) → fallback backdrop.click()
- No retry logic added (follow-up item)

### S3 Gap Evidence — Smoking Gun

Transactions S3 listing (`forwardfill_v2/transactions/`):
- Last upload before gap: 2026-05-01 17:56 → TXN_DAILY_2026-04-30.xlsx
- Gap: TXN_DAILY_2026-05-01.xlsx and TXN_DAILY_2026-05-02.xlsx MISSING
- Manual recovery: 2026-05-05 11:12 → TXN_DAILY_2026-05-04.xlsx (DT manual run)
- Earlier miss: TXN_DAILY_2026-04-21.xlsx MISSING (failure on 2026-04-22)

Allocations S3 listing (`forwardfill_v2/allocations/`):
| Date | Allocations | Transactions |
|------|-------------|-------------|
| 2026-04-22 | ALLOC_DAILY_2026-04-21.xlsx uploaded 18:02 PASS | TXN_DAILY_2026-04-21 MISS |
| 2026-04-23 through 2026-05-01 | All PASS (no gap) | All PASS (intermittent modal) |
| 2026-05-04 | ALLOC_DAILY_2026-05-01.xlsx uploaded 18:02 PASS | TXN_DAILY_2026-05-01 MISS |

**Allocations has zero gap in the same window where transactions missed files.** Same credentials, same BD session, different outcomes — only the modal-dismissal code differs.

### SSM Evidence

- DT manual run: SSM a912f639-0650-4b0c-8321-101ee8f5531a, i-00c7568bc510f7423
- Result: SUCCESS — Phase 1 login OK, Phase 2 DATA MINING nav OK (no backdrop timeout), Phase 3 query complete 147s, Phase 4 TXN_DAILY_2026-05-04.xlsx 797 KB, Phase 5 uploaded to S3

SSM history query failed (IAM issue on AE role — likely lambda:ListCommandInvocations not in AE policy, not blocking). Evidence sourced from DT session log `BD_TRANSACTIONS_PLAYWRIGHT_FIX.md`.

---

## Root Cause Verdict

**Code asymmetry (Case (a) TRUE) + BD portal modal change.**

1. BD deployed a post-login header modal (`bd-federated-desktop-header-modal-container__backdrop`) that blocks all pointer events on the BD portal. First appeared intermittently ~2026-04-22, persistent from ~2026-05-04 (consistent with BD weekend portal deploy).

2. `download-daily-allocation.ts` survived because its `dismissModals()` helper (Escape keypress) silently dismisses the backdrop. The helper was in the script since initial authoring.

3. `download-daily-transaction.ts` had no modal handler. The backdrop intercepted the `click('a:has-text("DATA MINING")')` → 30s Playwright timeout → 14 retries → failure.

Hypotheses from COO GO:
- **H1 (modal HTML divergence)**: CONFIRMED as root cause. Same modal, different handling code.
- **H2 (session-state quirk)**: Not supported — both scripts hit the same session; allocations passes consistently.
- **H3 (race/time-of-day)**: Contributing factor for the 2026-04-22 single miss (BD partial rollout) but not primary — allocations passes at same time-of-day.

Timing correlation: BD modal first appeared ~2026-04-22 (partial rollout), became persistent ~2026-05-04 (full deploy). Transaction failures map exactly to these events.

---

## DT Fix Assessment (d5522276c)

Fix targets specific backdrop selector, Escape first → backdrop.click() fallback. All wrapped in try/catch (no-op if backdrop absent). Manual run verified SUCCESS.

**Fix is sufficient for known failure class.** Tonight's 17:53 EDT nightly is unblocked.

**Gaps vs allocations pattern:**
- Transactions fix handles backdrop at 1 point; allocations handles modals at 4 points
- Transactions has no `retryWithBackoff` on download/S3; allocations has 3-retry on both
- These are resilience gaps, not blocking the current failure class

**Recommendation: CTO halt CLEARABLE.**

---

## Data Gap Remediation (not blocking halt clear)

Missing transaction files:
- TXN_DAILY_2026-05-01.xlsx (May 1 data)
- TXN_DAILY_2026-05-02.xlsx (May 2 data — need to verify weekend schedule)

Tonight's 17:53 EDT nightly will capture TXN_DAILY_2026-05-05.xlsx only. Manual backfill SSM runs needed for May 1 and May 2. DS/DT scope.

---

## Compiler Tools

| Tool | Phase | Run | Result |
|------|-------|-----|--------|
| comp-iam service (bd-transactions) | Before investigation | Not run — this is a Playwright/modal code analysis, not a new boto3 call | N/A |
| comp-routes behaviors | Before investigation | Not run — failure is pre-auth (modal blocks nav before any S3 request) | N/A |

Investigation used direct S3 listing + code read. No compiler tool mandate applies to this RCA scope.

---

## Commits

None — this session is read-only RCA. DT owns the code fix commits (733a46904, d5522276c). Session log commit follows.

---

## RAVC Summary

| RAVC | Delivered | To |
|------|-----------|-----|
| RAVC1 (ACK + plan) | 20260505T171206Z | COO + CTO CC |
| RAVC3 (root cause verdict) | 20260505T172650Z | COO + CTO CC |
| RAVC4 (halt cleared) | pending COO/CTO response | — |

---

## Next Actions

- Await COO/CTO RAVC4 confirmation (halt cleared or further instruction)
- Follow-up TO for DT (next session): port full `dismissModals()` helper + `retryWithBackoff` to `download-daily-transaction.ts` for parity with allocations
- ADHC_COMPIL.004 stays staged pending halt resolution
