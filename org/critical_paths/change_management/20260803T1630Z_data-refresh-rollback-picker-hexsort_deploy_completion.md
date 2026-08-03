# DEPLOY LEDGER: opal-data-refresh-api -- MDLP_MONPUB.W5 rollback-picker hex-sort fix

**Opened:** 2026-08-03T16:30Z by `0.2.0_DT_PortfolioAnalytics` (at deploy START, per NEVER#6)
**Status:** **CLOSED 2026-08-03T16:35Z -- APPLIED + VERIFIED, all legs closed.**

## Authorization
- CTO GO 20260803T160830Z (W5 deploy leg; TO `1.0.0_SA_CTO-2026-08-03-monpub-w5`).
- Grounding: CVO Andrew-direct audit @30a13b89b1 (deployed-zip-verified defect).
- Fresh ledger (W3 shipped 16:08Z before W5 was cut; "rides with W3" overtaken -- CTO ack'd 162123Z).

## The change
- Code: DS commit `5de42e3b7b` -- handle_history: full-partition paginate + startedAt-desc sort
  BEFORE limit (was ScanIndexForward=False on random-hex SKs = hex order, not recency);
  SSCN partition fixed identically; denominator logged.
- Baseline (pre-W5) CodeSha256: `dH/GOrT+Pj1/Jj3daUVPjDnY5MiROYYd8m3OebhE5yQ=` (= W3 deploy, 16:08:22Z).
- PRE-FIX CAPTURE (16:28Z, deployed data-refresh-v2.4.0 handler, saved history-prefix.json):
  20 returned, `exec-5a4149176fb6` ABSENT, leading ids all d/e/f hex -- defect live on record.

## Legs
- [x] Artifact build + upload write-verified (sha Z3rt+Opu1VJxZ/MW199SnNOOpE0FUnVNf8PBT7H/Spg=, 19,172 B)
- [x] Source-map delta committed dd14cc8aca (pre-build co-tenant check CLEAN; post-record sweep-check
      on 34d9867449: only the data-refresh entry + global timestamp moved -- CTO interim discipline)
- [x] plan: exactly the one Lambda hash change (dH/GOrT+... -> Z3rt+Opu...)
- [x] safe-apply complete (1 changed) + 0-diff + live CodeSha256 match (LastModified 16:29:56Z)
- [x] POST-FIX differential PASS: exec-5a4149176fb6 PRESENT (was ABSENT pre-fix, captured 16:28Z),
      startedAt strictly descending across all 20 returned, top entry 16:21:46Z (the live run).
      Denominator: Lambda logs "N EXECUTION items in table, returning top M"; independent scan
      measured 133 items, 20 returned by recency.
- [x] No-regression: 3 co-returned entries pre/post -- canRollback + key-set identical (NONE mismatched)
- [x] Tag data-refresh-v2.5.0 created + verified (cat-file -> tag); record commit 34d9867449 landed
      WITHOUT lane override (COO closed the TF-root gap @ac778cbbcd, DATA_REFRESH_DEPLOY enumerates DT)
- [x] Ledger closed 16:35Z
