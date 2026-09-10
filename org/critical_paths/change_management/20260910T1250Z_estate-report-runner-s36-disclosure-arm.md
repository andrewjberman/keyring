# DEPLOY COMPLETION LEDGER -- estate-report-runner S36 DISCLOSURE ARM (NFRA_OUTSET.TO-OS-s-22)

**Opened:** 2026-09-10T12:50Z by `0.7.0_AE_CloudOps~W`
**Status:** **OPEN**
**TO:** `org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-22.the-per-device-consumer.md`
(cell `OS-s-22`, outcome_ref FWD-3; face AMENDED @`221511c4ca`, PRD v0.9)
**Ordered by:** `2.0.0_SA_COO` 94889 clause 3, carrying `1.0.0_SA_CTO`'s ruling on `NFRA_OUTSET-S36`
clause (v) (record @`2e1bba37aa`).

⛔ **Committed OPEN before the upload**, so "opened first" is a fact in git history rather than a
claim in prose. Closed in a second commit after the legs verify. The OS-s-19 / OS-s-22 / OS-s-26
shape exactly.

## What

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`, carrying
`git show HEAD:infra/aws/ec2/estate-report-runner/estate_report_runner.py`.

**IT DOES NOT REPLACE THE HOST.** No `user_data` change is in this act, so
`instance.tf:83`'s `user_data_replace_on_change` is not triggered; the host pulls the runner at
every boot (`instance.tf:215` ExecStartPre). **No IAM change is in this act either** -- the
exact-key Condition landed separately @`a9972bf008` and is already on the applied plane.

**THE CHANGE:** a device whose drift key comes back `AccessDenied` renders in a FIFTH per-device
state, `NOT-PUBLISHED-OR-UNREADABLE`, which names both conditions and asserts neither, instead of
the `UNREADABLE` it asserted before.

## THE SERVED FALSEHOOD THIS REMOVES -- READ OUT OF THE SERVED BYTES, NOT ASSERTED

From the manual served day's own report (`daily/2026/09/09/estate-report-2026-09-09.md`,
VersionId `LDU91_HNL2W37JpxYerMhKjffcFDNje9`, the 00:29:57Z run), verbatim:

```
site-z: SILENT -- artifact UNREADABLE at s3://opal-estate-report/outset/site-z/comp_heat_drift.json: AccessDenied
```

⛔ **AND IT DID NOT STAY IN THE DENOMINATOR.** The same run's AI narrative carried it into served
prose twice:

```
Cross-device propagation is unverifiable because site-z is UNREAD (AccessDenied),
denominator 1 of 2 rostered devices reporting.
```

`site-z` has never published a drift artifact. So the served report told a reader that an artifact
EXISTS and cannot be read, on the one piece of evidence that cannot tell existence from
entitlement -- and an AI stage then reasoned from it. That is the defect, measured on the served
object rather than argued from the source.

## THE PRE-STATE, measured live before the upload (2026-09-10T12:47Z)

| | value |
|---|---|
| Served object | **173,482 B**, ETag `03298f0f5c2177335349ce053a744bc4`, LastModified 2026-09-09T22:44:33Z, VersionId `BUorf3uM3aGvDQRveDn8JvdMvWoPGVK6` (the OS-s-26 trigger-token runner) |
| Instance `i-0584e17d283fa7ef4` | **`stopped`** (read LIVE at 12:47:37Z) |
| Schedule `estate-report-0900et` | **ENABLED**, `cron(0 9 * * ? *)` `America/New_York` = 13:00Z |
| Applied grant (unchanged by this act) | `ListOwnPrefixes` Condition carries **9** `s3:prefix` values, six of them the exact seam keys (@`a9972bf008`) |

**THE BYTES ARE `git show HEAD:<path>`, COMPARED and not assumed equal to the worktree** -- a
worktree hash on this autocrlf box hashes the CHECKOUT, not the record. The comparison and both
digests are recorded in the legs below, not predicted here.

## THE WINDOW -- and this upload is deliberately racing a fire

The next scheduled fire is **2026-09-10 13:00Z**, roughly ten minutes after this entry opens. The
host is `stopped` and **is NOT started by this act**; the fire starts it on its own schedule.

⛔ **THE RACE IS THE POINT AND ITS LOSING BRANCH IS SAFE.** If the upload lands before the host's
`ExecStartPre` pulls the key, today's served report carries the disclosure and also answers the
CTO's residual (below) on the same run. If it lands after, the host runs the PRIOR runner -- the
object it pulls is whole either way, because `put-object` is atomic and the pull is a single
`GetObject` of one version. There is no partial-file branch. Losing the race costs a day of
disclosure, never a broken run.

⛔ **NO AD-HOC RUN IS FIRED TO WIN IT.** `2.0.0_SA_COO` 94867: "NO re-run before 13:00Z." The
manual path is the one that wrote the protected 09-09 keys and needed a rollback (row
`NFRA_OUTSET-S34`); it is not re-entered to save ten minutes.

## WHAT THIS DEPLOY ALSO INSTRUMENTS -- the CTO's residual, 94897

The residual asks that `estate-report-runner-role`'s OWN identity read a 404 on a certainly-absent
key under a newly-conditioned prefix, because the discriminator settled THE MECHANISM on a
different role and could not settle whether THIS statement is written correctly.

`outset/site-z/comp_heat_drift.json` is exactly that key: it is newly conditioned and it does not
exist. So the FIRST served run after this deploy answers the residual out of its own denominator,
and the two possible readings are told apart in the rendered bytes:

| what the runner's identity gets | what the report renders | what it proves |
|---|---|---|
| **404** NoSuchKey | `SILENT -- artifact ABSENT` | the statement is correct: APPLIED **and** EXERCISED |
| **403** AccessDenied | `NOT-PUBLISHED-OR-UNREADABLE` | the statement is applied and NOT working: a finding and a row, never a retry |

The positive control on the same identity in the same run is `outset/laptop/comp_heat_drift.json`,
which exists and must read 200, so a uniformly failing call cannot read as a verdict.

⛔ **UNTIL THAT READ LANDS THE OS-s-23 FIX STAYS RECORDED AS APPLIED, NOT EXERCISED**, in those
words. This entry does not claim it.

## EVERY CONSUMER OF THE KEY THIS ACT MOVES

Re-stated at this act rather than carried: exactly ONE functional consumer --
`estate-report.service` on `i-0584e17d283fa7ef4`, whose `ExecStartPre` pulls
`code/estate_report_runner.py` at every service start (`instance.tf:215`). The orchestrator Lambda
holds one environment variable, `ESTATE_INSTANCE_ID`, and reads no code key. **ONE task family, no
shared tag**, so the image-act clause that governs a moved `:latest` does not apply here.

## Rollback -- stated before the act

One `copy-object` from VersionId `BUorf3uM3aGvDQRveDn8JvdMvWoPGVK6` (173,482 B, the OS-s-26
trigger-token runner), in session, no Terraform. Versioning is Enabled and the prior object is not
deleted by an overwrite. **The data plane is untouched in either direction** -- no schedule, no IAM
grant, no instance, no served report key.

## Legs -- to be verified at the close

1. [ ] Uploaded; instance state read LIVE immediately before; new VersionId + ETag recorded.
2. [ ] ETag == the HEAD md5; ContentLength recorded.
3. [ ] **CONTENT diff** (Rule 22a -- deployed bytes against the BUILD INPUT, never by filename):
       served sha256 == `git show HEAD:<path>` sha256, **with a negative control** proving the
       comparator can report MISMATCH.
4. [ ] **THE DISCLOSURE, SHOWN IN THE SERVED BYTES**, with a control per token: the fifth state's
       tokens present in the new object and absent from the prior one.

## Close condition

All four legs checked. Closed in a second commit flipping the Status line.
⛔ **THE ACCEPT IS NOT THIS ENTRY.** `O22-AC1` reads a SERVED DAY. This entry closes on the DEPLOY.
