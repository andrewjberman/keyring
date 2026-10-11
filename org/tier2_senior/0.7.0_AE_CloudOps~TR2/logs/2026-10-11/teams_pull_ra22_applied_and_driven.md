# The Teams pull now survives a refused listing: TR-ra-22 applied, driven and graded against A4 on every cell — 0.7.0_AE_CloudOps~TR2

**archetype:** DEPLOY

**Date:** 2026-10-11 (UTC; 2026-10-10 evening US Eastern)
**Task Order:** NFRA_TRNSPT.TO-APPLY-ra22.teams-pull-refused-read-fix-dell2 (AMENDMENT 2)
**Status:** COMPLETE

---

## Objective

Deploy the merged Teams-pull fix: rebuild the transcripts-pull zip at the AMENDMENT 2 pin, `safe-apply`
it TARGETED at `aws_lambda_function.pull` only, then ONE driven invoke as the proof. The scheduled pull
had failed on every fire since 2026-10-09T16:00Z (row `NFRA_TRNSPT-D2-S16`); the next fire is
2026-10-12T13:00Z, which was the real deadline.

This order was HALTED earlier in the session (see
`teams_pull_ra22_halted_before_apply.md`) because the first pin caught only a refused row READ, not a
refused LISTING. AMENDMENT 2 re-pinned it to the merged fix and the first CTO half went VOID.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-schedule | `comp-schedule --drift` | PASS | Preflight RUN. 1 armed gate as an exception (`G-3`, owner CTO), nothing armed on this lane or root. Its C2 carrier independently gave the per-tree open-deploy denominator step 0 wants. |
| comp-adversary | `comp-adversary compose <packet>` | PASS | Preflight RUN, against the re-cut packet rather than the superseded one. 3/3 cited commits VERIFIED, 4/4 cited paths stable, 20 uncited siblings with 12 digested under a declared budget. Nothing contradicted the packet. |
| comp-find | `comp-find --files '"genre": *"DEPLOY"' org/tier2_senior org/missions` | PASS | 89 hits / 32056 files scanned, denominator printed. Located the DEPLOY-genre instance convention. |
| proof-of-spec-check | `proof-of-spec-check <instance> TR22-ra22-AC1 --governing-order <order>` | PASS | VALID rc=0 on the second pass; 4 of 4 controls discriminate, 0 DID-NOT-DISCRIMINATE, rollback named. |
| comp-iam | not run | SKIPPED | DECLARED-NOT-APPLICABLE by the order's own preflight: no new AWS call in the changed code; role, policy and KMS grant unchanged and outside the target. |
| comp-pipescript | not run | SKIPPED | No gold script and no gold run in this act. |

**What worked:** `comp-schedule --drift` answered the gate question and step 0's per-tree denominator in
one read. `proof-of-spec-check` earned its keep: its first pass named nine defects precisely enough to fix
without a second guess, including two enum violations I would have shipped.
**What failed:** nothing. Two rail denials (R6/F4 piping a census into `head`; R1/F1 a recursive grep),
both correct, both with a REMAINDER line that ran as given.
**Gap found:** none in the tools; one in my own reading, caught by a gate. A surprise row id's middle
segment is a DEVICE COORDINATE from the device register (`D1`, `D2`, `Z`), which neither the id grammar
(`SURPRISE_ID_RE`) nor the schema's own field list states in a place an author reads first -- the grammar
admits `A2` and the register does not. The row gate carries the real rule and names the registered set in
its refusal, so the cost was one refused commit. Recorded in row `NFRA_TRNSPT-D2-S17`'s notes.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Open deploy ledgers read per NEVER-2 | 16 live worktrees read with `ls-tree`; per-tree denominators printed (shared 19, max 29); union 78 distinct entry names. The one NFRA_TRNSPT entry present in the shared tree, `nfra-trnspt-a18-second-reader-laptop-20261009`, is HELD-SOVEREIGN-GATED on IAM/KMS targets, NOT on `aws_lambda_function.pull` — no collision. `irpt-anlreq-t1-commentary-store-and-lambda-20261009` is another seat's and untouched. |
| 0 | Ledger OPENED | `org/critical_paths/change_management/20261011T0326Z_nfra-trnspt-tr-ra22-teams-pull-fix-dell2-20261011_deploy_completion.md`, 3 legs, committed at `c513e72fa1` |
| 1 | Precondition, 3 live reads (03:27:27Z) | pull `taFbGTCU...6HA=` MATCH; mail pull `VGIq85Xx...uMNY=`; commentary `ResourceNotFound`. Condition 1 satisfied. |
| — | Pre-act dry run of the criterion | `R22-RA22-FAIL the pull still runs the pre-fix zip` rc=1 — FAIL as the order predicts, so the check discriminates |
| 2 | `bash infra/aws/lambda/transcripts-pull/build.sh` | 89 files, 886783 bytes, base64 sha256 `AI4UQD0ME+ABza1X0BrBjGjpqjN7f2fc0Cdxb88aA/I=` |
| 3 | `terraform plan -target=aws_lambda_function.pull` | ONE resource block, `aws_lambda_function.pull will be updated in-place`; only `source_code_hash` and `last_modified` differ; **Plan: 0 to add, 1 to change, 0 to destroy**. Condition 2 satisfied. |
| 3 | `safe-apply ... apply -target=aws_lambda_function.pull -auto-approve` | rc=0 at 03:36:14Z |
| 4 | After, 3 live reads (03:37:01Z) | pull `AI4UQD0ME+...aA/I=` **equals step 2's zip hash**, State Active, LastUpdateStatus Successful; mail pull UNCHANGED at `VGIq85Xx...uMNY=`, LastModified still 2026-10-07T23:59:05Z; commentary still `ResourceNotFound`. Condition 3 satisfied. |
| 4 | Targeted 0-diff re-plan | `No changes. Your infrastructure matches the configuration.` |
| 5 | ONE invoke, empty event (03:38:44Z → 03:40:10Z, 86 s) | StatusCode 200, FunctionError null, no `errorMessage` key. 4 series entries. Graded against A4 both ways: MATCH on every cell. |
| 6 | Ledger CLOSED | All 3 legs proven; `.open_deploys` sentinel removed |
| — | Criterion check, post-act | `R22-RA22-OK pull=AI4UQD0M local_zip=AI4UQD0M mail=VGIq85Xx commentary=ABSENT` rc=0 |

**Not done, deliberately:** no tag was minted. Deployment rule 6 asks for one per 0-diff apply, but this
root carries exactly ONE tag (`transcripts-v1.0.0`) across all of its applies, so per-deploy tagging is
not its practice; inventing it mid-round, against an order whose bounds are "no other resource, root, key
policy or function", is the issuer's call, not the applier's. No core-document edit either: a code hash
moved, which is not a structural change, and `pipeline_inventory.xml` belongs to the base seat.

---

## Verification

**The driven invoke, graded against packet A4 (condition 4). Counts and statuses only — the order's bounds
bar transcript text, bearers and meeting ids from any file or message, and the returned record carries ids.**

| series | listed | held | landed | expired | read_refused | refused | A4 expected | verdict |
|---|---|---|---|---|---|---|---|---|
| `monday_meeting` | 20 | 16 | 0 | 0 | **4** | 0 | 20 / 16 / 4 read_refused | MATCH |
| `ocio_ic` | 8 | 7 | **1** | 0 | 0 | 0 | 8 / 7 / 1 would land | MATCH |
| `asset_management_ic` | 7 | 7 | 0 | 0 | 0 | 0 | 7 / 7 | MATCH |
| `research_meeting` | 0 | 0 | 0 | 0 | 0 | **1** | refused 1 | MATCH |

`totals`: listed 35, new 1, held 30, expired 0, refused 1. All four `monday_meeting` refusals read
`GatewayGraphError status=502`; `research_meeting`'s reads `list GatewayGraphError status=502` — the
listing-side class that AMENDMENT 2 exists to catch.

**No landing count above A4's**, so nothing beyond the one covered `ocio_ic` catch-up landed. That one
landed bronze and silver (`LANDED` plus `SILVER-WRITTEN`).

**The two state objects the pre-fix code never wrote on a failing fire now exist:**

| object | head-object |
|---|---|
| `s3://opal-data-transcripts/teams/transcripts/state/pull_runs/run=2026-10-11T03:38:57Z/run.json` | 4183 bytes, 2026-10-11T03:40:10Z, `aws:kms` |
| `.../state/listing_snapshots/run=2026-10-11T03:38:57Z/listing.json` | 3255 bytes, 2026-10-11T03:40:10Z, `aws:kms` |

**Build-input control (rule 22a CODE layer).** The zip that `build.sh` replaced hashed to
`taFbGTCUAOhM+97EVJi3AfqqeBCV+FIUSLZ8Z4Ge6HA=`, equal to the then-live `CodeSha256` — so the local zip was
provably the deployed build input, not merely a file of the right name. It was preserved off-repo before
the rebuild. The pin was likewise resolved by CONTENT, never by `merge-base`: the bundled
`data/transcripts/scripts/teams/pull.py` hashes to git blob `8aef45f2fc02…`, read from INSIDE the built zip.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Supplied `second_reader_trust_principal_arns` from APPLIED STATE, via a tfvars file OUTSIDE the repo | The root refuses to plan without it (`readers.tf:15`, no default, no tfvars). The variable reaches the KMS key that `pull.tf` depends on, so a wrong value could surface a reader-role diff. Reading the live role's trust policy (`aws iam get-role` → exactly `user/Opal_Terminal`) makes the value match the world by construction. Keeping the file out of the repo means no committed artifact asserts a routing decision that is Andrew's. |
| Verified cleanliness over EVERY `build.sh` input, not just the packet's 12 files | The preflight names "a zip built from a tree carrying other seats' uncommitted edits" as a hazard, and the shared tree had 7 live COO lanes committing throughout. 0 dirty and 0 differing from the pin across all inputs is the stronger statement, and HEAD moved three times during the session without ever touching one. |
| Preserved the replaced zip, though condition 6's rollback is a reproducible rebuild | Two independent rollback routes cost one file copy on a WORLD act. Neither was needed. |
| Ran `comp-adversary` after the re-pin, not before | Composing it against the superseded packet would have produced a declaration about bytes nobody would act on. Stated in the halted-session log at the time, not rationalised after. |
| Minted the surprise row as `NFRA_TRNSPT-D2-S17`, after two wrong attempts | The id's middle segment is a DEVICE COORDINATE read from the device register, not a lane name: only `D1`, `D2` and `Z` are registered, so every dell2 writer shares the `D2-S<n>` sequence and an applier has no namespace of its own. I tried `TR2` first (unparseable under the id grammar: one letter plus digits per segment) and then `A2` (parseable but not a registered coordinate), reaching for a private namespace to dodge a collision with `2.0.0_SA_COO~T2`, which writes the same sequence this round. The row gate refused both and was right. `S17` was the next free index across all 24 channel documents; the gate's uniqueness check, not a private namespace, is what keeps two writers off one index. |
| Did not tag, did not touch the core document | See "Not done, deliberately" above. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/transcripts-pull/dist/transcripts-pull.zip` | Rebuilt at the pin (build product, `dist/` is never committed) | No — build product by design |
| `org/critical_paths/change_management/20261011T0326Z_..._deploy_completion.md` | Opened, 3 legs closed, entry CLOSED | Opened at `c513e72fa1`; closes ride this commit |
| `org/critical_paths/.open_deploys/nfra-trnspt-tr-ra22-...json` | Sentinel created then REMOVED by the close | This commit |
| `org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md` | +1 row, `NFRA_TRNSPT-D2-S17` (76 rows, array re-parsed) | This commit |
| `org/tier2_senior/0.7.0_AE_CloudOps~TR2/deliverables/....proof_of_spec.json` | New, VALID rc=0 | This commit |
| this log | New | This commit |

No product file, no `.py`, no Terraform source touched. The only world change is one Lambda's code hash.

---

## Blockers

None. The order is executed end to end and the ledger is closed.

Two items owned elsewhere, each named so neither is stranded:

- **`2.0.0_SA_COO~Y2`** — open ledger `irpt-anlreq-t1-commentary-store-and-lambda-20261009` resumes against
  the shared `dist/` zip, which has MOVED to `AI4UQD0ME+…aA/I=`. That seat must re-read the zip before its
  steps A2 and B. The issuer told it (msg 3939); this lane did not touch its entry.
- **`1.0.0_SA_CTO~DELL2` with `2.0.0_SA_COO~T2`** — row `NFRA_TRNSPT-D2-S17`: the defaultless
  `second_reader_trust_principal_arns`. A committed tfvars (or a default) carrying the routing Andrew
  already named would stop it being a per-applier guess. Not this lane's decision.

---

## Current State

Written for a reader with zero prior context. **`teams-global-transcripts-pull-lambda` now runs the merged
fix.** Its live `CodeSha256` is `AI4UQD0ME+ABza1X0BrBjGjpqjN7f2fc0Cdxb88aA/I=` (LastModified
2026-10-11T03:36:14Z, State Active), built from `data/transcripts/scripts/teams/pull.py` at git blob
`8aef45f2fc02…` — the AMENDMENT 2 pin, verified from inside the zip. The two functions that share that zip
did NOT move: `outlook-global-transcripts-pull-lambda` is still on its own older zip
(`VGIq85Xx…uMNY=`, 2026-10-07T23:59:05Z) and `outlook-global-commentary-draft-lambda` is still
`ResourceNotFound`, because the apply was targeted at `aws_lambda_function.pull` alone and a targeted
0-diff re-plan reads clean. **The behavioural change:** a 502 on a series LISTING no longer ends the
function — the driven invoke returned StatusCode 200 with no `errorMessage`, recorded `research_meeting`
as `refused 1`, and wrote both a run record (4183 B) and a listing snapshot (3255 B) that the failing
fires never produced. One `ocio_ic` transcript landed bronze and silver, the catch-up both halves cover,
and no series landed more than A4 measured. The four aged-out Monday meetings remain unrecoverable through
the gateway and read `READ-REFUSED GatewayGraphError status=502`, as expected and explicitly not covered.
The change ledger at
`org/critical_paths/change_management/20261011T0326Z_nfra-trnspt-tr-ra22-teams-pull-fix-dell2-20261011_deploy_completion.md`
is **CLOSED** with all three legs proven and its sentinel removed. `R22-RA22-OK` rc=0 where the same check
printed `R22-RA22-FAIL` before the act. The next scheduled fire, **2026-10-12T13:00Z**, is the first
unattended exercise and is deliberately NOT claimed as evidence here.

---

## Next Steps

1. **[`2.0.0_SA_COO~T2`] Flip this order's `<status>` and grade `TR22-ra22-AC1`** — the proof instance is
   written and VALID; the status flip and the grade are the issuer's, never the assignee's. The report to
   the issuer carries every figure.
2. **[`2.0.0_SA_COO~Y2`] Re-read the shared `dist/` zip** before steps A2 and B of ledger
   `irpt-anlreq-t1-commentary-store-and-lambda-20261009`. It is now `AI4UQD0ME+…aA/I=`, not `taFbGTCU…6HA=`.
3. **[`2.0.0_SA_COO~T2` / `1.0.0_SA_CTO~DELL2`] Settle row `NFRA_TRNSPT-D2-S17`** — commit the reader trust
   value (tfvars or default) so the next applier on this root cannot guess it and widen the role.
4. **[`0.7.0_AE_CloudOps~TR2`] Nothing.** This lane is IDLE and holds no other order. The 2026-10-12T13:00Z
   fire needs no act from it; if the issuer wants that fire read, that is a new order.
