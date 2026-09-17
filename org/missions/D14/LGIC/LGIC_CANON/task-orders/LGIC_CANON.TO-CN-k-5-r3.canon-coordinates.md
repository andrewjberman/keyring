# TO LGIC_CANON.TO-CN-k-5-r3 -- the canon: four coordinates, v1.1 title and census by recount, R1's census vintage, A-6 restated

<to_id>LGIC_CANON.TO-CN-k-5-r3</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.5 (ADMITTED; both halves current) | **Decomp cell:** `CN-k-5` (decomposition v5.1, section 0e) | **outcome_ref:** FWD-1 | **depends_on:** CN-k-4 (same slot, continues after its drain) -- level 0; CN-j-8, CN-j-9, CN-j-10 wait on this drain

---

## WORKER FACE

### THE CELL

`CN-k-5` -- rulings R-9 (iii), A-19, A-4 and A-6 restated (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md` R-9; `org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND2_ANALYSIS.md` s.2). **You edit `infra/logic/02_DOCTRINE.md` and `infra/logic/10_ONBOARDING_CHECKLIST.md`.** You continue on the tree CN-k-4 left; never touch the generated naming section by hand.

**WHY.** Round 2's blind judges split on six cells, and every split traced to one of FOUR places where the canon does not decide (R-9). The judges could not agree because the text is silent; this cell makes it speak.

1. **The four coordinates.** For each, add ONE line inside the named rule block, opening with the same middle-dot field marker the block's other fields use, followed by exactly `resolves R-9(iii) C<k>:`, and naming the counterpart shown, which states the canon's answer and the rule text it rests on:
   - **C1, in R10, naming R9** -- monolith SILVER clearance. R9's census clears monolith bronze on the live bucket-policy deny; R10 carries no equivalent clearance, so judges split CONFORMS vs UNDETERMINED on `orion/inflection/silver/` and `eclipse/inflection/silver/` axis A5.
   - **C2, in R1, naming census** -- R1's key grammar against R1's own census clearance ("53 of 53 ... CONFORMANT"): does that clearance decide axis A3 for a monolith plane, or is each key graded against the generated grammar.
   - **C3, in R6, naming R5** -- a firm's SHORT-FORM legacy bucket (`opal-data-inf` for `inflection`): whether R5/R6's which-bucket text reads it as the firm's bucket (judges split VIOLATES vs CONFORMS on its gold and platinum).
   - **C4, in R19, naming R18** -- duration and in-flight status: how a plane whose MIGRATE is in flight and still written is graded while the migration runs, against R18's dual-write clause.
   The splits are recorded in `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-compare-r2.md` s.1 (rows D1-D6). **Write the answer the existing rulings already give** (cite them); where an answer would need a sovereign call no record makes, write the line as `UNDECIDED -- Andrew's call: <the call>` and file a BLOCKING row -- never invent a ruling.
2. **Title and census by recount (A-19).** Line 1 reads `v1.1`. Section 0's line `RULES CARRYING ALL THREE PARTS: <a> of <b>` is RECOUNTED by rule block (a line opening `**R<n>` up to the next rule, heading or `---` line; a block carries all three parts when it has `authority:`, `census:` and `non-application:`), never typed. Measured at the cut: 22 blocks, the line reads `21 of 21`. Add a v1.1 entry to section 7's change log.
3. **R1's census vintage (A-4).** R1's `census:` field line gains its vintage in the form `(as of <source> @<commit>)` or `(as of <YYYY-MM-DD>)`. Section 0 dates every census tag to `01_CENSUS.md @d35653da5e`; check whether R1's claim predates the source-first ruling of 2026-09-13 ~03:2xZ and write the vintage that is TRUE.
4. **A-6 restated, in the checklist's INPUTS words.** In `## THE INPUTS -- ...` of `infra/logic/10_ONBOARDING_CHECKLIST.md`, the SHORT-form row's mark becomes `**SOVEREIGN**`, and its who-gives cell says: supplied ONCE on the identity row (by Andrew, or by the CRO in the registry on his word) and READ thereafter by every builder -- `name()` looks the short form up on the row and `validate()` refuses a FIRM row without one; no derivation is built. The count sentence under the table (`Nine rows: ...`) is re-counted from the marks.

**Read:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md` R-9; `org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND2_ANALYSIS.md` s.2 (A-4, A-6 RESTATED, A-19); `infra/logic/02_DOCTRINE.md` section 0, R1, R5, R6, R9, R10, R18, R19; `lib/opal_naming.py` `name` and `validate` (to cite A-6's mechanism).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="K5R3-AC1" cell_refs="CN-k-5"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py k5-census</invocation><expect>PASS-K5-CENSUS-RECOUNTED</expect></criterion>

<criterion id="K5R3-AC2" cell_refs="CN-k-5"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py k5-coordinates</invocation><expect>PASS-K5-FOUR-COORDINATES</expect></criterion>

<criterion id="K5R3-AC3" cell_refs="CN-k-5"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py k5-r1-vintage</invocation><expect>PASS-K5-R1-CENSUS-VINTAGED</expect></criterion>

<criterion id="K5R3-AC4" cell_refs="CN-k-5"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py k5-short-sovereign</invocation><expect>PASS-K5-SHORT-SOVEREIGN-READ</expect></criterion>

<criterion id="K5R3-AC5" cell_refs="CN-k-5"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py o3-sovereign</invocation><expect>PASS-O3-SOVEREIGN-ROWS-COUNTED</expect></criterion>

<criterion id="K5R3-AC6" cell_refs="CN-k-5"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k4-fresh</invocation><expect>PASS-K4-RERENDERED-AT-SCHEMA</expect></criterion>

<criterion id="K5R3-AC7" cell_refs="CN-k-5" judgment="true"/>

<expected_criteria>K5R3-AC1, K5R3-AC2, K5R3-AC3, K5R3-AC4, K5R3-AC5, K5R3-AC6, K5R3-AC7</expected_criteria>

**AC1-AC4 read RED at the cut** (title v1.0 and `21 of 21` against 22 blocks; 0 of 4 coordinates; R1's census line has no vintage; the SHORT row reads `SOVEREIGN where Andrew gives one, else DERIVED`). **AC5 reads PASS at the cut and must still pass. AC6 reads PASS once CN-k-4 has drained and must still pass after your edits.** **K5R3-AC7, for `3.0.0_SA_CVO` at L9:** each coordinate line answers the split it names from rulings that exist (or is marked UNDECIDED with a BLOCKING row), the R1 vintage is true, and A-6's words match `name()`/`validate()`.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including everything under `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array in the file, id `LGIC_CANON-W<n>-S<k>` (`<n>` your slot; `<k>` ONE ABOVE the highest `LGIC_CANON-W<n>-S` id already present in ANY document under `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/` -- slot numbers were used in earlier rounds, so `S1` is usually taken). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Do not change any rule's substance beyond the four coordinate lines, the R1 vintage and the title/count/change log.** A wider canon edit is a surprise row.

<paths>
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
infra/logic/02_DOCTRINE.md
infra/logic/10_ONBOARDING_CHECKLIST.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v5.1, round-3 cell `CN-k-5` (section 0e).
<owned_cells>CN-k-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `K5R3-AC1`, `K5R3-AC2`, `K5R3-AC3`, `K5R3-AC4`, `K5R3-AC5`, `K5R3-AC6`, `K5R3-AC7`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.TO-CN-k-5-r3.canon-coordinates.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> K5R3-AC1,K5R3-AC2,K5R3-AC3,K5R3-AC4,K5R3-AC5,K5R3-AC6,K5R3-AC7 --governing-order org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-k-5-r3.canon-coordinates.md` BEFORE the `complete` flip.
Result file `canon-coordinates.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`K5R3-AC7` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C only.
comp-iam: DECLARED-NOT-APPLICABLE -- repository documents only; no principal, policy or resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- the cited rulings are this project's own records; the coordinates are graded at L9.
lane: the <paths> block is the grant; both files were granted to round-2 workers the same way.
contention: 02_DOCTRINE.md is also CN-k-4's; same slot ~1, in sequence. The judges (slots ~3, ~4, ~5) are never this slot, so no judge wrote the canon it judges.
</preflight>

Seating: slot ~1, queue position 2. Round 3 of LGIC_CANON, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND2_ANALYSIS.md` @4a55888962); issued by `2.0.0_SA_COO~G`. Decomposition v5.1, section 0e. Rulings carried: R-9 (iii), A-19, A-4, A-6 restated.
