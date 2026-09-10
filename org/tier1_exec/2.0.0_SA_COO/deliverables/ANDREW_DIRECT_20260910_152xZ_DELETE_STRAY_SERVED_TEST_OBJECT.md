# ANDREW-DIRECT 2026-09-10 ~15:2xZ -- delete the stray served test object (open call 1 of 2)

**Recorded by:** `2.0.0_SA_COO`
**Channel:** Andrew's typed reply at this seat's own terminal, in response to `/open-calls`.
**Recorded at:** 2026-09-10 ~15:2xZ. Receipt-recording time, not a reconstructed send time.

---

## HIS WORDS, VERBATIM AND ENTIRE

> Yes to Call 1. On Call 2, I do not understand what this drift timer is for exactly, explain

---

## WHAT CALL 1 WAS, quoted from the card he answered

> **Delete the stray test object from the served August prefix -- yes or no?**
> A pytest run of EG-s-29's own suite PUT a real 1,878 B object at
> `platinum/reports/2026-08/coverage_egress_ask_ladder_skipped.json` (13:54:44Z).
> The bucket is UNVERSIONED, so the delete is unrecoverable and is yours.
>
> **REC --** YES, delete.

**"Yes to Call 1" is the confirmation CLAUDE.md's Agent Autonomy section requires** for an
S3 delete: *"Human confirmation ONLY for: recursive deletion, destructive git, dropping tables/S3
deletes, stopping EC2, anything unrecoverable."* The bucket carries no versioning, so the act is
unrecoverable and no agent may take it on its own judgment.

## THE ACT, EXECUTED THIS TURN WITH BEFORE AND AFTER READS

```
BEFORE   head-object -> ETag "647e565208eccd9a0d4b4a08159c082b", 1,878 B
DELETE   aws s3api delete-object --bucket opal-data-etfs \
           --key "platinum/reports/2026-08/coverage_egress_ask_ladder_skipped.json"
AFTER    head-object -> An error occurred (404) when calling the HeadObject operation: Not Found
```

⛔ **AND THE POSITIVE CONTROL, because a delete that removed more than it should would read the same
way on the target key alone.** The six legitimate August artifacts are UNTOUCHED at their original
sizes and timestamps:

| key | size | LastModified |
|---|---|---|
| `coverage_verdict.json` | 1,225 | 2026-09-10T00:24:44Z |
| `etf_ownership.html` | 43,376 | 2026-09-10T00:24:47Z |
| `etf_ownership.pdf` | 252,393 | 2026-09-10T00:24:48Z |
| `opaletfs_49financial_202608.csv` | 2,012 | 2026-09-10T00:24:48Z |
| `opaletfs_cottonwood_202608.csv` | 1,888 | 2026-09-10T00:24:50Z |
| `opaletfs_inflection_202608.csv` | 1,888 | 2026-09-10T00:24:49Z |

Prefix denominator: **7 keys before, 6 after, and the 6 are the 00:24Z re-render's own set.**

## WHY IT WAS THERE, so the record carries the cause and not only the cleanup

`0.9.0_WK_ETFS_GUARDRAIL~5` filed it as row `ETFS_GUARDRAIL-W5-S11`. One `pytest` run of `EG-s-29`'s
own suite PUT a real object into a served prefix **while every assertion passed.** Three arms shared
a premise that was a property of the code -- *"this branch touches no S3"* -- and that cell's own
change killed the premise for all three at once.

**The assignee's handling was correct on both halves and is why this was a clean decision rather than
an incident:** it closed recurrence with an autouse fixture so the suite cannot reach the real bucket
again, and it LEFT THE OBJECT IN PLACE with its exact delete command rather than exercising a
judgment that was not its to make.

## SCOPE, neither widened nor narrowed

His word covers **this one key**. It is not a standing grant to delete served objects, not a grant
over any other prefix or bucket, and not authorization for any other unrecoverable act. Call 2 is
UNANSWERED and remains open -- he asked for an explanation of the drift timer before ruling.

## CONSEQUENCE

Row `ETFS_GUARDRAIL-W5-S11`'s hazard no longer exists in the world, and the carrier for that is a NEW
row -- `ETFS_GUARDRAIL-S37`, in the same commit as this record.

⛔ **I FIRST WROTE THIS SECTION CLAIMING THE ROW WOULD MOVE `ARMED` -> `DISARMED` IN PLACE. THAT WAS
WRONG AND THE GATE REFUSED IT ON TWO LIMBS, BOTH CORRECTLY.** `investigation_item.schema.json` gives
`hazard_standing` the enum `['ARMED','INERT']` -- **`DISARMED` is not a value this row type has** --
and `additionalProperties: false` means the `disarmed_at` I added is not a field it carries. The
nested `disarm` object with a `state`/`at` clock, which the gate's monotone-advance limb does admit,
belongs to `remediation_row.schema.json` -- a DIFFERENT plane, and remediation rows are
`3.0.0_SA_CVO`'s. I reverted with `git checkout HEAD --` and verified the restore (89 rows, W5-S11
reading ARMED, no stray field) before writing `S37`.

**THE CONVENTION THE CHANNEL ALREADY USES**, read from its own rows rather than assumed: a disarm is
recorded in the `disarm_owner` PROSE **at authoring time** (`W4-S5` "DISARMED SAME-TURN by this
cell", `W5-S8` "DISARMED THIS TURN for the instance"). W5-S11 was authored ARMED because at that
moment it WAS armed, so there was no prose to write and a NEW ROW CITING THE OLD ID is the only
carrier -- the same mechanism `S36` used for the eleven re-pointed rows an hour earlier.

⚠ **AND THE GATE HAD ALREADY TAUGHT ME THAT LESSON ONCE TODAY**, on `S36`. The second refusal is
mine, not the gate's. W5-S11's own row will read `ARMED` permanently, and that is what an
append-only channel means: its standing lives in `S37`, found by id.
