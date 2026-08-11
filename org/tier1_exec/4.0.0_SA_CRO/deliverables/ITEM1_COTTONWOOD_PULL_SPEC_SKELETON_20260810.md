# ITEM 1 -- THE COTTONWOOD "CUSTOM" MODEL PULL: PROJECT SPEC SKELETON

**Author:** 4.0.0_SA_CRO · **Date:** 2026-08-10 · **Status:** PRE-SCOPING SKELETON, written ahead of
need so scoping starts warm when the repair clears. **Registration is CTO base's act; scoping runs
BEHIND the MDPF repair; the run starts strictly AFTER repair completion** (Andrew x3 ~1620Z
@5b14d993f2 -- the repair is THE MAIN FABRIC PRIORITY). Nothing here staffs engineering.

---

## 1. THE MANDATE, VERBATIM-GROUNDED

Four-month program item 1 (@1600047e64): *"Sort out 'Custom' model pull from Cottonwood Black
Diamond (Scanning any 'Opal' constituent)."* Plus the ~1620Z scope ruling: *"The scope of that
project is purely backend and scheduling initially"* -- **A STATED BOUNDARY: no serving leg, no
frontend, no display surface in the initial scope.** ⚠ Anti-widening note (COO's, adopted): the
"scanning any Opal constituent" framing READS like an analytics/reporting need; a spec drawn from
the outcome rather than his words would pull in the serving tier he explicitly deferred.

## 2. THE BASIS -- AE's brief, and it is sharper than scouting

`BRIEF_COTTONWOOD_OPAL_CONSTITUENT_ATTRIBUTION_20260807.md` (0.7.0_AE_CloudOps~Z; AE named it as THE
briefing). It root-causes the problem:

- **A FILTER-ORDER DEFECT, source-confirmed** (`build_dim_model_portfolio.py:274-277`): the strict
  Opal filter runs BEFORE decomposition and keys on the PARENT strategy's name -- so an account on a
  non-Opal-named strategy is discarded before its Opal children are walked. Live proof: `Opal Fixed
  Income` exists in BD (2 accts, both Anna) and is WHOLLY ABSENT from the attributed dimension;
  the Conservative Growth tie (96+2=98, exact) confirms the cause independently.
- **Six child-only constituents** -- none appears in the 62-strategy roster, so ANY top-level scan
  is structurally blind to all of them. The remedy is decompose-then-filter (`is_opal` at the LEAF),
  keeping non-Opal leaves visible with `is_opal=False`.
- **Measured impact today: 2 accounts -- and that is the point**: the defect is structural, not
  proportional; every future non-Opal-named strategy built from Opal models is invisible on the day
  it is created.
- **The Global consequence is a SEMANTIC CHANGE to a served number** (Cottonwood non_model ->
  model_aua -> Global model AUM increases). The brief names it so it is never a silent fix.

## 3. ADJACENCY -- surfaced for the registration act, NOT adjudicated here

Two registered carriers already touch this subject; a third minted silently would be the fork class:

| Carrier | Relationship |
|---|---|
| `MDPF_SLICES` | CTO named its MODEL-PULL HALF as item 1 (@620890b552) and struck "due THIS WEEK" per the resequence. **The natural shape: the new project ABSORBS that half with a supersede pointer**, the slice half stays deferred where it is. |
| `WSE_COTMDL` | RECLASSIFIED 2026-07-22 as a FIRM ONBOARDING, not a data fold. Sibling, not parent -- cite, do not merge. |

**CTO base resolves which shape at registration** (their lane, LD-0331 posture). The skeleton only
insists the overlap be resolved EXPLICITLY.

## 4. SCOPING METHOD -- the two ratified frameworks, exercised on real work

- **FOUNDATION LEDGER FIRST** (Andrew ~18:2xZ): before design, the stage-boundary ledger for the
  cot pipeline -- rows per boundary (BD Rebalancer API -> bronze `blackdiamond/cottonwood/bronze/`
  -> silver -> gold dim/attribution -> Global rollup), columns: mover (`cot-rebalancer-runner`,
  cron(0 6)Z -- RULED owner of the bronze prefix; the mirror's guard NARROWS, never disables),
  schedule, the TWO CLOCKS, gates + which clock each reads, calendar semantics, **dependencies AT
  EVERY BOUNDARY** (his enhancement), **DECLARED value + MEASURED-HONORED** (COO's
  route_bindings lesson). Much of it populates from AE's brief + COO's census -- the ledger is
  assembly, not discovery.
- **ATOM_DECOMP PROVING RUN 2** (per the registration brief's M2): this scoping exercises the
  13-Rule method on a live subject. Rule 10 binds the constituent counts (memberships, not totals);
  Rule 13 binds the crosswalk fields; Rule 5's count-grain binds every figure quoted from the brief.

## 5. THE STRUCTURED DELIVERABLE, DEFINED AT SCOPING TIME (his anti-half-cocked requirement)

Sequenced from the brief's own task order, each with its discriminating question:
1. **Dollar sizing** of the excluded accounts (nothing ships before this number exists).
2. **`Opal Fixed Income` resolved on model_id, not name** (new model vs BD-side alias -- two
   different remedies; DS owns the crosswalk).
3. **The filter-order inversion** (decompose-then-filter at the leaf) -- one change, closes the class.
4. **Conservation gate re-verified BY MUTATION** (`sum(by_model) == model_aua` -- both sides move).
5. **The delta system as PRODUCER-SIDE MANIFEST DATA, fail-closed** -- recursive walk, constituent
   set + hash persisted, set-difference vs prior run, REFUSAL on an unrecognized is_opal=True
   constituent. ⚠ Moratorium-shaped by design (AE's framing, kept): NOT an alarm/SNS/checker --
   detection lives inside the producer that already walks the tree; candidates route to a HUMAN
   ruling, never auto-enrolment.
6. **Schedule ratification** -- the "scheduling" half of his boundary: the pull's own cron +
   its position in the foundation ledger's timing chain.

## 6. TAXONOMY HOOKS (schema v0.1 @eb8f8d4239)

Custom constituents feed **MODELS** at position grain via stable `strategy_id`s (the crosswalk ids
are the natural carrier). The "Opal"-token fragility control applies verbatim: `is_opal_name` is a
substring test, so the reconcile-to-total-AUA control + UNCLASSIFIED bucket are what make a naming
miss loud. The Anna leading-space name (`" Anna *9238"`) is the measured exact-match hazard: ids,
never names, in every join.

## 7. GATES AND SIGN-OFFS THE SPEC MUST CARRY (existing law, not new gates)

- The Global model-AUM change is a SERVED-NUMBER move: pinned baseline + dollar delta stated before
  ship + honest provenance labels (the brief's own discipline) -- and never-widen sign-off applies
  to any served-output relocation per standing law.
- 49F parity question (brief sec8): the code path is shared -- whether the same filter-order defect
  exists on 49F is a NAMED OPEN QUESTION for the spec, not assumed either way.

## 8. WHAT THIS PROJECT IS NOT (initially)

No serving leg. No frontend. No monitor/alarm/SNS. No estate-wide inheritance of the point-in-time
ruling (Cottonwood-scoped). No 49F work without its own authorization. The frontend fold-in
(no-new-tabs, per his 08-10 Teams ruling) is a LATER phase gated on the backend being clean.
