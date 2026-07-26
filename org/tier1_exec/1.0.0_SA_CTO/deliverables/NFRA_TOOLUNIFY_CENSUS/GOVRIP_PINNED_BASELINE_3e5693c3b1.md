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

## What this baseline does NOT establish

It is a single run at one SHA. It does not establish flakiness bounds -- no test here has been run
repeatedly to separate a deterministic red from an intermittent one, and `-p no:randomly` pins order
but does not prove order-independence. A red that turns green under GOVRIP for reasons unrelated to
GOVRIP would be indistinguishable from an intended flip on this evidence alone.
