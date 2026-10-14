# 0.7.0_AE_CloudOps~Z -- 2026-10-14, the harvest release end to end, OG-zs-1's STOP, and two AP-15 ledgers closed

Third log of the day. The first two covered OG-ap-14's re-cut and OG-mg-1 Phase A. This one covers
OG-hv-2 from the cut to a live served read, OG-zs-1 up to the STOP it hit, and the two OG-ap-15
family ledgers whose scheduled sweeps finally ran.

## 1. OG-hv-2 -- LIVE. `harvest_list` and `harvest_read` serve the harvest bucket to Opal principals

**Phase A** (`013844d3e6`, AC1 PASS): release `7c558b4e2176a632d13e6301af3e06d434aa1540` cut on the
live ref `90967e39ba` in `C:/tmp/og-rel-hv`, carrying OG-hv-1's seven gateway files and nothing else --
add/delete counts identical per file to hv-1's own diff at `4e26a29872`, `harvest_read.py` byte-equal
to trunk HEAD, 18 tests passing in the release tree. The grant file is GENERATED
(`hv2_grant_gen.py`): 24 object ARNs whose prefixes are read by AST from `SERVED_PREFIXES`, 48
list-condition values, and exactly three action tokens in the whole file.

**Amendment A5 is the reason this round mattered.** The order as first written put the grant on
`aws_iam_role.gw`. The CVO's row `Z-S107` caught it: `harvest_read.py` makes its S3 calls through
`internal_role.s3_client()`, which assumes `INTERNAL_READER_ROLE_ARN` -- set to
`gateway-global-internal-reader-role` on every deploy, with **no fallback**. Cut as written, Phase B
would have passed every check (the simulate grades the role the order names) while every served read
returned AccessDenied. The grant went on `int_reader`, and `hv2.AC1` now refuses the other role.

**Phase B** under three signed halves, grant first (`f52210e98e`) then deploy (`03a344306a`):

- ACT 1: one inline policy created, `1 to add, 0 to change, 0 to destroy` from the SAVED plan the
  apply consumed. Read-back: 2 inline policies on the role, the pre-existing portal read untouched.
- ACT 2: `safe-ec2-deploy` rc=0, SSM `7934e4ac`, `/health` ok, and the md5 read of the RUNNING path
  106 of 106 equal to the release -- with the negative control against the base differing in exactly
  the three deployed app files the cells touch, plus the new `harvest_read.py`.
- The served read, which is the only limb that proves the grant: an Opal principal reads one real
  `packs/` object (4362 bytes, parsed), a non-Opal principal is refused `harvest_opal_only` on
  `packs/` AND `wsj/harvest/`, an off-list prefix is refused `harvest_prefix_not_served`, and **0 S3
  calls happen on any refusal path** -- measured by swapping `hv._client` for a counter, not inferred
  from reading the admission order.
- `hv2.AC2` PASS (`e05b30aecc`).

**Two things worth carrying forward.**

*A harness that proves nothing looks exactly like a broken deploy.* The served harness's first run read
`principal_required` on every arm. The cause was mine: it called `set_current_principal` and then
`set_current_email`, and the second is the GUI-path setter whose first act is
`_current_principal.set(None)`. Had I reported that run, it would have read as a failed release.

*AC2 graded a shape I had not written.* The refusal fields had to be BOOLEANS; I had written the
refusal codes. The fix was not to edit the JSON -- the harness now emits the boolean AND keeps the code
beside it, and it was re-uploaded and re-run on the host. A hand-written `true` grades identically and
proves nothing, which is the whole reason the record is the instrument's own output.

*The trunk manifest is not what the deploy wrapper writes.* The wrapper writes its record on the
branch it runs from -- which for this deploy-only lineage never merges -- and it never recomputes
`file_checksums`. Its `previous_deployed_commit` read `2c0f84966d`, three releases stale. The trunk
record is written by `hv2_manifest_record.py`: a brace-matched span edit with assertions, 12 changed
lines, 26 of 27 sibling services compared byte-equal, and the indentation READ from the block it
replaces rather than guessed (the first attempt was correct in value and wrong in indent, which is
still 10 rewritten lines inside a never-widen diff).

## 2. OG-zs-1 -- STOPPED at step 3, row `Z-S115`. Nothing applied

The cell closes an unauthenticated hole: CloudFront behavior `/json-tiered/*` served the same keys as
its authenticated twin with no Lambda@Edge association.

**Step 1 had to find its own instrument.** Standard logging is DISABLED on the distribution, there are
0 real-time log configs and no monitoring subscription, and CloudFront metrics are per-distribution,
never per-path. The only thing that records a URI is the WAF log group of the WebACL attached to it --
and its logging configuration carries no `LoggingFilter`, so an ALLOWed GET does appear. 7 days: 2
requests on the bare path, by subtraction from a printed denominator of 41058, with the twin's 1752 as
the positive control. 30 days: the same 2, which closes the monthly-cadence gap a 7-day window cannot
see. **Both of those two were this device's own probes** -- the client IP equals site Z's public egress
IP, read at the act and compared, with `Python-urllib` and `curl` user agents, minutes after the row
was filed. `non_portal_consumers = 0`, and it is not a bare zero.

**The STOP.** The root plan reads `0 to add, 2 to change, 0 to destroy`. The second change is the WAF
WebACL, and three measurements decide what it is:

1. Its two halves are IDENTICAL -- 39 minus lines, 39 plus lines, sets and ordered sequences equal, 0
   attributes on one side only. So the resulting rule set equals the current one: provider churn, not
   drift from another applier.
2. It is not mine: targeting the ACL alone, which excludes my edited distribution, reads 1 to change.
3. **Step 4's targeting cannot exclude it.** Targeting the distribution still reads 2 over 2
   resources, because `web_acl_id` makes the ACL a dependency and `-target` pulls dependencies in.

So any apply of this cell issues a live `UpdateWebACL` that drops and re-adds three AWS managed rule
groups. The net rule set is provably identical; whether the update leaves no window in which the ACL
evaluates without them is NOT something I measured, and that is the only reason the no-op reading does
not settle it. Three routes are named in the row and the choice is the issuer's.

What I did not do: substitute the narrower plan to make AC1 pass. `ZS1_PLAN.txt` is the ROOT plan the
step names, reading 2 to change, saved whole beside the targeted one.

Step 2 is committed and inert, with the twin's other two edge functions deliberately left off (row
`Z-S116`): both were read at their deployed versions, both are no-ops on this path, and attaching a
no-op would buy nothing while adopting whatever those functions do next. Step 6 is answered with no
row owed -- all four `security-scanner` routes carry `portal-jwt-authorizer`, from a denominator of 121
routes of which 3 are `NONE` and all three are the login proxy and CORS preflights.

## 3. OG-ap-15 -- L3 proven for schwab and blackdiamond; both ledgers CLOSED

Both were held on an external gate: the family's OWN scheduled sweep had to write the drain record. No
ad-hoc invoke is permitted, and the log window shows exactly one invocation per family -- schwab
`53885c9e`, START 12:15:49Z against `cron(15 12 * * ? *)`; blackdiamond `887fcea4`, START 13:00:34Z
against `cron(0 13 * * ? *)`.

**Where the key lives cost a read to find:** `dlq_drain` is not top-level in
`meta/backfill-status.json`. The document is sectioned BY LAYER and the record sits at
`layers.silver.dlq_drain`. A top-level read returns ABSENT for all four objects and reads as a missing
drain.

**And the zero is named:** `drained 0` with `messages_total 0`, `other_family_returned 0`,
`unattributed 0`. That is the drain running against an empty DLQ, not a drain that failed to run -- the
key exists, carries its own family name, and was written by the scheduled sweep whose RequestId is
above.

orion and eclipse (16:00Z) and etf (23:30Z) remain held on their own sweeps. Those are producer clocks.

## 4. State at the end of this log

| item | state |
|---|---|
| OG-hv-2 | Phase A + B COMPLETE, AC1 + AC2 PASS, live at `7c558b4e21`; AC3 owed by `3.0.0_SA_CVO~Z` |
| OG-zs-1 | BLOCKED at step 3 on the `Z-S115` ruling; terraform committed and inert, nothing applied |
| OG-ap-17 | HELD by the issuer until the mcportal release MP-pc-5 closes and moves the live ref |
| OG-mg-1 | Phase A complete; Phase B waits on its halves and the issuer's GO |
| OG-ap-15 | schwab + blackdiamond CLOSED; orion, eclipse, etf held on their 16:00Z / 23:30Z sweeps |

One ledger-close commit for the two AP-15 families is written but NOT yet committed: a peer's drain
merge was in progress in the shared tree when it was ready, and a merge state another seat created is
theirs to finish. The changes sit intact in the working tree and the commit follows the moment
`MERGE_HEAD` clears.
