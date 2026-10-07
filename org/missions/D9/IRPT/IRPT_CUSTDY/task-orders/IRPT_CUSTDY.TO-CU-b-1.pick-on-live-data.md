# TO IRPT_CUSTDY.TO-CU-b-1 -- round 2 CU-b-1 (E1): the advisor pick runs on live data -- the 'None' key's source named and fixed or routed, refused accounts counted

<to_id>IRPT_CUSTDY.TO-CU-b-1</to_id>
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

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-b-1` (`decompositions/IRPT_CUSTDY_DECOMP.round2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (round 1's code is at HEAD)

---

## WORKER FACE

### THE CELL

`CU-b-1`, item E1 of the CTO's round-1 analysis: "The advisor pick runs on live data." Round 1's tool
`data/assets/scripts/gold/irpt_custody/advisor_client_list.py` crashed on the real map: `--pick --as-of 2026-09-30 --ownership
s3://opal-data-bd/platinum/49financial/ownership_map.json` read Schwab silver for both masters, then raised `ids.IdRefused: a raw key
must be a non-empty value; got str(len=4, opaque-text)` in `book_of` (line ~226) via `ids.project`. Census over that map: 7022
distinct granted accounts, 6540 projected, 482 refused, 31 of 190 advisors affected. The refused value is the literal string `'None'`.

**Where it comes from (READ, never edit unless it is in your grant):** `infra/aws/lambda/investor-reporting/_ids/ids.py` line 387:
`mapped = idx.get(str(raw).strip())` then `base("account", mapped)`; the index comes from `load_seam_index` in the same file, and
`projection_for_firm(firm_id, registry_path=None)` at line 396. Trace where the index's VALUES are made (a loader that stringifies a
null, or a producer that writes `None` into the seam file). That code belongs to IRPT_BCKEND: **you do not edit it.** You name it.

**Build:**
1. A NEW script `data/assets/scripts/gold/irpt_custody/none_source.py --ownership <map>`: find the refused accounts, follow the
   projection to where `'None'` is produced, and print
   `NONE-SOURCE file=<repo path>:<line> owner=<project that owns that file> refused=<n> distinct=<m>`. If that line is in another
   project's path, also file a surprise row naming it (the issuer routes the fix; constraint 1 of the decomposition).
2. In `advisor_client_list.py`, `book_of` / the pick: an account the projection refuses is counted as UNCOVERED with reason `PROJECTION_REFUSED`, never raised.
   An advisor with any uncovered account stays ineligible (the CTO's rule: every account covered).
3. The pick's last line becomes `ADVISOR-PICK scanned=<s> eligible=<e> pick=<id> households=<h> classes=<c> projection_refused=<r>
   of=<distinct>`, and each `CENSUS` line carries the advisor's refused count.
4. Tests in a NEW file `data/assets/scripts/gold/irpt_custody/tests/test_advisor_projection_refused.py` (round 1's
   `test_advisor_client_list.py` must still pass; edit it only if a signature you change requires it): a projection that refuses
   one account makes that account uncovered with `PROJECTION_REFUSED` and does not raise; the refused count and denominator print in
   `ADVISOR-PICK`; `none_source.py` on a fixture map and fixture seam index prints `NONE-SOURCE file=`.

### ACCEPTANCE

<criterion id="CU5-AC1" cell_refs="CU-b-1"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_advisor_projection_refused.py</invocation><expect>passed</expect></criterion>
`CU5-AC1` -- refused accounts counted not raised, the denominator printed, the explain mode on a fixture; round 1's tests still pass.

<criterion id="CU5-AC2" cell_refs="CU-b-1"><invocation>python data/assets/scripts/gold/irpt_custody/advisor_client_list.py --pick --as-of 2026-09-30 --ownership s3://opal-data-bd/platinum/49financial/ownership_map.json</invocation><expect>ADVISOR-PICK scanned=</expect></criterion>
`CU5-AC2` -- the seam against its REAL neighbour: the pick completes on the live map (round 1 raised here). The counts are reported,
not graded; the map refreshes daily.

<criterion id="CU5-AC3" cell_refs="CU-b-1"><invocation>python data/assets/scripts/gold/irpt_custody/none_source.py --ownership s3://opal-data-bd/platinum/49financial/ownership_map.json</invocation><expect>NONE-SOURCE file=</expect></criterion>
`CU5-AC3` -- the source of the `'None'` value named at file:line on the live map (the analysis's E1 criterion 1).

<expected_criteria>CU5-AC1,CU5-AC2,CU5-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS: read only**, through the `.tools/aws` shim or boto3: `opal-data-bd/platinum/49financial/ownership_map.json` and Schwab silver
  under `opal-data-assets/schwab/`. A read the dell2 user is denied is a row, never a workaround. No write anywhere.
- **Never print a full account number.** Never edit `infra/aws/lambda/investor-reporting/_ids/` or any other project's file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W5-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/gold/irpt_custody/advisor_client_list.py
data/assets/scripts/gold/irpt_custody/tests/test_advisor_client_list.py
data/assets/scripts/gold/irpt_custody/tests/test_advisor_projection_refused.py
data/assets/scripts/gold/irpt_custody/none_source.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round2.md</decomp_doc> (round 2), cell `CU-b-1`.
<owned_cells>CU-b-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU5-AC1, CU5-AC2, CU5-AC3. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~5/IRPT_CUSTDY.TO-CU-b-1.pick-on-live-data.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU5-AC1,CU5-AC2,CU5-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `NONE-SOURCE` line with the code at that line, the real `ADVISOR-PICK` line, the test list, rows, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a tool run by hand; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads opal-data-bd and opal-data-assets with the dell2 box profile (both measured readable 2026-10-07).
comp-adversary: RUN -- cross-firm (49financial scope only, lookup()); read-only; BLIND: where the seam index's values are produced (the cell's first act).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Third criterion: the analysis's E1 names three; the source naming (AC3) is a separate invocation from the pick (AC2).
Source: round-1 analysis @822468e309 section 3 E1; rows S3, S2; decomposition round 2 constraints 1-2.
