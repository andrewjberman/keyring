# The event gate discharged, and the located evidence was on the wrong plane -- ETFS_INGEST.TO-10-AE -- 0.7.0_AE_CloudOps~M

**Date:** 2026-08-29
**Task Order:** ETFS_INGEST.TO-10-AE
**Status:** COMPLETE -- AC3 scored on the scheduled fire; 4 of 4 criteria PASS; instance VALID with coverage checked
**Session:** 13:05Z - 13:25Z
**Seat:** `0.7.0_AE_CloudOps~M` (re-address by `2.0.0_SA_COO~Z`; AC1/AC2/AC4 were filed 2026-08-28 by `0.7.0_AE_CloudOps~I`)

## Objective

Score `INGEST-TO10-AC3`, the one criterion the earlier lane correctly could not close. It was
`UNCOMPUTABLE-BY-CONSTRUCTION` because it is EVENT-GATED on the first scheduled producer fire after
the 2026-08-28T18:49:14Z apply, and the TO barred the one act that could have computed it sooner.
That fire happened at 2026-08-29T13:00Z. Nothing else in the face was mine to re-open.

## Compiler Tools

**None ran, and that is the answer rather than an omission.** AC3 is a census of field VALUES inside
one served JSON object against its own prior version. The comp-* set is connection- and code-shaped:
`comp-closure` compares deployed bytes to a build input, `comp-iam` models grants, `comp-pipescript`
audits columns. None reads a served artifact's value distribution, and the code-currency question
they serve was already closed by AC1 at the earlier lane.

`comp-validate` was **considered and deliberately not run.** Its config is keyed to gold-script
artifacts; per `COMP_VALIDATE_PROTOCOL`, a `NO_CONFIG` verdict is UNVALIDATED and never a pass. It
would have produced a clean-looking line certifying nothing, which is worse than no line.

**Instrument trap met, and it manufactured a false anomaly.** `aws logs describe-log-streams`
reported `lastEventTimestamp` 13:00:47Z for the 08-29 stream while that stream's own events run to
13:01:24Z -- an apparent 5-second run against 43 seconds on each prior day, which read as a failed
or short-circuited fire. That field is best-effort and lags. `get-log-events` is the sound read.
**I resolved it by reading the events, not by re-running the same command against the same plane.**

## Deployment Sequence

**None. This session deployed nothing and applied nothing.** The apply was the earlier lane's act
(AC2, `safe-apply`, ledger opened `16db6d3529` and closed `355911b9db`). This was a measurement
session against live state, so no `safe-apply`, no ledger entry, and no rollback handle are in scope.

## Verification

**AC3 -- the fire was the SCHEDULED one, measured rather than assumed.** The producer's own first log
line is `[etf_positioning_gold] lambda_handler: run_class=scheduled`, RequestId
`497b6400-2342-485d-9936-4a67aa35b60a`. The no-ad-hoc bar is discharged by the world, not by this
seat's restraint: over a **14-of-14 unpaginated log-stream census** (counted client-side, `nextToken`
absent), **0** streams start between the apply and the fire -- so this fire IS the first invocation
after the apply -- and **1** stream exists on 08-29, so nothing was interleaved.

**Grain -- the bytes I censused are the bytes the producer emitted.** The publisher logged
`built 148372 B, sha256 80c128dcf08b3855...`; the object I pulled is 148372 B and hashes
`80c128dcf08b3855a8ee38e8b288f9c36778313339fe3a116c4f1fb47cecd3f2`. I checked the local file size
against `ContentLength` before parsing, so the shim class where a get returns rc=0 and writes nothing
is excluded rather than assumed away.

**The criterion, term by term** (denominator 189 rows: 30 DIVZ + 45 IDVZ + 90 PFDE + 24 PFOE;
`data_date` advanced 2026-08-27 -> 2026-08-28):

| term | result |
|---|---|
| 7 completed labels | **7 of 7** distinct transitions, over 59 rows |
| basis on changed rows | `inferred-from-truncation` on **59 of 59** |
| basis retained where unchanged | `observed` on **121 of 121** unchanged equity rows |
| truncation on the served plane | **0** values at the 30-char cap, against 6 pre-fire; max length 30 -> 46 |

The full basis transition map over all 189 rows has exactly four entries and no others:
`observed->observed` 121, `observed->inferred-from-truncation` 59,
`not-applicable-non-equity->itself` 8, `absent-from-source->itself` 1. 121+59+8+1 = 189.

**Discrimination.** Had the deployed bytes not carried the decode, the served artifact would still
show 6 values at exactly 30 chars and a basis census of `observed`=180 -- which is precisely the
PRE-fire reading, and is what the prior served version actually shows. The two states are not
confusable, so the evidence could have come back different if the claim were false.

**A negative control that was in the data rather than planted.** `Household & Personal Products` is
29 chars and is a COMPLETE GICS name, not a truncation. The decode left it untouched and it retained
`observed`. A 59-row count alone could not have shown the decode does not over-fire on a
short-but-complete label; this does.

**AC4 re-scored on the stronger instrument.** The earlier PASS drove the deployed module over the
served rows. The real served before/after pair only became available with this fire: pre-fire
VersionId `5UfK2PDL0XlQCzoIjoFGivz3WqPp_h86` (146944 B) vs post-fire
`bpgnYq4ir2yrM5cnWgJ35DzmnqalquU5` (148372 B), joined on `(portfolio,ticker)` -- 189/189 rows, 0
unmatched either side, 0 gaining the key, 0 losing it, 0 losing a value, non-null 180 before and 180
after. The artifact GREW, which is the expected direction when 59 rows take longer labels; a shrink
would have been the signal to look.

**Instance check.** `proof-of-spec-check` reads **VALID, violations=0**, and I ran it WITH the TO's
declared expected set (`expected=4 carried=4 matched=4`) rather than accepting the default
`COVERAGE UNCHECKED` note. **Positive-control on the coverage limb: a planted fifth id makes it fire
(`INVALID`, `silent omission`)** -- so that limb is live here, not a vacuous pass. Separately, **rc
is not the oracle for this tool: my first run returned rc=0 while printing `INVALID`.** The verdict
line is what I read.

## THE FINDING -- the located evidence read as a negative and was not one

The re-address carried post-fire measurements that look like the fix did not land: *"industry_group
in the POST-FIRE artifact ... SIX sit at EXACTLY 30 chars, max len over all values = 30."* The issuer
flagged it as LOCATED, NOT ADJUDICATED and said plainly they had not read this face's AC text -- which
is exactly why it needed checking rather than believing in either direction.

**It is the GOLD parquet, and gold is CORRECT to look like that.** I re-read
`gold/holding/date=2026-08-28/holding.parquet` (45630 B, 189 rows) and reproduced the issuer's number
exactly: max length 30, the same six values at the cap. Then I read the decode's location at source,
at the applied pin: `git show b066be7a92:data/etfs/scripts/gold/etf_positioning_publisher.py`,
`_industry_group`. **The decode is publisher-side, applied at platinum-write time.** Gold is upstream
of it and legitimately still carries Bloomberg's capped strings. AC3's instrument is the platinum
served object, and on that plane the truncation is gone.

**Two planes share one artifact name, and the criterion names which plane it means.** Had I scored
the criterion on the plane handed to me, I would have failed a criterion that passes, and the failure
would have looked well-evidenced -- a real measurement, correctly taken, of the wrong object.

**The 7th label is why the issuer's scan found only six.** Six values truncate at exactly 30 chars;
the seventh, `Consumer Staples Distribution`, truncates at a space and is stripped to **29**. A
census keyed to the cap length structurally cannot see it. The transition diff, which keys on
CHANGE rather than on length, found all seven.

## Decisions Made

1. **Scored AC3 on what the artifact DID, not against the 59-of-189 prediction.** The TO bars grading
   it against that figure. The observed count IS 59 over 7 labels, reported as corroboration from a
   third independent instrument -- a served before/after diff, versus the issuing seat's pre-deploy
   simulation and the earlier lane's drive of the deployed module. Had it come back 61 over 7 labels,
   AC3 would still have passed.
2. **Did not re-open AC1 or AC2.** Out of this seat's scope; the earlier lane's evidence stands.
3. **Did not add the served artifact to `artifacts_produced`.** It is AC3's evidence, not something
   this TO produced, and the schema has no `deployed_state` member for a served object. I declined to
   stretch an enum to fit; the evidence lives in `output_evidence` where it belongs.
4. **Did not push.** Integrator's act (LD-0367).

## Files Modified

- `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/ETFS_INGEST.TO-10-AE_PROOF_OF_SPEC.json` -- AC3
  `UNCOMPUTABLE-BY-CONSTRUCTION` -> `PASS` with evidence and denominator; AC4 evidence extended with
  the post-fire re-score; exclusion #1 marked partially discharged; compiler-tools entry recording
  why none ran and the `describe-log-streams` trap; `assignee` -> `~M`; `session_log` -> this file.
- `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ETFS_INGEST.TO-10-AE.producer-apply-for-the-etfclassifier-fold.md`
  -- `<status>` pending -> complete, self-marked per `org/XXX.md`.

## Blockers

**NONE at this seat.** The face is closed and nothing in it waits on anyone.

## Current State

`ETFS_INGEST.TO-10-AE` is COMPLETE with 4 of 4 criteria PASS and a VALID instance. The ETFClassifier
fold is live and EXERCISED on the served plane: `platinum/etfs/positioning_data.json` at VersionId
`bpgnYq4ir2yrM5cnWgJ35DzmnqalquU5` carries 7 completed GICS labels across 59 of 189 rows, each
correctly stamped `inferred-from-truncation`, with every untouched row's basis preserved.

**Push state: LOCAL.** Commit is on `SITEZ` at this device only; `--follow-tags` and the shared-branch
push are the integrator's act and were not taken.

## Next Steps

- [`2.0.0_SA_COO~Z`] RAVC2 sent. Validate and close, or return REWORK against the AC text.
- [`0.0.0_AB_MSTR~Z`] Integrator: this commit, plus the still-outstanding annotated tag
  `etfs-positioning-v1.4.0` named as excluded in the earlier lane's filing.
- **NOT MINE, listed so it is not read as dropped:** `ABT`'s 0-of-8 return windows, reproduced across
  the 08-27 and 08-28 partitions, is `ETFS_POSITIONING.TO-13-DS` on `0.4.0_DS_ClientPlatform~Y`.

## Surprises (channel: `3.0.0_SA_CVO~Z`, class OBSERVATION, standing INERT -- not chased)

1. **`PROOF_OF_SPEC.schema.json`'s `deployed_state` enum has no member for a SERVED artifact.** The
   three values are `DEPLOYED-VERIFIED` / `COMMITTED-NOT-DEPLOY-SCOPE` / `STAGED-AWAITING-GATE`, all
   of which describe code reaching a runtime. An artifact a pipeline SERVES, verified on the served
   plane, is not expressible -- a Rule 24 MECE gap over the declared domain. I worked around it by
   not filing the row rather than by stretching a value. Surfaced, not proposed: a value-enum change
   needs its four-postulate record, which is not this face's work.
2. **`aws logs describe-log-streams` `lastEventTimestamp` lags its own stream's events** (13:00:47Z
   reported vs 13:01:24Z actual). It manufactured a plausible "the scheduled fire died early" reading
   that survived until I read the events. Worth knowing before anyone builds a freshness or duration
   check on that field.
