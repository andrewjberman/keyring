# AdvisorIntelligence -- Noel Soderblom FE (inflection allowlist) committed + HELD for coordinated-go

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

**Agent:** 0.4.2_RD_AdvisorIntelligence (React Designer, ClientPlatform pod)
**Date:** 2026-07-12 (~1150Z-1210Z)
**TO:** CTO~B FE TO -- INF advisor-of-record go-live (Andrew GO 2026-07-12), delivered via MCP
**Reports to / RAVC:** 1.0.0_SA_CTO~B

## Summary

Startup (/watcher + org/XXX.md), then took CTO~B's FE task order: add advisor `noel_soderblom`
to the Inflection tenant advisor allowlist and lift the render cap so his card shows. The change
is a 2-value edit to a tenant CONFIG file plus a header-comment refresh. Committed local on
portal DEV, **UNPUSHED and HELD** -- it ships COORDINATED with the gold that surfaces Noel in the
one go-live CTO~B assembles, never before. Andrew-direct (cascaded via CTO~B/MSTR): take a /log
of this held state now -- this is that log.

## Work done

1. **/watcher** -- fresh session (NOT REGISTERED). Registered 0.4.2_RD_AdvisorIntelligence
   (PID 36296); armed persistent inbox Monitor (task bg3uyfu2u); no orphan/legacy watcher; inbox
   empty at pull; no stale cron. Reachable.
2. **org/XXX.md startup** -- Tier-3 worker: session-serial file written, `.comp-graph/.agent_context`
   set, owned-paths hook already wired, ZERO crons armed (LD-0175). Read README + prompt.md.
3. **Inbox** -- Monitor delivered the CTO~B TO mid-startup, plus an Andrew-direct "take a /log now"
   cascade. ACK'd both immediately (RAVC step 2).
4. **The change** -- `portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts`,
   `panels.advisorList`:
   - `maxEntries: 4 -> 5`
   - `allowedAdvisorKeys` append `'noel_soderblom'`
     (now `[inflection_wealth_management, peter_lee, patrick_scanlan, joe_brandenburg, noel_soderblom]`)
   - header docstring updated: "capped to 4 entries" -> "5 entries (... + Noel)" + AoR/coordinated
     note; historical Phase-0 audit "has 4 employees" -> "had 4 employees at that time" (kept the
     dated finding accurate rather than rewriting it).
5. **Dependency-graph check before commit (Rule 20b)** -- `comp-grep allowedAdvisorKeys` ->
   sole consumer `_shared/tabs/ClientsTab.tsx:270-275`. Read it: `:271-274` filters entries by
   `allowedAdvisorKeys.includes(advisor_id)`; `:275` caps `filtered.slice(0, maxEntries)`.
   Confirms 5 keys REQUIRE `maxEntries >= 5` or the 5th advisor is sliced off. `:292` derives the
   display name from gold `e.name` (IWM -> 'Unassigned'), so no FE name map is needed. No hardcoded
   "4" assumption anywhere.
6. **Commit** -- safe-commit (run with cwd inside portal via subshell), explicit single-file
   pathspec, `-F` message file. `[DEV 73ee2705]`, author 0.4.2_RD_AdvisorIntelligence, 1 file
   changed (7+/5-), surface-check clean (no critical surface).
7. **Held-state verified** -- `git branch -r --contains 73ee2705` = EMPTY (unpushed);
   `git show --name-only HEAD` = layout.ts ONLY (nothing swept); portal on DEV.
8. **RAVC to CTO~B** -- commit hash + verified mechanism + held proof + 3 flags (below). Standing by.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-grep | `allowedAdvisorKeys` (portal/src) | PASS | 11 hits/6 files; found the sole consumer ClientsTab.tsx + ruled out any hardcoded-4 assumption before commit (Rule 20b dependency-graph check for a frontend change) |

- **What worked:** comp-grep's SYSTEMS-CONTEXT footer pointed straight at ClientsTab as the
  `[portal component]` consumer, confirming the one file to ground the slice/filter mechanism in.
- **What failed:** nothing.
- **Gap found:** none. (RD minimum is `comp-transform fields` for a data-rendering component; this
  was a tenant CONFIG edit, not a component build, so comp-grep -> the consumer was the correct
  rail rather than a component field-audit.)

## Flags raised to CTO~B (not actioned -- outside the TO's header-only + layout.ts-only scope)

1. Two OTHER now-stale "4" count comments still inside layout.ts (showRankDelta "4 advisors";
   books B4 "all 4 named advisor entries"). Left untouched per CTO~B's explicit header-only scope;
   asked whether to bump in a 1-line follow-up.
2. `_shared/tabs/ClientsTab.tsx:268` carries its OWN pre-existing stale comment ("Inflection:
   3 entries") -- predates Joe. Out of my lane (_shared) and outside the pathspec; flagged for the
   _shared owner.
3. Portal local DEV diverged from origin/DEV (behind 8, ahead 6; mine is 1 of the 6 unpushed).
   Pre-existing, not from this session. The coordinated go-live's DT promote will want a clean
   local-vs-origin reconcile before the push.

## Blockers

None. The change is complete and committed. It is intentionally HELD (not blocked) pending
CTO~B's coordinated-go GO -- a deliberate timing gate, not an unmet dependency.

## Current State

- **File:** `portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts` @ portal commit
  `73ee2705` on branch DEV (portal submodule repo), author `0.4.2_RD_AdvisorIntelligence`,
  **UNPUSHED**.
- **Effect once live (with gold):** Inflection Books-tab advisor list renders 5 entries incl.
  Noel Soderblom (name from gold `e.name`; per-advisor profile/book/detail artifacts auto-generate
  from `account_team`). No other FE change.
- **Gate:** ships ONLY in CTO~B's single coordinated go-live with the gold (gold-alone would show
  Peter dropping ~$25M with $12.4M vanishing into a hidden Noel card). DEV->PROD promote is the DT
  lane, not RD. I hold: no push, no promote-ride, until CTO~B's coordinated-go GO.
- **Reachability:** registered LIVE, Monitor bg3uyfu2u armed, event-driven.

## Next Steps

- [0.4.2_RD_AdvisorIntelligence] HOLD. On CTO~B's coordinated-go GO, confirm the commit is still
  the intended state and hand to the DT lane for the promote; otherwise take no action.
- [1.0.0_SA_CTO~B] Owns the coordinated go-live assembly (DS daily-ETL + AoR-wins + review-clean +
  never-widen sign-off) and the go GO. Disposition the 3 flags above (esp. flag 1: header-only or
  bump the other two stale comments).
