# TO LGIC_CANON.TO-CN-l-3-r3 -- the conformance ledger's state plane: a row, or the sentence narrowed, stated which

<to_id>LGIC_CANON.TO-CN-l-3-r3</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.5 (ADMITTED; both halves current) | **Decomp cell:** `CN-l-3` (decomposition v5.1, section 0e) | **outcome_ref:** FWD-6 | **depends_on:** none -- level 0; CN-j-11 continues on this slot later

---

## WORKER FACE

### THE CELL

`CN-l-3` -- ruling A-21 on row LGIC_CANON-S4 (`org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND2_ANALYSIS.md` s.2). **You edit ONE file: `infra/logic/06_CONFORMANCE_LEDGER.md`.**

**WHY.** FWD-6's claim is that every part of the estate carries a decision. Section 2 (THE FIRM BUCKETS) names a `state/` plane in prose inside `opal-data-49financial/gold/`'s disposition ("it absorbs `opal-data-bd`'s gold/platinum/state/code") and has NO row for any state plane, while the canon's R21 census (`infra/logic/02_DOCTRINE.md`, R21) names workflow state INSIDE tier planes in bd, inf and cot as VIOLATED-LIVE. A plane named only in prose carries no decision.

Do ONE of the two, and say which in your result file:
- **ROW** -- add row(s) to section 2 whose FIRST (plane) cell names the state prefixes (for example `opal-data-bd/gold/_state/` ...), whose `rules` cell carries `R21`, whose disposition applies the canon (R21: `{source}/{scope}/state/{family}/` in the bucket whose tenancy the state belongs to -- the FIRM bucket; R1's grammar), and whose `decided` cell is filled; or
- **NARROWED** -- narrow the sentence so section 2 names no `state/` plane anywhere.
The canon's R21 census is the source of which prefixes exist; cite it, and do not claim a count the ledger has not measured (write `UNMEASURED`).

**Keep the counts reproduced, never typed.** Section 7's totals are reproduced by `org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/ledger_recount.py` (read-only to you, even though its folder carries your serial). If your row changes a total the script prints, update section 7 from the script's own output.

**Read:** `infra/logic/06_CONFORMANCE_LEDGER.md` sections 0, 2 and 7; `infra/logic/02_DOCTRINE.md` R1 and R21; row LGIC_CANON-S4 in `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="L3R3-AC1" cell_refs="CN-l-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py l3-state-plane</invocation><expect>PASS-L3-STATE-PLANE-DECIDED</expect></criterion>

<criterion id="L3R3-AC2" cell_refs="CN-l-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py l2-recount</invocation><expect>PASS-L2-COUNTS-REPRODUCED</expect></criterion>

<criterion id="L3R3-AC3" cell_refs="CN-l-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py l2-header</invocation><expect>PASS-L2-HEADER-REVERTED</expect></criterion>

<criterion id="L3R3-AC4" cell_refs="CN-l-3" judgment="true"/>

<expected_criteria>L3R3-AC1, L3R3-AC2, L3R3-AC3, L3R3-AC4</expected_criteria>

**AC1 reads RED at the cut** (`BRANCH: NEITHER` -- 0 state rows, 1 prose mention). **AC2 and AC3 read PASS at the cut and must still pass.** **L3R3-AC4, for `3.0.0_SA_CVO` at L9:** the branch taken is stated in the result file, and a ROW's disposition applies R21 and R1 as the canon writes them.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including everything under `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array in the file, id `LGIC_CANON-W<n>-S<k>` (`<n>` your slot; `<k>` ONE ABOVE the highest `LGIC_CANON-W<n>-S` id already present in ANY document under `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/` -- slot numbers were used in earlier rounds, so `S1` is usually taken). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Do not edit `ledger_recount.py`** or any file under another serial's folder.

<paths>
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
infra/logic/06_CONFORMANCE_LEDGER.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v5.1, round-3 cell `CN-l-3` (section 0e).
<owned_cells>CN-l-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `L3R3-AC1`, `L3R3-AC2`, `L3R3-AC3`, `L3R3-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/LGIC_CANON.TO-CN-l-3-r3.state-plane.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> L3R3-AC1,L3R3-AC2,L3R3-AC3,L3R3-AC4 --governing-order org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-l-3-r3.state-plane.md` BEFORE the `complete` flip.
Result file `state-plane.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`L3R3-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C only.
comp-iam: DECLARED-NOT-APPLICABLE -- repository documents only; no principal, policy or resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the ledger and the canon are this estate's own records.
lane: the <paths> block is the grant; the ledger was granted to a round-2 worker the same way.
contention: written by this cell alone in round 3.
</preflight>

Seating: slot ~2, queue position 1. Round 3 of LGIC_CANON, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND2_ANALYSIS.md` @4a55888962); issued by `2.0.0_SA_COO~G`. Decomposition v5.1, section 0e. Rulings carried: A-21.
