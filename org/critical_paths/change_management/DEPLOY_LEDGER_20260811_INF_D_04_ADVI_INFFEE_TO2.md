# DEPLOY LEDGER — INF_D_04 fee-classification fix (ADVI_INFFEE.TO-2) — OPENED 2026-08-11 ~1522Z

**Owner:** 0.4.0_DS_ClientPlatform~A · **Status: CLOSED 2026-08-11 ~1524Z — deploy verified, re-hold restored**
**Deployed md5 (re-download verified, never the upload rc): 49712671e33a2bf19807e452c3b24006**
**Authorization chain:** Andrew-direct "get the fix deployed" (~151xZ, relayed COO 151053Z) ·
COO never-widen authorization w/ 5 conditions (151053Z, CTO notified as co-signer, nothing
waits on reply per the no-manufactured-gates law) · ADVI_INFFEE.TO-2 GO (COO 150226Z) ·
Andrew absence-serves-NULL law (~1450Z) · CTO single-basis flag ruling (145936Z).

## PROVENANCE — the commit-of-record statement (per COO 151601Z: a LEDGER act, not a git act)

Deployed bytes = repo HEAD state of `data/inf/scripts/gold/INF_D_04.client_portal_summary.py`
at commits **f92c47d2b7 + b5909dcf11**, minus the DEPLOY-SERVE-HELD sentinel line (lift/re-hold
pattern per base's exercised serve-releases #1/#2 today).
- f92c47d2b7 (author line: base, via the shared-worktree sweep) CONTAINS the TO-2
  holdings-valuation revision **AUTHORED BY 0.4.0_DS_ClientPlatform~A** under ADVI_INFFEE.TO-2.
  That commit's own scope statement ("@fac59e6e15 projection ONLY") is **SUPERSEDED BY THIS
  ENTRY as to contents**; base's re-hold commit carries the matching supersede-note.
- b5909dcf11 (author: ~A) re-bases classification onto the uncontaminated custody-ledger mask
  (single basis; billing flag exits classification entirely).

## THE CHANGE (what serving moves, on the SCHEDULED run only — no ad-hoc production trigger)

`header_metrics` fee block: valuation=holdings.market_value × classification=custody-ledger
Mgmt-Fee trailing-12m; three exhaustive buckets w/ exact-sum identity; confession field
RETIRED; count_model documented in-emit. Expected served delta ON THE NEXT SCHEDULED FIRE
(pre-registered, CTO 145936Z point 4 + CVO): fee_earning_aua $137.19M → **$202,842,851.06**
(+$65.7M, the artifact healing); non_fee $3.62M-class → **$6,287,061.91**; unclassified 0;
unreconciled 0.00.

## COO's FIVE CONDITIONS — status at deploy-start

(a) QA read INSIDE bands: fee $202,842,851.06 ∈ [$197.0M, $203.1M] ✓ (ledger-mask revision
    moots the earlier $196.75M AT-EDGE read); non-fee $6,287,061.91 ≈ $6.3M ✓
(b) identity EXACT (209,129,912.97 == 209,129,912.97); buckets 724+75+0=799 accounts,
    279/62 clients — the 13-clients-1-account impossibility structurally gone ✓
(c) serve scope UNWIDENED: same holdings universe as today's serve (799 holdings-observed);
    the $122.5M cross-vendor book remains excluded — this change touches classification and
    valuation basis only, never universe ✓
(d) stale confession field RETIRED in the deployed code ✓
(e) rollback SAME-WINDOW, stated here BEFORE the deploy leg: restore stash
    `scratchpad/rollback_INF_D_04_003301db.py` (md5 003301db99d2841c8378da76f05aac6d,
    220,609 bytes, verified post-download) via aws s3 cp back to
    `s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py` + re-download-md5 verify ✓

## DEPLOY STEPS (ticked as executed)

- [x] rollback bytes stashed + md5-verified (003301db…)
- [x] sentinel lift commit (same window; re-hold follows)
- [x] aws s3 cp + re-download md5 verify: TIE 49712671e33a2bf19807e452c3b24006
- [x] sentinel re-hold commit (same window)
- [x] ledger CLOSED with deployed md5 + verification evidence
- [x] report: COO (deploy + five-figure table) · next: first scheduled fire read

**NEVER#6:** this deploy FINISHES in-session or rolls back + escalates loud to COO.
