# WS-4 AC-2 DE-close (inc-10 + resolver land) + COTMVP.B & TAGATTR render-verifies

**archetype:** MIXED
**secondary_archetypes:** VALIDATE (primary), IMPLEMENT, COORDINATE

Serial: 0.4.0_DE_ClientPlatform | Window: 2026-07-02 (last log) -> 2026-07-06 13:44Z (Monday post-holiday restart) | Session start.

## Summary

Post-holiday restart on COO's DRIVE GO (WS-4 AC-2 close, resume from inc-9). Grounded the full
WS-4 AC-2 state against LIVE served artifacts + git HEAD (not self-report): found the oracle
read-side needed one more entry, a stranded resolver + a stranded DS-lane emit. Landed the
DE-lane pieces, routed the rest, and closed two parallel render-verifies (COTMVP.B + TAGATTR).
DE-side of WS-4 AC-2 is now COMPLETE + verified; close is externally gated on the INF gold-chain
re-dispatch + CVO re-cert.

## What I did (grounded)

1. **WS-4 AC-2 oracle read-side completion (inc-10, dd6257d12):** grounded that the served inf
   artifacts (clients_tab/dashboard/header) are STILL the 07-02 nightly (LastModified 07-02,
   data_as_of 07-02, as_of_by_dim=null) -- no nightly ran over the 07-03..07-06 holiday. Found the
   config was missing the `inf_platinum_timeseries_overview` entry (CVO's 07-03 ruling
   20260703T002557Z REQUIRES perf-masking on BOTH clients_tab AND timeseries_overview; only
   clients_tab was wired). Added it (as_of_map_field=as_of_by_dim {aua,nna,perf}) ->
   `data/inf/scripts/gold/gold_freshness_config.yaml`. All 4 AC-2 artifacts now config-wired.
   YAML-validated (38 artifact_ids). COO RAVC-ACCEPTED.

2. **resolve_page_threshold() land (exec-landed 4d77ff896 by COO):** DS~C's derive-schema seed
   (table_cadence.yaml e513cdde4) was consumed -- authored + verified `resolve_page_threshold()`
   + `_infer_firm()` in lib/served_vintage.py (was stranded-uncommitted). VERIFIED against the
   seeded registry: mdpf schwab_custody=2->3, cot override=3, bd=2, inf=2, no-gating->None -- every
   firm's derive matches its existing config page. lib/served_vintage.py is BASE_EXEC lib lane
   (owned-paths blocked my DE commit -- same as inc-3 08bce489c); routed to COO for exec-land per
   precedent. COO verified staged content + landed as 4d77ff896.

3. **COTMVP.B render-verify = SOUND (COO-CLOSED):** exercised toRoster() on the LIVE 220-entry
   client_directory.json payload (s3://opal-data-cot/platinum/firm/, $434.17M) -> 220 rows,
   empty-state does NOT fire, AUA column renders, 0 blank rows. Proved the fetch path
   (cottonwood->bucketSuffix='cot'->opal-data-cot, the 2026-06-22 P0 fix) via sibling cot panels'
   proven infra. Both COO failure-modes (empty / shape-mismatch) ruled out. Non-blocking data note
   routed to DS (subset show raw household_id as name + 2 zero-AUA households).

4. **TAGATTR render-verify = SOUND (already landed):** the FE follow-on DS re-flagged was already
   shipped pre-holiday (portal a58ff3a7, on DEV+pushed). Re-verified against the now-live
   full-tagged leaderboard.json (role_breakdown_semantics=advisor_tagged_full_nonadditive, 07-01):
   travis_penfield donut center = entry.total_aua = $444,185,773.56 (dedup, matches DS exactly),
   NOT the role-tile-sum ($360.7M) -- the Andrew 40M-vs-58M fix behaves correctly. Helptext honest
   (0 "reconcile to Total" matches), AdvisorsTab cross-advisor rollup guarded. Reported to DS.

5. **Independently verified DS~A's timeseries emit deploy (b7ca1a07c):** ground-truthed the
   DEPLOYED s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py (ETag 967729c5... ==
   md5, deployed 07-06 13:39Z) carries ts_as_of_by_dim x4 + the perf-map emit (:4226/:4232). The
   script tonight's nightly runs WILL emit the perf-map.

## Files Modified

See commit messages: **dd6257d12** (inc-10 timeseries_overview config-wire). resolver
(lib/served_vintage.py resolve_page_threshold + _infer_firm) exec-landed by COO as **4d77ff896**.
No stranded DE-lane uncommitted work (both confirmed clean at close).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-grep | "reconcile to Total" / cross-advisor-sum / role_breakdown in portal/src | PASS | 0 stale helptext -> confirmed a58ff3a7 removed it |
| comp-freshness | (referenced) chain inf via DS~A -- gold+platinum ~92h FAIL | WARN | grounds the gold-chain-frozen@07-02 gate |
| comp-transform | (referenced from a58ff3a7 verify) AdvisorPublicProfile+AdvisorsTab | PASS | no consumer sums role_breakdown as firm total |
| ds-commit-gate | lib/served_vintage.py | PASS | py_compile+ruff clean pre-resolver-land |
| safe-commit (surface-check) | gold_freshness_config.yaml | PASS | 0 critical-surface touch |

**What worked:** comp-grep decisively confirmed the TAGATTR FE follow-on was already landed
(0 stale strings) -- turned a suspected build into a verify. **What failed:** none. **Gap found:**
none. Grounding note: primary verification this session was live-S3 artifact reads (served
JSON structure + deployed-code ETag) -- the ground-truth layer comp-freshness/comp-pipescript
wrap; used raw aws for the exact as_of_by_dim/ts_as_of_by_dim content inspection the comp-tools
don't surface at field-granularity.

## Current State

**WS-4 AC-2 close-path (DE-side COMPLETE, externally gated):**
- Oracle read-side: all 4 AC-2 artifacts config-wired in gold_freshness_config.yaml
  (dashboard/header {aua,nna}, clients_tab {aua,perf}, timeseries_overview {aua,nna,perf}). Landed.
- Emits: all 3 committed + DEPLOYED + MATCH -- clients_tab @24fd8d1aa, dashboard/header
  @caf834348, timeseries_overview @b7ca1a07c (DS~A, independently verified on live S3).
- Served activation: BLOCKED on the INF gold chain re-dispatch (frozen @07-02, cron-held by
  0.6.1/CTO L7). Cannot ad-hoc gold-run (CLAUDE.md). All emits in-path the moment it fires.
- resolve_page_threshold migration: handed to DS~C (offered DE-lane inf gating_tables wiring;
  awaiting their word -- entangled with the AE-alarm generator, not a unilateral DE edit).

**Closed this session:** COTMVP.B-DS frontend loop (COO-closed); TAGATTR.DS-1 FE render-verify
(reported SOUND to DS).

## Next Steps

- **[0.4.0_DS_ClientPlatform~A]** (in-hand) chase 0.6.1/CTO on the INF gold --chain-full
  re-dispatch timing; CVO flagged to first-emit verify-channel the served timeseries_overview.json.
- **[3.0.0_SA_CVO]** re-cert BOTH AC-2 limbs (perf-masking DECISIVE on clients_tab+timeseries;
  NNA corroborating on dashboard/header) on the first post-re-dispatch nightly's served maps -> WS-4 close.
- **[0.4.0_DS_ClientPlatform~C]** drive the mdpf/cot/bd override->derived migration on the
  schema-owner lane; ping me if they want the inf gating_tables wiring (DE-lane, offered).
- **[0.4.0_DE, me]** event-driven: on the post-re-dispatch nightly, ground the served per-dim maps
  (as_of_by_dim present on all 3) + support CVO's re-cert. Nothing more DE-side until then.
- **[0.6.1_AE / COO]** own the pull_inflection_performance_dim.py tree-drift (manual_api _pull_date
  removal, NOT swept into b7ca1a07c; flagged).
