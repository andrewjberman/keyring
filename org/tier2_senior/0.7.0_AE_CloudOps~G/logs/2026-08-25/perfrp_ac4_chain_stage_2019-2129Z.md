# ADVI_PERFRP TO-R1-AE — AC4: the projection stage built, and the chain-abort defect I shipped into it

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Serial:** `0.7.0_AE_CloudOps~G` · **Window:** 2026-08-25T2019Z -> 2129Z · **Project:** ADVI_PERFRP (only)
**TO:** `org/tier2_senior/0.7.0_AE_CloudOps~G/task_orders/ADVI_PERFRP.TO-R1-AE.publisher-keys-route-chain-stage-iam.md`

---

## Current State

**Seat.** Fresh session. Registered LIVE (PID 26224) as the full lane serial. Inbox Monitor armed,
task `bos4cij9e`, confirmed `running` via `TaskOutput` — the only probe that observes a consumer.
No orphan watcher existed for this serial at startup, so no kill was needed and none was made.

**START CONDITION: MET.** `0.4.0_DS_ClientPlatform~G` `9af61d7e2e` produced the first local emission
and registered 11 PERFRP families. Publisher registry now carries **23 emitter entries** against
`perfrp_emitters.PUBLISHER_PRESTATE` of 12. Discharged by READING the registry, not by report.

**Four commits, ALL LOCAL ONLY on CLOUD** (verified with `git merge-base --is-ancestor` against
`origin/CLOUD`, not asserted). HEAD is 31 commits ahead of `origin/CLOUD`; none of this is visible
to a freshly-pulling seat until the integrator pushes.

| commit | what |
|---|---|
| `a07fa4f35e` | AC4 projection stage added to `chain_49f_entrypoint.py` — **carried the defect below** |
| `7d1558ed3f` | proof instance `git mv`'d from the BASE path to the lane path the TO names |
| `b9915d8271` | the fix: refusal-vs-failure classification off the run manifest + 5-arm control set |
| `d8a7f34b35` | instance AC4 updated with the defect, the fix, and the control set |

**The stage.** `_run_perfrp_projection()` in
`data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py`, called AFTER the c04 validation
battery block, gated on the same `upload` condition. Invokes
`d_publisher_port.py --asof <date> --staging-root <workdir>/perfrp_projection --keys <11 families>`,
build-only. The family list is DERIVED from `perfrp_emitters.PERFRP_EMITTER_FAMILIES`, never
hand-typed — the publisher's default `--keys` is EVERY EMIT key and would have dragged the 12 legacy
ADVI families into a stage that is not about them.

**Not live.** Deployed `s3://opal-data-49financial/_code/chain_49f_entrypoint.py` is
`sha256(LF)=070765998b787e34`, 25508 B, LM 2026-08-25T03:17:36Z. Local HEAD is
`sha256(LF)=fbe33be7bb91391f`, 28948 B. **DRIFT — the stage is not deployed.** Per Rule 13 that
`aws s3 cp` leg is the DS lane's cycle and the key EXISTS in `_code/`, so it updates on the
integrator's push under `safe-deploy`'s key-exists guard. **NEVER#6 does not attach: no deploy has
BEGUN at this seat.**

**Criterion state.** AC1 UNCOMPUTABLE (grain blocker CLOSED; residual is the sovereign DATA half and
D5 needing a live publish) · AC2 PASS · AC3 UNCOMPUTABLE (two independent sovereign holds) ·
AC4 UNCOMPUTABLE-in-schema / PARTIAL-in-fact (DESIRED + EXERCISED done, APPLIED rides the push) ·
AC5 PASS · AC6 proof instance VALID rc=0.

---

## The defect I shipped, and why my own green test did not catch it

`d_publisher_port.py:622-629` folds `emitter_refused` into the SAME `bad` bucket as
`error` / `no_payload` / `twin_diverged` / `verify_absent`, and returns 1 for any of them. **Five of
the eleven round-1 PERFRP families refuse BY DESIGN** — gainloss rel+acct, transactions (PAGED,
s.11 #6), roster, book_advisor — all read planes outside the gold plane that round 1 does not wire.

My stage did `rc != 0 -> CHAIN ABORT`. Measured live: publisher rc=1, census
`{would_publish: 6, emitter_refused: 5}` -> `CHAIN ABORT stage=perfrp_projection rc=1`. **On the
12:45Z fire that aborts the entire 49F gold chain, daily, on the completely expected state** — and it
would have presented as the projection stage failing rather than as a classification error, so the
diagnosis would have started in the wrong place.

**Why exercise (1) missed it — the transferable half.** My two-armed placement test replaced
`_run_perfrp_projection` with a SPY. It proved the CALL SITE is fail-closed; that was true then and
is still true now. But **a spy cannot fail the way the real callee fails** — the helper body had
never executed once. PLACEMENT and BEHAVIOUR are two different claims, and one test answered only
the first while reading as though it had answered both. **The spy version passes in exactly the state
where the real one fails.** I had already reported AC4 as exercised on that basis (71453/71454); the
only reason this is a correction rather than an incident is that I went back and ran the helper for
real instead of trusting my own green test.

**The fix, scoped to the stage and NOT to the publisher** (whose rc contract has other callers):
classify off the per-key `status` rows in the run manifest the publisher already writes. HARD_FAIL
aborts; `emitter_refused` is tolerated but printed with COUNT and KEY NAMES, so a family that quietly
stops emitting cannot read like one always expected to refuse. Absent / unreadable / zero-row
manifest -> ABORT rc=2, because an absent oracle is evidence of no evidence.

---

## Verification (ACTUAL output)

**Placement exercise — two arms, differing in exactly ONE input (c04's rc):**
```
ARM A  c04 rc=1 -> CHAIN ABORT stage=c04_validation, projection_invocations=0, chain rc=1  PASS
ARM B  c04 rc=0 -> STAGE OK c04_validation,          projection_invocations=1, chain rc=0  PASS
AC4 FAIL-CLOSED EXERCISE: PASS
```
ARM B is load-bearing: without it, ARM A's silence is equally consistent with the call site being
ABSENT altogether — a one-armed test here passes vacuously.

**Classifier control set — publisher rc HELD CONSTANT AT 1 in every arm, so the verdict is provably
the manifest's and not the return code's:**
```
  A tolerated: would_publish + emitter_refused    rc=0  expect=0        PASS
  B HARD: an `error` row                          rc=1  expect=non-zero PASS
  C HARD: a `twin_diverged` row                   rc=1  expect=non-zero PASS
  D no-oracle: manifest ABSENT                    rc=2  expect=non-zero PASS
  E no-oracle: manifest with ZERO rows            rc=2  expect=non-zero PASS
CLASSIFIER CONTROL SET: PASS (5/5)
```
B and C are what make the tolerance safe — without them the fix is indistinguishable from fail-open.

**Live helper re-exercise, build-only, zero S3 writes:**
```
STAGE OK perfrp_projection rc=0 wall=42.2s families=11 attempted=11 built=6 refused=5 hard_fail=0
(publisher rc=1; refusals are a DECLARED round-1 state, not a failure)
refused_keys=['perfrp_gainloss_relationship', 'perfrp_gainloss_account',
              'perfrp_transactions_relationship', 'perfrp_roster_relationship', 'perfrp_book_advisor']
```

**AC1 grain oracle — re-derived at the ARTIFACT** (DS~G fixed it at source in `5ec0ab865f`; I did not
re-derive their method, only their claim about the artifact). Source files verified CLEAN vs HEAD
`fffc9ef70a` before the run:
```
perf_rel ids == perf_acct ids          FALSE   (TRUE was the defect)
perf_rel ids == activity_account ids   FALSE   (TRUE was the defect)
perf_rel ids == activity_rel ids       TRUE    (correct relationship grain)
perf_acct ids == activity_account ids  TRUE    (correct account grain)
grain: level=relationship n=4385 distinct / level=account n=7335 distinct
```
Publisher's OWN derived denominator, located BY THE STRING IT PRINTS (never by line number — the
print has moved five times, 504->545->570->607->627):
`11 twin(s) attempted of 26 EMIT twins (23 emitter entries); 5 not clean`. BEFORE 12/15/10 -> AFTER 23/26.

**AC1 is still not PASS, and now for Andrew's reason rather than a defect:** `figure_state_census` is
`{NOT_COMPUTED_INPUTS_ABSENT: 4385}` and `{NOT_COMPUTED_INPUTS_ABSENT: 7335}` — performance computes
nothing at this asof. That IS the `twr_daily` BMV gap, his "let's just get the data part sorted",
visible in the artifact.

**Zero new triggers, BOTH planes, materialised client-side (never `--query length` on page 1):**
```
events rules DENOMINATOR = 137   matching 'perfrp' = 0
schedules  DENOMINATOR   = 18    matching 'perfrp' = 0
advi-49f-gold-floor  ENABLED     advi-49f-publisher  DISABLED (the P4I-3 activation act, not this stage)
```

**Proof-of-spec, positional, at the TO's stated instance_path:** VALID rc=0, violations=0.
alignment forward-1 6/6, forward-2 5/5, backward 5/5.

---

## Deployment Sequence

**None begun.** No Terraform, no `safe-apply`, no `safe-ec2-deploy`, no S3 code push, no tag, no
deploy-completion ledger entry. The only writes this window were four `safe-commit.sh` commits, all
LOCAL. Nothing was published: every publisher invocation ran without `--publish` and without
`OPAL_ADVI_PUBLISH_GRANT`, so `publish_one` returns `would_publish` and cannot touch S3.

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | `comp-which "how do I grep the repo"` (XXX.md A.3 exercise half) | PASS — a forwarder RAN (own banner), not merely resolved. PATH census 104 of 104 bare. |
| `comp-trigger` | `comp-trigger advi-49f-gold-floor` | PASS — `[scheduler] ENABLED`, denominator 137 events-rules + 18 schedules printed. Correctly labels itself declared-ness only and printed `schedule: -`, so the cron value came from the live plane. |
| `commit-gate.sh` | on `chain_49f_entrypoint.py`, twice (build + fix) | PASS both — py_compile + ds-precommit + ruff clean. |
| `proof-of-spec-check.py` | positional, 6 criteria, at the lane instance_path | PASS — VALID rc=0 after two corrections (see gap below). |
| `safe-commit.sh` | 4 commits under this lane's author line | PASS — msg-verify MATCH on each; risk-reflex HOLD read, not ignored. |

**What worked.** `comp-trigger` printing its denominator unprompted made the zero-new-rules claim
cheap. The `safe-commit` risk-reflex HOLD pointed me at the change-management record that told me the
chain runs from `_code/` via `s3 sync` — which is what made me check code currency instead of
assuming the commit was the deploy.

**What failed.** `proof-of-spec-check` rejected my AC4 status string. I had picked it by grepping the
checker's INLINE assertions and concluding the vocabulary was free-form; a jsonschema enforces an
enum. **I read one layer of an instrument and generalised to the whole of it.** The checker caught it
— the control working — and the substance never moved, only the label.

**Gap found (routed, not chased).** `d_publisher_port.py:622-629` merges a DECLARED `emitter_refused`
with a HARD error in one `bad` bucket, so **no caller can separate them from the return code alone.**
I worked around it locally in my own stage and deliberately did NOT change that contract. Surfaced to
`3.0.0_SA_CVO` as an OBSERVATION.

---

## MCP traffic

7 messages total. Significant: `2.0.0_SA_COO` 71354 GO (dispatch, ACKed) · `0.0.0_AB_MSTR` 70722/70725
(directive-tagging thread + Andrew's STAND DOWN — absorbed, no reply, as instructed) · `3.0.0_SA_CVO`
71372 (CLAUDE.md deletions DISARMED — Andrew is slimming the file himself) · my 71361/71362
(the CLAUDE.md OBSERVATION, correctly routed and now closed) · my 71453/71454 (TO-R1-AE return) ·
my 71487/71488 (the AC4 correction). All inbound acked via `ack_messages`.

---

## Blockers

**NONE held by this seat, and nothing is owed to it.**

The three criteria that are not PASS are held by SOVEREIGN conditions, not by any agent:
- **AC1 / AC3** — Andrew's ~08:5xZ DATA half (*"I'm fine with it on PROD, let's just get the data part
  sorted"*). He released the BRANCH half and explicitly did not release the DATA half. AC3 is
  additionally held by Andrew-direct 2026-08-21T19:18Z on the 49F flip. Not this seat's to move.
- **AC4 APPLIED** — rides the integrator's push, then the first scheduled fire. Not a blocker: it is
  a cell owned at an act that is not mine.

I am **not** idling on a CVO cert. `3.0.0_SA_CVO` 71372 was explicit that no seat is held by one.

---

## Next Steps

1. **[`2.0.0_SA_COO`]** Rule whether the AC4 deploy should be DRIVEN rather than left to ride
   integration — and if so, whether it is mine or the DS lane's under Rule 13. I did not assume it
   was mine. Asked in 71453.
2. **[`2.0.0_SA_COO`]** Confirm or redirect my reading of PRF-c-3's projection ENTRYPOINT: I proceeded
   on (a) invoke `d_publisher_port.py` build-only, rather than (b) waiting on a DS projection runner.
   Not untenable, so I did not hold — but it is five lines and cheap to redirect.
3. **[whoever watches the first scheduled fire after the push]** The healthy line is
   `STAGE OK perfrp_projection ... built=6 refused=5 hard_fail=0 (publisher rc=1 ...)`.
   **A publisher rc of 1 IS the expected round-1 state.** Read the stage's own verdict, never the
   child rc. This is written into the instance's AC4 `status_reason` so it does not live only in a
   message that scrolls.
4. **[UNOWNED — surfaced, not chased]** `audit-archive-invoker` reports baseline
   `2026-08-20T042433Z` is **136.0h old** with an uncaptured tail, and an UNCOVERED-AUDIT-LOG finding
   on `org/to-pos-override-audit.log`. A non-exec lane defers the snapshot by design; an EXEC startup
   is required to archive. Owner of the invoker is this lane's BASE serial.
