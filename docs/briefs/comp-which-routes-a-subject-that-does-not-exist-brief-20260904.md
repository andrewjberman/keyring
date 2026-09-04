# comp-which routes a subject that does not exist -- L1 brief (roll-up finding comp-which F2)

**Author:** `4.0.0_SA_CRO`. **Date:** 2026-09-04, measured 14:0xZ-14:2xZ. **Mode:** NEW.
**Commission:** Andrew-direct ~13:3xZ at the `3.0.0_SA_CVO` terminal, *"approve all recs"*, card 3 ruled (a): *"the first
piece of work from the ratified list -- comp-which F2 via the CRO's L1"* (CVO record
`ANDREW_DIRECT_20260904_133xZ_APPROVE_ALL_RECS_ESTATE_SITTING_ARCHIVE_CENSUS_COMPWHICH_F2.md`; relayed by the CTO in
94173). This is the act `NFRA_COMPEFFICACY` FWD-8's third limb names -- a seat starting work from the ratified short list.
**The finding, in the roll-up's words** (`CE-pass-1.rollup.md` v2, F2 on comp-which): *"a non-existent gold id routed with
confidence ... the most consequential finding across all three CE-t cells run so far -- a real wrong-object hazard on the
router every seat uses."* The router validates a subject's SHAPE and never its EXISTENCE.

**HOW TO READ THIS.** Part I is the territory `/endpoint --forward` cuts outcomes from -- five things a person can do.
Part II is the boundary. Part III the bar. Part IV what exists, measured, including the finding reproduced live at this
seat today. Part V preconditions, unsequenced. Part VI status with its clock, NOT outcome-bearing. Part VII what this brief
did not check. This brief is deliberately narrow: one finding on one tool, as his card named it.

---

## PART I -- THE OUTCOME TERRITORY

### O1. An agent who asks about a subject that does not exist is told so, not handed a confident route
An agent asks comp-which about a well-formed subject -- a gold-script id, a path, a component, a tool name -- that does
not exist in the estate, and the answer says SUBJECT_ABSENT_FROM_CORPUS in the router's own voice, with what it looked
in, before any route is printed. Today the same question gets a score-2.00 route to `comp-pipescript io A_00`, identical
to the route for the real script (Part IV F1).

### O2. A route line says what subject it resolved, so a reader can dispute the object before the tool
When comp-which routes on a named subject, the route line carries the subject as the router resolved it -- the id, where
it found it, and its vintage -- so a reader who doubts the object can contest it at the route rather than one hop later
when the routed tool refuses. Today the route carries only the prefix it matched (`A_00`) and the reader learns the
subject was wrong from comp-pipescript's refusal, if they run it.

### O3. The wrong-object case is a permanent RED arm in the routing harness
The routing test plants well-formed, non-existent subjects of each class the router recognises and fails the run if any
is routed with confidence -- zero tolerance, the way the harness already treats gibberish -- so the fix cannot regress
silently and the class of hazard is graded by an instrument, not by a memory of this finding.

### O4. The routed tool's refusal reaches the asker at the route, not one hop later
When a routed tool would refuse the subject ("Script not found: ... Did you mean: A_00?"), the asker sees that refusal
at comp-which's line, with the suggestion, instead of paying the hop and reading the refusal from the second tool.

### O5. A seat can measure how often the router was asked about nothing
From the rail log, a seat counts routes that resolved to SUBJECT_ABSENT over routes that resolved a subject -- the
wrong-object rate becomes a number with a denominator, per subject class, over a stated window -- so the next census of
comp-which's efficacy reads the class this finding named rather than rediscovering it.

---

## PART II -- WHERE THE BOUNDARY SITS

**This work OWNS:** the subject-existence read inside `.tools/comp-which` (the layer that turns a matched identifier into a
route); the answer-state it emits (adopting `SUBJECT_ABSENT_FROM_CORPUS`, an existing carrier -- never minting a spelling);
the route line's subject disclosure (O2); the RED arm in `.tools/comp-which-routing-test.py` (O3); the rail-log row shape
that makes O5 countable; and the bounded cost of the check under comp-which's Rule T budget.

**This work RELIES ON, and does not build or move:** the existence ORACLES per subject class, each already built --
comp-pipescript's script registry for gold ids (it already answers "Script not found ... Did you mean"), `comp-find --name`
/ `git ls-files` for paths, the graph-call-manifest for tool names, the kuzu graph and `comp-aws` for ARNs and estate
resources; the router's layers as they stand (curated rules, surface-first, the DR2 posterior, the COMPROUTE cascade --
`comp_route.py`, `comp_which_signals.py`), which are not re-ranked here; the four-way answer-state schema and Rule T from
`NFRA_COMPEFFICACY` PRD s.4 (inherited as the bar); the gibberish control already in the harness (kept; this adds the
well-formed case beside it).

**Siblings named:** `NFRA_COMPEFFICACY` (ROUND_CLOSE; the finding's source, T-3's result and CE-pass-1 v2), `NFRA_TOOLCHECK`
(P4 seed 18, the 2026-07-10 "confident on the unanswerable" lineage), `NFRA_COMPROUTE` (the DR1/DR2 routing layers),
`NFRA_GRAPHFEED` (the zero-rate harness), the PIPESCRIPT project (the gold-id oracle), and the comp-heat brief of the same
day (`docs/briefs/comp-heat-and-the-semantic-estate-pipeline-outset-tooling-brief-20260904.md`, whose Part VII left this
finding out on purpose).

---

## PART III -- THE QUALITATIVE BAR

- **B1.** The same question asked about a real subject and about a well-formed fake one gets two DIFFERENT answers, and the
  fake one names what was looked in -- today they are byte-identical to the route line.
- **B2.** A reader who stops at the route line cannot be misled about the object; what the routed tool would refuse is
  visible at the route.
- **B3.** The check never makes comp-which miss its own budget: a slow oracle degrades to "existence UNVERIFIED" in the
  router's voice, never to a silent confident route and never to a hang.
- **B4.** The harness fails on the first well-formed fake it routes, the way it fails on the first gibberish it routes.
- **B5.** The 2026-07-10 sentence -- *"comp-which cannot say 'nothing fits' about any vetted tool"* -- stops being true for
  the subject half of a question, and stays honestly true for the tool half, which this brief does not touch.

---

## PART IV -- THE SUBSTRATE: what exists, measured

### F1. The finding reproduces live, and the two answers are identical
At this seat 14:0xZ: `comp-which "what feeds gold:A_00.accounts_dimension"` -> `1. score 2.00 comp-pipescript io A_00`;
`comp-which "what feeds gold:A_00.accounts_dimension_zzz9"` -> `1. score 2.00 comp-pipescript io A_00`. Same top route,
same score, same second candidate (comp-transform 1.71). `comp-find --name 'A_00.accounts_dimension*'` -> 2 hits (the
black_diamond and cot gold scripts); the `_zzz9` subject -> 0. -- The finding is not historical; it is the router's
behaviour at HEAD (`.tools/comp-which` 2,445 lines @`2f6dca8204`, 2026-09-03).

### F2. The mechanism: the identifier extractor and the curated rules key on the prefix, and no oracle is asked
`_extract_term` (comp-which:1476-1487) picks "the most specific identifier-ish token" by pattern; the gold-script rules
(the "gold script write / io" family at :119-138 and the bare "gold script" rule-3 at :681-763) route on the `A_00`
shape. Nothing between the match and the route asks whether `A_00.accounts_dimension_zzz9` exists; the score is
overlap and the banner says so ("score is overlap, NOT a confidence"). -- The PRD buys a LOOKUP between match and route,
per subject class, against oracles that already exist (F4). It does not buy a registry.

### F3. The wrong object dies one hop later, loudly -- so the cost today is the confident line and the wasted hop
`comp-pipescript io A_00.accounts_dimension_zzz9` -> rc 1, `Script not found: A_00.accounts_dimension_zzz9. Did you mean:
A_00?`; the real id -> rc 0, the I/O manifest. -- The hazard is the reader who stops at the route (Part I O2, O4); the
oracle the router needs for gold ids is the very message the next tool already prints.

### F4. Gibberish IS handled; well-formed-and-absent is exactly the case nobody planted
The routing harness (`.tools/comp-which-routing-test.py`, 1,608 lines) treats a routed gibberish query as a failed run
("zero-tolerance, not a rate"); T-3's result records comp-which abstaining on 100% of generated gibberish after its F4
harness fix, and the harness's own docstring says "the live MIS-ROUTE happens DOWNSTREAM". The 2026-07-10 COO brief
(`comp-which-confident-on-the-unanswerable-20260710.md`, corrected 13:20Z the same day) found the general shape --
`relevance_floor = 0.15` never binds, so the router "cannot say 'nothing fits' about any vetted tool" -- and routed it to
the CTO; the gibberish half was fixed. -- The subject half is the gap, and it is narrower than the July finding: a
well-formed subject whose shape matches a rule and whose existence nobody checked.

### F5. An adjacent finding on the same tool is out of this brief by his card
T-3's F1: no layer-provenance disclosure -- the route line never says which layer decided (curated / surface-first /
DR2 posterior / manifest-fuzzy / legacy cascade) and prints no vintage. It shares a carrier with O2 (the route line) and is
NOT folded in here; his card named F2. Named so the PRD can decide whether O2's disclosure line carries the layer too.

### F6. A side finding met on the way, not this brief's
`comp-pipescript io <id> --budget 60` -> rc 2, `error: unrecognized arguments: --budget 60`. comp-pipescript is marquis and
verdict-bearing (rc 4 on `deployed`); its `io` subcommand takes no budget. Named for `1.0.0_SA_CTO` and the PIPESCRIPT
owner; not a cell of this work.

### F7. The answer-state vocabulary already carries the value this work needs
`SUBJECT_ABSENT_FROM_CORPUS` is one of the four states `NFRA_COMPEFFICACY` PRD s.4.3 ratified, and T-3's result quotes
comp-which's own planted case for it. -- Adopt, never mint; the census in PRD s.4.7 settled that spellings are not
re-coined.

---

## PART V -- WHAT MUST BE TRUE, without scoping it now

- **P1.** Each subject class the router recognises has a named existence oracle and its cost is known (gold id ->
  comp-pipescript's registry; path -> git index / comp-find; tool -> the manifest; ARN / resource -> the graph or
  comp-aws). Which classes the extractor actually recognises is a census the PRD needs (Part VII).
- **P2.** The lookup runs inside comp-which's Rule T budget and degrades loudly (B3); a slow oracle never becomes a hang
  on the tool every seat calls first.
- **P3.** The harness's red arm plants one well-formed fake per class beside the gibberish control, and the harness's own
  controls stay green (a harness that fails its own controls discards its numbers -- its rc 2 contract).
- **P4.** The route line's disclosure (O2) and the rail-log row (O5) are one shape, so the count and the reader read the
  same field.
- **P5.** Nothing here re-ranks the router or touches the DR2 posterior; a subject that EXISTS routes exactly as today.
- **P6.** The gold-id oracle's "Did you mean" suggestion is carried, not re-implemented (O4).

---

## PART VI -- STATUS, NOT OUTCOME-BEARING

Measured at this seat 2026-09-04 14:0xZ-14:2xZ at HEAD on CLOUD (LOCAL; origin/CLOUD @`351f309e0a` per the CTO's 12:40Z
ls-remote read, ageing at MSTR's window).

| what | state | clock |
|---|---|---|
| `.tools/comp-which` | 2,445 lines @`2f6dca8204` (2026-09-03); Rule T wired @`e8f67c34f5` | HEAD |
| the finding | reproduced: real and fake gold id both `score 2.00 comp-pipescript io A_00` | 14:0xZ |
| the oracle for gold ids | `comp-pipescript io <fake>` rc 1 "Script not found ... Did you mean: A_00?" | 14:1xZ |
| the harness | gibberish control zero-tolerance; no well-formed-fake arm (enumerate: 0 hits for nonexist/absent as a case) | HEAD |
| answer state carrier | `SUBJECT_ABSENT_FROM_CORPUS` ratified (PRD s.4.3), planted once in T-3's result | record |
| `comp-pipescript io --budget` | unrecognized argument (F6) | 14:1xZ |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It probed ONE subject class (a gold-script id). Whether paths, component names, tool names and ARNs are routed the
  same way is not measured; the extractor's class census is P1's first act.
- It did not read `comp_route.py` (the COMPROUTE cascade) or the DR2 posterior; the mechanism finding (F2) rests on
  `_extract_term` and the curated rule table, which is where the observed route came from, but a second path to the same
  confident line may exist.
- It did not measure the cost of an existence lookup per class, or comp-which's current p50 latency against its 90 s
  budget.
- It did not fold in T-3's F1 (layer provenance) or comp-find F1 (`--version` as a search pattern); both are adjacent,
  both named, neither is this card.
- It did not decide whether O2's disclosure belongs on every route or only on subject-bearing routes.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/comp-which-routes-a-subject-that-does-not-exist-brief-20260904.md
  PROJECT           NONE-YET
  EXISTING PRD      NONE (inherits the answer-state schema and Rule T from
                    org/missions/D11/NFRA/NFRA_COMPEFFICACY/prd/NFRA_COMPEFFICACY_PRD.md s.4)
  SIBLING PROJECTS  NFRA_COMPEFFICACY, NFRA_TOOLCHECK, NFRA_COMPROUTE, NFRA_GRAPHFEED, PIPESCRIPT; the comp-heat brief of
                    the same day
  PRIOR ART         .tools/comp-which @2f6dca8204 (:1476-1487 _extract_term; :119-138 and :681-763 the gold-script rules);
                    org/modules/graph/comp_which_signals.py; .tools/comp-which-routing-test.py; org/tier2_senior/
                    0.8.0_AE_CloudComp/deliverables/comp_which_zero_rate_harness.py; org/modules/graph/pipeline_cli.py
                    (the "Script not found ... Did you mean" oracle); docs/briefs/comp-which-surface-aware-router-brief-
                    20260630.md; org/tier1_exec/2.0.0_SA_COO/briefs/comp-which-confident-on-the-unanswerable-20260710.md
  RECORDS           org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-which.result.md (T-3,
                    findings F1-F4); org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/3.0.0_SA_CVO/CE-pass-1.rollup.md
                    (v2, F2); the CVO's Andrew-direct record of 2026-09-04 ~13:3xZ (card 3 ruled (a)); CTO relay 94173
  MEASURED AT       2026-09-04 14:0xZ-14:2xZ (every Part VI row carries its own clock)
```
