# DEPLOY LEDGER -- opal-data-research -> opal-data-harvest, a MEASURED MIGRATION

**Status: CLOSED -- COMPLETE AND VERIFIED** (opened 2026-09-11T19:15Z, closed ~19:4xZ, by `4.0.0_SA_CRO~Z`)
**Module:** `infra/aws/terraform/harvest/` | **State:** `harvest/tfstate`

## AUTHORITY, AND THE CORRECTION THAT RIDES WITH IT

Andrew ruled the rename ~18:5xZ: *"call 2 no it should actuall be a rename there is no data in there
anyway, better to have all of this stuff grouped by name right from the start."* He approved running
it as a measured migration at ~19:0xZ (*"yes to all recs"*) and scoped the sweep at ~19:2xZ
(*"live refs only"*).

⛔ **HIS STATED PREMISE WAS FALSE AND HE WAS TOLD BEFORE THIS RAN.** "there is no data in there
anyway" -- the bucket holds **53 objects / 60 versions**, measured independently by
`1.0.0_SA_CTO~Z` at 18:55:29Z and re-measured by this seat at 19:15Z. The ruling was NOT held
hostage to the correction; he was given the corrected facts and the act proceeds as a MIGRATION
rather than as the free rename his sentence describes.

## THE ACT, AND WHY THIS ORDER

1. `terraform state rm` the four old bucket resources -- **NON-DESTRUCTIVE**: the live bucket simply
   becomes unmanaged. It is NOT deleted, and nothing in the config is applied yet.
2. Point `s3.tf` at `opal-data-harvest` and `apply` -- **CREATE ONLY**. This also updates the enqueue
   Lambda's `RESEARCH_BUCKET` env automatically, because that value is
   `aws_s3_bucket.harvest.bucket` in terraform rather than an OS env anyone sets.
3. Copy all 53 objects preserving the key grammar.
4. **VERIFY destination count == 53 AND key paths match exactly.** This is the gate on step 5.
5. Only then delete the source.

⛔ **NOT `terraform apply` ON A RENAMED BUCKET RESOURCE.** Changing `bucket =` in place makes
Terraform plan a DESTROY-AND-CREATE, which would attempt to delete a bucket holding 53 live objects.
`state rm` then create is the same end state with no destroy in the plan at any point.

## WHAT IS KNOWINGLY LOST, STATED BEFORE THE ACT RATHER THAN DISCOVERED AFTER

**~7 non-latest object versions and 1 delete marker.** S3 has no rename; a copy carries CURRENT
objects only, so 60 versions collapse to 53 objects. Accepted explicitly.

⭐ **WHAT IS *NOT* LOST, because this was nearly got wrong in both directions.** `1.0.0_SA_CTO~Z`
first wrote that the rename "would destroy the evidence FWD-6's accumulate bar rests on" and
WITHDREW it; this seat separately checked one prefix (BABA, 4 distinct keys, all `IsLatest`) and was
ready to call the whole concern overstated before a BUCKET-WIDE read found the 7. **Neither the
alarm nor the dismissal survived measurement.** The accumulate evidence lives in DISTINCT TIMESTAMPED
KEYS -- `derived/model_block/<key>/<YYYYMMDDTHHMMSSZ>/` -- and distinct keys copy intact. The store
contract says so in its own words: *"versioning is the safety net for an accidental overwrite, not
the mechanism the grammar relies on."*

## THE CODE HALF, ALREADY LANDED AHEAD OF THIS

`@7f05870bb0` made all five LIVE definition sites `os.environ.get("HARVEST_BUCKET", <default>)` with
the default still on the OLD name -- so nothing pointed at a non-existent bucket in the interval.
The cutover flips those defaults after step 4 verifies. **Migrating the data with the code untouched
was the one variant where nothing announces the break:** five modules would have failed at RUN time,
not apply time.

⛔ **NOT EDITED, DELIBERATELY:** five worker check scripts under `deliverables/<serial>/` -- another
cell's graded PROOF ARTIFACTS. They stay hardcoded and need `HARVEST_BUCKET` set to reproduce.

## BLAST RADIUS

One S3 bucket and its 53 objects; the enqueue Lambda's env var (terraform-driven); five python
defaults. **No table is touched. No portal route changes** -- `POST /api/private/research/pull`
keeps its path by Andrew's word and the portal hold stands.

## THE CLOCK

`AMGT-rd-5`'s chatter producer fires `cron(0 10 * * ? *)` UTC, next **2026-09-12 10:00Z**. A rename
landing between two fires breaks the next one silently, so the whole act completes well inside this
window or is rolled back within it.

## ROLLBACK

Before step 5 the source bucket still holds every object, so rollback is: set `HARVEST_BUCKET=
opal-data-research` (or revert the default flip) and re-point the terraform resource. After step 5
the source is gone and rollback is a copy BACK from `opal-data-harvest`, which is why step 4's
verification is the gate and not a formality.

## PROGRESS -- 2026-09-11 ~19:3xZ. PAUSED AT A SAFE POINT, NOT HALF-LANDED

⛔ **AN OPEN LEDGER ENTRY IS AMBIGUOUS UNLESS IT SAYS WHERE IT STOPPED**, so this states it.

| step | state |
|---|---|
| 1. `state rm` the four old bucket resources | **DONE** -- non-destructive; live bucket kept all 53 objects throughout |
| 2. create `opal-data-harvest` via apply | **DONE** -- `4 to add, 2 to change, 0 to destroy`; versioning `Enabled` confirmed live |
| 3. copy 53 objects | **DONE** -- `aws s3 sync`, rc=0, no errors |
| 4. **VERIFY** | **DONE, PASS** -- 53/53 objects, 1742698/1742698 bytes, 0 missing, 0 extra, 0 size mismatches, negative control discriminates |
| 5. flip the five live defaults | **DONE ON DISK, UNCOMMITTED** -- blocked, see below |
| 6. **DELETE THE SOURCE** | ⛔ **NOT DONE, DELIBERATELY** |

⭐ **STEP 2's APPLY EMPIRICALLY CONFIRMED THE TERRAFORM-DRIVEN CLAIM.** The plan's two in-place
changes were `aws_iam_role_policy.harvest_enqueue_grants` and
`module.harvest_enqueue.aws_lambda_function.this` -- the IAM policy's bucket ARN and the Lambda's
`RESEARCH_BUCKET` env BOTH followed the bucket resource automatically. That is the measurement that
retires `1.0.0_SA_CTO~Z`'s split-brain concern (msg 21557): the enqueue Lambda never needed a source
edit or a promote, so the portal freeze was never in the path.

### WHY STEP 6 IS NOT DONE, AND WHY THAT IS THE CORRECT STOP

`safe-commit` REFUSED step 5's commit: **a MERGE IS IN PROGRESS in the shared worktree**, MERGE_HEAD
`aa484f6b62` (`0.1.0_DS_MarketIntelligence`, the CLOUD->SITEZ leg), 381 paths staged. The refusal is
CORRECT and there is deliberately no override -- git cannot honour `commit --only -- <pathspec>`
during a merge, so the run would have staged these files and let the next merge commit carry them
under the MERGING seat's authorship, where the owned-paths merge exemption means no lane check sees
them. **Nothing was staged; the six files are untouched and are NOT in the merge's staged set**
(verified with `git diff --cached --name-only` over those paths: empty).

⛔ **DELETING THE SOURCE WITH THE CUTOVER UNCOMMITTED WOULD BE THE ONE ORDERING THAT BREAKS THINGS.**
If the flip were lost, five live modules would default to a bucket that no longer exists. The source
bucket is the rollback, and it stays until the code that no longer needs it is durable. Measured at
pause: **`opal-data-research` 53 objects, `opal-data-harvest` 53 objects** -- both intact, rollback
is a one-line env var.

**This is a PAUSE, not a half-landed deploy.** Every live consumer still resolves to a bucket that
exists and holds every object. The remaining work is one commit and one delete, both gated on a peer's
merge closing in its own time -- and well inside the `cron(0 10 * * ? *)` window (next fire
2026-09-12 10:00Z).

## CLOSE-OUT -- 2026-09-11 ~19:4xZ. COMPLETE.

All six steps done. The pause above lifted when `0.1.0_DS_MarketIntelligence`'s merge closed.

**FINAL VERIFICATION, with a POSITIVE CONTROL beside the negative one** -- a 404 on its own only
proves *something* is absent, and could just as easily mean a broken client or wrong credentials:

| check | result |
|---|---|
| SOURCE `opal-data-research` | `head-bucket` -> **404 Not Found** -- gone |
| DEST `opal-data-harvest` (positive control) | exists, `arn:aws:s3:::opal-data-harvest`, **53 objects**, versioning **Enabled** |
| terraform drift | `plan -detailed-exitcode` -> **rc=0**, no changes |
| live Lambda env | `RESEARCH_BUCKET` and `HARVEST_BUCKET` BOTH = `opal-data-harvest` |
| live code naming the old bucket | `comp-find --band DEF` -> **5 hits, ALL of them worker proof artifacts.** Zero live references. |

**Deleted: 60 object versions + 1 delete marker = 61 entries, then the bucket.** The ~7 non-latest
versions named at the top are inside that 61 and are gone as disclosed. The 53 CURRENT objects live
on in `opal-data-harvest`, byte-for-byte (1,742,698 bytes both sides at the final pre-delete check).

### WHAT THE ORDER BOUGHT, since that is the transferable part

At NO POINT did a live consumer resolve to something that did not exist:
create the bucket -> copy -> **verify** -> flip the five defaults -> commit -> apply the env
transition -> **re-verify** -> delete. The delete was the LAST act and was gated on a check taken
immediately before it, not on the earlier pass.

⭐ **AND THAT ORDER ABSORBED A REAL MISTAKE.** Between the copy and the delete, Andrew asked
*"why is it not a straggler?"* and exposed that `pull_enqueue`'s FALLBACK still named this bucket --
missed by this seat (which called it "1 AUTOMATIC", true of its value and false of its fallback) and
then missed again when `1.0.0_SA_CTO~Z` withdrew its own correct flag on the strength of a rebuttal
that only addressed half of it. **The sequencing discipline held the destructive half behind a commit
while the reasoning was wrong.** That is the argument for the sequencing, not for the reasoning.

⛔ **AND THE OBVIOUS FIX FOR THAT STRAGGLER WOULD HAVE CAUSED THE FAILURE IT FIXED** -- renaming the
terraform env KEY and applying would have left the RUNNING bytes' variable unset, falling through to
a literal default pointing at this now-deleted bucket. Both keys are set instead, so the window is
unlosable rather than short. `RESEARCH_BUCKET` drops only after the function is next rebuilt.

### STILL OPEN, NAMED RATHER THAN LEFT IMPLICIT

- The three SOURCE terraform states (`research/tfstate`, `amgt-resapp/tfstate`,
  `amgt-resapp/rd-2-security-metrics/tfstate`) still exist and still describe resources this module
  now owns. They are inert -- nothing applies them -- but they are stale and should be cleaned up.
- `RESEARCH_BUCKET` remains set as the transition key until the enqueue Lambda is rebuilt.
- The two DynamoDB tables keep `opal-amgt-*` names. Their rename was approved in the draw and is
  cheap while both measure 0 items -- but `AMGT-rd-5`/`rd-6` are live writers into the metrics
  table's schema, so it is sequenced behind them. Not part of this entry.
