# TO MDPF_SECCLASS.TO-SC-t1 -- thread hop 1: the BD classifier library reads etf-classifications

<to_id>MDPF_SECCLASS.TO-SC-t1</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~3</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-t-1` (`decompositions/MDPF_SECCLASS_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-t-1`, thread hop 1 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` section 2). FWD-1: "An advisor
opens a Black Diamond client's holdings and sees each security's class and sub-class exactly as Opal's one shared list
holds it ... gold funds such as GLD and PHYS read as commodities and VXX reads as a hedge ... the old Black Diamond copy
of the list was never consulted at any step."

`data/black_diamond/scripts/gold/lib/etf_classifier.py` (the `ETFClassifier` singleton) today scans DynamoDB
`bd-securities` (10,929 rows) and resolves in four layers (:81-129):
1. a ticker lookup, folding `hedge -> alternatives` at :99;
2. a name-alias lookup (`name_aliases`, `asset_name_raw`), with the same fold at :108;
3. name-pattern GUESSES (`_RE_ALT`, `_RE_CASH`, `_RE_FI`);
4. a ticker-shape GUESS (any 1-5 letter ticker -> `equity`).
`get_sub_asset_class` (:131) and `resolve_ticker` (:145) read the same maps.

**Build (LOCAL build + record: no upload, no deploy):**
1. The library reads `etf-classifications` (344 rows) through the ONE client,
   `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`. Import it from its home, extending the import
   path the way the BD scripts already reach shared code; do not copy it. Serve `asset_class` and `sub_asset_class`
   exactly as the row holds them: no fold, so hedge stays hedge.
2. Remove layers 2-4. The canonical table has no name aliases. A holding the table does not know (by ticker) returns
   the library's unknown value, and its readers show it as unclassified, by name, never a guess. Keep the BD
   synthetic-cash override (`CASH_USD`) as it is: it is a cash rule, not a class copy. Keep the public API
   (`instance`, `classify`, `get_sub_asset_class`, `resolve_ticker`) so the readers keep working; `resolve_ticker`
   may return None where it relied on aliases.
3. The library never writes any table and never opens `bd-securities`.
4. **Tests** in `data/black_diamond/scripts/gold/tests/test_etf_classifier_canonical.py`, on a stubbed client:
   - GLD -> commodities/Metals, PHYS -> commodities/Metals (as the table will hold it), VXX -> structured/Hedge;
   - an unknown ticker -> unknown, not equity;
   - CASH_USD unchanged;
   - constructing the library opens no `bd-securities` resource.
5. **Census.** Classify the BD chain's LATEST real holdings (`opal-data-bd`, gold/holdings_lots, the day E_18 reads),
   BEFORE (the current library at CLOUD) and AFTER (yours). Write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_RESOLUTION_CENSUS_20260929.json` as
   `{"as_of", "principal": <the IAM role that runs the BD gold/silver scripts in production, read from the deployed
   runner or its instance profile>, "holdings", "before_layers": {layer: count}, "after_layers": {...}, "moved",
   "moves": [{"ticker", "name", "before": {"asset_class", "sub_asset"}, "after": {...}}], "unclassified",
   "bd_securities_reads_after": 0, "guessed_after": 0, "readers": [path:line, ...]}`.
   The readers include at least `silver/build_bd_assets_dim.py`, `gold/C_06.client_mix_timeseries.py`,
   `gold/D_03.composition_artifacts.py`, `gold/D_04.client_portal_summary.py` and
   `gold/E_25.aua_decomposition_audit.py`. The table today covers few BD tickers, so `unclassified` will be large
   until SC-k-1's backfill writes. That is expected: report it, never mask it.

### ACCEPTANCE

<criterion id="SC1-t1-AC1" cell_refs="SC-t-1"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_etf_classifier_canonical.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC1-t1-AC1` -- classes from the canonical table with no fold and no guess, and no bd-securities access.

<criterion id="SC1-t1-AC2" cell_refs="SC-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_CHECKS/r1_bd_resolution_census.py</invocation><expect>BD-CENSUS</expect></criterion>
`SC1-t1-AC2` -- the BD holdings before and after on real data: every move listed, zero bd-securities reads, zero guesses,
and the readers named.

<expected_criteria>SC1-t1-AC1,SC1-t1-AC2</expected_criteria>

Dry-run at the base 2026-09-29 22:0xZ: AC1 "no tests ran", AC2 NOT-CENSUSED (census absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** Reads `opal-data-bd` and both tables; no write, no upload, no deploy.
- **Readers are read-only here.** The assets dimension, composition and portal summary move in the next orders of your
  queue (SC-t-2, SC-t-3).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W3-S<k>`), and do not weaken the test to pass.

<paths>
data/black_diamond/scripts/gold/lib/etf_classifier.py
data/black_diamond/scripts/gold/tests/test_etf_classifier_canonical.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_RESOLUTION_CENSUS_20260929.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP.md</decomp_doc> (round 1), cell `SC-t-1`.
<owned_cells>SC-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC1-t1-AC1, SC1-t1-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~3/MDPF_SECCLASS.TO-SC-t1.bd-classifier-canonical.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC1-t1-AC1,SC1-t1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the library's new read path, the layers removed, the census (holdings, before/after by layer, moved,
unclassified, GLD/PHYS/VXX), the principal, the readers, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the BD gold/silver schedule is unchanged.
comp-iam: RUN -- the production principal of the BD scripts and its etf-classifications read right are unmeasured at the cut; the census names the principal, SC-t-3's half drafts the grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; decomposition findings inlined (four layers, fold lines, readers).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 section 2 hop 1 (S03); CTO 103040.
