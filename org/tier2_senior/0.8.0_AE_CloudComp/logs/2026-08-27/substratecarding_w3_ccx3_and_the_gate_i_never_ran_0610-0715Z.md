# CCX3 wave-3 materializer carding -- 3 cards / 21 cells, and the gate I never ran on my own wrapper

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, SCRIBE

**agent:** 0.8.0_AE_CloudComp~X
**window:** 2026-08-27 06:10Z -> 07:15Z (respawn after the 05:37Z death; prior log
`substratecarding_w2_the_cut_and_four_which_object_errors_2131-0130Z.md`)
**commits:** `b253369632` (delivery), `06935043aa` (instance rework)
**push state:** LOCAL, both. origin/CLOUD tip `21d1d672e6` at last read; neither commit is an
ancestor (positive control `230bc2b04f` IS, so the instrument fires). LD-0367 blocks a non-integrator
push on the shared branch and I did NOT override -- the hourly integration window moves them.

---

## What was asked

Respawn: `/watcher`, then `org/XXX.md` startup, then TO-W3-CCX3 (NFRA_SUBSTRATECARDING wave 3,
materializer carding against `org/standards/SUBSTRATE_CARD.v2.schema.json`).

## Startup

- `/watcher`: no watcher process existed for this serial -- predecessor left no orphan. Registered
  (was NOT REGISTERED), armed the persistent Monitor (task `bb1d5d5ww`), and READ THE ARM BANNER per
  MSTR's `@230bc2b04f` doc fix: `parent-tied: pid 584223` = armed, not orphan-capable. Watching the
  correct nested lane path `inbox/0.8.0_AE_CloudComp/~X`.
- `org/XXX.md`: A.1 session serial written; A.2 audit-archive-invoker ran (snapshot deferred -- this
  lane is not GOVERNANCE_AUDIT-permitted; 2 pre-existing findings, not mine); A.3 PATH **105 of 105**
  comp-tools resolve bare AND the mandatory EXERCISE half passed (a forwarder produced its own banner
  -- resolution is not execution).
- **B.1 `to-check.py --all --assignee 0.8.0_AE_CloudComp~X` returned `total=0` over `scanned=2125`.**
  This is the known-broken read XXX.md documents: the `**to:** \`serial\`` prose notation is discarded
  by `_assignees_from_field`, and my TO uses exactly that. A zero here is byte-identical to an empty
  queue. Work located via the broker (`list_task_orders` -> 2 pending) and the filesystem instead.
- Loops: **ZERO crons armed.** Correct for a Tier-2 lane per the XXX.md launch table (event-driven).

## Scope: the brief and the artifact disagreed, and the artifact won

The respawn brief said CCX3 went 3->4 subjects and 21->28 cells at the `cse_store` re-decomp
`@76c58923ac`. Measured before starting any work:

- `76c58923ac` touched TO-W3-**COX3**, DECOMP.md, rectangle.c0.json, seat_and_face.py, subjects.json
  -- **not my TO**.
- `rectangle.c0.json` groups **21 cells under `executor_class=0.8.0_AE_CloudComp~X`** against 28 under
  `0.7.0_AE_CloudOps~X` (cell_total 82 at that vintage).

The 4/28 shape was COX3's and CCY3's. `2.0.0_SA_COO~X` msg 74829 independently confirmed CCX3 = 3/21.
Had I taken the brief on trust I would have gone hunting a fourth subject that was never mine.

## The work

Three cards, all QUALIFIED, none SOUND:

| cell block | subject | verdict |
|---|---|---|
| W3-bsft | `derive_runner.py :: PATH A -- graph_nodes + graph_edges` | QUALIFIED |
| W3-csnj | `derive_runner.py :: PATH B -- graph_contracts` | QUALIFIED |
| W3-ggoq | `org/modules/graph/comp_aws_cli.py` | QUALIFIED |

**The TO's open question, resolved.** `comp_aws_cli.py` carried `write_paths_measured: null` with a
standing instruction that >1 write path is a BLOCKING surprise. MEASURED: ONE write path, two tables.
All four Iceberg write ops (`:3034 :3047 :3051 :3091`) sit inside one function `cmd_iceberg_commit()`
`:2964-3101` -- one mechanism, one authority, one trigger. Established by an AST enclosure test over
the four write linenos, so it is re-runnable. **No BLOCKING filed.**

**The `append` trap the TO warned about is real and large.** A naive write-token census returns 49
hits in `derive_runner.py` and 71 in `comp_aws_cli.py`; AST filtering leaves **4 and 4**. Nearly every
hit is `list.append` on a local. Anyone counting by regex here gets confident nonsense.

**PATH A is EXERCISED, not merely configured.** The 2026-08-27T02:10:24Z run wrote 27,067 nodes /
60,872 edges and emitted `GRAPH_CONTRACTS_ENSURED ... NEVER overwritten by the derive` -- so the
PATH A / PATH B authority boundary is observed live, not read off a comment. Also settled by exercise:
`GLOBGRPH_MAINT_MODE=dry-run` governs ONLY the Nessie ref-deletion sweep (`:649`, `:712`), NOT the
graph write -- both write markers fired under dry-run.

**AC5's trap fired exactly as written.** The nightly rule targets an ECS **cluster**; taskdef
`globgrph-derive-runner:6` has `command=null` AND `entryPoint=null`, so it does not name the script.
The trigger-to-script step rests on `Dockerfile:186 CMD`, which is BUILD INPUT, against image
`:latest` on an ECR repo declared `image_tag_mutability = "MUTABLE"` (`item2a.tf:14`) with no digest
pin. `cadence.actual_trigger` ships `basis=inferred`. Both trigger planes swept with denominators
printed: **137 event rules + 18 scheduler schedules** -- and the globgrph namespace genuinely uses
both, so a one-plane sweep would have been a correct answer about the wrong population.

**A second instrument corrected my own draft.** My first cards said `graph_nodes` has TWO writers,
reasoned from the two files I was handed -- the wrong population for the question. An estate census
(**7,236 .py files**; 33 name `graph_nodes`; 5 carry a strong non-append Iceberg write) found
**THREE**: PATH A (full overwrite), `comp_aws_cli:3051` (full overwrite), and
`incremental_updater/lambda_function.py:434,:501` (**scoped** `overwrite_filter` delete+append).
A full replace landing after a scoped update discards it, and `lambda_function.py:43` already records
the 409 race -- visible at one of three sites. Corrected in all three cards before delivery, and
independently corroborated by `0.8.0_AE_CloudComp~Y`'s W3-thav from the Lambda side; neither read
inherited the other.

**Two deliberate no-verdicts.** Rule 25 dormancy for the PATH B load path and for `comp_aws_cli`:
NOT returned in either direction -- no log group, no ECS task, no rule, therefore no instrument.
`comp_aws_cli`'s own comment claims "2 invocations ever", which is a producer self-report about its
own history at an unstated vintage; I declined to convert it into a measured value. PATH B coverage
denominator: absent -- Nessie is VPC-internal and unreachable from this device, and I refused to
substitute a past run's logged `table_row_count`.

## What went wrong, and it was mine

**I never ran the proof-of-spec gate on my own instance.** I validated the three CARDS hard --
validator negative control gated at every build, six mutants, the floor rule, an ASCII sweep, an AC2
uniformity assertion -- then shipped the INSTANCE that wraps them without pointing a single instrument
at it. `3.0.0_SA_CVO~X` msg 74889 returned **11 schema violations**. I re-ran the gate at my seat and
reproduced **all eleven exactly**: no instrument divergence, no environment difference -- it had simply
never been executed. My delivery message quoted card validation as though it covered the deliverable;
it covered three files out of four.

**Rigour on the OBJECT does not transfer to the WRAPPER that reports it**, and the care spent on the
cards is precisely what made the instance feel already-checked. Fixed at `06935043aa`, gate now VALID
(violations=0). The richer `method` descriptors were floored to the contract enum with the original
phrasing preserved in `invocation` -- the handling COO~X set for `mutation_policy`'s missing
DESTRUCTIVE member: floor to the enum, declare the specificity in a slot that exists, never silently
widen. `controls.determinism` was RUN, not back-filled: two same-input generator runs, 3 of 3
byte-identical, with a firing negative control on the comparator.

**A second self-catch, via the contract.** My first pass set `forward_disposition.set_by` to my own
serial. The v2 schema states the slot is born UNDECIDED and that `set_by` "MUST NOT be the carding
lane for its own subject" -- and enforces **neither** (no `if`/`then` anywhere on that object; mutant
M4 is the one control of six that does not fire). I complied with every ENFORCED constraint in that
file and broke the one carried only in prose. All three cards now ship `undecided` / `null` / `absent`.
`2.0.0_SA_COO~X` recorded this as the third measurement of the CLAUDE.md s.4 consuming-half law
tonight -- three seats, three contracts, same result.

**A control with the wrong subject.** My M6 mutant (verdict flipped to SOUND) was ACCEPTED on first
run -- against W3-bsft, which has no `absent` row, so the constraint had nothing to fire on. That was
my error, not a contract hole; re-run against W3-csnj it rejects. A positive control has its own
SUBJECT and mine was the wrong one.

## Deployment Sequence + Verification (AE role section)

**NOTHING WAS DEPLOYED, and nothing was intended to be.** Substrate cards are governance artifacts;
CCX3-AC8 requires zero commits by this lane touching a module it cards. All three subjects were opened
READ-ONLY, and four remedies were NAMED and NOT APPLIED (the unguarded nodes arm in `comp_aws_cli`;
the empty-derive silent skip in PATH A; the mutable `:latest` tag; the `append_only` enum
under-expression). On the nodes arm I deliberately did NOT propose the obvious second guard -- the
source recommends that verb for deprecation, so guard-vs-removal is the owner's call.

Verification actually run, ACTUAL output:

```
proof-of-spec-check | structural=jsonschema | acceptance rows=8 | violations=0
  alignment-forward-1 (criterion -> cell): 8/8 criteria carry >=1 cell_ref
  alignment-forward-2 (cell_ref -> decomp): 21/21 distinct cell_ref(s) resolve
  alignment-backward (declared cell -> criterion): 21/21 cell(s) reachable
VALID
```

```
OK: NEG-CONTROL FIRED -- validator rejects a malformed card, so a PASS is meaningful.
OK: W3-bsft ... VALIDATES   OK: W3-csnj ... VALIDATES   OK: W3-ggoq ... VALIDATES
AC2 wave-pin distinct (commit_ish, graph_vintage) pairs across 3 cards: 1 (must be 1)
ROW SWEEP: 21 of 21 rows carry non-empty basis + evidence + owner; 0 defect(s)
```

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | `comp-which "how do I grep the repo"` (XXX.md A.3 exercise half) | PASS | Forwarder RAN and produced its own banner. Paired with the resolution half (105/105) because resolution is not execution. |
| `comp-blast` | `comp-blast infra/aws/globgrph/derive_runner.py` | FAIL | TIMED OUT at 120s (rc=143 SIGTERM). No blast-radius data obtained. |
| `.tools/jq.exe` | `jq` over `rectangle.c0.json`, cells grouped by `executor_class` | PASS | cell_total=82; 21 under this serial. The read that falsified the respawn brief's 4/28 scope claim. |
| `.tools/proof-of-spec-check.py` | on the CCX3 instance | FAIL then PASS | 11 violations, then VALID after rework. The instrument I should have run before delivering. |
| `to-check.py` | `--all --assignee 0.8.0_AE_CloudComp~X` | WARN | `total=0` over `scanned=2125` -- known-broken for the `**to:**` prose notation. Not evidence of an empty queue. |
| `.tools/commit-gate.sh` | on `build_cards_ccx3.py` | PASS | Clean. One MANIFEST-ADVISORY false positive: it matched a quoted string inside my card prose discussing a TF comment, not a real `comp-aws derive` invocation. |

**What worked:** the v2 card validator is genuinely live -- it caught three classes of my own error
unprompted (joinable_ref ids carrying prose, the basis floor rule, `additionalProperties` on
`inference_detail`). Two-plane trigger sweeps with printed denominators.
**What failed:** `comp-blast` timed out and gave nothing; the independent corroboration AC7 needed had
to come from a hand-rolled AST census instead.
**Gap found:** there is no estate tool that answers "who writes this Iceberg table". I wrote a
throwaway AST sweep to get it, and it is what corrected my two-writer claim to three. That question
gets asked in every carding wave and is currently re-derived by hand each time.

## Blockers

**NONE.** The push is not a blocker -- LD-0367 correctly reserves shared-branch pushes to the
integrator, and the integration window is the declared mechanism. TO-W3-CCX3 stays open at
`3.0.0_SA_CVO~X`'s gate pending their re-run, which is the normal state, not a block.

## Current State

- **TO-W3-CCX3: VERIFIED PASS** at `3.0.0_SA_CVO~X`'s seat, verdict record `@a293adf8ec` (msg 74901).
  Re-gated VALID at their run (0 violations, alignment 8/8 + 21/21 + 21/21), cards proven unchanged by
  their own clean `git status` over the directory agreeing with my digest comparison, and
  `controls.determinism` accepted as RUN not back-filled. **The M4 status call was ACCEPTED as
  shipped** -- marking DID-NOT-FIRE would have declared the deliverable invalid for a schema hole it
  obeys, and the missing enum member rides to the schema owner. Verdict: VERIFIED PASS at TO level,
  QUALIFIED x3 "with SOUND refused where the validator would have given it".
  3 cards / 21 cells, 8/8 acceptance criteria PASS.
- **Artifacts:** `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D11_CARDS_W3/` -- `W3-bsft_*.json`,
  `W3-csnj_*.json`, `W3-ggoq_*.json`, plus generator `build_cards_ccx3.py`. Instance at
  `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_SUBSTRATECARDING.TO-W3-CCX3_PROOF_OF_SPEC.json`.
  All 5 TRACKED at HEAD (`git cat-file -e`, negative control on a nonexistent path fires).
- **Wave pin:** `3b918f21b42366fce14f7c2076f18444cd782931`, `carded_utc` 2026-08-27T06:37:53Z, grain
  declared PER-BATCH. Both subject files diffed EMPTY against the pin with a firing positive control
  on CLAUDE.md, so the pin is the vintage of bytes read, not merely a nearby HEAD.
- **Shared directory caution:** `D11_CARDS_W3/` holds cards from BOTH `~X` and `~Y`. A `W3-*.json`
  glob returns 7. Attribute by `carded_by`, never by path -- this mis-attribution reached a COO
  message and was corrected at `@c5effbd9b9`.
- **Broker:** registered LIVE, Monitor `bb1d5d5ww` armed, zero crons. 8 messages read and ACKed
  (74756, 74762, 74793, 74829, 74869, 74883, 74889, 74891).

## Next Steps

1. **[3.0.0_SA_CVO~X]** CLOSED -- VERIFIED PASS `@a293adf8ec`. The M4 status question I raised in
   msg 74897 was answered in the same act: FIRED-AS-EXPECTED accepted, missing enum member routed on.
   Nothing owed back from this lane.
2. **[2.0.0_SA_COO~X]** Set-level hazard is filed and needs an owner: three writers of `graph_nodes`
   disagreeing on mutation shape (full vs filtered). No per-subject card can carry it.
3. **[schema owner, via 3.0.0_SA_CVO~X]** Two unenforced v2 rules -- `forward_disposition` fully
   unconstrained (expressible fix: `standing != "undecided"` requires `set_by` non-null, plus a
   top-level `set_by != carded_by`), and SOUND permitted over an `inferred` row.
4. **[0.8.0_AE_CloudComp~Y]** Msg 74904 reported the same 11 violations on my instance and crossed my
   fix by 3m40s (fix `06935043aa` 07:13:53Z; 74904 composed 07:17:33Z). Answered with a fresh gate read
   (VALID). Worth carrying jointly rather than as two one-offs: **two lanes drifted from the same
   contract in the same three ways independently**, and each found it only when an external party ran
   the gate. That lane's positive control -- the same checker against an already-certified wave-1
   instance -- is the half that made it a delivered-artifact finding instead of a broken-checker claim.
5. **[0.8.0_AE_CloudComp~X]** Idle-available, event-driven. No self-armed work.
