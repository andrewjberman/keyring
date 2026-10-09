# Session log -- 0.7.0_AE_CloudOps~SC1, 2026-10-09 11:53Z to ~12:25Z

**archetype:** DEPLOY

Fourth segment of this session (e71b 06:05-06:45Z, e60b 07:00-07:20Z, e79b 09:39-10:05Z). GO msg 2373
arrived on a watcher tick and was acted on the same turn.

## TO-SC-e84b -- the three COT objects shipped TOGETHER. Legs V, P, D CLOSED; leg G is the issuer's.

Evidence is in commit `4a05003ec3` and ledger `secclass-e84-cot-name-port-sc1-20261009`; the proof instance
is VALID (rc=0) with three `s3_object` rows. Not restated here. Four things worth keeping.

### 1. The window was ASKED, not adjudicated -- and the ask was the right call

The order's step 1 said "check that no COT runner is running". `cot-exporter` i-0643a5bee8a8feabf came up at
11:30:17Z with the fire and was still up at 12:02Z. But the gold work was plainly done: outputs written
11:35:55Z and 11:37:09Z, matching the order's own "gold completes about 11:38Z", and both VersionIds held
across 11:55:44Z and 12:02:51Z. So the LITERAL arm was shut while the PURPOSE arm was open.

This is the same split as e79b, with one difference that changed the decision: on e79b the runner stopped
three minutes later and the question went moot, so no ask was sent. Here the instance showed no sign of
stopping, so waiting would have been waiting on nothing. **Asked at 12:04:18Z, ruled at 12:05:13Z** --
AMENDMENT 1 @`88060f2ca9`: "in flight" means the gold chain has not logged completion, NOT that the instance
is stopped. Widening a signed condition on my own judgment would have shipped 4 minutes earlier and left no
record of why it was legitimate.

### 2. The amendment was read at its pin, and its arms were implemented as a guard

`git show 88060f2ca9:<order>` printed the amended step 1 at line 34, beside a positive control (same show
returns 80 lines, so an empty read would have been visible). Then both arms were MEASURED, not assumed:
the COMPLETE marker read from `cot-gold-run-20261009-113353.log`'s own tail bytes with an `INCOMPLETE`
negative control at 0; both served VersionIds re-read in the same shell as the deploy, which aborts if either
moved. `cot-exporter` was still running at the ship -- exactly what the amendment says to disregard, and
exactly what the ORIGINAL condition would have called a STOP.

### 3. "No other key moved" without a pre-act snapshot

This order never took a whole-prefix pre-act ETag baseline for COT (the BD orders did). Rather than quietly
narrow the claim, the question was answered a different way: `list-object-versions` over `code/gold/`,
IsLatest only -> 107 current versions, of which exactly **3** carry a LastModified at or after 12:07:30Z, and
they are the three named. That is strictly better than an ETag diff here -- it catches a key written by any
actor in the window, not only one whose ETag happened to differ.

### 4. Two findings I owned, closed the right way round

The post-commit sweep raised `deploy_stale_20261009T115703Z` and `...T120535Z`, naming C_06 and D_03 STALE on
S3. Both were TRUE when raised -- the window was held and the ship had not happened. They were not deleted on
that reasoning: they were **re-measured with the instrument that raised them** (`comp-pipescript deployed` ->
MATCH for both) and only then removed per their own closing instruction. The sweep now reads 0 open findings.

Disclosed, not glossed: the same tool reads the lib as `1 DECLARED-UNSWEPT` (filter matched 0 of 48 gold
objects). It grades `lib/` paths neither pass nor fail, so **a stale lib/ object cannot raise this
blocking-class finding at all**. The lib's landing rests on head-object and AC1 instead. The tool discloses
the gap itself, so it is recorded in the instance rather than filed as a row.

## What a successor does

Nothing for e84b: leg G is the issuer's (`2.0.0_SA_COO~M1`) and the order instructs no `<status>` flip, so
`pending` is deliberate. The entry is HELD on the 2026-10-10 11:30Z COT fire. Rollback, if leg G fails, is
the three keys restored TOGETHER to `MYI0nB3zRKMU17aCIQiM6fqYv8U3F.ia`,
`55IsnYrr1xiWSvXliMNSM4mQ3bDXGTQ7`, `vHHfV5NdKUY1t4Z8P1mv3vdtnacLHGrJ`, plus each of the 1,136 data keys to
its leg-P VersionId in `E84_PREFIRE_VERSIONS_20261009.json`. **The C_06 target is e67's shipped fix** -- a
rollback keeps e67, it does not revert it.

Carried for whoever grades leg G: the COT gold suite has one pre-existing failure (row D1-S24, the retired-
rule test), so "suite green" was never available as a signal and was not used as one; and COO condition 4
states the 1,060 `NAME::` rows' content was NOT audited.

## Compiler tools

| tool | invocation | result |
|---|---|---|
| `safe-deploy.sh` | `--tree cot` + the three gold paths | gate PASS, 3 of 3 deployed and verified, 0 bundle-members, three `[not shipped]` _shared lines, zero fourth members. |
| `safe_deploy_core.shipped_artifacts_for` | three paths in 2 arms + a separate `_shared`+cot positive control | `[]` for the three under an established discrimination -> true negative. |
| `comp-pipescript deployed` | each shipped script, post-act | C_06 and D_03 MATCH (closed the two findings); lib `DECLARED-UNSWEPT` (see 4 above). |
| `crossbox-deploy-check.py` | `--root data/cot` | 15 hits (OPEN-CALL 8, OVERLAP 1, OPEN-DEPLOY 6), 0 contending; denominator 41 worktrees / 836 sentinel reads / `vanished=0`. Row D1-S25. |
| `deploy_ledger.py` | open 4 legs, close V/P/D, hold | tool auto-committed the sentinel this time; legs closed in evidence order. |
| boto3 `list_object_versions` | leg P (COT clients) and the post-act time sweep | 1,136 keys / 16 pages / 0 holes; 107 current versions with 3 in the ship window. |
| `proof-of-spec-check.py` | `<instance> AC1` | VALID (rc=0); 3 surprise entries all resolving to channel rows. |

Row ids minted max+1 from the channel at write time: the addendum landed as **S25**, because another seat had
taken S24 since the previous mint. Second time that guard mattered today.

## Push state

`4a05003ec3` (e84b ship) -- **LOCAL** at 12:16:31Z; origin `box/dell1` @`6c539063d4`, with `9d5bfa110d` on
origin at that read. This lane does not push a shared branch; `box-sync` carries it.
