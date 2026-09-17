# TO LGIC_ENFORCE.TO-EN-c-23-r4 -- the registry campaign: every name on round 3's measured RAISE list minted or carded

<to_id>LGIC_ENFORCE.TO-EN-c-23-r4</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-c-23` = round-4 cell 23 (decomposition v3.3, section 0d) | **outcome_ref:** FWD-5 | **depends_on:** nothing (level 0)

---

## WORKER FACE

### THE CELL

`EN-c-23` -- RULINGS R-29, R-32 and R-33 (`1.0.0_SA_CTO`'s round-3 analysis `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/1.0.0_SA_CTO/LGIC_ENFORCE_ROUND3_ANALYSIS.md` s.3). **You edit two files: `infra/logic/registry/systems.json` and `infra/logic/registry/resources.json`**, and you write your own deliverables.

**WHY.** FWD-5 is the one outcome LGIC_ENFORCE still misses: "one run lists every out-of-pattern name across the estate". Round 3's census stopped because names RAISE -- the grading rule cannot place them -- and no cell owned the registry rows behind them. Round 3 then MEASURED the whole population instead of grinding: **351 distinct `(plane, type, name)` triples**, listed in `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/RAISE_POPULATION_S6.r3.md` as a markdown table (plane | type | name | message). That table is your population and your denominator. It is a FIXED INPUT: never edit it.

**WHAT DONE MEANS.** Every one of the 351 triples is either **MINTED** (the registry now resolves it, so `grade(name, type)` no longer raises) or **CARDED** (recorded NOT-JUDGED with an owner card that says why nobody can measure its owner). Both halves count toward done: the closure bar for this round is `minted + carded == the population`, never "zero carded".

1. **MINT only from a MEASURED declared source.** A row's owner is read, never guessed, from one of:
   - `infra/aws/lambda/ci/lambda-source-map.json` -- its `source_dir` / `tf_file` / `tf_resource` for that resource;
   - `infra/aws/ec2/EC2_MANIFEST.json` -- its `source_path`;
   - the Terraform tree that declares the resource (the `.tf` file naming it).
   The row carries `"owner_claim": "inferred"` (or `"measured"` where the source names the owner outright) and `"owner_basis"` set to the citation in `path:line` form. **The citation must RESOLVE: the file exists and the line is inside it.** A row whose owner no declared source names is NOT minted.
   - `systems.json` holds token rows (a token like `news` that names a system); `resources.json` holds `(name, type)` rows. Use whichever the RAISE's own message points at: a message about an unresolved TOKEN (`R1.c`, `R1.f`, `R2`, `B2`, `K1`, `K3`) is a `systems.json`/scope-vocabulary question; a message about a specific resource needing its system is a `resources.json` row.
2. **CARD what you cannot measure.** Write one card per name to `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/OWNER_CARDS_R4.md` -- a `## Card <n> -- <name> (<plane> <type>)` heading, the question the card asks, why the name RAISEs, and what you measured (the sources you read and what they did or did not say). Record the name in `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/NOT_JUDGED_R4.json`, a JSON list of `{"name": ..., "plane": ..., "card": "<path>#<anchor>"}`. **The `card` anchor must match one of your headings** -- a bare path with no anchor is refused by the criterion, because "it is in that file somewhere" is not a card.
   - Cards may be grouped by token where the question is genuinely one question (all 114 `news` names asking "who owns `news`?" is ONE question), but **every name still gets its own row in the NOT_JUDGED json** pointing at that card's anchor.
3. **THE FENCE GUARD, VERBATIM (R-29).** "a row whose mint would change a GENERATED POLICY on an APPLIED resource is NOT minted -- card it BLOCKING for never-widen sign-off (`1.0.0_SA_CTO` + `2.0.0_SA_COO`)". The live case is `infra/logic/registry/exemptions.json`, whose rows are generated into the APPLIED `DenyForeignFirmPrincipals` policy on `opal-data-49financial` through `modules/opal_name/generated_locals.tf`. **`exemptions.json` is not in your `<paths>` and must not move.** A name that would need an exemption is carded BLOCKING, naming the principal and its evidence; you apply nothing.
4. **THE BOUND (R-33).** If the measured population grows past **376** (351 + 25) while you work -- for instance because a mint reveals further names -- **STOP minting, file ONE surprise row with the delta and the new count, and leave the rest for round 5.** The criteria are graded against the pinned 351-triple list either way. A campaign without a bound is the grind R-29 refused.
5. **DO NOT RUN `generate`, and do not touch `scopes.json` or `remediations.json`.** `python lib/opal_naming.py generate` re-stamps the two `opal_name` test fixtures, and LGIC_LGCTFM round 1's open `LT-x-1` writes `scopes.json` in the same window; the re-render is the issuer's act after both rounds drain. `python lib/opal_naming.py validate` must still read `VALIDATE: OK`.

**Read:** `RAISE_POPULATION_S6.r3.md` (whole, it is your population); `infra/logic/registry/systems.json` and `resources.json` (their `_about` blocks state each file's row shape); `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md` R-29 and R-6 (R-6 is the precedent this mint rule comes from); `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/OWNER_CARDS_S6.r3.md` (round 3's two cards -- the shape yours follow).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="C23R4-AC1" cell_refs="EN-c-23"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py c23-campaign-covered</invocation><expect>PASS-C23-CAMPAIGN-COVERED</expect></criterion>

<criterion id="C23R4-AC2" cell_refs="EN-c-23"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py c23-mint-basis</invocation><expect>PASS-C23-MINT-BASIS</expect></criterion>

<criterion id="C23R4-AC3" cell_refs="EN-c-23"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py c23-fence-untouched</invocation><expect>PASS-C23-FENCE-UNTOUCHED</expect></criterion>

<criterion id="C23R4-AC4" cell_refs="EN-c-23"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py c23-validate</invocation><expect>PASS-C23-VALIDATE-OK</expect></criterion>

<criterion id="C23R4-AC5" cell_refs="EN-c-23" judgment="true"/>

<expected_criteria>C23R4-AC1, C23R4-AC2, C23R4-AC3, C23R4-AC4, C23R4-AC5</expected_criteria>

**Measured at the cut, by the issuer, against this tree:** AC1 reads `FAIL-C23-CAMPAIGN-COVERED` -- 351 of 351 triples OPEN, 0 minted, 0 carded. AC2 reads `FAIL-C23-MINT-BASIS` -- 0 rows added since the pinned base, and a campaign that closes its population with no mint at all is refused. **AC3 and AC4 read PASS at the cut and must STILL pass at your close** -- AC3 is the fence guard (it fails the moment `exemptions.json` moves) and AC4 is the registry's own validator. **C23R4-AC5, for `3.0.0_SA_CVO` at L9 (no verdict from you):** every `owner_basis` citation names a source that genuinely declares that resource rather than merely mentioning it; every card states what was measured and what the missing instrument is; and any BLOCKING card names the principal whose access would change.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, everything under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` AND `RAISE_POPULATION_S6.r3.md`, which is round 3's measured population. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot, `<k>` one above the highest `W<n>-S` id already present in ANY document under that channel). **Append your row at the END of the existing JSON array and keep every existing row's bytes and 2-space indentation exactly as they are** -- other branches append to the same file this round, and a re-serialized array cannot merge. Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Nothing live moves.** No AWS write, no Terraform apply, no deploy, no rename of a live resource, no `generate`. Every read of the live plane is read-only.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
infra/logic/registry/systems.json
infra/logic/registry/resources.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.3, round-4 cell `EN-c-23` (section 0d).
<owned_cells>EN-c-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `C23R4-AC1`, `C23R4-AC2`, `C23R4-AC3`, `C23R4-AC4`, `C23R4-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-c-23-r4.registry-campaign.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> C23R4-AC1,C23R4-AC2,C23R4-AC3,C23R4-AC4,C23R4-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-c-23-r4.registry-campaign.md` BEFORE the `complete` flip.
Result file `registry-campaign.r4.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`C23R4-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-4 cut. This cell is level 0 and gated by nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- registry rows only; no principal, policy or resource changes. The one path that WOULD touch an applied policy (exemptions.json) is refused by the fence guard and carded BLOCKING.
comp-adversary: RUN -- DENOMINATOR 351 population triples plus every row this round adds; adversarial shapes covered 3 of 3 known here (a guessed owner: refused by the citation resolving to a real file AND a line inside it; a card that points at no heading: refused by the anchor check; a campaign that cards everything and mints nothing: refused by the 0-rows-added reading). BLIND to whether a resolving citation's file genuinely DECLARES that resource rather than merely mentioning it -- that residue is C23R4-AC5, the CVO's at L9.
lane: TREE_REGISTRY / the worker's own deliverables folder; the <paths> block adds systems.json, resources.json and the channel.
contention: censused at the cut across both live projects' non-terminal orders. LGIC_LGCTFM's LT-x-1 writes scopes.json and remediations.json -- disjoint from this cell's two files. EN-h-24-r4 shares resources.json and is therefore this slot's queue position 2, never a parallel worker.
</preflight>

Seating: slot ~1, queue position 1. Round 4 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-3 analysis @`969f89b0e7`; issued by `2.0.0_SA_COO~G`. Decomposition v3.3, section 0d. Rulings carried: R-29 (mint rule + fence guard verbatim), R-32, R-33 (the bound), R-6 (the precedent).
