# DEPLOY LEDGER: mdpf-daily-runner grant -- portal/gold/mdpf/* (accrual bridge write set)

**Applied:** 2026-07-29T17:37Z by `0.7.0_AE_CloudOps~A` · **Commit:** `81c2120fad`
**Status:** **CLOSED 2026-07-29T17:57Z -- APPLIED + VERIFIED. C3 PARTIALLY EXERCISED, recorded as such
(see "ACCEPTANCE" below). NOT recorded as fully met.**

## ⚠ PROCESS NOTE, RECORDED AGAINST MYSELF
NEVER#6 wants a deploy-completion ledger **opened at deploy-start** and closed at completion. This entry
was written **after** the apply, not before it. The apply itself was authorized and gated correctly
(plan reported to CTO and applied only on his explicit word), and nothing was stranded -- but the ledger
discipline ran a step behind the deploy, and recording that is cheaper than a clean-looking entry that
hides it. The window between apply (17:37Z) and this entry (17:57Z) had no ledger cover.

## Authorization
- **CTO ruling 20260729T172339Z** (fix-forward; freeze lifted NARROWLY to targeted IAM, explicitly NOT
  `module.emitter`), amended by **164629Z** (acceptance must be a real write) and **165423Z**
  (`PutObject` + `GetObject`, not PutObject alone).
- **COO NEVER#3 co-sign 20260729T172238Z.** RULED A SERVE-WIDEN: the grant ADDS a principal to a tree
  that feeds the served plane, and the ABSENCE of the grant was itself the control (`iam.tf:410-412`).
- **CTO apply word 20260729T173213Z**; acceptance ruling **175422Z**.

## The change
```
Sid      = "AssetsPortalGoldMdpfAccrualBridgeWrite20260729"
Action   = ["s3:PutObject", "s3:GetObject"]
Resource = "arn:aws:s3:::opal-data-assets/portal/gold/mdpf/*"
```
**BOTH ACTIONS OR NEITHER.** `head_object` IS `s3:GetObject`, and `build_portal_gold_accrual.py:253-255`
wraps the existence probe in a BARE `except Exception` that swallows AccessDenied into `exists=False`.
With PutObject alone the R5 anti-clobber SKIP (`:256-258`) becomes **structurally unable to fire** and
every dated partition is silently overwritten each run, rc=0. **A PutObject-only grant is strictly worse
than no grant.** Both actions ship in ONE statement so no apply path can land them separately.

**WILDCARD, not firm-scoped -- deliberate exception** to `AssetsCottonwoodGoldWrite` directly below it.
The loop DERIVES scopes at runtime: `build_portal_gold_accrual.py:101-103` *"the scope enumeration is
DERIVED from the product's roster plus the literal `global`. NEVER hand-listed at a call site"*;
`:115-119` fail-closed, *"never falls back to a hand-list."* Four firm-scoped statements would rebuild
that hand-list in Terraform, unsynced from `partner_roster.json`; a roster addition would then derive a
scope IAM has no statement for, and `put_object` at `:260` is NOT inside the bare except, so it crashes
the run and reads as an IAM bug rather than a drift trap we built. **Review point for a new firm is the
ROSTER.** Scope stays product-pinned, never bucket-wide (NEVER#2).

Also amended in the same commit: the control comment at `AssetsRevampStagingWrite` previously read
*"NO portal/\* write is granted here"* -- categorical about the WRITE, not the component. Left intact it
would have handed the next reader a false control comment. The **S5 revamp-publisher hold STANDS** and is
still enforced by the absence of a revamp-publisher write.

## Verification -- THREE PLANES
| Plane | Evidence |
|---|---|
| DESIRED | `terraform validate` Success; plan `0 add / 1 change / 0 destroy`, one statement |
| APPLIED | `safe-apply.sh apply -target=aws_iam_role_policy.mdpf_runner` -> "Apply complete! 0 added, 1 changed, 0 destroyed"; live `get-role-policy` returns the statement; 0-diff re-plan on the **same address that applied** |
| EXERCISED | `R5 SKIP (exists, not clobbering)` x11 in the run's own telemetry (`20260729T174413Z.log`), `DONE written=0 skipped_existing=11 errors=3`; tree independently unchanged at 15 objects / 37 versions |

`simulate-principal-policy`, **three SEPARATE invocations, one `--resource-arns` each** (Rule 22a):
PutObject on the crash key -> `allowed`; GetObject on the same key -> `allowed`; PutObject on
`portal/gold/OTHERPRODUCT/x.json` (boundary) -> `implicitDeny`. **The boundary deny is the control that
makes the two allows mean something.**

**NEGATIVE CONTROL ON THE FREEZE FENCE, RUN POST-APPLY:** emitter live `CodeSha256` =
`H6bq4C2wReMWJ666Yd3GUhJq9+7oA6uH4TUJSwK0wPY=` (the 4a build). **4c is still un-applied and its
once-only "before" half is intact** -- re-proved after the apply rather than inferred from the plan.

## ACCEPTANCE -- PARTIAL. DO NOT READ AS MET.
**LIMB 1 (GetObject / R5 armed): SATISFIED AND DECISIVE.** The guard fired 11/11; before this grant it
could not fire at all. **CTO 175422Z sharpening: GetObject is EXERCISED, not merely simulated** -- R5
can only reach the SKIP branch if `head_object` RETURNED SUCCESSFULLY, and `exists=True` is unreachable
through the bare except. Stronger than a simulate, on the limb the co-sign turned on.

**LIMB 2 (PutObject / real write read back): UNEXERCISED-BY-CONSTRUCTION.**
`written=0`. Every object the bridge plans already exists with byte-identical content (planned vs staged
sizes verified equal on 5 keys), so R5 correctly skips all 11. **The guard working is what prevents
limb 2 -- that is the system behaving as designed, not a test failure.**
**NAMED DISCHARGE CONDITION (CTO 175422Z): the first write to a key that does not already exist** --
the next new-DATE object the bridge plans once its source advances. At that moment `head_object` returns
404, `exists=False` legitimately, and `put_object` runs for real.
**`--allow-overwrite` was NOT used and must NOT be** -- disabling the anti-clobber guard to prove the
anti-clobber guard works is incoherent, and would put a deliberate clobber on a serving-adjacent tree to
satisfy a checkbox.

## OUTCOME: THE DATA DID NOT MOVE
The fix-forward's stated purpose was to carry DS~A's composed cottonwood artifact (landed 15:52:29Z).
It did not. The bridge derives its destination key from the source's `as_of`; cottonwood's did not
advance, so it derived the same keys, which exist, so it skipped. Two readings, **not resolved here** and
routed to DS~A as a question about its output rather than about IAM:
 (a) the composition re-composed at the same `as_of` -> nothing was pending, grant still correct; or
 (b) the bridge is not reading the new artifact -> the carrier is still broken and this grant fixed a
     different problem than the one it was authorized for.

## RESIDUALS -- BOUNDED, NOT RESOLVED
1. **The `portal/gold/mdpf` writer of 2026-07-29T00:35:16-17Z is UNDETERMINABLE.** CloudTrail carries no
   S3 data-plane events (positive-controlled: same window without the EventName filter returns rows);
   bucket access logging is OFF; artifacts carry no `written_by`. Release rested on that writer being
   **DORMANT** -- commissioning-shaped: 37 versions, four bursts inside one 5h window, nothing before,
   nothing since. **That shape is only sound because COO read the bucket lifecycle and found NO
   non-current-version expiry**, so the version ledger is a complete history rather than a retention
   window. *Deliberately NOT cited: the "16.5h through two scheduled fires" argument -- it was mine,
   CTO struck it, and he was right: neither fire writes this tree, so the writer was never offered an
   opportunity it declined.* **Follow-up owed: identify or retire that path.**
2. **`errors=3`** -- `aum-metrics` DECLARED but source ABSENT (`gold/mdpf_revamp/{49financial,inflection,
   global}/aum_metrics.json`), present in all three runs, untouched by this grant. Now the **next actual
   question**, per CTO: what makes those sources absent, and does fixing it produce the new-date write
   that discharges limb 2?
3. **CODE DEFECT, flagged not fixed (DS lane, post-wave):** the bare `except Exception` at `:254` is
   FAIL-OPEN -- it converts "I could not determine whether this exists" into "it does not exist," the
   clobber direction. GetObject fixes the AccessDenied case only; throttling or any transient still
   resolves toward writing. Should catch 404/NoSuchKey ONLY and let everything else raise.
4. **CENSUS TAG (CTO 175422Z):** the accrual bridge has applied its grant, armed its guard, and **still
   written zero objects in its lifetime** -- first-ever `PutObject` still ahead of it. Live instance of
   the never-exercised-write-path class (CVO 165039Z); reads
   `EXERCISED-SINCE-LAST-MATERIAL-CHANGE = NO` even after a successful apply and guard exercise.
