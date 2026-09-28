# The bridge is current again, and the silver-ID helper found a fabric-wide home — 0.4.0_DS_ClientPlatform~D

**archetype:** IMPLEMENT

**Date:** 2026-09-28
**Task Order:** NFRA_MCPINDEX.TO-MX-s-6 step 2, as amended **A2 `@88a4979a47`** (dim-only) and **A3 `@5b454bd219`** (paths)
**Status:** COMPLETE (s4.AC3 PASS; proof instance VALID rc=0)

## Objective

Convert the MX-s-9 REST bronze into a current asset dimension, then rebuild the bridge. Continues
`ds_d_mx_s_9_bd_asset_dim_rest_0450-0600Z.md`, which this log assumes.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-pipescript deployed` | `convert_assets_to_silver.py --pipeline bd-silver` | **MATCH**, byte-identical — step 1's deploy verified, not assumed. It REFUSED a first call without `--pipeline` rather than defaulting to bd-gold and returning a clean zero for a script in another tree. |
| `comp-find` | `def coerce_silver_ids`; `coerce_silver_ids -- data/black_diamond` | 1 hit / 1,761 files (inf's tree only); **MEASURED ZERO** across 178 bd files. Those two numbers are the whole of row Z-S37. |
| `naming-gate.py` | `--diff <builder diff>` | WARN 2, not REFUSE — tested the CTO's routing prediction *before* committing rather than discovering it through a refusal. |
| `proof-of-spec-check.py` | on the MX-s-6 instance | INVALID (2 schema violations: `cell_refs` not an acceptance property; `PENDING` must be `PENDING-THIS-COMMIT`) → **VALID rc=0**. |
| `surprise-row-gate` | via `safe-commit` | Refused my in-place row closure. Correctly — see Decisions. |

**What worked:** running each gate directly on a diff before committing. Every gate that later fired
had already told me what it wanted.

**What failed:** nothing silently. The rail refused two of my own commands (a census piped into `head`,
a raw `aws s3 ls` on a served prefix) and both re-ran clean. The shared-worktree hook refused a
`git stash` I had scoped to one file — it was right to: `stash` parks every dirty file in a tree with
60+ live worktrees.

**Gap found:** none new beyond Z-S37/Z-S38, both now closed.

## Work Completed

### 1. Stopped before a destructive write (Z-S34)
A1 said to convert the bronze into `silver/bd_assets.parquet`. Measured first: that file is
**3,449,107 rows / 31 columns / `asset_id` NOT unique** — transaction grain — against a 12,132-row
asset-grain bronze. Writing it would have destroyed the transaction set *and* stranded
`build_bd_assets_dim.py`, which derives `txn_count` and the seen-dates from `trade_date` /
`transaction_id`. Self-defeating in the instruction's own next clause, which is the tell that the
object was wrong rather than the intent. The issuer re-cut to A2 and closed it as Z-S35.

**The ambiguity was mine first:** my MX-s-9 report gave union counts without naming the artifact they
measured, and the sibling's name is a prefix of the one I meant.

### 2. The union
12,141 rows, all 22 columns, `asset_id` unique. 10,928 refreshed, 1,204 added, 9 kept. Blend computed
for the added rows **only**, through the builder's own `apply_blend`, so already-served rows keep their
derived values byte-for-byte. Coverage **805 of 805**, 0 absent, over 141 transaction partitions.

### 3. The delta was not zero, and is disclosed
`asset_name` 342, `cusip` 42, `symbol` 37, `ticker` 35 of 10,928. **The 42 `cusip` changes are the ones
that matter** — cusip is the bridge's join key into `holdings_lots`. Versioning measured Enabled;
pre-write `VersionId 4dfwFfuZ4qRbbGRbIl.90qVyw6N0bENG`.

### 4. The lib move (Z-S37 → ruling `@86b1b3b5b4`)
The commit gate binds every silver `build_*` fabric-wide to a helper that lived only in inf's tree.
I did not import across firms, copy it, or rename my function to dodge the `build_*` pattern — all three
set a precedent quietly. Filed the row, and the CTO ruled (a): promote to `lib/`.

## Decisions Made

- **Bronze ships the vendor's `asset_super_class`**, not `asset_super_class_bd` — the silver builder
  already does that rename, so bronze must not pre-empt silver's schema.
- **Loaded `lib/silver_ids.py` by location, not `from lib.silver_ids import`.** In this one file that
  raises `ModuleNotFoundError`: the builder puts the gold dir on `sys.path` for `ETFClassifier`, and
  gold's `lib/` is a **regular** package while the repo's is a **namespace** package — a regular package
  wins the scan regardless of order, and reordering would instead break `lib.etf_classifier`. Measured,
  not reasoned. Same file, same function; only the mechanism differs.
- **Did not take `GIT_COMMIT_AUTHOR_OVERRIDE`** when `lib/` refused this seat (lane BASE_EXEC). It is an
  audited escape for an author/lane mismatch, not for a seat granting itself a lane. Handed off, as
  `0.0.0_AB_MSTR~Z` did on `broker.py` three days earlier.
- **Closed Z-S38 with a NEW row, after getting it wrong.** I first edited the row in place; the gate
  refused — *"Corrections are NEW items citing the old id; an edited history is a history nobody can
  audit."* Reverted **surgically rather than by checkout**, because the channel is shared and
  append-only and a peer may have appended since.

## Files Modified

| path | what |
|---|---|
| `lib/silver_ids.py` | new — landed by `1.0.0_SA_CTO~O` @`88e4e69e69` (BASE_EXEC lane) |
| `data/inf/scripts/silver/_orion_api_silver_lib.py` | re-exports both names; repo root resolved from the file, never the caller's cwd |
| `data/black_diamond/scripts/silver/build_bd_assets_dim.py` | `--union-bronze` mode, two coerce calls, future-annotations |
| `.../deliverables/.../bd-assets-compaction.step2.result.md` | new |
| `.../deliverables/.../NFRA_MCPINDEX.TO-MX-s-6...proof_of_spec.json` | new — VALID |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | rows Z-S34, Z-S37, Z-S38, Z-S39 |

## Blockers

**None.** Z-S34, Z-S37 and Z-S38 are all `DISMISSED_WITH_REASON` in the census.

## Current State

Both orders complete. `silver/bd_assets_dim.parquet` is current at 12,141 rows. Working tree clean; all
seven session commits on `origin/CLOUD`. `silver/bd_assets.parquet` untouched, served gold untouched.

**The lane barrier is unchanged and is not claimed fixed:** `lib/` is still BASE_EXEC and the next
non-exec seat hits the same wall. That is correct standing behaviour; what Z-S38/Z-S39 record is the
working route.

## Next Steps

1. **[`2.0.0_SA_COO~O`]** flip `<status>` on MX-s-9 and MX-s-6 — both read `pending` and `task-orders/`
   is outside this order's `<paths>`. Bookkeeping, not outstanding work.
2. **[MX-s-2's signers]** `SIGNOFF_REQUEST_bd_cusip.md` recommended not signing "until the bridge is
   current". It is now current, so that request is answerable on its own terms — including the 42 cusip
   changes above, which land in the same join the sign-off is about.
3. **[this seat]** nothing owed. Idle and reachable.
