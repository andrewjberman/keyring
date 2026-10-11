# TO IRPT_DASHBD.TO-DB-b-120 -- the dim_return_method contract lists method row 3, and tieout_tolerance_proposed takes the same claim as the five thresholds -- one LOCAL cell before the Cottonwood mint; no S3 write

<to_id>IRPT_DASHBD.TO-DB-b-120</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~95</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>64</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ruling msg 4143 on row IRPT_DASHBD-D2-W93-S3 (both parts, one LOCAL cell) | **Decomp cell:** `DB-b-120` (decomposition section 66) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-118 (drained @4d4e3ee317).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-95`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~95/`.

**THE CLIENT-DATA RULE (binding):** never print an account number or a client figure in a commit message, a record, a row or a report. Fixtures are
synthetic. Do not print the pinned 49F thresholds file from git history.

**The cell (`DB-b-120`).** DB-b-118 gave the five thresholds of a `dim_return_method` row a per-value claim and took the contract to 0.4.0. The CTO
ruled two things left open by its row `IRPT_DASHBD-D2-W93-S3` (msg 4143):
1. **The contract lists method row 3.** A dim row written for a method the contract does not list is a served row outside its own contract. Row 3 is
   already `METHOD_ROWS[3]` in the producer; this is the contract catching up, with its rule-24 record.
2. **`tieout_tolerance_proposed` takes the same claim as the five thresholds.** Today it lands as a bare null (and null-typed) when no tie-out is
   passed. A null with no claim is a value a consumer cannot reject on; for Cottonwood, where no tie-out has been run, it reads `absent`.

Read in `C:/dev/wk-irpt-dashbd-95` first: `emit_method_row`, `METHOD_ROWS`, `THRESHOLD_CLAIMS` and the claim validation in
`data/assets/scripts/gold/irpt_reporting/account_return_daily.py`; `tests/test_threshold_claims.py`; the contract
`org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json` in full; DB-b-118's record
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~93/THRESHOLD_CLAIM_RULE24.json` (its decision is the rule you extend);
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~91/ROW3_VS_COTTONWOOD.json` (what row 3 states, field by field).

1. **Rule-24 record first** (`ROW3_AND_TIEOUT_CLAIM.json`, key `rule24` {mece, same_grain, intent_coherence, state_coherence}, each {finding,
   evidence: [{file, line}]}), covering both changes: that the tie-out is a sixth member of the SAME claim domain ("how the row's writer knows this
   value") at the same grain, and that listing row 3 adds a method row and no enum member. Commit it before any code.
2. **Producer, minimum change:**
   - the row gains ONE column `tieout_tolerance_proposed_claim`, a member of `THRESHOLD_CLAIMS` (the set itself is unchanged);
   - a stated claims object MAY carry the key `tieout_tolerance_proposed`; when it does, the same rules bind (a claim outside the set refuses; null
     only under `absent`; a value never under `absent`);
   - when it does not, the no-claims rule DB-b-118 decided applies to this one value: a null reads `absent`, a value reads `held`. A caller that
     passes five stated threshold claims and no tie-out therefore still works unchanged;
   - `tieout_tolerance_proposed` is written with the arrow type the contract names, so a null lands typed.
   Nothing else in the producer changes; `comparability()` and the grading paths are untouched.
3. **Contract to 0.5.0:** the new column (string, non-nullable, its meaning); `tieout_tolerance_proposed` nullable with "null only under the claim
   `absent`"; `method_versions` gains row 3, each field taken from `METHOD_ROWS[3]` and the writer, with the fields the row leaves to the source entry
   named as such (use ~91's field list; do not invent a value); `schema_hash` recomputed by the file's declared basis; `supersedes` names 0.4.0 and
   its hash; `rule24_record` points at your record. `landed_row` is not touched.
4. **Tests** in `data/assets/scripts/gold/irpt_reporting/tests/` (a new file): no tie-out with five absent claims gives a null value, claim `absent`,
   typed; a tie-out value with no stated claim reads `held`; a stated tie-out claim outside the set refuses; a null under `measured` refuses; the
   existing columns' arrow types on a row with values are unchanged against 0.4.0's `name:type` lines. Keep both test folders passing.
5. Record `tests` {passed, failed, new_test} and `row_example` (the all-absent row's claim fields) in the same JSON.

**No S3 write, no AWS call, no deploy.**

<criterion id="DB64-1-AC1" cell_refs="DB-b-120"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r64/p64_round64.py" . DB64-1-AC1</invocation><expect>DB64-1-AC1 PASS</expect></criterion>
`DB64-1-AC1` -- the contract at 0.5.0 lists row 3 and names exactly the row's columns, and the tie-out carries its claim and is typed. Base: FAIL.

<criterion id="DB64-1-AC2" cell_refs="DB-b-120"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r64/p64_round64.py" . DB64-1-AC2</invocation><expect>DB64-1-AC2 PASS</expect></criterion>
`DB64-1-AC2` -- the rule-24 record answers the four postulates with file-and-line evidence and the new test file passes. Base: FAIL.

<expected_criteria>DB64-1-AC1,DB64-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `infra/` or `portal/`, and under `data/` only the paths in the grant.
- **AWS:** none. NO Black Diamond or vendor call, no secret read, no S3 read or write, no deploy, no bun, no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~95/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~95/
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/
org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-120.row3-in-contract-tieout-claim.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 66 (round 64), cell `DB-b-120`.
<owned_cells>DB-b-120</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB64-1-AC1, DB64-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~95/IRPT_DASHBD.TO-DB-b-120.row3-in-contract-tieout-claim.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB64-1-AC1,DB64-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the contract diff in summary (version, the column, row 3's fields, old and new schema_hash), the all-absent row's claim fields, test counts for both folders, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the dim_return_method row writer and its contract; the returns tables and the gold Lambda's run do not read this path.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call, no new key.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB64-1-AC1 and DB64-1-AC2 FAIL at base (contract 0.4.0; no record). CTO ruling msg 4143.
lane: the <paths> block IS the grant.
</preflight>
