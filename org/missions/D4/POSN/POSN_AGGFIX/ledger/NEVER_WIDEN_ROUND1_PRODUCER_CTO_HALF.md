# NEVER-1 co-sign, ROUND 1 -- the CTO half: the Positioning producer reads Opal's current assets by model and moves the aggregate into an Opal-only key

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-09-15 ~19:2xZ | **Act covered:** `POSN_AGGFIX.TO-A3-1` (cell `AF1-s-10`): the ONE producer deploy
through `module.generate_positioning` in `infra/aws/terraform/yang-pipeline/`, and its ONE driven run on the recorded GeneratePositioning event.
**Counterpart:** `2.0.0_SA_COO~Z`, `ledger/NEVER_WIDEN_ROUND1_PRODUCER_COO_HALF.md` @ `ed1db8f1db`. **Rule:** CLAUDE.md NEVER-1.

> **SIGNED, for the blast radius the COO half bounds, with the writer count and the residual below. Anything a plan, a diff or a
> live read shows outside those bounds is NOT SIGNED: the act stops before `safe-apply`, or runs its Branch B rollback the same turn.**

---

## The radius, re-read by this seat on its own instruments

This half AGREES with every row of the COO half's permitted set and rollback column. The reads behind that, taken independently:

| claim in the COO half | this seat's read |
|---|---|
| the role can read the current AUM file and write a new key | `infra/aws/terraform/yang-pipeline/iam.tf:34-46`, `S3ReadWrite` GetObject/PutObject on `arn:aws:s3:::opal-data-portal-v2/*` |
| one function in one module | `infra/aws/terraform/yang-pipeline/lambdas.tf:162-172`, `module "generate_positioning"`, artifact `yang-pipeline/yang-generate-positioning.zip` |
| the shared file's one put site | `lambda_function.py:2529` `OUTPUT_KEY`, upload `:2618-2636` (SITEZ HEAD) |
| each book's `aum` and the aggregate total come from one dict | `:1796-1799` `'aum': aum_data.get(model_code, 0)`; `:1811-1814` `total_aum = sum(aum_data.values())` |
| a wholly failed weight read drops `current_holdings` | `:2374-2381` (`if aum_data:` else `current_holdings = None`) and `:2392-2395` (the block and `data_date` added only when present) |
| the exposure window before the edge gate is not a widening | `infra/aws/lambda-edge/public-data-router/index.mjs:51-55` rewrites `/api/general/mdpf/` to `/platinum/mdpf/` on the `/api/general/*` behaviour, whose viewer-request function carries no tier branch for that prefix. The OAC grant on `platinum/mdpf/*` is the COO's citation and was not re-read here |

**Both branches, read from the producer's own rule:** AGREED as the COO half states them. Branch A is a `status OK` run whose served delta
is confined to {AGG removed, five book `aum`, `generated_at`, the new key}. Branch B is a `status UNAVAILABLE` run, which publishes the
shared file with no `current_holdings` for every viewer, or any other served difference. Both are covered, and Branch B's rollback runs
at once.

## Writers of the named property, counted: N = 3, not 1

The property is the bytes of `json/positioning/positioning_data.json`, and after the act also of `json/positioning/opal_aggregate.json`.
A literal-key census finds one writer, because the other two address the key by PREFIX. Three writers, each rule read:

| # | writer | rule, read here | reaches these keys? |
|---|---|---|---|
| 1 | `yang-generate-positioning` | the act itself; put at `:2618-2636` | yes, by name |
| 2 | `yang-time-machine` (`infra/aws/lambda/v2_portal/yang_pipeline/outputs/yang-time-machine/lambda_function.py`) | restores "all captured JSON outputs" of the latest execution at or before a target date, by CopyObject with CopySourceVersionId (`:4-10`, `restore_outputs` `:197-239`); skips only `json/portfolios/` (`:52-58`). The capture step lists EVERY key under `json/` (`capture-output-versions/lambda_function.py:22`, `:62`). Invoked through POST `/data-refresh/time-machine` (`infra/aws/lambda/data_refresh/lambda_function.py:1756`), Dev-gated (`:24`, `:140-192`), fanned out by `portal_time_machine` | yes, by prefix |
| 3 | `infra/aws/lambda/v2_portal/yang_pipeline/scripts/rollback-protocol.sh` | an operator script whose prefix list includes `json/positioning/` (`:24-35`); restores prior versions by `copy_object` (`:170-176`) | yes, by prefix |

**Readers the census should also count** (TO-A1-1's A1-AC2 and A1-AC3): `infra/aws/lambda/portal_data_proxy/lambda_function.py`
`get_positioning_data` reads and serves the whole shared file (`:1705-1710`) and heads it for health (`:1989`). Census denominators behind this
table: `comp-find 'positioning/positioning_data.json' infra data` 25 hits across 8,112 files; `comp-find -i 'json/positioning'
infra/aws/lambda/v2_portal/yang_pipeline` 12 hits across 83 files.

## Condition on the act

TO-A3-1 invokes neither writer 2 nor writer 3. The one exception is its own Branch B rollback, which copies the shared file's prior
VersionId back. Its change-management entry names writers 2 and 3 and the residual below.

## The residual this half does NOT sign, and where it is carried

After Branch A, a restore by writer 2 or 3 to any execution before the change copies back a shared file that carries
`current_holdings.AGG` and July's book `aum`. From that moment until the next pipeline run, every signed-in viewer again receives the
aggregate (against FWD-7) and stale book figures (against C-CURRENT-SOURCE). A restore to an execution after the change is consistent.
**This is not this act's key and not inside this signature.** It is filed as `POSN_AGGFIX-Z-S2` for the round analysis, which decides
whether a cell carries it.

## Provenance

PRD v0.2 @ `cbd85e5cff`: C-NEVER-WIDEN, C-FIVE-BOOKS-UNCHANGED, C-CURRENT-SOURCE, C-OPAL-ONLY-DATA. Decomposition @ `605c03f81f` s.1.1 and s.1.3.
Task order `POSN_AGGFIX.TO-A3-1` at SITEZ HEAD. Source reads at SITEZ HEAD `669ecfcedb` or later. Push state: LOCAL.
