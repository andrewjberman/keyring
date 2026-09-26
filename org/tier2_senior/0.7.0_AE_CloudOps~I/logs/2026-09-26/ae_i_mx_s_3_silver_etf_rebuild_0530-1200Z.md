# The silver-etf Lambda was running 73-day-old bytes, and the guard could not see a third of its own feed — 0.7.0_AE_CloudOps~I

**archetype:** DEPLOY

**Date:** 2026-09-26 (0530–1200Z)
**Task Order:** `org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-s-3.silver-etf-rebuild.md` (issued by `2.0.0_SA_COO~O`, risk class WORLD)
**Status:** AC1 PASS, AC2 PASS, AC3 PASS. Deploy CLOSED. The proof-of-spec instance is written and is INVALID on one violation that belongs to the decomposition, not to this lane.

## Objective

Rebuild `opal-assets-silver-etf` from CLOUD HEAD so the TrueShares holdings converter runs in production. The
running zip was built 2026-07-15 and its `etf_conversion.py` held **zero** occurrences of
`_convert_trueshares_holdings`; the converter landed in the repo 2026-08-24 and was fixed twice since. The
function vendors repo modules FLAT into its zip, so the source of truth had moved and the deployed bytes had not
— for 73 days. Deadline 23:30Z, the next scheduled sweep.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-iam` | `comp-iam service opal-assets-silver-etf` | "No AWS operations detected" — the preflight's required run. **Not read as a pass.** |
| `comp-find` | `comp-find 'opal-assets-silver-etf' --files --limit 40` | 638 hits / 75,475 files; HEAD=69 SURFACED=145 CONFIG=221 DOC=203. **Zero `.tf` hits** — the signal that sent me to the `for_each`. |
| `comp-find` | `comp-find 'build-and-upload' --files --limit 30` | 2,831 hits / 75,482 files. Found the builder the S3 `artifact_key` requires. |
| `comp-find` | `comp-find 'comp_constants_cli' --band HEAD --limit 15` | Measured ZERO in HEAD over 75,560 files. The zero *was* the answer. |
| `comp-read` | `silver.tf --for "where is the lambda declared..."` | 871 lines, 41 qualifiers. Pointed at `:647 function_name = "opal-assets-silver-${each.key}"`. |
| `comp-read` | `.tools/owned-paths-validate.py --for "how does it decide..."` | 532 lines. Settled the write surface **before** the first commit. |
| `comp-read` | `build-and-upload.sh --for "...what S3 metadata..."` | 612 lines, 44 qualifiers. Surfaced `--metadata content-sha256` and the CRLF-ship warning. |

**What worked:** `comp-read`'s qualifier surfacing twice changed what I did rather than confirming it. The
`build-and-upload.sh` read flagged a CRLF-ship hazard whose parity check reads green, so I checked CR bytes
inside the shipped zip (0) instead of trusting the build line. The `owned-paths-validate.py` read let me settle
the write surface with a discriminating control — DS refused on the same infra paths, every serial refused on
`org/tier0/ledger` — instead of discovering it at a commit refusal.

**What failed:** `comp-iam service opal-assets-silver-etf` returned **"No AWS operations detected"** on a
function that makes four S3 calls. It parses `lambda_function.py` only, and this handler is two lines that
delegate into the vendored modules. The tool states its own list is a FLOOR, so this is documented rather than
broken — but the shape is the dangerous one: **a green silence on the exact question the preflight asked.** I
answered it a second way (old-vs-new call-surface diff across all 9 packaged files: 0 services added, 0 calls
added, 0 removed).

**Gap found:** `record-terraform-deploy.sh` — step 7 of the canonical Lambda deploy sequence — **cannot run on
this device.** Its reader at `:259` is a bare `open(source_map_path)`, and `lambda-source-map.json` carries 23
non-ASCII characters; byte `0x9d` at position 32218 is undefined in cp1252, so it raises. Filed as row
`NFRA_MCPINDEX-Z-S12` (BLOCKING / INERT). The issuer ruled it into order `MX-s-5`.

## Deployment Sequence

| # | act | instrument | result |
|---|---|---|---|
| 1 | Re-vendor 8 modules from CLOUD HEAD | binary read/write, sha256 per module | 5 of 8 moved; `etf_conversion.py` `623568f38934` → `013dfca3b41c`; CR bytes 0 |
| 2 | Silver suite | `pytest data/assets/scripts/silver/tests/` | **305 passed, 11 skipped, 0 failed** |
| 3 | Commit gate | `.tools/commit-gate.sh` (5 files) | exit 0, clean 5 of 5 (one inherited non-ASCII WARN, not repaired) |
| 4 | Commit + drain | `safe-commit.sh`, then `safe-merge.sh` | `753fe90fb1` → CLOUD `37af228a0c`, row gate clean on the merged index |
| 5 | Open NEVER-2 ledger | `deploy_ledger.py open --lambda` | `e76b307c67`, 7 legs, entry + sentinel in one commit |
| 6 | Build + upload | `build-and-upload.sh opal-assets opal-assets-silver-etf` | sha `Zyhzyrjuh…muTg=`, 60041 B, write VERIFIED, import-closure OK on 9 files |
| 7 | Plan | `terraform plan` | **0 to add, 1 to change, 0 to destroy** — only `module.silver_converter["etf"]` |
| 8 | Apply | `.tools/safe-apply.sh` (rule 18) | "Apply complete! Resources: 0 added, 1 changed, 0 destroyed." |
| 9 | 0-diff replan | `terraform plan -detailed-exitcode` | **EXIT 0** |
| 10 | Import-health smoke | live invoke, non-S3 non-sweep event | the module's own `ValueError` at `etf_conversion.py:694`; no `ImportModuleError` |
| 11 | Step-7 record | `record-terraform-deploy.sh` | **exit 1, UnicodeDecodeError** → row Z-S12; two fields hand-written instead |
| 12 | Close ledger | `deploy_ledger.py close` | `547cd9f613`, all 7 legs proven, sentinel deleted |
| 13 | Ad-hoc QA sweep | live invoke, `{"mode":"sweep"}` | 200, no error, `converted: 0`, 4 backfill-status written |
| 14 | Tag | `git tag -a opal-assets-v0.50.0` | created LOCAL (this seat never pushes) |

## Verification

- **AC1 PASS** — the check downloads the zip from the function's *own* `get-function` Code.Location and sha256s
  it against its *own* `CodeSha256`, so the graded bytes are the running bytes. `after-issue=yes
  zip-sha==CodeSha256=yes converter occurrences=2`.
- **AC2 PASS** — entry at HEAD=1, sentinel at HEAD=no, listed OPEN/HELD=0, denominator 13 of 13 sentinels.
- **AC3 PASS** — guard `expected` moved **73 → 106** on both DIVZ and IDVZ against 106 live silver objects of
  which 33 are `fact_holdings`. `106 − 73 = 33` is exactly the feed the guard was blind to.
- **The AC3 before-arm is the control that makes the after-reading mean anything.** AC3 was run *after the apply
  but before the sweep* and still read **0 of 2 at expected=73** — identical to the issuer's dry-run at cut. So
  the deploy alone does not move the guard; the sweep does. A post-hoc PASS alone cannot separate "the rebuild
  fixed it" from "it was already right".
- Independent re-reads agreeing on three planes: builder-computed sha = `head-object` metadata = downloaded-file
  sha = live `CodeSha256`.

## Decisions Made

1. **Worked in a linked sparse worktree, then drained** (rule 14b, 8 other seats live). Sparse cone rather than a
   full checkout, per the banked OOM lesson. The cone initially omitted `org/modules/graph`, which is where
   `commit-gate.sh` resolves `comp_constants_cli` — widened once and re-ran.
2. **Ran the suite the order did not name.** The order named `data/assets/tests/`, which does not exist. I asked
   the issuer, stated my assumption, and ran `data/assets/scripts/silver/tests/` rather than blocking. Confirmed
   in msg 26041; the order was amended.
3. **Did not repair the inherited non-ASCII in `etf_schemas.py`.** The order requires byte-identity with the
   source module; "fixing" it here would fork the vendored copy from its origin. WARN-only, gate exit 0.
4. **Did not fix `record-terraform-deploy.sh`.** Shared CI tooling for 218 functions; bound 1 forbids the rider.
   One row, keep working.
5. **Hand-wrote two source-map fields, and said so in the commit and the row.** Reproduced the script's own
   documented rule (last commit touching the function's `source_dir`, explicitly *not* HEAD) rather than
   inventing one. Verified the blast radius by diffing all 218 rows: exactly 1 moved.
6. **Fired the ad-hoc sweep with the schedule's byte-identical payload**, read from `list-targets-by-rule` rather
   than guessed, so the manual path reaches no state the scheduled path does not. The 23:30Z fire stays the
   acceptance.

## Files Modified

| path | commit |
|---|---|
| `infra/aws/lambda/opal-assets/opal-assets-silver-etf/` (5 `.py` + `BUILD_MANIFEST.json`) | `753fe90fb1`, drained `37af228a0c` |
| `org/critical_paths/change_management/20260926T0844Z_…_deploy_completion.md` + `.open_deploys/` sentinel | `e76b307c67` (open) → `547cd9f613` (close, sentinel deleted) |
| `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md` (row Z-S12) | `5f7b13787a` |
| `infra/aws/lambda/ci/lambda-source-map.json` | `5f7b13787a` |
| `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/…proof_of_spec.json` | this commit |

Tag `opal-assets-v0.50.0` created LOCAL. **Push state: LOCAL** — measured by `git ls-remote origin CLOUD` at
11:5xZ (local `9f323d492d`, origin `45ddd8d948`). This seat does not push; the integrator moves CLOUD.

## Blockers

**One, and it is not this lane's to clear.** `proof-of-spec-check.py` returns INVALID on exactly one violation:

```
VIOLATION: alignment: cell_ref 'MX-s-3' does NOT exist in
  org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md
```

Verified before declaring it: the decomp's MX-s series is `MX-s-1` and `MX-s-2` only, over an 88-id space.
`MX-s-3` was cut as a supplementary act on Andrew's option 4 and its decomp row was never added. The checker
reads `cell_refs` from the TO's own criterion attributes, so no edit to my instance can clear it. L5 is
`2.0.0_SA_COO`'s and the decomposition is FROZEN mid-round, so I did not touch it. Routed to `2.0.0_SA_COO~O`
(msg at 11:58Z); `MX-s-4` and `MX-s-5` are likely the same class.

## Current State

`opal-assets-silver-etf` runs `CodeSha256 ZyhzyrjuHLi9TfRC9CFSpvPHY6Rcyq/aPgseJafmuTg=` (60041 B, python3.11,
Active, LastUpdateStatus Successful), built from CLOUD HEAD and carrying the TrueShares holdings converter. The
DIVZ and IDVZ silver guards count the holdings feed, `missing 0`, `expected 106` against 106 live. The NEVER-2
ledger is CLOSED with all 7 legs proven and the sentinel removed. Rollback remains live and single-valued: S3
object version `prXNS9i0cDwKGWlFPhbwER.0tMof8kGj` is retained by bucket versioning.

**Named, not closed, and not widened to:** the six sibling silver families vendor the *same* mirror-framework
modules from the same repo source and still carry the bytes they were last built from. Each has its own
`artifact_key`, so this act could not have moved them. Recorded in the ledger entry.

## Next Steps

1. **[`2.0.0_SA_COO~O`]** Add the `MX-s-3` row to `NFRA_MCPINDEX_DECOMP.md` — the one thing standing between this
   instance and a VALID verdict.
2. **[`0.0.0_AB_MSTR~Z`]** Push. Everything from this seat is LOCAL, including tag `opal-assets-v0.50.0`.
3. **[`0.7.0_AE_CloudOps~I`]** `MX-s-5` (the source-map ASCII fix from my own row Z-S12), then `MX-s-4`.
4. **[nobody yet]** The 23:30Z scheduled sweep is the acceptance. It should read the same 2 of 2; if it does not,
   the ad-hoc run and the scheduled run disagree and that difference is the finding.
