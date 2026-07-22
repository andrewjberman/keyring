# MDPF_3FIRMS 3F-P1 + 3F-P2 read-only audits delivered — 0.4.0_DE_ClientPlatform

**Date:** 2026-07-22
**Task Order:** MDPF_3FIRMS.3F-P1 + MDPF_3FIRMS.3F-P2 (COO GO 20260722T203302Z)
**Status:** COMPLETE (both TOs, single session ~20:26Z-20:50Z)

---

## Objective

Fresh spawn on the MDPF_3FIRMS dispatch (lane 4 of COO's 202236Z spawn request). Execute both WS-P read-only audits in parallel: 3F-P1 (consumption contract — every rendered MDPF-page aggregate mapped to served-artifact-vs-FE-computation locus) and 3F-P2 (endpoint/route audit — two URL families, 9 declared-not-live behaviors, null-on-404 wrapper).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-transform | `schema-check ModelPortfolios` (P1 ph1) | WARN | "no types.ts found near ModelPortfolios.tsx" — types live in portal-proxy.ts/endpoints/aum.ts; no rendered-field inventory produced. vs expect: MISS (no inventory) — denominator taken from full-file walk instead |
| comp-transform | `fields ModelPortfolios` (P1 ph1) | PARTIAL | returned 7 field paths of the >=40 actually bound (missed all mdpf/per-firm/benchmark/peer hooks). vs expect: MISS — denominator stated manually per if_mismatch: **22 of 22 rendered aggregates, 9 of 9 hooks** |
| comp-platinum | `page ModelPortfolios` (P1 ph1) | PARTIAL/FAIL | traced 2 of 9 fetches; resolved getAccountDistribution to the commented-out `/api/private/` TODO (aum.ts:517) not the live `/api/general/` call (:552) — docstring-read defect, recorded as instrument finding F-4. (`page model-portfolios` = "Component not found") |
| comp-blast | `aum-timeseries.json` / `aum-metrics.json` (P1 ph2) | PARTIAL | consumer blast radii + incident RISK/HOLD pointers; producers resolved via pipescript + comp-grep instead. vs expect (producer named): met via pipescript |
| pipescript | `model-portfolios`, `mdpf`, `--resource aum-timeseries/mdpf/smartx` | PASS | producers grounded: mdpf_aggregate_aua.py on mdpf-daily-runner EC2 (mdpf thread), yang-model-portfolio-benchmarks / yang-generate-etf-returns / yang-generate-peer-performance (model-portfolios thread). Page spans TWO named threads |
| comp-routes | `behaviors` (P2 ph1, REQUIRED-first) | PASS | 25 rows (24 ordered + `/*` default); both MDPF families -> behavior `/api/general/*` -> S3-opal-data-portal-v2-json + 3-lambda edge chain |
| comp-routes | `trace <url>` x14 endpoints (P1 ph2 + P2 ph1) | PASS (with instrument caveats) | all 14 resolve to behavior 18, zero orphans. Gotchas: bare `/api/...` arg MSYS-mangles (fix: `MSYS2_ARG_CONV_EXCL="/api"`); blanket `MSYS_NO_PATHCONV=1` breaks the launcher's internal python path; `trace ModelPortfolios` found only 4 of 9 calls + same /api/private docstring mis-read |
| aws (rail-checked per TO ph2) | `cloudfront get-distribution-config --id EVTSA9VEHNZVH` | PASS | APPLIED truth: **24 behaviors / 7 origins / ZERO mdpf-portfolios patterns / CustomErrorResponses=0 / no assets origin**. vs expect: exact match, no escalation |
| comp-grep / comp-glob | writer greps for the 4 legacy keys + publisher dir | PASS | producers pinned: compute_account_distribution.py:81, compute_per_firm_account_distribution.py, build_legacy_compat_emit.py:54-55 ("sole SoT"), SmartX exporter (SMARTX_BIBLE.md:291) |
| comp-transform + comp-routes | ph3 re-runs post-commit | PASS | byte-identical outputs; portal + infra footprint zero (read-only honored) |

**What worked:** pipescript (producer grounding, two-thread discovery), comp-routes behaviors + live CF primitive as the 22a pair, comp-grep writer-pinning.
**What failed:** comp-platinum/comp-routes URL resolution reads the commented-out `/api/private` TODO as the live URL (F-4, flagged); comp-transform fields' extractor misses columnar/per-firm hooks (7 of >=40).
**Gap found:** no comp-tool renders "which S3 key does a FE URL resolve to under public-data-router rewrite" — hand-derived from the rewrite rule each time.

Appended to org/compiler-tools-log.md this session.

---

## Work Completed

1. **Startup:** /watcher armed (Monitor task bgx2tt6ts, persistent; no orphan found — serial was NOT REGISTERED, ps clean), LD-0290 serial file written, registered PID 12996. COO 181636Z ACK read (un-strike QUEUED behind hold — COO-owned, nothing owed). ACK'd spawn to COO 202906Z; GO received 203302Z; both TO files read.
2. **3F-P1 delivered:** `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/MDPF_3F_P1_CONSUMPTION_CONTRACT_AUDIT_20260722.md` @ `39ea5916e`. Complete locus table, denominator 22/22 aggregates + 9/9 hooks + 10/10 producers (zero UNKNOWN PRODUCER). Verdict on Andrew's "all client-side": **MIXED per-aggregate** — artifact layer fully served; **7 FE-computed GLOBAL number classes flagged for 3F-P5**, headline: **the Global trend aggregate as RENDERED is FE-summed (ModelPortfolios.tsx:724-731 @ 08c6d8b2) despite served `model_aua` in the same artifact** — refines PRD §2.4's "server-composed" (true of the artifact, not the rendered number).
3. **3F-P2 delivered:** `.../MDPF_3F_P2_ENDPOINT_ROUTE_AUDIT_20260722.md` @ `39ea5916e`. Premise CONFIRMED at applied truth (24/7/zero — **no escalation triggered**); 14/14 endpoints -> behavior 18, zero orphans; 9 declared behaviors mapped 1:1 to PUBLISH_MAP keys + producers, all confirmed not live; portal-auth drift recorded EXPECTED, zero TF touched. **F-1: the declared flip set has NO Cottonwood paths — `mdpf_assets_behavior_paths` (cloudfront-distribution.tf:77-87) is an 8th hardcoded firm-enumeration absent from PRD §3.3's registry-consumer list** (RF-1 class at the CF layer; flip-as-declared would silently split Cottonwood onto the legacy origin). F-2: null-on-404 at aum.ts:586-608 with rendered consequence. F-3: CustomErrorResponses=0 — the mask is SPA fallthrough, not error-response rules. F-4: instrument docstring mis-read.
4. **Zero footprint verified:** ph3 re-runs unchanged; no portal/infra/FE modifications; only org/ deliverables + this log committed.

## Handoffs / routing

- Report to COO (per both TOs) — sent post-log, incl. F-1 for CTO routing (WS-F/3F-G2 consequence).
- P1 locus table circulated to 0.4.0_DS (TO cross-domain: input to 3F-G3/G4/G8).
- F-4 instrument defect noted for the comp-tools lane via COO report (not self-routed — observer of the defect, not owner).

## Blockers

None. Both TOs complete. 3F-P2's 0.7.0_AE joint half (behavior-side follow-ups in WS-F) needs nothing from me now; the route table is his input when he spawns.
