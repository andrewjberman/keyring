# MDPF_COTTONWOOD.FIX1 -- Opal child attribution: gold fix landed, and the $0.00 delta that found the real blocker

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, DEPLOY

**Agent:** `0.4.0_DS_ClientPlatform` · **Window:** 2026-08-07 ~1650Z -> ~1815Z (session start -> now)
**TO:** `MDPF_COTTONWOOD.FIX1.opal-child-attribution` @03b975ac13, amended @505747e886 -- status stays `pending`
**Commit:** `75e379d6ae` (UNPUSHED -- lanes commit, integrators push)

---

## Summary

Spawned to implement the pinned Cottonwood filter-order fix (diagnosis AE~Z @924c3b669, semantics
ruled by Andrew via COO). Landed it, deployed it, verified it three ways -- **and its measured
delta on live data is `$0.00`, because a second filter of the same shape sits one layer upstream at
the bronze harvest and binds first.** Acceptance criterion 4 is therefore NOT met and cannot be met
by this TO. Reported as a finding rather than absorbed into a successful-fix narrative.

Two things were caught before they shipped, one in the TO and one in my own tests:

1. **The TO's original criterion 1 was wrong and I caught it before writing code.** It said "move
   the test from parent to child grain." That is the mirror of the overstatement trap it correctly
   warned about: leaf-only drops the non-Opal sleeves of Opal-named parents that attribute today
   -- **$779,478.54 across 3 live rows** -- moving a served number DOWN. I proposed the DISJUNCTION
   instead; COO verified at source and amended the TO @505747e886.
2. **My own `TRAP_3` test initially could not fail on the mutant it was named for.** Its fixture
   had no non-Opal sleeve, so it asserted "strictly additive" over a book with nothing to lose.
   Caught by running the mutant, not by reading the test.

---

## What I did

**The fix** (`data/assets/scripts/gold/build_dim_model_portfolio.py`): the strict Opal test moves
from the assigned PARENT strategy (`:277`, before the decomposition loop at `:287`) to a
disjunction evaluated at LEAF grain, in a new named function `attributes()`:

> a leaf attributes if **EITHER** the assigned strategy is Opal-named (pre-existing rule, unchanged)
> **OR** the leaf itself is an Opal model (Andrew-direct 2026-08-07).

Reuses the single child-level `is_opal` determination `dim` already carries (`rs.is_opal_name`)
rather than deriving a second Opal rule that could drift. No renormalization -- a non-Opal
remainder stays out and remains in `non_model`, a downstream balance. `opal_assigned_accounts` and
`opal_assigned_without_value` keep their ORIGINAL definitions so the PRD sec-5 roster tie cannot be
silently satisfied by the new population; the new population is reported in six new keys.

**Tests:** 26 pass (16 pre-existing + 10 new). Full mutation matrix run, because a green suite is
not evidence:

| mutant | meaning | caught by |
|---|---|---|
| control (real rule) | -- | **0 failures** |
| `parent-only` | the ORIGINAL DEFECT | 6 tests |
| `always-true` | filter deleted -> OVERSTATES | 8 tests |
| `leaf-only` | test moved not disjoined -> UNDERSTATES | 3 tests |

Also exercised: the PRD sec-5 tie still BREAKS under mutation of the roster's `account_count`,
proving the change did not turn the reconcile into a tautology.

**Deploy** (Rule 13, DS owns the full cycle): `safe-deploy.sh` -> `s3://opal-data-mdpf/code/scripts/assets_gold/`.

---

## The finding: the binding filter is UPSTREAM, at the bronze harvest

`infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py:303` @HEAD seeds the
model-detail harvest on **Opal-NAMED roster models only**. The transitive closure (`:316-319`) walks
children correctly but only DOWNWARD from a seed -- so a non-Opal-named parent is never fetched, its
Opal children never land in bronze, never become silver blend edges, and are structurally invisible
to gold. **Identical defect, one layer up.**

Measured 2026-08-07: roster **62** models | bronze `rebalancer_model_detail` objects **28** | silver
blend edges **33** | distinct non-Opal-named blend parents **0** | both Anna model_ids **ABSENT**
from bronze | blend children named `*fixed income*` **0**. `Anna *9237/*9238` ARE in roster and
assignment (2 live accounts) -- only their DETAILS were never pulled.
**Positive control on the ABSENT verdict:** the same search for Opal Satellite 70's id returns 1, so
the search discriminates and ABSENT is a measurement, not a broken retrieval.

`:31` records that scope as "Andrew-ruled, CTO-ratified", and the file is a **Lambda -- infra, not
the DS lane** (Rule 13). Surfaced to COO, not adjudicated, not touched. A supported switch exists
(`MODEL_DETAIL_SCOPE=all`, `:70`). Flagged that widening it also moves the harvest 28 -> 62 GETs/day
and re-baselines the `:26-29` assignment-reconcile ground truth ("296 Opal across 14 models"), which
is itself derived under the current scope.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | `--pipeline mdpf` | **FAIL** | "Unknown script" -- and `cot` too. **rc=0 anyway; the rc does not discriminate known from unknown.** Resolves only under `bd`/`inf` as `[assets-gold]`. The TO mandated `mdpf`, which cannot answer this file. |
| `comp-pipescript io` | `--pipeline bd` | PASS | I/O manifest: 4 monolith silver reads (roster/blend/assignment/holdings). WARN: no S3 constants detected -- dynamic keys. |
| `comp-blast` | `build_dim_model_portfolio` | **REFUSAL** | NOT-FOUND over a stated 20,603-node denominator + 5 corpus HOLD claims surfaced. Honest refusal, explicitly "not a nothing-breaks clear". |
| `comp-blast` | `decompose` | **REFUSAL** | AMBIGUOUS-SUBJECT, 6 candidate nodes, refused to guess. Correct behaviour. |
| `comp-find` | `dim_model_portfolio` | PASS | 435 hits / 24,852 files, banded. Located all 4 gold consumers + the deploy path. Used in place of the two comp-blast refusals. |
| `comp-find` | `rebalancer_model_detail` (`--band DEF`, `--band SURFACED`) | PASS | Located the bronze harvester Lambda -- the upstream finding. |
| `commit-gate.sh` | 2 files | PASS | py_compile + ds-precommit + ruff clean. |
| `safe-deploy.sh` | the gold producer | PASS | DEPLOYED + `comp-pipescript deployed` VERIFY OK / MATCH. |
| `comp-validate` | `build_dim_model_portfolio.py` | **NO CONFIG** | Script is not among the 21 in the BD validate config. **UNVALIDATED -- did NOT signal SAFE on it** (TO banked hazard). Evidence substituted: mutation matrix + live harness control. |
| `comp-pulse` (risk-reflex) | pre-commit, auto | CLEAN | 3 files vs 1,659 danger nodes; measured, not a default. |

**What worked:** `comp-find`'s banding + denominator carried the consumer census after comp-blast
refused twice -- the refusals were correct and the fallback was one call away. Both comp-blast
refusals were *honest*, which is worth more than a confident wrong answer.

**What failed:** `comp-pipescript io --pipeline mdpf` -- the TO's mandated invocation -- cannot
resolve this script, and returns **rc=0** while saying "Unknown script". An agent scripting on rc
would read that as success.

**Gaps found (routed to COO):** (a) `build_dim_model_portfolio.py` is unroutable under `mdpf`/`cot`
despite being the Cottonwood MDPF gold producer; (b) that UNKNOWN path exits 0; (c) no graph node
exists for this script, so `comp-blast` cannot answer change-safety on a client-facing producer;
(d) no `comp-validate` config for it.

---

## My own errors, recorded

1. **A false DIFFERS verdict from a broken retrieval.** My first deploy check wrote to `/tmp`, the
   `aws s3 cp` failed, and my comparator diffed an **empty** hash against a real one and printed
   `*** DIFFERS ***`. A retrieval failure returning a value -- the exact class CLAUDE.md names.
   Re-run with a size check and a non-empty precondition; it is IDENTICAL.
2. **`TRAP_3` could not fail on its own named mutant** until I put the sleeve in its fixture. The
   fixture comment now marks the sleeve load-bearing so it is not later deleted as decoration.

---

## Blockers

**BLOCKED (evidence-cited), not assumption-blocked:** acceptance criterion 4 ("Opal Fixed Income
must APPEAR in the gold dim") cannot be satisfied from the DS lane. Evidence: bronze holds 28 of 62
model details; both Anna ids absent (positive-controlled); 0 non-Opal-named blend parents in silver.
Remedy sits in `cot-rebalancer-runner` (infra lane) behind a recorded Andrew/CTO ruling.
**Owner: `2.0.0_SA_COO` to route.** TO left `pending`.

---

## Current State (zero-prior-context handoff)

- **Commit `75e379d6ae` on CLOUD, UNPUSHED** -- the only commit ahead of `origin/CLOUD`. **S3 is
  currently AHEAD of origin**; an integrator push is owed so the repo matches the deployed bytes.
- **Changed:** `data/assets/scripts/gold/build_dim_model_portfolio.py` (new `attributes()` at the
  module level, called from `build()`; 6 new report keys), its test file (+10 tests), and
  `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_COTTONWOOD_FIX1_BEFORE_AFTER_DELTA_20260807.md`.
- **Deployed:** `s3://opal-data-mdpf/code/scripts/assets_gold/build_dim_model_portfolio.py`,
  sha256 `e443330e1e4606ba2c8f7eb797d1c09c5cbb113d19dd1f10709f962974b691c3`, byte-identical to
  local on a confirmed non-empty 29,072B retrieval; new rule present at deployed `:275`; old
  parent-filter line absent (0 hits).
- **Pinned baseline for the next measurement:** Opal AUA **$134,113,436.27**, assignment date
  `2026-08-07`, value date `2026-08-05`, 10 dim rows. This is what the number should move FROM when
  the harvest scope widens.
- **09:00 ET fire:** nothing on Andrew's screen changes -- $0.00 across every row.
- **NOT claimed:** the `-1/-1/-1` residuals AE~Z flagged remain unexplained (untouched); I did not
  re-run AE~Z's live BD scan and do not inherit its figures; the 49F side is untested for the same
  defect (surfaced once, COO owns it, not chased).

---

## Next Steps

1. **[2.0.0_SA_COO]** Route the bronze-harvest scope question (`cot-rebalancer-runner:303` /
   `MODEL_DETAIL_SCOPE`). It is infra lane and sits behind a recorded Andrew/CTO ruling. Until it
   moves, this fix is inert by construction.
2. **[integrator]** Push `75e379d6ae` -- deployed S3 bytes are ahead of `origin/CLOUD`.
3. **[2.0.0_SA_COO]** Adjudicate whether `MDPF_COTTONWOOD.FIX1` closes as complete-with-blocker or
   waits on the harvest. Left `pending` by me.
4. **[2.0.0_SA_COO]** The four comp-tool coverage gaps above, if worth a routing item.
