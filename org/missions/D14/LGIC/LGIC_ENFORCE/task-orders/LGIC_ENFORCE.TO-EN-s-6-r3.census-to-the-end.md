# TO LGIC_ENFORCE.TO-EN-s-6-r3 -- the naming census run to the END on both planes, and the comparison over the real hand populations

<to_id>LGIC_ENFORCE.TO-EN-s-6-r3</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-s-6` = round-3 cell 6 (decomposition v3.2, section 0c) | **outcome_ref:** FWD-5 | **depends_on:** EN-r-5-r3 (spawns after its drain)

---

## WORKER FACE

### THE CELL

`EN-s-6` -- the census, run to the end (A-4). Round 2's run STOPPED on its first RAISE (`sentiment-query-api`): its report's fenced json reads `judged_live` 3 of `live_nameable` 1821 and `judged_repo` 0 of `repo` 1878, and one row's canonical carries a `{system}` placeholder.

1. **Run the census on BOTH planes to the end:** `python lib/opal_naming.py census --live --repo --report org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/NAMING_CENSUS_REPORT.r3.md`. The live plane's instrument is `comp-find --corpus aws`, and its `built:` vintage goes in the report. **A RAISE FAILS the criterion; it is never filed under a verdict.** If the run stops, record where and why, and file a row -- the RAISE is a defect in the rule, the schema or the registry.
2. **No placeholder reaches a report row** (W2-S10).
3. **Write the comparison** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/NAMING_CENSUS_COMPARISON.r3.md` over the REAL hand populations -- LGIC_NAMING's N2 worked cases (45) and N6 grader rows (88) -- with the same fenced-json shape as round 2's comparison (`census`, `against.N2`, `against.N6`, each with `hand_population`, `compared`, `uncompared_hand_rows`), the census block copied from YOUR report, and the totals beside the hand ranking.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="S6R3-AC1" cell_refs="EN-s-6"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py s6-live-complete org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/NAMING_CENSUS_REPORT.r3.md</invocation><expect>PASS-S6-LIVE-COMPLETE</expect></criterion>

<criterion id="S6R3-AC2" cell_refs="EN-s-6"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py s6-repo-complete org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/NAMING_CENSUS_REPORT.r3.md</invocation><expect>PASS-S6-REPO-COMPLETE</expect></criterion>

<criterion id="S6R3-AC3" cell_refs="EN-s-6"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py s6-no-placeholder org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/NAMING_CENSUS_REPORT.r3.md</invocation><expect>PASS-S6-NO-PLACEHOLDER</expect></criterion>

<criterion id="S6R3-AC4" cell_refs="EN-s-6"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py s6-comparison-arithmetic org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/NAMING_CENSUS_COMPARISON.r3.md</invocation><expect>PASS-S6-COMPARISON-ARITHMETIC</expect></criterion>

<criterion id="S6R3-AC5" cell_refs="EN-s-6" judgment="true"/>

<expected_criteria>S6R3-AC1, S6R3-AC2, S6R3-AC3, S6R3-AC4, S6R3-AC5</expected_criteria>

**All four arms read RED at the cut**, and against round 2's REAL files for substantive reasons (stopped on a RAISE; a `{system}` placeholder). AC4 requires the census embedded in your comparison to be COMPLETE on both planes -- closing arithmetic alone passed round 2's stopped census. **S6R3-AC5, for `3.0.0_SA_CVO` at L9:** every hand row the comparison leaves uncompared carries a stated reason.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **A value that must be read from the estate is read with the instrument this order names**, and its denominator is printed beside it.
- **Nothing live moves.** The live plane is READ through `comp-find --corpus aws` only.
- **Do not edit the registry.** A RAISE naming a missing row is a row for the owning cell, not an edit here.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.2, round-3 cell 6 (section 0c; the v3.1 and v3.2 amendments).
<owned_cells>EN-s-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `S6R3-AC1`, `S6R3-AC2`, `S6R3-AC3`, `S6R3-AC4`, `S6R3-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/LGIC_ENFORCE.TO-EN-s-6-r3.census-to-the-end.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> S6R3-AC1,S6R3-AC2,S6R3-AC3,S6R3-AC4,S6R3-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-s-6-r3.census-to-the-end.md` BEFORE the `complete` flip.
Result file `census-to-the-end.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`S6R3-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C and by EN-r-5-r3's drain.
comp-iam: DECLARED-NOT-APPLICABLE -- a read-only census; no principal, policy or resource changes.
comp-adversary: RUN -- a RAISE is the adversarial case; S6R3-AC1 and AC2 fail on any stop, and AC4 fails on an incomplete census even where the arithmetic closes.
lane: the worker's own deliverables folder; the <paths> block adds only the channel.
contention: the worker's own folder; no other round-3 cell writes it.
</preflight>

Seating: slot ~4, queue position 1. Round 3 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND2_20260916.md`); issued by `2.0.0_SA_COO~G`. Decomposition v3.2, section 0c. Rulings carried: A-4, RULING ROWS, W2-S10.
