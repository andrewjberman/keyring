# TO ADVI_COTBKF.TO-CB-o-1 -- round 15 CB-o-1: the near-match page regenerated from the served crosswalk

<to_id>ADVI_COTBKF.TO-CB-o-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~31</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-o-1` (`decompositions/ADVI_COTBKF_DECOMP.round15.md`) |
**outcome_ref:** FWD-8 (row D2-S25) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-o-1`, FWD-8: the crosswalk maps each old Commonwealth account to the client's Cottonwood account today. Accounts that score in the
near-match band -- `[NEAR_MIN, MIN_SHARE)`, i.e. 0.65 to 0.80, constants in `data/assets/scripts/silver/commonwealth_crosswalk.py` -- are
never linked by Opal; they go on a page for a person at Cottonwood to decide. The page put toward Andrew
(`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~14/near_matches.{csv,md}`) lists 21. The crosswalk was re-applied on
corrected transaction signs, and the run reported `near_matches=22`. Regenerate the page so it matches what Opal now serves.

Build `data/assets/scripts/analysis/commonwealth_near_match_page.py`, read-only, which:
1. reads the SERVED crosswalk (`opal_naming.address("commonwealth", <cottonwood scope via opal_naming.lookup>, "silver", "crosswalk",
   "date=2026-06-23")`, `crosswalk.parquet`) and records the VersionId it read (head_object);
2. takes the near-match set from it: rows whose `score` is in the band (import the constants; never type them);
3. builds each entry's position detail with the crosswalk's own generator (`crosswalk_rows` and `write_near_matches` from
   `commonwealth_crosswalk.py`, imported) over a local run on the same inputs, and requires the generator's set to equal the served set;
4. compares with the round-4 page and names each account that entered or left, with its score before (round 4's csv) and after (served);
5. writes `near_matches.csv` and `near_matches.md` to `--out` and prints as its LAST line exactly:
   `NEAR-MATCH-PAGE near_matches=<n> served_equals_generator=<True|False> crosswalk_version=<VersionId> entered=<e> left=<l> entered_accounts=<comma-separated>`.

**Tests** `data/assets/scripts/analysis/tests/test_commonwealth_near_match_page.py` (stubs, no AWS): a stub served table of 4 rows with 2 in
the band prints `near_matches=2`; a stub old page missing one of them prints `entered=1` and names it; a generator set that differs from the
served set prints `served_equals_generator=False` (the control).

### ACCEPTANCE

<criterion id="CB15o1-AC1" cell_refs="CB-o-1"><invocation>python data/assets/scripts/analysis/commonwealth_near_match_page.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~31</invocation><expect>NEAR-MATCH-PAGE near_matches=22 served_equals_generator=True</expect></criterion>
`CB15o1-AC1` -- the page from the served table, with the VersionId it read and the entries that entered or left on the same line (recorded,
not presumed).

<criterion id="CB15o1-AC2" cell_refs="CB-o-1"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_near_match_page.py</invocation><expect>passed</expect></criterion>
`CB15o1-AC2` -- the band, the entered/left diff and the served-vs-generator control on stubs.

<expected_criteria>CB15o1-AC1,CB15o1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Do not edit `commonwealth_crosswalk.py`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W31-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_near_match_page.py
data/assets/scripts/analysis/tests/test_commonwealth_near_match_page.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round15.md</decomp_doc> (round 15), cell `CB-o-1`.
<owned_cells>CB-o-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB15o1-AC1, CB15o1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~31/ADVI_COTBKF.TO-CB-o-1.near-match-page.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB15o1-AC1,CB15o1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the NEAR-MATCH-PAGE line, the entering account with its score before and after, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time page.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity on opal-data-assets; denominator 1 bucket; BLIND: none needed.
comp-adversary: RUN -- the list read from the SERVED table with its VersionId, the detail from the table's own generator, the two sets required equal; band constants imported; BLIND: Cottonwood's view of the clients.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-14 analysis @47ea1968e7, E1; row D2-S25.
