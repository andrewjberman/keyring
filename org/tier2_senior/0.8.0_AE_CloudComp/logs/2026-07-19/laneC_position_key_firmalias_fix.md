# 0.8.0_AE_CloudComp~C -- NFRA_ONTOLOGY variance _position_key firm-alias fix (CTO-gated, HELD for GO)
**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE, VALIDATE

Window: ~C RESPAWN (MSTR SPAWN-DIRECT under Andrew proceed-all-NFRA, 2026-07-19 ~18:00Z, PID 23764) ->
this session. PRIORITY = the variance _position_key firm-alias gap surfaced by ~D from CVO's PH2-C2 smell,
routed to ~C @c2a0cd66b with CTO arch-direction + 3 gate conditions. LOW urgency (no live defect, CVO PASS).

## Startup
- /watcher: NOT REGISTERED -> registered (PID 23764); persistent Monitor armed (task b7d237uh1). No prior
  ~C watcher process (clean fresh session; ~A/~D/~Z live, ~C absent). LD-0290 serial file written.
- org/XXX.md startup protocol + /cloud-ops folded (operational reference). No stale crons (arms ZERO).
- Inbox: MSTR SPAWN-DIRECT (corroborates launcher) + 5 COO/~D seam-sequencing msgs -- all acted.

## The finding + CTO direction (grounded)
`_position_key` (summary_corpus.py:518) strips only firm VALUE tokens `[bd,cot,inf]`. "49f" is bd's CLIENT
ALIAS (`firm_names {bd:49financial}`), not a value token, so it SURVIVES -> `bd-49f-etf-ownership-daily`
keys as `{firm}-49f-etf-ownership-daily` != cot/inf's `{firm}-etf-ownership-daily` -> the group read 2-way
`{cot,inf}` instead of 3-way `{bd,cot,inf}`. CTO ruling (c) @c2a0cd66b: 3-way is correct; firm-sep NOT
violated (analytical grouping over resource-summary metadata, no data-plane); 3 gate conditions on the diff.

## What I did
1. **Grounded the design (comp-kuzu live, 07-19 graph age 0.7h):** confirmed bd's `bd-49f-*` infix on live
   data; censused every alias token estate-wide. DECISIVE: `cottonwood`/`inflection` appear ONLY in data-file
   + portal-component names (capitalized / PascalCase), NEVER as an infra firm-position infix -- so
   case-sensitive lowercase value-token matching keeps them out. ONLY bd carries the 49f infix. Grounded ZERO
   over-merge collisions (no bare `bd-etf-ownership-daily`; bd-49f-runner/keepalive/fees/session are singletons).
2. **Declared edit surface to COO+~D before editing** (COO required); COO ACCEPTED (181955Z), seam CLEARED
   both ways (~D builds NEW comp_similar.py, zero edits to summary_corpus.py).
3. **Implemented (summary_corpus.py):** `_firm_aliases(dims)` reader; `_position_key` identifies firm by
   VALUE token only, then strips redundant same-firm alias residual (`bd-49f-* -> {firm}-*`); threaded
   firm_aliases through `_compute_variances` (+ 2-pass OVER-MERGE guard: distinct-real-ARN intra-firm
   collision -> revert to value-only key, never guess the twin) + `load_one_variance` (over-generated sibling
   candidates since the lossy forward key can't be naively inverted; mirror ambiguity guard) + 2 call sites.
4. **Governed catalog (variance_dimensions.yaml + deliverable mirror):** added `firm_aliases` map, all 3
   firms (complete, not a 49f hand-patch). Updated my contract deliverable §2.2 for parity.

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| comp-grep | locate `_position_key`, `firm_names`, alias declarations, callers, served consumers | PASS -- pinned summary_corpus.py:518 + variance_dimensions.yaml + .tools/comp-secrets:58 alias set |
| comp-kuzu | live grounding: etf-ownership-daily names, estate-wide alias census, bd- collision check | PASS -- bd/cot/inf 3 node types confirmed; cottonwood/inflection NEVER infra-infix; ZERO over-merge collisions |
| comp-describe | exercise --describe path re-verdict (both variance paths agree) | PASS -- bd=Canonical 3-way, inf=Twin, cot=Fork-Shadow (real a-event divergence) |
| summary_corpus --self-test | offline mutants + new alias/over-merge tests | PASS 10/10 (M10j = alias-3way + over-merge guard) |
| summary_corpus --build | live re-verdict on the 07-19 graph | PASS -- verdicts 46->50, fork-shadows 5->4 |
| py_compile + ruff py39 | commit-gate pre-check | PASS (clean) |

**What worked:** ground-before-design -- the alias census turned a potentially broad "strip aliases" change
into the TIGHT "strip redundant alias adjacent to a matched value token" (firm still value-keyed, nothing
newly firm-keyed), which is the over-merge-safe + firm-sep-safe reading. Exercising BOTH variance paths
(build + describe) caught that the --describe sibling reconstruction is lossy-inverse and needed
over-generated candidates. **What failed:** nothing. **Gap:** the full --build re-run is ~2min (timed out
once on a re-invoke); the single exercise + targeted describes sufficed.

## Verification (exercised, not read -- Rule 22a)
- self-test 10/10 incl. `posn-key+alias` + `alias-3way+overmerge-guard`.
- LIVE --describe: `bd-49f-etf-ownership-daily -> canonical firm-twin (reference) of cot/inf`; inf -> Twin
  (C2 [a-access,a-grant] == bd = modal); cot -> Fork-Shadow (C2 [a-access,a-event,a-grant] -- GENUINE
  divergence: its cot-etf-ownership-daily-schedule EventBridge trigger). IAM_ROLE class identical 3-way.
- Blast radius CONTAINED: bd-49f-runner/keepalive/fees remain singletons (no spurious grouping).
- served-leak: variance output consumed ONLY inside summary_corpus.py (comp-grep) -- no served consumer.

## Blockers
BLOCKED-GATE (legitimate hard external gate, not idle): fix COMPLETE + verified, HELD uncommitted in the
working tree, submitted to CTO for the arch-gate GO (183913Z) before push -- firm-sep-adjacent + governed
artifact, not self-authorizable (SCOPE#5). Not a coast-failure: scope is bounded to this fix (MSTR/launcher
scope guard); no other in-scope task to drive. Monitor b7d237uh1 armed for CTO's reply -> act same-turn.

## Current State
- summary_corpus.py + variance_dimensions.yaml (+ deliverable mirror + contract doc) MODIFIED, UNCOMMITTED
  (held for CTO GO). Full diff: scratchpad/position_key_firmalias_fix.diff (302 lines). Same shared repo, so
  CTO reviews via `git diff org/modules/graph/debtscan/summary_corpus.py org/modules/graph/variance_dimensions.yaml`.
- All 3 CTO conditions satisfied + grounded (complete map / over-merge guard / no served-leak).
- DEFERRED (surfaced to CTO, NOT self-authorized): standalone-alias / fused bd49f / case-insensitive widen
  -- singleton-only in the estate (zero verdict impact today); CTO's widen-call.

## Next Steps
1. **[1.0.0_SA_CTO]** arch-gate GO on the held diff (or the widen ruling). On GO I safe-commit + push +
   tag-none (comp-tool code, no Lambda) + ping COO + ~D + CVO.
2. **[0.8.0_AE_CloudComp~D]** on my land: pull + re-run comp-describe/--build to confirm the 3-way re-verdict
   (you offered); rebuild engine-supersede on the corrected keying.
3. **[3.0.0_SA_CVO]** semantic-axis re-verify: fork-shadow 5->4, the surviving cot fork-shadow is now a real
   3-way-majority divergence (a-event), not a keying artifact.
