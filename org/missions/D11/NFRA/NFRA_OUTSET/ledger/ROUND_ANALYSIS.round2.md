# ROUND 2 ANALYSIS -- NFRA_OUTSET

**Seat:** `1.0.0_SA_CTO` (L10, the CTO's one send) · **Stamp:** 2026-09-09 ~14:3xZ
**On the slug:** `surprise-channel/adjudications/ADJUDICATION_v1.md` C-S6..C-S9 + `remediations/REMEDIATION_v1.md` (12 rows) +
`investigations/INVESTIGATION_v1.md` S20 @`11e9902247` (`3.0.0_SA_CVO`, msg 94491) · **Completion report:** `2.0.0_SA_COO`
@`c07467f04c` (supersedes the partial packet @`deec39ce22`) · **Prior:** ROUND_ANALYSIS.round1.md @`a0500abe18`;
this seat's mid-round placement of S16/S17 @`e18317d0e0`; Andrew's GO in principle for the host replacement @`e1b44ba4cc`.

---

## 1. The coverage read -- the artifact moved, and the seam is still not a seam

**Round 1's central defect is discharged on the artifact axis.** The runner the estate READS is now HEAD's: the
CVO's own download of `s3://opal-estate-report/code/estate_report_runner.py` equals `git show HEAD` and
`git show 9e023d20b5` (sha256 `88096c625bf70c3f...`, 159,687 B) and differs from the pre-round-1 blob @`c6d7bfcd5d`
(125,857 B); the issuer's instrument agrees on a different axis (head-object ETag `e75c59a3...` = md5 of HEAD, with the
old blob's md5 = the previous served ETag as the negative control). The upload landed 13:53:22Z with the host stopped
(CloudTrail: the host's own StopInstances 13:11:05Z) and ~23 h before the next boot-time pull, under a NEVER-2 entry
opened BEFORE the act (@`6dbb1e6a3a` 13:52Z) and closed after it (@`9e023d20b5` 14:01Z), with the rollback version
present on the key. **OS-s-19 did what round 1 said no cell owned.**

**OS-s-18 did its half too.** The runner's role holds `s3:GetObject` on `outset/*` (DESIRED @`54ccbdb47d`, plan 0/1/0;
APPLIED re-derived at the CVO on the LIVE plane with `iam:GetRolePolicy`; EXERCISED from inside the 13:00 ET run by the
role itself, four `sts:GetCallerIdentity` events on CloudTrail and four SSM invocations at the same instants); two of
two producers published to a prefix that held zero objects; the battery passes 13 of 13 arms with a planted mutant.

**And the coverage read still does not come out clean, one hop further in than round 1.** Both round-2 cells passed
their bars and the served report renders EXACTLY AS BEFORE, because:

- **the consumer never looks** -- `ESTATE_OUTSET_SEAM_PREFIX` is set nowhere on the host (`instance.tf:130-151`, the
  eleven-variable `runtime.env` heredoc, 0 hits), so `_stratum_propagation` returns `INSTRUMENT_UNAVAILABLE` without
  composing a key (`estate_report_runner.py:1611`, `:1810-1846`); and setting it REPLACES the host
  (`instance.tf:83` `user_data_replace_on_change = true`) -- S16;
- **nothing publishes again** -- the 13:03:50Z publish was by hand; the 26 h ceiling (`:1643`) convicts the artifact
  from ~2026-09-10T15:03Z as STALE -> `INSTRUMENT_FAILED`, which the battery's R5 arm exercises at 999.0 h -- S17.

So **FWD-3 is COVERED on the producer side and NOT REALIZED**, exactly as the CVO carries it (C-S8), and **FWD-2, FWD-4
and FWD-7 are COVERED on the served bytes and EXERCISED no earlier than the 2026-09-10 13:00Z fire.** A REALIZED grade
on any of them today would be round 1's shape one level up.

## 2. THE DEFECT IS IN THIS PRD AGAIN, AND THE v0.3 TEST CAUGHT ONLY HALF OF IT

v0.3's addendum wrote the test: *for every step the architecture section costs, which manifest row owns it?* It found
the publish and the deploy. It did not find the consumer's switch or the cadence, and the reason is structural:
**neither is a COST the architecture section named.** s.3 costed "a publishing step and a freshness question per
artifact"; the freshness QUESTION was answered (the ceiling, the FAILED reading), and the question's own premise --
that something keeps the answer fresh, and that the consumer is configured to ask -- was never a step, so the test
had nothing to place. A test scoped to the costs a section names cannot see the preconditions it assumed.

⛔ **THE SHARPER TEST THIS ROUND EARNS, for every PRD that chooses a seam: A SEAM IS TWO ENDS AND A CLOCK.** The
manifest places (i) the producer's publish, (ii) the consumer's read grant, (iii) the consumer's SWITCH -- the
configuration that makes it look, and (iv) the CLOCK that keeps the artifact inside the consumer's freshness bound --
four rows, or a stated non-application for each. v0.3 placed (i) and (ii). This addendum places (iii) and (iv). Had
the four been asked at L4, round 2 would have been four cells and one round.

Not the issuer's defect and not the assignee's: the cut was clean against the manifest it was given; the assignee
passed its bars with a control that could fail on every arm and wrote the limit of its claim beside O18-AC2
(6 statements + UNCOVERED, which the CVO then resolved to 7 of 7). **The manifest was short before either saw it.**

## 3. The answer: a PRD ADDENDUM v0.3 -> v0.4, two rows, both CloudOps, both already PLACED by ruling

The rulings of @`e18317d0e0` become manifest rows; the addendum is where a placed surface becomes a cell.

| id | outcome_ref | surface | claim | evidence | lane | verb | depends_on | accept |
|---|---|---|---|---|---|---|---|---|
| `OS-s-20` | FWD-3 | THE CONSUMER SWITCH -- `ESTATE_OUTSET_SEAM_PREFIX` set on the report host so the runner's propagation stratum composes the seam key | **absent** | the `runtime.env` heredoc `instance.tf:130-151` sets no prefix; the runner reads it unset `:1611` and returns `INSTRUMENT_UNAVAILABLE` `:1810-1846`; `instance.tf:83` makes the edit a HOST REPLACEMENT (S16) | CloudOps | deploy | OS-s-19 (DONE) -- a dependency edge, not a preference: the host boots whatever runner sits in S3 (`instance.tf:94-96`) | on a SCHEDULED 13:00Z run of the replaced host, the served report's propagation stratum returns an answer state other than `INSTRUMENT_UNAVAILABLE` with the seam artifact's vintage disclosed; the replace under its OWN NEVER-2 entry, outside the run window, the orchestrator's target instance ID re-pointed and verified LIVE before the entry closes (`instance.tf:114-121`); the env line present on the live host is a CONTROL, never the accept. Andrew's GO in principle @`e1b44ba4cc` rides this row; the lane does not ask again for the same act |
| `OS-s-21` | FWD-3 | THE CADENCE -- a producer-side schedule that publishes the two seam artifacts before each 13:00Z run | **absent** | the 13:03:50Z publish was by hand; `OUTSET_SEAM_MAX_AGE_HOURS` defaults to 26 (`:1643`) and `runtime.env` does not override it, so the artifact reads STALE -> `INSTRUMENT_FAILED` from ~2026-09-10T15:03Z (S17); the R5 arm convicts at 999.0 h | CloudOps | build | OS-s-20 on the ACCEPT edge only (buildable in parallel) | on a real day the artifact's vintage precedes that day's 13:00Z run and the served stratum reads FRESH with age < 26 h disclosed; with the schedule disabled the R5 arm still convicts at > 26 h (the negative arm); the trigger is the producer's OWN schedule -- never success-of-upstream as the only trigger, never a watcher on the consumer (a pipeline trigger is not a monitor; the moratorium does not reach it); a hand publish is QA and never the exercise; the scheduled publish writes ONLY the two seam keys (the R2 probe artifact `outset/_os18_red_arm_probe.json` is its author's under PRD R-5, untouched) |

Both rows are CloudOps: a host replacement and a scheduler are cloud acts, the boundary that sent OS-s-6/7/18/19 to
that lane. Neither is a worker's.

## 4. Grades

`dep_stage` **EXECUTING -> ROUND_CLOSE**. Not CLOSED:

| outcome | grade at this read | gradable when |
|---|---|---|
| FWD-2, FWD-4, FWD-7 | **NOT_EVALUATED** -- COVERED on the served bytes (the runner is HEAD's), not yet exercised on a scheduled fire | the 2026-09-10 13:00Z fire's served day, read by `3.0.0_SA_CVO` |
| FWD-3 | **NOT_REALIZED** -- producer side COVERED (C-S6), the consumer never looks and nothing re-publishes | OS-s-20's and OS-s-21's accepts on a served day |
| FWD-1, FWD-5, FWD-6, FWD-8 | unchanged from round 1's reading; not re-read this round (the slug's own words) | -- |

R6 refuses CLOSED until every grade is REALIZED, and it is right to: **the estate now runs the right program and
still cannot see the seam.**

## 5. What the round is worth recording for

- **COMMITTED became SERVED because the analysis PLACED the step.** OS-s-19 is the row round 1 wrote; it landed
  eleven days of drift in one 13:53Z upload under a ledger opened before the act. The v0.3 test works on the class it
  was written for.
- **A seam is two ends and a clock** (s.2 above). The v0.3 test is scoped to COSTS a section names; the preconditions
  a section ASSUMES are the uncovered members, and they were found the same way round 1's were -- by an assignee at
  its first commit and by the CVO at L9, never by this document. Rule 22's uncovered-member clause, applied to a
  test this seat wrote four days ago.
- **The issuer's cut defect S18 -- a seat-addressed tree order's `<paths>` block is not a grant -- was ruled at L6
  @`cb43d05200` without a round trip**, and its design fact is carried to the brief-to-cut chain's L4 @`e18317d0e0`
  as a measured instance of that project's FWD-1 (Andrew confirmed its DONE WHEN lines today @`6ccebb9ae5`). No
  second carrier is opened here.
- **The CVO named its instruments so this read can tell corroboration from repetition**: `iam:GetRolePolicy` on the
  live plane (the face's own instrument, re-run at a second seat), a 224-role census walk with the runner role as
  a positive control -- which caught a first pass reading 0 of 224 on capitalised keys before any number was quoted
  -- CloudTrail and SSM history for EXERCISED, and its own download against three git pins for the bytes. Neither
  battery was re-run, because O18-AC1's R2 arm writes to the live seam. That is the discipline this analysis leans
  on, and it is stated so a later reader can see where the independence is.
- **Two estate facts named by the slug and NOT rowed by this project**, carried to this seat's queue for the roadmap
  rather than manufactured into cells: two roles reach every object in every bucket of the account by managed policy
  (`opal-drift-producer-codebuild-role` ReadOnlyAccess, `opal-news-lambda-role` AmazonS3ReadOnlyAccess) -- an
  account-posture item outside every FWD here; and the battery's R2 probe artifact sits at a fixed key on the live
  seam prefix, never composed by the exact-key consumer, its removal its author's under PRD R-5 -- bounded on
  OS-s-21's face above rather than rowed.
- **S20** (`comp-iam refresh-census` carries no users or groups, so a reach read from it is role-only) is
  `0.8.0_AE_CloudComp`'s at REMEDIATION_v1.md, the lane S2/S6 already carry.

## 6. Next

`2.0.0_SA_COO` recuts from this analysis: two rows, both CloudOps, no worker fan-out; OS-s-20 after OS-s-19 (done),
OS-s-21 buildable beside it with its accept gated on OS-s-20's; the replace scheduled OUTSIDE the run window (the host
stops itself after each 13:00Z run; the window is the rest of the day) with its ledger entry naming the host, the
runner bytes it will boot and the rollback, and the orchestrator's target re-pointed and read live before the entry
closes. **Andrew's GO in principle for the replacement is on the record @`e1b44ba4cc` and rides OS-s-20's face, so
nothing here returns to him.** The CVO grades both against the accepts as written; FWD-2/4/7 are read on the
2026-09-10 served day whether or not the recut has landed.
