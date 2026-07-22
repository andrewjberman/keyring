# comp-constants file->lane + the sovereign-hold retraction: 5 landed commits, 1 wave blocked on ownership

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE

Session 2026-07-22 ~13:47Z -> ~15:35Z. Serial `0.8.0_AE_CloudComp` (base). Two bounded comp-tool items
from COO (CTO-backed, MSTR governance weight); both closed, and each opened something larger.

## Window summary

| # | Commit | What |
|---|---|---|
| 1 | `9cfb2706f` | comp-constants file->lane resolution (unblocks DE) + CC2 sovereign guard lifted |
| 2 | `64fca8486` | a REFUSE is non-empty on stdout, not stderr-only |
| 3 | `3e31dc93d` | collection fix: `org/modules/graph/tests/` 0 tests -> 569 after 8 dark days |
| 4 | `c1bfbf781` | comp-which test harness reports the FAILURE instead of a parse error |
| - | BLOCKED | predicate-split wave: BUILT, 90/90 green, gate-clean, owned-paths refuses my author line |

MCP: ~14 messages. Significant: MSTR item-2 governance brief (in), sweep ACCEPTED @0590215d6 /
@e2ce238f6 / @9c26ef478 (LD-0330 8.20-8.22), CTO GO on the wave, CTO scope-ruling cascade via COO
(carve-out 2 names my work as CONTINUING), DE independent verification + @8a7208a70, COO RAVC close
on both items, COO correction-accepted.

## ITEM 1 -- a new firm was structurally unrepresentable

MECHANISM (source-confirmed, `comp_constants_cli.py:307` pre-fix): a `--file` target outside every
`search_surfaces` glob resolved to lane `None`, and cmd_check fanned its sites against EVERY lane's
canonical. With FIRM_ID in bd/inf/cot, any file necessarily drifted from the two firms it is not.
COO's cot-lane seed was necessary and insufficient -- her "still DRIFT 2 sites" measurement is what
proved a seed alone could not fix it.

FIX: per-file lane resolution (search_surfaces membership, else an explicit `file_lanes:` declaration);
fan-out deleted; unresolved files REPORTED, never compared. Shared trees get per-FILE declarations --
a directory rule over `data/assets/scripts/gold/` would silently re-home one firm's producer under
another firm's canonical.

DENOMINATOR MEASURED, and it turned a bug into a class: **57 files estate-wide** define a tracked
constant and sit outside every surface (incl. `infra/aws/lambda/inf-client-detail/lambda_function.py`).
Every one would hit DE's wall on its next commit. Hence LOUD-BUT-NON-BLOCKING on unresolved: blocking
57 wedges the commit gate, silence reports unchecked as clean. Notice goes to STDERR because
`commit_gate_runner._comp_constants_check` captures stdout and prints it only when rc != 0.

ACCEPTANCE (exercised on the REAL gate): commit-gate PASSES on DE's producer, FIRM_ID unrenamed,
bd/inf canonicals untouched -- it passes BECAUSE IT WAS CHECKED. Mutants: cottonwood->inflection
DRIFT rc=1; cottonwood->cottonwood_capital DRIFT rc=1.

## ITEM 2 -- a retracted sovereign hold, still enforcing 8 days on

Andrew LIFTED the 2026-07-09 bd/49F/Schwab hold COMPLETELY on 2026-07-14. The comp-constants CC2
guard kept enforcing it, refusing EVERY full-scan mode (bare check, --lane any, new, index) for ALL
lanes -- bd's 12 and inf's 11 constants had no drift gate, index/new dead. Only `check --file`
survived, which is why the commit gate kept working and nobody noticed.

SWEEP (denominator stated): comp-grep, 11,031 files scanned, 34 hits, 6 enforcing copies. `_comprail.py`
was already lifted 07-14 by CTO -- and its own comment names "the comp-constants CC2 guard" as its
mirror. The retraction stopped at the sibling its own documentation pointed to.

WHAT THE DEAD WINDOW LET THROUGH: **ZERO**. 7 real inf drifts exist, but git blame dates all 7 to
2026-04-28..05-11 -- months before the hold. Dated before attributed. Routed to DS via CTO.
`INFLECTION_REP_IDS` missing rep_id=6 is the founding ADHC_COMPIL_V4 incident, still live in 5 sites.

## The three things that were bigger than the items

**(a) The suite was dark.** `test_comp_system_metrics.py` (a standalone script with a `test_` prefix)
raised SystemExit at COLLECTION, aborting the entire `org/modules/graph/tests/` collection since
2026-07-14. Not "some tests failed" -- **no tests ran**, in CI and locally, for 8 days. Grounded on
two independent channels (CI log run 29929730773 naming `:114`; local same directory). Guarded ->
569 collected (CI 540 pass / 29 red; local 599 pass / 26 red -- the sets differ by quarantine and
environment and are NOT averaged).

**(b) The ratchet.** 18 tests across 6 files asserted the hold was ARMED -- 4x what the sweep or the
plan estimated. A test asserting a prohibition enforces it on whoever tries to REMOVE it: the lift
empties the tuple, tests go red, the red reads as "the lift broke something", and the cheapest repair
is to put the hold back. That is why this hold survived two retractions.

**(c) I corrected my own accepted finding.** I reported `_comprail` as "site 6, DONE" and called it
the model. True of the CODE, false of its TESTS -- 4 red since 07-14. My sweep denominator was
"enforcing copies in SOURCE" and silently excluded tests, which are enforcing copies with teeth. An
honest denominator over the wrong population.

## Traps I hit MYSELF (all caught, all banked)

1. **A mutant that did not mutate.** sed'd `'cottonwood'` against a double-quoted file; the check
   returned 0 and my run was formatted to read "expect 1 = still bites". Caught only by printing the
   line back. Both mutants now assert the sha256 CHANGED before any verdict is trusted.
2. **An arming fixture that armed the wrong module.** Consumers do `from sovereign_held import
   is_held_path`; that function resolves its tuple from the module it was DEFINED in, so patching a
   separately-imported copy changes nothing the code under test sees. Failed loudly; written the
   other way round it would have silently exercised an UNARMED hold and PASSED.
3. **A dropped `return` while refactoring** `_refuse()` made every `check --file` refuse whenever any
   surface was held -- strictly worse than the bug being fixed. `test_check_file_non_held_is_allowed`
   caught it immediately.

## Blockers

**BLOCKED (evidence-cited): predicate-split wave cannot land under my author line.**
`.tools/safe-commit.sh` -> owned-paths lane violation, BLOCK mode, on
`org/modules/graph/sovereign_held.py` and `org/modules/graph/clobber_scan.py` -- lane=ANY_EXEC
(CTO/COO/CVO/CRO only); agent=0.8.0_AE_CloudComp not permitted. CTO's GO is NOT missing. `--force`
exists and is audited; NOT USED -- staying blocked on an ownership gate on the sovereign leaf is
correct on the day we proved this hold cannot be half-handled. COO backed this explicitly and routed
to CTO recommending he land the ready tree under his own line. 13 files intact and UNSTAGED (safe-commit
left them staged on the block -- the documented sweep hazard).

SEAM: the GO and the path grant are separate systems with nothing reconciling them, so an exec can
approve a plan its assignee is structurally unable to execute and neither finds out until the commit.
Gate candidate (recorded by COO under my name, scoped to the advisory, deliberately NOT bolted onto
this wave): check the assignee's serial against owned-paths at TO/GO authoring time.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-constants | `check --lane cot` / `--lane bd|inf|multifirm` / `check` / `--file <n>` | PASS + real FAILs | Reproduced the rc=3 refusal, then restored all full-scan modes; `--lane inf` correctly rc=1 on 7 pre-existing drifts |
| comp-grep | sovereign_held / comp-constants caller sweeps | PASS | 11,031 files scanned; the denominator cited in the Item-2 sweep |
| comp-which | `--json --route-only` (direct, + cold-cwd) | PASS | rc=0, VALID JSON -- the check that refuted "the Rule-21 router is down" |
| commit-gate | 13-file wave + each landed commit | PASS | caught 2 ruff errors in my own patches (E401/E402) |
| comp-surface-check / comp-pulse / comp-system | auto via safe-commit | PASS | risk-reflex REFLEX CLEAN, denominator 1239 danger nodes |

**What worked:** comp-grep's denominator line is what made the sweep reportable as coverage rather
than a list. comp-constants' own `--file` disambiguation (CC1) is what let me tell "checked, clean"
from "nothing to check" while designing the UNRESOLVED state.
**What failed:** comp-grep silently returned `0 matches` for a BRE-style `\|` alternation -- it WARNED
clearly, which is the only reason I did not read 0 as absence. Good instrument behaviour, noted as a
positive.
**Gap found (2, both filed):**
1. **comp-constants has no exempt/deliberate/ratified field** (CTO instructed this be backlogged with
   his framing): a ratified divergence cannot be expressed, so it is re-reported forever -- which is
   how a real gate becomes noise people scroll past. The 7 inf drifts may include such cases.
2. **`git log --since=<absolute datetime>` compares LOCAL time and this host is UTC-4.** The /log
   skill's own gathering command returned 0 commits for a window in which I had made 4 -- I passed a
   UTC-derived `13:00` against commits stamped 10:18-11:30 local. CTO banked the SYMPTOM at
   `a2b1746d0` ("returns 0 across all authors"); this is the mechanism. Same 4-hour class as the
   banked `aws s3 ls prints local time` lesson. **Workaround: relative windows (`--since='13 hours
   ago'` returned 4) or an explicit `--date`.** A 0-result from this flag is not evidence of no work.

## Files Modified

See commit messages: `9cfb2706f`, `64fca8486`, `3e31dc93d`, `c1bfbf781` (each carries per-file detail).
Uncommitted (the blocked wave, 13 files): `sovereign_held.py` (+ vendored mirror), `tool_probe.py`,
`tool_corpus.py`, `clobber_scan.py`, `comp_constants_cli.py`, and 8 test files.

## Current State

- **comp-constants is healthy.** `check --file` and every full-scan mode work. `comp-constants.config.yaml`
  gained `file_lanes:` (cot -> `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`) and an
  optional `sovereign_held_markers:` re-arm surface. DE unblocked and committed @8a7208a70.
- **The comp-tool suite RUNS.** CI collects 569. It is still red (29 CI / 26 local) and that redness
  is now honest; 18 of the CI reds were the comp-which harness mis-reporting empty stdout as invalid
  JSON, fixed @c1bfbf781 -- the next CI run will print the REAL cause, which remains UNKNOWN and
  ungrounded (Rule 22; I am not guessing at it).
- **The predicate split is BUILT but UNLANDED**, sitting unstaged in the working tree. Leaf splits
  `SOVEREIGN_HELD_*` (= (), retracted; HELD_* back-compat aliases) from `PROD_TARGET_FORBIDDEN_*` (in
  force) + `RETRACTED_20260709_*` (re-arm) + new `is_prod_target_forbidden()`. All ~16 importers
  classified at source: 12 governance -> lifted; only `compproof/tool_probe.py` + `tool_corpus.py`
  guard probe write/scratch/ARN targets -> preserved. Commit body ready at
  `<scratchpad>/cc_wave.txt` for `safe-commit -F`.
- **One divergence from CTO's ruling, flagged not buried:** he directed `_KUZU_HELD_MARKERS` be
  converted to the prod-write predicate; source says it refuses a probe QUERY that left its designed
  inf/cot/mdpf scope -- neither governance nor a write guard. Renamed `_KUZU_OUT_OF_SCOPE_MARKERS`,
  re-justified as PROBE-SCOPE, kept ARMED. Overrulable.
- **6 CI reds UNDIAGNOSED** (routes_unresolved x2, failure_class_hardening x2,
  tool_graph_coupling_diff, iam_resource_verdicts). Stated, not guessed at. CTO: route when the wave lands.
- Off the MDPF hold path entirely (COO carve-out 2): zero MDPF data, pin, serve path, AWS, or TF.

## Next Steps

- **[1.0.0_SA_CTO]** land the 13-file wave under his author line (COO's recommendation) OR have an
  exec author a two-path owned-paths grant. SoD: I must not author a grant to myself. Sites 1+2 MUST
  be one commit (byte-identity test).
- **[1.0.0_SA_CTO]** rule on the `_KUZU_OUT_OF_SCOPE_MARKERS` classification divergence.
- **[0.4.0_DS_ClientPlatform]** the 7 pre-existing inf drifts (INFLECTION_REP_IDS x5 + GUARD_B_AUA
  bounds), routed by CTO; rep_id=6 prioritised.
- **[0.8.0_AE_CloudComp]** post-wave: the 6 undiagnosed CI reds; the CRO `liveness.json` item
  (mechanism UNKNOWN -- ground it before touching the identity guard, per CTO + COO); the
  comp-constants exempt/ratified backlog entry.
- **[unowned]** `data/assets/scripts/gold/cottonwood_aua.py:63-67` -- a prior agent took the rename
  escape DE refused (FIRM_ID -> COT_SCOPE), putting a live firm constant permanently outside the
  drift instrument; its justifying comment is factually stale. COO routing to CTO for an owner,
  queued to DE (his tree, mid-re-home).
