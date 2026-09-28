# SIGN-OFF (1.0.0_SA_CTO half) -- irpt-performance-adapter hcZpXDDo -> qfxZ0DzB: a retained 49F report with an impossible series reopens as a named refusal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_REOPEN_GUARD_20260928.md`
@`c67141630f`, blob `7bedf42ea83bce0a87b6643eaf08cc8ef7105261` (2.0.0_SA_COO~P msg 102481). **Signed:** 1.0.0_SA_CTO,
2026-09-28 ~23:4xZ. The 4.0.0_SA_CRO half is asked separately. Closes D1 of ledger `irpt-adapter-implausible-guard-20260928`.

## Signed, as the packet reads it

- **The act:** one safe-apply of the performance root moving CodeSha256 `hcZpXDDo..` -> `qfxZ0DzB..` (S3 version
  wVW7wVQw -> 5bmwADQs). Plan 0/1/0, code only; IAM unchanged; no plan armed.
- **The code:** `90c4b596f3` (worker ~63), an ancestor of CLOUD. Read at signing: `retained.py` adds
  `implausible_engine_series(report)` (a cumulative point <= -1.0) and checks it only when REOPENING an existing
  pointer for a 49 Financial owner; the fresh path's read-back is unchanged; one test file.
- **Nothing in the store is deleted, rewritten or re-derived.** Census 69 -> 69, only `retained.py` differs.

## Blast radius (both readers)

- **Moves:** exactly 2 of 23 retained 49F reports (790fe675, 74fb35a4: the NEW-01 account's 1Y and YTD) reopen as a
  named refusal instead of -100%. The other 21 reopen unchanged; fresh computes unchanged; INF and COT untouched.
- **Rollback per key:** re-apply at S3 version wVW7wVQw (hcZpXDDo).
- **Not covered, stated:** the two near-miss accounts (-0.9996, -0.99996) still pass this predicate, as the CRO's
  first half recorded. Both paths retire when the holdings-basis gold replaces the engine read
  (`ANDREW_DIRECT_20260928_224xZ_HOLDINGS_BASED_PERFORMANCE_ALL_FIRMS_SILVER_TO_ONE_GOLD.md`).

## Conditions

- D1 after apply: CodeSha256 readback == `qfxZ0DzB`, a REAL cold-start invoke, and the CRO's `/ui-walk` read of the
  NEW-01 account's 1Y and YTD (named refusal) plus one control account (its figure unchanged).
