# Schwab -> Daily-Box (SchwabAutoDownload) Re-Point -- Durability Design + Enumeration

**Status:** v0.1 DESIGN/ENUMERATION -- for CTO arch-gate (no implementation until gated)
**Author:** 0.4.0_DS_ClientPlatform~A | **Requested by:** Andrew-strategic (via CVO) -> 2.0.0_SA_COO [DRIVE] 2026-07-02
**Reviewers (RAVC):** 2.0.0_SA_COO (owner) + 1.0.0_SA_CTO (arch-gate) + 3.0.0_SA_CVO (verify)
**Scope fence:** does NOT touch bd(a) Black Diamond (separate feed). This is the SCHWAB feed only.
**Relationship:** the FRESHNESS/DELIVERY layer for the *currently-served* Schwab silver -- complementary to, and NON-blocking on, the DATA_SSOTMG never-widen canonical cutover (see Section 6).

---

## 1. Problem & goal

Andrew-strategic durability directive: re-point every Schwab-dependent process to draw from the **daily** Schwab EC2 box (SchwabAutoDownload) instead of the lagging manual batch path, so Schwab-fed surfaces get **daily** freshness -- preventing the batch-lag recurrence that shadowed the MDPF never-widen flip (the prime symptom: `schwab/silver/rps` floored at 06-30 while the flip needed fresh custody).

**Goal:** an automated daily Schwab silver refresh, so the ~15 downstream consumers (Section 3) advance every day with **zero consumer changes** (same served S3 contract).

**Non-goal (this brief):** the DATA_SSOTMG never-widen cutover to canonical-as-SSOT (separate, parity-gated program). This re-point is the tactical freshness BRIDGE that de-risks the recurrence NOW; it retires when the cutover lands.

## 2. Current-state ground truth (compiler + agent grounded 2026-07-02)

### PATH A -- the BATCH path (SERVED today; the lag source)

```
OneDrive 08242234\  --(MANUAL: sync_schwab_onedrive_to_s3.py --upload)-->  s3://opal-data-schwab/01_raw/ (+ bronze/rps/)
   --(MANUAL: /49-schwab-conv skill runs 6 converters)-->  s3://opal-data-bd/schwab/silver/{acc,rps,trn,trn_nna,uln,rld}
```

| Table | Converter (`data/black_diamond/scripts/bronze/`) | Input | Output `opal-data-bd/schwab/silver/` |
|---|---|---|---|
| acc | `convert_schwab_acc_to_parquet.py` | S3 `01_raw/` `CRS*.ACC` | `acc/date=/data.parquet` |
| rps | `convert_schwab_rps_to_parquet.py` | S3 `{bronze/rps,01_raw}` `CRS*.RPS` | `rps/date=/data.parquet` |
| **trn (A)** | `convert_schwab_trn_to_parquet.py` | **LOCAL DISK** (OneDrive `DEFAULT_SRC_DIR`) `CRS*.TRN` -- **not S3** | `trn/` |
| trn_nna (B) | `convert_schwab_trn_to_nna_silver.py` | S3 `silver/trn/` | `trn_nna/` |
| uln | `convert_schwab_lots_to_silver.py uln` | S3 `01_raw/` `CRS*.ULN` | `uln/` |
| rld | `convert_schwab_lots_to_silver.py rld` | S3 `01_raw/` `CRS*.RLD` | `rld/` |

*(Deprecated, NOT in the skill: `convert_schwab_rps_to_silver.py`, `convert_schwab_uln_to_silver.py` -- do not re-point these.)*

**LAG CAUSE (root):** PATH A has **no automated trigger**. Both the OneDrive->S3 sync AND all 6 converters run **only** when a human AE invokes `/49-schwab-conv`. The converters are idempotent + extend-from-last-date, so silver sits frozen at the last manual run. 49F is treated as a monthly-batch source; `rps` shows 06-30 only because a stray `CRS20260630.RPS` rode the last manual drop.

### PATH B -- the DAILY boxes (auto; parallel / NOT served today)

- **`canonical-schwab-si2`** (raw ingest, Win2022, `i-0f3d57a97f14727af`): scheduled tasks `SchwabAutoDownload` + `SchwabS3Sync` (`C:\SchwabData\sync-to-s3.ps1`), now driven by EventBridge SSM `AWS-RunPowerShellScript` at **08:35 + 20:35 UTC** (`infra/aws/terraform/canonical-schwab-si2-schedule/schedule.tf`), 14h-absence alarm. **Lands raw to `s3://opal-data-schwab/01_raw_quartz_validation/`, NOT `01_raw/`** -- production `01_raw/` repoint is **HELD on N=5 clean box-days** (Andrew Caution-B parallel ruling; 0.6.2_AE lane).
- **`canonical-schwab-runner`** (canonical build, r6i.xlarge, `i-0ed92ce2e72f505dc`): EventBridge xref-success sentinel -> `build_canonical_daily.py` reads production `01_raw/` -> `opal-data-bd/canonical/schwab/{silver,gold}/` (17 facts + 5 dims + G1-G14). Parallel/not-served.

**Key finding:** the daily-delivery infra (SI2 box + canonical-runner) **already exists and runs daily**. The gap is purely that the **SERVED PATH-A silver is not wired to it** -- it has no auto-trigger, the SI2 raw lands in a different prefix (`01_raw_quartz_validation/`), and one converter (TRN) reads local disk.

## 3. Enumeration -- Schwab-dependent consumers (COO ask step 1)

Consumers of the SERVED `opal-data-bd/schwab/silver/*` (the tables this re-point makes daily-fresh). Portal has **zero** direct reads (fed only by BD gold, one hop downstream). All get daily freshness for free once silver is daily -- no consumer change.

**`schwab/silver/rps` (the prime -- ~10 consumers):**
1. `data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py` -- MDPF WS-E 49F custody (the flip's served number)
2. `data/mdpf/scripts/gold/validate_schwab_native_custody.py` -- leg-2 sanity gate (verified active-PASS on live 06-30 RPS)
3. `data/black_diamond/scripts/gold/A_03.positions_cube.py` -- BD positions cube
4. `data/black_diamond/scripts/gold/B_00.canonical_holdings.py` -- BD canonical holdings -> served AUA
5. `data/black_diamond/scripts/gold/B_01.holdings_lots.py` -- BD holdings-lots
6. `data/mdpf/scripts/feeders/wsd_partner_held_etf.py` -- partner_held_etf feeder
7. `data/etfs/scripts/gold/avgcap_bd_rps_recon.py` -- ETFS avgcap<->RPS recon
8. `infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py` -- 49F ETF-ownership Lambda
9. `infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily-canonical/lambda_function.py` -- canonical variant
10. `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py` -- RPS-freshness gate that triggers the MDPF EC2 chain

**Other served silver tables:**
- `acc` -> `build_schwab_bd_account_xref.py` -> `schwab/silver/account_xref` -> canonical dim builders (dim_account/relationship/advisor_role/advisor_fee) + `build_gold_partner_analytics`.
- `trn_nna` -> `C_01.canonical_nna.py` (via `lib/schwab_flows.py`) -> `D_00b.portal_timeseries` + `D_01.partner_analytics` -> **portal NNA surfaces**.
- `uln` + `rld` -> `B_02.canonical_lots.py` (RLD = primary realized-tax source) -> tax/lot gold.

*(Diagnostics/probes read `rps` ad-hoc; not recurring processes -- excluded from the freshness contract.)*

## 4. Re-point design (COO ask step 2)

The daily-delivery infra exists; the durability fix is to **wire PATH A's converters to run automatically daily off the daily-box raw**. Three components:

**C1 -- Automated daily silver-conversion trigger (the core).** Replace the manual `/49-schwab-conv` cadence with an automated daily runner that executes the 6 converters in order (sync -> acc -> rps -> trn -> trn_nna -> uln -> rld) after the daily raw lands. Two implementation shapes for the arch-gate to choose (Section 5, D-A):
  - a lightweight EventBridge-triggered EC2/SSM chain (mirrors the `canonical-schwab-runner` start-stop pattern), OR
  - fold the 6 converters into the existing SI2/canonical daily orchestration as an added stage.
  Idempotent + extend-from-last-date already (safe to run daily; a no-new-date day is a clean no-op).

**C2 -- Resolve the raw-source seam (dependency on 0.6.2_AE).** The SI2 box lands daily raw to `01_raw_quartz_validation/`; PATH A converters read `01_raw/`. Options: (a) land the HELD SI2->`01_raw/` repoint (gated on N=5 clean box-days -- 0.6.2's Andrew-Caution-B ruling), then rps/acc/uln/rld auto-pick-up; or (b) INTERIM: point the automated converters at `01_raw_quartz_validation/` until the repoint clears. **Recommend (a)** -- do not fork the converters' source prefix; coordinate with 0.6.2 on the N=5 clean-day gate + expedite if the durability need outranks the caution window (COO/Andrew call).

**C3 -- Fix the TRN Layer-A local-disk read (DS lane, the one code change).** `convert_schwab_trn_to_parquet.py` reads **local OneDrive disk** (`DEFAULT_SRC_DIR`), not S3 -- so a `01_raw/` repoint alone would NOT make TRN (or the chained `trn_nna` -> portal NNA) daily-fresh headless. Re-point it to read S3 `01_raw/` `CRS*.TRN`. **Prerequisite:** confirm SchwabAutoDownload delivers `CRS*.TRN` to S3 (open question for 0.6.2 -- Section 5, D-C). Rule-13 DS lane; a scoped converter edit + parity re-verify (silver output unchanged vs a manual run).

**Consumer impact: NONE.** All Section-3 consumers read the same `opal-data-bd/schwab/silver/*` keys -- they simply see fresher partitions. The MDPF leg-2 gate + `mdpf-daily-trigger` RPS-freshness gate then observe daily-fresh RPS (the leg-2 gate already tolerates it -- verified active-PASS 06-30). No re-deploy of any consumer.

## 5. Open decisions for the arch-gate

- **D-A (shape of C1):** dedicated EventBridge EC2/SSM converter-chain vs folding into the SI2/canonical daily orchestration. Trade-off: isolation + a clean owner (DS-triggered) vs reusing proven infra. CTO call.
- **D-B (C2 timing):** wait for the N=5 SI2->`01_raw/` repoint, or run the interim `01_raw_quartz_validation/` source. Depends on how fast the durability need must land vs 0.6.2's caution window. COO/Andrew + 0.6.2.
- **D-C (C3 feasibility):** does SchwabAutoDownload deliver `CRS*.TRN` to S3? If not, TRN Layer-A (-> trn_nna -> portal NNA) cannot go daily-headless via the box, and stays on the manual/local path until the SI2 download set is extended. 0.6.2 to confirm the box's downloaded file set.
- **D-D (build-vs-ride-SSOTMG):** since DATA_SSOTMG will eventually replace PATH A entirely (canonical-as-SSOT), C1's automation is a BRIDGE that retires at cutover. Justified because (i) the batch-lag is recurring NOW and (ii) the cutover is several-days-parity + never-widen gated (not imminent). Confirm the bridge is worth building vs accelerating the cutover for the rps-derived served surfaces. CTO+CVO.

## 6. Relationship to DATA_SSOTMG (no conflict)

- **This re-point = silver CADENCE** (make the currently-served PATH-A silver daily-fresh). **DATA_SSOTMG = silver SHAPE** (replace PATH A with the canonical custodian-native model, parity-gated never-widen cutover). Complementary layers; this one is a non-blocking bridge that de-risks the recurrence until the cutover lands. It touches no canonical code and no served-surface contract -- pure ingest-cadence automation + one converter source-fix.

## 7. Compiler Tools (evidence)

| Tool | Command | Finding |
|---|---|---|
| comp-grep / Explore | `schwab/silver`, `canonical/schwab`, `RPS_PREFIX` sweep | the ~15-consumer inventory (Section 3); portal has zero direct reads |
| Explore (ingest map) | `sync_schwab_onedrive_to_s3.py` + the 6 converters + EC2_MANIFEST | the two-path map + the lag-cause (no auto-trigger) + the TRN local-disk gotcha |
| EC2_MANIFEST / schedule.tf | `canonical-schwab-si2` / `canonical-schwab-runner` | SI2 lands to `01_raw_quartz_validation/` (repoint HELD N=5); canonical-runner reads `01_raw/` daily |
| DATA_SSOTMG_PRD | read | the SSOTMG cutover boundary (Section 6) -- this stays non-blocking |

---

*Enumeration + design only. No implementation until the CTO arch-gate. RAVC -> 2.0.0_SA_COO (CC 1.0.0_SA_CTO + 3.0.0_SA_CVO). Depends on 0.6.2_AE for C2/C3 (SI2 raw prefix + the box's TRN delivery set).*
