# 4.0.0_SA_CRO — EVR employ + /mdpf-refresh skill build (15:10–16:10Z)

**archetype:** IMPLEMENT

## Arc
Andrew at this terminal: (1) pointed me at 0.2.0_DS's Eclipse Vintage Reconstruction spec →
found + assessed (truth table §5a @3b3adaa420); (2) ruled "yes to both" (@e4251a4567 — historic
scope extended to the six dates, internal-only lifted); (3) ordered the emitter structured +
employed on inflection, then a fresh gold+platinum publish, with the refresh mechanism built as a
skill (recorded verbatim; COO ruled RP-W7 SUPERSEDED-BY-DIRECT, I proceed unheld).

## Landed (commits, chronological)
- @3b3adaa420 truth-table §5a addendum (the ratified third path + all-7-dates factor coverage).
- @e4251a4567 ANDREW-DIRECT record: "yes to both".
- (employ-order ANDREW-DIRECT record, same file family, committed pre-broadcast.)
- @80b7bf651f `data/mdpf/scripts/backfill/eclipse_vintage_reconstruction.py` (evr-1.0.0):
  D3 method + Step 3 flows; D4 gate INSIDE the emitter (bars 10/25/50bp, FAIL=rc2+no-write).
  **Calibration discovered D3's flow list incomplete**: the 136bp opal_long_term_conservative
  cell was a $202,537.69 "Internal Account Journal Out" (portfolio 1423, 2026-08-04) — vocabulary
  reset against the full 46-description census. Calibration (08-04, end-convention):
  −3.37/5.90/40.9bp. Validation (08-11, untuned): −1.17/1.17/3.99bp. Through-hole 2-day shape
  (08-06←08-04): 8.47bp weighted. **7 artifacts EMITTED** to the ratified prefix (ETags logged),
  full Condition-1 bodies, audience serve-permitted per @e4251a4567.
- orion 08-06 custody fill: `orion_0806_fact_assets_backfill.py` run — REAL parquet-sibling data
  (35,262 rows, contract-checked 58/58 cols, 0 dtype drift, additive-only, `_source_file`
  honestly names the parquet). fact_assets ETag 478ad9a3, 15:53:01Z.
- @5b00923c11 builder consume: opt-in EVR read in `load_inflection_model_history` (mislabeled
  artifact REFUSED toward the gap), `_flat_point_class` + "reconstructed" (absent >
  interpolated_estimate > reconstructed > carried > measured), per-firm meta.reconstructed block,
  in-band cohort_provenance labels, global-fold inflection slot label. Deployed to
  s3://opal-data-mdpf/code/scripts/gold/ — comp-pipescript MATCH.
- **EXERCISED**: standalone inflection build 15:58Z — 62/62 post-launch dates read, the exact 7
  EVR-reconstructed, 0 named gaps; custody 445/445; artifact labels on EXACTLY the 7 and nowhere
  else (CTO evidence (a) True).
- /mdpf-refresh skill (SKILL.md + boto3 driver, device-agnostic): status/gold/full +
  --reland[--confirm] conflict protocol. Preflight exercised: 4/4 scopes behind=1 vs target
  08-13. Fixed in-flight: expected_last_trading_day returns TODAY mid-session (its T+1-priced
  contract) — serve bar corrected to the estate's own trading_days_behind<=1.

## Rulings received
- COO 154018Z: routing (proceed unheld; RP-W7 superseded-by-direct) + the conflict-guard flag
  (dated-key delete-and-re-land = Andrew's explicit word, folding the 4-key 15:19Z episode).
- CTO 153929Z: evidence criteria (a)-(d) for the serve ruling; 160936Z: **(a)-(c) DISCHARGED**
  on their independent reads; (d) completes on tonight's fresh cycle.

## Open at turn end
- **Andrew's dated-key word** (asked at his terminal ~16:07Z): authorize delete-and-re-land of
  the conflicted dated gold keys the fresh run re-lands (incl. the 4 from 15:19Z). On the word:
  /mdpf-refresh gold → --reland --confirm on whatever the guard names → re-run → verify →
  (d) evidence to CTO → report to COO.

## Surfaced, not chased
- fact_positions 08-06 gap (same parquet-sibling fill available; MDPF does not read it).
- Recurring builder WARN: eclipse_id=31 "90/10 Opal Intermediate/Ultra Short Term" candidate-NEW-
  Opal since 07-29, folded to non_model (F5) — crosswalk decision belongs to DS/CTO.
- Publisher IAM degradation on _manifests/latest.json (pre-existing, publish unaffected).
- inf-api-eclipse BR1 staging prefix until Gate-3 (pre-existing).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-find ×6 | spec/emitter/producer/consumer localization | incl. the opt-in premise re-check (2 hits, both the emitter itself = 0 consumers) |
| comp-pipescript deployed --pipeline mdpf ×2 | pre/post deploy verify | MATCH both |
| commit-gate ×4 | every .py before commit | clean (1 ruff unused-import fixed) |
| lib/trading_calendar | all date math | incl. the mid-session frontier-semantics fix |
| live primitives | lambda/s3/ssm via boto3 + aws cli reads | every leg read before the next |
