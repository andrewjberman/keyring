# 0.7.0_AE_CloudOps~G -- ADVI_PERFRP.TO-R1-AE re-seat: AC4 closed on the scheduled plane, and a fail-closed test whose subject had moved out from under it

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, SCRIBE

**Window:** 2026-08-28T15:54Z -> 16:40Z. First log of this seat since 2026-08-25 (predecessor
sessions died in the 08-27 ~00:0xZ drawdown).
**Serial:** `0.7.0_AE_CloudOps~G`, PID 12592. Re-seated by `2.0.0_SA_COO` 78244 under
`1.0.0_SA_CTO`'s D2-D3 ledger row 10, on Andrew's 15:32Z word. ONE project: `ADVI_PERFRP`,
ONE task order: `TO-R1-AE`.
**Zero crons.** Inbox Monitor `bxuipd592`, banner `parent-tied: pid 1121997` (armed, not
orphan-capable).

---

## What this session did

Closed `PRFR1AE-AC4` -- the last criterion on this TO that was not sovereign-held. It had been
open for three days **not because it was blocked but because it was UNSTAFFED**:
`0.7.0_AE_CloudOps~L` closed AC4's APPLIED half on 08-26 and named the remaining sub-clause in one
sentence -- *"the first SCHEDULED fire carrying the stage is 2026-08-27 12:45Z UTC"* -- and then
every executing seat on the project closed in the 08-27 ~00:0xZ drawdown. `org/projects/ADVI_PERFRP.json`
records the read was never taken (zero ADVI commits on 08-27). Two such fires had since fired.

**Two findings that were not in the brief, and both are the same class -- a true record whose
subject moved:**

1. **The deployed object had moved since `0.7.0_AE_CloudOps~L` measured it.** 31,943 -> 33,416 LF
   bytes: `0.4.0_DS_ClientPlatform~U` landed three P14-PRECOND/P14-STAMP edits to
   `chain_49f_entrypoint.py` on 08-27, deployed 20:07-23:17Z. Carrying the inherited hash forward
   would have been a true-when-written claim about the wrong bytes.
2. **The EXERCISED arm had gone stale and nothing said so.** AC4 requires *"a forced c04 failure
   leaves the projection UNRUN -- exercised."* That was run 2026-08-25 against `b9915d8271` --
   three commits and 1,473 LF bytes behind deployed by the time it was being quoted. A structural
   read of the new source is not an exercise. **Re-ran it against the deployed bytes** rather than
   re-citing it.

---

## Deployment Sequence + Verification (AE role section)

**NO DEPLOY. Nothing was deployed, applied, published, enabled or scheduled this session; no
Terraform ran; NEVER#6 does not attach.** The AE-plane work was entirely a read of the applied
world plus one local harness. Recorded explicitly rather than omitted -- an absent deploy section
and an unrecorded deploy look identical.

### Verification 1 -- the scheduled fires (ACTUAL output)

`s3api list-objects-v2` over `gold/advi/_logs/` (UTC; never `s3 ls`, which renders LOCAL time).
Denominator 22 `chain_*` objects; the three below are every 12:45Z scheduled fire from 08-26 on.

| fire (UTC) | `stages=` | `perfrp_projection` | `c04_validation` | verdict |
|---|---|---|---|---|
| 2026-08-26T12:45:42Z | 16 | **ABSENT** | line 97 | `CHAIN OK date=2026-08-25 wall=113.0s` |
| 2026-08-27T12:45:42Z | 17 | line **113** | line 97 | `CHAIN OK date=2026-08-26 wall=122.5s` |
| 2026-08-28T12:45:42Z | 17 | line **119** | line 103 | `CHAIN OK date=2026-08-27 wall=110.7s` |

```
STAGE OK perfrp_projection rc=0 wall=10.1s families=11 attempted=11 built=6 refused=5
  hard_fail=0 (publisher rc=1; refusals are a DECLARED round-1 state, not a failure)
```

**The negative control is a REAL fire, not a constructed one.** The 08-26 log is discriminating
rather than unreadable precisely because `c04_validation` IS present in it -- an instrument that
could not see the stage would have missed the battery too.

### Verification 2 -- which bytes each fire actually ran

`get-bucket-versioning` -> `Enabled`, so the object live at each fire is a thing you FETCH, not a
thing bracketed between two `LastModified` readings. 20 versions exist; 3 pulled by `--version-id`.
LF-normalised (a raw sha256 across the CRLF/LF boundary emits false drift).

| fire | version-id | LF sha256 | LF bytes | stage in source |
|---|---|---|---|---|
| 08-26 | `E_I103B_frOcXCQ6p.1CiUW_ut27vrlk` | `070765998b787e34` | 25,508 | **False** |
| 08-27 | `jRckhCWP9aW45Ezmb5PpYSFM450dLr9y` | `5df344ca97e8b17d` | 31,943 | True |
| 08-28 | `FGvWchopqxXt.d415Z8znam3jsIXYm8J` | `fc829256f45187bf` | 33,416 | True |

Deployed == `HEAD b5e05eee78` == clean working tree. Six of seven git vintages differ (the
negative controls). Ancestry deliberately NOT used for the deployed-bytes question
(Rule 22a `@4424c948f7`); it is not the correct instrument there.

### Verification 3 -- fail-closed, re-exercised at the DEPLOYED vintage (ACTUAL output)

Subject `fc829256f45187bf`, staged into the EC2 runner's own bundle layout and asserted
byte-identical to the fetched object first. Arms transcribed from the CRITERION before the
implementation was read.

```
[ARM A  c04 PASSES] c04_rc=0 -> main_rc=0 | c04_invoked=True | perfrp_projection_ran=True
[ARM B  c04 FAILS ] c04_rc=3 -> main_rc=3 | c04_invoked=True | perfrp_projection_ran=False
  PASS  ARM A: c04 was actually invoked (arm is live, not skipped)
  PASS  ARM A: projection RAN when c04 passed
  PASS  ARM B: c04 was actually invoked (arm is live, not skipped)
  PASS  ARM B: projection did NOT run when c04 failed
  PASS  ARM B: main() returned c04's rc (3), not 0
  PASS  ARMS DIFFER on the field under test
VERDICT: PASS (6/6 arms+assertions)
```

**ARM A is load-bearing.** Without it, ARM B's silence is equally consistent with the call site
having been DELETED by one of `0.4.0_DS_ClientPlatform~U`'s three edits -- an absent stage and a
fail-closed stage are indistinguishable on the failing arm alone. The `c04_invoked` assertion is
the same discipline one level down: an arm that skipped the battery would also report
`perfrp_projection_ran=False` and read as a pass.

Harness's own guard negative-controlled: a bundle missing `lib/trading_calendar.py` prints
`BLOCKED rc=2`, because the entrypoint's bootstrap ABORT exits before either arm runs.

### Verification 4 -- zero new schedules/rules, BOTH planes

Materialised client-side; **no `--query length()`** (returns the PAGE count), no `--no-paginate`.

| plane | rows | matching `perfrp` |
|---|---|---|
| `events list-rules` | 139 | **0** |
| `scheduler list-schedules` | 18 | **0** |

`advi-49f-gold-floor` `cron(45 12 * * ? *)` UTC ENABLED -> `advi-49f-gold-dispatch` (the existing
rule the stage rides). `advi-49f-publisher` `cron(15 13)` still **DISABLED** -- independent
confirmation that nobody activated a publish in the interval.

**Denominator moved and it is not mine:** 139 against `0.7.0_AE_CloudOps~L`'s 137 on 08-26. Two
rules added estate-wide by other lanes; 0 matching `perfrp` or this TO's surface. Recorded rather
than smoothed over -- a denominator quoted without noticing it moved is how a census stops being
a census.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `commit-gate.sh` | on the new `.py` deliverable | **PASS** | py_compile + ds-precommit + ruff py39, 1 of 1 file |
| `safe-commit.sh` | 2 commits, `-F` msgfile written by the Write tool | **PASS** | risk-reflex CLEAN (3 files then 1, against 1,910 danger nodes); `[msg-verify] MATCH` on both |
| `proof-of-spec-check.py` | positional, 6 criteria | **PASS** | `VALID rc=0`, 6 rows, violations=0, 5/5 cell_refs resolve, 5/5 declared cells reachable. **Run TWICE** -- the second run is the control that the `<cell_status>` face edit did not widen the harvested claim set (byte-identical verdict) |

**No `comp-*` tool was run, and that is a decision rather than an omission.** Every question this
session asked was about an APPLIED artifact at a named vintage -- which bytes ran, which fires
carried the stage, which rules exist on which plane. `comp-trigger` answers DECLARED-ness and
does not carry the cron expression (it prints `schedule: -`), so the APPLIED value comes from
`aws scheduler get-schedule` either way; its earlier run on `advi-49f-gold-floor` is already
recorded on the instance and re-running it would have been repetition, not corroboration.

**What worked:** S3 object VERSIONING as the instrument for "which bytes ran at time T". It
converts an inference (bracketing a fire between two `LastModified` readings) into a fetch. Worth
reaching for on any versioned bucket before writing "the deployed object at that time was...".

**Gap found:** nothing in the estate re-points a verification harness at a moving subject. The
08-25 fail-closed exercise was correct, was cited correctly, and silently stopped being about the
deployed code three commits later. Mitigated locally by committing the harness with a `--target`
flag; the general class is `NFRA_TORECORD`'s and is not this seat's to build.

---

## MCP traffic

6 messages handled, 4 acked via `ack_messages` (72151, 78244, 78266, 78267).

- **IN 78244** `2.0.0_SA_COO` -- the re-seat dispatch. ACK + first report owed on read.
- **OUT 78263/78264** -> COO + CTO -- TO state as measured at re-seat. Where it differed from the
  brief: `0.7.0_AE_CloudOps~K`'s 72788 "3 open criteria collapse to ONE gate" was **TWO** gates
  today, and the second was not sovereign-held.
- **IN 78266** `1.0.0_SA_CTO` -- two-gate framing CONFIRMED; take the read; state the correction
  on the face with the date it became true.
- **IN 78267** `2.0.0_SA_COO` -- same, accepted as measured.
- **OUT 78306/78307** -> COO + CTO -- the flip, hashes, measured push state.
- **IN 72151** `2.0.0_SA_COO`, 2026-08-26 -- MDPF_GLOBAL re-seat, its own s.6 stands a
  late-waking `~G` down. Two days stale, spent, nothing produced.

---

## Files Modified

See commit messages: `debe9bc7b4`, `a3b962f23d`. Additional context on one:

| file | note |
|---|---|
| `.../task_orders/ADVI_PERFRP.TO-R1-AE...md` | **Additive only.** `<status>`, `<issued_to>`, `<decomp_ref>` and every criterion are the ISSUER's and untouched -- `2.0.0_SA_COO` 73606 recorded damaging two TO faces by editing issuer fields. The cell ids sit OUTSIDE `<decomp_ref>` deliberately: that element is the one `proof-of-spec-check.py:259` harvests, and the issuer already had to relocate a clause out of it once for exactly this reason. |

---

## Blockers

**BLOCKED -- evidence-cited, and the gate has a named sovereign owner.**

`ADVI_PERFRP.TO-R1-AE`'s open set is now exactly **GATE A** -- `AC1` residual (D5 no-write needs a
live publish then a second identical run), `AC3` (the EXERCISED half needs a PUBLISHED leaf; 0 of
11 served), `AC6` (a deploy criterion cannot be evaluated before a deploy exists). **All three are
ONE act: the P4I-3 publish activation.**

Held by **Andrew-direct 2026-08-21T19:18Z** (the 49F flip waits on BOTH source gaps AND schedule),
recorded at `portal/src/api/endpoints/adviKeyRepoint.ts`, and independently by the ~08:5xZ DATA
half. Two mechanical arms confirm nothing has drifted: `advi-49f-publisher` **DISABLED** (measured
this session) and `OPAL_ADVI_PUBLISH_GRANT` unset -- a bare enable fails closed by design.

**Not inferring a lift and not asking for one.** `2.0.0_SA_COO` 78267 confirms it is already a
named sovereign card on the D2 register and is not re-asked on a timer.

**Not a blocker, listed so it is not read as mine:**
`org/critical_paths/.open_findings/ADVI_PERFRP_closeout_drift_20260826T192437Z.json` carries
`owner: 2.0.0_SA_COO` and `review_by: 2026-08-28` -- due today. Advisory, non-blocking, untouched;
the date was flagged to COO in 78306 s.6.

---

## Current State

**For a reader with zero prior context.**

`ADVI_PERFRP.TO-R1-AE` is a 5-cell / 6-criterion AE task order: wire the DS lane's PERFRP emitters
into the 49F publisher, IAM for the new keys, the scoped route, a projection stage on the EXISTING
49F gold cron, and the cross-firm firm-pin at IAM.

**Criteria: `AC1` UNCOMPUTABLE | `AC2` PASS | `AC3` UNCOMPUTABLE | `AC4` PASS | `AC5` PASS |
`AC6` UNCOMPUTABLE.** Instance:
`org/tier2_senior/0.7.0_AE_CloudOps~G/deliverables/ADVI_PERFRP.TO-R1-AE_PROOF_OF_SPEC.json`,
`VALID rc=0` positional.

**The projection stage is LIVE and healthy on the scheduled cron.** It runs inside
`data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py` at `_run_perfrp_projection()`
(`:322`), invoked at `:526` AFTER the c04 battery block that `return`s on failure (`:502-513`) --
fail-closed by CONTROL FLOW, not by a flag. It executes from
`s3://opal-data-49financial/_code/chain_49f_entrypoint.py` (`s3 sync` fresh every run), currently
version `FGvWchopqxXt.d415Z8znam3jsIXYm8J`, LF sha256 `fc829256f45187bf`, == `HEAD b5e05eee78`.
Trigger: Scheduler entry `advi-49f-gold-floor`, `cron(45 12 * * ? *)` UTC, ENABLED, target
`arn:aws:lambda:us-east-1:313476888478:function:advi-49f-gold-dispatch`.

**Nothing is SERVED.** The stage builds 6 of 11 families into a staging tree; the publisher returns
`would_publish`; **zero objects exist under `platinum/advi/49financial/perfrp_*`**. Five families
refuse BY DESIGN in round 1 (gainloss rel+acct, transactions, roster, book_advisor -- all read
planes outside the gold plane), and `publisher rc=1` IS the expected healthy state, which is why
the stage classifies off the run manifest's per-key rows rather than off the rc.

**Commits (both LOCAL):** `debe9bc7b4` (the AC4 flip + acceptance-read deliverable + the harness),
`a3b962f23d` (the face `cell_status`). `origin/CLOUD` reads `b6410c65d7` by `ls-remote`; 22 commits
ahead across 10 distinct author lines, so this is a fabric-wide integration window and 2 of the 22
are this seat's. Integrator pushes (`0.0.0_AB_MSTR`'s window, per `1.0.0_SA_CTO` 78266). Ancestry
instrument positive-controlled.

**Re-runnable evidence for a successor:**
`ADVI_PERFRP.TO-R1-AE_AC4_FAILCLOSED_EXERCISE.py --target <bundle>/chain_49f_entrypoint.py`. Fetch
the DEPLOYED object into a bundle layout first (it needs `lib/trading_calendar.py` beside it) --
running it against the repo copy answers a question nobody asked.

---

## Next Steps

- **[`2.0.0_SA_COO`] Hold this seat or release it.** Asked in 78306 s.5, no preference stated. With
  GATE A held there is no unblocked act on `TO-R1-AE`. (a) Hold: this seat reads tomorrow's 12:45Z
  fire as a one-liner and takes anything ad-hoc. (b) Release: `AC4` is closed and needs no watcher
  -- a regression shows as an ABSENT stage in a log anyone can read, and the harness is committed.
  A re-seat or release ask goes to COO, not MSTR (Andrew 15:32Z `@b3f9f207da`).
- **[`2.0.0_SA_COO`] The publish gate as an OPEN CALL to Andrew** -- if it is one he is ready to be
  asked about. Routed through COO by design; this seat does not raise it directly.
- **[`2.0.0_SA_COO`] `ADVI_PERFRP_closeout_drift_20260826T192437Z.json`** -- `review_by` is today.
