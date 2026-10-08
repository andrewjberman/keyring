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
  }
]
```
