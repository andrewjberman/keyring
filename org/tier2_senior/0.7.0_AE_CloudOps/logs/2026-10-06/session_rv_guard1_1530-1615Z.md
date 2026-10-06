# The stale-benchmark guard is live and graded — the deploy stopped on the CTO's own condition, and finished once he ruled — 0.7.0_AE_CloudOps~RV

**Date:** 2026-10-06
**Task Order:** OPAL_BBGTML.TO-GUARD-1.stale-benchmark-guard (@416573eac2, risk WORLD)
**Status:** COMPLETE

---

## Objective

**archetype:** DEPLOY

Execute track 1 of `1.0.0_SA_CTO~Z`'s index-benchmark fix route @5e0c045e8d: make
`yang-model-portfolio-benchmarks` refuse a benchmark series whose last bar predates `data_as_of`,
rather than serving a number compounded only through the stale frontier. Three legs under one
NEVER-2 entry, bounded by a signed never-widen pair (COO @1253afc83c, CTO @78a9e8a39e). Andrew-direct
singular priority for site Z (@f42219ebfe).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open --slug bbgtml-stale-benchmark-guard-20261006` (7 legs) | PASS | Printed the required commit pathspec for BOTH carriers unprompted, which is what stopped the sentinel being left behind. |
| deploy_ledger.py | `hold --gate-type sovereign ...` | PASS | REFUSED the hold because an apply/deploy-class leg was open: "a half-landed deploy cannot be HELD (stays RED)". The refusal was correct and I kept the entry RED. |
| deploy_ledger.py | `check` | PASS | Read my entry as `OPEN age=0.2h stranded=['G4','G5','G6','G7']`. |
| commit-gate.sh | on both code-leg files | PASS | Surfaced the 8 pre-existing non-ASCII lines as WARN; it does not distinguish pre-existing from added, so I printed the before/after character count myself. |
| surprise-row-gate | at commit, via safe-commit.sh | PASS | BLOCKED my first commit: `/surfaced_at '2026-10-06T16:1xZ' does not match` the strict ISO pattern. The fabric's fuzzy `16:1xZ` prose convention is NOT schema-legal. Fixed the state, no override. |
| naming-gate | at commit | PASS | `NAMING CONFORMANT ... opal-data-portal-v2 -> opal-data-portal-v2`, 1 graded. |
| build-and-upload.sh | `BUILD_ONLY=1 ... yang-pipeline yang-model-portfolio-benchmarks` | PASS | The BUILD_ONLY arm gave me the artifact sha before any upload, so the plan's expected hash was known in advance. |
| terraform show -json | on the saved plan | PASS | The only instrument that answered "which resources move"; the human-readable plan tail showed one resource and hid the second above the fold. |

**What worked:** `deploy_ledger.py hold` refusing a hold on an unfinished deploy — I had reached for a
state the mechanism correctly denies, and its refusal text named exactly why. `terraform show -json`
graded 69 resource_changes by address; `Plan: 2 to change` alone would not have told me WHICH two, and
the plan's tail rendered only mine.

**What failed:** nothing returned a wrong answer. Two advisories worth naming: `build-and-upload.sh`
prints `.tools/terraform.exe` in its next-steps block, which does not exist on this device (terraform
is on PATH at v1.15.8) — a copy-paste of its own instructions dies `rc=127`. And its bun fallback is
hardcoded to `/c/Users/AndrewBerman/.bun/bin/bun`, a device-specific path; node resolved first so it
never mattered here.

**Gap found:** no comp-tool answers "does this terraform plan move anything outside my blast radius".
That question is the whole of a never-widen condition 2 and it took a hand-written JSON walk. The
`comp-blast` family answers DECLARED edges, not a pending plan's diff.

---

## Work Completed

### 1. The code leg — a per-series recency guard (@513b25f522, 2 files, 305 insertions)

`lambda_function.py` gained `last_non_null_bar(series, end_date)` and, in the model loop, a per-series
staleness read applied inside the period loop:

- A series whose last non-null bar is BEFORE `end_date` returns `None` on every period — return,
  volatility, and both spreads fall with it (the spreads already required a non-null benchmark leg).
- `benchmark_last_date: {index, etf}` is added per model to the comprehensive output AND to the legacy
  output, which does carry per-model objects. A value carries its claim: a consumer can now distinguish
  a guarded null from a never-computed one.
- The nulling sits OUTSIDE `calculate_period_returns`, so the model path stays byte-identical. The
  daily timeseries is untouched.

**The defect, precisely:** `compound_returns` `dropna()`s a missing tail. So the four short periods
(1D/WTD/MTD/QTD) fell to null — the N/A the portal already shows — while the six long ones
(1M/1Q/YTD/1Y/Since Inception/TTW) served a WRONG number, unmarked, compounded through 2026-09-29
against a model through 2026-10-05.

### 2. AC1 — the plant test, with a two-arm negative control

`python -m pytest .../test_stale_benchmark_guard.py -q` -> **3 passed in 2.23s**, run before any deploy
act. The test drives the real `lambda_handler` over a synthetic data PKL with only the S3 boundary
patched, so the model loop, both output builds and the timeseries build are deployed code paths. Its
fixture mirrors the live asymmetry: 9 stale series at 2026-09-29, Intermediate Term ETF current at
2026-10-05.

| arm | bytes under test | result | what it proves |
|---|---|---|---|
| 1 | pre-patch HEAD | 3 failed, all `KeyError: 'benchmark_last_date'` | only that the FIELD is absent |
| 2 | field PRESENT, nulling REMOVED | failed on the guard: `UST 1D index_benchmark served nan`; `assert np.float64(2.95) is None` (INT YTD) | the guard itself is graded |

Arm 1 alone would have been a check conjoining its own precondition with what it measures. Arm 2 is the
discriminator, and it is the arm that proves a stale series serving 2.95 gets caught.

### 3. The artifact, verified by CONTENT not filename

Built sha `FLFjTpvIDptT+YqJGG9w3XaWN/Cwq4WJkNlmPd4p0tg=` vs base `dHTjheKzauUziiPc6Jkwn7Ys+C36Xb5KS0aAWPh7Th8=`.
Opened the zip and compared: packaged bytes 37,573 **identical** to the committed source;
`def last_non_null_bar` present; `ZZZ_NOT_PRESENT` negative control reads 0; the test file does NOT
ship. Uploaded with write VERIFIED (size 11,294, sha256 metadata match). The source map's recorded
`artifact_sha256` had equalled the live `CodeSha256` at the base, so artifact and deployed bytes agreed
before I touched anything.

### 4. The base, re-measured rather than re-cited

My own handoff flagged the 171 figure as citable only after a re-read, in case Yang's re-pull had
landed. It has not: the served comprehensive key is still VersionId `9NuMvtEAPll77jLbwgGKki5y7oVS9U8M`
at `data_as_of` 2026-10-05 — the signed base version itself. CTO condition 3 is on **BRANCH A**.

I re-partitioned the 300 cells by reading each series' frontier off the base artifact's OWN timeseries
key, so the 9-stale/1-current split is an output of the measurement, not a hardcoded mapping:

| bucket | re-measured | blast radius @162e733fff |
|---|---|---|
| stale-sourced, serving a number (the silent half) | 171 | 171 |
| stale-sourced, serving null (the visible N/A) | 99 | 99 |
| current-sourced, serving a number | 27 | 27 |
| current-sourced null (`min_points=5`) | 3 | 3 |
| **denominator** | **300** | 300 |

### 5. The deploy leg — STOPPED on CTO condition 2

The untargeted plan reads `0 to add, 2 to change, 0 to destroy`. Graded by `terraform show -json`:
69 `resource_changes`, 2 not no-op.

- **In radius:** `module.model_portfolio_benchmarks.aws_lambda_function.this`, exactly 3 attributes —
  `source_code_hash` dHTjheKz -> FLFjTpv, `s3_object_version` `Pzl.iT8...` -> `g0NaQztk...`,
  `last_modified` known-after-apply. The signed blast radius exactly.
- **Second resource:** `aws_sfn_state_machine.yang_pipeline`, `definition` only. The difference is line
  endings ALONE: 35,730 chars / 1,012 CR -> 34,718 chars / 0 CR; identical with CR stripped; identical
  as parsed JSON; a per-leaf walk compared **481 leaf values and found 0 differing**. The repo file
  carries LF and the deployed definition carries CRLF, so any apply of this root from any device
  normalizes it. This act did not produce it.

CTO section 4 condition 2 says any other resource is a STOP. **No apply ran.** Reading the condition as
satisfied because the delta measures zero would be this seat adjudicating the CTO's own condition wider
than its words.

### 6. The AC3 grader, committed and already exercised

`benchmark_guard_grade.py` classifies cells from the served artifact's own `benchmark_last_date`, so
staleness is measured rather than assumed; it handles BOTH branches of condition 3; and it refuses to
grade when the field is absent. Run against the current served output it correctly printed:
`BLOCKED: model UST carries no benchmark_last_date -- the guard is not deployed ... Refusing to grade
against a default.`

### 7. The ruling landed, and legs 2 and 3 finished

`1.0.0_SA_CTO~Z` chose route (a) in **ADDENDUM 1 @99f67b52e5** (msg 30142), which disarms Z-S6, and
`2.0.0_SA_COO~Z` GO'd leg 2 (msg 30144). The CTO re-measured the drift independently before ruling —
1012 CR live, 0 in source, `json.loads` equal — and added four conditions, all met:

| condition | evidence |
|---|---|
| (1) the plan moves exactly those 2 resources and attributes | re-planned; `terraform show -json`: 69 resource_changes, 2 not no-op; lambda -> exactly `{source_code_hash, s3_object_version, last_modified}`, SFN -> exactly `{definition}`. Both MATCH |
| (2) save `describe-state-machine` before the apply | saved: 35,730 chars, 1,012 CR, ACTIVE |
| (3) after the apply, 0 CR and parsed JSON equal to the saved one | 34,718 chars, **0 CR**; 481 leaf values compared, **0 differ**; roleArn unchanged; ACTIVE |
| (4) any third resource is still a STOP | none |

`safe-apply`: `comp-tagauthz` PASSED, `tombstone-gate` CLEAN, `0 added, 2 changed, 0 destroyed`.
0-diff re-plan: exitcode 0, `No changes.`

**AC2 PASS** — live `CodeSha256` `FLFjTpvIDptT+YqJGG9w3XaWN/Cwq4WJkNlmPd4p0tg=`, differing from base
and **equal to the artifact built from `513b25f522`**; `LastModified` 2026-08-04 -> 2026-10-06T16:14:11Z;
runtime and memory unchanged.

**Leg 3** — condition 3 re-read immediately before the invoke: served `data_as_of` 2026-10-05,
**BRANCH A**. ONE invoke on `benchmarks/data_20261005_v1.pkl`, payload 159 bytes, no `force_publish`.
200, no `FunctionError`, `model_count` 5, 3,175 timeseries rows, all three keys at 16:16:52Z.

**AC3 PASS**, exactly section 3:

| key | grade |
|---|---|
| comprehensive, 300 cells | 171 number->null, 99 null->null, 27 byte-equal, 3 null unchanged = **273 null / 27 numbers** |
| model cells | **100 of 100 equal** (denominator 100) |
| legacy, denominator 150 | number->null 95, null unchanged 55, number unchanged 0, **number CHANGED 0** |
| timeseries | rows **byte-identical**, 3,175 rows / 768,530 B both sides, only `generated_at` differs |

`benchmark_last_date`: index 2026-09-29 on all 5; etf 2026-09-29 on UST/ST/LT/ULT, 2026-10-05 on INT.
CTO section 2's watch: 13 legacy versions retained, **0 unpaired** — no dormant-exporter write.

NEVER-2 entry `bbgtml-stale-benchmark-guard-20261006`: all 7 legs proven, **CLOSED**, sentinel removed,
nothing stranded.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| STOP rather than apply, despite DELTA=0 | CLAUDE.md NEVER-1 says a verified DELTA=0 needs no hold, which argues for applying. But the condition is the CTO's and `org/XXX.md` says the receiving agent does not adjudicate scope. The cost of asking is minutes; the cost of widening a WORLD act unilaterally is the whole point of a never-widen pair. |
| Did not take the targeted-apply escape myself | It would keep the act inside the blast radius, but AC2 asks for an untargeted apply. Choosing between the two is the same adjudication, so it went in the ask as route (b). |
| Folded a 4th test into case 3 | I had written 4 tests; AC1's stated expectation is literally `3 passed`. A criterion's expectation is not mine to widen either — the timeseries assertion belongs inside case 3's "untouched" clause. |
| Committed the code leg on CLOUD in the shared tree, not a worktree | Rule 14b prefers a worktree for a >1-file commit while seats are live. Against it: the NEVER-2 entry must be readable by other seats DURING the deploy (a branch-resident entry is invisible), the Terraform build reads the tree it runs in, and a full worktree checkout OOMs on this device. No live seat writes these paths. Stated as a departure, not hidden. |
| Fixed `surfaced_at` rather than use the audited override | The override exists for a state that cannot be fixed. A fuzzy timestamp can be. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/.../yang-model-portfolio-benchmarks/lambda_function.py` | the guard: `last_non_null_bar`, per-series staleness, `benchmark_last_date` on both outputs | Yes — `513b25f522` |
| `infra/.../yang-model-portfolio-benchmarks/test_stale_benchmark_guard.py` | new; the 3-case plant test | Yes — `513b25f522` |
| `org/surprise_channel/OPAL_BBGTML/INVESTIGATION_v1.md` | row `OPAL_BBGTML-Z-S6`, BLOCKING/ARMED | Yes — `9ea9161ff4` |
| `org/critical_paths/.open_deploys/bbgtml-stale-benchmark-guard-20261006.json` | NEVER-2 sentinel, OPEN | Yes — `9ea9161ff4` |
| `org/critical_paths/change_management/20261006T1553Z_..._deploy_completion.md` | NEVER-2 entry, 7 legs | Yes — `9ea9161ff4` |
| `org/tier2_senior/0.7.0_AE_CloudOps~RV/deliverables/benchmark_guard_grade.py` | new; the AC3 grader | Yes — `9ea9161ff4` |
| `infra/aws/lambda/ci/lambda-source-map.json` | `artifact_sha256` -> FLFjTpv (written by the builder) | Yes — `9ea9161ff4` |
| `s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-model-portfolio-benchmarks.zip` | new version `g0NaQztkPzEyQXXiV2a4utvW1Er0V5dS` | n/a — S3, write verified |

**Push state, measured at `git ls-remote` (16:0xZ):** both commits are **LOCAL** — origin/CLOUD is
`e82f508eef`, local HEAD `9ea9161ff4`, and neither `513b25f522` nor `9ea9161ff4` is an ancestor of
origin/CLOUD. The CLOUD push is `0.0.0_AB_MSTR~Z`'s on Andrew's word.

---

## Blockers

**None.** The one blocker of this session — the ask to `1.0.0_SA_CTO~Z` on row `OPAL_BBGTML-Z-S6`
(msg 30139, `2.0.0_SA_COO~Z` copied at 30140) — was answered 7 minutes later with ADDENDUM 1
@99f67b52e5 choosing route (a), my recommendation. Leg 2 then ran under its four added conditions and
leg 3 followed on branch A. Nothing is owed by this seat and nothing waits on it.

The `<status>` flip on the order is the issuer's, not mine.

---

## Current State

The guard is **LIVE and graded**. `yang-model-portfolio-benchmarks` reads `CodeSha256
FLFjTpvIDptT+YqJGG9w3XaWN/Cwq4WJkNlmPd4p0tg=` (LastModified 2026-10-06T16:14:11Z, python3.12, 512 MB),
which equals the artifact built from code-leg commit `513b25f522` and differs from the base
`dHTjheKz...`; a 0-diff re-plan of `infra/aws/terraform/yang-pipeline` returns `No changes.` The three
served keys were rewritten by ONE no-`force_publish` invoke at 2026-10-06T16:16:52Z — comprehensive
`Qbef40yVOC1A7F31_vikeqMQSDK198.e` (19,610 B), legacy `g3QLGqWqXZEyIAC7yxgjrpy_TUluEr4D` (12,961 B),
timeseries `KfcDtAtDLdfXcrroQjAfopYl6UDJs0QI` (768,530 B) — and grade exactly as the CTO half's
section 3 predicted: **273 null / 27 byte-equal of 300 benchmark cells, 100/100 model cells equal,
legacy 0 numbers changed of 150, timeseries rows byte-identical.** The 171 numbers that were
compounded through 2026-09-29 against a model through 2026-10-05 now serve null with
`benchmark_last_date` beside them. NEVER-2 entry `bbgtml-stale-benchmark-guard-20261006` is CLOSED with
all 7 legs proven and its sentinel removed; row `OPAL_BBGTML-Z-S6` is disarmed by ADDENDUM 1
@99f67b52e5. Nothing is in flight and nothing is owed by this seat.

---

## Next Steps

1. **[Any seat fielding a portal question] 171 cells in the Benchmark Comparison panel just turned
   from a number into N/A — that is intended, not an outage.** Those numbers were wrong. The panel
   already rendered 99 nulls as N/A, which was the live proof that a null renders.
2. **[Yang, external, per Andrew verbatim] The CIX re-save and re-pull** — when the source reaches
   `data_as_of`, the guard serves numbers again with NO code change, each carrying
   `benchmark_last_date == data_as_of`. That is track 3's proof, not this act's.
3. **[`2.0.0_SA_COO~Z`] Flip `<status>` on TO-GUARD-1** — terminal status is the issuer's, never the
   assignee's. AC1/AC2/AC3 are reported with their output at msg 30145.
4. **[`0.0.0_AB_MSTR~Z`] The CLOUD push** — all three of my commits are LOCAL; origin/CLOUD read
   `e82f508eef` at `git ls-remote`.
5. **[`1.0.0_SA_CTO~Z`, optional] The SFN CRLF drift is now normalized** on `YangDataPipeline`, so the
   next apply of that root starts from 0 CR. If other terraform roots carry the same drift, the same
   STOP will fire there for whoever applies next — worth a sweep, but not this act's scope.
