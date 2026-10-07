# TO IRPT_CUSTDY.TO-CU-b-2 -- round 2 CU-b-2 (E2): the chosen advisor, by census, written to a file

<to_id>IRPT_CUSTDY.TO-CU-b-2</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~5</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-b-2` (`decompositions/IRPT_CUSTDY_DECOMP.round2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** `IRPT_CUSTDY.TO-CU-b-1` (same worker queue; this order starts when CU-b-1 is complete)

---

## WORKER FACE

### THE CELL

`CU-b-2`, item E2 of the CTO's round-1 analysis: "The chosen advisor, by census." The CTO's ruling (msg 103): from the 49 Financial
advisors, the one with the FEWEST households among those with 10 OR MORE, whose EVERY account has Schwab silver rows at 2026-09-30;
ties by the MOST asset classes held, then advisor id ascending. You built the pick in CU-b-1; this order runs it on the live map and
writes the census and the pick to a FILE the issuer records in the decomposition.

**Build a NEW script `data/assets/scripts/gold/irpt_custody/advisor_census.py`** (it imports the pick from `advisor_client_list.py`;
no second copy of the rule) taking `--as-of`, `--ownership` and `--census-out <path>`, that runs the pick and writes a
Markdown file: a header with the map's key, its LastModified and the run time (UTC); one table row per advisor scanned (advisor id,
households, accounts, accounts covered at the as-of, projection-refused, eligible yes/no and why not); then the pick line exactly as
printed. After writing, print `CENSUS-WRITTEN advisors=<n> eligible=<e> pick=<id> path=<path>`. Never write a full account number.

### ACCEPTANCE

<criterion id="CU6-AC1" cell_refs="CU-b-2"><invocation>python data/assets/scripts/gold/irpt_custody/advisor_census.py --as-of 2026-09-30 --ownership s3://opal-data-bd/platinum/49financial/ownership_map.json --census-out org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~5/ADVISOR_CENSUS_20260930.md</invocation><expect>CENSUS-WRITTEN advisors=</expect></criterion>
`CU6-AC1` -- the real census and pick on the live map, written to the deliverable file (the analysis's E2 criteria 1 and 2). The pick
itself is reported, not graded; commit the census file with your proof.

<expected_criteria>CU6-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **AWS: read only**, as in CU-b-1. No write anywhere outside your deliverables folder.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W5-S<k>`), and do not weaken it. A pick of `NONE` is a result to report, not a failure to hide.

<paths>
data/assets/scripts/gold/irpt_custody/advisor_census.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round2.md</decomp_doc> (round 2), cell `CU-b-2`.
<owned_cells>CU-b-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU6-AC1. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~5/IRPT_CUSTDY.TO-CU-b-2.advisor-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU6-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `CENSUS-WRITTEN` line, the pick, the eligible count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-off census run by hand; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads opal-data-bd and opal-data-assets with the dell2 box profile.
comp-adversary: RUN -- cross-firm (49financial only); read-only; BLIND: the map refreshes daily, so the census is dated by its header.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-1 analysis @822468e309 section 3 E2; CTO ruling msg 103; decomposition round 2.
