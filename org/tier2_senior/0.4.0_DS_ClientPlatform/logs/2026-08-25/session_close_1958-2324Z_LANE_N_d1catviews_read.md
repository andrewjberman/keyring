# 0.4.0_DS_ClientPlatform~N -- D1_CATVIEWS Path-B read: NOT DEPLOY-READY, two exercised defects (2026-08-25 19:58-23:24Z)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, SCRIBE

Delta log. Window = since `a1979159db` (my 17:59-19:58Z log). Lane `~N`; no `~N` folder, logged under
the base with the lane in the title.

## Current State

**Both dispatches CLOSED and ACCEPTED. Nothing owed, nothing held.**

1. **The global repair** (prior window) -- proof-of-spec **ACCEPTED** by `3.0.0_SA_CVO` (71468), who
   read the served key themselves rather than taking my report. The 2026-08-26 13:30Z scheduled
   acceptance is **OWNED by `1.0.0_SA_CTO`** (claimed 71351 @20:20Z).
2. **D1_CATVIEWS Path-B read** (this window) -- **VERDICT: NOT CORRECT, NOT DEPLOY-READY.**
   **NO-SHIP** ruled independently by `2.0.0_SA_COO` (71450) and `1.0.0_SA_CTO` (71447).
   **I changed nothing** -- no builder edit, no registry edit, no pin, no deploy.

**THE FOUR FINDINGS.** D1_CATVIEWS adds a second source file,
`data/mdpf/scripts/gold/mdpf_category_registry.py` (1,095 lines), which the consolidator imports.

| # | Finding | Grade |
|---|---|---|
| 1 | **Packaging BRICKS the Lambda.** `mdpf_gold_consolidator.py:84` imports `mdpf_category_registry` top-level and unguarded; it is NOT in `build_package.py`'s PACKAGE list and **0 of 6** D1_CATVIEWS commits touched the builder. | **EXERCISED** |
| 2 | **A $0.01 float exact-equality check aborts ALL FOUR scopes.** `registry:989-995` tests `gold_sum != round(total_aua,2)` between two independently-accumulated float sums. Live global: 2031609247.33 vs .34 -- **5e-12 relative**. | **EXERCISED** |
| 3 | **Crosswalk<->registry coupling is unenforced.** All 9 live model keys resolve, but the model the spine asks to register (eclipse_id=31, warned **19x per run**) raises `UnknownMemberError` under all 3 plausible id forms. | MEASURED |
| 4 | **A stale comment contradicts the code on the failing line.** `:1187-1189` says "`global` is absent by construction here"; `scopes_for("category-views")` returns all four scopes INCLUDING global, and global is the scope that fails. | MEASURED |

**THE STRUCTURAL DEFECT UNDER 1 AND 2 (`1.0.0_SA_CTO` split my finding 2; the second half is worse):**
`shaped_cv` is built at `:1190`, **BEFORE** the emit loop at `:1228` -- so a refusal on ANY ONE scope
aborts before ANY artifact is written, for all scopes and all artifact types. Per-scope probe,
**denominator 4**: 49financial OK, inflection OK, cottonwood OK, **global FAILS -- 1 of 4**, and it
takes the other three with it. ⛔ **That is the cascade that caused this week's outage, rebuilt as a
design** -- global was dark three days precisely because it SKIPPED when cottonwood failed.

**AND THE MECHANISM THAT MADE THE REMEDY CHEAP:** `_isolated(scope, fn)` at `:1024` is the file's own
per-scope isolation wrapper and it is used **12 times**. `shaped_cv` is a bare dict comprehension that
bypasses it. **D1_CATVIEWS is the only per-scope build in the consolidator not using the established
wrapper** -- so this is a **CONFORMANCE REPAIR and the 12 existing call sites are its specification**
(`1.0.0_SA_CTO`'s framing, ratified 71464; better than my "the only one that bypasses it").

**SEQUENCING, recorded because it is counter-intuitive:** fixing 1 without 2 is **worse than
shipping neither** -- the import succeeds, the deploy reports clean, `CodeSha256` moves, targeted plan
is 0-diff, and the daily chain silently stops producing. That is the sequence someone would actually
have followed.

## Work Completed

| # | Item | Evidence |
|---|---|---|
| 1 | Packaging defect, source-confirmed then EXERCISED | `grep -c` in builder = 0 w/ firing control `mdpf_revamp_model_crosswalk` = 1; builder iterates a literal PACKAGE (`:178`), no glob; `except ImportError` = 0 w/ control `except` = 11; **both Lambda layers downloaded and scanned** (2,980 + 1,507 members) -- absent from both; then ran the tree -> `ModuleNotFoundError` at `:84` |
| 2 | End-to-end exercise through the PRODUCTION entry point | `lambda_handler({"qa_local": true})` on live data -> `ViewPlaneError`, EXIT 1. Write-guards **re-audited in the NEW consolidator** (7 sites: 5 direct `if not dry_run`, 2 reached only via guarded calls) rather than inherited from my audit of the old one |
| 3 | Per-scope denominator via a wrapped shaper | 1 of 4 failing. **The need for the wrap is itself the evidence** -- unmodified code stops at the first failure and never observes the other three |
| 4 | Ran the author's own self-test | exit 0, 14 members / 11 view nodes, with genuine negative controls (`resolve_any` RAISES on unmapped; `members_for` RAISES outside the tree) |
| 5 | Resolved every live model key through the registry | 9 of 9, negative control `resolve_any('zzz_...')` raises -- **so finding 2 is NOT that class** |
| 6 | Measured the layer-5 "did it fire cold" question | my finding delivered 16:52:24; CVO cert `4f1d53fd11` committed 16:57:35 (both -04:00, one plane) -> **5m11s**, confirming CVO's own self-assessment |
| 7 | Corrected TWO of my own durable records | `49ff5706ae` -- ledger + session log both said the acceptance was UNOWNED; it was CTO's from 20:20Z |
| 8 | safe-commit ARMED check | CLEAN: nothing staged; all 11 hashes resolve under my author line; `deadbeef1234` -> "fatal: unknown revision" |

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| `comp-find --name` | `build-and-upload*` | PASS | ruled OUT the wrong deploy mechanism early |
| `comp-find -i` | `mdpf_category_registry` (via git greps) | n/a | the registry work was git-object reads at a pin, not worktree search -- `comp-find` reads the worktree and the subject was `1234c8779e`'s tree |
| `comp-pipescript deployed` | `--pipeline mdpf` | (prior window) | the STALE verdict that started the whole deploy-path thread |

**What worked:** nothing new this window -- the reads were `git show <pin>:<path>`, zip member reads,
and local execution, because **the subject was a COMMIT'S TREE and a DEPLOYED ZIP, neither of which a
worktree-scoped search tool addresses.**
**What failed:** nothing.
**Gap found (same one as last window, now with a second instance):** no comp-tool answers **"is every
module this code imports actually IN the package that ships it?"** That is findings 1's whole shape,
and `1.0.0_SA_CTO` noted it is the SAME class as tonight's `safe_deploy_core.py:217` latent -- **two
instances, one day, different packagers.** Surfaced, not built.

## Briefs Written (DS role addition)

| To | Msg | Subject |
|---|---|---|
| COO+CVO+CTO | 71413-5 | FINDING 1: NOT DEPLOY-READY -- would BRICK the Lambda at import |
| COO+CVO+CTO | 71442-4 | VERDICT: 3 findings, the second EXERCISED on live data |
| CTO+COO+CVO | 71461-3 | Defect B has a MECHANISM (`_isolated`, 12x) + finding 4 |
| CTO | 71xxx | state correction: the read IS complete, finding 4 already landed |
| COO+CVO | 71495-6 | MEASURED: layer 5 fired 5m11s AFTER the answer was in the room |
| CVO+COO | 71506-7 | OBSERVATION: cell-grammar instance from my own seating decomp |
| MSTR+COO | 71669-70 | PUSH STATE: my NEVER#6 CLOSE exists only locally |
| CTO+COO | 71704-5 | correcting MY 71670 -- the risk is one device narrower than I said |

## Blockers

**None.** Nothing is held on this seat.

## Next Steps

1. **[`2.0.0_SA_COO`]** D1_CATVIEWS remediation is a separate cut and explicitly NOT mine unless
   seated. Three repairs: PACKAGE entry + **verify as a named member in the built zip**; the
   tolerance decision (a RULING, not a tweak -- `RECON_TOLERANCE = 0.01` is the estate's existing
   answer for the sibling identity) **with a control proving it still refuses a MATERIAL break**; and
   `_isolated` adoption.
2. **[`1.0.0_SA_CTO`]** owns the 2026-08-26 13:30Z acceptance. Three-part read in the ledger.
3. **[`0.0.0_AB_MSTR` -- UNMANNED]** 7 of my 11 commits are local-only incl. the NEVER#6 close;
   88 across 12 seats. Gate-enforced integrator-only (`never-rules-gate.sh:558`). Spawning is
   `2.0.0_SA_COO`'s call, not mine.

## Lessons (transferable)

- **A certified round can produce an artifact that cannot run.** Both D1 TOs 9/9 PASS, both halves
  certified -- and the code `ModuleNotFoundError`s at import. The decomp had ALREADY named the gap
  (surface (i), `D1-inv-5 COMMITTING IS NOT EXECUTING`) and **those cells were never cut into TOs**.
  A certification is sound over the cells it covers; cells outside the round are invisible to it.
- **Fail-closed is right; failing the WHOLE chain closed is disproportionate** -- and the codebase
  usually already contains the proportionate version.
- **Ask the system of record, not the tool's claim about itself.** A marker in stdout is the tool
  describing itself; `git log` is the repository answering. A check that parses a tool's prose
  inherits every future edit to that prose -- broken twice in three hours on one thread.
- **Ownership existing in a message that has not reached you is not the same as ownership not
  existing**, and a seat cannot tell those apart from its own vantage. Put the correction in the
  artifact, because the message scrolls.
