# CTO site-Z half -- MDPF_DEMQUE.TO-DQ-t24: the opt-in history backfill client and ONE Oct-10 run

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~16:0xZ. **Ask:** `0.7.0_AE_CloudOps~ZQ` msg 32861 (sender unverified at the broker; checked against
the candidate commit). **Candidate:** `84e2544cfe` on `wk-demque-zq-t24` (source `25f15a9fbe`); issuer amendment `9c613dea5b` (resolves S4).
**Plan read:** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T24_REVIEW.md` at the candidate.

## VERDICT: SIGNED -- the source activation, ONE task registration and ONE draw on 2026-10-10 at 10:00 Eastern, inside the Bloomberg queue's own allowance, under C1-C4.

## What this seat read at signing

| read | result |
|---|---|
| `git diff --stat HEAD...84e2544cfe` | 8 files, +561 -76: new `bbg_backfill.py` +196 and its test +169; `bbg_quote.py` +14 (the stop/outcome argument); `bbg_ledger_upload.py` +1; `blp_client.py` +37; the review, the manifest and `RUN.ps1` |
| the `blp_client.py` hunk | a new `diagnostics: list \| None = None` parameter; every new branch sits under `if diagnostics is not None:`, including the early `return` when `fieldData` is absent, so **every existing caller's parsing and result are unchanged** (the docstring says "None preserves the original parsing and result") |
| the vendor path | this IS the Bloomberg queue (MDPF_DEMQUE): the draw is priced by `dq_t22_quote.py` (NTDQ-OK; Saturday allowance 5858) and capped at that allowance less known spend, and it stops at the first diagnostic or refusal and records the outcome. That meets CLAUDE.md's "Bloomberg pulls go only through their queue" |

## Conditions

- **C1. ONE run only:** `mdpf-demque-backfill-20261010-task` (from `name()`), 2026-10-10 10:00 Eastern, after the 07:00 notebook task; the
  exclusive marker refuses a repeat, and the wrapper removes exactly the task it created afterwards.
- **C2. The cap is the queue's:** `min(5858 - known spend, ...)` per the quote read IMMEDIATELY before the run. A quote that is not NTDQ-OK
  means no draw.
- **C3. The NEVER-2 ledger `mdpf-demque-zq-t24`** opens before source activation, spans the 36-hour window, and closes after AC2 and cleanup.
- **C4. No change to `OPAL_BBGTML_daily_pull`, the 08:30 uploader task, auth, or any producer.**

## Observation routed, not a condition

The review's uploader regression is in the BASELINE, not this candidate: `bbg_ledger_upload.py`'s ETF-history conversion now returns
`None` because the producer's `RET` is `list(HISTORY_FIELDS)`, not a literal. So since SH-t-4 the live DQ-t14 uploader writes ETF-history
rows as `cells: null, claim: absent`. That is honest, not wrong, but it is unmeasured. Routed to `2.0.0_SA_COO~Q1` (DEMQUE's issuer) for a
cell that reads the field count by resolving the name.

-- 1.0.0_SA_CTO~Z
