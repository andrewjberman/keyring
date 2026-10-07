# TO IRPT_CUSTDY.TO-CU-e-1 -- round 5 CU-e-1 (E1): the chosen advisor's 4 unkeyed accounts, measured -- found under another key, or not covered with the reason

<to_id>IRPT_CUSTDY.TO-CU-e-1</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~13</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-e-1` (`decompositions/IRPT_CUSTDY_DECOMP.round5.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CU-e-1`, item E1 of the CTO's round-4 analysis: "the 4 unkeyed accounts, measured". The chosen advisor (`matthew_gooch`, as-of 2026-09-30)
has 18 granted accounts in the ownership map; 14 are reported. 4 are NOT_IN_DIRECTORY and absent from IRPT_BCKEND's custodian key seam
(`infra/aws/lambda/investor-reporting/_ids/data/custodian_key_seam.json`, 5376 entries), so `hop3_real_run.py`'s `schwab_key()` returns
None and they are listed uncovered as `NO_SCHWAB_KEY` -- with no report. Masked, they are `****9851`, `****0041`, `****7341`, `****9421`.

**What exists (READ):**
- `data/assets/scripts/gold/irpt_custody/hop3_real_run.py` (your edit target for criterion 3), `advisor_client_list.py`, the ownership map
  via `opal_naming.legacy_address('blackdiamond-platinum-49financial-ownership-map')`.
- Schwab silver under `opal-data-assets/schwab/<master>/silver/` for masters `08242234` and `08335338` (account tables such as `fact_acc`,
  `fact_rps`, `fact_trn`; read their key columns), and the custodian key seam above.
- IRPT_BCKEND's census of every NOT_IN_DIRECTORY account with its cause:
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~144/IB64-1_directory_coverage.json` (opaque ids; classes
  `no bridge source`, `xref unresolved`, `absent from feed`).

**Build:**
1. A NEW script `data/assets/scripts/gold/irpt_custody/unkeyed_lookup.py --advisor <slug> --as-of <d>` that, for each of the advisor's
   NOT_IN_DIRECTORY accounts with no seam key, looks it up by EVERY identifier you can name (the raw ownership-map key; its digits with and
   without leading zeros / padding to Schwab's widths; the opaque id; every Schwab silver key column of both masters; the census row) and
   prints one line per (account, identifier) with its result, then per account `UNKEYED account=****NNNN class=<FOUND_UNDER_OTHER_KEY|NOT_HELD>
   evidence=<what matched or the census cause>`, then `UNKEYED-LOOKUP advisor=<slug> accounts=<n> found=<n> not_held=<n> classified=<n>`.
   Never print a full account number.
2. In `hop3_real_run.py`: an account classed NOT_HELD renders in its client's report DATA (the account document, under its household) as
   `"not_covered": {"reason": "<text>"}` with no figures -- never dropped, never zero-filled. A FOUND_UNDER_OTHER_KEY account is NOT re-keyed here
   (the seam is IRPT_BCKEND's): it is reported in your report as a seam-cell candidate, and stays `NO_SCHWAB_KEY` in the data.
3. Tests in a NEW file `data/assets/scripts/gold/irpt_custody/tests/test_unkeyed_lookup.py` (fixtures, stubbed readers, no AWS): each lookup
   identifier tried and printed; FOUND vs NOT_HELD classed with evidence; a NOT_HELD account appears in the report data as `not_covered`
   with its reason. Round 3/4 tests (`test_hop3_real_run.py`, `test_hop3_directory_gap.py`) must still pass; edit them only where the
   `not_covered` field requires.

### ACCEPTANCE

<criterion id="CU14-AC1" cell_refs="CU-e-1"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_unkeyed_lookup.py</invocation><expect>passed</expect></criterion>
`CU14-AC1` -- every identifier tried, each account classed with evidence, NOT_HELD rendered as `not_covered` in the data, on fixtures.

<criterion id="CU14-AC2" cell_refs="CU-e-1"><invocation>python data/assets/scripts/gold/irpt_custody/unkeyed_lookup.py --advisor matthew_gooch --as-of 2026-09-30</invocation><expect>classified=4</expect></criterion>
`CU14-AC2` -- the seam against its REAL neighbour: the advisor's 4 real accounts looked up in real Schwab silver and the census on dell2.
found/not_held split is reported, not graded; every one of the 4 must be classed.

<criterion id="CU14-AC3" cell_refs="CU-e-1"><invocation>python data/assets/scripts/gold/irpt_custody/tests/run_suite_check.py</invocation><expect>failed=0 errors=0</expect></criterion>
`CU14-AC3` -- the whole `irpt_custody` suite on your branch stays green (your change to `hop3_real_run.py` must not break round 3/4 tests).

<expected_criteria>CU14-AC1,CU14-AC2,CU14-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS: read only.** Never edit the seam or any IRPT_BCKEND file. Never commit a real-run output file. Never print a full account number.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W13-S<k>`; `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do
  not weaken a test.

<paths>
data/assets/scripts/gold/irpt_custody/unkeyed_lookup.py
data/assets/scripts/gold/irpt_custody/tests/test_unkeyed_lookup.py
data/assets/scripts/gold/irpt_custody/hop3_real_run.py
data/assets/scripts/gold/irpt_custody/tests/test_hop3_real_run.py
data/assets/scripts/gold/irpt_custody/tests/test_hop3_directory_gap.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round5.md</decomp_doc> (round 5), cell `CU-e-1`.
<owned_cells>CU-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU14-AC1, CU14-AC2, CU14-AC3. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~13/IRPT_CUSTDY.TO-CU-e-1.unkeyed-accounts.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU14-AC1,CU14-AC2,CU14-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the real `UNKEYED` lines and the `UNKEYED-LOOKUP` line, any FOUND account's other key (masked) as a seam-cell candidate, the SUITE line, rows, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a measurement run by hand; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads opal-data-assets, opal-data-bd and opal-data-49financial with the dell2 box profile.
comp-adversary: RUN -- cross-firm (49financial only); read-only; the seam is never edited here; BLIND: which Schwab key columns exist on each master (the cell enumerates them).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-4 analysis @16d9b128c0 section 3 E1; row W10-S1; IRPT_BCKEND census msg 413; decomposition round 5 constraint 1.
