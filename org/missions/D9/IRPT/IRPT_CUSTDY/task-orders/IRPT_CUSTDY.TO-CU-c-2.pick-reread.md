# TO IRPT_CUSTDY.TO-CU-c-2 -- round 3 CU-c-2 (E1): the 482 re-read -- the pick on the fixed seam, refused counts before and after, every remaining refusal with its reason

<to_id>IRPT_CUSTDY.TO-CU-c-2</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~8</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~K2-E1</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-c-2` (`decompositions/IRPT_CUSTDY_DECOMP.round3.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (IRPT_BCKEND's seam fix @b43f82c155 is in HEAD)

---

## WORKER FACE

### THE CELL

`CU-c-2`, item E1 of the CTO's round-2 analysis: "the 482 re-read". In round 2 the advisor pick on the live ownership map counted 482 of
7022 distinct granted accounts as refused by the custodian-key projection, because IRPT_BCKEND's seam file
`infra/aws/lambda/investor-reporting/_ids/data/custodian_key_seam.json` held 826 values as the string `'None'`. IRPT_BCKEND has fixed it
(drain @b43f82c155): the seam drops those 826 values, and `infra/aws/lambda/investor-reporting/_ids/ids.py` line ~388 now returns the RAW
account for an empty, `'None'` or `'nan'` mapping instead of minting the string. You measure what that changed for this project.

**What exists (READ, never edit):**
- `data/assets/scripts/gold/irpt_custody/advisor_client_list.py` -- the pick (`book_of`, the census lines, the
  `ADVISOR-PICK ... projection_refused=<r> of=<distinct>` line); import its functions, no second copy of the rule.
- The BEFORE figure: `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~5/ADVISOR_CENSUS_20260930.md` -- round 2's
  census; its pick line reads `projection_refused=482 of=7022` and names the pick `matthew_gooch`. Parse it; never re-type 482.
- The ownership map: `opal_naming.legacy_address('blackdiamond-platinum-49financial-ownership-map')` (never type the key).
- Schwab silver under `opal-data-assets/schwab/<master>/silver/` (readable from dell2).

**A behaviour change you must measure, not assume:** "unmapped returns the raw account" means an account the seam does not map now
projects from its raw value, which may be an id no directory entry carries. So an account can stop being REFUSED and still not be
COVERED. Every account the pick does not count as covered gets exactly ONE reason from this closed set, and the counts per reason sum to
the uncovered total: `PROJECTION_REFUSED` (the projection still raises), `NOT_IN_DIRECTORY` (it projects, but no directory entry carries
the id), `NO_SILVER_AT_AS_OF` (it is in the directory but Schwab silver has no position row at the as-of).

**Build `data/assets/scripts/gold/irpt_custody/pick_reread.py`:**
1. CLI: `--as-of <YYYY-MM-DD>` (default `2026-09-30`), `--before-census <path>` (required), `--advisor <slug>` (the pick to re-check;
   default: the pick named in the census), `--self-test`. Device-free; read-only.
2. Run the pick on HEAD's seam over the live map; print one line per reason with its count; then the LAST line:
   `PICK-REREAD before_refused=<from census> after_refused=<n> of=<distinct> uncovered=<n> reasons_sum_ok=<True|False>
   advisor=<slug> advisor_still_eligible=<True|False> pick_now=<slug|NONE>`.
3. Never print a full account number (last 4 at most, and only if an example is needed).
4. `--self-test`: a fixture census (before 3 of 10), a fixture map, seam, directory and silver where after the fix one account becomes
   covered, one becomes `NOT_IN_DIRECTORY`, one stays `PROJECTION_REFUSED`; print, as the LAST line,
   `PICK-REREAD-SELFTEST before_ok=<..> after_ok=<..> reasons_ok=<..> eligible_ok=<..>`.
5. Tests `data/assets/scripts/gold/irpt_custody/tests/test_pick_reread.py` (pytest, `tmp_path`, insert the module's directory into
   `sys.path`; no `__init__.py`): BEFORE parsed from the census, never typed; the reasons are the closed set and sum to the uncovered
   total; an account that projects but is in no directory entry is `NOT_IN_DIRECTORY`; the advisor re-check reports False when one of its
   accounts becomes uncovered.

### ACCEPTANCE

<criterion id="CU9-AC1" cell_refs="CU-c-2"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_pick_reread.py</invocation><expect>passed</expect></criterion>
`CU9-AC1` -- the re-read's behaviour on fixtures: before from the census, the closed reason set and its sum, the eligibility re-check.

<criterion id="CU9-AC2" cell_refs="CU-c-2"><invocation>python data/assets/scripts/gold/irpt_custody/pick_reread.py --as-of 2026-09-30 --before-census org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~5/ADVISOR_CENSUS_20260930.md</invocation><expect>reasons_sum_ok=True</expect></criterion>
`CU9-AC2` -- the seam against its REAL neighbour: the live map on HEAD's fixed seam. The before/after counts and the eligibility verdict
are reported, not graded (the map refreshes daily); the reasons must sum.

<expected_criteria>CU9-AC1,CU9-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS: read only** -- the ownership map (via legacy_address) and Schwab silver under `opal-data-assets/schwab/`. A denied read is a
  row, never a workaround. No write anywhere outside your deliverables folder.
- **Never edit** `advisor_client_list.py`, `infra/aws/lambda/investor-reporting/_ids/` or any other cell's or project's file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W8-S<k>`; `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do
  not weaken the test.

<paths>
data/assets/scripts/gold/irpt_custody/pick_reread.py
data/assets/scripts/gold/irpt_custody/tests/test_pick_reread.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round3.md</decomp_doc> (round 3), cell `CU-c-2`.
<owned_cells>CU-c-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU9-AC1, CU9-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~8/IRPT_CUSTDY.TO-CU-c-2.pick-reread.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU9-AC1,CU9-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the real `PICK-REREAD` line and the per-reason counts, the test list, rows, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-off re-read by hand; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads opal-data-bd (legacy_address) and opal-data-assets with the dell2 box profile, both measured readable 2026-10-07.
comp-adversary: RUN -- cross-firm (49financial only); read-only; BLIND: how many raw accounts the directory carries after the seam fix (the cell's measurement).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-2 analysis @10e64fe9df section 3 (gate 'E-P8 drained' -> E1, criteria 1-3); IRPT_BCKEND drain @b43f82c155 (msg 299); decomposition round 3 "E1" section.
