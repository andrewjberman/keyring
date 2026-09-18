# TO LGIC_ENFORCE.TO-EN-h-29-r5 -- S61's remedy: ONE evidence string that cites a file it cannot have read

<to_id>LGIC_ENFORCE.TO-EN-h-29-r5</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-h-29` (decomposition v3.4 s.0e) | **outcome_ref:** FWD-5 | **depends_on:** none -- this is the FIRST cell of round 5's queue and everything after it reads the bytes it corrects

---

## WORKER FACE

### THE CELL

`EN-h-29`. **You correct ONE evidence string in one registry row, and nothing else.** This is not a re-cut of
`EN-h-24` and not a new conclusion: the row's answer (`system: advi`) is RIGHT, and the Terraform half of its basis is
sound and stays exactly as it is. What is wrong is a measured claim that cannot have been measured.

**THE DEFECT, measured at the cut and reproducible by you in one command each.** The row
`Inflection-HistBackfill-FailureSpike` in `infra/logic/registry/resources.json` carries an `evidence` string that
quotes a phrase and attributes it to `org/projects/ADVI_HISTBF.json`'s `phase` field, with an asserted measurement
date of 2026-09-17:

> ... is the exact CW metric `org/projects/ADVI_HISTBF.json` (macro_code ADVI, EN-h-24-r4 measured 2026-09-17) names
> at its own phase field: 'CW recovery metrics -> Inflection/HistBackfill/RateLimiter' ...

Measured over **466 files** under `org/projects/` (recursive, every extension):

```
  files carrying 'Inflection/HistBackfill/RateLimiter' ............. 1   -> org/projects/ADVI_JWTRES.json
  org/projects/ADVI_HISTBF.json carries it ........................ NO
  files carrying the phrase EXACTLY AS THE EVIDENCE QUOTES IT ...... 0   (of 466)
```

**The citation is wrong TWICE and the second half is the trap.** Wrong FILE: the phrase lives in the sibling
`ADVI_JWTRES.json`. And the evidence transcribes the arrow as ASCII `->` while the real file writes `U+2192`, so the
quoted phrase as written occurs in **zero** files -- **a reader who greps the quote gets zero and a reader who greps
the distinctive core gets ONE CLEAN HIT IN THE WRONG FILE.** Both readings look like confirmation.

**WHAT YOU DO.** Correct the one `evidence` string so that (i) it no longer attributes the phrase to a file measured
not to carry it, and (ii) the file it now cites DOES carry it, and (iii) it states what that citation does and does
not establish about `ADVI_HISTBF`'s ownership of this alarm. Quote the phrase in whatever form makes it FINDABLE in
the file you cite -- if you reproduce the arrow, reproduce the one that is there.

**DO NOT:** change `name`, `type` or `system` on that row; touch any other row; touch `systems.json`; run `generate`;
or "fix" `ADVI_HISTBF.json` or `ADVI_JWTRES.json` -- the project files are not this cell's business and are outside
your grant.

**Read:** `infra/logic/registry/resources.json` `_about` and the row itself; the surprise row `LGIC_ENFORCE-S61` on
`org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` and its remediation row in
`.../remediations/REMEDIATION_v2.md`; `org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md` s.0e.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="H29R5-AC1" cell_refs="EN-h-29"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py h29-evidence</invocation><expect>PASS-H29-WRONG-OBJECT-CITATION-CORRECTED</expect></criterion>

<criterion id="H29R5-AC2" cell_refs="EN-h-29"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py h29-conclusion</invocation><expect>PASS-H29-CONCLUSION-AND-TERRAFORM-BASIS-UNDISTURBED</expect></criterion>

<criterion id="H29R5-AC3" cell_refs="EN-h-29" judgment="true"/>

<expected_criteria>H29R5-AC1, H29R5-AC2, H29R5-AC3</expected_criteria>

**AT THE CUT, measured by the issuer and stated so you are not surprised:** `H29R5-AC1` reads **FAIL** and names the
live defect. **`H29R5-AC2` reads PASS at the cut and is a GUARD, not a target** -- it exists to refuse a repair that
quietly moves the row's conclusion or drops the sound Terraform half of its basis. A guard that passes before you
start proves nothing about your work; it proves something about what you must not break.

**`H29R5-AC3`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the corrected evidence states honestly what
the `ADVI_JWTRES.json` citation does and does not establish about `ADVI_HISTBF`'s ownership of this alarm -- a
citation that is merely findable is not the same as a citation that supports the conclusion drawn from it.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation runs from your worktree root;
the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row, never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only** -- everything under `deliverables/2.0.0_SA_COO~G/fixed_inputs/`. If you believe an arm is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot; `<k>` ONE ABOVE the highest `LGIC_ENFORCE-W<n>-S` id already present in ANY document under that channel). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Nothing live moves.** No Terraform apply, no AWS write, no deploy. This cell touches one JSON string.

<paths>
infra/logic/registry/resources.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.4, round-5 cell `EN-h-29` (section 0e).
<owned_cells>EN-h-29</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `H29R5-AC1`, `H29R5-AC2`, `H29R5-AC3`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-h-29-r5.evidence-correction.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> H29R5-AC1,H29R5-AC2,H29R5-AC3 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-h-29-r5.evidence-correction.md` BEFORE the `complete` flip.
Result file `evidence-correction.r5.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`H29R5-AC3` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-5 cut: this cell creates no schedule and touches no trigger.
comp-iam: RUN at the round-5 cut: no grant moves; the cell edits one string in a registry file.
comp-adversary: RUN at the round-5 cut: the defect and its correction are both graded in BOTH directions -- the arm refuses a citation that names the file measured not to carry the phrase AND a citation that became vaguer instead of right, because "corrected" must not be satisfiable by saying less.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention, and 0.9.0_WK_LGIC_ENFORCE~1 is the serial whose folder this round's later cells write.
contention: resources.json is written by EN-c-28-r5 later in THIS SAME QUEUE and by no other open order in either LGIC project at the cut (censused from every non-terminal order's <paths>). LGIC_LGCTFM's open LT-x-1 writes scopes.json and remediations.json, not resources.json.
</preflight>

Seating: slot ~1, level 0, FIRST of a three-order queue (`EN-h-29-r5` -> `EN-c-31-r5` -> `EN-c-28-r5`). Round 5 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.4 s.0e, from `1.0.0_SA_CTO`'s round-4 analysis @`b74ffb43ae`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/` (`check_en_r5.py`, `R5_BASE.json` pinning `95fb561677`). Rulings carried: S61's remediation row, R-40.
