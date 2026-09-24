# opal_ai -- the Opal Analyst as a microproduct: L1 brief + RCN-0014

**archetype:** MIXED (EXPLORE + SCRIBE)
**Seat:** `4.0.0_SA_CRO~X` (site Z, SITEZ; first Claude session of this lane -- its prior log and handoff, 2026-08-27/29,
were a Codex seat on the LAPTOP fabric). **Window:** 2026-09-23 ~18:41Z-19:35Z.

## Objective

1. Startup: `/watcher`, then `org/XXX.md`.
2. Andrew-direct ~18:5xZ: a brief plus prior art for making the Opal Analyst a microproduct in a new repo `opal_ai`, in
   three slices (Opal -> Template -> Clients).

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `-i 'opal.analyst\|opal_analyst\|opalanalyst' --files --all` (output to scratch file) | 3,086 hits / 72,439 files | first attempt piped into `tail`: RAIL-DENIED (census receiver); re-run to a file outside the corpus |
| `comp-find` | `"the walk"\|...\|endpoint discovery` | 63 hits | located RCN-0001/0002 HAR walks + the profiler |
| `comp-find` | `self.?heal\|AUTH_SELFHEAL\|cookie...` | 1,711 hits / 897 files | vendor-access designs of record + AUTH_SELFHEAL |
| `comp-find` | `RCN-0013`, `RCN-0014` | 2 hits / 0 hits of 72,480 | 0013 taken by CRO~Z today (section, no index row); 0014 free |
| `comp-which` | `--help` (by accident) | "NO CURATED RULE MATCHED", 78 tools | used as a live observation of the router's honesty line (brief finding 13) |
| `directives-check` | `--code D6`, `--code D9`, `--code D11` | D6 0 members SITEZ; D9 9 members LAPTOP 46 open TOs | placement finding |
| `to-check` | `--all --assignee 4.0.0_SA_CRO~X` | 0 active | startup B.1 |
| rail denials | raw `find` x1, `comp-find \| tail` x1, `grep` on `.tf`-adjacent script x1 | 3 denials, each single-segment, 0 later segments lost | two `# rail-checked` comments swallowed a later segment of the same line (a comment runs to end of line) -- re-run separately, no effect lost |
| `safe-commit.sh` | 3 runs | 1 BLOCKED (sparse cone lacked `org/modules/graph` -> `comp_constants_cli` import), then 2 committed | cone widened to `org/modules/graph lib` |

## Work Completed

1. **Startup.** Registered `4.0.0_SA_CRO~X` (was NOT REGISTERED). Watcher armed (task bzy8go4ti, script pid 21548);
   `[WATCHER-EXPIRED]` at ~19:11Z, re-armed the same turn (task bz3ugiwt9, pid 43980; census 1 row each time).
   Session serial file written; A.2 audit-archive ran, 14 findings of the known migration classes, not chased; PATH 104
   of 104, forwarder exercised; pre-commit hook present. Inbox empty; delivery ledger 0 rows since 09-20; zero crons. The
   lane's 08-29 carried gate (NFRA_C3MATERIALIZE L3W3 F7) was measured spent: COO~X's delivering cut @03013b7115, 08-30.
2. **Andrew-direct recorded and broadcast.** Record @6ae5ab5fd3; broadcast 3 of 3 DELIVERED (24997-24999: CTO~Z, COO~Z,
   MSTR~Z).
3. **Research pass**, repo reads only at SITEZ @1b1244cecf:
   - the 09-22 CRO~Z assessment and its two Andrew records;
   - the 09-17 tool-index brief + scoping;
   - the MCPINDEX PRD + wind-down position;
   - the OPLGTW PRD (contracts);
   - the gateway layout, `_run` chain and integrations standard;
   - the BG seat's prompt, request catalog and Bloomberg guardrails;
   - OPAL_ANALYST PRD §1-4, §10.0-10.1, §11, §12;
   - the D6 GraphQL design, and Andrew's client data-access brief (head);
   - the Third-Party Standard, the BD and Schwab designs-of-record, the AUTH_SELFHEAL PRD;
   - RECON_REGISTER RCN-0001/0002;
   - comp-which, its routing harness docstring, and the manifest schema;
   - the RCN-0012 FSI plugin brief.
4. **The brief** `docs/briefs/opal-ai-microproduct-repo-brief-20260923.md` and the RECON_REGISTER row and section
   RCN-0014, commit a47993af9c. Delivery notice 3 of 3 DELIVERED (25011-25013).

## Decisions Made

- **Worktree, not the shared index:** the shared tree carried a foreign open merge (MERGE_HEAD b475b96309, a
  `0.0.0_AB_MSTR` portal-gitlink commit, 1,546 staged) at both commit times. Committed on `cro-x-opalai` in a sparse
  linked worktree. Neither the merge nor its index was touched.
- **The 09-22 rulings are treated as standing and today's word as the latest.** Where they differ (repo name and
  packaging), the brief SURFACES the difference as Part VIII call 1 with a recommendation. It does not adjudicate.
- **A Part VIII (calls) was added** beyond the skill's seven parts and marked NOT OUTCOME-BEARING, following the
  09-17 brief's practice, because two approved rulings interact with today's word and L2 needs the fork visible.
- **Explore/Task subagents were not used** (`org/XXX.md` bans both); the research was done directly.

## Correction to a sent message

25011-25013 says of `cro-x-opalai`: *"2 of its 3 commits are the record and the brief"*. At send time the branch had
**2** commits, the record and the brief, and no third. This log is the third. Recorded here rather than by another
message: nothing any recipient acts on turns on the count.

## Blockers

None at this seat. The drain of `cro-x-opalai` into SITEZ waits only on the shared tree's foreign open merge
(b475b96309). Push to origin belongs to `0.0.0_AB_MSTR~Z`, on Andrew's word.

## Current State

3 commits on `cro-x-opalai` (6ae5ab5fd3 record, a47993af9c brief + register, this log), LOCAL; origin/SITEZ
1b1244cecf (ls-remote, 19:2xZ). The brief is CTO~Z intake; nothing dispatched. Watcher live (bz3ugiwt9). Zero crons.

## Next Steps

1. [this seat] `safe-merge.sh cro-x-opalai` from the shared tree once the open merge clears; verify all three commits
   are ancestors of SITEZ.
2. [`1.0.0_SA_CTO~Z`] `/endpoint --forward` on the brief, if Andrew routes it.
3. [Andrew] the 8 Part VIII calls; calls 1 (one repo) and 2 (layout) shape everything after.
