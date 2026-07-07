# NFRA_COMPTEAM.A1 -- kit content refresh (req#1+#3): the comp-which search rail ported into agent_org_blueprint v2

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

Serial: 0.4.0_DE_ClientPlatform | Window: 2026-07-07 ~13:39Z (post-reboot session start, COO DRIVE dispatch) -> 14:32Z

**Workspace CLOUD commits:** none -- the deliverable lives outside the repo, at `Desktop\agent_org_blueprint_v2*` (the kit's own convention; nothing under `ajb_workspace/` changed). Memory updated (not git-tracked): `reference_agent_org_blueprint_kit_source_and_ship.md`.
**Portal DEV commits:** none (not a portal task).

## Summary

Post-reboot startup (watcher armed, org/XXX.md read), picked up the COO's Wave-1 dispatch: NFRA_COMPTEAM.A1 (KEYSTONE, joint w/ 0.8.0_AE_CloudComp) + NFRA_MOTIF.P1 (gated, held pending DS~A sync). Split A1 with AE (RAVC'd, agreed): I took req#1 (kit content refresh) + req#3 (versioned deliverable); AE owns req#2 (the strip-list build gate). Built + shipped `agent_org_blueprint_v2` -- the PRD's actual ask turned out to be a near-verbatim port of the SOURCE ESTATE's live comp-which/COMPROUTE rail (not a toy/reimplemented one), since NFRA_COMPTEAM_PRD.md section 2 frames this as "same-estate" onboarding (ship the router MECHANISM + Opal's coverage-PRIOR, cold-start the LEARNED term) -- confirmed by reading `docs/architecture/NFRA_COMPTEAM_PRD.md` + `NFRA_COMPRAIL_PRD.md` + `NFRA_COMPROUTE_PRD.md` before building.

## What I did (grounded)

1. **Read the PRD chain first** (Rule 22 -- grounded the mechanism, not just the ask): `NFRA_COMPTEAM_PRD.md` section 2 (Component A scope) + `NFRA_COMPRAIL_PRD.md` (the rail enforcement model) + `NFRA_COMPROUTE_PRD.md` (the posterior engine design). Traced `.tools/comp-which`'s actual live wiring (`comp-which:705` `_default_router` -> `comp_route.route()`, DR2 flip already CVO~B-certed) to confirm the router is ALREADY the default + `--live-affinity` is OFF by default (cold-start is the existing behavior, not something to build).

2. **Traced the real dependency closure** (Python AST import-walk, not guesswork): `.tools/comp-which` -> `org/modules/graph/{comp_route,comp_route_affinity,comp_route_shadow,comp_which_signals,comp_potion_relevance,comp_capability_provider}.py` + `{comp-coverage-map,graph-call-manifest}.yaml`. All pure-stdlib at import time (no AWS/Kuzu hard dependency) -- confirmed portable.

3. **Ported the rail into `Desktop\agent_org_blueprint_v2_src\`** (copy of v1_src): `.tools/{comp-which,comp-grep,comp-glob,_comprail.py,hooks/comp-tool-hud.sh}` + `org/modules/graph/` (the 6 `.py` + 2 `.yaml`), placed at kit-root so the existing relative-path resolution (`WS = dirname(dirname(__file__))`) just works with zero code edits to the engine.

4. **Found + fixed a real bug**: `comp-grep`/`comp-glob`'s shared `_comprail.py` hard-required `git ls-files`, which fails outright with no `.git` -- and this kit's standing invariant is NO GIT. Added `_walk_files_no_git()`, a plain junk-dir-skipping `os.walk` fallback, gated on the SPECIFIC "not a git repository" error signature (a real git failure elsewhere still surfaces loud, per the original docstring contract). v1 never shipped these tools so this had no prior surface.

5. **Trimmed the HUD hook for the kit** rather than porting it verbatim: the source estate's hook hard-denies 5 classes and nudges ~15 domain classes, all routing to comp-tools (comp-iam, comp-routes, comp-pipescript, ...) this kit does not ship, and the hard-deny's only escape valve (`/freeform`) also isn't a kit skill. Porting it as-is would have created exactly the dead-end the whole design principle exists to prevent. Rewrote it to ONE generic advisory-only class (nudge toward `comp-which`, never blocks) and documented why in the file's own header + `docs/SEARCH_RAIL.md` section 3.

6. **Wired + documented**: `templates/claude_settings.json` (PreToolUse hook block), `templates/CLAUDE_md.md` (new short rail section, no incident-prose -- matches v1's already-generic form), `BOOTSTRAP.md` (Step 3b sanity-check, no new copy-step needed since the rail ships pre-installed at kit root), `README.md` (folder map + reading order), new `docs/SEARCH_RAIL.md` (the full spec: 3 pieces, cold-start, why advisory, how to extend), new `CHANGELOG.md` (the v1->v2 delta record).

7. **Verified, not self-reported** (Rule 22 exercised, not just claimed): ran `comp_route.py --self-test` (18/18 PASS) and a live `comp-which` query inside the isolated `v2_src` tree with zero AWS/Kuzu present -- routed correctly, cold-start confirmed. Re-ran the SAME checks against the actual shipped `.zip` (extracted fresh, not the source tree) -- confirmed `comp-grep`/`comp-glob`'s no-git fallback works, HUD hook fires + throttles correctly, `claude_settings.json` is valid JSON, no `.git` present. Found + diagnosed a real extraction issue (Windows MAX_PATH on the PRE-EXISTING, v1, unrelated `deck_generation/brand/logo_package/.../Full Logo/Black/...` deep paths) via bisection -- confirmed it's a target-directory-depth artifact (my test scratch path is unusually deep), not a defect in my delta; all 251 non-logo-asset files (everything I touched) extract and run cleanly even at that same deep test path.

8. **Shipped**: `Desktop\agent_org_blueprint_v2.zip` (surgical fresh zip, `testzip()` clean, 283 files), source at `Desktop\agent_org_blueprint_v2_src\`. Updated the ship-source memory (`reference_agent_org_blueprint_kit_source_and_ship.md`) to point at v2 as canonical, v1 retained-not-canonical, full delta + two open items recorded.

## Open items (not resolved unilaterally -- flagged)

- **Strip-list scope tension**: `comp-coverage-map.yaml`/`graph-call-manifest.yaml` carry real source-estate tool/pipeline/bucket naming as documentation text -- intentional per the PRD ("ship the coverage-prior, same-estate-transferable"), but it sits close to the strip-list's "firm-internal specifics" scrub target. Two incidental "safe-commit" mentions are descriptive text about an enforcement gate elsewhere (not shipped tooling). This is CTO's arch-gate call on req#2, not something I should resolve by unilaterally scrubbing the catalog -- flagged in CHANGELOG.md + the memory update for AE/CTO.
- **Pre-existing (v1) MAX_PATH sensitivity** in `deck_generation/brand/logo_package/` -- not part of this delta, noted for awareness, not fixed (out of my req#1/#3 lane).

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `Desktop\agent_org_blueprint_v2_src\.tools\comp-which` + `comp-grep` + `comp-glob` + `_comprail.py` (fixed) + `hooks\comp-tool-hud.sh` (trimmed) | New: the search rail | No -- kit deliverable, outside the git repo |
| `Desktop\agent_org_blueprint_v2_src\org\modules\graph\*.py` (6 files) + `*.yaml` (2 files) | New: the router engine + capability catalog | No -- kit deliverable |
| `Desktop\agent_org_blueprint_v2_src\templates\claude_settings.json` | Added PreToolUse hook wiring | No -- kit deliverable |
| `Desktop\agent_org_blueprint_v2_src\templates\CLAUDE_md.md` | Added the search-rail section | No -- kit deliverable |
| `Desktop\agent_org_blueprint_v2_src\BOOTSTRAP.md`, `README.md` | Rail install/sanity step + folder map + version label bump | No -- kit deliverable |
| `Desktop\agent_org_blueprint_v2_src\docs\SEARCH_RAIL.md`, `CHANGELOG.md` | New docs | No -- kit deliverable |
| `Desktop\agent_org_blueprint_v2.zip` | New: the ship artifact (283 files, testzip clean) | No -- kit deliverable |
| `memory\reference_agent_org_blueprint_kit_source_and_ship.md` + `MEMORY_FULL.md` pointer | Updated to v2-canonical | N/A -- memory system, not git |

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| Python AST import-walk (ad-hoc) | traced the real transitive closure of `.tools/comp-which`'s local-module imports | PASS | pinned the exact 6-file + 2-yaml dependency set before copying anything -- avoided both under- and over-porting |
| `comp_route.py --self-test` | ran against the ported kit copy, isolated tree | 18/18 PASS | proves the engine is genuinely standalone-portable, not just import-clean |
| `comp-which` / `comp-grep` / `comp-glob` (live exercise, not config-read) | ran against the ported kit copy AND the extracted shipped `.zip` | PASS | render-verify pattern (Rule 22): exercised the actual shipped artifact, not just the source tree |
| N/A -- comp-which/comp-grep/comp-glob are the deliverable itself here, not a tool used to build something else | -- | -- | this TO IS "add a comp-tool-class capability," so the usual "which comp-tool answers this question" reflex does not apply the same way; used Grep/Glob/Read directly for kit-tree inspection (self-contained non-estate directory, no dependency-graph to illuminate -- same carve-out class as the deck-engine exception in NFRA_COMPRAIL_PRD.md sec 3) |

**What worked:** the AST-traced dependency closure kept the port minimal + correct (6 files, not a guess). Exercising the actual shipped zip (not just the source tree) caught the MAX_PATH bisection question before it could be mistaken for a real defect. **What failed initially, fixed:** `comp-grep`/`comp-glob` hard-required git; caught by smoke-testing before shipping, not after. **Gap found:** the strip-list-vs-transferable-prior tension on the catalog YAMLs (flagged, not resolved by me).

## Current State

- **NFRA_COMPTEAM.A1 req#1 (content refresh) + req#3 (versioned deliverable): DONE**, verified against the actual shipped artifact.
- **req#2 (AE's strip-list build gate): NOT started** by AE yet (queued behind their DEBTSCAN residual-shrink work per their reply). TO as a whole is NOT complete -- do not flip its status.
- **NFRA_MOTIF.P1**: held. Synced with 0.4.0_DS_ClientPlatform~A (COO resolved the lane ambiguity to DS~A); message sent, queued behind their COMPILERKIT work, no response yet.

## Next Steps

- **[0.8.0_AE_CloudComp]** build the req#2 strip-list gate against `Desktop\agent_org_blueprint_v2_src\` once free of DEBTSCAN; ping me to smoke-test jointly once it's up, and make the CTO-arch-gate call on the catalog-YAML scope tension flagged above.
- **[1.0.0_SA_CTO]** arch-gate the strip-list (PRD section 6, arch-gate #1) once AE's build lands; the catalog-scope open item needs a ruling before the kit can actually ship to a colleague.
- **[0.4.0_DS_ClientPlatform~A]** MOTIF.P1 sync, whenever COMPILERKIT queue clears -- no urgency flagged from my side.
- **[me]** on AE's req#2 landing: run the strip-list gate against v2, close the loop, RAVC COO. Until then, event-driven -- watching inbox.
