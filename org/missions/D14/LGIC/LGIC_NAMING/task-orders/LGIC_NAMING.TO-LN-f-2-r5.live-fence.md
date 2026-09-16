# TO LGIC_NAMING.TO-LN-f-2-r5 -- FWD-3's LIVE half: the fence over the live inventory

<to_id>LGIC_NAMING.TO-LN-f-2-r5</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.10 @592ff7a5de (ADMITTED; both halves current) | **Decomp cell:** `LN-f-2` (round 5, NEW at decomposition v7 section 0f) | **outcome_ref:** FWD-3 (its LIVE half) | **depends_on:** none -- one of three independent chains | **slot:** ~4, queue position 1

---

## WORKER FACE

### THE CELL

`LN-f-2` -- **the first criterion in this project's history that reads the LIVE plane.** FWD-3's repo half is REALIZED; its live half has never been measured. RULING R-17 classified it LIVE for the text's own reason: *"catches ALL of them"* is a claim about the SET of a firm's systems, and a repo read cannot see a system the repo never declared. RULING R-20 then cut this cell into three clauses so it cannot pass on an empty claim set.

**You write ONE record: `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r5/f2-live-fence.r5.md`,** carrying ONE json fence:

```json
{ "vintage": "<the comp-find VINTAGE line, verbatim>",
  "nodes_scanned": <int from the DENOMINATOR line>,
  "firms": { "49financial": ["<live IAM_ROLE node name>", ...],
             "inflection": [...], "cottonwood": [...], "demo": [...] } }
```

1. **Read the live plane with the estate's own instrument.** `comp-find --corpus aws <firm key>` for each of the four firm keys. **Never `simulate-policy`** (R-17 names it by name). Record the tool's own `VINTAGE` line and its `DENOMINATOR` nodes-scanned figure -- those ARE the provenance, not something you compute.
2. **The fence is BUILDER OUTPUT, never typed.** `fence_patterns(<firm long>)` from `lib/opal_naming.py`. So is every canonical form: `grade(<name>, "IAM_ROLE")`.
3. **What you will find, said plainly so it is not a surprise:** at the cut, **0 of 4** live IAM roles carrying a firm key are caught by that firm's own fence (row LGIC_NAMING-S25). R-20 ruled that this is **not** a defect in the rule or the generator: the four are legacy-named and belong to LGIC_ENFORCE DEC-4(ii)'s existing-writer re-identification and to their owners. **Your job is to MEASURE and RECORD it, not to fix it and not to explain it away.**

**Read:** `lib/opal_naming.py` (`fence_patterns`, `grade`, `name`); `infra/logic/registry/scopes.json`; `infra/aws/terraform/modules/opal_name/generated_locals.tf` (the generated fence map); RULING R-17 and R-20 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md`; row `LGIC_NAMING-S25` in the channel.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="F2R5-AC1" cell_refs="LN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_ln_r5.py f2-positive</invocation><expect>VERDICT: PASS-FENCE-CLAIMS-ITS-OWN</expect></criterion>

<criterion id="F2R5-AC2" cell_refs="LN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_ln_r5.py f2-negative</invocation><expect>VERDICT: PASS-FENCE-EXCLUDES-OTHERS</expect></criterion>

<criterion id="F2R5-AC3" cell_refs="LN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_ln_r5.py f2-coverage</invocation><expect>VERDICT: PASS-COVERAGE-DISCLOSED</expect></criterion>

<criterion id="F2R5-AC4" cell_refs="LN-f-2"><invocation>cd <WS> && timeout 180 comp-find --corpus aws cottonwood --limit 40</invocation><expect>DENOMINATOR: [0-9]+ hit\(s\) across [0-9]+ aws node\(s\) scanned</expect></criterion>

<criterion id="F2R5-AC5" cell_refs="LN-f-2" judgment="true"/>

<expected_criteria>F2R5-AC1, F2R5-AC2, F2R5-AC3, F2R5-AC4, F2R5-AC5</expected_criteria>

**F2R5-AC4 is the LIVE-PLANE criterion R-17 requires**: the estate instrument named in the invocation itself, not a repo record standing in for it. A LIVE row cut against a repo record is returned to the issuer, not worked.

**F2R5-AC3 is DISCLOSURE, NOT A BAR** (R-20 iii). It PASSES whatever the coverage number is -- including 0 of 4 -- provided the vintage, the nodes scanned, and every UNCAUGHT node with its `grade()` verdict and canonical form are printed. **A low number here is the finding, not a failure.**

**F2R5-AC5, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether your record's `firms` lists are the whole of what `comp-find` returned for each key, and whether your `vintage` and `nodes_scanned` are the tool's own words. Also: name what this read CANNOT see -- a firm's role that carries no firm key in its name is outside a text match, and this cell does not claim otherwise.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file. Nothing else.
- **READ-ONLY ON AWS, ABSOLUTELY.** `comp-find --corpus aws` is a READ of a built database. You create, modify and delete NOTHING in AWS. No `aws` write command, no Terraform, no rename of a live resource. If a criterion seems to ask for a write, it does not -- file a BLOCKING row.
- **Never `simulate-policy`** (R-17, by name).
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including `fixed_inputs/r5/check_ln_r5.py`. If you believe the checker is wrong, file a BLOCKING row rather than working around it.
- **Surprises** go to `surprise-channel/investigations/INVESTIGATION_v1.md`, ONE row each, id `LGIC_NAMING-W4-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names and cite them, never the CLAUDE.md or memory text every worker starts with.
- **Numbers** here are context, never acceptance values, except where a criterion prints one. The `0 of 4` is the issuer's measurement at the cut; yours is whatever your own run reads.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r5/f2-live-fence.r5.md
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v7.1, cell `LN-f-2`, round 5 (section 0f).
<owned_cells>LN-f-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F2R5-AC1`, `F2R5-AC2`, `F2R5-AC3`, `F2R5-AC4`, `F2R5-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~4/LGIC_NAMING.TO-LN-f-2-r5.live-fence.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F2R5-AC1,F2R5-AC2,F2R5-AC3,F2R5-AC4,F2R5-AC5` BEFORE the `complete` flip.
Result file `live-fence.r5.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `F2R5-AC5` is a JUDGMENT criterion -- `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`. **Flip `complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the recut. Gates G-A DISCHARGED, G-B met round 1, G-C at spawn. This cell is gated by G-C only.
comp-iam: DECLARED-NOT-APPLICABLE -- READ-ONLY on the AWS plane, measured rather than asserted: the cell's only AWS contact is comp-find --corpus aws, a read of a built node database whose vintage is its own built: line. No operation, policy, principal or resource is added, changed or removed. PRD S13's "nothing live moves" holds -- reading the live plane is not moving it, and the order forbids every write path by name.
comp-adversary: DECLARED-NOT-APPLICABLE -- this cell introduces no external citation; the 0 of 4 is the issuer's measurement at the cut (row LGIC_NAMING-S25) and is given as CONTEXT with that provenance, so a worker who reads a different number records its own. R-20 was re-derived by 1.0.0_SA_CTO on a third instrument (the builder) before this cell was cut.
lane: the <paths> block IS the grant. The registry and lib/ are excluded -- the fence and every canonical form are READ from the builder, never authored here.
contention: LN-f-2 writes exercises/r5/f2-live-fence.r5.md alone. No other round-5 cell names that path.
</preflight>

Seating: slot ~4, queue position 1. Round 5 of LGIC_NAMING, the CLOSING round, recut of `1.0.0_SA_CTO`'s round-4 analysis (@5a12d0b97c, msg 97396) as re-cut by RULING R-20 (@00196f8bee); issued by `2.0.0_SA_COO~G`. Decomposition v7.1, section 0f.
