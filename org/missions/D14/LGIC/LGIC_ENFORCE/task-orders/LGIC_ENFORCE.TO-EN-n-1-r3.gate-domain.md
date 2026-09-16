# TO LGIC_ENFORCE.TO-EN-n-1-r3 -- the naming gate's DOMAIN: declaration trees by subtraction, citations never minted, the binary bypass closed

<to_id>LGIC_ENFORCE.TO-EN-n-1-r3</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-n-1` = round-3 cell 2 (decomposition v3.2, section 0c) | **outcome_ref:** FWD-4 | **depends_on:** none -- level 0

---

## WORKER FACE

### THE CELL

`EN-n-1` -- the domain of `.tools/naming-gate.py` (round-2 analysis s.3 cell 2; rulings R-11 and R-13 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md`; A-6, A-7, A-8 in the analysis). **You edit ONE file: `.tools/naming-gate.py`.**

**WHY.** Two rows showed the gate grading things that are not name mints. W5-S6: a proof instance citing its own order `...fwd7-demo-firm.md` refuses on the token `demo`. W4-S4: a proof of a NAME CHANGE must quote the old name, and refuses. R-13 rules the axis: **a resource is MINTED where the applied plane is DECLARED (Terraform, code, the registry, the schema), never in a RECORD (proof instances, task orders, deliverables, surprise rows, logs, PRDs, project rows).**

What the gate must do, each measured by a criterion below:
1. **Grade DECLARATION trees only, written by SUBTRACTION.** The declaration set is the graded corpus MINUS the record trees `org/**` and `docs/**`, and every run PRINTS that as a subtraction with a DENOMINATOR, naming `org/` and `docs/` as EXCLUDED -- so a tree added later cannot silently land on the wrong side (Rule 24).
2. **Never open a RECORD tree**, regardless of suffix.
3. **Inside declaration trees, a value that RESOLVES to a tracked path at HEAD is a CITATION and is not graded** (R-11). A path-shaped value that does NOT resolve (a typo, an invented file) is still graded and still refuses.
4. **Print COVERAGE** -- the count of paths in its domain it could NOT see (S42).
5. **A `binary` or `-diff` attribute in `.gitattributes` on a path INSIDE a declaration tree must carry a same-line reason comment, or the gate refuses it** (A-6). Measured at the cut: all 3 existing `binary` lines sit in record trees, so none needs a reason today.
6. **Do NOT loosen real names.** The same literal as a `.tf` resource name or a `.py` constructor still refuses.

**THE BASELINE (A-7, a JUDGMENT criterion).** The pre-state pinned at `f1ecf97da7` was 3815 graded / 2917 REFUSE across 90 files. Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/GATE_DOMAIN_BASELINE.r3.md` recording the invocation you used, the pre-state you reproduce at `f1ecf97da7` with it, and the post-state at your tip, each with its denominator. If you cannot reproduce 3815 / 2917 / 90 at the pin, record what you measured and why -- never adjust a number to match.

**Read:** `.tools/naming-gate.py` (`GRADED_EXT`, `parse_diff`, `grade_file`, `run`); `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md` R-11 and R-13; `.gitattributes`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="N1R3-AC1" cell_refs="EN-n-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py n2-denominator</invocation><expect>PASS-N2-DENOMINATOR-PRINTED</expect></criterion>

<criterion id="N1R3-AC2" cell_refs="EN-n-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py n2-coverage</invocation><expect>PASS-N2-COVERAGE-PRINTED</expect></criterion>

<criterion id="N1R3-AC3" cell_refs="EN-n-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py n2-declaration-subtraction</invocation><expect>PASS-N2-SUBTRACTION-PRINTED</expect></criterion>

<criterion id="N1R3-AC4" cell_refs="EN-n-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py n2-record-tree-ungraded</invocation><expect>PASS-N2-RECORD-TREE-UNGRADED</expect></criterion>

<criterion id="N1R3-AC5" cell_refs="EN-n-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py n2-resolving-path-exempt</invocation><expect>PASS-N2-RESOLVING-PATH-EXEMPT</expect></criterion>

<criterion id="N1R3-AC6" cell_refs="EN-n-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py n2-binary-needs-reason</invocation><expect>PASS-N2-BINARY-NEEDS-REASON</expect></criterion>

<criterion id="N1R3-AC7" cell_refs="EN-n-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py regress-n2-tf-name-refuses</invocation><expect>PASS-N2R-TF-NAME-STILL-REFUSES</expect></criterion>

<criterion id="N1R3-AC8" cell_refs="EN-n-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py regress-n2-nonresolving-path-refuses</invocation><expect>PASS-N2R-NONRESOLVING-PATH-REFUSES</expect></criterion>

<criterion id="N1R3-AC9" cell_refs="EN-n-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py regress-n2-binary-with-reason-passes</invocation><expect>PASS-N2R-REASONED-ATTRIBUTE-PASSES</expect></criterion>

<criterion id="N1R3-AC10" cell_refs="EN-n-1" judgment="true"/>

<expected_criteria>N1R3-AC1, N1R3-AC2, N1R3-AC3, N1R3-AC4, N1R3-AC5, N1R3-AC6, N1R3-AC7, N1R3-AC8, N1R3-AC9, N1R3-AC10</expected_criteria>

**AC1-AC6 read RED at the cut** (measured: AC4 and AC5 refuse, AC6 passes `0 graded`, AC1-AC3 find no line) -- they are the work. **AC7-AC9 read PASS at the cut and must STILL pass**: they stop the fix over-reaching (an exemption that swallows a typo, a record-tree rule that stops a real `.tf` name refusing). **N1R3-AC10, for `3.0.0_SA_CVO` at L9 (no verdict from you):** `GATE_DOMAIN_BASELINE.r3.md` reproduces the pinned pre-state at `f1ecf97da7` by a stated invocation and prints the post-state, each with its denominator.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **A value that must be read from the estate is read with the instrument this order names**, and its denominator is printed beside it.
- **Nothing live moves.** The ENFORCE flip (`org/mcp/naming-gate.enforce`) is NOT yours -- it is the issuer's act after this cell drains and the 78-root read reads 0 refusals of existing resources (round-1 RULING ADD). Do not create that file.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
.tools/naming-gate.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.2, round-3 cell 2 (section 0c; the v3.1 and v3.2 amendments).
<owned_cells>EN-n-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `N1R3-AC1`, `N1R3-AC2`, `N1R3-AC3`, `N1R3-AC4`, `N1R3-AC5`, `N1R3-AC6`, `N1R3-AC7`, `N1R3-AC8`, `N1R3-AC9`, `N1R3-AC10`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-n-1-r3.gate-domain.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> N1R3-AC1,N1R3-AC2,N1R3-AC3,N1R3-AC4,N1R3-AC5,N1R3-AC6,N1R3-AC7,N1R3-AC8,N1R3-AC9,N1R3-AC10 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-n-1-r3.gate-domain.md` BEFORE the `complete` flip.
Result file `gate-domain.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`N1R3-AC10` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C only.
comp-iam: DECLARED-NOT-APPLICABLE -- the write set is one tool file and a record; no operation, policy, principal or resource is added.
comp-adversary: DECLARED-NOT-APPLICABLE -- the order introduces no external citation; each criterion's expectation is a checker token measured RED or PASS at HEAD before the cut.
lane: .tools/naming-gate.py is lane ANY; the <paths> block is the grant.
contention: .tools/naming-gate.py is written by this cell alone in round 3.
</preflight>

Seating: slot ~1, queue position 1. Round 3 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND2_20260916.md`); issued by `2.0.0_SA_COO~G`. Decomposition v3.2, section 0c. Rulings carried: R-11, R-13, R-15, A-6, A-7, A-8, S42, S45.
