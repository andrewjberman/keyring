# TO LGIC_NAMING.TO-LN-l-3 -- the cross-bucket reader's scoring

<to_id>LGIC_NAMING.TO-LN-l-3</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~5</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Status (2026-09-14, the issuer `2.0.0_SA_COO~G`):** complete on `1.0.0_SA_CTO`'s RULING T, in `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md` s.6 @de52d3db04. The FAIL criterion is round 1's measurement, graded at L10 by that analysis, and the proof instance is VALID. The worker was right not to flip; the issuer flips on the ruling.

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.4 @e04b802fe9 (ADMITTED @254ac1f2ab) | **Decomp cell:** `LN-l-3` | **outcome_ref:** FWD-4 | **depends_on:** LN-l-2 (merged) | **slot:** ~5, queue position 3

---

## WORKER FACE

### THE CELL

`LN-l-3` -- the cross-bucket scoring (PRD candidate N5). **You score; you do not read.**

Run the two mechanical criteria below against `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/N5_KEY.json` and write `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n5-reader-score.md`: the checker's output verbatim, and every WRONG line. Six addresses are target-state specimens written to the ruled string (one is the v1.3 entity partition, one the v1.3 code tier). The seventh is a LIVE legacy tier-first key, the negative control.

**Read:** n5-reader.tsv, N5_ADDRESSES.json, N5_KEY.json.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="L3-AC1" cell_refs="LN-l-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py l3-correct</invocation><expect>VERDICT: PASS-ALL-CORRECT</expect></criterion>
`L3-AC1` -- every conforming address is labeled as the ruled string reads it.

<criterion id="L3-AC2" cell_refs="LN-l-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py l3-control</invocation><expect>VERDICT: PASS-CONTROL-FLAGGED</expect></criterion>
`L3-AC2` -- the live legacy tier-first address is marked DOES-NOT-FIT.

<expected_criteria>L3-AC1, L3-AC2</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13). Reading the live plane is done for you: the fixed inputs below are one pull, at one vintage, and you read them instead of pulling again.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_ln.py` (the checker every criterion calls), `LIVE_NAMES.json` (every live AWS name by node type, vintage 2026-09-14 12:13:53 UTC, 2,531 nodes, 33 types), `N6_SAMPLE.json`, `N3_ITEMS.json`, `N3_KEY.json`, `N5_ADDRESSES.json`, `N5_KEY.json`. Read only those this order names. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n5-reader-score.md
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v3 @62b5c0819f, cell `LN-l-3`.
<owned_cells>LN-l-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `L3-AC1`, `L3-AC2`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~5/LGIC_NAMING.TO-LN-l-3.cross-bucket-scoring.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> L3-AC1,L3-AC2` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `cross-bucket-scoring.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- self-test 6/6; the 540 s view scanned 5 of 5 carriers, 25 gates armed, none on LGIC_NAMING. This project registered G-A (DISCHARGED @3514843a12), G-B (LGIC_ENFORCE E9's comparison half), G-C (worker admission, checked after this issuance) and G-D (the three-writer .tf). None is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on the write set, not assumed: 13 markdown/TSV/JSON records under deliverables/ and one comment-only hunk in one .tf; no cell adds an operation, a policy, a principal or a resource, so the lens would receive an empty input.
comp-adversary: RUN at L5 on the PRD at v1.3 -- 6 of 6 cited commits verified; 11 cited paths, 9 stable, 2 GONE (GRADING_RULE.md and TENSION_RANKING.md, which this project mints). Not re-run at v1.4: that diff adds no cited path or commit. Blindness stated: its complement is filesystem adjacency (T11), not the dependency chain.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, or under infra/aws/, refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~5, queue position 3. Round 1 of LGIC_NAMING; issued by `2.0.0_SA_COO~G` on Andrew-direct ~13:4xZ ruling 1 (relayed 96594, record @0d3ad7d496). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: one live pull at vintage 2026-09-14 12:13:53 UTC (manifest b578e47d733f). The N6 sample is 85 + 3 by the decomposition's rule over distinct names (row LGIC_NAMING-S11).
