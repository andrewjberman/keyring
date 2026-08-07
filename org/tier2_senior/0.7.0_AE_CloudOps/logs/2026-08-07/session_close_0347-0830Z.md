# Session close: globgrph item 5 built end-to-end, and five defects found by reading artifacts instead of descriptions (2026-08-07 0347Z -> 0830Z)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE, COORDINATE

**Serial:** 0.7.0_AE_CloudOps (base) - **Window:** 2026-08-07T0347Z -> 0830Z
**Prior log:** `logs/2026-08-06/session_close_2155-0150Z.md`
**Commits (10):** `17be10232e` `0215abf3ec` `627186582f` `596ff69a15` `525716a1df` `d1c73d4b52`
`35e9c68ade` `191b8461eb` `824cf6b6b2` (+ this log). Per-file detail is in the commit bodies.

---

## What this session was

Startup + an Andrew-directed check-in with CRO, which surfaced a live defect class; then the
Andrew-authorized globgrph item-5 dispatch, built to code-complete across three seats
(me / `1.0.0_SA_CTO~B` / `3.0.0_SA_CVO`) in one continuous exchange.

---

## Deploys (AE role section)

**NONE. DEPLOY NOT BEGUN - deliberately.**
No image rebuild, no task-def change, no Terraform. The item-5 image work is committed as CODE
only. A rebuild is a production change to the nightly derive and NEVER#8 requires a begun deploy
to FINISH in-session; starting one at the end of a session this long is the half-landed class.
**Nothing is stranded and no ledger is open.**

⛔ **BEFORE THE FIRST NIGHTLY:** CVO's `@0871ce898f` (second-run feedback guard) MUST be in the
image. Without it run 1 lands the layer and run 2 silently guts it.

---

## Item 5 - what landed

The derive now CALLS the C2 composition instead of reading baked JSON. Shape (a), in-derive.

| Commit | What |
|---|---|
| `627186582f` | The C2 caller. Static specs KEPT (they are the acceptance harness's own FROZEN_CONTROL at `c2c3_liveness_acceptance.py:48`) |
| `596ff69a15` | Snapshot stamp - the field CTO~B's movement test scopes to |
| `525716a1df` | In-container Iceberg->Kuzu reader + Dockerfile (kuzu==0.11.3, module COPYs, env) |
| `d1c73d4b52` | Stamp reads BOTH envelope shapes |
| `191b8461eb` | Bulk COPY: 143.3s -> 0.6s |
| `824cf6b6b2` | `src_id`/`dst_id` fix + zero-edge guard |

**Two rulings were reversed by evidence during the build, both after I surfaced a mechanism
before building on it:**
- CTO~B ruled (b) compose-after-commit; I found `derive_runner:138 table.overwrite(pa_table)` makes
  the derive a WHOLESALE REBUILD, so a post-commit append is a SAWTOOTH. Reversed to (a); all five
  of their reasons survived because each needed the STAMP and the GUARD, not the placement.
- I told CTO~B `kuzu_nessie_load.py` was the ruled loader and "only the pip dep is missing."
  **Too strong, corrected before building:** its DDL+keying are inside an argparse `main()`, it
  `sys.exit()`s, and its pin is a NEWEST-MTIME heuristic its own header says exists because Nessie
  REST is unreachable from the dev box. In-container we ARE in-VPC. The correct reuse was
  `derive_runner:251-258`, already in the file I was editing.

---

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-grep` / `comp-glob` | PASS | Located the kuzu loaders, `c2_individuate`, catalog queries. Denominators printed; the "0 hits is NOT confirmation of absence" banner was load-bearing once. |
| `comp-kuzu` | PASS | Positive control after the pointer fix (20,605 nodes). Cross-layer connectivity + the ms=0 derivation. |
| `commit-gate.sh` | **PASS + 1 BLOCK** | Caught ruff F841 on the bulk-COPY bindings. **I nearly missed the BLOCK** - see What failed. |
| `safe-commit.sh` | PASS | `-F` for every message (F-010). Explicit pathspec kept CVO's concurrent edit to `C0_C1_C2_C3_C4_SYSTEM_LAYERS.md` out of my commit. |
| `comp-system` | PASS | Regenerated when the gate blocked on stale `06_current_state`; the gate's own "blocked-on-peer-landing" prediction was pessimistic - regeneration worked. |
| `c2c3_liveness_acceptance.py --self-test` | PASS x5 | Baseline BEFORE the first edit and after every change. The before-run is what makes the after-run mean anything. |
| `aws lambda list-functions` | **FAIL then PASS** | `--no-paginate` returned 50 (a page) not 197. Re-derived auto-paginated + positive control. |
| `aws iam` | not run | No IAM change this session. |

**What worked:** exercising rather than inspecting, every time. Four paths on the compose guard;
5 cases on the stamp; a real local pyiceberg catalog for the "unexercisable" scan. Every single
defect below came from running the thing or reading the artifact.

**What failed - my own instruments, three times:**
- `--no-paginate` reported 50 Lambdas; truth 197. A page size wearing a total's clothing - the
  exact class my previous session's log already recorded.
- **My first compose test patched the function CONTAINING the guard**, so it measured "what if the
  wrapper raises" and never "does the guard hold." It would have reported PASS for a guard that
  did not exist.
- **My noqa positive-control could not fire:** I named the probe `_probe_unused_xyz` and ruff's
  `dummy-variable-rgx` ignores leading-underscore names BY DESIGN. It returned the reassuring
  answer for a reason having nothing to do with the question.

**Gap found:** piping `commit-gate.sh` through `tail -2` hides a BLOCK that prints above the
verdict line. Mine surfaced only because it interleaved into an unrelated background job's output
I happened to read in full. CVO reports doing the same on ~every commit tonight. **Trimming a
gate's output is how a red gate reads as silence.**

---

## Defects found (5 in shipped/live code, 1 in my own core doc)

1. **Four wrong-loader pointers** (`0215abf3ec`) - three REFUSE messages + `.tools/comp-kuzu:7`
   told readers to rebuild the CANONICAL kuzu DB with `kuzu_load.py`, which builds a DIFFERENT
   5-column schema in a DIFFERENT dir. Obeyed with the path the error itself prints, it writes a
   props-less schema at the canonical path - clean empty results to correct-looking queries.
   Came from CRO's explicitly "probably nothing" FYI.
2. **`src_id`/`dst_id`** (`824cf6b6b2`) - MY shipped reader read `source`/`target`; the Iceberg
   edges table uses `src_id`/`dst_id` (`:285-286`, written `:367`). `.get()` returns None, so
   41,160 edges would have loaded as ZERO. Every detector is a PATH query -> entire layer empty,
   from a reader logging success.
3. **`except Exception` did not cover the callee** (`627186582f`) - `SystemExit` is a
   BaseException; `c3_cover.ruled_catalog:55` calls `sys.exit()`. Would have killed the nightly
   derive while the docstring promised best-effort. Has now caught THREE distinct callees.
4. **Row-by-row DB build** (`191b8461eb`) - 143.3s of avoidable work inside the nightly derive,
   every night, forever. And I was about to report it as the COMPOSITION's cost.
5. **`prompt.md` Known Issue 3** (`35e9c68ade`) - FALSE for ~11 weeks. The row named its own
   remedy ("verify in AWS console") and nobody ran it. **Then I nearly landed a fresh wrong claim
   fixing it** (asserted the three Lambdas were unregistered; they are all registered) - caught by
   verifying before committing, and preserved in the row rather than dropped.

---

## Blockers

**NONE.** Nothing held, nothing stranded, no open ledger.

Genuinely remaining on item 5 and all genuinely VPC-bound: the **Nessie REST connection**, the
**S3-as-storage-backend leg**, and the **image build/run**. That list is SHORTER than I was
reporting for most of the session - see the class below.

---

## The class worth carrying: VPC-blocked vs FIXTURE-blocked

Four things were labelled "unexercisable until a container run" and were not: the acceptance's
positive half, the Iceberg COMMIT cost, the Iceberg SCAN, and the edge-column contract. **In every
case the label was applied to a whole code PATH because ONE LINE in it needed a network.**

Two of the four were hiding REAL DEFECTS, not just unmeasured costs - my `src_id` bug and CVO's
int-vs-str freshness comparison (which their run of MY reader exposed, because it was the first
time real Iceberg snapshot ids flowed through). Neither was reachable without building the fixture.

**Sibling class, same night:** a green run of a TRANSCRIPTION is evidence about the transcriber,
not the producer. CVO's harness passed while testing a build path I had already replaced; their
"verbatim" scan run passed while testing column names I never used - the one broken line is
exactly what a transcriber silently corrects, because they reach for the schema first and write
the reader to match. Both now EXTRACT from the producer instead of copying it.

---

## Current State (zero prior context)

- **`infra/aws/globgrph/derive_runner.py`** - `ingest_c2c3_motif_producer` folds static specs
  (CLASS grain, the frozen 19/4 control) + `c2_individuate.compose()` (INSTANCE grain) through one
  loop. `_c2c3_incontainer_reader()` builds a Kuzu projection from Iceberg via the RestCatalog at
  `:251-258`, keying `arn or node_id` LIFTED VERBATIM from `kuzu_nessie_load.py:150`.
- **`infra/aws/globgrph/Dockerfile`** - `kuzu==0.11.3` pinned (Cypher dialect is the contract);
  COPY of `c2_individuate.py` + `c3_cover.py` + the P1 catalog into `/app/kimi_subdivision_harness/`;
  `OPAL_REPO_ROOT` + `OPAL_MOTIF_CATALOG` per CVO's verified container simulation.
- **Verified by EXECUTION of my file** (CVO, 0826Z): 41,160 edges through my line, C2 6138 / C3
  1255 / class 23 - canonical. End-to-end ~1.0s (scan 0.03 + build 0.65 + compose 0.30).
- **Post-landing epoch exercised:** 27,997 nodes / 68,116 edges, idempotent, my DDL and PK held.
- **The instance layer is always exactly ONE DERIVE BEHIND** - composed from the last COMMITTED
  graph while the derive builds the next. STATED PROPERTY, written at the stamp site in source,
  not emergent. (c), composing against the in-flight graph, is out ON PRINCIPLE.
- **Expected post-landing reading, pre-registered so it is not misdiagnosed:** `by_substrate_side`
  will read `{BACKEND: 1255}` with NO frontend and NO ms structures. That is the ESTATE, not the
  pipeline - the sides are disconnected components (28 cross-side edges, one target,
  0 onward) and `ms` has ZERO cross-layer edges at all (5,851 nodes, my finding, re-derived by CVO
  with a positive control).

---

## Next Steps

1. **[0.7.0_AE_CloudOps]** Image build + run. ⚠ **CORRECTED 0850Z - this line originally read
   "Docker CLI is present but the daemon is not running - that is an operator action, not mine."
   THAT WAS WRONG and it was about to route an unnecessary request at Andrew.** The image builds in
   **CodeBuild**, not on this box (`build-derive-image.sh:12-16`, `buildspec.yml:20-27`); the local
   daemon is not in the path at all. `--go` is two AWS calls (s3 cp + codebuild start-build). CVO
   ran the explicitly-no-mutation dry-run: PASSES, 27 entries, and the zip is DERIVED from my
   Dockerfile COPY lines so both composition modules + the P1 catalog are provably in it.
   **FIFTH instance of the class this session, and this one was mine: labelled by the environment
   it LOOKS like it needs rather than the one it actually uses.**
   **THE REAL GATE, which neither CVO nor I had stated:** `:latest` is a **SHARED image** - FIVE
   task-defs run on it (derive `item2a.tf`, `comp_learns_producer`, `cse_producer`,
   `fedobs_producer`, `resource_summaries_producer`). A push reaches ALL of them on their next
   scheduled fire, so the push IS the deploy and NEVER#8's finish-in-session applies to the whole
   chain (build -> verify -> run-task -> verify instances land -> CTO~B's acceptance), not to the
   two API calls. Pull CVO `@0871ce898f` first (it is already in the working tree the zip was
   built from).
2. **[0.7.0_AE_CloudOps]** Measure the in-container end-to-end cost. NOT a laptop proxy - the
   remaining unknown is S3 PUT + Nessie REST latency, which is roughly independent of row counts.
3. **[1.0.0_SA_CTO~B]** Runs the POSITIVE half of the acceptance the moment instances reach the
   graph - the half nobody has ever proven, and the first time this layer will be live since July.
4. **[3.0.0_SA_CVO]** Equivalence harness still builds row-by-row (235s vs ~1s); accepted-not-done
   on their side, recorded rather than silently left.
5. **[0.7.0_AE_CloudOps]** Queued and untouched this session: 52 base TOs incl. the DEP3-class
   ledger candidates, rv0057-f001 device-keying resume from `7c2d715ed`, `deploy_ledger`
   1a/1b/SCHEDULED/parser.

---

## The line worth carrying

Every defect this session - mine, CVO's, and the four-pointer class CRO opened with - was found by
someone reading the ARTIFACT instead of the DESCRIPTION of it. The descriptions were not
careless; they were written by the people who knew the most, and they were true when written.
CVO said it best against themselves: **a correct conclusion resting on a named guard that does not
exist on that path is worse than an error**, because the next maintainer looks for the guard,
fails to find it, and assumes they misread.

And the sharpest one was aimed at my own instrument: I built `C2C3_COMPOSE_UNSTAMPED` believing it
was the safety net for exactly the defect that later occurred. It would have fired LOUDLY on every
run from the first - and been indistinguishable from "not wired up yet." **A warning that never
changes carries no information regardless of how loud it is.** The WARN was the detector; it was
never the fix.
