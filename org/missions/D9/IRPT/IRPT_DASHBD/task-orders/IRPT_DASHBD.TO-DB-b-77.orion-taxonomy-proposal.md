# TO IRPT_DASHBD.TO-DB-b-77 -- E5: the rule-24 amendment proposal for the two Orion flow classes that depart from the ratified orion_cashflow_taxonomy.yaml -- four-postulate record, word-boundary token census, and their measured effect on the returns (row W49-S3)

<to_id>IRPT_DASHBD.TO-DB-b-77</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~54</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>37</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-36 ADDENDUM 5 (on ADJUDICATION_v21 @37daf4f637; PRD v0.9 @e8f96f579c), enrichment item E5 | **Decomp cell:** `DB-b-77` (decomposition section 39) | **outcome_ref:** FWD-11 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-54`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~54/`.

**The cell (`DB-b-77`).** Round 36 (DB-b-72, row W49-S3) measured two flow classes behaving differently from the RATIFIED
`C:/dev/wk-irpt-dashbd-54/data/inf/scripts/silver/orion_cashflow_taxonomy.yaml`:
- the Internal Account Journal pair;
- Federal/State Tax Withheld.

The CTO ruled (ADDENDUM 5) that the ratified taxonomy governs until amended, and that one cell writes the amendment proposal under the
taxonomy law. That law is CLAUDE.md rule 24; read it, and `rcg/rulings/RULINGS.jsonl` R-0006 and R-0009.

1. **`ORION_TAXONOMY_AMENDMENT_PROPOSAL.md`.**
   - State the proposed change.
   - Write one section per postulate, each heading naming it: MECE (over a DECLARED domain; hunt the uncovered member by subtraction from a
     printed denominator), SAME GRAIN, INTENT COHERENCE, and STATE COHERENCE (name which values this remedy does NOT move).
2. **`TOKEN_CENSUS.json`.** Run a word-boundary census of each proposed or changed token over the corpus: `comp-find -i` with
   `--corpus all`, its denominator printed. Record `census` [{token, hits, files_scanned}].
3. **`MEASURED_EFFECT.json`.** Run round 36's tie-out twice on the same sample and denominator: once under the ratified flow set and once
   under the proposed one. Record `{denominator, within_ratified, within_proposed}`. Read `deliverables/0.9.0_WK_IRPT_DASHBD~49/` for
   the sample and its `flow_set_probe`.

This cell writes a PROPOSAL. It does not edit the taxonomy file; the CTO rules on it.

<criterion id="DB37-5-AC1" cell_refs="DB-b-77"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-5-AC1</invocation><expect>DB37-5-AC1 PASS</expect></criterion>
`DB37-5-AC1` -- the proposal carries the four postulate sections. Base: FAIL.

<criterion id="DB37-5-AC2" cell_refs="DB-b-77"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-5-AC2</invocation><expect>DB37-5-AC2 PASS</expect></criterion>
`DB37-5-AC2` -- a word-boundary token census with its denominator. Base: FAIL.

<criterion id="DB37-5-AC3" cell_refs="DB-b-77"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-5-AC3</invocation><expect>DB37-5-AC3 PASS</expect></criterion>
`DB37-5-AC3` -- the measured within counts under the ratified and the proposed flow sets over one denominator. Base: FAIL.

<expected_criteria>DB37-5-AC1,DB37-5-AC2,DB37-5-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~54/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-77.orion-taxonomy-proposal.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 39 (round 37), cell `DB-b-77`.
<owned_cells>DB-b-77</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB37-5-AC1, DB37-5-AC2, DB37-5-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~54/IRPT_DASHBD.TO-DB-b-77.orion-taxonomy-proposal.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB37-5-AC1,DB37-5-AC2,DB37-5-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the proposed change in one line, the census, the two within counts, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: offline records and code in the worker folder; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB37-5-AC1/AC2/AC3 FAIL at base (no files). Row W49-S3; CTO ADDENDUM 5.
lane: the <paths> block IS the grant.
</preflight>
