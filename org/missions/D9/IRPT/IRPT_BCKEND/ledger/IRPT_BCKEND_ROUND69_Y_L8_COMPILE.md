# IRPT_BCKEND round 69, workstream ~Y -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~Y2` (issuer, dell2) **for** `3.0.0_SA_CVO`, 2026-10-08 ~23:1xZ. Risk WORLD, by the L6 gate floor on infra/aws
paths (ADDENDUM 10 names it LOCAL; nothing is deployed). Decomposition: `decompositions/IRPT_BCKEND_DECOMP_R69_Y.md`. Issuance:
@af1e1b08b6. The cell is E11 (CTO ADDENDUM 10): Performance client statement submissions compose with the custody revision.

## Terminality

**1 of 1** order is terminal: `IRPT_BCKEND.TO-IB-yr-691`, status complete, proof VALID. It drained @b1ba475229 (6 paths, 0 dropped,
0 foreign) after a sync merge of box/dell2 into the worker branch @1f07d95945.
- **Why the sync:** the append-only channel conflicted at the same offset. A hunk-wise union split two fenced JSON blocks (the gate
  caught 2 malformed). It was re-resolved as the box/dell2 file plus the two W220 rows appended whole: 0 malformed, corpus at baseline.
- `round-close-check.py --round 69`: `judgment=0 ungraded=0 verdict=MAY-CLOSE`. The worktree and branch are removed.

## The cell

| item | change |
|---|---|
| `ycharts/generate/custody_submission.py` +10/-2 (@128b6f7db1) | `submit` probes `reporting_policy(CUSTODY_POLICY_REVISION)`. On success it passes `additional_policy_revisions=(CUSTODY_POLICY_REVISION,)`; on `ValueError` it passes `()`. This is E9's probe, inline, because `submit_installed` sits in the export package. |
| new `tests/test_custody_submission_revision.py` | three arms: a registered custody revision is requested and `CUSTODY_REPORT` resolves under it; PERFORMANCE and ANALYSIS stay on `irpt-x10-v1`; an unregistered revision composes as before. Against base, 2 of the 3 fail. |
| AMENDMENT 1 @608ef4c1f9, then `tests/test_custody_retained.py` +12/-3 (@9e6d041f93) | That fixture's `reporting_policy` answered EVERY revision and never raised, which the real registry does not do. So the correct probe added the custody revision, and composition correctly refused the overlap (2 failures). The fixture now raises `ValueError` for an unregistered revision. The probe is untouched, and nothing catches `ReportRefused`. |

| criterion | worker | issuer re-run at b1ba475229 |
|---|---|---|
| Y69-1-AC1 | `3 passed` | `3 passed` |
| Y69-1-AC2 | base `66 passed, 2 skipped`; after the probe 2 failed; after AMENDMENT 1 `66 passed, 2 skipped` | `66 passed, 2 skipped` |

**No judgment criteria. Not served:** this change rides `~Y2`'s next `irpt-ycharts-generate` release (packaged from `source_dir`).

## Rows for your L9

| row | what it says | my read |
|---|---|---|
| D2-W220-S1 (BLOCKING, INERT) | AC2 failed after the probe: the fixture never raised `ValueError`. | Right to stop rather than catch `ReportRefused`. Ruled by AMENDMENT 1 (fix the fixture); disposed by D2-W220-S2. |
| D2-W220-S2 (OBSERVATION, DISMISSED_WITH_REASON) | Disposition of S1. | Agreed. |
