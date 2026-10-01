# AMGT_CORPUS -- L5 decomposition v28.0 -- ROUND 28, THE FRIDAY ROUND (three worker cells in two chains; one paired served act after the sign cell)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-01 ~06:3xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-27 analysis
`ledger/ROUND_ANALYSIS.round27.md` @`99b83b495a` (msg 27551, READ-acked), s.3 ENRICHMENT LIST; PRD v0.7 Addendum B (FWD-12 amended,
FWD-20, FWD-21; ratified-text half SIGNED by `3.0.0_SA_CVO~Z` @`089a39f74c`); CONTRACT amendment 1 @`c7f9fa44fa` (CORPUS is the one
writer of `ModelTab.tsx` through the freeze, msg 27546); COO~D's input on the pack wording (msg 27552). Round 27's decomposition is
kept as `AMGT_CORPUS_DECOMP.round27.md`. Base of the cut: CLOUD `bd29533457`, portal DEV `a41cf763`.

**Deadline (Andrew, placement s.1):** cells ad-1 and ad-3 land on portal DEV before Thu 2026-10-01 18:00 ET (22:00Z).

## 0. What this round IS

| # | item (analysis s.3) | cell | slot | FWD |
|---|---|---|---|---|
| 1 | `modelSheet.ts`: the five null rows map to the fields already pulled; the Other lines leave the sheet; the sheet takes the served forecasts as 2026E-2028E columns | `CRPS-ad-1` | `~1` (worker-light) | 20, 12, 21 |
| 2 | the zero-value sign over-refusal, BA's DPS as the control | `CRPS-ad-2` | `~2` | 20 |
| 3 | `ModelTab.tsx`: ScoreTiles and Opal's rule lines out; `model.forecast_figures` passed in; one face (k-5); no presupposed pack | `CRPS-ad-3` | `~1` after ad-1 | 12, 21, 15 |
| 4 | the paired re-derive of the blocks ad-2 moves | `CRPS-ad-4` | the issuer's WORLD act after ad-2 drains; no order | 20 |

**Not cut:** FWD-22 (the scheduled re-pull of every name) waits on Andrew's standing word (PRD v0.7 B.2; placement s.5 item 2).

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-ad-1` | LOCAL | `portal/src/pages/SecurityAnalysis/modelSheet.ts` | Revenue/Sh `REVENUE_PER_SH`, FCF yield `FREE_CASH_FLOW_YIELD`, FCF margin `FREE_CASH_FLOW_MARGIN`, RoTA `RETURN_ON_TANGIBLE_ASSETS`, Earnings margin `PROF_MARGIN`; no Other-lines group; `buildModelSheet(figures, years, names, forecastFigures?)` adds `<year>E` columns from the served forecast figures (EPS `BEST_EPS`, BVPS `BEST_BPS`, DPS `BEST_DPS`, Dividend yield `BEST_DIV_YLD`, P/E `BEST_PE_RATIO`, EBITDA `BEST_EBITDA`); history cells byte-unchanged |
| `CRPS-ad-2` | LOCAL | `integrations/bloomberg/research/model_block_pull.py`, `integrations/bloomberg/research/build_unit_map.py`, the new `tests/test_zero_sample_sign_round28.py` | a figure is signed by its own value when the map's sign is UNRESOLVED only because the SAMPLED year was exactly zero (a zero figure reads ZERO); BA's DPS passes the check face; no value, unit or other sign moves. The served blocks move only at ad-4 |
| `CRPS-ad-3` | LOCAL | `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`, `__harness__/modelPattern.harness.cjs`, `__harness__/tabs.harness.cjs` | no `ScoreTiles`, no `CasesBlock` rule lines; `buildModelSheet(..., data.model?.forecast_figures)`; the ABSENT face shows a figure with its label or the empty sentence, never both; no "in the research pack" / "in this pack" where the served reason names no pack |
| `CRPS-ad-4` | WORLD | S3: the newest block of each name ad-2 moves (18 names), their dossiers | under a pair: serializing dry run over every key, predecessor-code diff, the act-start gate in its own call, each sentinel committed after every leg close |

## 1a. Re-groundings at L5 (measured at base; `deliverables/2.0.0_SA_COO~X/checks/round28/`)

- **ad-1** `sheet.cjs`: 2 of 6 arms at base (history and the no-forecast negative pass by design). `CENSUS keys 100 rows 1700 shown
  1055 absent 145 unmapped 500` -- the brief's 500 unmapped reproduced exactly. BA serves 32 forecast figures (FY1-FY3 = 2026-2028); 17
  sit on sheet rows (BA serves no BEST_PE_RATIO FY1).
- **ad-2** `ad2_check.py` (3m26s): `ad2 keys 100 refuse 364 refuse_zero_sample 354 ba_dps_shown 0 of 10 value_moves 0 unit_moves 0
  other_sign_moves 0 errors 0`. Of the 36 zero-sample series, 30 are all-zero (non-payers, 294 figures) and 6 are one-sign (60).
  The cause: `build_unit_map.classify_sign` (`:504`) returns UNRESOLVED for a zero SAMPLE, and `model_block_pull._resolved_sign`
  (`:734`) keeps a map-UNRESOLVED sign on every figure. Expected after: `refuse 10` (BBSE3's ZERO-DOMINATED capex, unit not measured).
- **ad-3** `face.cjs`: 2 of 8 arms at base (team cases kept and no state words pass by design). The k-5 pair is reproduced: "No
  figure, case or estimate is shown in its place" beside "Opal's historical-multiple reference: forward EPS (FY1) is -0.828".
- **Harnesses at base:** modelPattern 12/12, tabs 20/20, shell 10/10, errorEmpty 12/12. `modelPattern` anchors `score_tiles` = 3,
  `score_empty_state` and `year_heads`; `tabs:384` counts sheet cells against the fiscal count. ad-3 NECESSARILY breaks these, so
  both harnesses are granted to ad-3 to re-anchor onto the same facts at their floors. `exportCompare.harness.cjs` reads RED at base
  (rc 2, needs file arguments; DSGN decomp round 12: never in a bound list).

## 4. Dependency edges and chains

- **ad-1 -> ad-3:** ad-3 passes `model.forecast_figures` into the parameter ad-1 adds, and face.cjs arm 8 grades the rendered E
  columns. ad-3 is handed to slot `~1` on a worktree brought to ad-1's merged head.
- **ad-2 -> ad-4:** the paired re-derive carries ad-2's code.
- ad-1/ad-3 (portal) and ad-2 (Python) write disjoint files.

## 5. The round -- one issuance, fan-out as data

- `fanout: 2 of 2 chains, cap 3, reason: chain A is ad-1 then ad-3 on slot ~1 (ad-3 consumes ad-1's signature); chain B is ad-2 on slot ~2; ad-4 is the issuer's paired act after ad-2.`
- **Drain:** each cell re-graded with pins read by content and merged (portal branch into portal DEV with a one-line receipt per
  CLAUDE.md Portal; the outer branch into CLOUD); the ONE REAL RUN is BA's Model tab on the local DEV build (`localhost:5174`)
  looked at; ad-4 opens with its pair; the L8 packet then goes to `3.0.0_SA_CVO~Z`.
- **Judgment (L9, analysis s.3):** the CVO reads ad-3's render as a person: the Model tab reads like the analyst's SharePoint sheet.
- Surprise rows from `Z-S75`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
