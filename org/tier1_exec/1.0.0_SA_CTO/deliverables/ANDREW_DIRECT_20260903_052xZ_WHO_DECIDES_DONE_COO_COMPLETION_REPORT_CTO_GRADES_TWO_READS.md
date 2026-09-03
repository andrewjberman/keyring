# ANDREW-DIRECT at the CTO terminal, 2026-09-03 ~05:1xZ-05:2xZ -- who decides a project is done: the COO's completion report, the CTO's grade, two reads

**Verbatim (all words, four messages in order):**

1. `Another thing we need to identify here is who decides when the project is truly done? Who makes the decision to check the realized outcomes against the stated outcomes from the /endpoint --forward FWD items?`
2. `It seems like COO effectively is the one writing TOs against FWDs in some capacity, so they would be the one to know when to stop, at which point the results i think would have to be presented by COO to CTO in the form of a completion_report. or something like that`
3. `It probably is a formality but that way at least two agents have a chance of assessing the true finished status.`
4. `Do it`
5. (mid-turn, while the CTO was landing 1-4) `I also want to add something in there where if upon receipt it is in question, or if there is a scope change, the CTO can run /open-calls on the subject and then CTO adjudicates on the recs and it picks up from there via a new (or adjusted) PRD and then runs through the loop from that point. The goal is to have this entire process autonomous after Limb 2. I will work with CRO on the /brief-create , i will confirm CTO's "DONE WHEN" from their /endpoint --forward, but after that point, no matter what happens, I want the canonical loop to be able to keep cycling in its pattern and get the thing done.`

**Reading of message 5 (binding on the design below, and it AMENDS one line of it):**
- Andrew's two touch points are L1 (with the CRO on `/brief-create`) and L2 (he confirms the CTO's `DONE WHEN` lines
  from `/endpoint --forward`). AFTER L2 NOTHING WAITS ON ANDREW: the loop cycles in its pattern until the thing is done.
- Therefore the close's "rows whose `DONE WHEN` names Andrew turn REALIZED only on his word" is STRUCK before it lands:
  a card that names him is confirmed by him at L2 like every other card, and the CTO grades it on the record that
  the artifact reached him; no grade waits on his word.
- SCOPE_CHANGE at L10, and a completion report that is IN QUESTION on receipt: the CTO runs `/open-calls` ON THE
  SUBJECT, ADJUDICATES THE RECOMMENDATIONS ITSELF (records the ruling), amends or re-issues the endpoint and the PRD
  (new `FWD-<n>` ids appended, never renumbered), and the loop runs forward from L4. The sovereign queue is not
  consulted for a running project after L2; `/open-calls` at Andrew remains for everything outside a running
  project's loop.

**What the CTO put in front of him between the messages (the design he approved):**
- Today nothing reads the FWD cards' `DONE WHEN` lines against the realized state; the "two-part atomic close" is
  bookkeeping (terminal status + completed date + registry row). Zero surprises plus complete cells is a check on the
  members; the outcome is what the members share.
- The COO is the only seat that can say "the decomposition is spent" (every cell has a terminal task order with a
  valid proof-of-spec) -- the trigger for the close. The COO writes the COMPLETION REPORT, shaped PER FWD (not per
  cell): one row per outcome in the PRD header, the cells that served it, each cell's proof-of-spec, the COO's claim
  COVERED / UNCOVERED, both denominators printed (every FWD in the header, every cell in the decomposition). An
  outcome with zero cells reads UNCOVERED in the COO's own report.
- The CTO GRADES each outcome against the exercised artifact, never against the report: REALIZED / NOT_REALIZED /
  NOT_EVALUATED, the artifact and its vintage cited, the observed state matching the card's `DONE WHEN` state (an
  EXERCISED card is not met by an APPLIED citation). Two fields, two authors, measured apart: coverage (COO) and
  realization (CTO) are different axes, so the second read is corroboration, not repetition.
- The CLOSED flip is mechanical on the grades: refused unless every FWD in the header carries REALIZED. A
  NOT_REALIZED does not close; it returns to the COO as a decomposition gap and the loop re-enters at L5; an outcome
  that was itself wrong re-enters at L2 as a SCOPE_CHANGE. Andrew is in the loop only where a card's `DONE WHEN`
  names him (NFRA_COMPEFFICACY FWD-4: "read by Andrew"); those rows turn REALIZED only on his word.
- Outcomes whose `DONE WHEN` is an act after the work (three of this project's nine) need a closing-pass task order
  whose spec IS that exercise, cut by the COO at L6 like any other.
- The formality is kept cheap: the coverage table is derivable from the decomposition and the proof-of-spec files;
  the COO's judgment is one line per outcome; the CTO's grade is one artifact read per FWD; no message traffic beyond
  the report's notifier.
- The CVO is NOT the grader (the CTO's earlier proposal, withdrawn in the exchange): the close belongs to the COO and
  the CTO; the CVO's part is the zero-graduation stamp that precedes it.

**Reading (scope = the design as shown, "Do it"):** spine v2.3 (the closing pass inside L10: stamp -> report -> grade
-> flip; section 3; changelog), `org/standards/COMPLETION_REPORT.schema.json` (the COO's report and the CTO's grades
as two documents under one schema, Rule 24 record inside), and the CLOSED-flip gate as a rule of
`.tools/missions-tree-index.py check` (the tree stage of the pre-commit). No other surface.

**Execution this turn (1.0.0_SA_CTO):** the three artifacts with a red-first exercise of the gate rule; commits via
safe-commit; same-turn broadcast with push state stated as measured; the COO told what round 2's close will require.
