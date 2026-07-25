# comp-iam investigate-candidates: RoleLastUsed triage — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE, VALIDATE

## Objective

CTO~Z dispatched a new, modest tool (@133907Z) after CVO~Z killed the original framing
(RoleLastUsed as positive evidence licensing least-privilege deletion — wrong, since it's a
ROLE-grain signal and cleanup is an ACTION-grain question). Corrected scope: license exactly
ONE inference, "this role warrants human investigation," with the noun itself as the control
(`INVESTIGATE-CANDIDATE`, never `UNUSED`/`stale`).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| WebFetch | AWS IAM API Reference (`API_RoleLastUsed.html`) | grounded: null = "not used within the tracking period," not "never used" | live-fetched, not recalled |
| WebFetch | AWS IAM User Guide (`access_policies_access-advisor.html`, `id_roles_manage_delete.html`) | grounded: 400-day tracking window; console phrase "Not accessed in the tracking period" | 2nd source confirms the 1st |
| `bash .tools/aws iam list-roles --query RoleLastUsed` vs `get-role` | positive-controlled same-role comparison | `list-roles` returns null UNCONDITIONALLY; `get-role` returns the real value | measured live, this account, not assumed — settles the "no bulk shortcut" design decision |
| `python3 -m py_compile` | `comp_iam_investigate.py`, `iam_cli.py` | PASS | |
| `bash .tools/comp-iam investigate-candidates` | 6 real roles in one run | all 3 states (ACTIVE/UNKNOWN/AGED) rendered distinctly | acceptance (a), all on live data |
| grep, whole-word case-insensitive | full command output | `\bunused\b\|\bunused-role\b\|\bstale\b`: ZERO occurrences | acceptance (b) — required rewriting the refusal line to avoid the words even in negated form |
| ad-hoc DR-exemption test | synthetic exemption file, `load_dr_exempt(path=...)` override | exempt role still renders its real verdict, tagged exempt, never hidden; missing-file case degrades to empty set, disclosed | acceptance (d) |
| `bash .tools/comp-iam census-self-test` / `simulate-self-test` | regression | all pass | |
| `python3 -m pytest org/modules/graph/tests/test_iam_census_vintage.py` | regression | 10/10 pass | acceptance (e) |
| `bash .tools/comp-iam service .../gaps/roles` | cross-command regression | 7/7, clean | new module is additive-only |
| `.tools/commit-gate.sh` (via safe-commit) | ruff | caught 1 real lint defect (f-string with no placeholders) before it landed | fixed immediately |

**What worked:** grounding the region-semantics question via 2 live AWS doc fetches instead of
recalling it — the API schema itself (one `RoleLastUsed` object per role, not a per-region
list) settled the question structurally, independent of prose.
**What failed:** first draft of the refusal line used "not UNUSED" (negated) — correct in
meaning, but a literal grep for the forbidden noun cannot distinguish assertion from negation,
so acceptance (b)'s "prove zero occurrences" would have failed on my own deliverable. Caught
and rewritten before commit, not after CVO~Z's verify.
**Gap found:** the DR-exemption seed file (`iam_dr_exempt_roles.json`) hit an `.owned-paths.yaml`
lane boundary I don't hold (`ANY_EXEC`, exec-only — JSON/config files under
`org/modules/graph/` default to exec-locked where `.py` comp-tool code is opened to my lane).
Left on disk, not committed; disclosed below, not routed around.

## Work Completed

New module `comp_iam_investigate.py`: `get_role_last_used()` (one `get-role` call per role,
`.tools/aws` shim resolution matching `comp_iam_census.py`'s precedent), `classify()` (three
distinct states: ACTIVE / INVESTIGATE-CANDIDATE-UNKNOWN / INVESTIGATE-CANDIDATE-AGED, never
collapsing), `load_dr_exempt()` (declared-once exemption file, missing-file-safe), and
`REFUSAL_LINE` (printed unconditionally). New CLI subcommand `comp-iam investigate-candidates`
(`--role` repeatable, defaults to sweeping all TF-parsed roles; `--stale-days`, default 90,
disclosed as a judgment call distinct from AWS's documented 400-day tracking window).

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/comp_iam_investigate.py` | new module |
| `org/modules/graph/iam_cli.py` | new import, `cmd_investigate_candidates`, argparse subcommand + dispatch |
| `org/modules/graph/iam_dr_exempt_roles.json` | new seed file, **NOT COMMITTED** — `.owned-paths.yaml` lane boundary (`ANY_EXEC`), left on disk for exec commit |

Self-committed: `1a857e488` (the two `.py` files only).

## Blockers

The DR-exemption JSON file could not be self-committed — genuine, correctly-functioning
governance boundary, not a defect. The tool functions correctly without it committed (missing
file degrades to an empty exemption set, disclosed in its own output), so this is not
load-bearing for the tool's correctness, only for making the seed file a durable, reviewable
artifact rather than untracked local state.

## Current State

`comp-iam investigate-candidates` is live and verified end-to-end against real AWS data (6
real roles, all 3 states, zero forbidden-noun occurrences, DR-exemption honored). Awaiting
CVO~Z's verify per the dispatch's routing.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Either commit `org/modules/graph/iam_dr_exempt_roles.json` (currently
   on disk, empty/seed content, documented) under exec authority, or grant the appropriate
   lane if this class of file should be AE-editable going forward — your call, not mine to
   route around.
2. **[3.0.0_SA_CVO~Z]** Verify — the region-semantics grounding and the forbidden-noun
   grep-zero claim are the two highest-value items to independently re-derive.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
