# DS~C 2026-05-13 session 1 — IWM book.json gaps brief (RD 0.4.2) — empirical diagnosis + Lambda orphan-bucket fix

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~14:30Z → ~14:50Z 2026-05-13 (~20 min)
**Trigger:** RD 0.4.2_RD_AdvisorIntelligence inbox brief `20260512T215426Z_0.4.2_RD_AdvisorIntelligence_Brief__IWM_advisor_book.json_data_gaps__.md` — Andrew-forwarded, 4 alleged gaps in IWM Book Overview view (no allocation / no holdings / em-dash AUA strip / "Pending DS emit" relationship_since). Brief was authored 21:54Z 2026-05-12 — BEFORE chain #23 ran at 23:01Z.

## TL;DR

Diagnostic-first cadence (reinforced from session-3 decision note #1, 2026-05-12): pulled live S3 artifact before any code edit. Found **3 of 4 alleged gaps were already populated** — chain #23/#24 post-brief shipped the fields. 1 real bug surfaced: phantom `clients[0]` row synthesised from IWM catchall's unallocated bucket (19 accounts, $284K, `household_id=null`, `display_name=""`) drove FE "Pending DS emit" placeholder by virtue of sort-by-AUA-desc placing the headless row first. Shipped Lambda fix (`52478bb3a`); AE brief authored (`9b9746358`); RAVC2 to RD; AE 0.6.1 brief delivered.

Brief mis-attributed the emitter — INF_D_02 writes v0 book.json, but `inf-portal-advisor-publisher` Lambda (`lambda_function.py` L504-578 `_build_book`) overwrites it with `headline` / `composition` / `top_holdings` / `clients[].relationship_since`. The fix lives in the Lambda, not the gold script.

## Ship roster

| Time (UTC) | Commit | Scope | Lines |
|---|---|---|---|
| 14:47 | `52478bb3a` | Lambda `_client_list` skip when `_hh_int is None` | +12/-2 |
| 14:48 | `9b9746358` | AE brief for v1.7.54 build-and-upload | +64/0 |

Total: 2 commits, +76/-2 lines.

## Per-commit detail

### Lambda orphan-bucket drop (`52478bb3a`)

**Symptom (Andrew via RD brief):** IWM Book Overview shows "Pending DS emit" on Newest Relationship card + empty-name row above named households in Client List panel.

**Root cause:** `_client_list` (L504-525 pre-fix) groups `adv_df` by `household_id` and for IWM the catchall produces accounts where account_team has null/'unknown' household_id. `groupby('household_id')` synthesises a group for those rows. The existing `_hh_int = None if (pd.isna(hh_id) or str(hh_id) == 'unknown') else int(float(hh_id))` defends `client_key` and `relationship_since` rendering (correctly emits null) but the loop still appends the phantom client row at `clients.append({...})`. `clients.sort(key=lambda c: c['aua'], reverse=True)` then places it at position [0] because the orphan ($284K) beats the largest named household (Thompson, $225K).

**Fix:** insert `if _hh_int is None: continue` immediately after the resolution. Also drops two dead `if _hh_int is not None else None` ternaries on `client_key` and `relationship_since` (unreachable after the continue). 12 inserts / 2 deletes.

**Why orphan-skip not orphan-relabel:** considered emitting orphan as a structured `is_unallocated: true` pseudo-client with `display_name: "Unallocated Accounts"` so FE could surface the $284K explicitly. Deferred — that's a product decision (does Andrew want unallocated AUA visible-as-row or rolled-into-totals-only?). Current fix puts the orphan into `summary.total_aua` / `summary.account_count` (unchanged at $536K / 41) but invisible in `clients[]`. RD can request the relabel variant if desired.

**Cross-firm impact verified:** only IWM has orphans. `peter_lee` (201 clients / 0 orphans), `patrick_scanlan` (73 / 0), `joe_brandenburg` (small / 0). The fix is safe for all advisors.

### AE brief (`9b9746358`)

`docs/briefs/ae-brief-inf-portal-advisor-publisher-orphan-bucket.md` — build-and-upload command + terraform apply expectations + verification sentinel + out-of-scope flags for the 2 follow-up investigations (Q4 '25 anomaly, $0-AUA stale households, upstream household_id null gap).

## Empirical state of the 4 alleged gaps (chain #23 post-fix)

| Gap | Brief | Live S3 (2026-05-13T07:11:41Z book.json) |
|---|---|---|
| 1 composition | "No allocation data" | `composition.total_market_value: $252,185.25`, `mix` = fixed_income 53.8% / equity 33.6% / alternatives 6.5% / cash 6.1%, 6+ nested top_holdings per asset_class |
| 2 top_holdings | "Top Holdings empty" | Both `composition.top_holdings` AND top-level `book.top_holdings` have 10+ ticker rows with `pct_of_aua` |
| 3 historical_quarters | "all em-dashes" | 25 entries 2020-Q2 ($459,980) → 2026-Q2 ($252,185). **Q4 '25 = $1.19** — real but unrelated to em-dashes |
| 4 relationship_since | "Pending DS emit" | 10 of 11 clients have it; the 1 null is the orphan row at clients[0] — **THE FIX** |

## Out-of-scope flags surfaced (separate investigations)

1. **Q4 '25 = $1.19 in `headline.historical_quarters`.** `_quarter_ends_from_timeseries` picks the latest daily row ≤ quarter end. IWM Q4 '25 timeseries has 31 of 92 daily rows under $100 (reorg-window volatility — accounts churning in/out of catchall during 2025-10 → 2025-12). The picked row was 2025-12-01 with `total_aua=$1.19, account_count=1`. Strip 4-chip values: Q3'25 $1.36M / Q4'25 $1.19 / Q1'26 $25K / Q2'26 $252K. If "all em-dashes" is what FE actually renders, it's likely an FE threshold/rounding rule on $1.19 — DE/RD investigation. Or DS revisits `_quarter_ends_from_timeseries` to use period-median / last-stable-non-anomaly. Product call needed.

2. **8 of 11 IWM households show `aua=$0`** with valid `relationship_since` (2023-10 / 2025-01 / 2025-04 dates). Stale relationships where accounts dropped out of IWM during reorg. After orphan fix, the visible clients[] is: Thompson ($225K), Collins ($27K), then 8× $0 rows. Same product question — surface dormant or suppress?

3. **19 IWM accounts have `household_id=null` in `account_team`.** Real upstream data-quality gap (silver or INF_C_07). Separate DS investigation pending; not blocking this fix.

## Compiler Tools

| Tool | Runs | Result |
|---|---|---|
| `ds-commit-gate.sh inf-portal-advisor-publisher/lambda_function.py` | 1× | PASS — py_compile + ds-precommit + ruff py39 clean |
| `safe-commit.sh --author 0.4.0_DS_ClientPlatform~C` | 2× | Both clean. First (Lambda fix) one-shot; second (AE brief) required prior `git add` since brief is a new untracked file — `safe-commit --only` does not add untracked. |
| `safe-deploy.sh` pre-push hook | 2× | Both OK — Lambda code + docs not in `data/*/scripts/{gold,silver,bronze}` deploy-scope, no S3 upload required |
| Live S3 diagnostics (4 calls) | 4× | `inflection_wealth_management/book.json` (full structure dump) + `peter_lee/book.json` + `patrick_scanlan/book.json` + `inflection_wealth_management/timeseries.json` (Q4 '25 anomaly source) + listing of `platinum/advisors/` (joe_brandenburg confirmation) |

No `comp-pipescript io` run — the change is in Lambda code, not gold-script `.py`. `comp-iam service` not needed (no new boto3 ops introduced).

No owned-paths blocks. No commit gate failures. No SHA mismatches. No hook bypasses.

## Inbox watcher hygiene

| Incident | Resolution |
|---|---|
| Initial inbox-watch launch | Clean (PATH wrapper, run_in_background tracked) |
| Mid-session watcher-exit notification | Expected (one-launch = one-delivery = one-relaunch). Relaunched via tracked Bash tool. |

## Files Modified

| File | Change |
|---|---|
| `infra/aws/lambda/inf-portal-advisor-publisher/lambda_function.py` | `_client_list` skip when `_hh_int is None` (+12/-2) |
| `docs/briefs/ae-brief-inf-portal-advisor-publisher-orphan-bucket.md` | new AE brief for v1.7.54 (+64/0) |

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **AE 0.6.1 / AE 0.7** | `build-and-upload.sh inf-portal-advisor-publisher` → terraform plan/apply → tag `inf-pipeline-v1.7.54`. Single Lambda code change, no IAM/EC2/env/layer changes. Drop-in. ETA whenever AE bandwidth allows; non-urgent. |
| **DS~C self — post-deploy** | Validate next chain run output. Hard sentinel: `clients[0].relationship_since != None` and `clients[0].display_name = "Richard L Thompson & Cheryl L Thompson"` and `clients` length = 10 (was 11). RAVC2 to RD + DE + Andrew with pre/post numbers. |
| **RD 0.4.2_RD_AdvisorIntelligence** | (1) post-deploy smoke on IWM Book Overview + Client List + Newest Relationship card. (2) product call on Q4 '25 $1.19 anomaly + $0-AUA stale households. (3) flag to Andrew on upstream household_id null gap for 19 accounts. |
| **DE 0.4.0_DE_ClientPlatform** | Post-chain smoke — Newest Relationship card renders Thompson 2026-04-15 (not "Pending DS emit"); Client List panel no longer has empty-name row at top. |

## Decision notes (worth keeping)

1. **Always pull S3 first.** Brief's hypothesis "3 of 4 gaps are missing-emit" was wrong — chain #23 had already shipped the fields. The 4th was a real bug, but a *different* bug from the brief's description (orphan-phantom, not missing-emit). Reinforces session-3 decision note #1. Cost: 30 seconds of `aws s3 cp` saved hours of pipeline work.

2. **Re-read the brief's hypothesis against actual emitter.** Brief named INF_D_02 (line 128-129 comment) as the emitter. Actual emitter is the Lambda. The L128-129 comment is correct in its scope (IWM-as-first-class in placeholder set) but unrelated to the rendered fields. When grep finds the alleged emitter, *also* grep the alleged fields — if they don't appear in the named file, the brief misidentified the source.

3. **Sort discipline beats filter discipline.** The orphan was getting through `groupby` because pandas-groupby-with-non-NaN-string-key ('unknown') doesn't drop. A defensive `if _hh_int is None: continue` after the type-coerce is more robust than trying to fix the groupby behavior at the source (which would have required investigation of the upstream account_team schema).

4. **AE brief should call out null-IAM / null-layer changes explicitly.** AE shipped 5+ inf-pipeline Lambda revs in May; each one differs in whether IAM / layers / env vars need changes. Stating "no IAM, no EC2, no env vars, no layer changes" up front saves AE a `terraform plan` review cycle. Borrowed from `9301dfe97` v1.7.53 brief which did this well.

5. **Don't take on Andrew/RD product calls without surfacing them.** The Q4 '25 $1.19 anomaly and $0-AUA stale households are real but not "fix me silently" candidates — they're "should this surface or not" judgments. Surface as out-of-scope flags so Andrew/RD can pick the direction; don't preempt with a unilateral filter.

## Pacing

20 min from inbox-read to RAVC2-sent. Diagnostic-first saved ~80% of pipeline work the brief implied was needed. The fix is 14 lines of touched code in a Lambda; the analysis around it (cross-firm orphan check, anomaly cause, out-of-scope follow-ups) is what makes the RAVC2 closure-ready vs. a half-fix that punts on the data weirdness.
