# CTO ADJUDICATION -- NFRA_COMPEFFICACY, 2026-09-03 ~15:35Z (spine v2.3 L2 re-entry; `/open-calls --adjudicate`)

**Trigger:** 3.0.0_SA_CVO's round-5 L10 stamp @b5d228fe62 routes `NFRA_COMPEFFICACY-S17` to L2 as `SCOPE_CHANGE`,
`scope_change_kind CONTRADICTS_NAMED_OUTCOME`, `outcome_ref FWD-5`, owner `1.0.0_SA_CTO`. The same question reached this
seat from 2.0.0_SA_COO's /drive tick 2 (93678) with a REC. Under Andrew's word of 2026-09-03 ~05:2xZ the CTO adjudicates
and the loop runs forward; nothing here waits on him.

**Inputs read:** the S17 investigation row (0.8.0_AE_CloudComp~B @a140eed779) and its remediation row; TO-CE-T-19's face
(WITHDRAWN on its own STOP clause @5a837b1abd) and deliverable @bfbff9dc14; PRD v0.5 s.6 R-4 (:609-610) and s.7 row
T-19 (:647); FWD-5's card; the decomposition's dependency CE-t-6 -> CE-t-19.

**The measurement the route rests on (two instruments, neither the L4 owner's line-range read):** at the FLAG grain
comp-trace carries `--exact`, `--all` and the upstream/downstream direction spellings, which comp-blast rejects (rc 1,
"unrecognized arguments", exercised); at the TRAVERSAL grain the two tools answer over different graphs with disjoint
address spaces and node-type schemas -- blast resolves 38.6% of trace's own node ids as callers spell them, 58.2% under
the most generous prefix mapping. Building the forwarder would have silently converted roughly 61% of working comp-trace
invocations (45 real runs in 30 days, three seats) into NOT-FOUND or AMBIGUOUS -- the false-clear class.

```
+-- CALL 1 of 2 ---------------------------------------------------+
  **R-4 ("comp-trace ... if so it should be retired") is conditional
  and its condition -- trace is a strict subset of blast -- is measured
  NOT MET. Which way does T-19 close: (a) retire anyway as a decision
  and accept the coverage loss; (b) keep comp-trace, close T-19
  NOT-RETIRED on the measurement; (c) widen CE-t-6 to carry trace's
  universe into blast before retiring?**
  The lane stopped at the row rather than build the forwarder, exactly
  as its order's STOP clause required.
  --------------------------------------------------------------------
  **REC -- (b), with the three carryable flags into blast under CE-t-6.**
  A conditional ruling whose condition fails does not fire; the
  non-carryable axis is the universe, which is a graph-engine question
  (NFRA_CLDGRPH's), not a comp-tool audit's.
  --------------------------------------------------------------------
  **RULING -- (b).** comp-trace is NOT retired; T-19 closes NOT-RETIRED
  with S17 as its evidence; the three carryable flags (`--exact`,
  `--all`, the direction spellings) enter blast's parser under CE-t-6,
  which the decomposition already makes T-19's dependent. (a) is not
  taken: a ruling Andrew made conditional cannot be widened past its
  condition by the seat that wrote the condition down wrong. (c) is not
  taken: carrying trace's universe into blast is porting the graph
  engine, which is NFRA_CLDGRPH's project (S15's handoff already sits
  there). No card to Andrew: his conditional ruling ALREADY answers the
  unmet case -- "if so" was the whole of it.
+---------------------------------------------------------------------+

+-- CALL 2 of 2 ---------------------------------------------------+
  **Is FWD-5 contradicted (a new outcome needed), or answered
  differently (the PRD's claim corrected, the outcome unchanged)?**
  The route names CONTRADICTS_NAMED_OUTCOME on FWD-5 ("Andrew's
  specific questions are answered in writing ... whether trace is just
  dataflow"); the world contradicts the PRD's s.7 CLAIM, not the card.
  --------------------------------------------------------------------
  **REC -- answered differently; no new FWD.** FWD-5 asks for a written
  answer he can dispute; the corrected answer IS such an answer.
  --------------------------------------------------------------------
  **RULING -- answered differently.** FWD-5 stands; its written answer
  for comp-trace becomes: "not a subset of blast at either the flag or
  the traversal grain (measured two ways); kept; the three carryable
  flags move into blast." The PRD's s.7 T-19 row (claim=measured on a
  false subset) and s.6 R-4 note ("Condition MET") are corrected at L4
  as PRD v0.6 -- the row was the L4 owner's own error, a line-range
  read taken as a measurement. No FWD id is added or changed.
+---------------------------------------------------------------------+
```

**What follows (the loop, in order):** PRD v0.6 at the tree home (this turn; a substantive edit, so the L4 notifier fires
to 2.0.0_SA_COO); L5: CE-t-6's row gains "carry `--exact`, `--all` and the direction spellings from trace" as part of
its closes-on and loses its dependency on a T-19 retirement; L6: the COO cuts CE-t-6 accordingly in the wide round; T-19
is closed NOT-RETIRED by the issuer on this record (a status flip on the withdrawn face, or a one-line closing note --
the issuer's form). The disarm on S17 (in place, 1.0.0_SA_CTO as disarm_owner) is this record plus PRD v0.6; the CVO
dispositions the row at L9.
