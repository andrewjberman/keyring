# TO LGIC_NAMING.TO-LN-f-1-r5 -- the gaps re-run at HEAD, with the new count printed BESIDE 49

<to_id>LGIC_NAMING.TO-LN-f-1-r5</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.10 @592ff7a5de (ADMITTED; both halves current) | **Decomp cell:** `LN-f-1` (round 5, decomposition v7.1 section 0f) | **outcome_ref:** FWD-5 | **depends_on:** none -- one of three independent chains | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`LN-f-1` -- the placeholder gaps re-run at HEAD (round-4 analysis s.3 item 2; rows LGIC_NAMING-W4-S3 and `3.0.0_SA_CVO`'s C-S25). **You write ONE record: `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r5/f1-gaps.r5.md`.**

**WHAT MOVED, and it is the whole reason this cell exists.** Round 4's headline was **49** unplaceable names, each RAISEd with a `missing_row`. That number was measured at base `5e908a4929`, where `infra/logic/registry/resources.json` **does not exist**. That file now exists at HEAD -- added by LGIC_ENFORCE EN-r-4 -- and rows **30** resource-to-system entries. So a sibling project's drain moved the world under a correctly-measured number.

Your record carries, in ONE json fence:

```json
{ "population": <int>, "placeholder_count": <int>, "r4_headline": 49,
  "r4_base": "5e908a4929", "registry_rows": <int>,
  "raises": [ {"name": "...", "missing_row": "...", "step": "..."} ] }
```

1. **`population`** -- how many names you graded, and from where. Use the fixed input `fixed_inputs/LIVE_NAMES.json`, `by_type.IAM_ROLE`.
2. **`placeholder_count`** -- how many of those still grade to a canonical form carrying a `{token}` at YOUR tree.
3. **Print the new count BESIDE 49, never instead of it, and never subtracted from it.** The two numbers do not share a stated denominator: 49 came from round 4's own subset at a base without the registry file. **An inherited `N of M` is a SUBSET measurement until you ask what population it enumerated.** Say in prose which population each number counts, and whether they are comparable. If you conclude they are not, say so -- that is a finding, not a failure.
4. **Every remaining raise names a REAL `missing_row`, 0 guessed.** A raise whose `missing_row` you cannot point at in `infra/logic/registry/` is not a raise you may record.
5. **NEGATIVE CONTROL, and it is a criterion:** plant a name with no registry row and show it STILL RAISES. Record both readings.

**Read:** `infra/logic/registry/resources.json` and `systems.json`; `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/LIVE_NAMES.json`; `lib/opal_naming.py` `grade()`; round 2's record `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md`; the round-4 analysis s.3 item 2 (@5a12d0b97c) and the slug's C-S25 (`surprise-channel/adjudications/ADJUDICATION_v5.md` @3fe3d30b15).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="F1R5-AC1" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_ln_r5.py f1-gaps</invocation><expect>VERDICT: PASS-GAPS-COUNTED-WITH-DENOMINATORS</expect></criterion>

<criterion id="F1R5-AC2" cell_refs="LN-f-1" judgment="true"/>

<expected_criteria>F1R5-AC1, F1R5-AC2</expected_criteria>

**F1R5-AC1 checks your RECORD against the tree** -- `population`, `placeholder_count` and `r4_headline` must EQUAL what the checker measures independently. It is not enough to write numbers; they must be the tree's.

**F1R5-AC2, for `3.0.0_SA_CVO` at L9 (no verdict from you):** every remaining raise names a real `missing_row` with 0 guessed, AND the planted-rowless-name negative control still RAISES, both readings recorded. Also for the CVO: your prose on whether 49 and your count are comparable populations.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file. Nothing else. **The registry is NOT yours** -- if a name needs a row that does not exist, that is a RAISE to record and a surprise row, never a row you add.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Nothing live moves.** No AWS write, no Terraform, no rename of a live name.
- **Fixed inputs are read-only**, including `fixed_inputs/r5/check_ln_r5.py` and `fixed_inputs/LIVE_NAMES.json`. If you believe the checker is wrong, file a BLOCKING row; do not work around it.
- **Surprises** go to `surprise-channel/investigations/INVESTIGATION_v1.md`, ONE row each, id `LGIC_NAMING-W3-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names and cite them, never the CLAUDE.md or memory text every worker starts with.
- **Numbers** here are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r5/f1-gaps.r5.md
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v7.1, cell `LN-f-1`, round 5 (section 0f).
<owned_cells>LN-f-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F1R5-AC1`, `F1R5-AC2`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~3/LGIC_NAMING.TO-LN-f-1-r5.gaps-at-head.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F1R5-AC1,F1R5-AC2` BEFORE the `complete` flip.
Result file `gaps-at-head.r5.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `F1R5-AC2` is a JUDGMENT criterion -- `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid. **Flip `complete` only when F1R5-AC1 PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the recut. Gates G-A DISCHARGED, G-B met round 1, G-C at spawn. This cell is gated by G-C only.
comp-iam: DECLARED-NOT-APPLICABLE -- the write set is one markdown record and the channel; no operation, policy, principal or resource is added.
comp-adversary: DECLARED-NOT-APPLICABLE -- this cell introduces no external citation; the 49 and the 30 in this order are CONTEXT and the order says so; the acceptance value is what the checker measures at the worker's own tree, and F1R5-AC1 compares the worker's record TO that measurement rather than to any number typed here.
lane: the <paths> block IS the grant. infra/logic/registry/ is excluded deliberately -- a missing row is a finding to record, not a row for this cell to write.
contention: LN-f-1 writes exercises/r5/f1-gaps.r5.md alone. No other round-5 cell names that path.
</preflight>

Seating: slot ~3, queue position 1. Round 5 of LGIC_NAMING, the CLOSING round, recut of `1.0.0_SA_CTO`'s round-4 analysis (@5a12d0b97c, msg 97396); issued by `2.0.0_SA_COO~G`. Decomposition v7.1, section 0f.
