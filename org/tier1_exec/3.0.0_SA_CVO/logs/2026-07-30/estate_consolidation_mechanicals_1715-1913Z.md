# 3.0.0_SA_CVO -- comp-estate naming consolidation + adjudication drift fixes + mechanicals pass (2026-07-30 17:15Z -> 19:13Z)

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, IMPLEMENT, SCRIBE

## Summary

Andrew-direct continuation of the 1714Z handoff thread. (1) Reinstantiation: context-clear
discriminated correctly (same PID 30716 -> watcher is MINE, round-trip [INBOX] self-test proved a
live consumer -- no kill, no re-arm; the MSTR 07-16 false-positive shape avoided). LD-0354 fabric
halt release ACKed to MSTR; the 07-29 2350Z brief-wait ruled non-binding (Andrew re-engaged
directly). (2) Adjudication + comp-estate review produced findings F1-F5; Andrew ordered the fixes
plus a naming consolidation. All landed: canon C3.ii fold, fam2sys view-compile, engine renamed
opal_estate_infrastructure.py + legacy CLI renamed estate_infrastructure_cli.py (Andrew mid-turn:
"extremely important we try to stay consolidated/canonical with naming"), comp-semantic-estates +
comp-opalbizsem DELETED per their own delete-together conditions, every live reference re-pointed
(CLAUDE.md:71 under Andrew's law-surface word), two commit-gate members made DELETION-AWARE (a
delete-together retirement was structurally uncommittable), comp-lambdamap given curated routing
vocabulary (latent self-route MISS, present at HEAD too -- verified against a git-show copy).
(3) Mechanicals pass: 18-mode wall-clock + volume harness, SIGPIPE probe, heavy-registry review
that found a DUPLICATE tools_index KEY (silent last-wins override) + 4 more classification
defects -- all trued and committed. Design note for the tool-wide head/pagination solution
recorded below (PROPOSED; walk-through with Andrew is the next agenda item).

## Work (evidence = commits)

- @29c3fedeb8 (mine, 24 files): consolidation + drift fixes + gate fixes. Per-item detail in the
  commit message (items 1-7).
- @296ce15db5 (1.0.0_SA_CTO): my two ANY_CTO doc re-points (USEPATHS, TWO_FABRIC) landed verbatim
  under CTO author after the owned-paths hook correctly refused my serial. Gate-fix owner-review
  QUEUED at CTO (revert-first discipline if the gate regresses).
- @b38d005b08 (mine, 5 files): heavy-registry truing -- duplicate comp-estate tools_index key
  merged to one canonical row (20 subcommands, was 5); entry ids renamed off dead tool names
  (estate.thread.traversal + estate.ontology.views -- the ontology views had NO classification
  row); classifications trued to measurement; frozen digits 25/134/169 -> live-derivation phrasing
  @ 2026-07-30 vintage (29/138/188); TOOL_MASTER.yaml + tool_index.py REGENERATED (tool_index is
  GENERATED/DO-NOT-EDIT -- my earlier hand-edit of its embedded corpus copy was wrong-layer,
  subsumed by regen); comp-system 06 refolded.

## Mechanicals measurements (raw table -- durable home is THIS log; registry carries the summary)

| mode | rc | wall_ms | lines | stdout_B |
|---|---|---|---|---|
| --list | 0 | 116 | 37 | 2602 |
| flagship smartx | 0 | 112 | 51 | 5580 |
| flagship news | 0 | 301 | 158 | 14272 |
| flagship advi-bd | 0 | 127 | 202 | 16544 |
| --resource mdpf | 0 | 137 | 3 | 213 |
| --segments | 0 | 165 | 80 | 6730 |
| --layers | 0 | 134 | 102 | 6647 |
| --definitions (all) | 0 | 153 | 32 | 4144 |
| --definitions estate | 0 | 132 | 11 | 750 |
| --matrix | 0 | 190 | 51 | 3676 |
| --debt | 0 | 365 | 49 | 2377 |
| --fe-reachability | 0 | 120 | 147 | 9934 |
| --validate | 0 | 122 | 10 | 501 |
| --gate-b | 0 | 232 | 35 | 2324 |
| --census-drift | 0 | 1237 | 52 | 1799 |
| --self-test | 0 | 24720 | 16 | 1162 |
| bare | 0 | 103 | 38 | 951 |
| --drift | 0 | 24917 | 48 | 2914 |

SIGPIPE probe (reader closes after 5 lines): --list and --debt both rc=0, 0 stderr bytes, CLEAN --
no BrokenPipe traceback spew. Max output 16.5KB/202 lines: volume is NOT the truncation hazard;
verdict-at-the-bottom placement is (a piped head cut eats the verdict/denominator lines).

## DESIGN NOTE -- tool-wide head/pagination (status: PROPOSED, Andrew walk-through next)

Problem (Andrew-named): truncated results give agents a truncated worldview that manifests as
neurotic error reporting. Measured shape of the risk: comp-estate outputs are small (<=16.5KB) and
SIGPIPE-clean, but EVERY mode prints its verdict + denominator LAST (gate-b RESULT line,
census-drift routing note, drift summary) -- so a unix `| head -N` removes exactly the lines that
prevent the spiral. The hazard is not volume; it is that naive truncation is verdict-destroying
and silent.

Proposed design, three commitments:
1. NATIVE `--head N` flag: emit the first N BODY lines only, then a mandatory self-declaring
   marker -- `[TRUNCATED --head: showing N of M body lines; verdict/denominator follow]` -- then
   ALWAYS the mode's verdict/denominator footer. Truncate the middle, never the verdict; the
   denominator survives every cut; the truncation names itself (no silent worldview shrink).
2. REFERENCE IMPLEMENTATION in comp-estate (same rollout pattern as the source-timestamp header
   contract, which also debuted there), as a small stdout-shaping helper so every mode gets it
   uniformly rather than per-mode hand-wiring.
3. CONTRACT-IZE in comp-output-contracts.yaml as a declared convention; roll to other comp-tools
   as they are touched. Unix head stays available, but the native flag is what agents are taught,
   because it is the only form that structurally cannot cut the denominator.

Open design questions for the walk-through: default N when --head given bare; whether --json modes
are exempt (structured output should never be truncated mid-object); whether the marker line also
belongs in stderr for pipe-survivability; pagination (--offset) or head-only.

## Compiler Tools

| Tool | Runs | Result | Note |
|---|---|---|---|
| comp-estate | ~30 | PASS | full battery pre+post every change: self-test 5/5, gate-b 29/29, matrix byte-identical post-fam2sys-refactor, segments/census-drift live; 18-mode harness above |
| comp-manifest-check | ~8 | PASS after 2 gate fixes + 1 cure | completeness BLOCKED x3 en route: comp-lambdamap latent MISS (cured w/ curated vocab; verified pre-existing at HEAD), placement + registration members not deletion-aware (fixed, owner-review queued at CTO); final PASS 70 tools |
| comp-which | ~6 | PASS | routing exercises pre/post re-point; gate does-query tested against HEAD copy via git show (stash BLOCKED by never-rules gate -- correctly; used the non-mutating path) |
| comp-system | 2 | PASS | ledger_union_count 93->91 regen folded; second run spans-current |
| comp-pulse / commit-gate / coverage-check | auto | PASS | advisory manifest findings read; coverage-check 91 homed post-row-deletions |
| gen_tool_registry.py | 1 | PASS | tool_index.py + TOOL_MASTER regenerated from corrected sources |

What worked: exercise-don't-read caught the duplicate tools_index key (yaml.safe_load last-wins
silent override) and the latent comp-lambdamap MISS; the never-rules gate correctly blocked my
git-stash baseline attempt in the shared worktree (used git show instead). What failed: I
hand-edited GENERATED tool_index.py before noticing its DO-NOT-EDIT header -- wrong layer, caught
and subsumed via regen; and my first commit attempt's failure path mangled staging (renames split,
deletions unstaged) -- recovered by re-running the wrapper with the full pathspec. Gap found: the
two commit-gate members' universes were not deletion-aware (fixed, see above).

## MCP traffic

~5 significant. Received: MSTR LD-0354 halt-release (ACKed; brief-wait ruled non-binding with
grounds); CTO doc-landing + gate-fix-queued confirmation @296ce15db5. Sent: MSTR ACK; CTO
two-item route (doc edits + gate-fix owner-review flag).

## Files Modified

See commit messages @29c3fedeb8 (24 files incl. 2 renames + 2 deletions) and @b38d005b08 (5
files). CTO landed docs/architecture/{NFRA_COMPTOOL_USEPATHS,TWO_FABRIC_OPERATIONS_AND_GATES}.md
@296ce15db5.

## Blockers

None at me. CTO's gate-fix review is queued in their post-census block (their lane, revert-first).

## Current State (zero-context handoff surface)

- comp-estate is THE canonical name estate-wide; old names (pipescript, comp-semantic-estates,
  comp-opalbizsem) do not resolve (executables deleted, ~/bin deprovisioned, negative controls
  exercised). Engine org/modules/graph/opal_estate_infrastructure.py; delegated legacy
  thread-model engine org/modules/graph/estate_infrastructure_cli.py (owned-paths key followed
  the rename, same NFRA_PIPESCRIPT_TOOL lane; owner = AE per Andrew-direct 2026-06-23, stale DS
  labels corrected with citation).
- Canon: NFRA_ONTOLOGY_C2C3_CANONICAL.yaml carries the folded adjudication (29 verticals, +3
  entries, residue 8 chains/7 verticals, causality RETIREMENT-PENDING w/ WS-E3 teardown);
  cmd_matrix view-compiles fam2sys from the catalog (collision-guarded); LAYERS.md v1.3.
- Heavy registry: single comp-estate tools_index row (20 subcommands), entries
  estate.thread.traversal + estate.ontology.views, classifications measurement-trued.
- Standing worklists unchanged: census regeneration (14 UNMODELED / 33 CENSUS-ONLY + family
  encoding normalization), 70/70 self-route WARN grounding (task #6), tasks #5/#7, tool-walk
  2/93 on Andrew's word.
- NEXT AGENDA (Andrew-set): walk through the head/pagination design note above.

## Next Steps

1. [3.0.0_SA_CVO + Andrew] Pagination design walk-through -> build decision on the reference
   implementation in comp-estate.
2. [1.0.0_SA_CTO] Deletion-aware gate-fix review (queued, their post-census block).
3. [3.0.0_SA_CVO] Standing: tasks #5/#6/#7, census-regen worklist, tool-walk 2/93 on the word.
