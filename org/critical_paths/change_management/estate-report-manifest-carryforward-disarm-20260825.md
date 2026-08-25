# DEPLOY-COMPLETION LEDGER -- estate-report manifest carry-forward disarm

**Opened:** 2026-08-25T04:5xZ by `4.0.0_SA_CRO~BUILD` (the estate build lane) at deploy-START, per NEVER#6.
**Status:** **CLOSED 2026-08-25T05:4xZ** -- applied (0 added / 1 changed / 0 destroyed), plan
0-diff re-confirmed with `-detailed-exitcode`=0, IAM verified on the live primitive in BOTH
directions with isolated controls, the artifact re-uploaded and verified FIVE ways including a
token read of the DOWNLOADED BYTES with a negative control on those same bytes. All 8 legs closed;
nothing stranded.

⚠ **ONE RUNG IS DELIBERATELY NOT CLOSED HERE, and it is stated rather than implied: the EXERCISED
rung on the real box.** The instance is TRANSIENT and was `stopped` at deploy time (last launch
2026-08-24T13:00:46Z); its systemd oneshot pulls the artifact on EVERY boot, so the change takes
effect at the next scheduled 09:00 America/New_York start (~13:00Z today). Runtime acceptance rides
that boot BY DESIGN and is CVO's layer, exactly as the 2026-08-05 ledger for this same service
recorded. **A staged artifact proves what is THERE, never what RUNS** (Rule 22a) -- and here the
boot-pull is what closes that gap, which is why this is a schedule wait and not an open leg.

**Authorization:** Andrew-direct 2026-08-24 ~2200Z, *"All recs approved"* over the master
`/open-calls` sheet, R-1: *"ONE ESTATE BUILD LANE ... with the substrate migration ... and the
manifest-ledger disarm folded in."* Spawn brief:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/SPAWN_BRIEF_ESTATE_BUILD_LANE_20260824.md` item 4.

**Applying seat / device:** this seat, on THIS device, per **Rule 26** (the apply runs on the device
that owns the work; no cross-fabric ferry).

**SCOPE, stated narrowly -- anything outside this is not covered:**
1. `infra/aws/ec2/estate-report-runner/estate_report_runner.py` -- add `_carry_forward_verdict()`
   and route `write_manifest()` through it.
2. `infra/aws/terraform/estate-report/iam.tf` -- add ONE resource ARN
   (`.../manifest/*`) to the existing `ReadPredecessorAndOwnCode` `s3:GetObject` statement.
3. Re-upload `s3://opal-estate-report/code/estate_report_runner.py` (the deploy IS the upload).
4. `infra/aws/ec2/EC2_MANIFEST.json` -- refresh this service's `deployed_commit`/`deployed_at`
   (Rule 8), plus two record corrections found while measuring (below).

Nothing else. No alarm, no SNS, no monitor (NEVER#13, and `main.tf` carries an explicit
DO-NOT-ADD marker for this module).

## Why this deploy exists

`4.0.0_SA_CRO~D` filed an ARMED surprise item on 2026-08-24 (msg 66380), measured on S3 object
versions. `write_manifest()` is an unconditional `put_object` called three times per run, so a
same-day RE-RUN of an already-adjudicated day resets the ledger key to `PENDING` and the verdict
is gone. It has happened once: `manifest/2026-08-06.json` version `Ew4TJljh` (13:58:21Z, 2,573 B)
carried a full CVO adjudication; version `qiXbAvJj` (21:49:22Z, 3,318 B) is `status=PENDING` with
no adjudication block. The adjudicated COPY survived. Only the LEDGER lied.

That is load-bearing because this module has **no alarm by design** -- `main.tf` states the
miss-detector IS the per-day manifest ledger, *"a gate whose default state is the alarming one."*
A reset day reads as un-adjudicated, so the backstop false-fires on work that was in fact done.

**DISARMED != REMEDIATED.** This stops NEW clobbers. Two things it does NOT do, each needing its
own owner: repairing the already-clobbered 2026-08-06 entry, and teaching `/estate-pull` to READ
`readjudication_required` (CVO's half of the interface).

## The design choice, recorded

`~D`'s pricing sketch was *refuse to overwrite a non-PENDING manifest*. This deploy carries the
verdict FORWARD instead, per the spawn brief. The reason is that refusing would make a legitimate
re-run of an adjudicated day **unrecordable** -- the run would produce a report the ledger never
mentions, which is a different lie in the other direction. Carry-forward keeps every run recorded
AND makes the supersession visible.

The verdict discriminator is the **COMPLEMENT** of the statuses this runner writes
(`{RUNNING, PENDING, FAILED}`), never an enum of CVO's verdict vocabulary. `/estate-pull` already
carries a fourth value this runner had never heard of (`NO-SEMANTIC-CHANGES-BY-ABSENCE`, minted
2026-08-06) -- a hand-maintained roster of verdict names would have classified the exact clobbered
value as "not a verdict." A fifth value needs no edit. This is also `~D`'s Rule-24 note discharged
by construction rather than by extending an enum.

## State pinned at deploy-start

```
baseline terraform plan (before my edit)   No changes. Your infrastructure matches the configuration.
staged artifact ETag                       223b3103204100c17063fe48f2f90af1   120,980 B  2026-08-11T00:08:06Z
local file md5 (pre-edit)                  223b3103204100c17063fe48f2f90af1   120,980 B
                                           => BYTE-IDENTICAL: zero accumulated drift; this deploy
                                              lands ONLY this change (Rule 22a, resolved through the
                                              build input, not by filename)
IAM grant BEFORE (3 isolated simulations):
  s3:GetObject  manifest/2026-08-25.json   implicitDeny     <- the blocker
  s3:GetObject  daily/2026-08-25.json      allowed          <- positive control: action+role resolve
  s3:PutObject  manifest/2026-08-25.json   allowed          <- positive control: the ARN resolves
  (one --resource-arns per call, each a SEPARATE invocation; no Condition on these statements)
offline battery                            17/17 PASS incl. a planted mutant that reproduces the
                                           08-06 clobber exactly, and a negative control
non-ASCII in the added region              0 bytes (3 pre-existing lines at 1173-1175 unchanged)
commit-gate                                All checks passed
terraform validate / fmt -check            Success / clean
```

## Legs -- each closed or rolled back, none stranded

| # | Leg | State |
|---|---|---|
| 1 | `estate_report_runner.py` carry-forward | **CLOSED** -- commit-gate clean, 17/17 offline battery |
| 2 | `iam.tf` one-ARN grant | **CLOSED** -- `validate` Success, `fmt -check` clean |
| 3 | commit (code + TF) | **CLOSED** -- `b94d147844`, msg-verify MATCH len=4865. Written LOCAL; **since confirmed ON `origin/CLOUD`** (see the push-state note below) |
| 4 | `safe-apply.sh` | **CLOSED** -- comp-tagauthz PASS, tombstone-gate CLEAN, `0 added / 1 changed / 0 destroyed`; re-plan `-detailed-exitcode` = **0** (no changes) |
| 5 | IAM re-verified, APPLIED plane | **CLOSED** -- see the two-direction table below |
| 6 | artifact upload + verify | **CLOSED** -- five ways, see below |
| 7 | `EC2_MANIFEST.json` refreshed | **CLOSED** -- plus two record corrections, JSON re-parsed valid (27 services) |
| 8 | ledger closed | **CLOSED** -- this entry |

## Verification -- what was SHOWN, not asserted

**IAM, APPLIED plane, BOTH directions, every call isolated (one `--resource-arns`, separate
invocation -- a positive control run alongside the target is silently disarmed by mode (1)):**

| call | before | after |
|---|---|---|
| `s3:GetObject` `.../manifest/2026-08-25.json` | `implicitDeny` | **`allowed`** |
| `s3:GetObject` `.../daily/2026-08-25.json` (pos. control) | `allowed` | `allowed` |
| `s3:PutObject` `.../manifest/2026-08-25.json` (pos. control) | `allowed` | `allowed` |
| `s3:GetObject` `.../signed-review/2026-08-25.md` (**neg. control**) | -- | **`implicitDeny`** |

The last row is the one that matters after the fact: **the grant did not widen.** The reviewer
surface stays unreachable, which is this module's whole IAM boundary.

`comp-iam service estate-report-runner` reported `s3:GetObject` PRESENT for this role and could
not have caught this -- it models `(action)`, never `(action, resource)`. That is Rule 22a's named
insufficiency, and `iam.tf`'s own neighbouring comment (the `kuzu_nessie_db` line) already warns
about it in this exact file. The warning was correct and the next grant still went missing.

**The artifact, FIVE ways -- and the fifth is the only one that reads the change itself:**

```
ETag        "223b3103204100c17063fe48f2f90af1" -> "58113db66bf3819f3515333d55fd5877"  == local md5
            (no -N suffix: single-part, so the ETag-as-md5 comparison is VALID)
Size        120,980 B -> 125,857 B                       (changed)
Modified    2026-08-11T00:08:06Z -> 2026-08-25T05:36:35Z (newer)
round-trip  independent `s3 cp` down, md5 identical
BYTES       the DOWNLOADED file carries the new tokens 9x
            NEGATIVE CONTROL on those SAME bytes: 0
VersionId   bvnr1MynPuJ8Asn3u6Tgo9LPd5CrL5OO             (rollback point)
```

The first four all pass on an object that is merely *present and recent*. Only the fifth reads
whether the deployed bytes contain the change -- resolved through the build input
(`EC2_MANIFEST._deploy_note`: the systemd unit pulls this exact key on every boot), never by
filename.

**Rollback, one call, if the 13:00Z run misbehaves** -- version ids READ from
`list-object-versions`, not recalled:

```
prior version   5BxTUUHPZYEGQiEssTBK7l_uyHrypvDV   2026-08-11T00:08:06Z  ETag 223b3103204100c17063fe48f2f90af1
this version    bvnr1MynPuJ8Asn3u6Tgo9LPd5CrL5OO   2026-08-25T05:36:35Z  ETag 58113db66bf3819f3515333d55fd5877

aws s3api copy-object --bucket opal-estate-report --key code/estate_report_runner.py \
  --copy-source "opal-estate-report/code/estate_report_runner.py?versionId=5BxTUUHPZYEGQiEssTBK7l_uyHrypvDV"
```

The TF grant needs no revert: an unused read grant is inert, and reverting it would leave the
rolled-back code unable to read a ledger it never reads.

**Push state, read rather than assumed.** All three commits were written LOCAL under the
integrator-only push gate, and the ledger said so. They have since been integrated and are **ON
`origin/CLOUD`** -- confirmed against `git ls-remote origin refs/heads/CLOUD`
(tip `317ded2eae`) with `merge-base --is-ancestor` per commit, NOT against the local
remote-tracking ref, which only moves on fetch/push and can therefore agree with a stale belief:

```
b94d147844  code + TF                ON origin/CLOUD
ad37d51a86  EC2_MANIFEST.json        ON origin/CLOUD
84ee8fb3af  this ledger              ON origin/CLOUD
```

This paragraph exists because the ledger otherwise carried "LOCAL, rides integration" forever --
true when written, false within the hour, and indistinguishable from the two stale
`EC2_MANIFEST` fields this very deploy was correcting.

**The deploy path is the service's own, not an improvised one:** ONE `s3api put-object`, NOT
`safe-ec2-deploy.sh`. That wrapper takes a deploy SCRIPT and this service has `deploy_script: null`
because its instance is transient and pulls on boot. Same act, same reasoning, as the
2026-08-05 ledger for this service.

## Record corrections found while measuring (surfaced, not chased)

- `EC2_MANIFEST.json` records `deployed_commit: ce5f0c7e45 / deployed_at: 2026-07-30T23:35:00Z`
  for this service, but the staged object was last written **2026-08-11T00:08:06Z** and 13 commits
  have touched the file since that date. The record was stale by ~11 days and 13 commits.
- `EC2_MANIFEST.json` records `instance_id: i-04981b6aec3bed86b`; the live Terraform state carries
  `aws_instance.estate_report_runner = i-0512bd3cbaf602b7f`. This is the churn the manifest's own
  `_id_churn_note` predicts (`user_data_replace_on_change=true`), recurring.
- `iam.tf` records that the reviewer surface was renamed `adjudicated/` -> `signed-review/` on
  2026-07-31, but the runner's module docstring still says *"WHAT IT MUST NEVER DO: write
  adjudicated/*"* and the 08-06 manifest's own adjudication block points at
  `adjudicated/2026/08/06/...`. NOT resolved here -- it is a naming question for the surface's
  owner, and it is recorded so it is not rediscovered.
