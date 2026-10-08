# IRPT_BCKEND round 64 -- workstream ~Y decomposition (X-1 release 2: the staged repin)

Issuer `2.0.0_SA_COO~Y2`, 2026-10-08 ~13:1xZ. One item, ruled by `1.0.0_SA_CTO~DELL2` msg 1089: "Release 2 (later): X-1's
repin cell plus the smoke test, under its own pair. It also waits on the filer entitlement." ONE issuance, one cell, no
edges. Base: dell2 CLOUD `f09b802cdc`.

| item | cell | cut? |
|---|---|---|
| X-1 release 2: repin `irpt-ycharts-generate`'s staged rows for `uploads.py`, `interactive_access.py` and `generate_installed.py` so the build carries both X-1 halves and IB-pr-358's reader wiring | `IB-yr-641` | **CUT** |

## Why a repin

The release-1 census showed that `irpt-ycharts-generate` packages those three files from `staged_from` pin `3f29017cfc`,
which predates IB-yr-631 (`b7dc881c10`, uploads.py), IB-pr-354 (`c101699a71`, interactive_access.py) and IB-pr-358
(`c246d6a180`, generate_installed.py passes the profile reader). The base commit `f09b802cdc` contains all three.

## Cell IB-yr-641

The worker moves those three `staged_from` rows' `pin` to `f09b802cdc`, with each row's `sha256` recomputed from the blob at
that pin. Nothing else in the row changes.

| criterion | invocation | base reading |
|---|---|---|
| Y64-1-AC1 (the build carries X-1) | `python infra/aws/lambda/ci/release-census.py irpt-ycharts-generate --pin HEAD` | at `f09b802cdc`: `changed_members=0` (live `ZspX0qD2..` equals a HEAD build). Expected after: `changed_members=3`, naming exactly the three files |
| Y64-1-AC2 (control: import closure) | `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate` | `OK: import-closure -- 63 packaged .py file(s)` (the release-1 build at `1b5afe6a49`; the map has changed only in deployed-hash fields since). It must stay OK. |

Risk WORLD (the L6 gate floors the source map at WORLD). Release 2 is a later act under its own never-widen pair,
derived from the X-1 draft `x1_release/NEVER_WIDEN_PAIR_DRAFT.md` @f0056a55a4. It waits on Andrew naming a real filer
entitlement (CTO msg 944). This cell deploys nothing.

## Four-postulate record

(i) Domain: the three staged rows whose sources moved since `3f29017cfc` and that X-1 needs. The other 81 rows stay pinned,
and the census proves that no other member changes. (ii) One row each. (iii) One intent: carry X-1. (iv) No deployed byte
moves; the release does that later.

fanout: 1 of 1 chains, cap 8, reason: one item.
