# NFRA_ENDPOINTS close, inf value-parity false-positive fix, 49F freeze diagnosis + tie-target pre-stage — 0.4.0_DS_ClientPlatform~A

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, COORDINATE, EXPLORE, VALIDATE

**Date:** 2026-07-09
**Task Order:** NFRA_ENDPOINTS.TO-2/TO-3 (SmartX/Schwab) + ad-hoc P0 (inf value-parity) + ad-hoc P0 (49F frozen-AUA) + 49F value-parity tie-target
**Status:** COMPLETE (NFRA_ENDPOINTS, inf parity fix) / HANDED-OFF (49F freeze-root) / READY-GATED (49F tie-target)

---

## Objective

Close out the NFRA_ENDPOINTS vendor-catalog initiative (SmartX + Schwab, the last two of four vendors); then, live-dispatched mid-session, triage and root-cause a P0 hourly-firing inf value-parity alarm; then a second live dispatch, root-cause a 49F served-AUA correctness question that pivoted into a genuine frozen/stale-serve finding.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript io | `io INF_D_04` | PASS | I/O manifest for the inf platinum producer — confirmed `header_metrics.json` as a terminal write, surfaced the full upstream input list |
| comp-pipescript io | `io INF_C_01` | PARTIAL | Returned reads/writes but `WRITES: (none detected)` — the f-string-keyed S3 write wasn't statically detected; had to trace the output key by reading the script directly |
| comp-pipescript io | `io C_02` | PASS | Confirmed the BD C_02→D_00 write chain (`CLIENT_PERFORMANCE`, `aua_certification_key`) and its consumers |
| comp-pipescript deployed | `deployed INF_C_01` | FAIL (wrong scope) | Defaults to the `opal-data-bd` code-bucket comparison; returned "No scripts matched filter" for an inf script. Not useful for an inf deployed-vs-repo check as invoked; didn't retry with a firm flag given time pressure — fell back to direct S3 checks |
| comp-freshness | `inf` | PASS | Decisive: flagged `inf_platinum_header_metrics`/`dashboard` WARN with the exact `worst dim 'nna' as_of 2026-07-06` detail that anchored the NNA staleness finding, and `inf_silver_aum_snapshot` N/A that (correctly) turned out to be a red herring, not the AUA mechanism |

**What worked:** `comp-freshness inf` was the single highest-leverage call all session — it handed both the inf AUA per-dim staleness signature AND the NNA lag in one table, no manual S3 archaeology needed to find WHERE to look next.
**What failed:** `comp-pipescript deployed` needs a firm-scoping flag (or better error messaging) — it silently assumed BD/49F's code-bucket for an inf script name instead of erroring clearly on firm mismatch; cost a few minutes of confusion before falling back to raw `aws s3 ls` (rail-marked).
**Gap found:** no comp-tool answers "which script actually writes S3 key X" when the write is behind an f-string/computed key (`io` under-reports writes in that case) — had to Read the script directly both times (INF_C_01, and implicitly for the BD chain). Worth a coverage note for whoever owns comp-pipescript's static analyzer.

Compiler-tools-log line appended below.

---

## Work Completed

### 1. NFRA_ENDPOINTS.TO-2 (SmartX retrofit) + TO-3 (Schwab file-feed assessment) — CLOSED

Built `data/smartx/API/` to the canonical `domains/{d}/endpoints/payloads/` shape (3 domains: model-api, performance, compliance-graphql), relocated `sxpl_restin_probe.py` into `tools/`. Found + corrected a real staleness gap: the pre-existing `QUICKSTART.md`/`QA_ENVIRONMENT.md` described a QA-bootstrap auth model (`ids.svc.qa.smartx.us`) with zero live-code references, superseded by the real production integration — applied the errata pattern (supersession notices, not deletion). `data/smartx/**` is a `SHARED_OPAL_ETL` owned-paths lane (AE-only) — discovered this only at commit time (the gate doesn't fire on Write/Edit); handed the commit to 0.5.0_AE_OpalETL rather than bypass (landed `2837f033e`). CVO caught one real overstatement in my own wording post-commit ("zero references" to `opal/smartx/qa-models` was false — the secret is still active, used by migration tooling + the catalog's own test scripts) — corrected to "no production-pipeline consumer" across 5 files, landed by 0.5.0 as `8c5a3e885`.

Schwab: ratified the FILE-FEED variant (no REST surface exists). The real finding: `data/schwab/`'s 2025-11-14 docs describe a Snowflake+Lambda-fanout warehouse that was **never built** (zero live CloudFormation stacks) — the actual shipped architecture is S3+Python bronze/silver, documented in the CTO-accepted D1 spec. Rewrote `README.md` as the grounded entry point, added supersession notices to the four historical docs, committed `505940947` (POD4 lane, no gate friction — checked ownership up front this time per COO's explicit ask after the SmartX blocker).

CVO certified all 4 vendor catalogs (BD/Orion/SmartX/Schwab) grounded-claims PASS; CTO's completeness gate PASSED (live-verified the Eclipse fold). NFRA_ENDPOINTS is closed.

### 2. inf value-parity phantom $1.44M divergence — P0, ROOT-CAUSED + FIXED + VERIFIED

COO dispatched a live P0: `opal-inf-value-parity` firing hourly since 2026-07-06T17:16:36Z, served AUA "$1.44M below source." Triage: confirmed UNATTENDED (60h continuous fire, zero remediation ticket) via CloudWatch log timestamps (PowerShell, not Bash — the leading-`/` log-group name mangles under Git Bash path conversion).

Mechanism, grounded byte-exact:
- Anchor is `silver/api_dims/positions_mv/snapshot_date={date}/data.parquet` (confirmed fresh).
- Served `header_metrics.json` `total.aua` (202,246,989.07) exactly equals BOTH `holdings_2026-07-08.parquet.market_value.sum()` and `positions_mv/snapshot_date=2026-07-08.current_value.sum()` — the served value is **correct for 07-08**, not wrong.
- The guard (`infra/aws/compdiff/value_parity_reader.py`, built 06-30) resolves its anchor via `data_as_of` literally as the raw Orion partition key. A 07-02 fix (`_orion_vendor_asof.py`'s `orion_normalize_as_of`, sealed, CTO arch-gated) changed what `data_as_of` means (shifted -1 NYSE trading day) without the guard being updated — a cross-team temporal-coupling gap. The July-4-weekend compression finally pushed the fixed 1-day offset past the zero-tolerance epsilon on 07-06, the first post-holiday trading day.

Initially proposed fixing this in `value_parity_reader.py` directly (a hardcoded inverse shift); pushed back on my OWN plan before shipping when I realized reverting INF_D_04's normalization would regress the sealed 07-02 fix. CTO ruled in favor of my pushback (fix belongs in the guard, INF_D_04 holds) and set two conditions: share the calendar via genuine import (not a duplicated copy), and ground the firm-scoping (don't assume from names). Added `next_trading_day()` to the canonical `_orion_vendor_asof.py` (commit `9696ed88d`, my own lane, pure-additive) and designed a Terraform `archive_file` `source{content=file(...)}` block to bundle it live into the inf-only Lambda zip. Grounded firm-scoping by grep: exactly 5 inf gold scripts import the Orion calendar, zero in cot/bd.

0.8.0_AE_CloudComp applied (after an initial ~40min silent-wedge on their end, resolved by MSTR respawn): reproduced the root cause byte-exact offline before touching Terraform, found and fixed two real corrections to my draft (the `source`/`source_dir` Terraform incompatibility, and a path-depth-off-by-one), and proved the fix on a **real scheduled EventBridge invoke** (07:16:36Z fired=True/exit=1 before → 08:16:24Z fired=False/exit=0 after). Ledger closed GREEN 7/7. Commits `c9e42d485` (fix) + `b210835f9` (ledger).

**Bonus finding from the apply:** `opal-49f-value-parity` was never actually deployed (TF written, cert-mode ready, never applied) — 49F has had zero automated value-parity detection this whole time, which connects directly to Work Unit 3 below.

### 3. 49F frozen-AUA discovery + freeze-root diagnosis + tie-target pre-stage

Dispatched to re-determine the 49F value-parity tie-target (CTO: `gold_aua` — C_02's account-derived total_aua — is structurally ~5% off positions, an exact tie cries wolf every run; decomposition-reconcile is the lean). Pulling live numbers to verify CVO~B's cited figures ($1.743B/$1.650B) surfaced a bigger problem: the actual **served** `platinum/firm/header_metrics.json` AUA ($1,837,159,865.68) didn't match either CVO~B's numbers or my own live pull — traced it to `D_00.portal_aggregates.py`'s `DEGENERATE_CERT_MODE='hold'` (Andrew-ruled, correctly refusing to serve a $0 degenerate cert) serving a **frozen historical certified_aua** because `silver/allocations` has been degenerate.

Root-caused the freeze: confirmed via the raw upstream feed (not just our processing code) that BD's original Playwright-scrape export died 06-19 (SS&C MFA, a known incident). First-pass conclusion ("nothing since 06-18") was **incomplete** — caught my own truncation error (read only the last ~15 lexicographic S3 entries) and re-pulled the full 119-file listing, which revealed ADVI_BDAPIMIG's REST-bypass restoration under a new filename convention (`ALLOCATIONS_DAILY_*`) landed 06-24 and has been running **intermittently** since — full files some days, empty 4.5KB stubs others, with the **last 5 straight days (07-05 through 07-09) all empty, no self-heal**. Corrected this before it reached CTO framed as "known dormant issue, nothing to chase." Handed the live-failure diagnosis to the ADVI_BDAPIMIG owners (0.6.0_AE_PartnerETL / 0.7.0_AE_CloudOps~A) per COO — not my lane to dig into their REST/cookie internals.

Also caught and owned a **basis error** in my own severity figure: I'd computed "$185M/11% overstated/~3wk" by subtracting a certified_aua-type value (the held figure) from a raw total_aua value (gold_aua) — different bases, which conflates staleness with the separate structural gold_aua-vs-cert gap. 0.6.0's same-basis comparison (cert-vs-cert across the time gap) correctly isolated staleness alone: $6.86M/0.372%/7 days. Struck my figure from the record on COO's ask, confirmed the tie-target brief never referenced it (grep-verified, zero hits).

Pre-staged the tie-target design (`docs/briefs/49f-value-parity-tie-target-design-20260709.md`, `d5d3ab305` + `ed95c78ae`) per COO's ask so turnaround collapses once the freeze clears. While pre-staging, found the original E_00/E_05/E_07-reuse lean doesn't fit as-is: those scripts decompose gold-POSITIONS vs SILVER-allocations (the same frozen feed), not gold_aua vs positions — a different pair. Traced gold_aua's real construction (`B_03.account_gains.py:222` → `C_00` → `C_02`) to a pure holdings-market-value sum joined against `accounts_dimension` downstream, reframing the likely gap driver as account-coverage, not cash/valuation-timing. Folded in CTO's (a)-vs-(b) demonstration steer: a genuine decomposable timing/valuation gap gets a tolerance (legitimate); an accounts_dimension coverage gap gets reconciled, not tolerated (the same anti-pattern as widening a threshold to silence a true positive). Demonstration runs live post-gold (~04:00Z 2026-07-10) on real un-frozen data.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Fix the inf value-parity guard's anchor resolution, NOT `INF_D_04`'s date normalization | INF_D_04's shift is a sealed, CTO-arch-gated 07-02 correctness fix serving other consumers (WS-4 AC-2 per-dim vintages); reverting it would regress a real fix and just relocate the mismatch. Pushed back on COO's initial "ship it, your lane" ACK before shipping; CTO ruled in favor after independent verification at source. |
| Share the Orion trading-day calendar via a genuine Terraform `archive_file` `source{content=file(...)}` import, not a duplicated copy in `value_parity_reader.py` | CTO's explicit condition: a duplicated `NYSE_CLOSED_DATES` set re-arms the exact temporal-coupling gap that caused this incident the next time the calendar changes. |
| Scope `VP_ANCHOR_DATE_SHIFT` to inf only, not cot/49f | Grounded by grep: `orion_normalize_as_of`/`_orion_vendor_asof` imported by exactly 5 inf gold scripts, zero in cot/black_diamond; the module's own docstring states Orion-only, never call on Schwab/BD-sourced labels. |
| Hand the ADVI_BDAPIMIG live-failure diagnosis to its owners rather than dig into the REST/cookie internals myself | COO's explicit lane call: I have the S3-side grounding (the handoff artifact); the API/cookie-path context is theirs. |
| Strike my own $185M/11% severity figure rather than defend it | It compared different bases (held certified_aua vs raw total_aua/gold_aua), conflating staleness with the separate structural gap the tie-target work exists to measure. 0.6.0's same-basis comparison is the accurate one. |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Schwab file-feed retrofit + Snowflake-plan supersession | `data/schwab/README.md` + 4 supersession notices + `data/schwab/findings/README.md` | CTO/COO, NFRA_ENDPOINTS closure |
| NNA/INF_C_01 staleness handoff | `docs/briefs/advi-infref-nna-c01-staleness-handoff-20260709.md` | ADVI_INFREF durable-fix owner (Andrew-gated decision) |
| 49F value-parity tie-target design (pre-staged, 2 commits) | `docs/briefs/49f-value-parity-tie-target-design-20260709.md` | CTO (gate), 0.6.0/CVO~B (demonstration) |

Next Steps must name the receiving agent — see below.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/smartx/API/**` (12 files) | Domains/endpoints/payloads retrofit + errata | Yes — `2837f033e` (0.5.0, lane-owned) |
| `data/smartx/API/{README,QA_ENVIRONMENT,findings/README}.md` + 2 testing docs | Precision-fix "zero references" → "no production consumer" | Yes — `8c5a3e885` (0.5.0) |
| `data/schwab/{README,INDEX,DATA_DICTIONARY,SNOWFLAKE_SCHEMA,AWS_SNOWFLAKE_ARCHITECTURE}.md`, `findings/README.md` | File-feed retrofit + Snowflake-plan supersession | Yes — `505940947` |
| `data/inf/scripts/silver/_orion_vendor_asof.py` | Added `next_trading_day()`, the inverse of `prior_trading_day` | Yes — `9696ed88d` |
| `infra/aws/compdiff/value_parity_reader.py`, `infra/aws/terraform/inf-value-parity/inf_value_parity.tf` | Anchor-date-shift fix (drafted by me, applied + corrected by 0.8.0) | Yes — `c9e42d485` (0.8.0) |
| `org/critical_paths/change_management/*` | Deploy ledger, opened + closed 7/7 | Yes — `b210835f9` (0.8.0) |
| `docs/briefs/advi-infref-nna-c01-staleness-handoff-20260709.md` | New handoff brief | Yes — `c5172830e` |
| `docs/briefs/49f-value-parity-tie-target-design-20260709.md` | New design brief, revised with CTO's (a)-vs-(b) steer | Yes — `d5d3ab305`, `ed95c78ae` |

---

## Blockers

None open. The 49F tie-target demonstration is GATED (not blocked) on 0.6.0_AE_PartnerETL's ADVI_BDAPIMIG freeze-root fix, scheduled to clear post-gold ~04:00Z 2026-07-10 — evidence: 0.6.0 actively grounding it live (COO's 092741Z sync cited 0.6.0's own root-fix ground-truth work in progress).

---

## Current State

NFRA_ENDPOINTS is fully closed (4/4 vendors, CVO-certified, CTO completeness-gate PASSED). The inf value-parity phantom-divergence is fixed and verified live (`opal-inf-value-parity` now `fired=False` on real scheduled invokes; ledger `b210835f9` closed 7/7). `opal-49f-value-parity` is confirmed never-deployed (TF written, unapplied) — a real detection gap, named but not yet actioned (sequencing: freeze-fix → tie-target demonstration → then apply). The 49F served AUA is currently a stale hold via `DEGENERATE_CERT_MODE='hold'` (Andrew-ruled, working as designed) pending BD's allocation feed restoration; the tie-target design (`d5d3ab305`/`ed95c78ae`) is fully ready to execute the moment live data returns — no further design work needed, only live-data execution of the demonstration plan's steps 1-5 with the (a)-vs-(b) routing.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL]** Land the ADVI_BDAPIMIG freeze-root fix (why the REST-bypass allocation pull has returned empty 5 straight days) — my S3-side diagnosis is the handoff artifact, theirs to execute.
2. **[0.4.0_DS_ClientPlatform~A]** Once live data returns (~04:00Z 2026-07-10 or later), run the tie-target demonstration plan against `docs/briefs/49f-value-parity-tie-target-design-20260709.md` steps 1-5; report the (a)-vs-(b) split to CTO for the gate ruling.
3. **[1.0.0_SA_CTO]** Rule on applying `opal-49f-value-parity` (8 unapplied Terraform resources) once the tie-target is demonstrated sound — sequenced after, not before, per my note in the joint RAVC with 0.8.0.
4. **[0.4.0_DS_ClientPlatform~A]** No action pending on the NNA/INF_C_01 staleness thread beyond watching the scheduled 2026-07-09 nightly run for the structural-vs-one-off signal (no ad-hoc trigger) — the handoff brief stands.
