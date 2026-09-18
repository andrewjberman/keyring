# TO LGIC_ENFORCE.TO-EN-g-43-r10 -- grade() HONOURS R3: `bd` next to a firm token is the vendor, and the canonical form spells `blackdiamond`

<to_id>LGIC_ENFORCE.TO-EN-g-43-r10</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-g-43` (decomposition v3.9 s.0j) | **outcome_ref:** FWD-5 | **depends_on:** none -- the only order this round

---

## WORKER FACE

### THE CELL

`EN-g-43`. Row `LGIC_ENFORCE-W1-S73` found that `grade()` departs from its own written rule.
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md:204`, rule R3:

> *"bd is refused in every slot (S10). It is the VENDOR blackdiamond when a V4 firm token is next to it ...
> Either way it is an alias, and the canonical form spells blackdiamond, or the firm's form for the slot."*

Measured at the cut: `grade('opal-cot-bd-session-fetch', 'SSM_DOCUMENT')` returns
`('OUT-OF-PATTERN', 'opal-cot-bd-session-fetch-document')`. The hand grader wrote
`opal-cot-blackdiamond-session-fetch-document`. The verdict is right; the canonical form carries a refused
token. **Make `grade()` return `('OUT-OF-PATTERN', 'opal-cot-blackdiamond-session-fetch-document')`**, by
fixing the rule's implementation in `lib/opal_naming.py` (the V-4 alias replacement and `_BD_VENDOR` are the
places to read first), never by special-casing the one name.

### THE BLAST RADIUS IS THE BAR

At the cut, `grade()` reproduces **all 3254** rows of the round-8 census EXACTLY (0 canonical and 0 verdict
differences), and exactly **2** canonicals carry a `bd` token. So after your fix, every census row that
differs from the recorded census is YOUR change -- and the arms require:

- **every moved row NAMED** in your record, no more and no fewer;
- **no COLLATERAL** -- no row moves whose recorded canonical carried no `bd` token;
- **no VERDICT moves** (R3 changes a form, not a verdict);
- **no canonical in the census still carries a `bd` token.**

The census is `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NAMING_CENSUS_REPORT.r8.md`,
its `rows` fence (`current`, `canonical`, `verdict`, `type`, `plane`). Re-grade it in memory; do NOT re-run
or rewrite the census.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/R10_BASE.json`; this is a quotation of it)**

```json
{
  "fixed_row": "LGIC_ENFORCE-W1-S73",
  "census_rows_regraded": 0,
  "moved": [
    {"current": "<name>", "type": "<node_type>", "plane": "<live|repo>",
     "canonical_before": "<recorded>", "canonical_after": "<grade() now>",
     "verdict_before": "<recorded>", "verdict_after": "<grade() now>"}
  ]
}
```

Written to `<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/GRADE_FIX_R10.json`.
`census_rows_regraded` is measured at your write time; `moved` lists every row whose canonical OR verdict now
differs from the recorded census.

### THE TEST SUITE: TWO FAILURES MUST STAY FAILING

`lib/tests/test_opal_naming.py` reads **2 failed, 88 passed** at the cut. Both failures are
`test_grade_agrees_with_every_worked_case[inf-silver-chain|LAMBDA]` and
`test_grade_agrees_with_every_worked_case[Inflection-SilverChain-DimConversionFailure|CW_ALARM]` --
HAND-SIDE STALE worked cases (GRADING_RULE.md leaves `{system}` open; `grade()` fills it with `advi` from
registry rows added after the rule's last edit). The round-9 analysis REFUSES counting a hand-stale case as
agreement, so **they must still fail after your change: no new failure, and neither silenced** by editing the
test, its fixture or GRADING_RULE.md. You MAY add a new test for R3's `bd` case.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G43R10-AC1" cell_refs="EN-g-43"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/check_en_r10.py g43-fixed</invocation><expect>PASS-G43-FIXED</expect></criterion>

<criterion id="G43R10-AC2" cell_refs="EN-g-43"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/check_en_r10.py g43-no-bd</invocation><expect>PASS-G43-NO-BD</expect></criterion>

<criterion id="G43R10-AC3" cell_refs="EN-g-43"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/check_en_r10.py g43-blast-radius</invocation><expect>PASS-G43-BLAST-RADIUS</expect></criterion>

<criterion id="G43R10-AC4" cell_refs="EN-g-43"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/check_en_r10.py g43-tests</invocation><expect>PASS-G43-TESTS</expect></criterion>

<criterion id="G43R10-AC5" cell_refs="EN-g-43" judgment="true"/>

<expected_criteria>G43R10-AC1, G43R10-AC2, G43R10-AC3, G43R10-AC4, G43R10-AC5</expected_criteria>

**AC1-AC3 READ FAIL AT THE CUT.** ⚠ **AC4 (`g43-tests`) IS GUARD-SHAPED AND READS PASS AT THE CUT** -- it
protects the suite's existing behaviour, including the two failures that must stay failing; it measures
nothing you build.

**`G43R10-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the fix implements R3 as written --
the vendor reading when a firm token is next to `bd`, and "the firm's form for the slot" otherwise -- rather
than a substitution that happens to satisfy the one census instance.

**THE CHECKER'S CONTROLS:** run `... check_en_r10.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`.
An arm a CORRECT change cannot satisfy is a BLOCKING surprise row quoting the arm and its output.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **YOU DO NOT EDIT GRADING_RULE.md, NAMING_SCHEMA.json, ANY REGISTRY, OR THE TWO FAILING TESTS.** The rule is LGIC_NAMING's; you conform the code to it.
- ⛔ **YOU DO NOT TOUCH THE CAMEL RE-JOIN (row W1-S74).** It is a ruling pending with 1.0.0_SA_CTO; a change there is out of scope and will show up in the blast radius.
- ⛔ **NOTHING LIVE MOVES.** No AWS call is needed.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; assert the non-ASCII CHARACTER count and backslash-u count unchanged.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time.
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
lib/opal_naming.py
lib/tests/test_opal_naming.py
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.9, round-10 cell `EN-g-43` (section 0j).
<owned_cells>EN-g-43</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `G43R10-AC1` through `G43R10-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-g-43-r10.bd-is-blackdiamond.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G43R10-AC1,G43R10-AC2,G43R10-AC3,G43R10-AC4,G43R10-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-g-43-r10.bd-is-blackdiamond.md` BEFORE the `complete` flip.
Result file `bd-is-blackdiamond.r10.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`G43R10-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the diff of `grade()`'s behaviour in one sentence, every moved census row (before -> after), the suite's failing set before and after, and the commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-10 cut: no schedule is created or read.
comp-iam: RUN at the round-10 cut: no grant moves; the cell reads no AWS surface.
comp-adversary: RUN at the round-10 cut: the adversarial control is g43-blast-radius. The cheapest satisfying move for g43-fixed is a special case on the one name; the blast arm re-grades all 3254 census rows and refuses any unnamed move, any collateral move and any verdict move, and AC5 asks whether R3 is implemented as written. g43-tests refuses silencing the two hand-stale failures, which the round-9 analysis forbids counting as agreement. g43-tests is guard-shaped and disclosed.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~1/ by the tree convention. lib/opal_naming.py and its tests have no other writer this round.
contention: the channel is the only shared file; one order this round.
</preflight>

Seating: slot `~1`, level 0, the only order this round. Round 10 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.9 s.0j, from the round-9 analysis's item (3), W1-S73 only. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/` (`check_en_r10.py`, `R10_BASE.json` pinning `b36edd606e`). Rulings carried: R-47, LGIC_ENFORCE-S85, S79.
