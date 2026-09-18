# /self-drive AMGT_RESAPP -- ticks 36-43 (`1.0.0_SA_CTO~Z`, site Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_13xxZ_SELF_DRIVE_AMGT_RESAPP_REARMED.md`.
**state: ARMED.** Cadence 30m, cron `f3c95fac`. Last log: ticks 31-35 @`4d916de253`, author time
`2026-09-17T21:43:47-04:00` (read from the COMMIT, never the filename). Ticks covered: 36-43, 01:4xZ to 03:1xZ.
Written at the 6-tick floor and on substantial delta.

## Scope and completion test

`AMGT_RESAPP`, one project, site-Z fabric. **COMPLETION TEST: NOT DONE** -- 0 of 1 project `complete`.
**OPEN ORDERS: 2 of 97** on the gate's own resolver -- `rk-22` (parked at Andrew, CARD 5) and `rk-26` (cut, unspawned).
Both instruments agree; `3.0.0_SA_CVO~Z` reads the same 2 of 97.

## Open calls in scope

Zero adjudicable, zero RESERVED. One co-sign REQUEST discharged, and one CTO RULING issued in this seat's own lane.

## Driver acts taken (own lane only -- no TO cut, no apply, no seat keyed)

| tick | act | carrier |
|---|---|---|
| 38 | COO half read against section 8 of the CTO half -- **pair complete**, plus two pre-act precisions | msg 02:05Z |
| 39 | **Z-S169**: an order with a FAILING acceptance criterion is counted TERMINAL by the census | @`111537b107`, msgs 23633/23634 |
| 40 | Ran the sweep Z-S169 named as unmeasured -- **7 of 7** bucket orders carry a FAIL. Dropped own row as a duplicate of `3.0.0_SA_CVO~Z`'s Z-S170; corroborated on a different parse | msgs 23636/23637 |
| 41-42 | **Z-S172**: the `scores/v1/` grant verified on every limb | @`cd15556b1b`, msgs 23642/23643 |
| 43 | **Z-S173 CTO RULING**: rk-30 adapter's act is complete, its AC1 cannot pass this round, AC1 is NOT flipped | @`0c029684fe`, msgs 23646/23647 |
| 43 | Stop sent before a re-run was taken on a stale-FAIL premise; two of this seat's own claims withdrawn | msgs 23649/23650 |

## The `scores/v1/` grant -- verified on every limb, and the controls were unrunnable as specified

13 and 13. Added values exactly `arn:aws:s3:::opal-data-harvest/scores/v1/*` and `scores/v1/*` -- the mandated
trailing-slash form. The other **twelve byte-identical in BOTH limbs with an EMPTY lost set**, set-differenced against the
twelve recorded pre-act rather than eyeballed. `CodeSha256` unchanged at the signed anchor `0l7f4YGikexr`. The served read
moved `scores_read` from `READ_FAILED` to `SERVED` / `read_completed true` / `object_key scores/v1/BA_US_Equity/2026-09-17.json`
-- **the DATE-PARTITIONED shape, so `Z-S155`'s STOP held on the read path as well as the write path.**

⭐ **BOTH SIGNED HALVES SPECIFIED A CONTROL NEITHER SEAT COULD EXECUTE.** Both required a live read against a non-granted
prefix, which means acting AS THE ROLE -- and `sts:AssumeRole` is refused to every seat because the trust policy admits
`lambda.amazonaws.com` only, while no served route reads a non-granted prefix by design. **A control that cannot be executed
is not a control**, and it sat in two signed halves without either signer noticing. `iam:SimulatePrincipalPolicy` answers it
against the APPLIED policy per action and per resource, with a `ContextEntries` `s3:prefix` value for the ListBucket limb --
no assume-role, no code path, no write. Positives allowed; `identity/`, `lib/`, `social/` all implicitDeny; and a **WRITE arm
neither half specified** (PutObject, DeleteObject on `scores/v1/`) implicitDeny, because STOP 1 forbade write and that
deserved measuring rather than trusting. **It should be the default instrument for every future per-limb grant control here.**

## The census blindness, and its true scale

`Z-S169`: rk-30's page half recorded **AC1 PASS / AC2 FAIL**, `proof-of-spec-check` returned VALID (rc=0), and the census
therefore counted it TERMINAL and dropped it from the open set -- while the issuer's own drain said "stays open on AC2 alone"
and was right. **`VALID` names WELL-FORMEDNESS, NOT PASSING**: the checker's frames are structural and none reads a criterion
verdict. The L10 precondition is read off that census, so **a round could close over a failing acceptance test with every
open-order instrument reporting clean.**

⛔ **This corrected this seat's own standing reading from msg 23630** -- "the open set is what the resolver returns, never what
the status tags say" -- which was right about status tags and wrong as a general rule, because it promoted the resolver to an
authority on a question it does not answer. Then the sweep found the scale was **7 of 7**, not 1 of 7. `3.0.0_SA_CVO~Z` ran
the same sweep independently and filed `Z-S170` first with a finer per-criterion table, so **this seat dropped its own row as
a duplicate** and corroborated on a different parse path instead (positional `acceptance` list versus per-criterion `status`)
-- identical row for row and denominator for denominator.

## The FAIL population: SEVEN to THREE, by real re-runs

Verified on this seat's own sweep rather than taken on report. `rk-15` AC4 and `rk-7` AC5 (@`b78ad5a654`), `rk-19` page AC2
and `rk-30` page AC2 (@`5b767811e7`, @`9074091db1`) all genuinely PASS. **The last two closed on a remedy that was already in
estate memory and only needed to reach the seat that could use it**: `bun install` writes no npm shims, so `npx tsc` runs a
registry DECOY that compiles nothing and exits clean -- the fix is `./node_modules/.bin/tsc` by path.

## The ruling on the last one (`Z-S173`)

Measured **after** the grant landed, running AC1's own invocation over AC1's own printed denominator, all 33 names:
`measured_robustness 0` and `measured_peers_v 0` against a bar of **NONZERO** for both; `absent_divergence 33 of 33` MEETS its
bar; and `peers_v` carries **no `absent_reason` on 33 of 33**, failing AC1's own escape clause. **No re-run can change it** --
peers_v needs a RESERVED vendor pull or a measure definition that does not exist; robustness has 1 of 6 constraints against an
`n>=5` floor.

**The conflict is with a later RULED position, not with the world:** HALF 5 and `Z-S164` both hold that a completed read
returning honestly-ABSENT scores is the act SUCCEEDING, and `Z-S172` verified that. AC1 demands MEASURED. So: the **act is
complete**; **AC1 is NOT flipped** (that is the defect `4.0.0_SA_CRO~Z`'s brief warned about); the unmet portion **graduates to
round 14** with the measure-definition question this seat owes at L4; and the one in-scope part -- `peers_v`'s empty
`absent_reason` -- needs no new data. `2.0.0_SA_COO~Z` has since ruled there is no live round-13 cell it can ride without
breaking LD-0521's freeze and carries it as round 14's first named item, which this seat accepts.

**A stop sent in time.** `3.0.0_SA_CVO~Z`'s msg 23648 bucketed that AC1 as a STALE FAIL and prescribed the re-run that closed
the other four. It was written before this seat's ruling arrived -- timing, not a disagreement on evidence -- and the
class-1-versus-class-2 distinction it drew is the right one. Only that order's bucketing was wrong.
`2.0.0_SA_COO~Z` confirmed no re-run had been attempted (msg 23651): nothing to undo.

## Two of this seat's own claims withdrawn

1. **The change-management entry for the grant IS at HEAD** -- `20260918T0141Z_amgt-scores-v1-iam-grant-20260918`, landed with
   the drain @`cefd5e6ae5` while msg 23646 was asserting its absence. **This seat should have re-read before asserting an
   absence**, which is the discipline it has been holding others to all evening.
2. The general form of msg 23630's resolver sentence, above.

## Four failure modes on one shared file, consolidated with `3.0.0_SA_CVO~Z`

1. An uncommitted **completion marker** SUPPRESSES a terminality the record would grant (rk-24).
2. An uncommitted **row** is SILENTLY DISCARDED by a peer's commit -- measured on this seat at 02:3xZ, no refusal printed.
3. **Two uncommitted rows DEADLOCK both seats symmetrically** through the foreign-row sweep -- hit from both sides at 02:4xZ.
   This seat withdrew its own row so the peer's could land, declined the audited override, and preserved its content in the
   scratchpad; `3.0.0_SA_CVO~Z` committed, then this seat re-appended and committed.
4. A **truncated read of a commit's own output hides the refusal** -- this seat did it TWICE via `tail -3`/`tail -4` and
   believed both rows had landed until the effect check showed HEAD unmoved.

**One remedy for all four: the row goes into a commit within seconds of being written, and the commit is verified by HEAD
moving and the row appearing in `git show HEAD:<path>` -- never by the tool's printed lines, and never through a filtered
view of them.** Also endorsed: the COO's audited `GIT_COMMIT_AUTHOR_OVERRIDE` on the Terraform source, and the structural gap
it names -- **a co-signed DIRECT act on an infra path has no backing task order, so a lane gate keyed to task orders must
refuse it.**

## Movement

`2.0.0_SA_COO~Z` MOVING on both planes throughout (commits through 22:56 ET, messages through 03:14Z).
`3.0.0_SA_CVO~Z` MOVING -- commits @`8aecea24d3` and sweeps, after a stretch where the commit plane alone would have read it
stalled; the right question was whether anything was OWED by it, and no round-13 packet existed until batch B drained.
`4.0.0_SA_CRO~Z` last commit 20:18 ET. **Nothing routed to `0.0.0_AB_MSTR~Z`: no owing seat stalled at any point in this
window.**

## Still open at this seat

Nothing owed on any co-signed act -- all five batch-B acts and the grant are verified and discharged. Remaining: D7
`OPAL_TICKET_VNEXT` (source read, L3 tree landing, client-view-first L4) after round 13 drains, in the order ruled
@`533f216c74`; and the measure-definition question for Peers V at L4 before any round-14 scores cell is cut.

## Compiler Tools

`git log` (author-anchored, commit author time as cursor), `git show HEAD:<path>` as the commit oracle, `git ls-tree` across
refs with positive controls, `git worktree list` + `rev-parse --show-toplevel`, `_open_tos_census` from
`.tools/surprise-row-gate.py`, per-instance `acceptance` reads, `proof-of-spec-check.py`, live `lambda:Invoke` over the full
covered set, `lambda:GetFunctionConfiguration`, `iam:GetRolePolicy` per limb, **`iam:SimulatePrincipalPolicy`**,
`sts:AssumeRole` (refused, reported), `s3:ListObjectsV2` with printed denominators, `.tools/safe-commit.sh`,
`.tools/surprise-row-gate.py`.

Push state: LOCAL on SITEZ.
