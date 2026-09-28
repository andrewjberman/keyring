# The registry stops travelling: the asset-dim pull resolves its names at build time — 0.4.0_DS_ClientPlatform~D

**archetype:** IMPLEMENT

**Date:** 2026-09-28
**Task Order:** NFRA_MCPINDEX.TO-MX-s-11 (asset-dim-build-time-pin), issued `864ea3b7ef` by `2.0.0_SA_COO~O`
**Status:** COMPLETE (AC1/AC2/AC3 PASS; proof instance VALID rc=0)

## Objective

MX-s-10's test run of the ported asset-dim schedule could not start: `pull_bd_asset_dim_rest.py`
imported `lib/opal_naming.py`, which reads the multi-firm registry and NAMING_SCHEMA. Neither is on
the instance, and shipping the registry to a firm's bucket is refused outright (NEVER#2). Ruling
`1.0.0_SA_CTO~O` @`e4b19b9898` (row Z-S43): resolve at build time instead.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `opal_naming generate` | `generate --out <dir> --target <pin>` | Rendered three times — mine, mine post-landing, and the CTO's renderer — **byte-identical (2,020 bytes) every time**. |
| `naming-gate.py` (via safe-commit) | pin + module commit | **PASS 0 graded.** It also did the real work on the `lib/` side: it refused my `_long_scope(reg, "49financial")` as a hand-kept carrier. |
| `proof-of-spec-check.py` | on the instance | INVALID (2 control-status enum violations) → **VALID rc=0**. |
| `comp-schedule` / `comp-iam` / `comp-adversary` | not run | All three DECLARED-NOT-APPLICABLE by the order's own preflight; the declarations held as executed. |
| `comp-pipescript` / `safe-deploy.sh` | not used for the `lib/` pair | Neither models `code/lib/`; `safe-deploy`'s mapping covers `data/<firm>/scripts/{gold,silver,bronze}/*.py` only. Verified by ETag against local HEAD md5 instead, before and after, denominator printed. A coverage boundary, not a skipped check. |

**What worked:** capturing the oracle before touching anything. The whole risk of this cell was the
S3 target silently moving, and that control only exists if taken first.

**What failed:** my own patch, on one line — see Decisions. Also two small environment traps: native
Python cannot spawn the MSYS `.tools/aws` shim (redid the census in bash), and `s3 ls` renders LOCAL
time, which would have mis-dated the pin object by four hours had I not used `s3api`.

**Gap found:** none new. No surprise row was filed this cell.

## Work Completed

### 1. The pin
`_asset_dim_rest_pin.py`, a GENERATED view carrying scope, short, vendor, routed bucket, tier, table,
key prefix and object. `TARGET_REGISTRY_KEYS` declares **`("scopes",)` alone** — `tiers.json` is
deliberately undeclared, because this pipeline's bronze sits in the ROUTED bucket alias rather than
the tier home, so a tiers move must leave the pin's bytes unchanged (`r6-undeclared-inert`).

### 2. The module
Imports the pin **by location** (no package root exists on the instance), drops `opal_naming`, gains
`bronze_key(partition)`. `assert_firm_separation()` is narrower and says so in its own docstring: the
old arm asked the live registry a question the instance cannot ask, and which is now true by
construction; the environment-override arm — the one that could ever fire — is kept.

### 3. The publish
4 of 4 keys byte-identical to HEAD. **I published only two of them** (the `code/lib/` pair).

## Decisions Made

- **Handed `lib/opal_naming.py` over as a patch rather than committing it.** Lane BASE_EXEC; edited in
  my tree only to render. `GIT_COMMIT_AUTHOR_OVERRIDE` was available and not taken.
- **Did not publish before the CTO landed.** The order gates it, and the reason is real: had that seat
  changed the renderer, the pin's bytes would move and anything published would no longer match HEAD —
  which is exactly what AC3 grades.
- **Re-rendered from the CTO's renderer rather than trusting their byte-identical claim.** It matched,
  so their one-line change is *provably* output-neutral.

## Files Modified

| path | what |
|---|---|
| `data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py` | new — generated view |
| `data/black_diamond/scripts/bronze/pull_bd_asset_dim_rest.py` | pin import, `bronze_key`, `opal_naming` and `sys` dropped |
| `.../deliverables/.../opal_naming_pin_target.patch` | the three `lib/` entries, handed to the CTO |
| `.../deliverables/.../NFRA_MCPINDEX.TO-MX-s-11...proof_of_spec.json` | new — VALID |
| `s3://opal-data-bd/code/lib/{silver_ids,trading_calendar}.py` | published by this seat |

## Blockers

**None.**

## Current State

MX-s-9, MX-s-6 step 2 and MX-s-11 all complete. MX-s-10 step 2 is clear and `0.7.0_AE_CloudOps~I` was
notified (DELIVERED). Tree clean.

**Two things recorded because they are not mine to claim otherwise:** my patch was wrong on the
`_long_scope` line and a gate caught it, not me; and two of the four published objects were written by
another actor before I reached them — plausibly `1.0.0_SA_CTO~O`, but **I did not measure who**.

## Next Steps

1. **[`0.7.0_AE_CloudOps~I`]** MX-s-10 step 2, the ad-hoc run, on this AC2+AC3 PASS.
2. **[`2.0.0_SA_COO~O`]** close MX-s-11, and flip `<status>` on MX-s-9 and MX-s-6 — all three still read
   `pending` and `task-orders/` is outside these orders' `<paths>`.
3. **[this seat]** nothing owed. Idle and reachable.
