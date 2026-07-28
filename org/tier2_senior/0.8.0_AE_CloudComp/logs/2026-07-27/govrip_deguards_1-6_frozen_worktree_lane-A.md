# GOVRIP de-guards 1-6 -- executed and measured in a frozen worktree (lane ~A)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Window:** `634a9f775` (2026-07-26T23:55Z) -> now. **Zero commits to the shared tree by design** --
base CTO ruled MEASURE per-file, LAND ONCE, and nothing lands until it has the diff.

## Objective

Execute the GOVRIP batch: remove the tool-level governance hold predicate from the comp-tool surface
per Andrew-direct 2026-07-25 ~185538Z (*"our comp tools should absolutely never be limited on
governance ... that sounds like the tools have built in blind spots for absolutely no reason"*),
measuring each de-guard against a pinned baseline so any movement is attributable.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-iam` | `investigate-candidates-self-test` | PASS | behaviour smoke after de-guarding `extract_iam` -- my own arc; confirms the de-guard did not break the tool |
| `pytest` (measurement instrument, not a comp-tool) | `org/modules/graph -q --tb=no`, 8 runs | see deltas below | full-directory per de-guard; ~8 min each, ~50 min total, deliberate |
| `python -m py_compile` | every touched module | PASS | |
| ad-hoc AST classifiers (`classify_functions.py`) | per-function (a)/(b)/(c) partition | 13 DELETE / 2 RE-EXPRESS / 36 KEEP | written this window; supersedes CTO~Z's grep partition |

**Why so few comp-* tools:** this window is source de-guarding whose only sound verification is
EXERCISE (does the guarded path now read? does a re-introduced guard redden the control?). The
estate-query comp-tools answer "what connects to what", not "did this edit change behaviour", and
substituting one for the other is the wrong-instrument class. `comp-iam` was run because it is the
tool I de-guarded.

**What worked:** measuring instead of classifying. Three rounds of static partition -- CTO~Z's grep,
my file-level AST, my per-function AST -- all missed that `_SH = cd._is_held.__globals__` breaks
COLLECTION for a whole file. Running the de-guard found it in one command.

**What failed:** my own de-guard comment silently defeated a live drift control (below). And my
first PROD_WRITE hard-keep rule never fired.

**Gap found:** four, all filed for after landing rather than fixed mid-batch (a detector change
inside the measurement window makes every subsequent delta incomparable).

## Work Completed -- 6 of 10 de-guards, each mutant-verified

| # | Target | Tests | Delta |
|---|---|---|---|
| 1 | `.tools/freshness_manifest_gen.py` | 2 DELETE, 1 KEEP (non-vacuity control) | clean |
| 2 | `clobber_scan.py` (+ `--allow-held` CLI flag) | none (self-test in-file, 5/5) | clean |
| 3 | `comp_dispatch.py` | 1 DELETE, 1 RE-EXPRESS, 1 KEEP-strengthened | clean |
| 4 | `comp_recognizers_code` + `_config` (ONE unit) | 4 DELETE, 1 RE-EXPRESS, 1 KEEP-strengthened | clean |
| 5 | `extract_iam.py` | 6 DELETE, 3 re-expressed | clean |
| 6 | `pipeline_cli.py` (TWO sites) | 2 -> 1 consolidated | clean |

**Cumulative vs pinned BEFORE @`3e5693c3b1`: ZERO new node IDs. Collection reconciles exactly at
every step** (880 -> 868 after dg5, each drop matched to an intended deletion).

## Findings

**1. The live PROD_WRITE control routed THROUGH the governance internal being deleted.**
`_SH = cd._is_held.__globals__` at module level, in TWO files. Deleting `_is_held` made the whole
file fail at COLLECTION, taking `test_prod_target_control_did_NOT_retract` with it -- a guard both
CTOs ruled untouchable. **The 2026-07-22 split moved the DEFINITIONS apart and left an ACCESS PATH
joining them; a split that leaves a reference bridging the halves is not fully split.**

**2. `is_prod_write_forbidden` is defined TWICE, independently, with no import edge**
(`prod_write_guard.py:95`, `sovereign_held.py:123`), over two independent tuple copies. They agree
today by coincidence of content, not construction. My proposed bare re-point would have left
`sovereign_held`'s copy untested; CTO~Z's both-assert-plus-equivalence form is what landed.

**3. A test fixture that NEVER PARSED.** `parse_catalog` wants a heredoc; the fixture was a quoted
assignment, so `catalog` was `{}` on every run since the file was written. Invisible because the only
assertion was `not over.get("held")` -- **an empty parse satisfies "no skip flag" exactly as well as
a real read.** Asserting positive content is what surfaced it.

**4. My own comment masked a live drift control.** `_imports_sovereign_held` is a SUBSTRING check;
my note *"the sovereign_held import ... are REMOVED"* contains the substring, so the control reported
"still imports" about a file whose import I had deleted -- a FALSE NEGATIVE, the direction that hides
a missing guard. **I retracted part of de-guard 1's "clean delta" on this: an empty delta is only
evidence if the instruments that could have filled it were able to fire.** CTO~Z then swept and found
**4 files in the shared tree already defeat that control pre-GOVRIP, including the control's own file.**

**5. A de-guard silently turned a unit test into a network test.** `test_pipescript_deployed_bd_hold`
stubbed `shutil.which` only on the override arm, because the default arm short-circuited at the guard.
With the guard gone it ran a REAL S3 deploy-verify -- **87 seconds of live AWS against `opal-data-bd`**.
Now stubbed unconditionally; 0.07s.

**6. Scope gaps in the handed batch, all from enumerations corrected after the batch was scoped:**
`.tools/comp-secrets` (extensionless, invisible to a `*.py` scan) is a confirmed importer and was
NOT in the 9 -- CTO~Z ruled it in as de-guard 10, FORCED because my own widened gate covers `.tools`
and would go red at land time. `pipeline_cli` had TWO sites, not one. `extract_pipeline` holds its
own guard, not merely a cluster reference.

## Blockers

None. Clear to run 4-10 without checking in (CTO~Z 20260727T015111Z).

## Current State

Frozen worktree `wt2` @ pinned `3e5693c3b1`, de-guards 1-6 applied, **nothing committed to the shared
tree**. (`tools/news_scanner/*` shows dirty in that worktree -- pre-existing line-ending churn present
at checkout, NOT mine; CTO~Z observed the same 43 files in its own worktree.)

Protocol per de-guard: `rm -f .comp-graph/graph.json` (my worktree only -- it is UNTRACKED, so a
frozen worktree does NOT pin it) -> apply de-guard + owning tests -> full-directory pytest ->
node-ID diff + collected-count reconciliation -> PROD_WRITE enumeration (a drop is a STOP) -> mutant.

**Filed for AFTER landing, deliberately not fixed mid-batch:**
- `_imports_sovereign_held` substring -> AST (with CTO~Z's 4-file sweep attached)
- `comp_ws4_crosswalk` `_skip_if_live_plane_unavailable` takes an `Exception`, so it cannot fire on
  the LOADS-EMPTY path -- fails `0 >= 22` where it should skip
- duplicate `is_prod_write_forbidden` with no identity binding
- `investigate-candidates` fleet-scale (NOT SCHEDULABLE constraint already mechanical)

## Next Steps

1. **[0.8.0_AE_CloudComp~A]** de-guards 7 (`validate_cli`), 10 (`comp-secrets`), and the
   `trace_graph` CLUSTER -- which must now also carry `extract_pipeline`'s own column-gaps guard, and
   still owes a MEASURED verdict on whether `infra/aws/globgrph/extract_gold_compute.py` is inside it.
2. **[1.0.0_SA_CTO]** takes the landing: cumulative delta, per-de-guard PROD_WRITE enumeration,
   cluster verdict, mutant results. Step-3 `git rm` is its boundary.
3. **[1.0.0_SA_CTO~Z]** the four filed defects, post-landing.
