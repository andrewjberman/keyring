# Never-widen half, MDPF_SECCLASS thread hops 1-4 (SC-t-1 through SC-t-4) -- ROUND 2 RE-CENSUS,
# deploying the BD chain's canonical-class read onto served S3 artifacts

**This half SUPERSEDES `NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_20260929.md`, which is left
UNEDITED.** That half's evidence was measured on 2026-09-25/29, BEFORE the scheduled backfill
landed (release step 1, `~02:2xZ`, CLOSED @ad921b0c47) and before release step 2 (CLOSED
@f13cddd058) brought the live `etf-classifications` table to 2,309 rows. At that time 3,699 of
3,992 BD holdings were unclassified at the library layer. This half re-measures against TODAY's
live table (2,309 rows, read live at build time via a full DynamoDB scan, `Select=COUNT` +
item scan cross-checked identical) and TODAY's real BD data (`gold/holdings_lots/2026-09-25.parquet`,
still the latest BD day; `silver/bd_assets_dim.parquet` and `gold/views/firm_composition.json` read
live from S3 with their version IDs, below). The evidence file is
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_THREAD_CENSUS_20260930.json`.

**Author:** 0.9.0_WK_MDPF_SECCLASS~4, 2026-09-30. **For:** the issuer (2.0.0_SA_COO~M) to sign and
send, same "never widen without a named blast radius + rollback per key" discipline as the round-1
half and CLAUDE.md HARD STOPS section 5.
**Status of the act described here: NOT YET RUN.** SC-e-3 is a LOCAL build + record cell (LOCAL/
SERVED/WORLD risk class WORLD per the round-2 decomposition, since the deploy it describes touches
served portal-facing artifacts): no upload, no deploy happened in this cell. This half covers the
FIRST real deploy of the already-committed, already-merged BD gold-chain files
(`lib/etf_classifier.py`, `build_bd_assets_dim.py`, `D_03.composition_artifacts.py`,
`D_04.client_portal_summary.py`, `C_06.client_mix_timeseries.py` -- merged @ae7aa281b0, round 1
SC-t-1..t-4) to `opal-data-bd/code/{gold,silver}/...` via `.tools/safe-deploy.sh`, plus the first
production RUN of those deployed scripts, plus the COO's one live run of FWD-1 to the page for a
real client, as the closing act.

## The act

Four ordered steps:

1. **Deploy (candidate diff, not yet applied):** `.tools/safe-deploy.sh`, DS lane (CLAUDE.md rule
   13), on the four already-committed files -- `data/black_diamond/scripts/gold/lib/etf_classifier.py`,
   `data/black_diamond/scripts/silver/build_bd_assets_dim.py`, and
   `data/black_diamond/scripts/gold/{D_03.composition_artifacts.py, D_04.client_portal_summary.py,
   C_06.client_mix_timeseries.py}` -- S3 cp to `opal-data-bd/code/...` under the PIPELINE_MAP's
   bd-only mapping, SHA-verified post-copy. **Candidate bytes:** CLOUD @ae7aa281b0 (the round-1
   drain commit) for these five files -- no other pipeline's tree is touched. **Firm tree kept:**
   `data/black_diamond/scripts/{gold,silver,bronze}/*.py` maps ONLY to `opal-data-bd`, never
   `opal-data-inf` or `opal-data-cot` (cot is a separate firm, never mirrored/synced, NFRA_DTAFLP).
2. **IAM grant (DESIRED, NOT APPLIED, precondition to step 3):** `bd-exporter-ec2-role` (the
   principal these gold/silver scripts run as -- named in round-1's SC-t-1 census, confirmed
   unchanged: `infra/aws/terraform/bd-pipeline/iam.tf` line ~341 `aws_iam_role.bd_exporter`)
   needs `dynamodb:GetItem` on `arn:aws:dynamodb:us-east-1:*:table/etf-classifications`. **Measured,
   not assumed:** reading `infra/aws/terraform/bd-pipeline/iam.tf` at HEAD today, the ONLY policy
   attached to this role (`aws_iam_role_policy.bd_exporter_s3`, plus the schwab-silver-read
   addition) grants S3 actions only -- there is NO DynamoDB statement of any kind on this role
   today. This half does NOT apply that policy; it is named as a candidate Terraform statement
   below, to be added (never a hand-typed workaround -- LGIC registry/naming gate applies) before
   step 3 runs, never assumed from step 1 succeeding.
   ```hcl
   resource "aws_iam_role_policy" "bd_exporter_etf_classifications_read" {
     name = "etf-classifications-read"
     role = aws_iam_role.bd_exporter.id
     policy = jsonencode({
       Version = "2012-10-17"
       Statement = [{
         Sid      = "EtfClassificationsGetItem"
         Effect   = "Allow"
         Action   = ["dynamodb:GetItem"]
         Resource = ["arn:aws:dynamodb:*:*:table/etf-classifications"]
       }]
     })
   }
   ```
3. **Run:** the next scheduled (or ad-hoc QA, per the moratorium exception) invocation of
   `build_bd_assets_dim.py`, `C_06.client_mix_timeseries.py --upload`, then
   `D_03.composition_artifacts.py --upload`, then `D_04.client_portal_summary.py` -- the pipeline
   order the module docstrings already name. This is the run that overwrites the SERVED objects
   listed in Blast radius below.
4. **Closing act -- COO's one live run of FWD-1 to the page for a real client:** after step 3
   lands, the COO opens the portal page for a real relationship (the evidence file's
   `gold.served_client_portal_summary_key`, `platinum/clients/z08327149/summary.json`, is the
   candidate) and confirms VXX (that client's largest single holding by this cell's own fresh
   measurement, $21,459,506 across open lots firm-wide) reads `structured`/`Hedge` end to end on
   the real page, not from a census file. This is the ONE real run CLAUDE.md rule 22 (EVIDENCE LAW)
   requires at close for a WORLD-risk outcome.

## Evidence (this cell's real local build, 2026-09-30, LOCAL, no upload, no table write)

`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_THREAD_CENSUS_20260930.json`:
- `table_rows_at_build: 2309` (live DynamoDB scan, `Select=COUNT` cross-check identical).
- `bd_securities_reads: 0` across all three stages.
- **resolution** (library, SC-t-1): 2,220 currently-held distinct tickers (`gold/holdings_lots/
  2026-09-25.parquet`, open + ghost-excluded + AP-gated, 524,413 lots -> 2,220 distinct tickers,
  same real filters `D_03.composition_artifacts.py` applies, imported and run unmodified from
  `lib.exclusions`), 203 unclassified, 429 moved relative to round 1's OWN frozen pre-backfill
  measurement (`R1_BD_RESOLUTION_CENSUS_20260929.json`'s `before` values, unaffected by the
  backfill; `after` recomputed fresh against today's live table). `guessed: 0`.
- **silver** (assets dimension, SC-t-2): 12,146 rows in the CURRENTLY SERVED
  `silver/bd_assets_dim.parquet` (VersionId `gY8SA9ruIsLh90CuCCf42I5TBl.wceEq`, `LastModified`
  2026-09-30 00:11:40Z UTC -- grown from round 1's 10,937 via the scheduled union-mode job, an
  unrelated normal refresh, not this cell's act) -- 9,980 unclassified, 2,166 moved (every row that
  now resolves via `etf-classifications`; the served dim carries NO canonical column at all today,
  confirmed by reading its schema). `guessed: 0`.
- **gold** (C_06/D_03/D_04, SC-t-3/SC-t-4): 524,413 open lots (workaround named below), reduced to
  3,939 unique (ticker, asset_name) pairs, 1,822 unclassified, 2,017 moved (every pair that
  resolves via `etf-classifications`; the served `gold/views/firm_composition.json`, VersionId
  `8JNm8uFxWdOVMeoZ2rj5OVRI2yJvj1IY`, carries no canonical field on any holding today). `guessed: 0`.
  **Largest move by weight, overall:** IEFA, $203,112,369.65 held (equity/Developed). **Largest of
  the three acceptance-named tickers:** VXX, $21,459,506.36 -- GLD $304,940.34, PHYS $58,890.57.

**Laptop-memory workaround named (TO step 1):** the gold stage classifies the 3,939 unique
(ticker, asset_name) pairs the 524,413 filtered lots reduce to, not the full row-wise call -- a
pure function of (ticker, asset_name), so this is the identical classification the full row-wise
call would produce, not an approximation. Same source file, row filter (`is_open` + ghost exclusion
+ AP gate, via the production `lib.exclusions` functions, unmodified) and columns the product
scripts use throughout.

**Every BD-held ticker whose served class moves, including GLD, PHYS and VXX (measured, this
build):**

| ticker | resolution (library) before -> after | silver (assets dim) after | gold (composition) after |
|---|---|---|---|
| GLD  | alternatives/Gold -> commodities/Metals | commodities/Metals | commodities/Metals |
| PHYS | alternatives/Gold -> commodities/Metals | commodities/Metals | commodities/Metals |
| VXX  | alternatives/Volatility -> structured/Hedge | structured/Hedge | structured/Hedge |

Every other BD-held ticker's move is enumerated IN FULL in
`R2_THREAD_CENSUS_20260930.json`'s three stage `moves` arrays (429 + 2,166 + 2,017 entries with
`ticker`/`before`/`after`/`artifact`, gold's sorted descending by held market value) -- this half's
blast-radius reasoning below applies UNIFORMLY to all of them, not only the three named; GLD/PHYS/
VXX are named because the task order singles them out as the acceptance targets.

## Blast radius

**Served artifacts this act overwrites, and their readers (unchanged from round 1's own analysis,
re-confirmed live today):**

1. **Advisor-facing composition (`D_03.composition_artifacts.py`).**
   - `gold/views/firm_composition.json` (`FIRM_COMPOSITION`, VersionId
     `8JNm8uFxWdOVMeoZ2rj5OVRI2yJvj1IY` today) -- served via `GET /api/scoped/partners/books/
     firm/all/composition` (opal-partners-data, pure S3 proxy).
   - `gold/advisors/{advisor_id}/composition.json` -- served via `GET /api/scoped/partners/books/
     advisor/{id}/composition`.
   - `gold/entities/clients/{rel_id}_composition.json` -- read by `D_04.build_client_summaries`
     and passed through verbatim to `platinum/clients/{rid}/composition.json`.
   - **Change:** every holding in `top_holdings`/`mix[].top_holdings` gains three new keys
     (`asset_class_canonical`, `sub_asset_class_canonical`, `class_source`); the pre-existing
     `asset_class` keeps its value for every ticker except the ones the three census stages list
     as moved. No key is REMOVED from any existing holding object.
2. **Client portal summary (`D_04.client_portal_summary.py`).**
   - `platinum/accounts/{acct_id}/summary.json` -- `top_items[]` per account gain the same three
     canonical keys (previously carried none; additive).
   - `platinum/clients/{rid}/summary.json` (e.g. `platinum/clients/z08327149/summary.json`,
     VersionId `21F7AYujmWEhIsooNdXGlPU4c8eApavB` today) -- `concentration.items` is a pass-through
     of D_03's `top_holdings`, inherits the three new keys; `mix` (coarse dollar snapshot) is
     UNCHANGED in shape.
   - `platinum/firm/mix_summary.json` -- `mix` snapshot UNCHANGED (coarse, dollar-based, from
     C_06's `mix_daily_summary.json`); `concentration.items` inherits the three new keys via the
     D_03 pass-through.
   - **Known gap, not widened here (carried from round 1, row MDPF_SECCLASS-W3-S3):**
     `build_advisor_positions`'s `positions[]` (platinum/advisors/{id}/positions.json, PRD
     ADVI_49EXEC.md Section 4.5's frozen wire contract) still classifies via its own
     `_classify_ticker` closure and does NOT carry the three canonical keys -- SC-e-5 (round 2,
     separate cell) is the fix; this half does not cover it.
3. **Client mix timeseries (`C_06.client_mix_timeseries.py`).**
   - `gold/client_timeseries/{relationship_id}.json` -- `concentration[].holdings[]` gain the
     three canonical keys; `asset_class` per holding CHANGES VALUE for any ticker previously
     mis-classified to `equity` by the removed guess -- a genuine, intended value change.
   - `gold/views/mix_daily_summary.json` -- daily dollar totals by class; can shift for the same
     reason. This is the ONE case where a coarse, already-served NUMBER changes as a result of
     this act (not just gains new keys), named explicitly per HARD STOPS section 5: the real
     magnitude is this cell's fresh gold-stage `unclassified` count (1,822 unique pairs, down from
     round 1's 3,565 pre-backfill -- the backfill measurably shrank the previously-mis-guessed-to-
     equity population).

**IAM read `etf-classifications` needs (DESIRED, NOT APPLIED):** see step 2 above -- the candidate
Terraform statement, the principal (`bd-exporter-ec2-role`, confirmed unchanged from round 1's
census), and the measured absence of any DynamoDB statement on that role today.

**Release order:** this deploy runs AFTER the scheduled backfill (release steps 1 and 2, both
CLOSED) already landed its table rows -- so a holding the backfill resolves (GLD, PHYS, VXX, and
every other ticker the three census stages list) is never shown unclassified in the served
artifacts in the gap between deploys. This is the SAME ordering constraint round 1's half named;
it is satisfied today (2,309 rows already live) where round 1 could only state it as a precondition.

## Rollback per key

S3 IS versioned for `opal-data-bd`: rollback restores the PRIOR object version at each key, not an
attribute-level undo.

- **Code rollback:** `.tools/safe-deploy.sh` on the PRE-cell commit (the parent of the round-1
  SC-t-1 commit, i.e. before @ae7aa281b0's five files) for the same five files, re-verified by
  SHA -- returns every gold/silver script to its pre-MDPF_SECCLASS behavior (old two-layer
  classifier, old equity-guess fallback in C_06, no canonical columns anywhere).
- **Data rollback, per served key:** every key named in Blast radius above (`gold/views/
  firm_composition.json`, `gold/advisors/{id}/composition.json`, `gold/entities/
  clients/{rid}_composition.json`, `platinum/accounts/{id}/summary.json`, `platinum/clients/
  {rid}/summary.json`, `platinum/firm/mix_summary.json`, `gold/client_timeseries/{rid}.json`,
  `gold/views/mix_daily_summary.json`, `silver/bd_assets_dim.parquet`) is an S3-versioned object;
  `aws s3api list-object-versions --key <key>` + `aws s3api copy-object --copy-source
  <bucket>/<key>?versionId=<prior>` restores the exact pre-deploy bytes for that one key,
  independent of every other key. The VersionIds recorded above (as of 2026-09-30, this build) are
  the PRIOR versions this rollback would restore to, for the three artifacts this half reads by
  name.
- **IAM rollback:** the candidate `bd_exporter_etf_classifications_read` policy (step 2), once
  actually applied under its own future sign-off, rolls back by `terraform destroy -target` on
  that one resource (safe-apply only, never a hand `aws iam` call) -- it is additive-only
  (`dynamodb:GetItem`, one Sid, one resource ARN), so removing it cannot affect any other grant on
  `bd-exporter-ec2-role`.
- **No table write:** this act reads `etf-classifications`, never writes it -- there is no
  DynamoDB rollback needed for this half.

## COO half -- [PENDING SIGNATURE]

## CTO half -- [PENDING SIGNATURE]
