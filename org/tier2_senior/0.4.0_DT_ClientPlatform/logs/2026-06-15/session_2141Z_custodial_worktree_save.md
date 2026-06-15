# DT session 2026-06-15 ~2141Z — custodial working-tree save (Andrew-direct)

**archetype:** DEPLOY
**secondary_archetypes:** SCRIBE

## Request
Andrew-direct: "make sure all portal changes are committed and pushed to DEV and that all ajb_workspace changes are committed and pushed to CLOUD."

## Outcome
- **Portal (DEV):** already fully in sync — `DEV == origin/DEV` (0/0). The only working-tree content was scratch (`.runtmp/`, `.frontend-dev/`, a stray `org/` cwd-artifact dir). Nothing legitimate to commit; left scratch untouched. Main tree confirmed on DEV (rule 19).
- **Workspace (CLOUD):** now `CLOUD == origin/CLOUD` (0/0). Two pushes:
  1. `644979773` — pre-existing ahead-1 commit (DS log, FIND_DUALBIZ.001) pushed as-is.
  2. `d17d45be0` — **custodial cross-lane save, 150 files** (10,543 ins / 101 del), authored `0.4.0_DT_ClientPlatform` with owned-paths **OVERRIDE** (`custodial-save-andrew-direct-20260615`, audited in `org/git-author-override-audit.log`). Andrew chose "custodial sweep under DT" when asked.

## Method (curation, not blind sweep)
Working tree held ~10,044 untracked files (~2.6 GB) + 26 tracked-modified across ~15 agents' lanes. Blind `git add -A` was unsafe (nested git repo, personal files, multi-GB scratch). Built an explicit allowlist: all 26 tracked-modified + 125 curated untracked = 151, minus 1 CL-fabric file caught by the CLOUD/CL branch-isolation gate = **150 committed**. All 11 included `.py` were `py_compile`-clean (preflight).

### Excluded (intentional)
- ~2.6 GB scratch: `.runtmp/`, `.playwright-mcp/`, `.frontend-dev/`, `.claude/projects/` (session+memory state), `org/mcp/sessions/`, and **dozens of stray nested `org/` dirs** (lingering-cwd artifact — misplaced telemetry/mcp writes, e.g. `data/black_diamond/scripts/gold/org/mcp/agent_telemetry/*.jsonl`).
- Personal: `.italy_img/`, `Italy_7Day_*` (trip deck).
- `Factor_Scanner.V0/` — a **nested git repo** (committing would embed a broken gitlink).
- `comp/` (whole untracked compiler-framework dir) + `org/threads/handoff/*.patch` — per Andrew's answer (exclude both).
- Root diagnostic PNGs, `infra/aws/lambda/globgrph/kuzu_nessie_db`.
- `data/cot/scripts/bronze/cot_backfill_date_probe.py` — **DS deploy-cycle (rule 13)**; safe-deploy pre-push gate scope. Left for DS.
- `org/tier1_exec/2.1.0_SA_COO/task_orders/COMP_LEARNS.271...md` — **CL-fabric**, belongs on COMP branch (feature_clb).

Final audit: the only real source/doc left uncommitted are exactly those 3 intentional items (+ comp/, handoff patch). 0 tracked-modified remaining.

## Compiler Tools
None run. Scope was a git custodial **save** of other agents' already-authored working-tree edits, not a logic/pipeline/portal/data-prop change I designed — so the Rule-20 dependency-graph pre-change checks and comp-* gates don't apply. Verification was via the repo's own gates: owned-paths hook (block→override, audited), CLOUD/CL branch-isolation gate (caught 1 CL file), safe-deploy pre-push gate (no deploy-scope `.py` → no-op), plus a `py_compile` preflight on all included `.py`.

## Notes for owners
- DS (find): `data/cot/scripts/bronze/cot_backfill_date_probe.py` still uncommitted — yours to commit+deploy via the DS cycle.
- CL COO: `COMP_LEARNS.271` TO still uncommitted on CLOUD — commit on COMP via feature_clb.
- Standing hygiene: the ~2.6 GB of nested-`org/` cwd-artifacts + scratch dirs are not gitignored; a `.gitignore` sweep would stop them re-surfacing every status.
