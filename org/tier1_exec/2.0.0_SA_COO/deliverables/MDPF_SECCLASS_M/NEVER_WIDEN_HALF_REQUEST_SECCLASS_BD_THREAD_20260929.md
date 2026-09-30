# Never-widen half, MDPF_SECCLASS thread hops 1-4 (SC-t-1 through SC-t-3) -- deploying the BD
# chain's canonical-class read onto served S3 artifacts

**Author:** 0.9.0_WK_MDPF_SECCLASS~3, 2026-09-29. **For:** the issuer (2.0.0_SA_COO~M) to sign and send, same
"never widen without a named blast radius + rollback per key" discipline as the seed-fields half
(`NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_FIELDS_20260929.md`) and CLAUDE.md HARD STOPS section 5.
**Status of the act described here: NOT YET RUN.** SC-t-1..3 are LOCAL build + record cells (LOCAL/SERVED/WORLD risk
class LOCAL): no upload, no deploy. This half covers the FIRST real deploy of the rewritten BD gold-chain files
(`lib/etf_classifier.py`, `D_03.composition_artifacts.py`, `D_04.client_portal_summary.py`,
`C_06.client_mix_timeseries.py`) to `opal-data-bd/code/{gold,silver}/...` via `.tools/safe-deploy.sh`, plus the first
production RUN of those deployed scripts (the write that actually replaces the served JSON artifacts on S3).

## The act

Two ordered steps, DS lane (CLAUDE.md rule 13):

1. **Deploy (candidate diff, not yet applied):** `.tools/safe-deploy.sh` on the four changed files --
   `data/black_diamond/scripts/gold/lib/etf_classifier.py` (SC-t-1), `data/black_diamond/scripts/silver/
   build_bd_assets_dim.py` (SC-t-2), and `data/black_diamond/scripts/gold/{D_03.composition_artifacts.py,
   D_04.client_portal_summary.py, C_06.client_mix_timeseries.py}` (SC-t-3) -- S3 cp to `opal-data-bd/code/...`
   under the PIPELINE_MAP's bd-only mapping, SHA-verified post-copy. The candidate bytes are this worktree's
   committed diff at HEAD (branch `wk-MDPF_SECCLASS-3`); no other pipeline's tree is touched -- **firm tree kept**:
   `data/black_diamond/scripts/{gold,silver,bronze}/*.py` maps ONLY to `opal-data-bd`, never `opal-data-inf` or
   `opal-data-cot` (cot is a separate firm, never mirrored/synced, NFRA_DTAFLP).
2. **Run:** the next scheduled (or ad-hoc QA, per the moratorium exception) invocation of
   `build_bd_assets_dim.py`, `C_06.client_mix_timeseries.py --upload`, then `D_03.composition_artifacts.py
   --upload`, then `D_04.client_portal_summary.py` -- the pipeline order the module docstrings already name
   (`C_07 --> D_03 --> C_06` for D_03/C_06; D_04 reads D_03/C_06's output). This is the run that overwrites the
   SERVED objects listed in Blast radius below.

Evidence -- the exact class moves this act would produce on real BD data, computed from a REAL local build of all
three thread hops (LOCAL, no upload):
- `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_RESOLUTION_CENSUS_20260929.json` (SC-t-1, the
  library) -- `principal: bd-exporter-ec2-role`, 3,992 holdings, `bd_securities_reads_after: 0`, `guessed_after: 0`.
- `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_SILVER_CENSUS_20260929.json` (SC-t-2, the assets
  dimension) -- 10,937 rows, 296 `etf-classifications` (pre-backfill count; re-read below).
- `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_GOLD_CENSUS_20260929.json` (SC-t-3, this cell) --
  524,413 open lots, `class_sources: {"etf-classifications": <see file>, "unclassified": <see file>}`, one real
  client (`z08327149`, holds $1,193,572 of VXX, 1.6951% of a $70.4M book) whose page carries VXX
  `structured`/`Hedge`/`etf-classifications`.

**Every BD-held ticker whose class moves, read back after (live DynamoDB `etf-classifications`, 2026-09-30
~00:02Z, post CLOUD's release step 1 @ad921b0c47):**

| ticker | before (bd-securities / no canonical row) | after (etf-classifications, read back live) |
|---|---|---|
| GLD  | alternatives / Gold      (SC-t-1 census) | commodities / Metals   (measured: `GLD` item, `classified_by: seed`) |
| PHYS | alternatives / Gold      (SC-t-1 census; absent from etf-classifications until the release step 1 backfill row MDPF_SECCLASS-W3-S1 named) | commodities / Metals (measured: `PHYS` item, `classified_by: seed`) |
| VXX  | alternatives / Volatility (SC-t-1 census) | structured / Hedge    (measured: `VXX` item, `classified_by: seed`) |

Every other BD-held ticker's move is enumerated in full in the three census files above (3,880 tickers moved at
SC-t-1's library layer alone); this half's blast-radius reasoning below applies UNIFORMLY to all of them, not only
these three -- GLD/PHYS/VXX are named because the task order singles them out as the acceptance targets.

## Blast radius

**Served artifacts this act overwrites, and their readers:**

1. **Advisor-facing composition (`D_03.composition_artifacts.py`).**
   - `gold/views/firm_composition.json` (`FIRM_COMPOSITION`) -- served via `GET /api/scoped/partners/books/
     firm/all/composition` (opal-partners-data, pure S3 proxy).
   - `gold/advisors/{advisor_id}/composition.json` (per architect + non-architect advisor) -- served via
     `GET /api/scoped/partners/books/advisor/{id}/composition`.
   - `gold/entities/clients/{rel_id}_composition.json` -- read by `D_04.build_client_summaries` (below) and
     passed through verbatim to `platinum/clients/{rid}/composition.json`.
   - **Change:** every holding in `top_holdings`/`mix[].top_holdings` gains three new keys
     (`asset_class_canonical`, `sub_asset_class_canonical`, `class_source`); the pre-existing `asset_class`
     (equity/fixed_income/alternatives/cash/other) keeps its value for every ticker except the ones the three
     census files list as moved (e.g. VXX equity-bucket membership does not change: VXX classified as
     `alternatives` in D_03's coarse bucket both before and after, since `classify_series`'s cash/other rule is
     unaffected -- ONLY the new canonical columns and the underlying etf-classifications-sourced VALUE for a
     moved ticker like VXX/GLD/PHYS change). No key is REMOVED from any existing holding object.
2. **Client portal summary (`D_04.client_portal_summary.py`).**
   - `platinum/accounts/{acct_id}/summary.json` (`build_account_summaries`) -- its `top_items[]` per account gain
     the same three canonical keys (previously carried NO class field at all on `top_items`; this is additive).
   - `platinum/clients/{rid}/summary.json` (`build_client_summaries`) -- `concentration.items` is a pass-through
     copy of D_03's `top_holdings`, so it inherits the three new keys automatically; `mix` (the coarse-class
     dollar snapshot) is UNCHANGED in shape (still keyed by equity/fixed_income/alternatives/cash only, sourced
     from `mix_daily_summary.json`).
   - `platinum/firm/mix_summary.json` (`build_firm_mix_summary`) -- `mix` snapshot is UNCHANGED (coarse,
     dollar-based, from C_06's `mix_daily_summary.json`, itself unchanged in SHAPE -- see C_06 below);
     `concentration.items` inherits the three new keys via the same D_03 pass-through.
   - **Known gap, not widened here:** `build_advisor_positions`'s `positions[]` (platinum/advisors/{id}/
     positions.json, PRD ADVI_49EXEC.md Section 4.5's frozen wire contract) still classifies via its own
     `_classify_ticker` closure and does NOT carry the three canonical keys -- it is a fourth classify site in
     this file the task order's cell text did not name (only `_classify` near :1235 was named). Row
     MDPF_SECCLASS-W3-S3 files this as an observation for the round.
3. **Client mix timeseries (`C_06.client_mix_timeseries.py`).**
   - `gold/client_timeseries/{relationship_id}.json` -- `concentration[].holdings[]` gain the three canonical
     keys; `asset_class` per holding CHANGES VALUE for any ticker that was previously mis-classified to `equity`
     by the removed guess (row MDPF_SECCLASS-W3-S1's sibling defect) -- this is a genuine, intended value change,
     not additive-only. The `mix` dict (equity/fixed_income/alternatives percentages) is UNCHANGED IN SHAPE; its
     VALUES can shift for a relationship that held a previously-mis-guessed-equity position, since that position
     now buckets to `cash`/`other` (neither of which `MIX_ASSET_CLASSES` reports) instead of `equity` -- the
     `pct_sum` validation (tolerance 0.001) is unaffected (it sums ALL groups, not just the three reported ones).
   - `gold/views/mix_daily_summary.json` (`MIX_DAILY_SUMMARY`, read by `D_04.build_firm_mix_summary`) -- daily
     dollar totals by class; can shift for the same reason (a position leaving the `equity` guess bucket moves its
     dollars out of the firm's daily `equity` total). This is the ONE case where a coarse, already-served NUMBER
     changes as a result of this act (not just gains new keys) -- named explicitly because HARD STOPS section 5
     requires it named, not predicted from the input's shape: the real magnitude is in the gold census's
     `class_sources` (this cell's local build measured 46,446 rows -- see `unclassified` in the census file --
     that the removed guess would previously have folded into `equity`; C_06's own local run in this cell's census
     confirms the identical count, since C_06's `classify_series` was fixed to the same no-guess rule).

**IAM read `etf-classifications` needs (DESIRED, NOT APPLIED):** SC-t-1's own census names the principal
(`bd-exporter-ec2-role`) that runs these gold scripts. That principal needs `dynamodb:GetItem` on
`arn:aws:dynamodb:us-east-1:*:table/etf-classifications` for the shared client
(`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`) to resolve at runtime; this half does NOT
apply that policy -- it is named here as a precondition the deploy step depends on, to be granted (or confirmed
already granted) before step 2 (Run) executes, never assumed from step 1 (Deploy) succeeding.

**Release order:** this deploy is MDPF_SECCLASS release step 2, run AFTER SC-k-1's scheduled backfill write (release
step 1, already CLOSED @ad921b0c47) lands its table rows -- so that a holding the backfill resolves (GLD, PHYS,
VXX, and every other ticker the three census files list) is never shown unclassified in the served artifacts in
between. Deploying the gold-chain readers BEFORE the backfill would have made GLD/PHYS/VXX show as unclassified in
production for the gap between deploys; deploying AFTER means every served artifact's first read already sees the
backfilled rows.

## Rollback per key

S3 IS versioned for `opal-data-bd` (unlike the seed half's DynamoDB target): rollback restores the PRIOR object
version at each key, not an attribute-level undo.

- **Code rollback:** `.tools/safe-deploy.sh` on the PRE-cell commit (the parent of this worktree's first SC-t-1
  commit) for the four files, re-verified by SHA -- returns every gold/silver script to its pre-MDPF_SECCLASS
  behavior (old two-layer classifier, old equity-guess fallback in C_06, no canonical columns anywhere).
- **Data rollback, per served key:** every key named in Blast radius above (`gold/views/firm_composition.json`,
  `gold/advisors/{id}/composition.json`, `gold/entities/clients/{rid}_composition.json`,
  `platinum/accounts/{id}/summary.json`, `platinum/clients/{rid}/summary.json`, `platinum/firm/mix_summary.json`,
  `gold/client_timeseries/{rid}.json`, `gold/views/mix_daily_summary.json`) is an S3-versioned object; `aws s3api
  list-object-versions --key <key>` + `aws s3api copy-object --copy-source <bucket>/<key>?versionId=<prior>`
  restores the exact pre-deploy bytes for that one key, independent of every other key.
- **No table write:** this act reads `etf-classifications`, never writes it -- there is no DynamoDB rollback
  needed for this half (SC-k-1's own seed-fields half covers that table's rollback separately).

## COO half -- [PENDING SIGNATURE]

## CTO half -- [PENDING SIGNATURE]
