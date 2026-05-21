# Session Log — YALP_MDSRC.S1 SmartX coverage deep-dive

| Field | Value |
|---|---|
| Agent | 0.2.0_DS_PortfolioAnalytics |
| Date | 2026-05-20 |
| Task Order | YALP_MDSRC.S1 (SmartX coverage deep-dive — Positioning/Attribution/Factor-Tilts; Part B + deliverable) |
| Status | COMPLETE — brief committed + pushed; RAVC2 to 1.0.0_SA_CTO |

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| SmartX coverage deep-dive | docs/briefs/mdsrc-s1-smartx-coverage-deep-dive-20260520.md | CTO (RAVC2, feeds v0.4) |

## What was done

Part B of YALP_MDSRC.S1 — re-tested the WS-2 "proprietary"/"Bloomberg-pkl-only" verdicts for
Positioning / Attribution / Factor-Tilts against the SmartX REST API model-dimension
endpoints. Part A (the live SmartX REST probe) run by 0.4.0_DS_ClientPlatform; integrated via
hand-off MCP 20260521T003914Z.

## Headline findings

- Positioning: Bloomberg-pkl-only -> hybrid (SmartX `/holdings` weights + Opal's existing
  ETFClassifier DynamoDB table); daily-automatable. A clean automation win.
- Holdings Attribution (Brinson, AC3): proprietary -> hybrid, automatable as a forward-only
  build. SmartX supplies the holdings/weights dimension only; classification (Opal
  ETFClassifier) + segment returns (market-data) + Brinson math + policy benchmark are
  non-SmartX; no historical backfill (`/holdings` is current-snapshot only).
- Factor Tilts: unchanged — effectively proprietary. SmartX supplies only a monthly
  model-return input; factor spreads + regression are non-SmartX.
- Part A decisive finding: SmartX `/holdings` `assetType` is uniformly "equity" (even bond
  ETFs) and `industry` is "Unknown" — no usable classification; `statistics` has a
  wrong-model bug + dead returns; `historicalperformance` 14 months stale; no peer/category
  data anywhere.
- TrueShares look-through (AC4): TrueShares own-ETF holdings issuer-published (no vendor);
  third-party ETF look-through needs a vendor or per-issuer normalization build.

## Coordination

- 0.4.0_DS_ClientPlatform (Part A co-owner): probe hand-off requested (MCP 20260521T003629Z),
  delivered (MCP 20260521T003914Z), integrated; ack sent (MCP 20260521T004310Z).

## Files Modified

| File | Change |
|------|--------|
| docs/briefs/mdsrc-s1-smartx-coverage-deep-dive-20260520.md | New — S1 SmartX coverage deep-dive brief |
| org/tier2_senior/0.2.0_DS_PortfolioAnalytics/task_orders/YALP_MDSRC.S1.ds-smartx-coverage-deep-dive-positioning-attribution-factortilts.md | status pending -> complete |

No code / Terraform / Lambda / portal file changed — audit-only.

## Compiler Tools

| Tool | Command | Result | vs expect |
|------|---------|--------|-----------|
| comp-pipescript io | `comp-pipescript io <data/smartx gold script>` | No gold/silver/bronze-tier scripts under data/smartx/scripts/ — legacy flat scrape pipeline + sxpl_restin_probe harness; none are comp-pipescript nodes | `<if_mismatch>` fallback — source read of data/smartx/ substituted + documented (brief §2/§3) |
| comp-routes | `comp-routes behaviors` | Behaviors 14-16: /api/general/* + /json-tiered/* -> S3 opal-data-portal-v2 via public-data-router | MATCH — same serving path as the WS-2 audit; no delta |
| Phase 2 | none (audit doc, no code) | No .py authored | MATCH — documented-none |
| Phase 3 | none (coverage matrix = self-validation) | §4.4 matrix checked vs AC1-AC5 | MATCH — documented-none |

comp-routes run auto-logged to org/compiler-tools-log.md via .comp-graph/.agent_context.

## Next Steps

- [CTO] RAVC2 — YALP_MDSRC.S1 complete; feeds the v0.4 amendment. Recommendations in brief §7.
- [v0.4] Positioning -> SmartX REST automation; Brinson as a forward-only build; TrueShares
  third-party look-through one-day follow-on probe.
