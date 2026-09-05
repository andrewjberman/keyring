# CTO ADJUDICATION -- NFRA_CLDGRPH, CG-x-2 limb (i) second arm

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-05 ~05:45Z · **On:** `2.0.0_SA_COO~A` 94349 (drive tick 25)
**Authority:** Andrew-direct 2026-09-03 ~05:2xZ at this terminal -- *"if upon receipt it is in question, or if
there is a scope change, the CTO can run /open-calls on the subject and then CTO adjudicates on the recs and it
picks up from there via a new (or adjusted) PRD and then runs through the loop from that point ... after that
point, no matter what happens, I want the canonical loop to be able to keep cycling in its pattern and get the
thing done."* Nothing here returns to Andrew.

---

```
+-- CALL 1 of 1 ------------------------------------------------------+
  **CG-x-2 limb (i)'s second arm -- "no seat invoked anything" -- is UNMEETABLE
  while the round works. Re-cut it to the CAUSAL form, or spend an idle night?**
  Measured by `2.0.0_SA_COO~A`: SEAT_INVOCATIONS_IN_WINDOW = 2150 of 2150, because that
  seat was driving the round all night. The arm and the work compete for the same hours,
  and every night since TO-CG-D-1's pins landed has been a worked night. Re-handing the
  order fails again tomorrow. The bar comes from the CELL, and the decomposition is
  FROZEN mid-round, so the change is L5's and above that seat's limb.
  --------------------------------------------------------------------
  **REC --** re-cut the second arm to the causal form: *no invocation in the window CAUSED
  the rebuild*. `2.0.0_SA_COO~A`'s recommendation, reached independently by the worker first.
  --------------------------------------------------------------------
  **RULING -- ADOPTED, and it is a CORRECTION rather than a scope change, because the cell
  already carries the causal form in its own DONE WHEN.**

  1. THE PROXY IS THE OUTLIER INSIDE ITS OWN CELL. CG-x-2's DONE WHEN reads "...no question is
     ever the reason a rebuild starts" -- CAUSAL. Its limb (i) then asks for "no seat invoked
     anything" -- a PROXY. The PRD's acceptance 2 at :164 reads, verbatim, "no question is
     ever the cause of a rebuild. (FWD-2)". So the causal form is what the endpoint, the PRD
     and the cell's own headline all say; the proxy is a restatement that drifted from the
     sentence directly above it. Re-cutting the arm makes the limb match its own cell.
  2. THE PROXY IS STRICTLY WEAKER THAN THE THING IT STANDS FOR. An idle night proves nobody
     asked. It does not prove that asking would not have caused a rebuild -- which is the
     claim FWD-2 actually makes. The causal arm is both measurable on a WORKED night and a
     STRONGER statement of the same property.
  3. THE CELL ALREADY DISTRUSTED IT. Limb (i)'s own parenthetical says "a zero-invocation
     window is not evidence for limb iii". The cell knew the proxy was thin one limb over.
  4. THE ALTERNATIVE COSTS A DAY AND BUYS LESS. A deliberately idle night stalls the round
     and yields the weaker claim. That is `2.0.0_SA_COO~A`'s line and it is correct.

  SCOPE OF THE RULING: limb (i)'s SECOND ARM only. The first arm (the pointer's manifest
  vintage later than the previous evening's) is untouched and still binds. Limbs (ii) and
  (iii) are untouched. FWD-2 is not amended and needs no endpoint change -- this ruling
  moves an instrument INTO line with the outcome, never the outcome toward the instrument.
+---------------------------------------------------------------------+
```

---

## The two instrument defects: `2.0.0_SA_COO~A`'s, and holding them was right

That seat held both pending this ruling rather than amending twice. Correct, and they should now land in
ONE amendment with the arm re-cut.

**Defect 1 is the serious one and it fails in the FALSE-GREEN direction.** The face filters telemetry rows
"naming kuzu|derive|projection|globgrph|comp-blast|run-task", and the telemetry carries NO command or argument
field at all -- a row's keys are `['agent','kind','session_id','tool','ts']`, where `tool` is the tool NAME
("Bash"), never the command. So the filter returns 0 for a STRUCTURAL reason and **would certify a fully
worked night as unattended**. That is the same class as tonight's argv cliff and the corpus pass's worktree
read: an instrument that answers a question it was never able to ask, in the direction that reads clean.

⛔ **AND THAT SEAT'S OWN DISCRIMINATION IS THE PART TO KEEP:** this is NOT S47. S47 found the telemetry PATH
invisible from a worktree; fixing the path does not fix the filter, and a seat that fixed only the path would
get the SAME false green with the defect apparently closed. Two defects on one surface, one of which hides the
other.

**Defect 2** -- the legitimate-starter enumeration names TWO starters where the window holds FOUR -- convicted
a chronos-scheduled producer as a human invocation. The worker's classifier caught it only because its
per-row labels disagreed with its own count, which is the shape of control worth keeping in the re-cut.

**Note for the amendment, so it is done once:** with the arm re-cut to the causal form, defect 1's filter is
no longer asked "did anyone invoke anything" but "did an invocation CAUSE this rebuild" -- a different
instrument, keyed on the rebuild's own trigger rather than on a name-match over rows that carry no command.
Re-cut the instrument with the arm, not after it.

## Not this seat's, and correctly routed elsewhere

**D9-AC3's clock is `3.0.0_SA_CVO`'s.** STAMP->ANSWER is 82.186 s on the estate's clock and 2660.328 s on the
worker's wall clock; it PASSES under the first and FAILS under the second. Both numbers are in the record, so
L9 grades either without a re-run. `2.0.0_SA_COO~A` declined to choose for the CVO and that is the right
boundary.

**D9-AC4 is an honest NOT-CAUGHT** (BEHIND_CAUGHT=false after 27 client reads and 138 marker polls over
55m30s; the marker sat unchanged 88 minutes). The worker refused to provoke a stamp because doing so
**would have manufactured the very event the criterion exists to observe**. That refusal is correct and is
worth the record: an arm satisfied by staging its own trigger measures the stager, not the world.

## What happens next, and none of it waits on Andrew

`2.0.0_SA_COO~A` amends TO-CG-D-9's CG-x-2 limb (i) second arm to the causal form, folds both instrument
defects into the same amendment, and re-hands the order. The decomposition's frozen text is corrected for this
one arm on this ruling, cited by id. D-10, D-11, D-7 and D-8 stay gated behind D-9 as they are.
