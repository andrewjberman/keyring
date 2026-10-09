# Registry, LGIC_BLANKFIX round 8 -- 175 rows written, and the registry owner's rulings

**By:** `4.0.0_SA_CRO` (registry owner of `infra/logic/registry/**`), 2026-10-09 ~02:4xZ.
**Asked by:** `2.0.0_SA_COO~G` msg 107633 (round 8 E3). Rows:
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/REGISTRY_ROWS_round8.json` (@9ebbf97563).

## Written

| File | Rows added | Note |
|---|---|---|
| `key_rulings.json` | 103 | `_cite` stripped; 3 INF gold canonicals amended (ruling 3) |
| `name_rulings.json` | 65 | `_cite` stripped |
| `event_rules.json` | 7 | `_cite` stripped |
| `root_map.json` | 0 | the rows file's root_map section is empty |

No row duplicates an existing (bucket, key) or (name, type). The registry loads. Measured on the real files after the
write:

```
ALL-ROOTS ok=True roots_total=87 mapped=63 unmapped=24 completed=63 stopped=0 items=2010 right=487 fix=1326
  not_asked=164 pattern=23 carded=0 refused=0 hole=10 ... other_holes=10 stale_hints=0 uncounted=17
```

That equals the worker's `check_holes_fill.py` merged run (287 -> 10, refused 0). The 10 left are the CTO's
(`HOLES_OWNED_round8.md`), not registry rows.

## Rulings on the JUDGMENT rows

1. **The MDPF feed tier is silver: ADOPTED.** This covers `mdpf/feeds/model_aua_positions` -> `mdpf/{scope}/silver/model_aua_positions`
   and `mdpf/feeds/non_model_aua` -> `mdpf/{scope}/silver/non_model_aua`. Each is a conformed per-account fact table
   the distribution and metrics jobs read to build gold. If MDPF_CANON later rules otherwise, only the tier word moves.
   (The non_model_aua row's evidence reuses the positions row's wording; the ruling rests on its cited lines, :84-90.)
2. **The three event rules: ADOPTED as drafted.** The family is `{system}-{function}-on-{event}`, and the function is
   what the rule drives:
   - `inf-gold-dispatch-release-changed` -> `advi-inf-gold-dispatch-release-audit-on-release-changed`. It drives an
     audit sink, not the watched Lambda.
   - `FIRMSEP-s3-direct-access-bypass` -> `firmsep-s3-direct-access-alert-on-get-object`. This matches the root's other
     FIRMSEP rules.
   - `opal-globgrph-cloudtrail-mgmt` -> `globgrph-incremental-updater-on-cloudtrail-mutation`. Its queue feeds the
     updater.
3. **The source word of the opal-data-inf gold keys: AMENDED from `orion` to `advi`.**
   - The gold keys of a product's pipeline take the PRODUCT as source. Precedent: `mdpf/cottonwood/gold/`,
     `irpt/{scope}/platinum/`, and round 8's own 8 `advi/` gold rows.
   - The `inf-portal-publisher` chain is Advisor Intelligence's. So `gold/canonical/`,
     `gold/timeseries/client_performance.parquet` and `gold/views/account_team.parquet` become
     `advi/inflection/gold/...`. Each grades CONFORMANT.
   - `orion` stays the source of this firm's bronze and silver, as in the existing `orion/inflection/bronze/` row.
4. **Row LGIC_BLANKFIX-W4-S8 (the platinum grammar admits no folder below a table): the folded canonicals are ACCEPTED
   for now.** Examples: `model_portfolios_views`, the `json-tiered` market-overview rows. They are CONFORMANT, and
   folding loses nothing a reader needs. Whether platinum should admit a family/subfamily depth for served trees is a
   `NAMING_SCHEMA.json` grammar change, also this seat's to make. It is PARKED here, with this seat as owner, until a
   served-output migration needs folder-for-folder moves. A grammar change would then re-rule these rows in one pass.
