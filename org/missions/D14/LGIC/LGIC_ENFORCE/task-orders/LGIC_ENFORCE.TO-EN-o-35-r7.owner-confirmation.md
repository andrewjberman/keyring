# TO LGIC_ENFORCE.TO-EN-o-35-r7 -- THE CLAIM THAT UNDER-STATES: 41 rows read `inferred` because leg B inherits from a sibling

<to_id>LGIC_ENFORCE.TO-EN-o-35-r7</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-o-35` (decomposition v3.6 s.0g) | **outcome_ref:** FWD-5 | **depends_on:** `EN-t-34-r7` -- SECOND of this slot's queue

---

## WORKER FACE

### THE CELL

`EN-o-35`. Round 6 resolved 41 placeholder rows and **every one of them carries `owner_claim: inferred`**
-- 41 of 41, measured. The cell that produced them DISCLOSED that unprompted, and `3.0.0_SA_CVO` weighed
the disclosure rather than discounting it, so the word stays in the grade. Your job is to take each of
the 41 as far as the evidence actually reaches, and no further.

### WHY THEY READ `inferred`, WHICH IS THE WHOLE PROBLEM IN ONE SENTENCE

Each row carries a TWO-LEG `owner_basis`:

```
  LEG A (declared)  a declared source -- a manifest row, a tf_type_map name attribute
  LEG B (inherited) the system carried by the resource's OWN IAM ROLE, read from resources.json
```

**LEG B INHERITS FROM A SIBLING WHOSE OWN CLAIM IS INFERRED.** A sibling's reading is not a confirmation;
it is the same reading, one resource over. So the whole row reads `inferred`, correctly, and it will keep
reading `inferred` forever unless something OUTSIDE that chain speaks.

### WHAT A CONFIRMATION HAS TO REACH

**AN OWNING DIRECTIVE.** The registered project or directive that CLAIMS the resource -- the thing that
can say "this is mine" rather than "this looks like mine". The trail is usually already in leg B: a
sample row's Terraform header reads *"Inf Pipeline -- inf-bronze-runner EC2 (ADVI_INFSHIP.B1)"*, and
`ADVI_INFSHIP` is a registered project with a directive row. That is the shape; it is NOT a promise that
all 41 have one.

For each of the 41, exactly one of:
- **CONFIRMED** -- `owning_directive` names it, `directive_citation` cites where you read it
  (`org/missions/DIRECTIVES.yaml:<line>`, a `project.json` path, a tree register row), and `owner_claim`
  is no longer `inferred`.
- **CARDED** -- no directive claims it. `owner_claim` STAYS `inferred` and a `reason` says what you
  looked at and did not find.

⛔ **CARDING IS NOT FAILING.** A row with no owning directive is a REAL FINDING about the estate and is
worth more than a confident guess. `confirmed + carded == 41` is the arm; the split is whatever the
evidence gives.

### THE ARM THAT WILL CATCH THE TEMPTING SHORTCUT

⛔ **A CLAIM CANNOT MOVE WITHOUT ITS BASIS MOVING.** `o35-no-silent-upgrade` requires every CONFIRMED row
to carry `owner_basis_round_6` beside its new `owner_basis`, and REFUSES them if they are
BYTE-IDENTICAL. Upgrading `inferred` to something stronger while the evidence string stays the same is a
RELABELLING, not a confirmation -- and it is exactly the shape that makes a value stop carrying its
claim. If the basis did not change, neither did what you know.

**Read:** `R7_BASE.json`'s `the_41_inferred_owner_claims`; round 6's `PLACEHOLDER_CAMPAIGN_R6.json`
`resolved` list whole, including every `owner_basis` string; `R-42` on the three addressee owner fields;
`R-19`.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/OWNER_CONFIRMATION_R7.json`

Any script you cite as an instrument goes in that same folder and is **COMMITTED** (row
`LGIC_ENFORCE-S69`).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="O35R7-AC1" cell_refs="EN-o-35"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_en_r7.py o35-population</invocation><expect>PASS-O35-EVERY-ROW-ADDRESSED</expect></criterion>

<criterion id="O35R7-AC2" cell_refs="EN-o-35"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_en_r7.py o35-directive</invocation><expect>PASS-O35-CONFIRMED-CITES-A-DIRECTIVE</expect></criterion>

<criterion id="O35R7-AC3" cell_refs="EN-o-35"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_en_r7.py o35-claim-moves</invocation><expect>PASS-O35-CLAIM-MATCHES-ITS-LIST</expect></criterion>

<criterion id="O35R7-AC4" cell_refs="EN-o-35"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_en_r7.py o35-no-silent-upgrade</invocation><expect>PASS-O35-NO-SILENT-UPGRADE</expect></criterion>

<criterion id="O35R7-AC5" cell_refs="EN-o-35" judgment="true"/>

<expected_criteria>O35R7-AC1, O35R7-AC2, O35R7-AC3, O35R7-AC4, O35R7-AC5</expected_criteria>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, each because your record does not exist yet --
MEASURED by the issuer, not assumed. There is no guard-shaped criterion in this cell.

**`O35R7-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether each CONFIRMED row's directive
genuinely CLAIMS that resource rather than merely mentioning it, and whether each CARDED row's reason
reflects a real search rather than a shrug. The arms can only check that the fields differ and that the
arithmetic closes.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives **21 arms, 8 POSITIVE-SATISFIABILITY** against
simulated correct records. Run it first. An arm a correct record cannot satisfy is a BLOCKING surprise
row quoting the arm and its output -- never a workaround, never an edit to a fixed input.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **YOU DO NOT EDIT `DIRECTIVES.yaml`, ANY `project.json`, OR `infra/logic/registry/`.** You READ them and you CITE them. A register row is `1.0.0_SA_CTO`'s L3 carrier and a directive row is not a worker's to touch -- if one is WRONG, that is a surprise ROW with its measurement.
- ⛔ **NO GRADE MOVES AND NO PLACEHOLDER IS RESOLVED.** Round 6's 41 resolutions stand exactly as graded; you are annotating their PROVENANCE, not re-deciding them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md`, appended by **TEXTUAL SPLICE** to the fence that PARSES AS A LIST. ⛔ **NEVER RE-DUMP THE ARRAY** -- assert the non-ASCII CHARACTER count and the backslash-u count are both unchanged afterwards. **A JSON array append costs exactly ONE deletion**, the previous element's comma; verify the deleted line is only ` }` becoming ` },`.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time -- `EN-t-34-r7` appended to this same file earlier in this queue.
- **Commit before you grade.**
- **Nothing live moves.** Every AWS read is read-only through the `.tools/aws` shim. No apply, no write, no deploy.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.6, round-7 cell `EN-o-35` (section 0g).
<owned_cells>EN-o-35</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `O35R7-AC1` through `O35R7-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-o-35-r7.owner-confirmation.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> O35R7-AC1,O35R7-AC2,O35R7-AC3,O35R7-AC4,O35R7-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-o-35-r7.owner-confirmation.md` BEFORE the `complete` flip.
Result file `owner-confirmation.r7.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`O35R7-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT `confirmed + carded == 41`, the split, and for the confirmed rows how many changed their `owner_basis` (which must be all of them).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-7 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-7 cut: no grant moves. The cell READS DIRECTIVES.yaml, project.json rows and infra/logic/registry/ and writes NONE of them -- a read-only widening of what it consults, stated here because the <paths> block cannot express "may read, must not write".
comp-adversary: RUN at the round-7 cut: the adversarial control is o35-no-silent-upgrade, which refuses a CONFIRMED row whose owner_basis is byte-identical to round 6's. Without it the cheapest way to satisfy every other arm is to relabel 41 claims and change no evidence, and each remaining arm would pass. It is the arm that makes the cell about EVIDENCE rather than about a field's value.
lane: the <paths> block is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~1/ is granted by the tree convention. DIRECTIVES.yaml and the register rows are read-only by a BOUND: a register row is 1.0.0_SA_CTO's L3 carrier under Rule 27 and a directive row is nobody's to edit from a cell.
contention: the channel is written by EN-t-34-r7 EARLIER IN THIS SAME QUEUE and by no other open order in any LGIC project at the cut. ONE QUEUE -- see EN-t-34-r7's contention note for the refuted splice hypothesis that settles it, measured at LGIC_LGCTFM round 2's second drain.
</preflight>

Seating: slot `~1`, level 1, SECOND of a two-order queue (`EN-t-34-r7` -> `EN-o-35-r7`). Round 7 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.6 s.0g, from the REGISTER's round-7 material at `last_updated 2026-09-18T08:40:00Z`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/` (`check_en_r7.py`, 8 subcommands and a 21-arm self-test with 8 positive-satisfiability arms; `R7_BASE.json` pinning `2c3d7b0cb2`). Rulings carried: R-42, R-19, R-40.
