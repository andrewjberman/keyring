# IRPT_BCKEND round 66 -- workstream ~Y decomposition (E6, part 1: the served.py re-pin)

Issuer `2.0.0_SA_COO~Y2`, 2026-10-08 ~18:5xZ. Input: `1.0.0_SA_CTO~DELL2` ADDENDUM 3 @3b0845f19e (E6 = re-pinned release 2 under
a new pair, after E5). E5 drained by `2.0.0_SA_COO~P2` @038b35d676 (IB-pr-366, fix fff1b0395a: the served CREATE guard resolves an
on-behalf owner from a verified advisor email; msg 1418). ONE issuance, one cell, no edges. Base: dell2 CLOUD HEAD (carries
038b35d676).

| item | cell | cut? |
|---|---|---|
| E6 part 1: `irpt-ycharts-generate` packages `served.py` from staged pin `db8161f46e`, which predates E5; re-pin that one row so the build carries the on-behalf guard | `IB-yr-661` | **CUT** |
| E6 part 2: the release under a NEW pair | -- | NOT CUT: the pair must name the S1 read-back/delete path and row D2-W174-S3 (the role has no read on `opal-partner-<firm>`; a laptop IAM grant), msg 1418 |

## Cell IB-yr-661

Move the `staged_from` row `served.py` (`infra/aws/lambda/investor-reporting/_authz/served.py`) of `irpt-ycharts-generate` to pin
`038b35d676`, sha256 recomputed from the blob at that pin. `git log db8161f46e..038b35d676 -- served.py` is exactly one commit
(fff1b0395a), so nothing else rides.

| criterion | invocation | base reading |
|---|---|---|
| Y66-1-AC1 (the build carries E5) | `python infra/aws/lambda/ci/release-census.py irpt-ycharts-generate --pin HEAD` | at base: `changed_members=3` (generate_installed, interactive_access, uploads). Expected after: `changed_members=4`, the three plus `served.py` |
| Y66-1-AC2 (control: import closure) | `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate` | `OK: import-closure -- 63 packaged .py file(s)` at f7a9d0b34f; must stay OK |

Risk WORLD (the L6 gate floor on `lambda-source-map.json`). This cell deploys nothing.

## Four-postulate record

(i) Domain: the one staged row whose source moved for E5. (ii) One row. (iii) One intent: carry E5. (iv) No deployed byte moves.

fanout: 1 of 1 chains, cap 8, reason: one item.
