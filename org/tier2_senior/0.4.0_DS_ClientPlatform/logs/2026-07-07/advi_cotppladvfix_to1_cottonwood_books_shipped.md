# ADVI_COTPPLADVFIX.TO-1 — Cottonwood single-synthesized-advisor Books tab SHIPPED (live-call fast-track)
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, DEPLOY, COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform · **Window:** post-reboot respawn 2026-07-07 ~19:45Z → ~22:40Z · **TO:** ADVI_COTPPLADVFIX.TO-1 (Andrew-direct P0, re-scoped mid-session to a live-call fast-track).

## What shipped
Injected a single synthesized advisor **"Cottonwood Capital Advisors"** into the cot pipeline and drove the full Books-tab drill chain to SERVED + verified, under a live-Cottonwood-call clock. The injection worked first try; the surrounding 49F-cloned gold scripts needed 6 cot-safety fixes to actually deliver the artifacts.

Commits (all cot-only `data/cot/`, deployed to `s3://opal-data-cot/code/gold/` via safe-deploy on push, byte-verified):
- `0bb589a29` — A_01 inject single advisor (guard: fires only when all role cols all-`Unassigned`; self-disables on real matching).
- `64ad3a5fd` — D_02/D_03/D_04 `_load_parquet` schema-drift tolerant (stop crashing on absent 49F `implementor` col).
- `588f4c56f` — D_02 resilient `client_tax_liability` load (cot has none → empty frame).
- `776b85eab` — D_02 ns-normalize `merge_asof`/`merge` date keys (pandas-2.2 ms/ns MergeError).
- `99982fbf4` — D_02 floor NaT `effective_date` before `merge_asof`.
- `442b00a17` — D_04 synthesize `dashboard.json.employee_leaderboard` (the N1 advisor CARD; was fee-gated null).
- `f75998b62` — D_04 synthesize `platinum/firm/leaderboard.json` (the `getFirmLeaderboard` DRILL; was absent → infinite spinner).

## Diagnosis chain (why 5 gold runs)
The cot D_02/D_03/D_04 are verbatim 49F(bd) clones running **`optional`** in the `opal-cot-gold-run` SSM chain → each crash logged `WARN: exit 1 (optional)` and the chain STILL reported Success while `advisors/` stayed EMPTY (this, not "all-Unassigned", is why cot advisors/ was always empty). Served-verified after every run. D_02 crashes, in order: (1) pyarrow prune requesting absent `implementor`; (2) unguarded `get_object` NoSuchKey on missing `client_tax_liability`; (3) pandas-2.2 `merge_asof` ms/ns; (4) `merge_asof` NULL effective_date. Then two FE-render gaps (DE-ground-truthed): (5) `dashboard.employee_leaderboard`=null → no card; (6) `platinum/firm/leaderboard.json` absent → drill spins. Both leaderboards are fee-gated (built from C_08 fee detail) → cot has no fee data → synthesized from AUA/book in D_04.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | A_01.advisor_assignments.py (x2) | PASS | consumers C_08/D_00c/D_02 confirmed unchanged (before/after) |
| `comp-blast` | build_advisor_assignments_history | PASS | resolved to bd (cot 1-thread under-instrumented) → source-grounded the override sites instead |
| live S3 probe | account_team/rel_architect_lookup MISSING | PASS | grounded A_01 as safe injection site (no D_02 override to clobber) |
| `.tools/commit-gate.sh` | each changed script (7 commits) | PASS | py_compile + ds-precommit + ruff clean each |
| `/code-review` (Workflow) | D_02 full-file cot-crash audit | PARTIAL | 18 agents; top "confirmed" (implementor KeyError) was a FALSE POSITIVE (team_pit re-adds the col — empirically the book landed); real dormant findings folded to hardening pass |

**Worked:** comp-pipescript io before/after cleanly proved the IO contract was unchanged; live-S3 grounding of the missing override files settled the injection-site decision (validated later by CTO's C_07 finding). **Failed/Gap:** comp-blast + the graph resolve A_01→bd (cot is 1 pipescript thread — §7 Q3 observability gap); `comp-pipescript deployed` can't see cot code/gold/ (bd-resolve) so deploy-verify was raw `aws s3 cp` byte-compare. **Gap:** the /code-review verifier didn't trace the team_pit merge re-adding implementor → mis-ranked a false positive #1.

## Current State (handoff — zero prior context)
- **SERVED + verified** (`opal-data-cot`): `gold/entities/advisors/cottonwood_capital_advisors/book.json` (summary.tagged_aua $434,165,337.25 == firm headline, 220 clients nested, 825 accts) + `platinum/advisors/cottonwood_capital_advisors/summary.json` + `platinum/firm/dashboard.json.employee_leaderboard` (card) + `platinum/firm/leaderboard.json` (drill). advisor_id==book_key so the drill resolves.
- **Ad-hoc run mechanism** (Andrew-authorized override of NEVER#4 for the call): runner = `opal-cot-gold-run` SSM doc on **cot-exporter** `i-0643a5bee8a8feabf` (the dual-role cot EC2, NOT just a scraper). Fire via Lambda `cot-bd-session-trigger {"mode":"gold-run"}`, or `aws ssm send-command --document-name opal-cot-gold-run --parameters StartAt=D_02` (or D_04) for single-group runs.
- **Known data-quality caveats** on the served Books (pre-existing, NOT this injection; surfaced to Andrew): tax panel ~100% taxable + ~12% blank client names (A_00 incremental corruption — CTO gold-review), numbers frozen at data_as_of 2026-07-02 until DATEMODE holdings-revert lands. Per degrade-clean doctrine, 3 further degraded artifacts (exec_summary/advisor_nna_canonical/accounts summary) were deliberately LEFT ABSENT (absent renders clean; 0-panels look broken).
- **TO-1 CLOSED** by CTO (served evidence meets acceptance). CVO can add a formal served-cert if COO wants.

## Blockers
None on the DS leg. The ONE remaining Books gap (L3 client-click) is **NOT DS** — it routes through the `opal-partners-data` lambda (`getPlatinumClientSummary`, unexercised for cot); the data (220 `platinum/clients/{key}/summary.json`) is already served in the correct shape. Routed to COO for DT/DE (AE dead).

## Next Steps
- **[0.4.0_DE_ClientPlatform]** re-verify full render path (card→drill→profile→book); own or route the L3 client-click (frontend static-read passthrough) — data is ready.
- **[2.0.0_SA_COO / 1.0.0_SA_CTO]** route the L3 lambda-routing fix (DT); rule the container for the systematic cot-gold hardening pass.
- **[0.4.0_DS_ClientPlatform — me]** on Andrew's container ruling: own the systematic cot-gold hardening pass = strip the 49F assumptions (CTO's 17 gold-review defects at `org/tier1_exec/1.0.0_SA_CTO/deliverables/cot_gold_bughunt_reports/` + the D_02 /code-review findings incl. the **stale-advisor-delete DATA-LOSS** at D_02 ~L3262 (empty books list wipes ALL served advisor entities), `build_fee_bps_pit` ms/ns sibling, A_00 tax/names corruption, C_07 `account_is_open` crash, D_03 degrade-loud, and synthesizing the 3 degraded artifacts once DATEMODE restores real numbers).
