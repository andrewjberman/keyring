# NFRA_TRNSPT decomposition -- ROUND 8 (2026-10-08, issuer 2.0.0_SA_COO~T2, dell2)

Cut on 1.0.0_SA_CTO~DELL2's ruling msg 1519 (correcting msg 1516): "revert TR-g7's class change in criterion.py, pull.py,
land_bronze.py, silver.py and gold.py; no env flag ... The work stays recoverable at ff7846f9f7. Round-8 cell: (1) a fake-route test
showing an internal encrypted author email does not land; (2) the bundle import check passes and the five modules equal their
pre-ff7846f9f7 behavior. No Lambda deploy until it drains." Basis: round 7 E1 (`R7_CLOSE.md` @9787a68b10): 368 of 368 encrypted-only
author emails are internal, 0 client; the class would land 0 in 120 days and ships in the bundle, on by default.

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-k-8` | revert the ENCRYPTED_UNVERIFIED class (five outlook modules + the silver pin + its test file) to pre-merge content; add the internal-encrypted not-landed test | FWD-7 | dell2 worker | LOCAL | worker-light | -- |

**Chains.** A = TR-k-8 (slot ~1). Fan-out 1 of 1, cap 8.

**Write set.** `data/transcripts/scripts/outlook/{criterion,pull,land_bronze,silver,gold}.py`,
`data/transcripts/scripts/tests/test_outlook_silver.py`, `data/transcripts/scripts/tests/test_encrypted_class.py` (deleted),
`data/transcripts/scripts/tests/test_internal_encrypted_not_landed.py` (new).

**Issuer rulings.** (1) "Pre-ff7846f9f7 behavior" is measured as BYTE equality with the merge's first parent `8394179dec` (no commit has
touched these paths since the merge; `git log ff7846f9f7..9787a68b10` on them is empty). (2) The new test runs against the reverted code:
an author sender, an `opalinvest.com` recipient, one non-inline `.asc` `application/octet-stream` attachment, through `pull.run(...,
admitted_only=True)` with a fake s3 -> nothing lands. (3) Row NFRA_TRNSPT-D2-W1-S1's fix is reverted with the class; the row stays
resolved (its subject, the 20th column, no longer exists).

## ADDENDUM 1 (issuer 2.0.0_SA_COO~T2, 2026-10-08 ~20:1xZ) -- the round-7 analysis lands; cell TR-s-8 added

The CTO's round-7 analysis (`CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_7_20261008.md` @117ee1fa17, msg 1521) arrived after this round's
issuance (`cecfa091b1`) and names round 8 as E1 (= TR-k-8, already issued; its criterion (3), "the proof pins the revert commit by
content", is on TR-k8's face) plus E2. E2 is added here as one cell, issued in its own commit (the analysis is the round's rectangle;
the earlier issuance covered only its E1):

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-s-8` | E2: the 29 Research Meeting transcripts (`research_transcripts/structured/`) as silver rows with the teams COLUMNS, text wiped, speaker kept; local only | FWD-5 | dell2 worker, then ISSUER (read one back) | LOCAL | worker | -- |

Chains: B = TR-s-8 (slot ~2), no edge with A. Fan-out now 2 of 2, cap 8. Rulings: speaker kept and text wiped (`parse_silver.py:5-6` vs
the analysis's wipe); `start_utc`/`end_utc` None (the stored times are derived, not observed); nothing written to S3 (the store's home is
undecided, PRD :154). Checks `R8_CHECKS/r8s_checks.py` at base box/dell2 a1f2d9f43c: s8-all FAIL (import), s8-wipe FAIL (absent).

## Rule 24 record

Domain: msg 1519's cell, criteria (1) and (2). (1) = TR8-k8-AC1; (2) = TR8-k8-AC2. Remainder: none. No deploy, no AWS call.

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R8_CHECKS/r8_checks.py`, dry-run at base CLOUD 9787a68b10: k8-notland FAIL
(absent), k8-revert FAIL (6 files differ from 8394179dec). Drain: the outlook/mail suite once after the merge.
