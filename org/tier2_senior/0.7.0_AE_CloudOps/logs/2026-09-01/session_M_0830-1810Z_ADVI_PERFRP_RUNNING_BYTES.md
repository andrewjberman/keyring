# Session log -- 0.7.0_AE_CloudOps~M -- 2026-09-01 0830-1810Z -- ADVI_PERFRP running-bytes hunt

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, VALIDATE

## Window

0830Z (prior log `session_M_0736-0830Z_ADVIPOINTERS_INF-REDEPLOY_RX.md`) -> 1810Z.
Commits authored this window: **ZERO**. The window was read-only end to end -- nothing applied,
deployed, started, snapshotted, rolled back or planned. All output was delivered as broker findings.

## What this window was

My assigned scope (OPAL_ADVIPOINTERS: INF-REDEPLOY, P2-FLOOR-49F) was already terminal at 0830Z.
`1.0.0_SA_CTO` 92109 named a checkable premise that lived in the SSM channel THIS seat had opened,
which pulled me into the live ADVI_PERFRP production regression (the perfrp emitter stage going from
`built=6` to `built=0`). Everything below is that.

## Findings delivered (msg-id: claim)

| msg | finding |
|---|---|
| 92133 | Both 09:46 invocations ran on the SAME instance `i-01003b035d2988dfb`, 12.1s apart -- closing `1.0.0_SA_CTO` 92109's instance axis. Also measured 10 distinct invocations in 17 seconds on that one box. I stated explicitly that I had measured the INSTANCE and NOT the workdir; `2.0.0_SA_COO` closed the workdir half in one command off that sentence. |
| 92209 | **The baseline was invalid.** Runs on 08-29/08-30/08-31 ALL re-processed `asof=2026-08-28` (correct trading-calendar behaviour, NEVER#4 -- Friday IS Monday's answer). Today is the first NEW asof in four days, so the cause window is 08-28 -> 09-01, not today. Also: untruncated chain logs are SERVED at `s3://opal-data-49financial/gold/advi/_logs/`, removing the instance start COO was sequencing. Also: gold inputs at the failing asof are IDENTICAL to the last-good asof (16 tables, empty delta both directions). Also: my own concurrency hypothesis REFUTED by the isolated 12:45 run. |
| 92228 | **Located the discontinuity by S3 object VERSIONS**: `_code/perfrp_emit_core.py`, the one file all 11 emitters import, went 19,742 -> 114,406 bytes at 2026-09-01T00:10:20Z. Every `built=6` run used the 19.7KB core; the failing run used 118,465. The fabric had spent the afternoon on a 4,059-byte fix sitting on a 94,664-byte rewrite nobody had named. |
| 92256 | Dependency delta introduced by the rewrite: `+pandas +lib +subprocess +datetime +perfrp_book`; 397 -> 2,116 lines, 11 -> 34 defs. Led with a correction: the VersionIds I published at 92228 were TRUNCATED by my own `awk substr($4,1,16)` display and fail with `InvalidArgument`. Full ids supplied; the two 19,742-B versions confirmed md5-identical. |
| 92269 | **Refuted `0.4.0_DE_ClientPlatform~D`'s counter-indication at source**, on bytes verified `md5 == deployed ETag`: `d_publisher_port.py:415-417` maps ANY non-zero exit to `emitter_refused` -- there is no `error`/HARD_FAIL branch on rc, so an ImportError yields refusal rows and no chain abort. **Same read explained the bare dashes**: `:396 emitter_tail` reads STDOUT, a traceback goes to STDERR, and `:417` captures stderr into `error`. The reasons were never missing; the wrong FIELD was being read. Carried a falsifiable pre-registration naming the condition that would kill my own candidate. |
| 92280 | EC2/EBS sequencing hazard: runner is EPHEMERAL (boots ~12:45:16Z, chain 12:45:42-12:48:36Z, self-halts). Today's 07:00:15Z snapshot PREDATES the 12:45 run, so the only copy of the decisive manifest is on live volume `vol-0a29e29786d44bc37`; a boot-time `/tmp` clean (or `/tmp` being tmpfs) destroys it, meaning STARTING the host to recover it may be the act that loses it. Proposed snapshot-before-start. Implemented nothing. |
| 92290 | **KILLED MY OWN CANDIDATE.** `a00`/`a01`/`a02`/`a03` and `chain_49f_entrypoint` ALL import pandas and ALL ran `STAGE OK` in the same run that refused 11 of 11 -- pandas IS importable on that box. And emitters spawn under `sys.executable` (`:359`), so there is no interpreter gap. Sent ahead of everything else because `1.0.0_SA_CTO` 92264 had adopted it. |
| 92300 | AMI is `ami-0c7217cdde317cfec` = Ubuntu 22.04 LTS, whose system python3 IS 3.10 -- INDEPENDENT corroboration of the cpython-310 read (distro release vs pycache filename, different instruments per Rule 22). Also: the failing core's entire direct pandas surface is `pd.concat` x2, which WEAKENS the library-skew axis. Also flagged a discriminator of mine that DOES NOT WORK and must not be re-run (`.append(` matches `list.append()`, `.map(` matches `Series.map()`). |
| 92303 | **Refuted a benign closure forming around my own finding.** `2.0.0_SA_COO` 92284 credited "no new data so it's just not populating anything." Measured: the failing partition holds 5,998,529 bytes vs 5,651,743 at the last-good asof -- 6 percent MORE, `flow_ledger` up 4.2x -- and 14 other stages BUILT and EMITTED from it. "No new data" is TRUE of 08-29/30/31 and FALSE of today. |
| 92333 / 92347 | Corrected item #6 of COO's re-usable absence census: the reason is in `error` (stderr), NOT `emitter_tail` (stdout, structurally empty for this mode). As written it would have manufactured instance EIGHT out of the catalogue of the first seven. COO accepted and found a second instance of the same wrong field in its own 91793. I then added the clause the corrected pointer still needed: I measured that stderr is CAPTURED into `error`, not that a reason IS there. |

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-iam` | `--help`, `refresh-census --help` | PASS | Verified the `refresh-census` verb and its `--out` default exist BEFORE recommending them in a memory entry, per the "verify a flag before recommending it" rule. Also surfaced the sibling `census-self-test`. |
| native `Read` | `d_publisher_port.py:386-427` | PASS | Rule 21 permits native Read ungated. Preceded by a GRAIN control (worktree md5 vs deployed ETag) so the read was of RUNNING bytes, not a repo copy. |
| `.tools/aws` (operational) | s3api / ec2 / ssm, ~20 reads | PASS | Operational AWS is not comp-rail-gated. Denominators printed on every census; `s3api` used throughout for UTC (never `aws s3 ls`, per Rule 22a). |

**What worked:** `s3api list-object-versions` was the decisive instrument of the entire window and no
other tool in the estate would have produced it. `2.0.0_SA_COO` 92232 named it as the answer to its
own open question at 92111 s.4 -- "what is the ORACLE for RUNNING BYTES, as distinct from deployed
bytes?" A `head-object` only ever shows NOW; versions resolved against run timestamps answer "which
bytes were live when this run fired."

**What failed:** two of my own instrument errors, both caught before they changed a decision but ONE
after it was published. (a) `awk substr($4,1,16)` silently produced valid-LOOKING VersionIds that I
published at 92228 -- a version id has no natural length a reader can check, same family as the
`head` class. (b) A pandas 1.x-vs-2.x discriminator whose markers were false-positive by construction.

**Gap found:** **there is no comp-tool surface for S3 object VERSIONS.** `comp-find --corpus aws`
covers the live AWS plane as a NAME/ARN/props regex over CloudNodes; it has no notion of an object's
version history, which is precisely the axis that located this regression. Raising as an observation
only -- NOT proposing a build (Rule 27 scope, and a new surface is not mine to commission).

## Deployment Sequence + Verification (AE role-specific)

**NO DEPLOYMENT. Nothing was applied, started, snapshotted, terminated or rolled back this window.**
Stated affirmatively because the AE role minimum expects this section and an empty one reads as an
omission rather than a fact. The verification reads performed instead:

```
  GRAIN control on the source read:
    repo worktree md5   944a936ef33f726f39200f781fd5e54a
    deployed ETag       "944a936ef33f726f39200f781fd5e54a"  _code/d_publisher_port.py
    deployed mtime      2026-08-25T07:17:37Z, 32,294 B -- unchanged across the incident
    -> IDENTICAL: the file read IS the file the runner loads.

  Instance state (the gate on every remaining read):
    i-01003b035d2988dfb   state=stopped   r6i.4xlarge   LaunchTime 2026-09-01T12:45:16Z
    ssm describe-instance-information -> EMPTY list (agent unreachable, not a timeout)
```

## Blockers

**BLOCKED, evidence-cited** -- the two reads that would settle the open mechanism:
1. The runner's INSTALLED PACKAGE VERSIONS. Evidence: instance `stopped`, SSM agent list empty (above).
2. The run manifest's `error` field (`/tmp/49f_chain_work/perfrp_projection/out/manifest_2026-08-31_064462fd61e7.json`). Evidence: same, plus it is local-only per `1.0.0_SA_CTO` 92130.
Both are gated on `2.0.0_SA_COO` sequencing an instance start, with the 92280 snapshot-before-start
caution attached. NOT assumption-blocked: I measured the instance state rather than inheriting it.

**OUT OF LANE (not blocked):** the diff of the two `perfrp_emit_core.py` versions is emitter-lane.
`0.4.0_DS_ClientPlatform~G` is dark and `2.0.0_SA_COO` 92284 s.3 decided NOT to respawn it, with a
stated re-take condition.

## Current State (zero-context handoff)

The 49F ADVI gold chain runs daily from EventBridge at 12:45:42Z on EC2 `i-01003b035d2988dfb`
(ephemeral: boots, runs, self-halts via the `StartedByDispatcher` gate in SSM document
`advi-49f-chain-dispatch`). That document does `aws s3 sync s3://opal-data-49financial/_code/
/tmp/advi_49f_code/ --delete` then `python3 chain_49f_entrypoint.py --production`. **It installs
nothing** -- the deploy path ships CODE ONLY, and there is no dependency manifest anywhere in
`_code/` (0 of 83 objects).

The chain's `perfrp_projection` stage built 6 of 11 families every day from 2026-08-27 through
2026-08-31, and 0 of 11 on 2026-09-01. The five families that refused throughout are a stable
DECLARED round-1 state, not part of the regression; the SIX that flipped are activity_relationship,
activity_account, performance_relationship, performance_account, allocation_relationship,
allocation_account.

**The one change in the cause window to the file all eleven emitters import:**
`s3://opal-data-49financial/_code/perfrp_emit_core.py`
```
  2026-08-25T07:17:50Z   19,742 B  VersionId 2xvlnmbBVvdME9XB8Wt5zyPsXCMDDfzF  <- every good run
  2026-09-01T00:10:20Z  114,406 B  VersionId D2ffWfCU88mSmEN3Pb9j1rSVCzE0JN6T  <- the rewrite
  2026-09-01T09:15:31Z  118,465 B  VersionId bkKaLySq0wKv3Bav50Tp25.MAoQQ_8yM  <- live at the failure
```
Mechanism UNKNOWN. Refuted this window: concurrency, missing inputs, a pre-08-27 baseline, the
absent-dependency story, and the "no new data" story. What survives is that the cause is inside the
~94KB of new LOGIC, not in what that logic imports or in the data it reads.

Untruncated per-day chain logs are readable at `s3://opal-data-49financial/gold/advi/_logs/chain_<YYYYMMDD>T124542Z.log`
without touching the host. The refusal REASONS are not in them -- `emitter_tail` renders a bare dash
because it reads stdout while a traceback goes to stderr.

## Next Steps

- [`0.4.0_DS_ClientPlatform~G`, when re-seated] Diff VersionId `2xvlnmbBVvdME9XB8Wt5zyPsXCMDDfzF` against `bkKaLySq0wKv3Bav50Tp25.MAoQQ_8yM` for what in the new logic refuses at a NEW asof. Emitter lane; not mine.
- [`2.0.0_SA_COO`] Sequences any instance start. If the manifest is wanted, snapshot `vol-0a29e29786d44bc37` FIRST (92280); read the `error` field and `emitter_rc`, NOT `emitter_tail` (92269, 92347).
- [`0.0.0_AB_MSTR`] Owns the comp-iam APPLIED census: 24h TTL, nothing refreshes it on a schedule, measured 664h stale today. Surfaced only -- the standing monitor moratorium forbids building a refresher.
- [this seat] Nothing owed. Holding, event-driven on Monitor-delivered mail.

## Memory (outside the repo, not in this commit)

Three files under `C:\Users\AndrewBerman\.claude\projects\C--Users-AndrewBerman-Desktop-ajb-workspace\memory\`:
one NEW (`feedback_a_rerun_of_an_already_built_date_is_a_green_that_is_not_a_test.md`), two UPDATED
rather than duplicated (the comp-iam census entry, which already existed since 06-26 and was
unindexed -- I nearly wrote it twice, which is itself the recall-failure tell; and the caveat entry,
extended with the split-carrier variant). Two index lines added to `MEMORY.md`.

## Self-assessment

Five candidates raised from this seat this window; five refuted, four by controls I built to kill
them. `1.0.0_SA_CTO` 92293 s.4 recorded that pattern. The version timeline is the only thing I said
today that has not been falsified, and it is a timeline, not a cause.
