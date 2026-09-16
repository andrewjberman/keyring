# TO LGIC_ENFORCE.TO-EN-i-3-r3 -- proof-of-spec-check resolves a cited row from the INSTANCE's checkout (LGIC_NAMING-S21)

<to_id>LGIC_ENFORCE.TO-EN-i-3-r3</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-i-3` = round-3 cell 3a (decomposition v3.2, section 0c) | **outcome_ref:** FWD-5 | **depends_on:** none -- level 0; EN-t-8-r3 waits on this drain

---

## WORKER FACE

### THE CELL

`EN-i-3` -- row LGIC_NAMING-S21. **You edit ONE file: `.tools/proof-of-spec-check.py`.**

**THE DEFECT, reproduced RED at HEAD by the issuer.** The surprises limb resolves a cited row through `_channel_row_ids(code)` (`:1132-1157`), which globs `WORKSPACE`; `WORKSPACE = Path(__file__).resolve().parent.parent` (`:498`) is the checkout holding the SCRIPT. So the main checkout's script, pointed at an instance on a side branch or in a linked worktree whose channel carries the row, reads "resolves to NO row" although the row is committed in the graded tree. The CVO's L9 and the L10 gate run this script.

**THE FIX:** the channel is resolved from the checkout that holds the INSTANCE being graded (for example the repository root found from the instance's own directory), while every other limb's behaviour is unchanged. Add a self-test arm for it to the script's own `--self-test`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="I3R3-AC1" cell_refs="EN-i-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py i3-channel-root</invocation><expect>PASS-I3-ROOTED-AT-INSTANCE-CHECKOUT</expect></criterion>

<criterion id="I3R3-AC2" cell_refs="EN-i-3"><invocation>cd <WS> && timeout 300 python .tools/proof-of-spec-check.py --self-test</invocation><expect>RESULT: ([0-9]+) of \1 arm\(s\) behaved</expect></criterion>

<expected_criteria>I3R3-AC1, I3R3-AC2</expected_criteria>

**AC1 reads RED at the cut** (`FAIL-I3-ROOTED-AT-SCRIPT-CHECKOUT`, frame `0 resolve to a channel row`): it plants a row in a throwaway repo that the script's own checkout does not carry and runs YOUR script against an instance citing it. **AC2 reads `RESULT: 44 of 44 arm(s) behaved` at the cut** and must still read N of N, with your new arm among them.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **A value that must be read from the estate is read with the instrument this order names**, and its denominator is printed beside it.
- **Change only the channel-resolution root.** Every other limb (coverage, invocation alignment, count-bar, drives, binding) must behave exactly as before; AC2 is the regression read.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
.tools/proof-of-spec-check.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.2, round-3 cell 3a (section 0c; the v3.1 and v3.2 amendments).
<owned_cells>EN-i-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `I3R3-AC1`, `I3R3-AC2`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-i-3-r3.channel-root.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> I3R3-AC1,I3R3-AC2 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-i-3-r3.channel-root.md` BEFORE the `complete` flip.
Result file `channel-root.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C only.
comp-iam: DECLARED-NOT-APPLICABLE -- one tool file; no principal, policy or resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; AC1 is a planted-row fixture and AC2 the script's own self-test count.
lane: .tools/proof-of-spec-check.py is lane ANY; the <paths> block is the grant.
contention: written by this cell alone in round 3.
</preflight>

Seating: slot ~3, queue position 1. Round 3 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND2_20260916.md`); issued by `2.0.0_SA_COO~G`. Decomposition v3.2, section 0c. Rulings carried: LGIC_NAMING-S21, R-5 addendum.
