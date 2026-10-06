# The two round-9 tables are granted, and the grant is proven on the live roles rather than on the plan -- 0.7.0_AE_CloudOps~RV

**archetype:** DEPLOY

**Date:** 2026-10-06 (session 2026-10-05T22:50Z - 2026-10-06T00:10Z)
**Task Order:** `ETFS_RIVALS.TO-RIV-iam-1.round9-table-grants` (issuance `35e554c407`; amended `bca8c774d0`, `acc8246c10`, `2553a624f7`)
**Status:** APPLIED and VERIFIED. NEVER-2 ledger `etfs-rivalfunds-iam-1` CLOSED on all 3 legs. Drained to CLOUD at `5d75016e03`. Push state LOCAL (`git ls-remote origin CLOUD` read `01a47ac2e7`; the push is `0.0.0_AB_MSTR`'s on Andrew's word). `<status>` flip left to the issuer.

## Objective

Grant `etfs-rivalfunds-daily-role` and `rivalfunds-publish-page-role` READ on `rivalfunds/etfs/gold/security_names/`
and READ/WRITE on `rivalfunds/etfs/gold/security_universe/` (row Z-S31). The 2026-10-05 D12 Step B refresh republish
failed `holding_contribution` with `etfs-rivalfunds-daily-role ... not authorized to perform: s3:ListBucket on
opal-data-etfs`, and the sweep's `security_universe` write had no grant either; `gen_policies.py` named neither prefix.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `deploy_ledger.py` | `open` / `close-leg` x3 / `close --slug etfs-rivalfunds-iam-1` | OPENED 3 legs before the act, sentinel committed with the code at `762a984992`; CLOSED after the readbacks. Pre-open sweep of the shared tree's `.open_deploys/` with `ls -a` over a printed denominator of 29 entries: no etfs or rivalfunds entry, so a first open, not a re-execution. |
| `comp-iam gaps` | `comp-iam gaps` | Estate-wide 37 missing / 294 deny-present / 1 coverage-unknown / 3 resource-mismatch across 33 services. ZERO rows name either role I changed -- and that zero is NOT a pass (see Gap found). |
| `terraform` + `safe-apply.sh` | `plan -out`, `show -json`, `safe-apply.sh apply <file>`, `plan -detailed-exitcode` | 0 add / 2 change / 0 destroy; `Apply complete! Resources: 0 added, 2 changed, 0 destroyed`; post-apply `No changes`, exit code 0. Resolved on PATH (no `.tools/terraform.exe` on site Z). |
| `aws accessanalyzer validate-policy` | `--policy-type IDENTITY_POLICY --policy-document file://<live after doc>` | `findings=0` on both live documents; the planted-bogus-action mutant returned `INVALID_ACTION`. |
| `comp-find` | `comp-find 'etfs-rivalfunds-daily-policy|rivalfunds-publish-page-policy' --all --files` | DENOMINATOR 19 hits across 121,213 files, bands HEAD=3 SURFACED=3 CONFIG=3 DOC=10. N=1 writer of the property, so one rule read instead of one assumed. |
| `comp-read` | `--for` on `investigation_item.schema.json`; `--enumerate 'Z-S[0-9]+'` on the channel | Caught a real error before it landed (see What failed) and gave the next row id from a census (39 ids, max 39) rather than from the file's tail. |
| `safe-commit.sh` / `commit-gate.sh` / `safe-merge.sh` | per commit | commit-gate clean 1 of 1; NAMING-GATE PASS 4 graded, all four new S3 keys CONFORMANT; surprise-row-gate OK; drain graded the MERGED index, 11 files needed, 0 dropped, 0 foreign. |

**What worked:** grading the plan from `terraform show -json` instead of its prose. The prose hides elements
(`# (2 unchanged elements hidden)`); the JSON gave 45 `resource_changes`, 2 non-no-op, 0 `source_code_hash` on any
moving change and 5 of 5 `aws_lambda_function` entries `no-op` -- which is what let an UNTARGETED plan carry the
issuer's "two role policies only" requirement instead of a `-target` that by construction cannot say what else moved.

**What failed:** two instrument traps, both caught. (1) The mutant control first ran `.tools/aws` from a Python
`subprocess` and exited `rc=3221225477` (0xC0000005, an MSYS-spawn access violation) with EMPTY stdout -- which reads
exactly like "no findings". Re-run through bash it fired `INVALID_ACTION`. (2) The surprise row was first written
`hazard_standing: BLOCKING` and refused: the schema puts BLOCKING on `class` (the interruption right) and
`hazard_standing` is ARMED|INERT (future-operation harm). Also my own first equality-check loop mis-assigned the
`generated.auto.tfvars.json` reference and printed DIFFERS on two unrelated files; `git status` showed the file
unmodified, which is what exposed it.

**Gap found:** a `comp-iam gaps` zero on a changed role is not evidence. It models `(action)`, never
`(action, resource)` -- it fails GREEN -- and its own output declares 266 calls in 26 role-UNMAPPED services not
resource-checked, so the zero cannot distinguish "no gap" from "these roles were never verdicted". The oracle here is
`simulate-principal-policy` on the live roles, run one `--resource-arns` per call with `--context-entries` for the
prefix-conditioned statement and the positive control as a separate invocation.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Apply `Z-S31_IAM_GRANT_FOR_AE.patch` at HEAD | All three blob ids at HEAD equal the patch's own index lines (`66095dd96f`, `b33dd2c486`, `536a113d7a`) |
| 2 | `gen_policies.py --out` | Regenerated policy files BYTE-EQUAL to the patch's; `generated.auto.tfvars.json` byte-identical to HEAD |
| 3 | AC1 at base | `AC1 RESULT: FAIL 4` -- (a)(b) `implicitDeny` on both roles, (c)(d) PASS |
| 4 | Second worktree at the deployed pin `b8b47bb8e7` | All 10 files of the terraform dir blob-identical to CLOUD `d5114d3367`; the pin resolved BY CONTENT, not by ancestry |
| 5 | `rivalfunds_package.py` at the pin + live hash read | Five live `CodeSha256` measured (`CGLr1BNO`, `nhBoabXY`, `wLYfa47Z`, `CTEET1+c`, `RBRmqCj9`), equal to the amendment's list |
| 6 | `terraform plan -out` (UNTARGETED) | 0 add / 2 change / 0 destroy; 45 `resource_changes`, 2 non-no-op, 5 of 5 Lambdas `no-op` |
| 7 | Open NEVER-2 entry + commit code and sentinel | `762a984992` (5 files) |
| 8 | Never-widen ask to the pair | COO half SIGNED `@1c714fe3e2`; CTO half SIGNED `@4e9b59ea50` under conditions 1-6 |
| 9 | Condition 1: re-plan before the apply | IDENTICAL moving set (2 of 45), compared as sorted address/action tuples from the two plans' JSON |
| 10 | `safe-apply.sh apply <signed plan file>` | tagauthz GATE PASSED, tombstone-gate CLEAN, `Apply complete! Resources: 0 added, 2 changed, 0 destroyed` |
| 11 | Conditions 2-3: AC1, re-plan, live readback | See Verification |
| 12 | Close the entry, commit, drain | `e460141b7b`, drained `5d75016e03`; sentinel ABSENT on CLOUD with a positive control at the same ref |

## Verification

```
AC1 AFTER:
etfs-rivalfunds-daily-role   | names list/get ('allowed','allowed') | universe put/get ('allowed','allowed') | control names put / sibling get ('implicitDeny','implicitDeny')
rivalfunds-publish-page-role | names list/get ('allowed','allowed') | universe put/get ('allowed','allowed') | control names put / sibling get ('implicitDeny','implicitDeny')
positive control holding_contribution get: allowed on both roles
AC1 RESULT: PASS 0 failures          (base read on byte-identical calls: FAIL 4)

RE-PLAN:  No changes. Your infrastructure matches the configuration.   -detailed-exitcode 0
          45 resource_changes | 0 non-no-op

LIVE READBACK (aws iam get-role-policy, key-sorted against the AFTER documents):
etfs-rivalfunds-daily-role   | live == AFTER: True | statements 10 -> 10 | ADDED 4 | REMOVED 0
rivalfunds-publish-page-role | live == AFTER: True | statements  5 ->  5 | ADDED 4 | REMOVED 0
  + GetUpstreamPrefixes        R  arn:aws:s3:::opal-data-etfs/rivalfunds/etfs/gold/security_names/*
  + PutGetOwnPrefixes          R  arn:aws:s3:::opal-data-etfs/rivalfunds/etfs/gold/security_universe/*
  + ListOwnAndUpstreamPrefixes P  rivalfunds/etfs/gold/security_names/*
  + ListOwnAndUpstreamPrefixes P  rivalfunds/etfs/gold/security_universe/*

CONTROLS: validate-policy findings=0 on both live documents; planted s3:ZzzNoSuchActionName9999 -> INVALID_ACTION.
          AC1 re-run: identical verdicts (stable on a live plane).
```

Mode 4 of the simulator's false-deny set (a wrong-grain ARN reading `implicitDeny` even for an admin principal) is
excluded BY CONSTRUCTION rather than by argument: the four calls that read `implicitDeny` before the apply are
byte-identical in principal, action, resource ARN and context entries to the four that read `allowed` after it.

## Decisions Made

1. **Staged the plan at the deployed pin rather than using `-target`.** The issuer's amendment `acc8246c10` admitted
   both. A `-target` plan cannot state what else would have moved, which is exactly what a never-widen half needs; a
   full plan at the pin reads 0/2/0 over the whole root. Cost: one extra worktree and one package build.
2. **Full worktree over a sparse cone, chosen on a measurement.** 25.07 GB of 63.46 GB free RAM, 28.1 h uptime; the
   banked OOM was measured at 0.2-4.6 GB free. The cone would have excluded `infra/`, which this cell needs.
3. **Appended the surprise row in the SHARED tree, not the worktree** -- rule 14b inverts for an append-only shared
   channel, because two branches appending to one file land at the same offset and guarantee a conflict.
4. **Did not mint a `etfs-rivalfunds-v*` tag** (cloud-ops Rule 6). `git tag -l` reads ZERO tags for this pipeline under
   either candidate prefix, so there is no series to continue and the pre-flight's own warning is not to assume a
   version. Surfaced here rather than inventing a convention; raise it if the pipeline should carry one.

## Files Modified

| Path | Commit |
|---|---|
| `infra/aws/terraform/etfs-rivalfunds/gen_policies.py` | `762a984992` |
| `infra/aws/terraform/etfs-rivalfunds/policies/etfs-rivalfunds-daily-lambda.json` | `762a984992` |
| `infra/aws/terraform/etfs-rivalfunds/policies/rivalfunds-publish-page-lambda.json` | `762a984992` |
| `org/critical_paths/change_management/20261005T2322Z_etfs-rivalfunds-iam-1_deploy_completion.md` | `762a984992` (open) -> `e460141b7b` (CLOSED) |
| `org/critical_paths/.open_deploys/etfs-rivalfunds-iam-1.json` | created `762a984992`, removed `e460141b7b` |
| `org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md` | `5dc2e64de2` (row Z-S40) |
| `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.7.0_AE_CloudOps~RV/` (instance + plan text + 4 policy documents) | `e460141b7b` |
| drain | `5d75016e03` |

`generated.auto.tfvars.json` is in the order's `<paths>` but regenerates byte-identical to HEAD, so it never moved.

## Blockers

**None.** Nothing is owed by this seat on this order.

Row `ETFS_RIVALS-Z-S40` (filed `@5dc2e64de2`, class BLOCKING, hazard INERT) was DISARMED by the issuer at
`2553a624f7` within the session: the order's section 5 directed the instance to
`deliverables/0.9.0_WK_ETFS_RIVALS~RV/`, which owned-paths clause 4 refuses to this serial, because the cell went to
an AE lane rather than a worker slot. The amendment granted `deliverables/0.7.0_AE_CloudOps~RV/`, and the amended
order bytes were merged onto the working branch (`fec8fb400b`) because the lane gate reads `<paths>` from the order
file on the branch where the commit lands. It never held the apply.

## Current State

The two inline role policies are live with four additions each and zero removals. A re-plan reads 0-diff, so the
committed configuration and the deployed state agree. The NEVER-2 entry is CLOSED with nothing stranded, and its
close has reached CLOUD. Both never-widen halves are on CLOUD.

**The capability is granted; it is NOT proven to serve data.** AC1's oracle is the policy simulator, which evaluates
authorization and touches no object. Reading AC1 PASS as "the 10-05 `holding_contribution` failure is fixed" would be
the ABSENT-equals-EXERCISED-AGAINST error.

## Next Steps

1. **[`2.0.0_SA_COO~RV`]** Flip `<status>` on the order, and decide whether the 10-05 `holding_contribution`
   republish is wanted at all -- the COO half notes the fail-soft repair already serves it OK. That write is out of
   this cell's bounds.
2. **[`1.0.0_SA_CTO~Z`]** CTO half condition 6: the capability is proven by data only at tomorrow's vehicle --
   `nm-3`'s stored-names read and `su-2`'s universe write -- graded with the other round-9 ruling-6 first-run reads.
3. **[`0.0.0_AB_MSTR~Z`]** The push. Everything from this seat is LOCAL on CLOUD; `git ls-remote origin CLOUD` read
   `01a47ac2e7` at 23:4xZ and neither `762a984992` nor `5dc2e64de2` is an ancestor of it.
4. **[unowned, surfaced not filed]** `audit-archive-invoker.py` at startup reported `LIVENESS/STALE-BASELINE`
   (baseline `2026-10-04T190905Z`, 27.8 h, >24 h, with an uncaptured tail), one `INTEGRITY/NON-APPEND-EDIT` on
   `org/mcp/agent-spawn-audit.log` (first divergence line 13871) and four `ERROR-FAILCLOSED` baseline-missing rows.
   Device hygiene, outside this order; named here for whoever owns the archive cadence.
