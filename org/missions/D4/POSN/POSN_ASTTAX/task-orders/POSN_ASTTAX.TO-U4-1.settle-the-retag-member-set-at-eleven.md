# TO POSN_ASTTAX.TO-U4-1 -- SETTLE the retag member set by SUBTRACTION over a printed denominator; the standing figure is ELEVEN and it is to be re-derived, not confirmed (AT4-s-4, FWD-1)

<to_id>POSN_ASTTAX.TO-U4-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~17</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-13</issued_date>
<status>complete</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.6**
@`ae66157381` - **Decomp cell:** `AT4-s-4` - **Issuance:** round 4. **INDEPENDENT. RECORD ONLY.**

---

## THE CELL

Round 3 left the retag set as a durability item in no triple: **settle the member set at ELEVEN.**
The retag itself is **NO-GO** and is NOT yours -- `TO-T6-1` stays unspawned. This cell settles WHICH
members the retag would touch, so that whenever the retag is unblocked it runs against a derived set
rather than a remembered one.

### THE METHOD IS THE DELIVERABLE

**ELEVEN IS A STANDING FIGURE, NOT A TARGET.** Derive the set yourself and print the denominator. If
your derivation returns a number other than eleven, **that is the finding** -- report it with the
delta named member by member. A cell that reproduces a remembered number by looking for it has
measured nothing.

**Write the enumeration as `the printed denominator MINUS what you exclude`, never as a forward list
of members you thought of.** A forward list covers what its author had in mind and omits silently;
the same set written as a subtraction cannot lose a member without the count disagreeing.
**And the domain is itself a claim:** run ONE unscoped read of the classification term over the
corpus with its denominator printed, and compare it against what your chosen domain holds. A member
the domain does not hold VOIDS the subtraction. A wrong domain returning EMPTY gets acted on, which
is why this clause is here.

---

## CRITERIA -- one clause each

**AC1 -- Print the DENOMINATOR you subtract from**, with the instrument named and its vintage.
**EXPECTATION:** a count and the population it counts, cited.

**AC2 -- Derive the retag member set by subtraction.**
**INVOCATION:** denominator MINUS each stated exclusion, each exclusion carrying its reason.
**EXPECTATION:** the member set and its size. **If it is not eleven, name every member of the
difference in both directions** -- present-but-unexpected and expected-but-absent.

**AC3 -- For each member, record current class and target class**, cited `file:line @ <commit-ish>`
or the store and key it was read from.
**EXPECTATION:** a (member, current, target) table with no blanks. A member whose target cannot be
determined is recorded as UNDETERMINED with the reason -- never guessed, never omitted.

**AC4 -- Falsify the domain once, out loud.**
**INVOCATION:** one UNSCOPED read of the classification term over the corpus, denominator printed.
**EXPECTATION:** either a statement that every hit lies inside your chosen domain, or the list of
hits that do not -- and if any does, AC2's subtraction is VOID and you say so rather than keeping the
number.

**THIS CELL SPAWNS NOTHING AND RETAGS NOTHING.** It produces a record. The retag remains NO-GO.

## SURPRISE ROWS

Off-cell findings: ONE row as `POSN_ASTTAX-W17-S<k>`, then keep working.

## CRITERIA -- structured, one clause each

<criterion id="U4-AC1" cell_refs="AT4-s-4"><invocation>timeout 300 comp-find &lt;the classification term you choose&gt; --all --files</invocation><expect>the DENOMINATOR you will subtract from, with the instrument named and its vintage printed. A count and the population it counts, cited.</expect></criterion> `U4-AC1` -- THE DENOMINATOR, FIRST.

<criterion id="U4-AC2" cell_refs="AT4-s-4"><invocation>timeout 180 python &lt;your subtraction&gt;</invocation><expect>the member set written as DENOMINATOR MINUS each stated exclusion, every exclusion carrying its reason -- never as a forward list of members you thought of. State the resulting size. ELEVEN is a STANDING FIGURE carried from round 3 and is the thing being TESTED, not the answer to reproduce: if your derivation returns another number, name every member of the difference in BOTH directions, present-but-unexpected and expected-but-absent.</expect></criterion> `U4-AC2` -- THE SET, BY SUBTRACTION. A forward list omits silently; a subtraction cannot lose a member without the count disagreeing.

<criterion id="U4-AC3" cell_refs="AT4-s-4"><invocation>timeout 180 python &lt;your member table&gt;</invocation><expect>per member: current class and target class, cited file:line @ &lt;commit-ish&gt; or the store and key it was read from. No blanks. A member whose target cannot be determined is recorded UNDETERMINED with its reason -- never guessed, never omitted.</expect></criterion> `U4-AC3` -- EVERY MEMBER, WITH ITS PROVENANCE.

<criterion id="U4-AC4" cell_refs="AT4-s-4"><invocation>timeout 300 comp-find &lt;the same term, UNSCOPED&gt; --all --files</invocation><expect>one UNSCOPED read over the corpus with its denominator printed, compared against what your chosen domain holds. Either state that every hit lies inside the domain, or list the hits that do not -- and if any does, AC2 subtraction is VOID and you say so rather than keeping the number. A wrong domain returning EMPTY gets acted on, which is why this clause exists.</expect></criterion> `U4-AC4` -- FALSIFY THE DOMAIN ONCE, OUT LOUD. Choosing the domain is itself a claim.

<expected_criteria>U4-AC1, U4-AC2, U4-AC3, U4-AC4</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-U4-1.settle-the-retag-member-set-at-eleven.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~17/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round4.md</decomp_doc> round 4, cell `AT4-s-4`.
<owned_cells>AT4-s-4</owned_cells>
Read-dependencies, NOT claimed: `TO-T6-1` (the retag) is NO-GO, carried, and NOT yours -- do not flip it, do not spawn against it. Round 3's bar `AT3-s-5` priced ten change-groups; READ that instance rather than re-deriving it.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only; no job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied, THREE items: (1) the issuer has NOT re-derived this set and ELEVEN is a STANDING FIGURE
carried from round 3, offered as the thing to test rather than the answer to reproduce; (2) the
retag is NO-GO and nothing in this cell changes that, so a settled member set does not imply the
retag may run; (3) the issuer names no domain for the subtraction -- choosing it is part of the cell
and AC4 exists because that choice is itself a claim.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~17/POSN_ASTTAX.TO-U4-1.proof_of_spec.json
</proof_of_spec>
