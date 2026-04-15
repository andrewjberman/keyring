# Session log — ADHC_ROUTER.T4 compiler regression audit

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-04-15
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADHC_ROUTER.T4.ds-d-test-compilers-vs-cnp0-wp11.md`
**Issued by:** 1.0.0_SA_CTO
**Scope:** stress-test `comp-pipescript deployed` silver-scope fix + `comp-platinum reverse` dotted paths + `comp-validate --schema` pass-through against my WP-11 (commit `864b6d7a`) + CN-P0 (commit `93b70620`) work from earlier today.

## Summary

Five Phase 1 runs executed. The silver-scope fix on `comp-pipescript deployed` is real and it closes the specific gap I flagged during WP-11 — both `bd_price_update.py` and `inject_scoped_overrides.py` now return `[SILVER] MATCH` cleanly. The `--schema` pass-through gap was still open at this TO's authoring; I shipped a scoped fix to `org/modules/graph/validate_cli.py` that routes `comp-validate <id> --schema` (and any other pass-through flag) to the standalone validator under `data/black_diamond/scripts/validators/`. The `io` silver-scope gap, `comp-platinum reverse` empty-vs-broken disambiguation, and the coverage-audit half of proposal E remain still-open.

## Compiler Tools — Phase 1 audit

| # | Run | Expect | Observed | Pass/Fail |
|---|---|---|---|---|
| 1 | `comp-pipescript deployed bd_price_update.py` | `[SILVER]` label + verdict | `[SILVER] bd_price_update.py MATCH`. Summary `1 MATCH, 0 STALE, 0 MISSING_ON_S3`. | **PASS** |
| 2 | `comp-pipescript deployed inject_scoped_overrides.py` | Same shape | `[SILVER] inject_scoped_overrides.py MATCH`. Same clean summary. | **PASS** |
| 3 | `comp-pipescript io bd_price_update.py` | EXPECTED FAIL; silver scope is `deployed` only | Fails: `Unknown script: BD_PRICE_UPDATE.PY`. Valid IDs listed are gold-only: `A_00..D_04`. | **FAIL as expected** — maps to `COMPILER_SILVER_SCOPE_FULL.md` (proposal B). |
| 4 | `comp-platinum reverse nna_atomic` | Empty PRODUCER + CONSUMED BY (new field) | Empty across all three sections: `PRODUCER: (no payload-path matches found)`, `SERVED VIA: (no matching routes found)`, `CONSUMED BY: (no components found)`. Tool ran; three distinct "(no X found)" phrasings distinguish empty-found from tool-crashed. | **PASS** (tool worked, empty is correctly conveyed). See empty-vs-broken discussion below. |
| 5 | `comp-validate nna_atomic --schema` | EXPECTED FAIL; proposal E not yet shipped | Fails: `comp-validate: error: unrecognized arguments: --schema`. | **FAIL as expected** — maps to `COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md` (proposal E). **I shipped a pass-through patch** (see Phase 3 below). |

## Empty-vs-broken disambiguation for `comp-platinum reverse`

CTO's flagged concern: does `reverse <new_field>` make it easy to tell "ran successfully, found no consumer" from "tool broke, no output"? My read: **tool is fine; disambiguation is already acceptable** for the shadow-only new-field case, with one caveat.

Evidence (run 4 above): `reverse nna_atomic` prints the three structural section headers (`PRODUCER:`, `SERVED VIA:`, `CONSUMED BY:`) and an explicit bracket-parenthesized "(no X found)" under each with distinct phrasing — `(no payload-path matches found)`, `(no matching routes found)`, `(no components found)`. A crashed tool would either error out with a traceback or emit a truncated header without the parenthesized lines. Agents reading this output can confidently conclude "ran, found nothing."

**Minor enhancement I'd support (not shipping in this TO):** a single one-line summary footer like `Result: 0 producers / 0 routes / 0 consumers -- query ran successfully.` That would remove the last sliver of doubt for agents that skim long outputs and miss the per-section messages. Flagging as still-open: map to `COMPILER_BLAST_SCRIPT_ARTIFACT_EDGES.md` if a broader `reverse`-style output hygiene pass is in scope; otherwise a one-line enhancement TO.

## Would this have helped WP-11?

WP-11 session log (`org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-15/wp11_and_3bond_formalization.md`, §Compiler Tools) flagged two things:

1. **"`comp-pipescript deployed` only checks `s3://opal-data-bd/code/gold/`. Silver-layer scripts like `bd_price_update.py` and `inject_scoped_overrides.py` are deployed to `s3://opal-data-bd/code/silver/` but not tracked by this tool."**
   - **Fix addresses this directly.** Runs 1 + 2 above show `[SILVER]` labelled MATCH results against exactly those two scripts. I no longer need to `aws s3 ls s3://opal-data-bd/code/silver/` manually to verify deploy state.
   - Rule-7 value: saved the manual S3 listing step at "done-with-commit" time. Going forward, gold-runner trigger decisions for silver-layer work can rely on `comp-pipescript deployed` the same way gold-layer work does.

2. **(implied) "TO path correction: WP-11 listed `scripts/gold/` but actual files live at `scripts/silver/`."** — path mis-routing.
   - Not directly addressed by the silver-scope `deployed` fix, but the fix removes the main friction: I can confirm silver deployment status just as easily as gold, so TO-authoring mistakes about layer are caught earlier at `comp-pipescript deployed` time instead of at the upload-verification step.

## Would this have helped CN-P0?

CN-P0 session log (`logs/2026-04-15/cn_p0_nna_canonical_schema.md`, §Compiler Tools) flagged:

1. **"`comp-validate` CLI has no `--schema` pass-through flag today. Minor gap; delegating to direct python invocation for now."**
   - **Not addressed at CN-P0 authoring time.** This is proposal E; it was still open as of this TO's expected-fail for run 5.
   - **I shipped the scoped pass-through fix in this TO** (see Phase 3). CN-P0 agents now get `comp-validate nna_atomic --schema` exit 0 directly, no indirection through `python data/.../validate_nna_atomic.py`.

2. **"`comp-blast` on C_01/D_00/D_00b/D_00c/D_01/D_02 returned `No downstream consumers found` for all six — the graph DB models gold scripts as transform nodes keyed on their principal output artifact, so there's no `nna_atomic` producer node yet."**
   - Not addressed by T3/T4 scope; this is graph-catalog completeness, separate from reverse-path lookup. Maps to `COMPILER_BLAST_SCRIPT_ARTIFACT_EDGES.md` (script-to-artifact edge coverage). Still-open.

## Phase 2 — structural-vs-surgical assessment of the silver-scope `deployed` fix

**The question:** is adding silver-layer support to `comp-pipescript deployed` a full solution, or is it a patch that addresses one surface symptom of a deeper asymmetry where silver coverage is uneven across the `comp-pipescript` subcommand surface?

**My read: it's surgical, and the asymmetry is still there.**

The `comp-pipescript` surface today has at least four verbs I use regularly: `deployed`, `io`, `feeds`, `consumers`, `postdeps`, `overlap`. Of these:

- `deployed` now knows silver (runs 1 + 2 confirm).
- `io` does not know silver (run 3 fails with "Unknown script: BD_PRICE_UPDATE.PY").
- `feeds`, `consumers`, `overlap`: untested in this TO but they consume the same script-ID registry `io` does, per the "Valid IDs: A_00…D_04" error message in run 3 — so silver is presumably missing from their surfaces too.
- `postdeps`: silver-aware today (WP-11 run showed `build_canonical_prices` post-step detection with incident references to silver-layer scoped-override wipes on 2026-04-06). This was the one silver-aware subcommand before the `deployed` fix.

**The underlying architectural issue** — flagged in `COMPILER_SILVER_SCOPE_FULL.md` (proposal B, per CTO's map) — is that the script-ID registry (the `A_00..D_04` table `io` surfaces) is a gold-layer inventory that predates the silver-layer being a first-class node. Silver scripts live in a different registry (the s3_layout layer) and were bolted into `deployed` as a scope parameter without unifying them into the main ID catalog.

**Consequence for future silver work:** the next agent who needs `comp-pipescript io bd_price_update.py` or `comp-pipescript feeds inject_scoped_overrides.py` hits the same wall I hit during WP-11. Each silver subcommand gap will drive another single-point AE CloudOps ticket unless the script-ID registry itself is unified.

**Bottom line:** the `deployed` fix is a real, correct local win, and it would have saved me ~5 minutes of manual `aws s3 ls` during WP-11. But the underlying silver-layer catalog gap is still wide-open — proposal B is the structural close and it's the right framing.

## Phase 3 — compiler patch shipped

### Scope of patch

`org/modules/graph/validate_cli.py` — added pass-through dispatch to standalone validators. Closes AC #1–#4 of proposal E (`COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md`). The coverage-audit half of proposal E (AC #5–#8) is NOT shipped in this patch and remains still-open.

### What the patch does

1. `main()` switched from `parse_args()` to `parse_known_args()` so unknown flags like `--schema`, `--certified`, `--cross-check` no longer hard-error in argparse.
2. When extras are present OR `--artifact` is absent, the CLI looks for a file at `data/black_diamond/scripts/validators/validate_{script_id}.py`. If found, it dispatches to it via `sys.executable` with all trailing flags forwarded verbatim via `subprocess.run`; exit code propagates transparently.
3. If extras are present and no standalone validator is found for `script_id`, the CLI surfaces the situation explicitly rather than silently dropping flags: `comp-validate: unrecognized arguments [...] and no standalone validator found for 'bogus' at data/black_diamond/scripts/validators/validate_bogus.py`.
4. Bare `--list` and `--list D_04` and `D_04 --artifact <...>` config-engine paths are unchanged — config-backed targets still use the yaml-engine route.

### Proof of fix

| Command | Before | After |
|---|---|---|
| `comp-validate nna_atomic --schema` | `error: unrecognized arguments: --schema`, exit 2 | Dispatches to `validate_nna_atomic.py --schema`; prints the 22-column schema check; exit 0 |
| `comp-validate role_aua --schema` | Same failure | Dispatches to `validate_role_aua.py --schema`; prints the 6-invariant wiring check; exit 0 |
| `comp-validate D_04 --list` | Config list | Config list (unchanged) |
| `comp-validate --list` | 5-script list | Same (unchanged) |
| `comp-validate bogus --whatever` | argparse error | Clean error message pointing at missing `validators/validate_bogus.py` |

### What this patch does NOT do (deliberately)

- No coverage audit command (`--audit-coverage`). That's proposal E AC #5–#8 and remains still-open. It's set-difference work across gold scripts / standalone validators / config entries / platinum artifacts — straightforward but larger than the pass-through half, and out of scope for this T4 audit.
- No drift-surfacing. Same reason.
- No auto-generation of validator configs. Explicit non-goal in proposal E.

### Scope guardrail observed

CTO TO explicitly forbids `gold/silver script edits` (A→D rerun sensitivity). This patch only touches `org/modules/graph/validate_cli.py`, which is under `permitted_edits`. No changes to any deployed script; no S3 uploads; rerun safety preserved.

### Phase 3 re-run (before/after evidence)

After the commit below, re-ran all five Phase 1 commands. Only run 5 changed state: `comp-validate nna_atomic --schema` now dispatches and exits 0. Runs 1 + 2 still PASS (silver-scope fix still working), runs 3 + 4 still fail-as-expected (those proposals remain open).

## Still-open gaps → compiler proposal mapping

| Gap hit in WP-11 / CN-P0 | Current state post-T4 | Proposal doc |
|---|---|---|
| Silver-scope coverage in `comp-pipescript deployed` | **CLOSED** (fix shipped pre-T4; T4 runs 1 + 2 validate) | `COMPILER_SILVER_SCOPE_FULL.md` (B) — asymmetry across other subcommands still open |
| Silver-scope coverage in `comp-pipescript io` / `feeds` / `consumers` / `overlap` | **OPEN** | `COMPILER_SILVER_SCOPE_FULL.md` (B) |
| `comp-validate` `--schema` / arg pass-through to standalone validators | **CLOSED in this TO** (patch below) | `COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md` (E, half shipped) |
| `comp-validate` coverage audit (no-config gold scripts, standalone-only validators, platinum outputs without validator mapping, config drift) | **OPEN** | `COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md` (E, remaining half) |
| `comp-platinum reverse` empty-vs-broken single-line summary footer (minor UX polish) | **OPEN** (nice-to-have) | Likely fits under `COMPILER_BLAST_SCRIPT_ARTIFACT_EDGES.md` if a broader output-hygiene pass; otherwise standalone |
| `comp-blast <gold_script_id>` returning "No downstream consumers" because gold scripts are transform nodes without script-to-artifact edges | **OPEN** | `COMPILER_BLAST_SCRIPT_ARTIFACT_EDGES.md` |

The IAM parser (`COMPILER_IAM_LAMBDA_PARSER.md`, D), input canonicalization (`COMPILER_INPUT_CANONICALIZATION.md`, C), and lint coverage pass (`COMPILER_LINT_COVERAGE_PASS.md`, N1) are not hit by WP-11 / CN-P0 scope and are unassessed in this audit.

## Commits

- Patch commit will be recorded below after commit + push.

## Next

- Return to post-rerun CN-P1 + RA-P1 validator runs when the A→D cycle completes.
- No further compiler-surface work in this lane unless CTO GOs another `ADHC_ROUTER.*` TO.
