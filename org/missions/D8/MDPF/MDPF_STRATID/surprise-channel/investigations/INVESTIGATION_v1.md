# MDPF_STRATID -- surprise channel, INVESTIGATION v1 (round 1)

Append-only. Worker rows `MDPF_STRATID-W<n>-S<k>`; seat rows `MDPF_STRATID-S<k>`.

```json
[
  {
    "id": "MDPF_STRATID-D1-W1-S1",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~1",
    "surfaced_at": "2026-10-08T21:12:00Z",
    "one_line": "ST-t-1 build step 2 (default None -> every slot None) cannot hold beside AC2: the existing test asserts an exact dict for by_model['pfde'], so an unconditional overlap_model_value key fails it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/assets/scripts/gold/tests/test_cottonwood_custom_and_sma.py@e20899bce7 test_opal_sma_sleeves_are_sma_cohorts_outside_model_aua: `assert bm[\"pfde\"] == {\"display_name\": \"PFDE\", \"cohort_class\": \"sma\", \"model_value\": [9.0, 10.0], \"account_count\": [1, 1]}` -- dict equality over exactly four keys; that file is outside this order's <paths>, so it cannot be edited to admit a fifth",
        "build_slice(dates, gold) with no measurement argument therefore OMITS overlap_model_value; build_slice(..., sma_overlap_by_date=<dict>) writes it on every cohort_class 'sma' entry, None where unmeasured; build_composed always passes the dict, so the SERVED artifact carries the key on every sma entry"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Build step 2: build_slice writes overlap_model_value on every cohort_class 'sma' entry, default None -> every slot None, so existing callers and tests keep working. AC2: test_cottonwood_custom_and_sma.py still passes.",
    "world_is": "Writing the key on the default path fails that test's exact-dict assertion (the key set is part of what it asserts). The key is written on every sma entry whenever the measurement argument is supplied, which is the production path; the default path emits no key. A reader of an artifact built without the argument sees an absent key, not a list of None."
  },
  {
    "id": "MDPF_STRATID-D1-W1-S2",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~1",
    "surfaced_at": "2026-10-08T21:12:00Z",
    "one_line": "compose_cottonwood_leg copies each by_model entry whole (dict(entry)) and re-aligns only model_value and account_count to the composed axis, so a new per-date key would be left on the pre-backfill axis; re-aligned it in the same file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/assets/scripts/gold/build_cottonwood_mdpf_slice.py compose_cottonwood_leg: `e = dict(entry)` then `e[\"model_value\"], e[\"account_count\"] = mv, cnt`; the composed `dates` axis is the union of the daily dates and the backfill splice, so any other per-date list keeps the daily axis length",
        "the fix is two lines in the same file (inside <paths>): overlap_model_value is rebuilt over the composed axis, None on a backfilled date; nothing is touched when the key is absent, so every existing compose input is byte-identical"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Build step 2 names only build_slice and the reader wiring; the field is 'a list aligned to dates'.",
    "world_is": "The served artifact is the COMPOSED leg, whose dates differ from build_slice's dates when backfill splices. Without the re-alignment the served overlap_model_value would not be aligned to the served dates. No test of compose with a measured key existed; the four named tests do not cover it."
  },
  {
    "id": "MDPF_STRATID-D1-W1-S3",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~1",
    "surfaced_at": "2026-10-08T21:12:00Z",
    "one_line": "Neighbouring tests were red at the base before this change: test_cottonwood_pair_identity_cents.py (6 failures, KeyError 'custom' at build_cottonwood_mdpf_pair.py:502) and test_cottonwood_aua.py::test_live_cottonwood_derives_and_is_PARTIAL_today; neither imports the slice file edited here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "python -m pytest data/assets/scripts/gold/tests/test_cottonwood_pair_identity_cents.py -> 6 failed, KeyError: 'custom' at data/assets/scripts/gold/build_cottonwood_mdpf_pair.py:502 (u[\"custom\"][\"dollars\"]); that test imports build_cottonwood_mdpf_pair only, and this order edits build_cottonwood_mdpf_slice.py only",
        "test_cottonwood_aua.py::test_live_cottonwood_derives_and_is_PARTIAL_today fails on live data (cot cash zero-row-frozen); a live-state test, not a slice test. INFERRED because the base was not re-run: git stash is barred in the shared tree and no second checkout was made"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AC2 names only test_cottonwood_custom_and_sma.py as the regression guard; no other test is expected to be affected.",
    "world_is": "Two other cottonwood test files fail in this tree. Neither is in this order's paths and neither was fixed or investigated further."
  },
  {
    "id": "MDPF_STRATID-D1-W2-S1",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~2",
    "surfaced_at": "2026-10-08T21:14:12Z",
    "one_line": "The ST-t-3 contract puts `sma_additive_withheld` on arts['global'] only, but assert_keyset_identity requires an identical key set on all four scopes with no ruled extra for it; built so every other scope also gains `sma_additive_withheld` = [].",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/gold/mdpf_gold_consolidator.py assert_keyset_identity (R2_RULED_EXTRAS has no entry for aggregate-aua-timeseries sma_additive_withheld): a first build with the key on Global only failed test_cottonwood_and_49financial_views_unchanged with the key-set mismatch (2026-10-08, worktree wk-MDPF_STRATID-2)",
        "build_all calls assert_keyset_identity(shaped_ts, 'aggregate-aua-timeseries') whenever all four scopes built, so Global-only would have stopped the whole Gold run"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Output on arts['global']: sma_additive_aua, sma_additive_withheld, by_model[m]; every other scope gains sma_additive_aua all-None.",
    "world_is": "The key-set identity has no modulo clause, so a Global-only list key fails the L-1 gate. Every other scope now carries sma_additive_withheld = [] (additive to the contract; Global's content is as specified). The consumer of the contract (the drain's writer census, and any reader keyed on exact scope key sets) should read this."
  },
  {
    "id": "MDPF_STRATID-D1-W2-S2",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~2",
    "surfaced_at": "2026-10-08T21:14:12Z",
    "one_line": "The Global aum-metrics `sma_additive` component carries as_of = the frontier date and carried = False even on a date where the sleeve value is the last measured Cottonwood value carried forward, because Global's doc holds no per-date source-date channel for the sleeve.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py compose_current: the sma_additive component reads only agg['sma_additive_aua'][gi]; the contract's output keys carry no source-date list, unlike the Tax component's tax_coverage[...]['last_complete_date']",
        "mdpf_gold_consolidator.apply_sma_sleeve_overlay carries Cottonwood's last measured value past its last date (same rule as the Tax fold); the basis string names the carry but the boolean is not set"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The sma_additive_aua series is counted at the frontier as its own labelled component beside taxsma, so the Global total equals the fold's opal_aggregate_aua.",
    "world_is": "The total reconciles to the cent; the component's as_of/carried labels are not vintage-exact on a carried date. A per-date source-date channel (round-2 enrichment) would let the label match the Tax component's."
  },
  {
    "id": "MDPF_STRATID-D1-S1",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-09T13:50:00Z",
    "one_line": "Each MDPF run restates the per-firm aggregate-aua timeseries on the PRIOR frontier date: Cottonwood account_count_total goes from a measured count to None (count_basis measured -> absent), Inflection account counts and 49financial model_aua are restated, and tax_coverage.business_active_accounts goes to None. For the per-firm producer's owner.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_STRATID/deliverables/2.0.0_SA_COO~S1/L4_READ_20261009.md: 10-07->10-08 transition (post-D2) moves on 2026-10-07 only -- cottonwood 6 (account_count_total 384 -> None), inflection 8 (account_count_total 548 -> 578), 49financial 8 (model_aua 1,477,814,415.54 -> 1,477,815,850.93)",
        "the pre-D2 control 10-06->10-07 (portal/gold/mdpf/<firm>/aggregate-aua-timeseries/2026-10-06.json vs the pinned 2026-10-07 versions) shows the same key families on 2026-10-06: cottonwood account_count_total 382 -> None, inflection 548 -> 577; 0 moves before the prior frontier date in either transition",
        "CTO ruling org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_STRATID_L4_PERFIRM_PRIOR_FRONTIER_RESTATEMENT_20261009.md (msg 2501) admitted it as baseline restatement and asked for this row"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A served per-date figure for a date already published does not change on the next run unless a source restatement is recorded (point-in-time; and a measured count is not replaced by None).",
    "world_is": "The prior frontier date is rewritten on every run: Cottonwood's measured account count for that date becomes None/absent once the next date is published, and counts/model values elsewhere are restated, with no restatement record. Not caused by MDPF_STRATID's fold (present before D2)."
  },
  {
    "id": "MDPF_STRATID-D1-W6-S1",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~6",
    "surfaced_at": "2026-10-09T05:00:18Z",
    "one_line": "On Cottonwood's 2026-10-08 Rebalancer names the unidentified list holds 38 of 362 names, because opal_sma_member_of knows only the four ETF SMAs, so every Opal-named model and sleeve (Opal Satellite 50, Opal Short-Term, ...) lists NO_MEMBER beside the real unknowns.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~6/UNIDENTIFIED_STRATEGY_CANDIDATES.md: RESULT LISTED 38; Opal_Muni_Income 64,119,753.85 RULE_NOT_COUNTED (HOLDINGS join fact_model_assignment.external_id = fact_holdings.AccountID, 1 of 1 accounts)",
        "data/assets/scripts/silver/rebalancer_schemas.py:226 opal_sma_member_of returns a member only for DIVZ/IDVZ/PFDE/PFOE name rules"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Anything that looks like an Opal strategy but matched nothing is listed with firm, name and dollars (FWD-7); the order's names are roster.model_name, definition.model_name/sleeve_name/component_name.",
    "world_is": "The list is correct to the order's rule but mixes ordinary Opal models (not SMA strategies) and one holdings-component name (OPAL INTERNATIONAL DIVIDEND INCOME ETF) with the true unknowns; a reader wanting only SMA candidates needs a model-vs-sleeve scope on the names. ID FORM: the order names id MDPF_STRATID-W2-W6-S<k>, which proof-of-spec-check SURPRISE_ID_RE (.tools/proof-of-spec-check.py:1206) cannot parse, so the row is minted MDPF_STRATID-D1-W6-S1 (the dell1 worker form the row gate requires). Also fact_model_assignment.account_id does not join fact_holdings.AccountID (external_id does)."
  },
  {
    "id": "MDPF_STRATID-D1-W6-S2",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~6",
    "surfaced_at": "2026-10-09T05:17:30Z",
    "one_line": "ST-w-4 AC2 cannot be met with opal_models = fact_model_roster is_opal names: Opal Short-Term is not in the roster at all, so it stays listed (LISTED 12, seam W24-SEAM-BAD); roster plus fact_model_definition is_opal names gives LISTED 4 and meets the seam.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "fact_model_roster date=2026-10-08: 71 names, 29 is_opal true; Opal Short-Term, Opal Fixed Income, Opal Long-Term Aggressive, Opal Moderate Income, Opal_Moderate_Income_Tax_Efficient are absent from it (found_in definition only)",
        "fact_model_definition date=2026-10-08 model_name column carries is_opal: all 37 Opal-named model names are True, including Opal Short-Term; the union of the two tables gives 37 model names",
        "Record as the order words it (roster only): RESULT LISTED 12, EXCLUDED-AS-MODEL 26; w2_4_seam.py reports W24-SEAM-BAD Opal Model(s) still listed: ['Opal Short-Term']. Union variant (uncommitted, .scratch/union_record.md in the worker worktree): RESULT LISTED 4 (Opal_Muni_Income and Opal_Muni_Sleeve RULE_NOT_COUNTED, OPAL INTERNATIONAL DIVIDEND INCOME ETF and POLEN DIVIDEND INCOME ETF NO_MEMBER), EXCLUDED-AS-MODEL 34"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "opal_models = the model_name values of fact_model_roster (latest date=) where is_opal is true; with it the re-made record lists neither Opal Satellite 50 nor Opal Short-Term (W2-4-AC2).",
    "world_is": "Opal Short-Term is a definition-table model name with is_opal true there, absent from the roster; the roster source alone leaves it (and four other ordinary Opal Models) listed. The function and its eight tests (W2-4-AC1) are correct under either source; only the record's opal_models source decides AC2. Worker stopped per the refusal clause: record committed as the order words it, order left pending, status not flipped; the issuer decides roster-only versus roster union definition."
  },
  {
    "id": "MDPF_STRATID-D1-W6-S3",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~6",
    "surfaced_at": "2026-10-09T05:21:00Z",
    "one_line": "The worktree copy of MDPF_STRATID_DECOMP_W2.md lacks cell ST-w-4, so proof-of-spec-check reports W2-4-AC1 and W2-4-AC2 cell_refs as citing a cell that does not exist.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "proof-of-spec-check rc=1: VIOLATION alignment: cell_ref 'ST-w-4' does NOT exist in org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP_W2.md (worker worktree, branch wk-MDPF_STRATID-w2-6); the amended order came from the shared tree at issuer commit 75d44d9e82"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The amended order's cell_refs ST-w-4 resolve in decomp_doc MDPF_STRATID_DECOMP_W2.md (amendments A1, A4).",
    "world_is": "The decomp file is outside the worker's grant (order file, deliverables folder, source and test files, investigation file), and the worker branch predates the amendment commit, so the cell is absent in the worktree; the drain merge brings the amended decomp. The instance is otherwise valid apart from the W2-4-AC2 FAIL row."
  },
  {
    "id": "MDPF_STRATID-D1-W6-S4",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~6",
    "surfaced_at": "2026-10-09T05:40:00Z",
    "one_line": "D1-W6-S2 resolved: under ruling A6 the opal_models union gives RESULT LISTED 4 and EXCLUDED-AS-MODEL 34, and W2-4-AC2 passes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ruling A6 @d6d6bed0f0; record RESULT: LISTED 4; w2_4_seam.py prints W24-SEAM-OK rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Ruling A6: opal_models = union of is_opal model_name values in fact_model_roster and fact_model_definition (latest date=).",
    "world_is": "With the union, Opal Short-Term and the other four definition-only Opal Models are excluded as models; Opal_Muni_Income stays RULE_NOT_COUNTED. Row S3 is also cured: the amended decomp is copied onto the branch."
  },
  {
    "id": "MDPF_STRATID-D1-W5-S1",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~5",
    "surfaced_at": "2026-10-09T05:03:30Z",
    "one_line": "rebalancer_schemas.py now imports its sibling opal_strategy_matcher.py, so every package or S3 copy that ships rebalancer_schemas.py without the new file raises ImportError at import.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~S1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/assets/scripts/silver/rebalancer_schemas.py: 'from opal_strategy_matcher import StrategyMatcher' (flat sibling import, same pattern as rebalancer_conversion.py:40-43)",
        "data/assets/scripts/silver/mirror_conversion.py:695-700 names rebalancer_conversion.py AND rebalancer_schemas.py as vendored FLAT into opal-assets-silver-blackdiamond/BUILD_MANIFEST.json; gold scripts import it flat (build_dim_model_portfolio.py:81)",
        "No deploy was done by this worker (GUARD 1); armed only at the deploy of any consumer."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Delegation keeps the signature of opal_sma_member_of and the five callers unchanged.",
    "world_is": "The callers are unchanged, but the module they import gained a file dependency. At deploy, opal_strategy_matcher.py must be added beside rebalancer_schemas.py in the silver-blackdiamond BUILD_MANIFEST and in whatever copies the gold scripts (and the vendored lambda copy infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/rebalancer_schemas.py, which has no name rules today), or the import fails."
  },
  {
    "id": "MDPF_STRATID-D1-W5-S2",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~5",
    "surfaced_at": "2026-10-09T05:03:40Z",
    "one_line": "The repo etf_universe.json at the base commit carries only the tickers key; the full_names and sma_name_rules keys the matcher reads are in a sibling worker's uncommitted worktree, so AC2 was run against a local copy of that file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/etfs/config/etf_universe.json at 7575b70c45: keys schema_version, tickers, description, owner, last_updated, deployed_to",
        "C:/dev/wk-stratid-4 (branch wk-MDPF_STRATID-w2-4) working tree: the same file with full_names and sma_name_rules, uncommitted at the read",
        "AC2 (w2_2_seam.py) printed: DENOMINATOR 362 distinct names, same 361, gained 1 (POLEN DIVIDEND INCOME ETF -> divz, a full-name hit), changed 0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AC2 builds the matcher from infra/aws/etfs/config/etf_universe.json in the worker's worktree, with the contract's keys.",
    "world_is": "The file was copied into this worktree and left uncommitted (not in the grant). The AC2 result holds for the sibling worker's content as read at 2026-10-09T05:0xZ; on a base without the keys the matcher reads only the tickers and the seam still passes, but the gained full-name hit would not appear."
  },
  {
    "id": "MDPF_STRATID-D1-W5-S3",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_STRATID~5",
    "surfaced_at": "2026-10-09T05:23:00Z",
    "one_line": "The branch copy of MDPF_STRATID_DECOMP_W2.md lacks cell ST-w-5 (amendment A5), so proof-of-spec-check on the branch reports INVALID on the W2-5-AC1 cell_ref until the shared decomp merges.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "proof-of-spec-check on the branch instance: rc=1, 'cell_ref ST-w-5 does NOT exist in ...DECOMP_W2.md'",
        "same instance with the shared-tree decomp copied in temporarily (not committed, restored): VALID rc=0; the shared copy is 34 lines longer"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The worker validates its instance on its branch before flipping the order complete.",
    "world_is": "The decomposition file is outside the worker's grant and the branch predates amendment A5; validity holds only once the shared decomp is on the branch (the drain)."
  },
  {
    "id": "MDPF_STRATID-D1-S2",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-09T13:52:00Z",
    "one_line": "DISARM of MDPF_STRATID-D1-W5-S1 by its disarm owner: ST-w-5 landed with ST-w-2 in drain merge 4bb33bbed6, so every one of the 6 carriers that ships rebalancer_schemas.py also ships opal_strategy_matcher.py; no package built or deployed between the two.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_5_ship.py on the shared tree at 4bb33bbed6: W25-SHIP-OK 6 of 6 carriers",
        "decomposition amendment A5: the ~5 branch never merges without ST-w-5; it merged as one branch carrying both cells",
        "mdpf-gold-lambda's deployed package is still the pin-148f715f8c build (ledger mdpf-stratid-r1-global-pfde-fold L3); no rebuild since"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row D1-W5-S1: a carrier that ships rebalancer_schemas.py without opal_strategy_matcher.py raises ImportError at deploy.",
    "world_is": "After 4bb33bbed6 no carrier ships one without the other. The hazard named by D1-W5-S1 is disarmed; its disposition is the CVO's."
  },
  {
    "id": "MDPF_STRATID-D1-S3",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
    "surfaced_at": "2026-10-09T14:12:32Z",
    "one_line": "TO-APPLY-W2-a's stated rollback does not exist: step 2 says 'Record the prior object VersionId first (rollback = restore it)', but s3://opal-data-etfs is NOT a versioned bucket, so head-object returns VersionId None and an overwrite destroys the prior bytes irrecoverably. A substitute rollback was secured before the write; the bucket-level gap outlives this order.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "head-object s3://opal-data-etfs/config/etf_universe.json before any write: VersionId None, ContentLength 564, LastModified 2026-06-23T15:54:47+00:00, ETag 8f8546ce6b6fec2c42948a07c74365ff.",
        "get-bucket-versioning --bucket opal-data-etfs returns EMPTY -- no Status field at all, which is how S3 reports versioning never enabled, as distinct from Suspended.",
        "POSITIVE CONTROL, so the empty read is the world and not the instrument: the same call against opal-313476888478-terraform-state returns {\"Status\": \"Enabled\"}.",
        "SUBSTITUTE ROLLBACK SECURED BEFORE THE WRITE, which is why this row is INERT rather than ARMED: the prior 564 bytes are downloaded and committed at org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.7.0_AE_CloudOps~DELL1/etf_universe_PRIOR_s3_object_20261009.json, sha256 338bc12081261a7942d9ba9f364f0f7738573b97063c20d1463c4de9c2e39539. Restoring it is a single put-object executable by anyone from the repo rather than from this session's scratch space.",
        "SERVED DELTA IS ZERO ON THE LOADERS' PLANE, measured not assumed: the loaders' rule (cfg.get('tickers') or cfg.get('etfs') or cfg) over the CURRENT S3 bytes ALREADY yields exactly ['DIVZ','IDVZ','PFDE','PFOE']. The new file adds only full_names and sma_name_rules, which the file's own description states _load_universe does not read. No producer's universe changes."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-APPLY-W2-a step 2: 'Record the prior object VersionId first (rollback = restore it).' AC2 requires 'the prior VersionId is recorded'.",
    "world_is": "There is no VersionId to record and none to restore: the bucket has never had versioning enabled. The criterion as written is unsatisfiable on this bucket, and the honest reading is that 'record the prior object' is met by preserving its BYTES, which is what was done. THE STANDING GAP: every S3 write to opal-data-etfs -- a bucket three ETFS producers read config from -- has no version-history rollback, so any overwrite is irrecoverable unless the writer preserves the prior bytes by hand first. Owner of the choice: whoever owns opal-data-etfs (the order names 0.4.0_DS_ClientPlatform as the config's owner). Two options, either acceptable: enable versioning on the bucket, or make 'preserve the prior bytes into the writer's deliverables' an explicit step in any order that overwrites a key there.",
    "notes": "Reported, not worked around, and the write proceeded because a sound rollback was secured first and the served delta on the loaders' plane is zero. ID NOTE: this seat first appended as D1-S1 after reading an id census truncated by `tail -12`, which hid the existing bare D1-S1 and D1-S2; the gate refused it as a duplicate and as an in-place mutation, correctly. Re-read with a printed denominator (14 distinct ids at HEAD, max bare D1-S index 2) and re-filed as D1-S3. A page is not an answer."
  },
  {
    "id": "MDPF_STRATID-D1-S4",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
    "surfaced_at": "2026-10-09T15:03:10Z",
    "one_line": "For about seven minutes the DEPLOYED code path was broken: rebalancer_schemas.py went to S3 at 14:51:14Z importing opal_strategy_matcher, which was 404 -- the two silver files shipped in the REVERSE of the order's required sequence, because the push gate carried one and skipped the other as a first-mint. Disarmed at 14:58:45Z by a version restore, executed by 0.0.0_AB_MSTR~DELL1 on the CTO's ruling, and verified by content here.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE BREAK, measured 14:5xZ: head-object code/scripts/silver/opal_strategy_matcher.py -> 404 Not Found, against a POSITIVE CONTROL on the sibling key returning 15970 B / 14:51:14Z / VersionId I9x_OdzKuGDLTQNbzgKQ7.FhaQGE18pa. list-objects-v2 on the prefix returned 2 members (single page) with the matcher not among them. So the 404 was absence, not a failed read.",
        "WHY IT BREAKS: data/assets/scripts/silver/rebalancer_schemas.py:42 'import opal_strategy_matcher' and :43 'from opal_strategy_matcher import StrategyMatcher' are unconditional module-level imports, so any execution of the deployed module fails.",
        "THE ORDER PREDICTED EXACTLY THIS and is why it fixes the sequence: 'rebalancer_schemas.py imports opal_strategy_matcher, so the reverse order would break the runner's import until the second upload.'",
        "THIS SEAT DEPLOYED NOTHING. safe-deploy on the matcher was refused twice over: '[seat-gates] STOP: 1 hit(s) in OPEN-DEPLOY -- open deploy mdpf-stratid-w2-wiring-silver (author 2.0.0_SA_COO~S1, status OPEN, opened 2026-10-09T14:44:28Z) names a carried file', and 'SKIP-NOT-MEMBER ... A NEW shared-home script first-mints explicitly, never via the push gate'. The issuer's own open ledger entry blocked the act its own order required.",
        "RC WAS NOT THE ORACLE: safe-deploy exited rc=0 printing 'OK: safe-deploy gate PASS -- 0 file(s) deployed; 1 SKIPPED (first-mint, 404). NOTHING WAS DEPLOYED' and 'This line is NOT evidence of a deploy ... Measure the artifact, not this sentence.' The artifact was re-measured after the run: still 404. Output committed at deliverables/w2b_safe_deploy_refusal_20261009.out.",
        "THE DISARM WAS NOT THIS SEAT'S ACT. AMENDMENT 1 @362882be61 ordered this seat to run the restore as STEP 0; msg 2606 then relayed 1.0.0_SA_CTO~DELL1 msg 2601 naming 0.0.0_AB_MSTR~DELL1 to execute it instead, with 'skip STEP 0 unless you already ran it'. This seat had NOT run it, and the artifact proves that independently of memory: the restore timestamp is 14:58:45Z, before msg 2606 arrived at 14:59:21Z and after this seat's last S3 call on that key was a read.",
        "VERIFIED BY CONTENT, not taken on report: the new latest version xskFuVE3IWqW5_2MxWfDbA7em55dPpHW (14493 B, 14:58:45Z) has sha256 af5d894cc7a17de1a72d166f13bd5728ad9a213e1467899af75212c929c03606, IDENTICAL by cmp to version uKomD3MoIqKKqrpnZOJ4cjdBzi5Dtnnk's bytes; and the restored body carries ZERO references to opal_strategy_matcher, which is what makes it consistent with that key still being 404.",
        "THE PREFIX IS SELF-CONSISTENT NOW: build_fact_taxsma_report.py (30788 B, 2026-08-20) and rebalancer_schemas.py (14493 B, 14:58:45Z). AC1 had passed before any upload attempt: 'W25-SHIP-OK 6 of 6 carriers'.",
        "ROLLBACK EXISTED HERE because opal-data-mdpf IS versioned (get-bucket-versioning Status Enabled) and the key had 3 versions. Contrast row MDPF_STRATID-D1-S3, where opal-data-etfs has no versioning at all and the prior bytes had to be committed into the repo by hand before writing."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-APPLY-W2-b: deploy the matcher FIRST, then the schemas, 'one file per invocation', the second 'only after 1 verifies'; and on a refusal 'stop before any upload and report the refusal line; do not use --allow-stale and do not hand-copy with aws s3 cp'.",
    "world_is": "The deployed state is consistent again and the immediate hazard is gone. WHAT IS NOT FIXED: the matcher is still 404, so the forward wiring has not shipped, and the structural cause stands -- a push gate that carries one file of an import-coupled PAIR and skips the other as a first-mint can always leave the deployed prefix broken, whatever order a task order specifies, because the gate is not sequence-aware across a pair. The issuer says it is re-cutting the forward fix with the matcher's owning lane (Rule 13: DS owns QA-deploy of data/*/scripts/silver). Worth more than this order: any import-coupled pair shipped through that gate carries the same risk.",
    "notes": "Filed on the issuer's explicit instruction after a collision: the issuer had appended its own row under this same id, the gate refused the commit as both a duplicate and a FOREIGN-ROW (surfaced_by 2.0.0_SA_COO~S1 committed by this seat), and msg 2606 then withdrew the duplicate and said 'your row D1-S4 stands; commit it'. This seat reverted its working copy so the issuer's commit could land clean first -- the shared append-only file race CLAUDE.md 14b predicts -- and re-filed from a printed denominator. Standing is INERT rather than ARMED because the disarm landed before this row was written; the window it was live is 14:51:14Z to 14:58:45Z."
  },
  {
    "id": "MDPF_STRATID-D1-S5",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
    "surfaced_at": "2026-10-09T15:12:03Z",
    "one_line": "A deploy-ledger AUTHORSHIP HANDOVER does not clear safe-deploy's OPEN-DEPLOY seat-gate: the handover lands in the sentinel JSON's author field, which deploy_ledger.py check renders, but the gate reads the change_management ENTRY's '**Authored by:**' line, which the handover does not rewrite. The gate still named the old author and returned verdict=STOP; the act proceeded only because that limb is in WARN mode, and under ENFORCE an authorized act would have been blocked.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AMENDMENT 2 @f150585b25 states the intent in its own words: 'The ledger mdpf-stratid-w2-wiring-silver is now AUTHORED BY YOU (handed over so your seat gate does not stop on it).'",
        "THE HANDOVER DID LAND IN THE SENTINEL: .open_deploys/mdpf-stratid-w2-wiring-silver.json author reads 0.7.0_AE_CloudOps~DELL1 BOTH at HEAD and in the worktree (git show HEAD:<path> and the worktree file, both read with jq), and deploy_ledger.py check renders 'author=0.7.0_AE_CloudOps~DELL1'.",
        "THE GATE DISAGREED ANYWAY: safe-deploy printed 'safe-deploy: [seat-gates] STOP: 1 hit(s) in OPEN-DEPLOY -- first: OPEN-DEPLOY: open deploy mdpf-stratid-w2-wiring-silver (author 2.0.0_SA_COO~S1, status OPEN, opened 2026-10-09T14:44:28.884670+00:00) names a carried file' and 'open_deploy=hit verdict=STOP'.",
        "WHERE THE GATE'S STRING COMES FROM: the change_management ENTRY 20261009T1444Z_mdpf-stratid-w2-wiring-silver_deploy_completion.md still reads '**Authored by:** 2.0.0_SA_COO~S1' at line 5, with 4 occurrences of that serial in the file. The gate's string matches the ENTRY, not the sentinel field.",
        "WHY IT DID NOT STOP THE ACT: 'safe-deploy: WARN [seat-gates] would stop under ENFORCE ( crossbox-deploy:data/assets ); WARN mode proceeds.' So the authorized deploy landed on the WARN mode, not on the handover having worked.",
        "THE FIRST INVOCATION OF THE SAME GATE, before the handover, printed the identical author string -- so nothing about the gate's reading changed when the sentinel changed, which is the discriminating observation rather than a single reading."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The amendment asserts that handing the ledger's authorship to the applying seat stops the seat gate from stopping on it. deploy_ledger.py check corroborates the handover by rendering the new author.",
    "world_is": "Two carriers hold the same fact and the gate reads the one the handover does not touch. The practical consequences: (a) an authorship handover intended to clear a seat-gate silently fails to clear it; (b) deploy_ledger.py check rendering 'author=<me>' is NOT evidence the gate sees me, so no seat should cite it as one; and (c) this only stayed harmless because the crossbox-deploy limb is in WARN -- the same sequence under ENFORCE blocks an act the issuer and the CTO had both authorized. REMEDY, for the gate's owner: either have the gate read the sentinel's author field (the one deploy_ledger.py actually maintains), or have the handover rewrite the entry's 'Authored by:' header as well, so the two carriers cannot disagree. Not fixed here: the gate and the ledger renderer are both outside this order's paths.",
    "notes": "Found while executing AMENDMENT 2's acts A-C, which all passed; this row is about the instrument, not the act. Distinct from D1-S4 (the import-coupled pair shipping out of order) and D1-S3 (the unversioned opal-data-etfs bucket). Id taken from a printed denominator -- 16 ids at HEAD, max bare D1-S index 4 -- after a truncated census in this same channel earlier produced a duplicate and a foreign-row refusal."
  },
  {
    "id": "MDPF_STRATID-D1-S6",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-09T15:12:00Z",
    "one_line": "DISARM of MDPF_STRATID-D1-S4: the live silver code is consistent again -- opal_strategy_matcher.py first-minted 15:05:53Z, then rebalancer_schemas.py re-shipped 15:06:59Z, both byte-equal to ff8b8452f0; an import of both S3 copies from an empty directory resolves. The broken window was 14:51:14Z-14:58:45Z (rolled back by 0.0.0_AB_MSTR~DELL1 on 1.0.0_SA_CTO~DELL1 msg 2601).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "issuer re-read 15:1xZ: s3://opal-data-mdpf/code/scripts/silver/opal_strategy_matcher.py 4296 B 15:05:53Z and rebalancer_schemas.py 15970 B 15:06:59Z, each == git show ff8b8452f0:data/assets/scripts/silver/<file>; py_compile OK; isolated import OK, STRATEGY_CONFIG_SOURCE None before first call",
        "ledger mdpf-stratid-w2-wiring-silver L1 and L2 CLOSED (L2 by 0.7.0_AE_CloudOps~DELL1 under TO-APPLY-W2-b AMENDMENT 2 @f150585b25, msg 2634)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row D1-S4: the deployed rebalancer_schemas.py imports a module absent from S3.",
    "world_is": "Both modules are present and import; the hazard is disarmed. Whether the next scheduled silver run reads the S3 list cleanly is ledger L3."
  }
]
```
