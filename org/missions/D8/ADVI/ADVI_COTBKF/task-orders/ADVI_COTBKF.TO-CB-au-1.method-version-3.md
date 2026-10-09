# TO ADVI_COTBKF.TO-CB-au-1.method-version-3 -- round 47 CB-au-1: Cottonwood's sources entry declares method_version 3; rebuild

<to_id>ADVI_COTBKF.TO-CB-au-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~74</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>47</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-au-1` (`decompositions/ADVI_COTBKF_DECOMP.round47.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

ADVI_COTBKF's adapter `data/assets/scripts/silver/commonwealth_account_return_daily.py` builds Cottonwood's `account_return_daily`
days locally. It builds them through IRPT_DASHBD's producer `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, using
Cottonwood's entry `_commonwealth_delivery` in `data/assets/scripts/gold/irpt_reporting/sources.json` (round 43). That gives 3,325 days
and 1,691,729 rows, with all three valuation fields present.

IRPT_DASHBD has now changed its producer (TO-DB-b-102 @e18a26ad12). `build_manifest`, the row frame and the method row take
`method_version` from the firm's entry:
- 2 is `custodian_reported`;
- 3 is `positions_based`;
- no entry writes `absent`;
- a positions-based entry naming 2 is refused.

The Cottonwood entry has no `method_version` yet. Record: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~77/
METHOD_FROM_SOURCE.json`.

**Your item.** No S3 write and no deploy.

1. **Add ONE key, `"method_version": 3`, to the `_commonwealth_delivery` entry** in `sources.json`. Nothing else in the file changes.
2. **Rebuild every day locally** with the adapter, through the changed producer, into `.scratch/advi_cotbkf/ard_cottonwood_r47/`, with
   a sha256 manifest. Read back ALL manifests and the rows' `method_version`:
   - every manifest reads `method_version` 3;
   - every row reads 3, or the producer's own blank rule for unmeasured rows (print which);
   - the three valuation fields stay present.
3. **Run IRPT_DASHBD's producer tests** (`data/assets/scripts/gold/irpt_reporting/tests/`) and the reporting-gold handler tests
   (`infra/aws/lambda/investor-reporting/reporting-gold/tests/`). Both must stay green.
4. **Rule first.** Commit the one-key change in its OWN commit before the rebuild run.

Write `method_version_3.md`. LAST line exactly: `ARD-COTTONWOOD-R47 days=<n> manifests_mv3=<m>/<n> rows_mv3=<r> producer_tests=<passed> handler_tests=<passed>`.

### ACCEPTANCE

<criterion id="CB47au1-AC1" cell_refs="CB-au-1"><invocation>python data/assets/scripts/silver/commonwealth_account_return_daily.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~74</invocation><expect>ARD-COTTONWOOD</expect></criterion>
`CB47au1-AC1` -- the rebuild runs, and the R47 line prints `manifests_mv3=<n>/<n>`.

<expected_criteria>CB47au1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Built files go under `.scratch/`,
  uncommitted.
- **In `sources.json`, the edit is ONE key in ONE entry.** The producer and the handler are never edited. If the adapter needs no
  change, leave it.
- **No S3 write.** Reads are limited to the served FWD-3 tables. Never read or list `opal-data-bd`, `opal-data-49financial`,
  `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W74-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/gold/irpt_reporting/sources.json
data/assets/scripts/silver/commonwealth_account_return_daily.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round47.md</decomp_doc> (round 47), cell `CB-au-1`.
<owned_cells>CB-au-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB47au1-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~74/ADVI_COTBKF.TO-CB-au-1.method-version-3.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB47au1-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the R47 line; the one-key diff; one manifest's method fields; the test lines; commits, with the rule commit first.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- 1 scheduled consumer of sources.json (the reporting-gold Lambda, packaging it by staged_from pins); BLIND: none beyond it; a repo edit reaches no deployed Lambda until IRPT_DASHBD redeploys, and the entry is underscore-prefixed (never a computed source).
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: RUN -- one key only; every manifest read back; IRPT_DASHBD's producer and handler tests green; BLIND: a row the producer blanks with no method_version (its own rule, printed).
lane: the <paths> block IS the grant (worker RULING 1); sources.json is IRPT_DASHBD's file, and ~D2 msg 3564 names this one-key declaration as CB-al-2's need.
</preflight>

Source: `2.0.0_SA_COO~D2` msg 3564 (TO-DB-b-102 @e18a26ad12); IRPT_DASHBD ADDENDUM 13.2 @304cb81ef6.
