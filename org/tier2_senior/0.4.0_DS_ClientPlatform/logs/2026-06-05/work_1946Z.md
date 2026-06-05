# 0.4.0_DS_ClientPlatform — work_1946Z (MDPF_COUNTS blend-split fix authored+gate-clean)

**archetype:** DIAGNOSE + IMPLEMENT

## MDPF_COUNTS blend-split — Andrew-direct URGENT

Andrew (via COO, 193409Z + 194026Z) flagged a Global COUNT bug: blend accounts showing as
SEPARATE keys in the Global by_model, and Inflection base models claimed dropped.

### Investigation findings

Pulled the live 2026-06-05 partition + served global artifact (18:37Z, post-AE b25ed02a2).

**Finding 1: Inflection base models ARE correctly included (not dropped).**
The 18:37Z served global slice shows opal_intermediate=1,757=49F(1,580)+INF(177), LTC=3,108=
3,038+70, ST=688=676+12, LTA=1,444=1,420+24, UST=178=171+7. All INF base model accounts present.
The "~449 accts dropped" claim conflates total Inflection accounts (456) with base-model drop.

**Finding 2: Blend-split is the only bug.**
`build_global_by_model()` was a single-pass accumulate-by-model_key. Blend entries
(`opal_blend_5050_int_ltc`=143, `opal_blend_5050_st_int`=23) passed through as SEPARATE keys
instead of being folded into component base model keys. The 166 blend accounts were stranded
outside the base model bars.

### Fix — two-pass `build_global_by_model()`

**`_BLEND_GLOBAL_SPLIT` constant added (above function):**
```python
_BLEND_GLOBAL_SPLIT = {
    "opal_blend_5050_int_ltc": ("opal_intermediate", "opal_long_term_conservative"),
    "opal_blend_5050_st_int":  ("opal_short_term",   "opal_intermediate"),
}
```

**Two-pass rewrite:**
- Pass 1: accumulate base model + SMA entries only (skip blend keys)
- Pass 2: fold blend account_count (FULL count to each component per Andrew ruling) +
  model_value (FULL to each component per COO interim; AUA-split pending Andrew; 1-line to 50/50)

**Gate: py_compile + ds-precommit-check + ruff — exit 0.**

### Expected Global by_model after fix (2026-06-05)

| key | count | delta |
|---|---|---|
| opal_intermediate | 1,923 | +166 |
| opal_long_term_conservative | 3,251 | +143 |
| opal_short_term | 711 | +23 |
| opal_long_term_aggressive | 1,444 | 0 |
| opal_ultra_short_term | 178 | 0 |
| opal_div_sma | 43 | 0 |
| opal_growth_sma | 50 | 0 |
| ~~opal_blend_5050_int_ltc~~ | REMOVED | — |
| ~~opal_blend_5050_st_int~~ | REMOVED | — |

Total non-SMA = 7,507 (intentional: blend accounts counted in 2 models each).

### Handoff

[COMMIT-REQUEST] sent to COO (194602Z) for AE (data/mdpf/** lane):
- commit `build_aggregate_aua_timeseries.py`
- re-run rollup (--upload)
- CF-invalidate `/api/general/mdpf/*` on EVTSA9VEHNZVH

AUA semantics flagged in commit message: Andrew ruling pending for 50/50 vs full-value per component.
Bug 2 (FE routing) handled by DE base in parallel.

## Standing / open obligations
- **MDPF_COUNTS blend-split:** COMMIT-REQUEST pending AE; post-deploy verify served global by_model
- **I3 close:** Andrew-visual on ADV panel pending (COO coordinates); RAVC2-close 237aa6dbd filed
- **I1+I2 close:** AE deploying in event-gated 11:30Z job; post-deploy served-verify pending
- **R2 close:** next-day BucketSizeBytes trend read

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| (S3 read) | served global + 2026-06-05 partition + inflection slice | Inflection base confirmed present; blend keys confirmed separate |
| ds-precommit-check + ruff + py_compile | build_aggregate_aua_timeseries.py | exit 0 |

work-cycle:0020
