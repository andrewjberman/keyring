# The `#2`/`#4` field-2 rows, walked

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Date:** 2026-08-06, workspace @84232990b7
**Subject:** `docs/doctrine/INTENT_DENOMINATOR_SYNCHRONIZATION.md` section 9, FIELD 2 table. The
canonical carried: *"The mapping is worked for `#1` and `#3`; `#2` and `#4` are reasoned, not
exercised. Do not build on the `#2`/`#4` rows until someone walks them."* This is the walk.

**VERDICT: BOTH ROWS CONFIRMED BY EXERCISE.** `#2` GRAIN SHIFT lands in **not traversed** (the
C-row), `#4` VOCABULARY POVERTY lands in **coerced to nearest sayable** (ROUTE B) -- each on the
estate's own measured specimen, each with the denominator printed. One sharpening surfaced on `#2`
(trigger-grain vs verdict-grain, below); no correction to the table was needed.

---

## Walk 1 -- `#2` GRAIN SHIFT -> "not traversed". Specimen: D-7.

**The specimen** (`docs/references/INTENT_DENOMINATOR_INSTANCES_20260723.md` D-7): the comp-which
self-route invariant was written at TOOL grain; the declaration surface grew SUBCOMMAND grain
(`comp-iam simulate`, `comp-iam reconcile`, `comp-pipescript postdeps`) and the invariant did not
follow it down.

**The guard, at source** (chain verified end to end, this walk):
`.tools/comp-manifest-check` (bash shim) -> `org/modules/graph/manifest_check_cli.py:716
@29c3fedeb8` -> `self_route_verdicts()` in `.tools/comp-which-routing-test.py:484-492 @4489d4cd8d`.
Fail-closed commit gate, repo-wide.

**The measurement -- is the finer grain traversed, or never emitted?** The two field-2 candidates
prescribe different remedies (widen the sensor vs sharpen the oracle), so the cell assignment is
load-bearing, not taxonomy housekeeping.

1. **Population:** the gate's universe is `sorted(tools_index)` minus 3 exclusions
   (`comp-which-routing-test.py:490`) = **72 tool-grain members, 0 subcommand-grain members.**
   The live manifest carries **324 subcommand-grain members across 72 tools**
   (`tools_index[t].subcommands` lists) -- none can enter the universe: keys are the population,
   and no key contains a subcommand.
2. **Query:** `self_route_query` (`:439-447`) groups `entries[]` by
   `str(e["tool"]).split()[0]` -- a tool-grain coercion -- and returns `ucs[0]["use_case"]`, the
   FIRST entry only. The three D-7 declarations now have `entries[]` rows (post-remediation) and
   `subcommands` list members; neither surface is ever itself a tested member.
3. **Mutant exercise (in-process, pure -- no router invocation, no rail-log pollution):** grew the
   subcommand surface both ways it grows in life -- appended `"zzz-mutant-subcmd"` to
   `tools_index["comp-pipescript"].subcommands` AND appended an `entries[]` row declaring it.
   Result: **universe 72 -> 72 identical; all 72 tested queries byte-identical.** The gate
   structurally cannot fail on subcommand-grain growth. (Denominator of the exercise: all 72
   universe members compared, all 72 queries compared, both manifests.)

**Cell assignment: NOT TRAVERSED.** The sensor -- the enumeration producing checked members --
never emits a subcommand-grain member, under any growth mode. This is the C-row, exactly as the
canonical's own line *"GRAIN SHIFT (`#2`) IS A C, NOT A B"* reasoned. It is NOT "monotone
predicate": a predicate cannot be monotone over members it never receives. Exercised, no longer
reasoned.

**The sharpening the walk surfaced -- TRIGGER-GRAIN IS NOT VERDICT-GRAIN.** The gate is not even
silent on a subcommand edit. `manifest_check_cli.py:699-701` diffs `tools_index` keys, so editing
`tools_index[t].subcommands` marks tool `t` changed and the gate RE-RUNS on it -- and passes,
because what it verifies is tool-grain routability of `t`'s first-entry query. **Detection fires;
the member is still never traversed.** This is the precise mechanism of D-7's *"the guard kept
passing, correctly, over a population that had quietly stopped being the whole population"* -- and
it is one notch worse than a silent gap: a gate that visibly runs on your edit reads as coverage
of your edit. Sibling of the banked *"a control must fire on the defect event"* rule, distinct
from it: here the control DOES fire on the event and verifies a property at the wrong grain.

**Honest bound on the mutant:** `self_route_query` returns `ucs[0]`, so a subcommand `entries[]`
row PREPENDED (first for its tool) would change the tool-grain QUERY -- the gate's verdict is not
invariant under arbitrary insertion order. The invariant that holds under ALL orders, and the one
the cell assignment rests on: **no subcommand-grain member ever enters the checked population as a
member.**

## Walk 2 -- `#4` VOCABULARY POVERTY -> "coerced to nearest sayable". Specimen: `auth_api_gw`.

**The specimen:** `org/modules/graph/extract_routes.py @b9f80e6dae`, field `auth_api_gw: bool`
(`:164`, comment: *"API GW authorizer present"*).

**The measurement -- does the sensor emit a legal-looking value for a truth the type cannot say?**

1. **The assignment:** `:1053` -- `route.auth_api_gw = True` fires on
   `origin.origin_type == "api_gateway"` ALONE. No authorizer lookup exists in the path.
2. **Denominator:** `grep -n "authorizer|auth_api_gw"` over the entire file = **3 hits**: `:164`
   (the field + its comment), `:369` (a comment), `:1053` (the assignment). **Zero code consults
   an authorizer configuration.** The discriminating fact (does an authorizer exist?) is absent
   from the sensor's inputs, so the `bool` slot receives the nearest sayable value: `True`.
3. **Legal-looking downstream:** consumers render posture from the bool -- `routes_cli.py:409`
   prints `API GW: YES`; `pii_cli.py:351/:714`, `platinum_cli.py:181/:430/:583/:664/:929` branch
   on it. A predicate over the emitted vocabulary cannot discriminate grounded-True from
   coerced-True -- byte-identical values. ROUTE B: traversed, and the oracle cannot move.
4. **The residual was already named** at `org/modules/graph/comp-output-contracts.yaml:451`:
   *"an API Gateway origin with NO authorizer configured still reports API-GW auth -- a
   topology-inferred posture, not a grounded one."* This walk adds the field-2 classification and
   the evidence lines; the gap itself was honestly declared by its owner.
5. **The cost is measured, not hypothetical:** `extract_routes.py:365-370` records MACHINEFLAG R1
   (ruled P1 by `1.0.0_SA_CTO~Z`): the coerced value produced a FALSE-SECURE reading -- *"an agent
   asking what protects an origin was told an API Gateway authorizer guards a path no authorizer
   guards. The wrongness pointed toward safety, and a reassuring answer does not get re-checked."*
6. **The remedy pattern already exists ONE FIELD OVER, in the same dataclass:** the
   static-resolvability note (`:177-181`) -- *"the auth_* flags are UNDETERMINED, NOT proven
   absent -- consumers must report UNRESOLVED, never a false auth:NONE."* That is the
   widened-vocabulary remedy (`#4`'s fix is a slot, not a recomputation) applied to a sibling
   axis, while `auth_api_gw` itself retains the poverty. A future fix has an in-file precedent to
   copy.

**Cell assignment: COERCED TO NEAREST SAYABLE.** Exercised at source; the reasoned row stands.

---

## What changes where

- `INTENT_DENOMINATOR_SYNCHRONIZATION.md` section 9: the PARTIALLY-EXERCISED block flips to
  exercised, citing this record. The do-not-build-on hold on the `#2`/`#4` rows LIFTS.
- **Not changed, deliberately:** the field-2 table itself (both rows confirmed as written); the
  `auth_api_gw` defect (owned by the graph-tooling lane, residual already declared in its
  contract -- a walk classifies, it does not fix another lane's sensor); the gate's grain
  (whether the self-route invariant SHOULD follow declarations down to subcommand grain is a
  design question for the gate's owner, `0.8.0_AE_CloudComp` -- this record gives them the
  trigger-grain/verdict-grain mechanism if they take it up).

**Method note:** the `#2` exercise deliberately never invoked the live router --
`comp-which-routing-test.py`'s own header documents that gate runs append ROUTE rows to the rail
log it measures (the instrument-as-polluter class). The population/query claims are pure functions
over the manifest; exercising them in-process proves the same invariant with zero pollution.
