# TO POSN_ASTTAX.TO-U1-1 -- DERIVE every reader that renders an asset-class label, and grade EACH against the FIVE-CLASS bar (AT4-s-1, FWD-6). READ-ONLY. THE PORTAL IS FROZEN

<to_id>POSN_ASTTAX.TO-U1-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~15</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-13</issued_date>
<status>complete</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.6**
@`ae66157381` - **Decomp cell:** `AT4-s-1` - **Issuance:** round 4. **GATES `AT4-s-2`.**

---

## THE CELL

**FWD-6, verbatim from the PRD v0.6 endpoint block: "The places that show asset classes agree with
each other."** No cell has ever been cut against it in three rounds. This is that cell.

### THE OBVIOUS BAR IS THE WRONG BAR -- read this before the first command

**DO NOT grade "do the views agree."** They DO agree today -- because each carries its own copy of
the same wrong two-class list. **A criterion built on agreement returns PASS on the broken system.**
That is the `S2-AC5` shape this project has now hit three times, and it is why this outcome is being
cut with a different bar rather than the one its own sentence suggests.

>> **YOUR BAR IS: CAN EACH READER DISPLAY ALL FIVE RATIFIED CLASSES?** It fails in today's world and
   passes only when the world is fixed. <<

Read the five ratified class names from the PRD at `ae66157381`. Do not retype them from this order.

### THE PORTAL IS FROZEN. YOU READ IT. YOU DO NOT WRITE IT.

Andrew's freeze, restated twice inside his 03:21Z direction. **READING portal source is permitted and
is explicitly not a write.** Your `<paths>` grant contains NO portal path -- if you find yourself
editing one, stop: you are outside your grant and have misread the cell. You produce a CENSUS and a
PRICE. You change nothing.

---

## CRITERIA -- one clause each

**AC1 -- DERIVE the reader set; do not inherit it.**
PRD surface row S3 says *"The two surfaces."* The round-3 analysis states the world holds **at least
three** readers, and that *"a surface row scoped to two cannot generate a cell that checks three."*
**INVOCATION:** enumerate candidate readers by SUBTRACTION over a PRINTED DENOMINATOR of portal
source files, never as a forward list of files you thought of. Print the denominator line.
**EXPECTATION:** a reader set with its denominator and its derivation shown. **If your set has
exactly two members, state explicitly how you excluded the third** -- the analysis says it exists.

**AC2 -- For EACH reader in AC1's set, print the class vocabulary it can display.**
**INVOCATION:** cite the literal list at `file:line @ <commit-ish>`. A citation without a vintage is
not a citation.
**EXPECTATION:** one verbatim vocabulary per reader, each with its pin.

**AC3 -- Grade each reader against the FIVE-CLASS bar, and name what drops each class.**
**INVOCATION:** for each reader, for each of the five ratified classes, can that class reach the
screen? Name the mechanism that drops it (a hardcoded literal, a type union, a two-key map).
**EXPECTATION:** a (reader, class, verdict, mechanism) table.
**NEGATIVE CONTROL, REQUIRED:** include one class you expect to PASS on every reader. If every cell
of your table reads the same value, your instrument is not discriminating -- say so rather than
report the table.

**AC4 -- Price the smallest change per failing (reader, class).**
**INVOCATION:** the smallest change that would let it render, at `file:line`, and whether that file
is under `portal/` (FROZEN) or not (OWNED).
**EXPECTATION:** a priced list, every row marked FROZEN or OWNED. **This is the deliverable Andrew
needs in order to decide the freeze**, and it is worth more than a verdict.

**DO NOT claim FWD-6 REALIZED.** This cell COVERS the outcome; it does not serve it. Covering and
serving are different populations, and conflating them is the exact defect PRD v0.6 item 2 exists to
stop.

## SURPRISE ROWS

Anything off-cell: append ONE row to the project channel as `POSN_ASTTAX-W15-S<k>` and KEEP WORKING.
Never halt to investigate.

## CRITERIA -- structured, one clause each

<criterion id="U1-AC1" cell_refs="AT4-s-1"><invocation>timeout 300 comp-find &lt;the asset-class rendering term you choose&gt; --all --files</invocation><expect>the printed DENOMINATOR (files scanned) and the full file list, never a page. Then the READER SET as a SUBTRACTION: start from every portal source file this enumeration reaches, subtract each one you PROVE cannot render an asset-class label, and name the proof per subtraction. State the surviving set as a count and by name. PRD surface row S3 names TWO; the round-3 analysis says the world holds AT LEAST THREE. If your set has exactly two members, state explicitly how you excluded the third.</expect></criterion> `U1-AC1` -- THE READER SET, BY SUBTRACTION, WITH ITS DENOMINATOR. A denominator certifies the SWEEP, never the SET.

<criterion id="U1-AC2" cell_refs="AT4-s-1"><invocation>timeout 180 python &lt;your vocabulary read, per reader&gt;</invocation><expect>for EACH reader in your AC1 set: the class vocabulary it can display, quoted VERBATIM, cited file:line @ &lt;commit-ish&gt;. A citation without a vintage is not a citation. Where the vocabulary is a hardcoded literal, paste the literal.</expect></criterion> `U1-AC2` -- WHAT EACH READER CAN SAY, IN ITS OWN BYTES.

<criterion id="U1-AC3" cell_refs="AT4-s-1"><invocation>timeout 180 python &lt;your five-class grade, per reader per class&gt;</invocation><expect>the full READER x CLASS table. For each of the five ratified classes read from the PRD at ae66157381, can that class reach the screen on that reader -- PASS or FAIL -- and for each FAIL name the MECHANISM that drops it (a hardcoded literal, a type union, a two-key map), cited file:line. NEGATIVE CONTROL, REQUIRED: include one class you expect to PASS on every reader and show it passing. If every cell of the table reads the same value, your instrument is not discriminating -- say so and do not report the table as a result.</expect></criterion> `U1-AC3` -- THE BAR. ** DO NOT grade "do the views agree" -- they agree today because each carries the same wrong two-class list, so an agreement bar reads PASS on the broken system.**

<criterion id="U1-AC4" cell_refs="AT4-s-1"><invocation>timeout 120 python &lt;your pricing table&gt;</invocation><expect>for EACH failing (reader, class): the SMALLEST change that would let it render, at file:line, and whether that file is under portal/ -- marked FROZEN -- or outside it, marked OWNED. Count and print both totals. This table is what Andrew needs to decide the freeze; it is worth more than a verdict.</expect></criterion> `U1-AC4` -- THE PRICE, PER FAILURE, WITH THE FREEZE BOUNDARY MARKED.

<criterion id="U1-AC5" cell_refs="AT4-s-1"><invocation>timeout 120 python -c "print('COVERAGE STATED, NOT REALIZATION')"</invocation><expect>one explicit line stating that this cell COVERS FWD-6 and does NOT serve it, with the reason: the bar is EXERCISED and this evidence is SOURCE-AT-PIN because the portal is frozen and this worker has no rendered DOM. Do NOT grade FWD-6 REALIZED.</expect></criterion> `U1-AC5` -- THE HONEST GRAIN. Covering and serving are different populations.

<criterion id="U1-AC6" cell_refs="AT4-s-1" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether the reader set derived in AC1 is genuinely the set that renders an asset-class label, or merely the set reachable with the instruments at hand. Record the readings and offer NO verdict.</expect></criterion> `U1-AC6` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>U1-AC1, U1-AC2, U1-AC3, U1-AC4, U1-AC5, U1-AC6</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-U1-1.derive-the-readers-and-grade-the-five-class-bar.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~15/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round4.md</decomp_doc> round 4, cell `AT4-s-1`.
<owned_cells>AT4-s-1</owned_cells>
Read-dependencies, NOT claimed: round 3's `AT3-s-2` and `AT3-s-3` measured two collapse sites -- READ their rows, do not re-run their cells. `AT4-s-2` consumes YOUR census and is NOT yours.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only; no job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; repository source reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied, THREE items: (1) the issuer has NOT run this census and is NOT predicting the reader count --
"at least three" is the round-3 analysis's figure, not a target to hit; (2) the portal is FROZEN, so
every finding here is SOURCE-AT-PIN and no rendered DOM is available to this worker, and the criteria
are cut to that grain deliberately rather than cut unsatisfiable; (3) the issuer holds no view on
whether any reader already passes.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~15/POSN_ASTTAX.TO-U1-1.proof_of_spec.json
</proof_of_spec>
