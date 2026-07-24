# MDPF Portal Lineage — Findings Briefing

**Author:** 2.0.0_SA_COO
**Date:** 2026-07-24 (~2030Z)
**For:** Andrew; cross-check by 3.0.0_SA_CVO (parallel trace) → CVO postmortem
**Status:** Findings, grounded. Fabric is PAUSED (Andrew-direct ~1943Z); this is read-only investigation only — no writes to AWS, no commits landed by me for this work.
**Purpose:** Establish, with evidence, where the MDPF data the portal renders actually comes from, and who wrote and ran the script that produced it. CVO to confirm alignment before writing the postmortem.

> **How to read this doc:** every load-bearing claim is tagged **[MEASURED]** (from live AWS, the HAR, or source `@HEAD`) or **[INFERRED]** (reasoned from measured facts, not directly observed). The reproduction appendix (§8) carries the exact keys, ETags, VersionIds, commits, and commands so CVO can re-derive each claim independently rather than take it from this relay.

---

## 0. The question

Andrew asked three things, in sequence:
1. Where does the MDPF data the current portal renders actually come from?
2. What script produced it, and how did it reach the served location?
3. Who created that script and who ran it (logs/commits, 07-23 / 07-24)?

The portal visibly shows **2026-07-22** data (confirmed by an Andrew HAR + a Cottonwood screenshot, tooltip `2026-07-22 / Total AUM $458M`, captured 2026-07-24 ~16:40 local). Andrew's hypothesis: an ad-hoc revamp run on 07-23 pushed data through, correctly serving the prior day (07-22), developed through the **`opal-data-assets` monolith lineage**. **This briefing confirms that hypothesis in full.**

---

## 1. Method / grounding stance

- **comp-tools first** (Andrew-direct ~1924Z), raw checks only to verify: `pipescript mdpf`, `comp-platinum page ModelPortfolios`, `comp-grep`. Raw `aws`/`grep` used only where a comp-tool did not fit, each with a `# rail-checked:` marker naming the call I ran and its output.
- **Ground truth = the browser HAR Andrew recorded** (`opalinvest.dev.har`), not code inference. A HAR shows exactly what the browser fetched and the exact origin object (ETag/Last-Modified from S3).
- **All keys, sizes, timestamps, ETags, VersionIds read from live AWS this session; all code read at `@HEAD`.** I did **not** rely on `pipescript`'s 39-day-old snapshot for any load-bearing key (it warns about its own vintage).

---

## 2. What the portal actually reads — HAR + ETag proof **[MEASURED]**

The browser (`opalinvest.dev`, ModelPortfolios page) fetches these, all via CloudFront `/api/general/mdpf/*`, all served **directly from S3** (`server: AmazonS3`):

| Request (`/api/general/mdpf/…`) | Origin object | HAR ETag | Last-Modified |
|---|---|---|---|
| `49financial/aggregate-aua-timeseries.json` | `opal-data-portal-v2/json/mdpf/49financial/…` | `501407448f554a77a7ff7e2a5dceb954` | 2026-07-23 21:47:06Z |
| `49financial/account-distribution.json` | `…/json/mdpf/49financial/…` | `959b5b4e633153fe45fc8e537bf825e6` | 2026-07-24 11:30:39Z |
| `inflection/aggregate-aua-timeseries.json` | `…/json/mdpf/inflection/…` | `e3c8db35d7bfedb15d0876eed6ffdbb4` | 2026-07-23 21:47:06Z |
| `cottonwood/aggregate-aua-timeseries.json` | `…/json/mdpf/cottonwood/…` | `194e5bb05c4523abb2cc05988f53005f` | 2026-07-23 21:47:07Z |
| `cottonwood/aum-metrics.json` | `…/json/mdpf/cottonwood/…` | `55b1f1a48e0089ec081798683ecca110` | 2026-07-23 04:04:42Z |

**Decisive test — ETag match:** for every request, the HAR ETag matches the live object in **`opal-data-portal-v2/json/mdpf/`** byte-for-byte. The candidate on the monolith — `opal-data-assets/gold/mdpf_revamp/{firm}/aggregate-aua-timeseries.json` (hyphen) — **404s**. An ETag is a content hash; a match is identity.

> **Conclusion:** the portal **reads** `opal-data-portal-v2/json/mdpf/`. It does **not** read the monolith `gold/mdpf_revamp/` prefix directly. **[MEASURED]**

---

## 3. The lineage — the served content IS the monolith revamp output **[MEASURED]**

The served files carry a self-describing provenance stamp written by their producer. From the live 49F `aggregate-aua-timeseries.json`:

- `meta.basis = "schwab-rps"`
- `meta.generated_at = "2026-07-23T21:43:50Z"`
- `as_of_last = "2026-07-22"` · `source_vintage_last.overall = "2026-07-22"` · `trading_days_behind = 1`
- `count_provenance = ["measured", …]` (all measured, not interpolated)
- `source_vintage_last.semantics = "TO-5 (b) **REVAMP-SILVER** honest provenance … the REVAMP's OWN consumed AUA-bearing sources (model_aua = **smartx aum_daily** [49F] / **eclipse fact_portfolios_full** [inf…])"`

**Cottonwood** (Andrew's screenshot): served `aggregate-aua-timeseries.json` has `as_of_last = "2026-07-22"` — exactly the tooltip date.

**The feeders named in the stamp are all `opal-data-assets` monolith silver** (`channel_sources.py:56-64`, `MONOLITH_BUCKET="opal-data-assets"`):
- `schwab/08242234/silver/fact_rps_s2` (49F custody)
- `smartx/platform/silver/fact_model_aum_daily` + `…/fact_model_allocation_roster` (49F model)
- `orion/inflection/silver/fact_assets`, `eclipse/inflection/silver/fact_portfolios_full` (inflection)
- `blackdiamond/cottonwood/silver/fact_holdings` (cottonwood)

> **Conclusion:** the served files are the **monolith revamp output**, content as-of 07-22, generated 07-23. The portal reads a **published copy on `portal-v2`**; the lineage is the `opal-data-assets` monolith. **Andrew's hypothesis confirmed. [MEASURED]**

---

## 4. The confound Andrew predicted — the dead legacy `platinum` path **[MEASURED]**

Andrew said "it cannot be 07-18 unless there is a confound on date provenance." There is, and this is it:

- `opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json` — **newest partition = 2026-07-18** (frozen at the INF-chain failure).
- The **legacy** serving path was: `mdpf_aggregate_aua.py` (WS-A) → `platinum/mdpf/…` → `build_aggregate_aua_timeseries.py` (reads `platinum`, writes `json/mdpf/`). That path **died 07-18**.
- `build_aggregate_aua_timeseries.py`'s docstring **still claims** it feeds `json/mdpf/` — but that code is **stale vs what actually ran** on 07-23. The ad-hoc revamp run bypassed it.

> This is precisely why my first-pass code trace (which followed the legacy docstrings) said "07-18 / frozen," while the live data is 07-22. **The 07-18 timestamp is a red herring: that path is dead, and it is not the serving path.** It is a code/reality drift trap for the next reader (row-19 class). **[MEASURED]**

---

## 5. Who wrote the script, and who ran it

### 5a. The producer script — **created by DS, 07-20** **[MEASURED]**

The served content was produced by **`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`** — fingerprinted decisively: the strings `REVAMP-SILVER`, `serve_real_D1`, `schwab-rps`, `count_provenance` exist in that file **and no other** under `data/mdpf/scripts`.

- **Creation commit:** `f4a4091823`, **2026-07-20 16:47:21 EDT**, author **`0.4.0_DS_ClientPlatform`**.
- Commit subject: *"feat(MDPF_REVAMP): TO-0 model crosswalk + TO-1 spine skeleton (49F, build-alongside)… **Spine skeleton reads monolith silver** (aum_daily day-col + roster basis + fact_rps custody), emits the served F4 shape."*
- The script itself only writes to a **local `--out-dir`** (arg at `:2017`; `--dry-run`/no-out-dir = no write, `:2077`). It does not PUT to `portal-v2` on its own.

**Distinct, do not conflate:** `channel_sources.py` (the four-channel re-source layer) was authored by **`0.7.0_AE_CloudOps`** (`d263bf93b2`, 07-23) — but that is the input layer for the **`opal-assets-daily-emitter` / DDB** path, which Andrew has explicitly set aside as a separate concern. The **portal serve** content comes from the DS gold producer above.

### 5b. Who ran it and published to the served keys — **DS, 07-23 evening** **[MEASURED, from the deploy ledgers]**

The scheduled pipeline writes only **staging** (`opal-data-assets/gold/mdpf_revamp/`). The writes to the **served** `portal-v2/json/mdpf/` keys were an **ad-hoc serve run by `0.4.0_DS_ClientPlatform`**, iterated through 07-23 evening.

> **CORRECTED after CVO cross-check (211344Z):** the cadence below is **49F-specific and does NOT describe every firm.** I generalized 49F's write times to all firms; that was imprecise. Measured per key: **49financial** = 18:49:04 · 20:57:16 · 21:47:06 (3 writes); **global** = 19:29:40 · 21:18:53 (2 writes, none at the 49F times). Both traces are right on their own key. See §11 for the resolution and why the difference matters (non-atomic serve).

Version history of `json/mdpf/49financial/aggregate-aua-timeseries.json`:

| Served-key write (49F) | Size | Corresponds to | Run by |
|---|---|---|---|
| 2026-07-18 15:01:52Z | 156,730 | last **legacy** nightly write | legacy chain |
| 2026-07-23 18:49:04Z | 171,643 | ledger `…1849Z_mdpf-allfirms-serve` (first revamp serve) | **0.4.0_DS_ClientPlatform** |
| 2026-07-23 20:57:16Z | 171,643 | interp-suppress / W-3b label bundle | 0.4.0_DS_ClientPlatform |
| **2026-07-23 21:47:06Z** | **183,004** | **W-7 count anchor** (`af0867e9`) — **the version rendered now** | 0.4.0_DS_ClientPlatform |

**The `1849Z` serve ledger** (`org/critical_paths/change_management/20260723T1849Z_mdpf-allfirms-serve_deploy_completion.md`):
- `OPENED: 2026-07-23T18:49Z by 0.4.0_DS_ClientPlatform`
- `AUTHORITY: CTO serve-fire 184804Z on COO clean counter-sign 184724Z + DE render evidence @5ae6762da` (never-widen co-sign satisfied: CTO+COO)
- `PATTERN: per key, staged-md5 assert → put → fresh-GET byte-compare → ListObjectsV2 key+size → served ETag cited`
- Served 6/6 keys byte-identical, each with size + ETag.

### 5c. Who pointed the portal renderer at these keys — **DT, 07-23** **[MEASURED]**

The portal DEV→PROD promotes that activated the Global view and pointed the renderer at the hyphenated `json/mdpf/*` keys were owned by **`0.2.0_DT_PortfolioAnalytics`** (COO relay/dispatch 194221Z), across `v2.1.145` → `v2.1.148`, 19:43Z–~22:15Z. The `21:47Z` served version pairs with the **W-7 count** promote (`v2.1.148`, ledger `…2215Z`).

**Two-trace confirmed (CVO 211729Z, at source — portal PROD merge history):** **`v2.1.145` = `5bc8be7e`** is the exact re-point commit, subject verbatim *"ACTIVATE MDPF Global view (cottonwood-inclusive) + **point renderer at json/mdpf/\* serving keys**"*, authored `0.2.0_DT_PortfolioAnalytics`. `v2.1.146` (`41ce41eb`), `v2.1.147` (`7ac7bafd`), `v2.1.148` (`17256834`, deployed PROD head pin `@343e7b2a`) — all DT-authored. §5c is no longer single-sourced.

---

## 6. Timeline (07-23, all Z) **[MEASURED]**

```
16:47 (07-20)  dim_mdpf_aggregate_aua_timeseries.py CREATED  (DS, commit f4a4091823) reads monolith silver
   …
07-23 evening  ad-hoc revamp serve run (DS), authority CTO serve-fire 184804Z + COO counter-sign 184724Z
18:49Z         first all-firms serve -> portal-v2/json/mdpf/*   (ledger 1849Z, DS)
~19:29Z        global re-stage (frontier 07-22 = $1,951,676,164.42)
19:43-20:05Z   portal promote v2.1.145 (DT) — renderer points at json/mdpf/*
20:20-20:57Z   interp-suppress + W-3b label bundle re-serve (DS) + promotes (DT)
21:43:50Z      producer generated_at of the CURRENT served file (W-7 count build)
21:47:06Z      CURRENT served version written -> what the portal renders now (as_of 07-22)
~22:15Z        W-7 count promote v2.1.148 (DT)
```

---

## 7. Separate thread, so CVO can reconcile cleanly

`account-distribution.json` (49F/inf) has a **different, fresher** writer — Last-Modified **2026-07-24 11:30:39Z**, distinct from the 07-23 evening aggregate serve. Grep points to a smartx-pipeline path (`compute_per_firm_account_distribution.py`, "CF rewrite `/api/general/*` → `json/mdpf/{firm}/account-distribution.json`"). **Andrew's screenshot is the "Daily AUM Analysis" chart = `aggregate-aua-timeseries.json`** (the DS revamp serve). The account-distribution write is a **separate serving thread** and should be traced independently before the postmortem treats the two as one. **[MEASURED that they differ; the account-dist writer is INFERRED from grep, not confirmed at its run.]**

---

## 8. The publish *mechanism* is a DS procedure, not a committed script — **[SOURCE-CONFIRMED via the DS 07-23 log, CVO 211344Z]**

I proved the **producer** (DS gold script) and the **serve authorship** (DS ran the puts; ledger-documented, byte-verified per key). I did **not** find a *committed* serve/publish script that PUTs to `portal-v2/json/mdpf/` — and CVO's pull of the DS log confirms there is none; it was a hand-run procedure:

- The `1849Z` ledger documents the serve as a **procedure** (`staged-md5 → put → GET-verify`), i.e. a DS-run put, **not** a named checked-in script.
- **DS 07-23 log** `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-07-23/p1_broken_charts_a2_serve_perfirm_counts.md` (CVO-pulled) shows the serve was **iterative, corrective, per-key manual puts/copies**, byte-verified each — e.g. global's 21:18:53 write was a **corrective byte-copy** of `55a8b379 → /global/` after DE's parity gate caught a W-7 count artifact published to the wrong key; per-firm 21:47:06 was a **separate** count-defect fix (`@3efc9dc6d`). Confirms: a documented DS procedure, **not** a committed script.
- The committed publisher (`opal-assets-mdpf-portal-publisher`) copies **within `opal-data-assets`** (`gold/mdpf_revamp/` → `json/mdpf/` on the *monolith*, `copy_object(Bucket=BUCKET, CopySource={Bucket:BUCKET})`, `BUCKET=opal-data-assets`) as a **build-alongside for a future CloudFront cutover** — it explicitly "does not re-point until that cutover." **It is NOT what wrote the live `portal-v2` keys.**
- CloudTrail S3 **data events are OFF** (PutObject principal lookups returned empty); writer identity comes from **ledger + version history + the DS log**, which is sufficient — CloudTrail was never needed.

---

## 9. What this implies to implement / clean up — **candidates, surfaced not adjudicated**

(These are for CVO's postmortem + CTO's routing to own. I am recording, not ruling.)

1. **The live serve is a MANUAL ad-hoc procedure, not a scheduled or committed path.** There is no durable production path that writes the served `portal-v2/json/mdpf/*` from the monolith lineage — it was hand-run. This is the exact shape of the amended **NEVER#4** ("a production pipeline must have a schedule"). The MDPF_CHANNEL_INDEPENDENCE program (closure rows, esp. row 10 scheduled floor + the migration rows) is the work that fixes it.
2. **Two serving locations / an unfinished cutover.** The committed publisher writes `opal-data-assets/json/mdpf/` (build-alongside), while the live portal reads `opal-data-portal-v2/json/mdpf/`. The cutover from portal-v2 to the monolith serve is **not done**; the migration (Andrew ~1832Z: "migrate MDPF to the monolith ENTIRELY") is what converges them.
3. **Code/reality drift is a live trap.** `build_aggregate_aua_timeseries.py` reads the dead `platinum/mdpf/` path and its docstrings still claim to feed `json/mdpf/`. A reader (or a scheduled re-enable) that trusts that code would serve 07-18 data. This is closure **row 19**'s class (a check/instrument whose scope silently differs from reality).
4. **The account-distribution serve is a separate, unverified thread** (§7) — trace it before the postmortem unifies the two.
5. **Instrument gaps found en route** (for CTO's gate, already routed): `comp-which` mis-routes an mdpf lineage question to a `bd|inf|cot`-only tool (a *wrong answer*, not a silence); `pipescript --resource` has no mdpf thread and answers from a 39-day snapshot; the I/O model does not represent `SERVED_BUCKET` (`portal-v2`) reads at all, so self-referential reads are invisible to `comp-pipescript io` on every tree.
6. **The serve is NON-ATOMIC across artifacts — the single most concrete implementation requirement (CVO 211344Z).** Because the 07-23 serve was iterative per-key hand-puts, the **currently-served global (`55a8b379`, from the 20:55 gold generation) is an OLDER gold build than the currently-served per-firm (from the 21:44 generation)** — ~52 minutes and one gold generation apart. CVO verified they still reconcile numerically (residual sweep clean but for the known +92 frontier), so **it is not a data defect** — but it is a fragile pattern. **The eventual scheduled publisher must be ATOMIC across all four artifacts from ONE gold generation in ONE run.** **Do NOT re-serve/re-run to reconcile the skew** — it reconciles numerically and the fix is the atomic publisher, not another hand-run (CVO explicit).
7. **The publish is unscheduled on the COMPLETE surface (CVO 211344Z):** nothing schedules it across EventBridge *Rules* **and** EventBridge *Scheduler* (a separate service that `list-rules` cannot see). Confirms §9.1 on both surfaces.

---

## 10. For CVO — alignment checklist

Please confirm your parallel trace agrees on each, or flag divergence:

- [ ] Portal reads `opal-data-portal-v2/json/mdpf/` (ETag identity, §2), **not** the monolith directly.
- [ ] Served content is monolith `REVAMP-SILVER` lineage, as_of 07-22, generated 07-23 (§3).
- [ ] The `07-18 platinum` path is the dead legacy confound (§4).
- [ ] Producer script = `dim_mdpf_aggregate_aua_timeseries.py`, created by `0.4.0_DS_ClientPlatform` @`f4a4091823` on 07-20 (§5a).
- [ ] Serve run + published by `0.4.0_DS_ClientPlatform`, authority CTO serve-fire 184804Z + COO counter-sign 184724Z, three iterations 18:49/20:57/21:47Z (§5b).
- [ ] Renderer pointed at `json/mdpf/*` by `0.2.0_DT_PortfolioAnalytics` promotes v2.1.145–148 (§5c).
- [ ] The publish *mechanism* is a DS-run procedure, not a committed script; CloudTrail data events off (§8).
- [ ] Divergences, if any, on the account-distribution writer (§7).

Where our two traces disagree, treat **the disagreement itself as a finding** — that is where the lineage record is weakest.

---

## 11. Cross-check reconciliation with CVO (parallel trace, 211344Z)

CVO independently traced this and cross-checked every load-bearing claim **at source, not from my relay.** Result: **ALIGNED on all 8 checklist items**, reached by partly different methods (the strongest form of alignment). Recorded here so the postmortem inherits the reconciled state.

- **§3 lineage — confirmed by a SECOND independent route.** I proved monolith `REVAMP-SILVER` lineage via the in-file provenance stamp; CVO proved it via **ETag identity between the served objects and specific monolith gold *versions*** (`list-object-versions`). Two routes, one conclusion.
- **§4, §5a, §5b, §7, §8 — verified exact** at source by CVO (git creation commit, the `1849Z` serve ledger, the DS 07-23 log, the account-distribution writer + 07-24 11:30Z timestamp).
- **§5c (DT promote lane) — NOW TWO-TRACE CONFIRMED (CVO 211729Z).** CVO took the one open verification at source (portal PROD merge history): **`v2.1.145 = 5bc8be7e`** is the exact re-point commit ("point renderer at json/mdpf/* serving keys"), DT-authored; v2.1.146/147/148 likewise. The earlier single-sourced caveat is **retired** — see §5c.
- **The one divergence (now resolved):** my §5b cadence was **49F-specific**; global writes at 19:29:40 / 21:18:53, not the 49F times. The DS log resolves it (above, §8) and it surfaces the **non-atomic serve** finding (§9.6).

> **STATE OF THE MERGED RECORD (CVO 211729Z): every load-bearing claim is now ETag/source-proven or two-trace-confirmed. NO single-sourced claims remain.** Cross-check closed clean; nothing further owed between COO and CVO on lineage.

**CVO's specificity additions, folded in:**
- **Hyphen vs underscore keys** (so no one conflates): monolith **STAGING** = underscore `aggregate_aua_timeseries.json` (exists; ETag-matches the served object — CVO's lineage proof key); portal **SERVE** = hyphen `aggregate-aua-timeseries.json`; the publish **renames across the two**. My §2 correctly shows the monolith *hyphen* key 404s; CVO's proof uses the monolith *underscore* key. Both true, different keys.
- **Cottonwood descends from the `_interpolated` gold variant** specifically — `gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries_interpolated.json` — while the other three descend from the plain underscore key. Adds specificity to §3.

**Ownership of the postmortem:** CVO will fold this briefing + their trace into one postmortem record with both authorships credited, once Andrew lifts the write-hold. No re-serve/re-run to reconcile the gold-gen skew (§9.6).

---

## Appendix — reproduction (exact, read-only)

**Read path (HAR ETag ↔ live object):**
```
aws s3api head-object --bucket opal-data-portal-v2 --key json/mdpf/49financial/aggregate-aua-timeseries.json --query '[ETag,LastModified,ContentLength]'
  -> "501407448f554a77a7ff7e2a5dceb954"  2026-07-23T21:47:06Z  183004
aws s3api head-object --bucket opal-data-assets --key gold/mdpf_revamp/49financial/aggregate-aua-timeseries.json
  -> 404 Not Found   (monolith hyphen key does not exist; portal does not read it)
```

**Served-key version history:**
```
aws s3api list-object-versions --bucket opal-data-portal-v2 --prefix json/mdpf/49financial/aggregate-aua-timeseries.json
  latest VersionId UahmCwsDRvQ1F73aBhnowC5Mm62YWu8S  2026-07-23T21:47:06Z  183004  IsLatest=true
  … 20:57:16Z … 18:49:04Z … 2026-07-18T15:01:52Z (legacy)
```

**Producer fingerprint & creation:**
```
comp-grep "REVAMP-SILVER" data/mdpf/scripts   -> data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py (unique)
git log --diff-filter=A -- data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
  -> f4a4091823 | 2026-07-20T16:47:21-04:00 | 0.4.0_DS_ClientPlatform | feat(MDPF_REVAMP): TO-0 … reads monolith silver
```

**Monolith feeders (lineage):** `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/channel_sources.py:56-64` (`MONOLITH_BUCKET="opal-data-assets"`, `fact_rps_s2` / `fact_model_aum_daily` / `fact_portfolios_full` / `fact_assets` / `fact_holdings`).

**Serve authorship:** `org/critical_paths/change_management/20260723T1849Z_mdpf-allfirms-serve_deploy_completion.md` (`OPENED … by 0.4.0_DS_ClientPlatform`, `AUTHORITY: CTO serve-fire 184804Z … COO counter-sign 184724Z`).

**Portal promotes:** ledgers `20260723T1943Z_mdpf-global-view-activate-promote`, `…2020Z…`, `…2052Z…`, `…2215Z…` (`Owner: 0.2.0_DT_PortfolioAnalytics`).

**Publisher (build-alongside, NOT the live writer):** `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py:27-89` (`BUCKET=opal-data-assets`, same-bucket `copy_object`).

*— 2.0.0_SA_COO, 2026-07-24*
