# The BD asset dimension comes back by REST, and the super-class was never absent — 0.4.0_DS_ClientPlatform~D

**archetype:** IMPLEMENT

**Date:** 2026-09-28
**Task Order:** NFRA_MCPINDEX.TO-MX-s-9 (bd-asset-dim-rest), issued `0c557f19da` by `2.0.0_SA_COO~O`
**Status:** COMPLETE (AC1/AC2/AC3 all PASS; proof instance VALID rc=0)

## Objective

The 49F Black Diamond asset dimension has been frozen since 2026-04-14 because the portal downloader
dies at BD's MFA (row Z-S8, 69 of 119 runs failed since 2026-06-23). Andrew's word was to try a REST
pull rather than build a second crawler. This cell builds the bd-tree bronze module, makes ONE ledgered
discovery read, makes ONE ledgered pull, and reports — the silver dim rebuild is MX-s-6 step 2, not this.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `comp-find 'rest api pull for those tables' -- 'org'` | 6 hits / 59,203 files. Located the Andrew quote and showed the TO's pin for it is the WRONG record. |
| `comp-find --name` | `build_bd_assets_dim.py`, `naming-gate*` | Found the consuming builder and the gate; denominators printed. |
| `comp-freshness` | `artifact s3://opal-data-bd/silver/allocations/` | PASS at 29.2h — the served half of the step-1.1 allocation answer. |
| `naming-gate.py` | `--diff <new module>` | REFUSE 16 → REFUSE 2 → WARN 1, run directly instead of rediscovering the verdict through safe-commit. |
| `proof-of-spec-check.py` | on this instance | INVALID (2 schema enum violations) → **VALID rc=0**. |
| `comp-schedule` / `comp-iam` / `comp-adversary` | not run | All three DECLARED-NOT-APPLICABLE by the order's own preflight, and the declarations held as executed. |
| `comp-pipescript` | not run | Known coverage gap: the BD asset-dim scripts resolve in no indexed pipeline. Recorded as a gap, never as a skipped check. |

**What worked:** running `naming-gate.py` on a bare diff turned an opaque commit refusal into a
three-step measurable fix. `comp-find` with a printed denominator is what caught the mis-pinned citation.

**What failed:** nothing silently. The rail correctly refused two of my own commands (a raw `find`, and
a census piped into `tail` which would have erased its denominator); both were re-run clean.

**Gap found:** the naming gate's context rule has no "already at HEAD, mints nothing" grandfather, which
its S3Key rule does have. Row `NFRA_MCPINDEX-Z-S33`.

## Work Completed

### 1. Authority resolved from the RECORD, not from memory
The vendor NEVER line applies to BD REST. I asked the two questions separately: does the rule apply
(yes) and has the word been given (yes) — then verified by printing the bytes at the pin rather than
grepping for the quote. `@785fc4d71f` states "That word is now given". **The quote the TO attributes to
that pin is not in those bytes** — it is genuine but belongs to the ~20:1xZ refinement. Reported, not
silently corrected. The MECHANISM half (R-21) is satisfied because the pull is a script, not an agent turn.

### 2. The module
`data/black_diamond/scripts/bronze/pull_bd_asset_dim_rest.py`. Auth inlined from the vendor catalog (no
cot cross-import). Scope, vendor, firm short-code, session secret and routed bucket are all read from
the registry at import; a positive control asserts the derived values equal the four the live pull used.

### 3. The discovery read — the anticipated outcome was overturned
`asset_super_class` is **dim id 7**, not absent, found by scanning 148 qt4 dimensions. Also measured:
the persisted `AssetDimTXNs_OpalCapital_Daily` is queryType **Transactions (qt2)**, which is the concrete
reason the earlier qt2 read found no route to `assetClass`/`segment`.

### 4. The pull
12,132 rows, one per `asset_id`, 15 columns, as-of Friday 09/25/2026 (the last COMPLETED trading day —
the run fired ~01:2x ET Monday, pre-market). Reused persisted qt4 template 486228's envelope, so no
vendor-side template was created.

## Decisions Made

- **as-of = `prev_trading_day`, not `expected_last_trading_day`.** The latter returns today because today
  IS a trading day; that answers the frontier question, not the settled-data question.
- **Bronze ships the VENDOR's column name** `asset_super_class`, not `asset_super_class_bd`. The silver
  builder already does that rename; bronze should not pre-empt silver's schema.
- **Bucket `opal-data-bd`** — the registered, provisioned, routed alias — over `address()`'s LGIC tier
  home, under rule 30's non-application for existing pipelines. Recorded as a departure, not taken silently.
- **Did NOT flip the TO `<status>`**: `task-orders/` is not in this order's `<paths>`.

## Files Modified

| path | what |
|---|---|
| `data/black_diamond/scripts/bronze/pull_bd_asset_dim_rest.py` | new — the bronze module |
| `.../deliverables/0.4.0_DS_ClientPlatform~D/EGRESS_LEDGER_MX-s-9.md` | new — 3 ledgered vendor ops |
| `.../deliverables/0.4.0_DS_ClientPlatform~D/bd-asset-dim-rest.result.md` | new — OUTPUT_KEY + the answers |
| `.../deliverables/0.4.0_DS_ClientPlatform~D/discovery_MX-s-9.json` | new — machine discovery record |
| `.../deliverables/0.4.0_DS_ClientPlatform~D/...proof_of_spec.json` | new — VALID rc=0 |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | appended row `Z-S33` |
| `s3://opal-data-bd/blackdiamond/49financial/bronze/assets_dim_rest/2026-09-28/` | new bronze object |

## Blockers

**None.** Three things are declared rather than blocking:
1. The order's **two-call bound was exceeded by one** — a response-shape defect in my own parser fired an
   orphan run (541481). Ledgered in full rather than netted out.
2. The **TO's citation is mis-pinned** — genuine quote, wrong record. Substance unaffected.
3. The **naming gate's context rule** has no in-lane remedy for a new file that must emit an existing
   `_bd` column. Worked around legitimately here; row Z-S33 carries it to the gate owner.

## Current State

MX-s-9 is COMPLETE on all three criteria, verified against the SERVED object rather than the build
buffer. The bronze object exists and is unique on `asset_id`. The union counts MX-s-6 step 2 needs are
measured: union 12,141; 1,204 pull-only; 9 frozen-only. Nothing served was moved, no schedule was built,
no alarm was built, and nothing was pushed.

## Next Steps

1. **[`2.0.0_SA_COO~O`]** close MX-s-9 (the `<status>` flip is the issuer's — `task-orders/` is outside
   this order's `<paths>`), and cut MX-s-6 step 2, which now has its union counts.
2. **[this seat]** MX-s-6 step 2 on that cut: rebuild the dim as the union, latest-wins per `asset_id`,
   stating both counts.
3. **[`1.0.0_SA_CTO~O`]** row `Z-S33` — one ask: should the naming gate's context rule carry the same
   "already at HEAD, mints nothing" grandfather its S3Key rule already has?
