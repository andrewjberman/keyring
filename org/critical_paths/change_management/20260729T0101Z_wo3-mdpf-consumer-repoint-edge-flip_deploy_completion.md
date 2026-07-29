# Deploy: wo3-mdpf-consumer-repoint-edge-flip

**Opened:** 2026-07-29T01:01Z by 0.2.0_DT_PortfolioAnalytics · **Authority:** MDPF_RESET WO-3
(Andrew ~2334Z "do the consumer re-point" + ~2357Z "ok proceed with the DT flip, that is my GO" +
~0000Z "Option 1, fix then flip tonight" + ~0059Z via COO "I do not want to wait to tomorrow to
repoint"; CTO GO 005733Z with full four-leg chain; COO acceptance diff PASS 005548Z/005606Z;
AE trio verified 6/7-EXACT accepted by CTO 003928Z; Step-0 ACCEPTED 000536Z).

**The change:** ONE added prefix-disjoint branch in `public-data-router` (Lambda@Edge):
`/api/general/mdpf/` -> `/platinum/mdpf/` (was: fell through the default to `/json/mdpf/`).
Nothing else in the router moves. Deploy = build (esbuild minify) -> S3 artifact ->
safe-apply portal-auth (one apply mints the new version AND re-points all three behavior
associations via `qualified_arn`) -> L@E replication -> scoped CF invalidation
`/api/general/mdpf/*` only.

**Pre-flip baselines (all authenticated live-URL fetches, positive-controlled 00:10-00:14Z):**
| what | value |
|---|---|
| live global URL (pre) | 200, 254,419 B == S3 `json/mdpf/global/` ETag `5f758b470372da18ad04e5248037cdd0`, as_of_last 07-22 |
| non-mdpf control `portfolios/aum-metrics.json` | 200, 7,234 B, md5 `9bae4b42ff312c72817ca27861c1e28b` |
| firm URLs (pre) | 49f 183,004 B `50140744...` · inflection 146,290 B `e3c8db35...` · cottonwood 87,262 B `194e5bb0...` |
| deployed router (pre) | `public-data-router:5` on dist `EVTSA9VEHNZVH` (CF config ETag `E2DYWYC9UJPDWJ`) |
| post-flip expected global | platinum object ETag `31e64570d3090eff4df3baab91d2a1dd`, 200,059 B, as_of_last 07-27, last value 1,950,519,805.86 |

**Acceptance (CTO dispatch 234425Z + addendum 234528Z + COO 005606Z):**
1. live global URL -> 1,950,519,805.86 @ as_of_last 07-27 (B content)
2. one URL per firm (49financial / inflection / cottonwood) -> 200, platinum per-scope content
3. CONTROL: non-mdpf `/api/general/` path byte-identical to pre-flip
4. NEGATIVE: frozen `json/mdpf/global/` object UNTOUCHED (ETag `5f758b47` unmoved)
Plus: no historical value change on any of the 447 shared dates (COO's oracle: any historical
delta = routing/caching artifact -> escalate, do not rationalise).

## Legs
- **L1 (git):** router edit + ledger committed to CLOUD. — *opened*
- **L2 (deploy):** build+upload zip -> source map commit -> safe-apply portal-auth -> new version
  live on all 3 behavior associations -> 0-diff plan. — *opened*
- **L3 (activation):** CF distribution Deployed + scoped invalidation `/api/general/mdpf/*`
  Completed. — *opened*
- **L4 (verify):** four exercises + negative + shared-date spot-check; report to CTO/COO. — *opened*

## Ledger items beyond the script (recorded at open, discharged at close)
- **CLOBBER-DETECTOR RE-BASELINE (COO 005606Z, CTO 005733Z):** at cutover the serve-integrity
  baseline MOVES: new served-content reference = `platinum/mdpf/global/aggregate-aua-timeseries.json`
  (ETag `31e64570d3090eff4df3baab91d2a1dd` at flip). The old `json/mdpf/global` ETag `5f758b47`'s
  ONLY remaining meaning is the NEGATIVE control (frozen legacy, must never move). Any reader
  verifying the serve against `5f758b47` after this deploy is verifying a retired baseline.
  (The A.3 served-freshness instrument re-point is separately routed by CTO — not this deploy.)
- **JWT wipe attestation due at close:** the one-night verify token + key material
  (scratchpad `jwt-priv.pem`, `svc.jwt`) destroyed after L4. One-night instrument per CTO
  001643Z — a durable serve-verification identity, if ever wanted, is a designed artifact with
  its own review, flagged as an open item, never a quiet re-mint.
- **Riding for awareness (CTO):** COO O4 — the artifact's trading-day calendar mechanism changed
  (hardcoded-fallback -> pandas_market_calendars), value-equivalent across all 447 shared dates
  tonight; frontier-definition change on record at CTO's desk. Andrew ~0059Z: "using NYSE
  official market calendar is the way to go for this."
- **Render-disclosure question (COO item 3, raised pre-render):** the three frontier dates carry
  cottonwood `carried_at_declared_cadence(as_of=2026-07-22)`; whether the portal renders a
  carried point distinguishably from a measured one is a disclosure question for DE/CTO — named
  here so Andrew hears it from us first.

## Completion
*(open)*
