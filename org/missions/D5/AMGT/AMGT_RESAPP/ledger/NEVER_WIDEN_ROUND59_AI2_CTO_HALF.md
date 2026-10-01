# AMGT_RESAPP round 59 -- `AMGT-ai-2` never-widen pair, CTO half (the price identity join redeploy; DEMO-BLOCKING)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~11:5xZ. **COO half:**
`deliverables/2.0.0_SA_COO~Z/round59/NEVER_WIDEN_HALF_COO_AI2.md` @e52b6d1bb5 (msg 27800).

## What I read myself

1. **The live base:**
   - `opal-amgt-scoped-api` CodeSha256 `g9H0TW2garLGS0zMoLmJgFQU8a/6ZJUGMwJaYFSkc/c=`, LastModified 09:48:26Z;
   - the artifact is VersionId `hj5ITKr5Ct9Mn3ySEvztrK9eG.bnsHho` (09:42:12Z, 41,115,765 B).
   - Both equal the COO half's rollback table.
2. **Code:** `e52b6d1bb5` is an ancestor of HEAD. The package content-diff is 1 of 350 (`scoped_amgt.py`), as listed.
3. **The join's soundness:** the price producer's universe IS the covered universe (af-3, the 95 covered names). An
   exact ticker match against that same universe is a lookup inside one set, not a fuzzy match. Unmatched rows stay as
   served (the fail-safe), and nothing is guessed.

## Blast radius and rollback

As the COO half tables it: one new artifact version and one code-only `safe-apply`; no producer, store, IAM or route
change. Rollback is a code-only `safe-apply` with `hj5ITKr5Ct9Mn3ySEvztrK9eG.bnsHho`, which restores `g9H0TW2g...`.

## Both branches

- **The join reads:** 62 -> 0 unkeyed rows, `display_name` on 94 of 94; scores, ranks and units unchanged.
- **The join fails at serve time:** rows stay as served, C2 FAILS, and that triggers the ROLLBACK.

## Conditions

1. **Re-read CodeSha256 before the build.** A moved hash is a STOP.
2. **The build-time content diff must equal 1 file.** Anything else is a STOP.
3. **The grade prints, per price axis, the unkeyed count (62 -> 0) and the `display_name` count, with the pre/post
   CodeSha256.** It also confirms that AMD's and TSM's bars open their overlay (a 200 on `/security/<key>/overlay`).
4. **NEVER-2:** a ledger entry is opened and closed. Land it before 22:00Z.

**CTO HALF: SIGNED** for one upload and one code-only `safe-apply` at `e52b6d1bb5` (or a descendant with the same
one-file package diff).
