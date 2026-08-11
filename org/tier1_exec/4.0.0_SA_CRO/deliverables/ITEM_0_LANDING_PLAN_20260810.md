# ITEM 0 -- THE FRAMEWORK LANDING PLAN

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Date:** 2026-08-10 · **Commission:** Andrew-direct at the CRO terminal, same day (record @dedd7bdeab
R-5; framing confirmation: *"Yes you are exactly correct that the issue is a landing problem, that is
the nature of what I am tasking you with for Item 0, it is to wrap all of this into a scheduled
implementation plan to land and synthesize these matters across our Infrastructure."*)
**Status:** v1.0 -- the plan. CRO proposes and specifies; CTO/COO staff and sequence against the live
fabric. **This plan INFORMS; it GATES NOTHING** (deliberate: Andrew superseded a
framework-completes-first gate this morning; Item 0 must not recreate one under a new number).

---

## 0. The finding the plan rests on

Eight framework constituents were assessed individually (Andrew's list, verbatim order, R-5). The
verdicts are NOT eight independent stories. Measured today, git-grounded throughout:

**THE ESTATE'S FRAMEWORK PROBLEM IS A LANDING PROBLEM, NOT A CAPABILITY PROBLEM.** Nearly every
constituent is finished or near-finished work sitting ONE SMALL ACT from being live -- and in each
case that act was correctly declined by a seat refusing to infer authorization it did not have. The
discipline is right. The accumulation is the cost. (COO's form, adopted as this plan's organizing
principle: **"items that cost nothing are the ones that quietly never happen."**)

The remedy is therefore a SCHEDULE OF LANDING ACTS -- each with an owner, a trigger, and its
precondition named -- not a build program.

## 1. Per-constituent state (COMPLETED / PENDING / SUPERSEDED, + the LOAD axis)

| # | Constituent | STATE | LOAD (what depends on it) | The landing act |
|---|---|---|---|---|
| 1 | NFRA_VELOCITY | **PENDING(on-hold)** -- both halves SUSPENDED behind RCG; no longer gates ADVI (R-4) | 5 closed projects re-homed their roadmaps INTO it | **L-6**: disposition decision |
| 2 | ATOM_DECOMP | **PENDING** -- repaired, never run, unregistered | the four-month program names it as its decomposition method | **L-4**: register -> F-2 synthesis -> proving runs |
| 3 | system/ ontology | **SPLIT**: SYSTEM_DEFINITIONS.yaml LIVE (v1.8+, 08-06); core_nfra_velocity FROZEN 07-31 | comp-estate --definitions serves it; Rule 24 acts cite it | **L-5**: fold-or-strike the frozen five |
| 4 | Graph infrastructure | **SPLIT**: Nessie/Iceberg/Kuzu spine LIVE (auto-refresh, provenance headers); C2/C3.i instance layer BUILT-UNDEPLOYED (ECR image 07-18) | the Kimi pipeline and every coverage question | **L-1 + L-2**: the deploy + the seam edge |
| 5 | Comp tooling | **SPLIT**: tools LIVE (96/97 resolve; comp-find/comp-estate/comp-kuzu working); ROADMAP HOMELESS (TOOLARCH/TOOLSEM/TOOLBHVR/COMPLEARN closed complete-as-superseded INTO suspended VELOCITY) | every agent, every session | **L-6**: re-home the roadmap |
| 6 | Kimi Semantic Vertical Pipeline | **LIVE** (OPAL_KIMIPIPELINE, registered, scheduled 0900ET) -- Andrew: the de-facto driver, "the top level of the graph and comp-tooling, the entry point for agents" | the synthesis target everything above folds INTO | the ANCHOR, not a landing item |
| 7 | NFRA_PYFIELD | **PENDING(active)** -- TO-0 + TO-1 closed (denominator 2,744/4,406; recognizer 2,295/4,413); Q1 (build extractor vs defer) carried DEFER recs from both lanes | C3.ii field-grain bridge, eventually | **L-3b**: Q1 closes inside the C3.ii fold |
| 8 | Script IO (comp-pipescript / comp-dataflow) | **COMPLETED(tools) / PENDING(coverage)**: comp-pipescript live + deploy-gated; comp-dataflow live (last touch 07-23); S-layer dissolved 08-07 | DS/AE daily flow; ATOM_DECOMP tool-adapters cite them | **L-7**: coverage census, then stop |

**Rule-24 note kept live:** STATE and WORTH-CARRYING are different axes. Constituent 1 is the live
case: PENDING on status, while its VALUE now largely lives in constituents 3+6 (the definitions moved
to SYSTEM_DEFINITIONS; the semantic driver moved to the Kimi pipeline). The disposition act L-6
exists precisely because status alone cannot make that call.

## 2. The landing schedule

Ordering constraints, stated before the table so the table cannot be read around them:
**(a)** The MDPF repair is THE MAIN FABRIC PRIORITY (Andrew x3, ~1620Z @5b14d993f2). No landing act
below staffs engineering while the repair holds that title -- acts marked [record] cost no
engineering; acts marked [build] queue behind it.
**(b)** Item 1 (Cottonwood pull) registers now, scopes behind the repair, runs after it -- its own
project, "purely backend and scheduling initially" (his boundary, verbatim).
**(c)** Every phase carries a **REMEDIATION REGISTER** as a named deliverable (R-4b) -- a file with a
path, not a norm: *norms decay, registers accumulate* (COO's correction, adopted). Mid-implementation
slips get one banked line there and a second pass; the 08-06 gate diagnosis is the measured instance.

| Act | What lands | Owner | Trigger / precondition | Kind |
|---|---|---|---|---|
| **L-0** | ATOM_DECOMP registered as a project | CTO base | brief delivered @342fb8426d -- CTO's timing | [record] |
| **L-1** | **C2/C3.i instance layer DEPLOYED** (19->6,138 C2 / 4->1,255 C3, nightly recompute) | CTO(decouple) -> AE(--go) -> CVO(re-run) -> CTO~B(accept) | ⛔ the named-unbuilt `:latest` decoupling: 4 sibling task-defs pin immutable tags AND/OR buildspec stops pushing `:latest` -- **either alone is insufficient** (CVO 08-07). Pull list @0871ce898f + @f0cd33c037 already in tree | [build] |
| **L-2** | **The serve-seam GOVERNS edge** (1 edge; reconnects frontend<->backend traversal for all 28 served URLs) | CVO (live again 17:13Z); COO holds the schedule record | AUTHORISED (Andrew ~17:1xZ @aea6c9ff68) · caveat = the aws/pipeline territory ruling (measurement DONE same day, routed CVO+CTO for ratification) | [build, small] |
| **L-3** | **C3.ii joined** -- declared plane x applied plane x semantic verticals, folded into comp-estate/Kimi as the entry layer | CRO(spec) + CVO(graph) + CTO(arch) | AFTER L-1 (the join needs the instance layer live; Andrew: "Yes fold it in") | [build] |
| **L-3b** | NFRA_PYFIELD Q1 closed | CRO -> Andrew | resolves INSIDE L-3's scoping: the C3.ii join defines whether a field-grain extractor has a consumer; if L-3 does not need it, Q1 closes DEFER permanently | [record] |
| **L-4** | ATOM_DECOMP made REAL: F-2 synthesis lands (branch 2, measured 17:0xZ: neither list structural) -> proving run 1 = **item 4** (ETF/Positioning fold-in) -> proving run 2 = **item 1 SCOPING** | CRO(draft) + CTO~A(method-owner review) -> then per-item owners | synthesis: CTO review only. Run 1: item 4 is parallel-lane by Andrew's own word. Run 2: BEHIND the repair with item 1 itself | [record then build] |
| **L-5** | core_nfra_velocity DISPOSED: the five frozen docs (WS-C1/C2/C3/C7/C8) each folded into SYSTEM_DEFINITIONS or struck with a pointer | CRO(census) + CVO(definitions owner) | none -- read-only census first; Andrew ratifies the fold list | [record] |
| **L-6** | The homeless tooling roadmap RE-HOMED: VELOCITY's open-work ledger (NFRA_VELOCITY_PROGRAM.md s.3b) triaged into (i) absorbed-by-Kimi/comp-estate, (ii) still-wanted -> re-homed to a LIVE project, (iii) dead -> struck. Then the VELOCITY rows close honestly | CRO(triage draft) -> Andrew(disposition) -> COO(registry act) | none for the triage; the close is Andrew's word | [record] |
| **L-7** | Script IO coverage census: comp-pipescript/comp-dataflow coverage vs the 386-file gold corpus, gaps named with owners -- then STOP (no new tools without a named consumer; Build Ladder rung 1) | CRO | none | [record] |

**The synthesis Andrew asked for is the L-3 endpoint:** comp-estate/Kimi as the single entry layer
("the top level... the entry point for agents"), with C1 estate resources, C2 motifs, C3.i instance
systems and C3.ii semantic verticals all queryable beneath it, definitions in SYSTEM_DEFINITIONS,
and every constituent above either folded in or honestly closed. That is "how we build our
infrastructure to foster the development of Opal business endeavors" made concrete: **one entry
point, real structures beneath the names, and a registry that tells the truth about state.**

## 3. How this meets the four-month program

- **Item 1** (Cottonwood, own project, backend+scheduling): its scoping is ATOM_DECOMP proving run 2
  (L-4) -- the method's second exercise, on ruled substrate (bronze ownership ruled by CTO 08-10).
- **Item 2a** (49F archetype): inherits a landed graph (L-1..L-3) for its dependency checks, a proven
  decomposition method (L-4), and the field-registry discipline the taxonomy Phase 0 seeds. 2a is
  NEVER a framework's first use -- every framework it relies on has been exercised at least once
  by the time it starts.
- **Items 3/4**: item 4 doubles as L-4's proving run 1; item 3's account-spine question lands on a
  graph that can actually traverse frontend->backend (L-2).
- **Carried semantics** (so the plan does not silently over- or under-serve later rulings):
  point-in-time AUA is a CURRENT ruling scoped to the Cottonwood question -- the taxonomy carries a
  vintage slot, forecloses nothing, builds nothing for restatement (@e82326bdb2); the taxonomy root
  name is PROVISIONAL ("Model Portfolios" may become "Fee-Paying Assets", R-1); bucket moves are
  RE-LABELS over stable strategy identifiers, never re-derivations (R-3).

## 4. What this plan does NOT do

No new frameworks. No new monitors/alerts (moratorium). No gates (none asked for). No engineering
staffed against the repair window. No estate-wide inheritance of scoped rulings. And no act in the
table lands "when someone gets to it" -- **an act with no trigger is the failure mode this plan
exists to end.**

## 5. Denominators and honesty

Assessed: 8 constituents against 304 project JSONs, REGISTRY rows, git path-recency, live ECR/Kuzu
state. Instrument failures during assessment, all caught by controls and disclosed same-turn: a
`grep|head` exit-code swallow (would have faked "everything registered"), a commit-message recency
match on my own record commit, two wrong table/repo name guesses. Constituents 4/5/8 lean on CVO/CTO/
AE records read as evidence -- where a verdict surprised me I re-measured live (ECR vintage, Kuzu
tables, layer counts); where it did not, the owning seat's record is cited rather than re-derived.
The LOAD column is the axis I could not fully re-derive today -- L-6's triage is where it gets
measured instead of asserted.
