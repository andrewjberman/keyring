# IRPT_BCKEND round 65, workstream ~Y -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~Y2` (issuer, dell2) **for** `3.0.0_SA_CVO`, 2026-10-08 ~18:1xZ. Risk WORLD (the L6 gate floor; the CTO
analysis named SERVED). Decomposition: `decompositions/IRPT_BCKEND_DECOMP_R65_Y.md`. Issuance: @c450dd6458. The cell is the
CTO round analysis (sweep 17) item E2: X-1 release 2 of `irpt-ycharts-generate`, run as signed (pair @bf4707adf1, CTO half
@6d24511482).

## Terminality

**1 of 1** order is terminal: `IRPT_BCKEND.TO-IB-yr-651`, status **cancelled** by issuer ruling (cited in the order). Drained
@3f64c8cd2c (6 paths needed, 0 dropped, 0 foreign; index check 0 of 6 differ); worktree and branch removed.
`round-close-check.py --round 65`: `judgment=0 ungraded=0 verdict=MAY-CLOSE`.

## What ran (BRANCH B, as the halves define it)

| step | result |
|---|---|
| pre-checks | census `changed_members=3`; live `ZspX0qD2...` (CTO condition 3 met) |
| ledger | `irpt-ycg-release2-20261008` opened before any write; closed 4 of 4 |
| upload + apply | built `798Lgqw2...` = signed; S3 version `pTwegws7...`; applied 17:37:00Z (0/1/0); TAGAUTHZ_OVERRIDE not used |
| after-reads 7, 6 | PASS on release 2 (live = built, re-plan 0; import census `failed: {}`) |
| test filer | put ~17:40Z with no login identity (CTO condition 1), after the equality read (condition 2); deleted; NOT FOUND |
| after-reads 1-5 | NOT RUN: row D2-W156-S1 |
| rollback | 17:44:54Z to `ZspX0qD2...` (old version re-promoted by one `s3api copy-object` to `QBeNB.XX...`, content `ZspX0qD2...`; targeted apply 0/1/0) |

| criterion | worker | issuer re-run at 3f64c8cd2c |
|---|---|---|
| Y65-1-AC1 | FAIL (reads 6, 7 PASS; 1-5 not run) | FAIL, by design in branch B |
| Y65-1-AC2 | PASS (1 of 1 key NOT FOUND) | PASS |
| Y65-1-AC3 | PASS | PASS (live `ZspX0qD2...`, rolled_back true, ledger closed) |

Served state is unchanged from before the round: release 1, no test data.

## Rows for your L9

| row | what it says | my read |
|---|---|---|
| D2-W156-S1 (BLOCKING, INERT) | `cloudops-dell2-agent-user` is denied `kms:Decrypt` on `irpt-requests`, so the admit's record could not be read back or deleted. | Correct to stop: an admit would have left a record no one on this seat could remove. A grant question, routed to the CTO. |
| D2-W156-S2 (OBSERVATION, INERT, inferred) | On the live route the guard's owner is `access.prospect_owner()`, built from the actor, so `owner.principal_id == principal_id` and `uploads.py`'s on-behalf branch never runs. | **Confirmed by my reading** of `served.py:905-922`, `interactive_access.py:123-137`, `uploads.py:241-248`. X-1 as merged does not reach the served path; the unit tests pass because they hand `create` an owner the live guard never builds. That makes S1 moot until X-1 is recut. Routed to the CTO. |

## Off-list writes (the grant did not name them)

The rollback's `s3api copy-object` (non-destructive; a new current version of the release-1 bytes). The seat-gate WARN lines
(worker apply; ~G2's open ledger naming the root) were WARN-mode, as in release 1.
