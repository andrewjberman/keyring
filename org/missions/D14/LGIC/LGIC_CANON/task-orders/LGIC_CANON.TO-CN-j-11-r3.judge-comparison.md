# TO LGIC_CANON.TO-CN-j-11-r3 -- the comparison: intersection and positive control first, the roll-up recounted, every divergence traced

<to_id>LGIC_CANON.TO-CN-j-11-r3</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.5 (ADMITTED; both halves current) | **Decomp cell:** `CN-j-11` (decomposition v5.1, section 0e) | **outcome_ref:** FWD-1 | **depends_on:** CN-j-8, CN-j-9, CN-j-10 -- level 2; continues slot ~2 after CN-l-3

---

## WORKER FACE

### THE CELL

`CN-j-11` -- rulings R-9 (ii) and A-17 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md` R-9; `org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND2_ANALYSIS.md` s.2). **You write ONE file: `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r3/judge-compare-r3.md`.**

**WHY.** Round 2's comparison ran over an EMPTY plane intersection and compared vocabularies, so it could only return "no divergence". This one prints its population first and compares the ROLL-UP -- each judge's single most-severe finding per plane -- which is the ORDER question: judges F and G were BRIEFED with a severity order, judge H was not.

**INPUTS** (read columns BY NAME from the header, never by position): `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r3/judge-f.tsv`, `judge-g.tsv`, `judge-h.tsv`; the tree `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/CN_TREE_R3.md` (its planes are the denominator `m`); `infra/logic/02_DOCTRINE.md`.

**THE FILE, lines starting at column 0, in THIS order:**
1. `PLANE INTERSECTION F.G.H: <n> of <m>` -- planes present in all three answer files, over the tree's planes.
2. `POSITIVE CONTROL F.F: <k> of <k>` -- judge F intersected with itself (its row count), which proves the intersection instrument can return a full set.
3. Only after both: `ROLL-UP AGREE F.G.H: <a> of <n>`, `ROLL-UP AGREE F.G: <a> of <n>`, `ROLL-UP AGREE F.H: <a> of <n>`, `ROLL-UP AGREE G.H: <a> of <n>` -- planes on which those judges' `worst_verdict` values are identical, over the intersection.
4. `ROLL-UP DIVERGE: <d> of <n>` -- planes where the three `worst_verdict` values are not all equal; then ONE line per such plane starting `DIVERGE <plane> ` that names each judge's `worst_verdict` and `worst_rule` and cites the canon coordinate the split traces to as `infra/logic/02_DOCTRINE.md:<line>` at your HEAD.
5. `UNION REACHED: <k> of 6` with the list -- the union of the three `reach` columns over `R3, R8, R14, R15, R19, R21`.
6. A short prose section: did the unbriefed H diverge from the briefed pair (F.H and G.H) more than F diverged from G (F.G)? Say what the numbers do and do not show; could the arms have diverged on this tree, and did they?

Every number is COUNTED from the three files, never typed from memory; the criteria recount each one.

**Read:** the three answer files, the tree, the canon; `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md` R-9.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="J11R3-AC1" cell_refs="CN-j-11"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py j11-intersection</invocation><expect>PASS-J11-INTERSECTION-FIRST</expect></criterion>

<criterion id="J11R3-AC2" cell_refs="CN-j-11"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py j11-rollup</invocation><expect>PASS-J11-ROLLUP-RECOUNTED</expect></criterion>

<criterion id="J11R3-AC3" cell_refs="CN-j-11"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py j11-traced</invocation><expect>PASS-J11-DIVERGENCE-TRACED</expect></criterion>

<criterion id="J11R3-AC4" cell_refs="CN-j-11"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py j11-reach</invocation><expect>PASS-J11-UNION-REACH</expect></criterion>

<criterion id="J11R3-AC5" cell_refs="CN-j-11" judgment="true"/>

<expected_criteria>J11R3-AC1, J11R3-AC2, J11R3-AC3, J11R3-AC4, J11R3-AC5</expected_criteria>

**AC1-AC4 read RED at the cut** (no comparison, no answer files). **J11R3-AC5, for `3.0.0_SA_CVO` at L9 (row S6 disarms here if the arms could have diverged and did not; the word is `1.0.0_SA_CTO`'s):** every divergence traces to a canon coordinate that actually decides it, and the briefed-versus-unbriefed paragraph claims no more than the counts support.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including everything under `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array in the file, id `LGIC_CANON-W<n>-S<k>` (`<n>` your slot; `<k>` ONE ABOVE the highest `LGIC_CANON-W<n>-S` id already present in ANY document under `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/` -- slot numbers were used in earlier rounds, so `S1` is usually taken). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Do not edit the judges' files.** A row you believe is malformed is a surprise row, and you compare what is there.

<paths>
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r3/judge-compare-r3.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v5.1, round-3 cell `CN-j-11` (section 0e).
<owned_cells>CN-j-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `J11R3-AC1`, `J11R3-AC2`, `J11R3-AC3`, `J11R3-AC4`, `J11R3-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/LGIC_CANON.TO-CN-j-11-r3.judge-comparison.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> J11R3-AC1,J11R3-AC2,J11R3-AC3,J11R3-AC4,J11R3-AC5 --governing-order org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-j-11-r3.judge-comparison.md` BEFORE the `complete` flip.
Result file `judge-comparison.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`J11R3-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C only.
comp-iam: DECLARED-NOT-APPLICABLE -- repository documents only; no principal, policy or resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are the three round-3 answer files.
lane: the <paths> block is the grant.
contention: written by this cell alone; the judges' files are read-only to it.
</preflight>

Seating: slot ~2, queue position 2. Round 3 of LGIC_CANON, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND2_ANALYSIS.md` @4a55888962); issued by `2.0.0_SA_COO~G`. Decomposition v5.1, section 0e. Rulings carried: R-9 (ii), A-17.
