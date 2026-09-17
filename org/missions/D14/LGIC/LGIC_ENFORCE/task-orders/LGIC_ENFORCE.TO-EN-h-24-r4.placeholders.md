# TO LGIC_ENFORCE.TO-EN-h-24-r4 -- the eight {system} placeholder rows resolved or carded

<to_id>LGIC_ENFORCE.TO-EN-h-24-r4</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-h-24` = round-4 cell 24 (decomposition v3.3, section 0d) | **outcome_ref:** FWD-5 | **depends_on:** EN-c-23-r4 (same slot, queue position 2 -- both write `resources.json`)

---

## WORKER FACE

### THE CELL

`EN-h-24` -- row `LGIC_ENFORCE-W2-S10`'s class, R-32's cell 24. **You edit ONE file: `infra/logic/registry/resources.json`**, and you write your own deliverables.

**WHY, AND WHY IT IS NOT A RAISE.** Round 3's census report carries **8 rows whose canonical form contains a literal `{system}` placeholder**. These are NOT RAISEs: the grading rule placed each name fine and returned a canonical form, but it could not fill the system slot, so it emitted the placeholder verbatim rather than guessing (that refusal to guess is correct and stays). `grade()` fills `{system}` from a `resources.json` row matched on **both** the name and its node type; W2-S10 measured the asymmetry directly -- `inf-otp-relay-api` (API_GW) leaked `{system}-inf-otp-relay-api` while its registered sibling `inf-otp-relay-lambda-role` (IAM_ROLE) resolved to `advi-inf-otp-relay-lambda-role`, because the sibling had a `(name, type)` row and it did not.

**THE EIGHT, as round 3's report prints them** (all live plane; `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/NAMING_CENSUS_REPORT.r3.md` is the fixed input the criterion re-reads):

| type | name |
|---|---|
| CODEBUILD_PROJECT | `semantic-clustering-lambda-build` |
| CW_ALARM | `ExecIncrParityFailure` |
| CW_ALARM | `Inflection-HistBackfill-FailureSpike` |
| CW_ALARM | `Inflection-JwtResilience-NearExpirySpike` |
| CW_ALARM | `Inflection-SilverChain-DimConversionFailure` |
| CW_ALARM | `OPSEC-auth-login-rate-limit-blocked` |
| CW_ALARM | `OPSEC-auth-throttled` |
| CW_ALARM | `PortfolioExcelGenerator-Errors` |

**WHAT DONE MEANS.** For each of the 8: either the tree now has a `resources.json` row that fills its system (so `grade(name, type)` returns a canonical with no `{`), or the name is CARDED NOT-JUDGED with an owner card. Minted + carded == 8.

1. **MINT from a MEASURED declared source**, exactly as EN-c-23-r4 does: the owning system is read from `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/ec2/EC2_MANIFEST.json`, or the Terraform tree that declares the alarm or project -- a CloudWatch alarm is declared in a `.tf` file whose own directory names its pipeline, which is the citation to record. The row carries `owner_claim` (`measured` or `inferred`) and `owner_basis` in `path:line` form, and **the citation must resolve** (the file exists, the line is inside it).
2. **CARD what no declared source owns.** Append the name to the same two deliverables this slot's first order created: a `## Card <n> -- <name> (live <type>)` heading in `OWNER_CARDS_R4.md`, and a row in `NOT_JUDGED_R4.json` as `{"name": ..., "plane": "live", "card": "<path>#<anchor>"}`. **The anchor must match your heading.**
3. **Do not change how `grade()` fills the slot.** The placeholder behaviour is the rule working as ruled; this cell supplies the missing DATA, never a new derivation. If you believe a row cannot be expressed in `resources.json`'s shape, that is a BLOCKING row with the evidence, not a schema change.
4. **DO NOT RUN `generate`**, and do not touch `scopes.json`, `exemptions.json` or `remediations.json`. `python lib/opal_naming.py validate` must still read `VALIDATE: OK` when you are done.

**Read:** `NAMING_CENSUS_REPORT.r3.md` (its json fence, the 8 rows with `{` in `canonical`); row `LGIC_ENFORCE-W2-S10` in the project's `surprise-channel/investigations/INVESTIGATION_v1.md`; `infra/logic/registry/resources.json` (its `_about` block states the row shape); `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/OWNER_CARDS_S6.r3.md` (round 3's cards -- the shape yours follow).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="H24R4-AC1" cell_refs="EN-h-24"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py h24-placeholders</invocation><expect>PASS-H24-PLACEHOLDERS</expect></criterion>

<criterion id="H24R4-AC2" cell_refs="EN-h-24"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py c23-mint-basis</invocation><expect>PASS-C23-MINT-BASIS</expect></criterion>

<criterion id="H24R4-AC3" cell_refs="EN-h-24"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py c23-validate</invocation><expect>PASS-C23-VALIDATE-OK</expect></criterion>

<criterion id="H24R4-AC4" cell_refs="EN-h-24" judgment="true"/>

<expected_criteria>H24R4-AC1, H24R4-AC2, H24R4-AC3, H24R4-AC4</expected_criteria>

**Measured at the cut, by the issuer, against this tree:** AC1 reads `FAIL-H24-PLACEHOLDERS` -- 8 of 8 rows still leak a placeholder, 0 filled, 0 carded. AC2 is the SAME mint-basis arm your slot's first order carries, re-read here so a row minted for a placeholder is held to the same citation standard (it reads FAIL at the cut, 0 rows added). **AC3 reads PASS at the cut and must still pass.** **H24R4-AC4, for `3.0.0_SA_CVO` at L9 (no verdict from you):** each minted row's `owner_basis` names a source that declares that alarm or project, and each card states what was measured and which instrument is missing.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, everything under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` AND round 3's census report and population list. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). **Append at the END of the existing JSON array, keeping every existing row's bytes and indentation** -- other branches append to this file in the same window. Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Nothing live moves.** No AWS write, no Terraform apply, no deploy, no rename, no `generate`.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
infra/logic/registry/resources.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.3, round-4 cell `EN-h-24` (section 0d).
<owned_cells>EN-h-24</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `H24R4-AC1`, `H24R4-AC2`, `H24R4-AC3`, `H24R4-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-h-24-r4.placeholders.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> H24R4-AC1,H24R4-AC2,H24R4-AC3,H24R4-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-h-24-r4.placeholders.md` BEFORE the `complete` flip.
Result file `placeholders.r4.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`H24R4-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-4 cut. This cell is gated by EN-c-23-r4's completion in the same slot.
comp-iam: DECLARED-NOT-APPLICABLE -- one registry file; no principal, policy or resource changes.
comp-adversary: RUN -- DENOMINATOR 8 placeholder rows, re-graded by (name, type) at the worker's own tree; adversarial shapes covered 2 of 2 (an EMPTY input reading clean: the arm FAILS on a report with 0 placeholder rows rather than passing vacuously; a card with no resolving anchor: refused). BLIND to a placeholder class that round 3's census never reached, since the denominator is round 3's report and not a fresh run -- EN-s-25-r4's own no-placeholder arm is the read that covers that.
lane: TREE_REGISTRY / the worker's own deliverables folder; the <paths> block adds resources.json and the channel.
contention: shares resources.json with EN-c-23-r4, which is why the two are ONE queue in slot ~1 and never parallel. Disjoint from LGIC_LGCTFM LT-x-1 (scopes.json, remediations.json), censused at the cut.
</preflight>

Seating: slot ~1, queue position 2. Round 4 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-3 analysis @`969f89b0e7`; issued by `2.0.0_SA_COO~G`. Decomposition v3.3, section 0d. Rulings carried: R-32, W2-S10, R-29's mint rule.
