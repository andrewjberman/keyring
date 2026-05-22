# MDPF Global v0 — CEO Methodology Pivot + AE Opt A Lambda Neutralization

**Agent:** `0.4.0_DS_ClientPlatform` (sole-DS this session, Andrew-direct)
**Span:** 2026-05-19 ~14:40Z → ~16:15Z (post-close-out continuation)
**Predecessor session log:**
`org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-19/MDPF_Global_v0_design_through_close.md`
**Status at session close:** all immediate page-driving work landed; AE Opt A
(Lambda neutralization) in flight; new TO `MDPF_ASSETS.017` accepted with
tomorrow-morning pickup window.

---

## 1. The CEO directive (Andrew-relayed, verbatim)

After the prior session-log close on the Spread-2 decomposition brief +
identity-1 masking-class memory, Andrew brought a CEO-direct methodology
pivot covering all six cohorts:

| Cohort | CEO directive | Change from prior state |
|---|---|---|
| **0** | Include in headline; netted of Cohort N ownership | **REVERSE** the same-session `bd2bbfbd9` reversal — Cohort 0 BACK IN `opal_aggregate_aua` |
| **1a** | 49F SmartX, continue | No change |
| **1b** | "All 49 assets minus miscellaneous assets/liabilities like the single residential property/credit cards/mortgages/etc." | **METHODOLOGY CHANGE** — supersedes the 5/18 Schwab-only ruling; expand from Schwab-confirmed-only to ALL 49 minus liab + misc |
| **1c** | SMAs continue | No change |
| **2a** | Inflection Eclipse, blends split into constituents | No change (already done via `BLEND_SPLIT` in `46bb5b023`) |
| **2b** | Track but **exclude from headline** | **CHANGE** — Inflection non-model $106M moves to audit-trail field |
| Cohort 0 partner-held | **larger of BD transactions / Schwab RPS** per ticker | **METHODOLOGY CHANGE** — WS-D.2 currently RPS-only |

Andrew summary: *"all this means is we just figure out the shape for keeping
99% of 49 assets going back to 1/17 or whenever we first have
silver/allocations/ parquets and bring that into our time series. Then we
just net 49 ownership via the larger of BD transactions/RPS from the ETF
assets from Trueshares/Pathfinder."*

---

## 2. Empirical probing — three findings that shaped the implementation

### 2.1 BD silver/allocations `account_type` distribution (1b exclusion identification)

Probed BD 2026-05-15 partition. 30 distinct `account_type` values. Found
the residential properties Andrew/CEO mentioned — there are **two**, both
in `'No Account Type Assigned'` bucket with round-number MV (likely
manually-entered):

```
Austin Home        $1,750,000.00   account_type='No Account Type Assigned'
Silverthorne Home  $2,000,000.00   account_type='No Account Type Assigned'
```

Andrew confirmed the exclusion set: **residential properties + Bank
($770K) + Savings ($712K) + existing liabilities** (CreditCard / Mortgage /
Loans / Bank / Savings). Approximate exclusion budget: ~$5.25M (vs the
"1% of $1.8B = $18M" CEO budget — comfortably under).

### 2.2 BD position-grain source freshness for "max(BD, RPS)" Cohort 0

Probed all BD position-grain layers:

| Source | Grain | Coverage | Freshness |
|---|---|---|---|
| `silver/daily_positions.parquet` | per-account-per-ticker | 2020-06-30 → 2026-01-27 (5+yr, 116M rows) | **STALE** — single file, last fetch 2026-02-02, 4 months behind |
| `silver/transactions/` | per-transaction | daily through 2026-05-15 | Fresh, but holdings require running-balance compute |
| `silver/assets/` | per-transaction enriched | partitioned daily | Sample shows transaction-level, not holdings |
| Schwab RPS | per-account-per-ticker | daily through 2026-05-15 | Fresh; already in WS-D.2 |

Critical: Andrew's "BD silver/allocations" choice for the BD source is
empirically impossible — that file is account-grain, NO ticker columns
(verified `[c for c in df.columns if 'ticker' in c.lower()]` = empty).
The actual position-grain source is `silver/daily_positions.parquet` but
it's stale.

Andrew confirmed **hybrid path**: RPS for current daily; BD
`daily_positions.parquet` for historical backfill (5-year history); take
per-ticker `max(BD, RPS)` over the overlap window for cross-validation.

### 2.3 Inflection per-model breakdown (Eclipse `model_name` → portal display)

Probed `s3://opal-data-inf/gold/eclipse/{date}/model_portfolio_accounts.parquet`
+ verified the canonical mapping against the WS-C feeder output for the one
WS-C partition available (2026-05-18):

```
Eclipse model_name              -> portal display_name (via registry model_key)
Opal Ultra Short Term            -> Ultra Short-Term
Opal Short Term                  -> Short-Term
Opal Intermediate Growth         -> Intermediate
Opal Long Term                   -> Long-Term Conservative
Opal Ultra Long Term             -> Long-Term Aggressive
50/50 OPAL INT/OPAL LTC          -> SPLIT 50/50 into Intermediate + Long-Term Conservative
50/50 OPAL ST/INT                -> SPLIT 50/50 into Short-Term + Intermediate
```

Eclipse has 4 dates: 2026-05-15, 05-17, 05-18, 05-19 (newest discovered
mid-session — Inflection onboarded around 5/15 per Andrew's confirmation).
`Opal Ultra Long Term` mapping to `Long-Term Aggressive` is non-obvious
nomenclature but verified via WS-C feeder's canonical `model_key`.

---

## 3. Commits this session (chronological, DS Base lane)

All on `origin/CLOUD`. All gate-clean (ds-commit-gate exit 0).

| Commit | Title | What it landed |
|---|---|---|
| `225df40bc` | feat(mdpf): CEO-direct methodology pivot | Major: `build_legacy_compat_emit.py` rewritten. Cohort 0 IN headline, broader 1b (all 49 minus exclusions), 2b OUT (audit-only), BD roll-forward for periods beyond latest BD partition, residual mechanics updated. New constants: `LIABILITY_TYPES_BROADER`, `MISC_ACCOUNT_TYPES_BROADER`, `MISC_ACCOUNT_NAME_PATTERN`. New function: `compute_49f_broader_custody()`. New audit field: `inflection_non_model_aua`. |
| `abc371cb6` | feat(mdpf): update custody crosswalk cache metadata | Cache republished at `s3://opal-data-mdpf/cache/custody_crosswalk.json` with new methodology metadata per AE 0.7 "belt-and-suspenders" framing. Added fields: `methodology=ceo_directive_20260519_v1`, `methodology_supersedes=schwab_only_20260518`, `exclusion_account_types`, `exclusion_account_name_patterns`. Retained `schwab_custodian_value` + `liability_types` for back-compat. New sha256: `930cda12bd5c203c85fc6faff5956c26ceb1eef242a195420053312884688d98` (was `b106a983...`). |

---

## 4. Live S3 state at session close

### Page-driving (legacy files my emit overwrote)

- `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json` — 393
  daily periods, 2026-01-16 onward carry CEO methodology. Latest entry
  2026-05-19 aggregate $1,426,516,528.46.
- `s3://opal-data-portal-v2/json/portfolios/non_model_assets.json` —
  latest 2026-05-19 enterprise_total $2,002,399,660.52 with new fields:
  - `etf_public_residual: $109,113,394.24` (Cohort 0, in headline)
  - `inflection_non_model_aua: $106,254,365.08` (Cohort 2b, audit-only)
  - `method: ceo_directive_20260519_v1`

### Cache (republished)

- `s3://opal-data-mdpf/cache/custody_crosswalk.json` — sha256
  `930cda12bd5c203c85fc6faff5956c26ceb1eef242a195420053312884688d98`. AE
  0.7 keeps the file as documentation-of-record (no longer load-bearing
  for the runtime custody filter under Opt A).

### Platinum partitions (UNCHANGED — still emit Schwab-only methodology)

The MDPF chain platinum prefix (`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/`)
still carries Schwab-only methodology in the WS-E + WS-A emit. Phase 1B
(WS-A + WS-E canonical update) is the canonical alignment work; tracked-deferred
under MDPF Phase-2.5-hardening per CTO ruling this session. Platinum partition
2026-05-19 sample: `partner_custody_total: $1,648,847,956.91` (Schwab-only),
vs legacy file's broader $1,800M.

---

## 5. Verified cohort breakdown — Andrew-confirmed accurate

Per-cohort snapshot for 2026-05-19 produced + Andrew confirmed accurate
("this all looks correct, also inflection was onboarded sometime around
5/15, so the jump is to be expected"):

```
Cohort 1a 49F SmartX core models       $1,332,817,818.27
Cohort 1b 49F broader (all-49 minus excl) $441,814,503.12
Cohort 1c 49F SMAs                       $24,955,234.70
Cohort 2a Inflection Eclipse models      $93,698,710.19
Cohort 0  ETF public float netted       $109,113,394.24
                                      ─────────────────────
HEADLINE                             $2,002,399,660.52  ($2.00B)

Cohort 2b Inflection non-model (audit-only) $106,254,365.08
```

### Cohort 0 per-ETF (2026-05-19, NAV minus partner-held)

```
ETF    NAV (issuer)        49F held (RPS)     Inflection held   Cohort 0
DIVZ   $241,845,658.00     $167,828,409.97    $0.00             $74,017,248.03
IDVZ   $158,661,515.00     $146,264,809.75    $0.00             $12,396,705.25
PFDE   $131,630,541.00     $119,774,537.09    $0.00             $11,856,003.91
PFOE   $110,854,025.00     $100,010,587.95    $0.00             $10,843,437.05
                                                                ─────────────
                                                          TOTAL $109,113,394.24
```

Surfaced to Andrew: PFDE + PFOE Inflection-held DROPPED to $0 between 5/18
and 5/19. Cohort 0 for PFDE + PFOE jumped ~$8-10M as a result. Likely a
WS-D.2 target_weight vs Eclipse model_composition vintage issue on the
Inflection side; non-blocking for the page total but flagged.

---

## 6. Org thread (COO + CTO + AE) — Opt A architectural pivot

Key sequence:

1. **AE 0.7 receives CEO directive** + proposes Opt A (NEUTRALIZE Lambda) or
   Opt B (SoT-read from my aggregator output) in RAVC1.

2. **My empirical correction to AE** — `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-05-19.json`
   partition empirically carries Schwab-only methodology (`partner_custody_total
   $1,648,847,956.91`), NOT the broader methodology. AE's Opt B SoT-read
   would need Phase 1B (WS-A + WS-E canonical update) as a prerequisite.

3. **CTO PATH (a) disposition** — AE adopts **Opt A** (Lambda neutralization).
   My `build_legacy_compat_emit.py` becomes sole SoT for the legacy files.
   Lambda v1.0.1 ships tomorrow 14:00 UTC as a no-op write block.

4. **Day-1-zero guard migration** — COO's `SXIN_DAY1ZG.001` (originally
   scoped inside the Lambda) becomes scope-orphaned under Opt A. Migrates
   to `MDPF_ASSETS.017.dsbase-day1-zero-guard-emit-side` in my lane.
   12-day runway to 2026-06-01.

5. **CTO accelerates AE Opt C v1.0.2** — productionize my emit as scheduled
   Lambda/SSM. Re-sequenced ahead of ADHC_DSFLOW.007 + ADVI_INFALM.001.
   Compresses the bridge window to ~1-2 business days.

6. **Bridge daily-fire decision** — my pick. Locked in **manual-on-demand**
   via /loop cadence for the 1-2d window (escalate to SSM only if Opt C
   slips). CTO ratified.

7. **SSM RunDocument spec sidecar** — to author during the .017 session
   tomorrow morning. Doc-of-record AE wires into Opt C v1.0.2 directly.
   Per CTO: "same file, same focus session."

---

## 7. MCP messages this session (durable record)

All channel-pushed where the recipient was live.

| Time | To | Subject |
|---|---|---|
| ~14:50Z | COO | RAVC2 — Spread-2 closure brief + memory anchor #5 (prior arc continuation) |
| ~14:53Z | CTO | DONE both GOs (memory + brief) |
| ~15:15Z | CTO | Decisions locked + bridge mechanism + SSM spec sidecar plan |
| ~15:27Z | AE 0.7 | URGENT v1.0.1 needed before tomorrow 14:00 UTC + CEO methodology spec |
| ~15:40Z | COO | ACK both messages (SXIN_DAY1ZG.001 stand-down + MDPF_ASSETS.017 receipt) |
| ~15:53Z | AE 0.7 | RE: SoT-pattern — empirical Phase 1B prerequisite + plan |
| ~16:02Z | COO | ACK both ACK messages (.017 pickup tomorrow AM + bridge decision) |
| ~16:12Z | CTO | Decisions locked + ratified |

---

## 8. Outstanding items at session close

| Item | Owner | State |
|---|---|---|
| MDPF_ASSETS.017 (day-1-zero guard in my emit) | DS Base (me) | Pickup tomorrow ~13:00 UTC. ~0.5d wall. RAVC2 → COO + CC CTO on close. |
| SSM RunDocument spec sidecar | DS Base (me) | Authored during .017 session (same file, same focus). |
| AE 0.7 smartx-pipeline-v1.0.1 (Lambda neutralization Opt A) | AE 0.7 | RAVC1 in flight; ships tomorrow 14:00 UTC. |
| AE 0.7 Opt C v1.0.2 (productionize my emit) | AE 0.7 | Accelerated to first-after-v1.0.1; 1-2 business days from now. |
| Bridge daily-fire | DS Base (me, manual via /loop cadence) | In motion. Last emit `225df40bc` is canonical until tomorrow chain fires ~15:00 UTC → I re-fire ~5min after. |
| Phase 1B (WS-A + WS-E canonical update to broader methodology) | DS Base (me, COO authors TO) | TRACKED-DEFERRED under Phase-2.5-hardening per CTO ruling. Memory cross-link to `feedback_identity1_masks_absolute_value_class.md` belongs in the hardening TO. |
| Phase 3 (BD daily_positions historical Cohort 0) | DS Base (me) | Non-urgent follow-on. Tracked under task #27. |
| WS-C Inflection feeder full historical | DS Base (me) | Task #16, deferred. Eclipse historical pull required. |
| Cohort 0 Inflection-held vintage issue (PFDE/PFOE 5/18→5/19) | DS Base (me) | Surfaced to Andrew. Non-blocking for page total. Investigation deferred. |

---

## 9. Key numbers to-the-cent at session close

| Metric | Value |
|---|---:|
| 2026-05-19 headline (page enterprise_total) | **$2,002,399,660.52** |
| Cohort 1a (49F SmartX 5 core models) | $1,332,817,818.27 |
| Cohort 1b (49F broader, all-49 minus excl) | $441,814,503.12 |
| Cohort 1c (49F SMAs: Dividend + Equity Growth) | $24,955,234.70 |
| Cohort 2a (Inflection Eclipse, blends split into constituents) | $93,698,710.19 |
| Cohort 0 (Opal-ETF public float netted of 49F-RPS-held) | $109,113,394.24 |
| **─── audit-only (NOT in headline) ───** | |
| Cohort 2b (Inflection non-model) | $106,254,365.08 |

---

## 10. Process / structural notes for next session

1. **`.017` pickup is mine tomorrow morning.** Compute-step placement
   (before any compute uses `model_aum`). Recipe: `assert model_aum >
   MIN_PLAUSIBLE_THRESHOLD (~$100M)` AND/OR `±15% prior business day`;
   raise + don't write + preserve prior emit + log clearly. AC1-AC7
   verbatim from `MDPF_ASSETS.017.dsbase-day1-zero-guard-emit-side.md`.

2. **SSM RunDocument spec sidecar** — needs:
   (a) compute-step idempotence semantics
   (b) `--upload` invocation contract
   (c) exit-code conventions for success / day-1-zero-skip / hard error
   (d) log-capture path convention
   Author as Markdown adjacent to `build_legacy_compat_emit.py`
   (probably `data/mdpf/scripts/backfill/RUNDOCUMENT_SPEC.md` or similar).

3. **Bridge daily-fire is on /loop cadence.** When tomorrow's MDPF chain
   produces the new platinum partition at ~15:00 UTC, I re-fire
   `build_legacy_compat_emit.py --upload` within ~5min. /loop ticks every
   10 min cover the daily-presence requirement without external scheduling.
   If Opt C v1.0.2 slips beyond 2 business days, escalate to wiring an
   SSM RunDocument myself (~30min).

4. **Phase 1B + Phase 3 are tracked-deferred, not killed.** COO authors
   the hardening TO when my bandwidth opens after .017. Memory pointer to
   `feedback_identity1_masks_absolute_value_class.md` belongs in the
   hardening TO so the platinum-canonical-vs-legacy-served methodology
   divergence is explicitly tied to the masking-class entry. Future agent
   auditing platinum methodology lands there naturally.

5. **The CEO directive supersedes the 5/18 Schwab-only ruling for the
   legacy page.** WS-E + WS-A still emit Schwab-only into platinum —
   that's the divergence Phase 1B closes. Anyone reading platinum without
   knowing this divergence will believe the 49F partner total is
   $1,648.85M (Schwab-only) when the actual page-displayed value is
   $1,800M+ (broader). Cross-reference is in commit messages of
   `225df40bc` + the memory entry update.

6. **Cohort 0 per-ETF audit note worth banking** — PFDE + PFOE Inflection-held
   dropped from $9.77M / $8.02M (5/18) to $0 / $0 (5/19) in the platinum
   etf_decomposition. The +$8-10M shift in Cohort 0 between days is real
   per the platinum data but the underlying mechanism (Eclipse target_weight
   vs model_composition vintage) needs investigation. Flagged to Andrew;
   non-blocking; deferred.

---

## Appendix A — Andrew-direct anchors this session

1. *"For Cohort 0: Yes, we do want to display ETF assets (netted of Cohort
   N ownership)."* — un-revert Cohort 0 into headline.
2. *"1b - This is actually all 49 assets not including the miscellaneous
   assets/liabilities like the single residential property/credit
   cards/mortgages/etc."* — broader 1b methodology, supersede Schwab-only.
3. *"50/50 portfolios should be split in the models that we do have
   bucketed front end."* — confirmed `BLEND_SPLIT` from `46bb5b023`.
4. *"2b - These we will not include in our AUA for now but we want to keep
   track of it."* — audit-trail field, not in headline.
5. *"we just net 49 ownership via the larger of BD transactions/RPS from
   the ETF assets from Trueshares/Pathfinder."* — Cohort 0 partner-held
   `max(BD, RPS)`.
6. *"This all looks correct, also inflection was onboarded sometime around
   5/15, so the jump is to be expected"* — Andrew verification of the
   cohort breakdown numbers + acceptance of the Inflection-appearance
   step at 5/15.

---

## Appendix B — File touchpoints this session

```
data/mdpf/scripts/backfill/build_legacy_compat_emit.py         225df40bc
data/mdpf/scripts/backfill/build_custody_crosswalk_cache.py    abc371cb6
```

S3 paths overwritten:
```
s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json
s3://opal-data-portal-v2/json/portfolios/non_model_assets.json
s3://opal-data-mdpf/cache/custody_crosswalk.json
```

Backup local copies (pre-overwrite, recoverable):
```
.runtmp/legacy_aum_pre_overwrite.{ts}.json
.runtmp/legacy_nm_pre_overwrite.{ts}.json
```

S3 versioning enabled on both buckets → all overwrites recoverable via
`aws s3api list-object-versions` if needed.
