# DEPLOY LEDGER — MDPF_GLOBAL: mdpf-gold-lambda spine hotfix (clause (vi) membership fix)

**Opened:** 2026-08-25T19:35:11Z by 0.5.0_AE_OpalETL~B (deploy-start; NEVER#6)
**Status:** **CLOSED 2026-08-25T19:41:37Z** — applied, targeted 0-diff clean, and verified on the
DEPLOYED package bytes downloaded post-apply. All 7 legs landed, nothing stranded.
⛔ **THE DEPLOY IS CLOSED; THE OUTAGE IS NOT.** See "What this ledger does NOT close".
**Ruling:** `2.0.0_SA_COO` 71246 — **PATH A, hotfix pin**. Build accepted 71265; ship on DS~N's green,
no further ruling required. Decided on mechanism, not scope-creep: the new consolidator's
`_shape_category_views` raises `SystemExit` during CONSTRUCTION (`:1190`) BEFORE the emit loop
(`:1228`), and `category-views` is ALL_SCOPE — so a refusal on any scope aborts the build **before**
the restored `aggregate-aua-timeseries` is written. Being first in that loop does not protect it.
**Ship gate:** `0.4.0_DS_ClientPlatform~N` 71267 — PASS through the production entry point.
**Fix author:** `0.4.0_DS_ClientPlatform~N` @`1234c8779e` (authorship preserved through the cherry-pick).

## The pin

`530ba66971d1dbb08f1339b556b811604e07fddc` — DS~N's spine fix cherry-picked onto the **deployed** pin
`1daf1913dd`. Minted in an **ephemeral detached worktree** (shared multi-agent checkout — a branch
switch on the main tree moves every other seat's tree); worktree torn down after build. Anchored by
local tag `mdpf-gold-hotfix-pin-20260825`.
⚠ **That tag's own sha `9165a40d0e` is the TAG OBJECT and is NOT a valid pin** — `resolve_immutable_pin`
rule 4 rejects it (`type=tag`). Pass `530ba66971`, or peel with `^{commit}`.
**Mainline UNTOUCHED. Nothing reverted. D1_CATVIEWS deliberately NOT carried.**

Cherry-pick was mechanical, not a merge judgment: the spine at the deployed pin is **byte-identical**
to the fix's parent (both 171,111 B / sha256 `a7db07bb68f465d5`), so the patch applied to exactly the
bytes it was authored against.

## Legs

| Leg | Act | Status |
|---|---|---|
| 1 | Mint + verify hotfix pin `530ba66971` | DONE (pre-deploy) |
| 2 | Local build → zip, verified at the bytes | DONE (pre-deploy) |
| 3 | DS~N exercise through `lambda_handler` (production entry point) | DONE — PASS, 71267 |
| 4 | Upload artifact + `content-sha256` metadata | OPEN |
| 5 | `safe-apply` **-targeted** `aws_lambda_function.mdpf_gold` | OPEN |
| 6 | Verify DEPLOYED package bytes carry `count_membership` = 14 | OPEN |
| 7 | Source-map record | OPEN |

## Pre-deploy measured state

```
scope at the pin        21 module->path pairs, 21 comparable, 0 unresolved
                        CHANGED 1  dim_mdpf_aggregate_aua_timeseries.py 171,111 -> 175,795 B
                        UNCHANGED 20 incl. mdpf_gold_consolidator.py 55,629 B sha256 8da6c0a19480fd98 == DEPLOYED
built zip               684,807 B  sha256 hex 5154f95d15f74763b7cecafe8364133eb0f60c36254229523fe21f9a30f69887
                                   sha256 b64 UVT5XRX3R2O3zsr+g2QTPrD2DDYlQilSP+IfmjD2mIc=   <- PREDICTED CodeSha256
spine member            175,795 B  md5 952bbc16ea07ed14cf51a497f1b4cde5  count_membership 14 OCCURRENCES
consolidator member     55,629 B   scopes_for 0        (DISCRIMINATING: same count = 5 at 1234c8779e)
member-by-member vs deployed package   21 compared, CHANGED 1, UNCHANGED 20
negative control        'Zzz_no_such_symbol_9999' in spine -> 0
resolve_immutable_pin   4/4 rules re-run against the NEW sha (not inherited): hex PASS, not-a-ref PASS,
                        1 object PASS, type=commit PASS
LIVE pre-apply          CodeSha256 sNAnYFKGr8d1eCVJCO0tuHChOXVXRwAnp83Lwjj0BUw=  LastModified 2026-08-24T12:54:28Z
```

⚠ **`count_membership` is 14 OCCURRENCES / 13 LINES** — line 1786 carries two. `grep -c` returns 13
and is not wrong; it is a different grain. Use occurrences for the post-deploy proof.

## ⛔ The root is DIRTY — the apply is TARGETED

`mdpf-pipeline` plan reads `0 to add, 1 to change, 0 to destroy`:
`aws_s3_object.mdpf_route_bindings` — **NOT MINE**, and **NOT D1_CATVIEWS-coupled** (zero commits
touching `route_bindings.yaml` since the deployed pin, absent from all six D1_CATVIEWS commits,
UNCHANGED in the 21-module scope). **Precedent: the identical rider was explicitly excluded from the
2026-08-19 rebuild of this same Lambda** (`20260819T1349Z_...`, COO option (i)). Post-apply 0-diff is
therefore **SCOPED to the target**, and a residual row is not this deploy's leftover.

## Rollback

Same-window: re-upload the prior artifact (VersionId `kBAYR2tk4JfgYmKx79_72aUw1CVzK0Mt`, 680,153 B,
CodeSha256 `sNAnYFKGr8d1eCVJCO0tuHChOXVXRwAnp83Lwjj0BUw=`) with its `content-sha256` metadata and
re-apply targeted. Bucket is versioned; the prior bytes are recoverable by VersionId.

## Close (checked only when TRUE, with evidence)

- [x] Artifact uploaded with `content-sha256` metadata. Verified on a **live `head-object`**, not the
      `cp` exit code: VersionId `r819XZni2appiJCYjDj4ack.BzFrBnJq`, ContentLength 684,807,
      `content-sha256` = `5154f95d…f69887`.
- [x] `safe-apply` targeted (HALTGT: 1 routine pending message, `HALT_ACK=1`) —
      **`Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`** The plan carried exactly the
      two expected field moves: `s3_object_version kBAYR2tk… -> r819XZni2app…` and
      `source_code_hash b0d02760… -> 5154f95d…`, confirming the metadata mechanism end to end.
- [x] Targeted 0-diff re-plan: *"No changes. Your infrastructure matches the configuration."*
- [x] Live `CodeSha256` = `UVT5XRX3R2O3zsr+g2QTPrD2DDYlQilSP+IfmjD2mIc=` — **identical to the value
      PREDICTED in this ledger before the upload.** LastModified 2026-08-25T19:38:55Z; runtime
      python3.11 / 3008 MB / 900 s unchanged.
- [x] **DEPLOYED package DOWNLOADED POST-APPLY** (proves what RUNS, not what was uploaded):
      package sha256 b64 `UVT5XRX3…` · in-zip manifest pin **`530ba66971`**, commit `530ba66971d1`
      · spine **175,795 B**, md5 `952bbc16ea07ed14cf51a497f1b4cde5`, **`count_membership` = 14
      occurrences** · consolidator **55,629 B**, sha256 `8da6c0a19480fd98`, **`scopes_for` = 0 —
      D1_CATVIEWS ABSENT, observed in the deployed artifact rather than inferred from the pin**
      · member diff vs the pre-apply package: **21 compared, CHANGED 1 (the spine), UNCHANGED 20**
      · negative control `Zzz_no_such_symbol_9999` → 0.
- [x] Source-map record updated **SCOPED to `mdpf-gold-lambda`** — a 3-line diff in one entry.
      `artifact_sha256` → the live `CodeSha256`; `last_deployed_at` → the live LastModified.
      ⛔ **`last_deployed_commit` = the BUILD PIN `530ba66971…`, deliberately, and it is NOT on
      CLOUD.** That is the honest value: the pin is the ONLY commit whose tree matches the deployed
      package. Recording `1234c8779e` would falsely imply the package matches that commit's tree,
      which it does not — the consolidator differs by design. A `verify-local` comparison will show
      deployed ≠ HEAD, and **that is TRUE**: the deployed code deliberately omits D1_CATVIEWS.
      *Semantics flagged to CTO rather than decided silently.*
      **The pipeline-wide `record-terraform-deploy.sh` was NOT run** — it would write false records
      for functions not applied (measured earlier today: 6 of 7).
- [x] **CLOSED 2026-08-25T19:41:37Z**

## Pre-state was WRONG on BOTH fields (pre-existing, now closed for this instance)

```
recorded artifact_sha256   t0w3vTNV0CpImT1EqzIdtVhUZlkwNzCrx3zA0zpM8/c=   != live sNAnYFKGr8d1… (pre-apply)
recorded last_deployed_at  2026-08-11T03:20:00Z                           != live 2026-08-24T12:54:28Z
```
Something deployed this function on 08-24 without running any recorder. **Instance closed by this
entry; the CLASS stays open** — routed to D0 / NFRA_DEPLOYLEDGER, same item raised at 70781.

## ⛔ What this ledger does NOT close

**NEVER#6 discharges on the SERVED payload, not on this deploy.** Acceptance is the scheduled
`cron(30 13)` gold run + `cron(50 13)` publish, and the bar is `global` reading
`as_of_last=2026-08-24` with `_provenance.source_keys` naming the `2026-08-24` gold partition, with
`49financial` + `inflection` moving zero data-bearing fields. DS~N's exercise is a QA read and is
**never production evidence**; their NEVER#6 ledger stays OPEN.

**Residual named by DS~N (71267 §5b), NOT closed by this deploy:** their exercise ran local
python3.12 against the same module bytes. The function runs **python3.11 with layers and an IAM
role** — import-time dependency resolution, layer contents and IAM are NOT exercised by it. A green
local run and a working deployed function are different claims. DS~N's proposed remedy (invoke the
DEPLOYED function once with `{"qa_local": true}`, a no-S3-write mode) is **routed to COO and NOT
performed here** — COO's clearance covered the ship sequence, not an extra invocation.
