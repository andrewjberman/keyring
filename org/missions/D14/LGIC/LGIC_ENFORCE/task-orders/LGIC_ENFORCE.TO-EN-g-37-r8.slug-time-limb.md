# TO LGIC_ENFORCE.TO-EN-g-37-r8 -- THE SLUG-TIME LIMB: a GRADUATED item with no remediation row is a clock nobody can ever write

<to_id>LGIC_ENFORCE.TO-EN-g-37-r8</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-g-37` (decomposition v3.7 s.0h) | **outcome_ref:** FWD-2 | **depends_on:** none -- FIRST of slot `~2`'s two-order queue

---

## WORKER FACE

### THE CELL

`EN-g-37`. Add ONE limb to `.tools/surprise-row-gate.py`: **refuse a slug when a GRADUATED item in the
staged set carries NO remediation row.**

`S74` found the structural reason this backlog cannot drain itself: **a missed clock cannot be written
outside a round**, because the gate grades a new remediation row as a SLUG ACT. So an item whose clock
was missed at round N's L10 can only acquire one at a LATER round's L10 -- and every round that closes
without noticing a rowless GRADUATED hands it to a round with no reason to look at it. The bar is now
law: **ONE REMEDIATION ROW PER GRADUATED ITEM, ASSERTED AT THE L10 THE ITEM'S OWN ROUND IS CLOSING,
BEFORE THE SLUG.** 14 of the 16 known instances come from the two rounds where that was not run.

### THIS LIMB HOLDS REFUSAL POWER OVER EVERY SLUG IN THE ESTATE

⛔ **SO IT IS NOT BUILT ON THE STRENGTH OF AN ARGUMENT.** `R-66` approved it in principle and
DELIBERATELY DID NOT BUILD IT, in those words: *"a gate built at 10:2xZ on the strength of a good
argument is how a correct rule acquires a wrong implementation."* `R-56`, `R-61` and `R-62` are this
project's own instances of a mechanism reached for without reading what it does.

**TWO CONTROLS, GRADED AS PEERS:**
- **MUTANT** -- a planted rowless GRADUATED item is REFUSED.
- **POSITIVE CONTROL** -- a COMPLIANT slug still PASSES.

⛔ **A MUTANT ALONE BOUNDS UNDER-FIRING AND SAYS NOTHING ABOUT OVER-FIRING.** A limb that refuses EVERY
slug passes any mutant table ever printed and halts the fabric. The positive control is not a courtesy;
it is the half that proves the limb discriminates.

**AND THE GATE'S OWN SELF-TEST MUST STILL READ rc=0.** Call the gate's own runner -- its own run is the
authority and everything else is an estimate.

### WHAT YOU MUST NOT DO

⛔ **DO NOT WIDEN THE LIMB TO STALENESS.** An OPEN remediation row that exists but has not moved is
`EN-k-38`'s, the SECOND order on this same slot, and it is a DIFFERENT QUESTION: **no rowlessness limb
will ever see it, because the row exists.** If you make this limb also grade staleness, 38 has nothing
to build and the round buys one limb where it needed two. Your limb grades ROWLESSNESS ONLY.

**Read:** `R8_BASE.json`'s `gate_limbs_absent_at_the_cut` (0 hits over 2437 lines -- the negative
control for your own arm) and `clock_failure_classes_that_must_not_share_a_remedy`; the gate's
`_resolve_latest` at `:375` and `_latest_dispositions` at `:420`; rows `LGIC_ENFORCE-S74` and `S73`.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/SLUG_TIME_LIMB_R8.json`

```
  {"limb": {"positive_control": {"what": "...", "outcome": "PASS"},
            "mutant":           {"what": "...", "outcome": "REFUSED"}},
   "gate_selftest": {"invocation": "...", "rc": 0}}
```

The limb's function must be named `_graduated_without_row` -- the arm reads that token in the gate
source, and R8_BASE pins its absence at the cut so the arm cannot pass on something already there.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G37R8-AC1" cell_refs="EN-g-37"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py g37-limb-present</invocation><expect>PASS-G37-LIMB-PRESENT</expect></criterion>

<criterion id="G37R8-AC2" cell_refs="EN-g-37"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py g37-controls</invocation><expect>PASS-G37-CONTROLS</expect></criterion>

<criterion id="G37R8-AC3" cell_refs="EN-g-37"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py g37-gate-unmoved</invocation><expect>PASS-G37-GATE-UNMOVED</expect></criterion>

<criterion id="G37R8-AC4" cell_refs="EN-g-37" judgment="true"/>

<expected_criteria>G37R8-AC1, G37R8-AC2, G37R8-AC3, G37R8-AC4</expected_criteria>

**ALL THREE MECHANICAL CRITERIA READ FAIL AT THE CUT**, MEASURED: the limb token has 0 occurrences in
the gate across 2437 lines, and your record does not exist. No guard-shaped criterion in this cell.

**`G37R8-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the positive control is a
GENUINELY compliant slug rather than one shaped to pass, and whether the mutant plants a defect the
limb could not have caught by accident. The arms can only check that both outcomes were recorded and
that they describe different inputs.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives **31 arms, 13 POSITIVE-SATISFIABILITY**. Run it
first. An arm a correct record cannot satisfy is a BLOCKING surprise row quoting the arm and its
output -- never a workaround, never an edit to a fixed input.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **ONE LIMB. ROWLESSNESS ONLY.** Staleness is `EN-k-38`'s and follows you on this same slot.
- ⛔ **NO EXISTING LIMB CHANGES BEHAVIOUR.** `G37R8-AC3` is the arm that says so, and it reads the gate's OWN self-test rc rather than your description of it.
- ⛔ **NOTHING LIVE MOVES.** No AWS, no deploy.
- **Surprises** go to the project channel by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump the array; assert the non-ASCII CHARACTER count and the backslash-u count unchanged. `len(b)-len(b.decode())` is a BYTE DELTA, not a character count.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **Three other orders are open this round.**
- **Commit before you grade.**

<paths>
.tools/surprise-row-gate.py
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.7, round-8 cell `EN-g-37` (section 0h).
<owned_cells>EN-g-37</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `G37R8-AC1` through `G37R8-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-g-37-r8.slug-time-limb.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G37R8-AC1,G37R8-AC2,G37R8-AC3,G37R8-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-g-37-r8.slug-time-limb.md` BEFORE the `complete` flip.
Result file `slug-time-limb.r8.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`G37R8-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the mutant's verdict, the positive control's verdict, and the gate self-test rc.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-8 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-8 cut: no grant moves and no IAM surface is touched. The cell edits one repo file.
comp-adversary: RUN at the round-8 cut: the adversarial control is the POSITIVE CONTROL being graded as a PEER of the mutant. The cheapest way to satisfy a mutant-only arm on a refusal limb is to refuse everything, which passes the mutant table and halts every slug in the estate. This is the one cell this round where the ADVERSARY IS THE CELL'S OWN GREEN.
lane: the <paths> block is the grant; .tools/ is lane ANY. deliverables/0.9.0_WK_LGIC_ENFORCE~2/ is granted by the tree convention.
contention: .tools/surprise-row-gate.py is written by THIS cell and by EN-k-38 -- the SECOND order on this SAME SLOT, sequenced, never concurrent. That serialisation is the reason this round is three slots and not four (decomposition v3.7 s.0h.4). The channel is shared with all three slots and no slot isolates there per 14b.
</preflight>

Seating: slot `~2`, level 0, FIRST of a two-order queue (`EN-g-37-r8` -> `EN-k-38-r8`). Round 8 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.7 s.0h, from the REGISTER's ROUND 8 MATERIAL block `(d)`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/`. Rulings carried: R-66, R-56, R-61.
