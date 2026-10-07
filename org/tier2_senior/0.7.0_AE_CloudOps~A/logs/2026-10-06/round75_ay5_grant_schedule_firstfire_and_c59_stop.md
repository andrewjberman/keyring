# round 75 / AMGT-ay-5 -- the snapshot grant, the schedule, the first fire, and a STOP on an oracle that crosses environments

**Seat:** `0.7.0_AE_CloudOps~A` | **archetype:** DEPLOY | **date:** 2026-10-06
**TO:** `AMGT_RESAPP.TO-AMGT-ay-5` | **GO:** msg 29998 (`2.0.0_SA_COO~Z`)
**Pair:** COO half @265f85f8fe, CTO half @452acb4e68 (conditions 1-7), carrying `ROUND_ANALYSIS.round74.md` ADDENDUM 1 @82afef1fd8 option (b)
**NEVER-2:** `amgt-resapp-r75-ay5`, opened @d02825e9e3 before the first apply; **L0-L5 CLOSED, L6 OPEN**

## What landed

| leg | act | state |
|---|---|---|
| L0 | gating reads: base, absence, grant base arm, worktree union, comp-schedule | closed |
| L1 | detached build at exactly `ab28d0ba0112e85d` | closed |
| L2 | upload `UvQ9tuNULwnl6bUSLq8uUB0Fg91.MuJC`, independent head-object | closed |
| L3 | code apply `0MZWPl7n` -> `D29LJCXh` at memory 1769, leadpanel | closed |
| L4 | grant + schedule on an UNTARGETED plan, both grant controls | closed |
| L5 | first fire + plant test | closed |
| L6 | AC1 + AC2 | **OPEN -- one clause STOPPED** |

Code is live at `D29LJCXhOStZ51JD4TTt2Jk0QUVDUbXDouXRTUS1ULI=`. The schedule
`amgt-global-freshness-snapshot-daily` is ENABLED at `cron(30 12 ? * MON-FRI *)` UTC. The snapshot
object exists, 2,850,172 B, 302 rows, and `/freshness` serves it warm in 564-617 ms.

## The round's substance

### 1. The one open clause, and why I did not act on the half's own FAIL branch

AC1 c59 C1 reads **0 of 302**. The half's outcome table reads that branch as "grant or fire fault:
the route falls back; a row, then the reverse of the grant and schedule legs". I did not reverse,
because neither named fault is present and the measurement says what is:

- the route IS serving the snapshot (`served from snapshot: True`, `age_hours 0.06`);
- the grant's control pair discriminates;
- the fire wrote 302 rows with the function's self-reported ETag equal to an independent head-object.

**0 of 302 is not 302 wrong values.** Same 302 keys both sides, same 10 fields, nothing present on
one side only, and exactly ONE field differs in all 302 rows -- `rot`. Ignoring `rot`, 302 of 302
are byte-equal. Each side carries ONE uniform `rot` value, which is the signature of a single
environment difference replicated 302 times.

**The discriminator was free and decisive:** `c59 --where local` compares
`build_freshness_snapshot()` against `read_coverage_freshness()` **both in one environment** and
reads `302 of 302; e.g. differing []`. So builder and compute agree; the deployed arm's failure is
produced by crossing environments, not by the producer.

**What I deliberately did NOT conclude.** The Lambda's `rot` is the richer computed signal and the
local one is the "no signal" fallback, so the tempting read is "the Lambda is right". Nothing I ran
establishes that the richer value is the correct one to STORE, and the opposite reading -- that the
Lambda carries a stale 2026-09-10 review date where "none at this vintage" is correct -- is excluded
by nothing I measured. I checked before theorising: no objects under `lists/` in `opal-data-harvest`,
and no `rot_signal.json` in the built zip (only `lists/rot.py` plus the two packaged data files).
The repo's one `rot_signal.json` sits in a worker deliverable directory, on neither path. Row
**AMGT_RESAPP-Z-S359** @51a2532a9c states the question and leaves it to the issuer; three options
priced in msg 30010, recommending (a).

**RULED (a), msg 30011** -- "Row Z-S359 is the check's fault, not the act's. No reversal." The issuer
settled the question the row deliberately left open: the deployed `rot` is **correct**, because the
package carries the list register and the local tree does not. The check was re-cut @bf909b6665 to
judge `rot` within one environment (against the deployed `/lists`) and every other field against the
local view. Z-S359 disarmed by that ruling, `disarm_owner` `2.0.0_SA_COO~Z`. Holding the legs rather
than reversing them was right, and the deciding read was the one that cost nothing -- the local arm.

### 1a. The re-cut then failed the NEXT clause, vacuously

At @bf909b6665 (blob `3f92e60b43`, verified byte-identical to my working tree before running), C1
passes `302 of 302` with `rot` equal to the deployed register. **C2 then failed reading
`cold invokes 0 []`.** The clause is `cold and all(c == 200 and t <= bar for c, t in cold)`, so an
EMPTY cold list fails for want of a measurement -- not because a cold invoke was slow. The same
clause passed earlier in this round at `cold invokes 2 [(200, 881), (200, 858)]`, and the issuer's own
run read 900/924 ms.

The cause is my own instrumentation: AC1 and AC2 between them invoke the function dozens of times, so
by the re-run the warm pool absorbed all six concurrent invokes and no container had to be created.
The only honest lever is idleness -- a larger burst of my own would only widen the warm pool, and
forcing new containers by touching configuration would be a change outside the signed plan. So I
stopped invoking for an idle window and re-ran. **That wait is named, not open-ended:** the clause
exists to measure a cold start, container reclamation is the only thing that produces one, and 65 s
(C3's own hold) demonstrably does not -- C3's post-hold read came back at `Duration 234 ms`, warm.

### 2. Two wrong objects in my own reading, both caught by printing the bytes

**AC2's last item.** My note said "r71 c38" and I ran `r71_served.py --cell c38`. That script
defines only c34/c35/c36 and answered `invalid choice: 'c38'` -- which my loop scored as a FAIL,
giving a false "6 pass, 1 fail" regression. The TO's *invocation* names `r71_latency.py --where
deployed` with no `--cell` at all; only its *expectation* text says "R71 C38". Run verbatim, **AC2
is exit=0 with all seven SERVED: YES.** A paraphrased criterion redirects its only oracle, and here
the paraphrase was mine.

**A `|| echo` that reported a clean verdict on an error.** Checking the delivered STOP for stray
tags, my `grep -c ... || echo "0 -- clean"` printed "clean" because `grep` could not open the file
at all -- the path was wrong. Re-read at the right path, the count is 1: the body does carry a stray
`</body></invoke>` from my own parameter. Never put a reassuring fallback on the failure branch of a
read whose emptiness carries the verdict. The substance of msg 30010 is complete and legible, so I
did not send a second message about two tag lines -- that is the FYI-to-an-inbox Rule 31 forbids.

### 3. The naming rule explained itself once I stopped guessing

`name()` refused `SCHEDULE` as a kind, and `IAM_ROLE`/`IAM_POLICY` too, while the *grader* uses
those exact tokens as node_types. Reading `NAMING_SCHEMA.json` settled it:
`resource.last_slot = {"default": "kind", "EVENT_RULE": "cadence", "SCHEDULE": "cadence"}` -- the
last slot is the kind EXCEPT for schedules and event rules, where it is the **cadence**. So the name
ends `-daily`, by design. `name()` has no expression for an IAM last slot, so those two were settled
against `grade()`, which also prints the canonical form when it refuses (`-scheduler` ->
`-scheduler-role`). Three independent confirmations: `name()`, `grade()`, and the commit-time gate's
`NAMING-GATE: PASS 3 graded`.

The sibling was **not** the template: `chatter-axis-schedule.tf`'s `amgt-resapp-chatter-axis-daily`
uses the very scope `name()` refuses, so copying its shape would have carried a non-conformant name
into a new resource. Rule 30's non-application covers the existing one.

### 4. Round 74's finding, adopted and paying off

Condition 2 graded these legs on an **untargeted** plan -- row Z-S357's point, now practice. The
plan read 53 changes -> 48 no-op + 3 create + 2 update, 0 deletes, exactly condition 2's four named
items, and `terraform_data.scoped_amgt_route_count_check` **was present in the graph**, which is the
guard a `-target` plan structurally could not show. I also read the grants-policy delta rather than
trusting "update": statements 6 -> 7, ADDED exactly one Sid, REMOVED and CHANGED both empty.

### 5. The plant test, widened past what was asked

Condition 5 asks that an HTTP GET never writes. One arm would have left the obvious attack untested,
so I ran three: a plain GET (200, no write), **a GET carrying the action as a query parameter** (200,
no write), and an unknown action (400, no write). ETag and VersionId byte-identical across all three.
NEVER-1's "one writer" is now measured rather than asserted.

### 6. The moratorium, answered in the file rather than in a commit message

This leg sits beside a hard NEVER naming "freshness-checker". The new file states why it is outside:
nothing watches, nothing notifies, and it computes a snapshot an already-served route reads. The
precedent is local -- `chatter-axis-schedule.tf` draws the same distinction in the same words at the
top of this very root -- so the reasoning is not invented here.

## Numbers worth keeping

- `/freshness` warm: **564-617 ms**, against round 73's 10,300-11,800 ms. Row Z-S356's loop, on which
  the issuer held Andrew's DEV push, is closed at roughly 19x.
- c59 cold: **881 / 858 ms**; post-hold **744 ms** -- both inside the 2,000 ms bar.
- Cold chatter: **3,339-3,774 ms** (r74 3,668-4,729; r73 6,381-7,786). Band narrowed to 435 ms from
  1,061. Still above ~2 s, so provisioned concurrency stays on Andrew's list -- now within ~1.7x.
- CONTENT-DIFF reproduced on the uploading pass: files 371, IDENTICAL 365, CHANGED 3, ADDED 3,
  REMOVED 0; 255,343,763 B at 97.4% of the ceiling, the COO half's figure to the byte.

## 7. The proof-of-spec validator earned its keep

The instance was INVALID on its first two passes, and every violation was real rather than
pedantic. The ones worth remembering:

- **`artifact_covered_by` is an array of CRITERION IDS, not prose.** I had written the build
  provenance into it, and the validator's reply is the sharpest line in the tool: *"a citation to a
  row that is not there is worse than no citation"* -- it had dutifully parsed my sentence as a
  criterion id and reported that no such criterion exists.
- **`status` is the bare token; the prose goes in `status_reason`.** A PASS with an explanation
  stapled to it is not a PASS the schema can read.
- **The AC2 invocation had to be verbatim.** I had abbreviated three long paths to `.../round74/...`
  and the alignment limb caught all three, with the reason attached: a correction that reaches the
  spawn prompt and never the task-order file leaves the record ungoverned.
- **`s3_object` is the kind that exempts the commit-ish rule.** My `terraform (IAM grant)` was not in
  the enum, which is also what pushed two S3 rows into the artifact-resolution check they should
  never have been in.

Then an advisory I acted on rather than banked: the two terraform rows read **PRESENCE-ONLY** -- "the
pin exists and carries the path, nothing here says it carries the CHANGE". Adding `introduces`
tokens moved both to **CONTENT-resolved**, and I verified the claim myself rather than trusting the
field: `ReadAndWriteTheFreshnessSnapshotObjectOnly` is present 1x at the pin and 0x at its parent,
`amgt-global-freshness-snapshot-daily` 2x and 0x. Final read **VALID (rc=0)**, with
**12 of 12 named controls discriminating** and the rollback named.

## State at close

**NEVER-2 `amgt-resapp-r75-ay5`: CLOSED 7/7, sentinel removed**, entry
`org/critical_paths/change_management/20261006T1106Z_amgt-resapp-r75-ay5_deploy_completion.md`.
Nothing stranded, no rollback taken, no S3 delete in any branch.

AC1 `exit=0` (c57/c58/c59/c61 all SERVED: YES) and AC2 `exit=0` (all seven), both against the same
deployed code `D29LJCXh`. Proof instance VALID. Row Z-S359 filed and disarmed by the ruling.

Both of the round's blockers were in the *measuring apparatus*, not the act -- one in the check's
oracle, one in the check's precondition, and the second was caused by my own instrumentation. The
act itself needed no correction after the first build: the CONTENT-DIFF matched the halves on pass
one, the grant landed as exactly one statement, and the schedule's name was conformant on the first
derivation that respected the schema.
