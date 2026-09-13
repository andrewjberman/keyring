# TO POSN_ASTTAX.TO-U3-1 -- DURABILITY: extend preserve-don't-clobber to seed_canonical_securities.py so a re-seed cannot revert a five-class value (AT4-s-3, FWD-5/FWD-1)

<to_id>POSN_ASTTAX.TO-U3-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~16</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-13</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.6**
@`ae66157381` - **Decomp cell:** `AT4-s-3` - **Issuance:** round 4. **INDEPENDENT.**

---

## THE CELL

Round 3's `AT3-s-4` proved the classification list survives a re-seed for ONE writer, and surfaced
row `W14-S3` naming a SECOND: **`seed_canonical_securities.py`, with 4 of its 11 members carrying a
two-value vocabulary.** That row was left in no triple at the close of round 3. This cell closes it.

**The durability property is the point, not the edit:** a value that is correct until somebody runs a
routine script is not durable, and FWD-5 ("defined in one place and it flows") cannot be true while a
re-seed silently reverts it.

### THE HARD STOP THAT SHAPES YOUR METHOD

**NEVER run the seeding script against the live table.** Round 3's equivalent cell proved its claim
with a before-and-after control **against a scratch copy**, and the live table was never touched.
Do the same. A mutation control must snapshot BYTES, never the index -- a git-native restore
(`stash`, `checkout --`, `show :path`) has already destroyed a peer's uncommitted work in this estate.

---

## CRITERIA -- one clause each

**AC1 -- MEASURE the current behaviour before changing anything.**
**INVOCATION:** on a scratch copy, seed a record carrying a five-class value, re-run the seeding
path, and read the value back.
**EXPECTATION:** the measured BEFORE state, stated as a value and not as a description. If it does
NOT clobber, say so plainly -- a cell that finds its premise false has done its job, and you stop at
AC1 with that recorded.

**AC2 -- Implement preserve-don't-clobber in `seed_canonical_securities.py`.**
**INVOCATION:** the change itself, matching the mechanism the sibling writer already uses -- read it
rather than inventing a second pattern.
**EXPECTATION:** the diff, and a statement of which existing behaviour it does NOT change (a first
mint must still mint).

**AC3 -- Prove it with a control that FAILS in the broken world.**
**INVOCATION:** re-run AC1's exercise against the patched script on the scratch copy.
**EXPECTATION:** the five-class value SURVIVES. **POSITIVE CONTROL, REQUIRED:** the same run must
still mint a record that does not yet exist -- a script that preserves everything by refusing to
write at all would pass AC3 and be worthless.
**NEGATIVE CONTROL, REQUIRED:** the pre-patch script, same input, must still revert. If both read the
same, your control is not discriminating and you report that rather than the result.

**AC4 -- Pass the commit gate on your own bytes.**
**INVOCATION:** `.tools/commit-gate.sh` over the changed `.py`.
**EXPECTATION:** clean, cited. The ASCII limb's commit-MESSAGE arm is BLOCKING; a staged `.py` arm is
WARN-ONLY and ships -- check both rather than the one that stopped you.

## SURPRISE ROWS

Off-cell findings: ONE row as `POSN_ASTTAX-W16-S<k>`, then keep working.

## CRITERIA -- structured, one clause each

<criterion id="U3-AC1" cell_refs="AT4-s-3"><invocation>timeout 300 python &lt;your BEFORE control on a SCRATCH copy&gt;</invocation><expect>on a SCRATCH copy only -- never the live table -- seed a record carrying a five-class value, re-run the seeding path, read the value back, and state the BEFORE result as a VALUE, not a description. If it does NOT clobber, say so plainly and stop here: a cell that finds its premise false has done its job. Name the scratch target explicitly so a reader can see the live table was untouched.</expect></criterion> `U3-AC1` -- MEASURE BEFORE CHANGING. W14-S3 asserts the clobber; this clause TESTS that premise rather than confirming it.

<criterion id="U3-AC2" cell_refs="AT4-s-3"><invocation>timeout 180 git diff -- infra/aws/lambda/v2_portal/yang_pipeline/seed_canonical_securities.py</invocation><expect>the diff implementing preserve-don-t-clobber, matching the mechanism the SIBLING writer already uses -- read that writer and reuse its pattern rather than inventing a second one. Plus one line naming what the change does NOT alter: a first mint must still mint.</expect></criterion> `U3-AC2` -- THE CHANGE, AND WHAT IT DELIBERATELY LEAVES ALONE.

<criterion id="U3-AC3" cell_refs="AT4-s-3"><invocation>timeout 300 python &lt;your AFTER control, same scratch exercise&gt;</invocation><expect>the five-class value SURVIVES the re-seed. POSITIVE CONTROL, REQUIRED: the same run still MINTS a record that did not previously exist -- a script that preserves everything by refusing to write at all would pass this clause and be worthless. NEGATIVE CONTROL, REQUIRED: the pre-patch script on the same input still reverts. If both arms read the same, the control is not discriminating and you report that rather than the result.</expect></criterion> `U3-AC3` -- THE PROOF, WITH BOTH CONTROLS FIRING.

<criterion id="U3-AC4" cell_refs="AT4-s-3"><invocation>timeout 180 bash .tools/commit-gate.sh</invocation><expect>clean on the changed .py, output cited. Check BOTH ASCII limbs and say so: the commit-MESSAGE arm is BLOCKING while a staged .py arm is WARN-ONLY and ships, so clearing the one that stopped you teaches nothing about the other.</expect></criterion> `U3-AC4` -- THE GATE, BOTH LIMBS.

<expected_criteria>U3-AC1, U3-AC2, U3-AC3, U3-AC4</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-U3-1.extend-preserve-dont-clobber-to-the-seed-script.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~16/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/yang_pipeline/seed_canonical_securities.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round4.md</decomp_doc> round 4, cell `AT4-s-3`.
<owned_cells>AT4-s-3</owned_cells>
Read-dependencies, NOT claimed: round 3's `AT3-s-4` (the first writer's preserve-don't-clobber, terminal) and row `W14-S3`, which named this second writer. READ them; do not re-run that cell.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no job, monitor, alarm or alerting built or changed; the
seeding script is run ad hoc against a SCRATCH copy only.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied, THREE items: (1) the issuer has NOT verified that this script currently clobbers -- `W14-S3`
asserts it and AC1 exists to test that premise, not to confirm it; (2) the live table is OUT OF
SCOPE and must not be written, so the evidence is scratch-copy evidence and is scoped as such;
(3) the issuer names no target for how many of the 11 members are affected -- "4 of 11" is the row's
figure and is to be re-measured, not inherited.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~16/POSN_ASTTAX.TO-U3-1.proof_of_spec.json
</proof_of_spec>
