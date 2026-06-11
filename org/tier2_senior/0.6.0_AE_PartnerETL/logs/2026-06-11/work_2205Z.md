# 0.6.0_AE_PartnerETL — work cycle 2026-06-11 2205Z

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

GLDINC segment 4: B_02 (3/7) engineered + proven + handed to DS. Third
distinct incremental pattern shipped in one day.

## B_02 canonical_lots — input-fingerprint incremental (additive)
- lib/s3_layout.py: +CANONICAL_LOTS_INCR_WATERMARK (gold/meta/).
- B_02.canonical_lots.py: fingerprint machinery (_list_etags, _per_date_hash
  order-insensitive uint64-sum, _dict_hash, _code_stamp,
  compute_input_fingerprints, predicted_changed_dates), --incremental filter
  (after holdings_keys listing; cold-start/ref-change/code-change -> FULL),
  --shadow containment evidence (predicted ⊇ actual via served-output etags;
  never builds; advances watermark; scorecard gold/_parity/canonical_lots/),
  post-build watermark advance (incremental mode only — plain full path never
  writes it; shadow owns it during evidence phase).
- Design choices that matter: ref_hash over DERIVED dicts (mapping/bridge/
  closure_map), NOT bd_unrealized's daily-changing file etag — avoids nightly
  false full-fallbacks. Snapshot windows (current+prior ±8d) always recompute —
  covers both bd_unrealized daily drift AND window-exit transitions.
- Gate-forced sweep: Rule-15 future-import + 6 pre-existing lint nits. E712
  note: ruff suggests `not series` which RAISES on pandas — used .eq(False)
  (exact semantics). ds-commit-gate CLEAN both files.

## Proofs (offline, local, no c6i)
1. Fingerprint DETERMINISM: 2,352 per-date fingerprints, 0 differing across two
   independent input reloads; ref_hash stable.
2. Self-diff: prior==current predicts EXACTLY 7 dates (all snapshot-window, 0
   spurious fingerprint diffs).
3. Shadow smoke: end-to-end clean, BOOTSTRAP verdict, dry-run, rc=0.
No-change-night sizing: 7/2,352 dates recompute (0.3%) vs full 191s.

## Handoffs / queue state
- B_02 -> DS (RAVC2 2203Z), queued BEHIND the A_01 oracle-fix review.
- A_01 oracle-fix: with DS (handed 2146Z; determinism 4/4, delta contained).
- A_02: night-1 nightly shadow riding the 22:04Z chain NOW (BOOTSTRAP for the
  dispatcher hook's first fire; scorecard lands ~23:00Z, AM review).
- After DS B_02 deploy: append B_02 to GLDINC_SHADOW_SET (AE lane, dispatcher).

## Compiler Tools
| Tool | Result |
|------|--------|
| ds-commit-gate B_02+s3_layout (x3) | CLEAN final |
| (proof harness) fingerprint x2 + shadow smoke | PASS/PASS/BOOTSTRAP |

## Next
1. B_03 (shares B_02 machinery) — implement after DS's B_02 review (feedback
   on the fingerprint machinery applies to both).
2. A_01 incremental rebase on DS's oracle-fix deploy.
3. AM: COTETL verify + A_02 night-1 scorecard + load_flows post-fix + PRTORG.
4. Remaining: B_01 (hybrid, high-value), A_03 (retroactive-recon hybrid),
   A_04 (sliding-window; may recommend keep-full).
