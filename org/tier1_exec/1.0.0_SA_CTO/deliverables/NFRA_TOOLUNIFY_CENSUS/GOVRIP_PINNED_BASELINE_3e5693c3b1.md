# GOVRIP pinned baseline -- 31 failed / 840 passed @ 3e5693c3b1

**Measured by:** `1.0.0_SA_CTO~Z`, 2026-07-26. **Supersedes my withdrawn "23 @1fcf560b8".**

## How it was measured (the part that makes it PINNED)

Isolated detached worktree at `3e5693c3b1`, verified `0 dirty under org/modules/graph` BEFORE the run.
The live tree was NOT used: it carried an uncommitted `boundary_report.py` and a DELETED `ts_source.py`,
with other lanes committing during the window. A baseline over a moving dirty tree is what produced my
withdrawn "23 @1fcf560b8" and my retracted "34 and climbing" (which settled at 28).

    command : python -m pytest org/modules/graph -q -p no:randomly
    result  : 31 failed, 840 passed, 2 skipped, 2 xfailed, 6 warnings in 486.26s
    worktree: 43 dirty files, ALL tools/news_scanner/ line-ending churn, OUT of scope

**Enumeration completeness checked, not assumed:** 31 captured `FAILED` lines vs pytest's own total of
31. I truncated a distribution exactly this way earlier in this session -- reported 24 of 34 failures as
a complete list -- so the capture is verified against the tool's own count rather than trusted.

## The 31

> **The GOV/OTHER split below is a FILENAME REGEX. It is a HYPOTHESIS about expected movement.**
> It is NOT a structural determination, and it is NOT the (a)/(b) partition. `0.8.0_AE_CloudComp~A`'s
> AST partition -- **6 delete / 16 rewrite, denominator 22 files / 118 test fns** -- governs that
> question. My text-grep attempt at the same partition scored **5 of 8**, with three prose false
> positives (module docstring, comment, f-string) and one miss. Same instrument, same class of error.
> Re-derive structurally before relying on this split for anything that lands.

### GOV -- 18 (expected to move under GOVRIP; their ABSENCE of movement is the finding)

```
test_comp_secrets_bd_hold.py::test_consumers_excludes_bd_and_schwab_by_default
test_extract_column_gaps_bd_hold.py::test_include_held_override_reads_the_bd_gold_script
test_extract_column_gaps_bd_hold.py::test_inf_path_reads_and_finds_the_gap_but_bd_path_is_skipped
test_extract_column_gaps_bd_hold.py::test_schwab_silver_path_also_skipped
test_extract_iam_sovereign_guard.py::test_MUTANT_flag_check_off_would_read_bd
test_extract_iam_sovereign_guard.py::test_agent_context_refuses_held_source_without_opening
test_extract_iam_sovereign_guard.py::test_build_reads_zero_bd_source_end_to_end
test_extract_iam_sovereign_guard.py::test_rel_is_held_covers_bd_and_schwab_silver
test_freshness_manifest_gen_bd_hold.py::test_bd_config_held_by_default_reads_under_flag_nonvacuous
test_freshness_manifest_gen_bd_hold.py::test_is_held_predicate
test_graphreach_discrimination.py::test_sovereign_held_query_REFUSED
test_incrparity_cli_bd_hold.py::test_bd_blocked_for_agent_by_default
test_indexer_bd_content_exclusion.py::test_indexer_never_reads_held_content
test_indexer_bd_content_exclusion.py::test_mutation_off_reintroduces_the_read
test_kuzu_discrimination.py::test_sovereign_held_query_REFUSED
test_pipescript_deployed_bd_hold.py::test_bd_branch_held_and_named_by_default
test_platinum_held_path_guard.py::test_guard_prevents_read_on_a_held_bd_path
test_platinum_held_path_guard.py::test_held_path_hit_is_a_pure_string_check_never_opens
```

### OTHER -- 13 (expected to STAY red; any move here is a finding)

```
test_adapter_audit.py::test_d2_MUTANT_concatenated_name_would_not_exist
test_comp_types_index_idempotent_and_fallback.py::test_default_fallback_flag_agrees_with_category_and_counts_or_style
test_comp_types_index_idempotent_and_fallback.py::test_index_manifest_is_idempotent_and_carries_no_run_duration
test_iam_census_vintage.py::test_F2_live_census_limb_is_gated_and_DISQUALIFIED_not_silently_used
test_iam_resource_verdicts.py::test_deny_overlay_incompleteness_is_counted_and_never_silent
test_lambdamap.py::test_detects_mislocated_top_level
test_lambdamap.py::test_detects_missing_entry_blindspots
test_multi_pipeline.py::TestCrossPipelineEdge::test_silver_accounts_dim_has_inf_gold_consumer
test_multi_pipeline.py::TestInfGoldScriptIO::test_d04_reads_silver_accounts_dim
test_routes_comment_blindness.py::test_getAccountDistribution_resolves_to_live_general_url
test_routes_unresolved_not_none.py::test_real_build_client_composed_is_unresolvable_not_open
test_routes_unresolved_not_none.py::test_real_build_does_not_blanket_relabel_everything_unresolved
test_tool_graph_coupling_diff.py::test_live_coupling_diff_is_total_and_pure
```

`test_iam_resource_verdicts::test_deny_overlay_incompleteness` was independently confirmed
PRE-EXISTING by `~A` in an isolated worktree at `83aa8a93e3` (identical 2-vs-3 failure before its
first Stage-5 touch) -- verified, not reasoned.

## Acceptance, restated so it is usable

The criterion as originally handed to `~A` -- *"an output move IS a finding"* -- was **unusable**
against an unpinned baseline, because a pre-existing red and an introduced one are indistinguishable
to the executing lane. That was my scoping error. Against THIS set:

- a move in the **18** is expected; its **absence** is the finding
- a move in the **13** is a finding, full stop
- `test_prod_write_guard.py` is OUT of scope, currently GREEN, and must stay green -- verify it
  independently before and after every commit; if it moves, stop and escalate rather than diagnose

## ⚠ AMENDMENT 2026-07-27 -- THIS BASELINE WAS NOT FULLY PINNED, AND THE "2 skipped" WERE DATA

**Two of the numbers above are state-dependent, not code-dependent. Corrected here rather than
rewritten, because the original run is a true record of what it measured.**

`comp_ws4_crosswalk_test.py` reads `_WORKSPACE_ROOT / ".comp-graph" / "graph.json"`
(`comp_ws4_crosswalk.py:230`, `_WORKSPACE_ROOT` derived from `__file__` at `:44`, so per-tree).
**That file is UNTRACKED** -- `git ls-files .comp-graph/` returns **0** -- so `git worktree add`
does not create it and a SHA does not pin it. **The suite writes it mid-run:** my worktree was
created ~23:33Z with no `.comp-graph/`; the file appeared at **23:42:43Z, inside the 486s run.**

### Controlled demonstration -- same SHA, same worktree, same command, artifact state the ONLY variable

    baseline (artifact ABSENT when comp_ws4 ran)   31 failed, 840 passed, 2 SKIPPED, 2 xfailed = 875
    rerun    (artifact PRESENT from the start)     33 failed, 840 passed, 0 skipped,  2 xfailed = 875

**33 = 31 + 2.** The two skips became the two failures. Nothing else moved -- 840 passed in both.

Positive control, both directions, reproduced independently by `0.8.0_AE_CloudComp~A`:

    artifact ABSENT   ->  10 passed, 2 SKIPPED   (FileNotFoundError -> the guard fires correctly)
    artifact PRESENT  ->  10 passed, 2 FAILED    (loads, returns 0 nodes, no exception, hits the assert)

### The two findings

> **1. A FROZEN WORKTREE PINS TRACKED CONTENT ONLY.** Anything generated is unpinned inside a
> "pinned" baseline -- and the more thoroughly the pin is trusted, the less likely anyone is to
> check. The worktree was adopted precisely to defeat a moving population; it silently did not
> cover the generated plane, and that bound was never stated.

> **2. THE `2 skipped` WERE THE FINDING AND BOTH OF US READ PAST THEM.** The cross-validation that
> "agreed 31 of 31, member-for-member" was a FAILURE-set diff; these two lived in the SKIPPED
> bucket, where such a diff structurally cannot see them. I published `2 skipped` as a number and
> never asked which tests they were; `~A` read the same line and did not ask either.
> **A test that does not COLLECT is invisible; a test that SKIPS is invisible too** -- and in a
> summary line a skip from a missing file is indistinguishable from a deliberate platform guard.
> **The summary line is the blind spot, not the bucket.**

### Separately: a real defect in that test, independent of GOVRIP

`_skip_if_live_plane_unavailable(exc: Exception)` (`:223`) can only fire from an `except` block.
A load that SUCCEEDS and returns EMPTY never reaches it and falls through to `assert len(...) >= 10`.
The guard catches THROWS and is blind to LOADS-EMPTY. `matched=0 missing=[]` then renders
"nothing was reachable" as "22 components disappeared." **It should skip on empty, not assert.**

### Method correction for anyone using this baseline

Delete `.comp-graph/graph.json` in the measurement worktree before EVERY run, BEFORE and AFTER
alike. Then these two skip deterministically in both and cancel honestly rather than by luck.
Do NOT delete the shared tree's copy -- it is live for other lanes and `.agent_context` sits beside it.

## What this baseline does NOT establish

It is a single run at one SHA. It does not establish flakiness bounds -- no test here has been run
repeatedly to separate a deterministic red from an intermittent one, and `-p no:randomly` pins order
but does not prove order-independence. A red that turns green under GOVRIP for reasons unrelated to
GOVRIP would be indistinguishable from an intended flip on this evidence alone.
