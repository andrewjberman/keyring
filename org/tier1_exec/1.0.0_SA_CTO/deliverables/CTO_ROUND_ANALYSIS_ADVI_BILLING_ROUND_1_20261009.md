# CTO ROUND ANALYSIS -- ADVI_BILLING round 1 (FWD-1, the thread)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~07:4xZ | **Input:** the CVO's L10 slug msg 2814,
`org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/adjudications/ADJUDICATION_v1.md` @4f374d90d5. Grade:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BILLING_ROUND_1_L9_GRADE_20261009.md`. MAY-CLOSE, ARMED 0. **PRD:** v0.2.

## Grade

**FWD-1: thread EXERCISED on DEV, not yet REALIZED.**
- One 49 Financial household (`z08219260`) and one billed quarter (2026Q3) are worked out from Opal's own values.
- They are served by the new read route and render on the DEV page, with each difference shown with its reason:
  - the advisor component DIFFERS within 1%, the leading reason being the SMArtX prior-quarter true-up;
  - the platform component DIFFERS by construction, because Opal holds no SMArtX platform rate.
  The CVO graded AB1-3-AC3 MET on the real render.
- The ACCEPT clause "an advisor reads it in Opal" is not met while the page is on DEV only. It becomes REALIZED on the PROD push, which is Andrew's act
  because the page is client-facing (law d92d08c448). That push follows the book check below.

FWD-2 to FWD-6 are not served this round.

## Ruling: W1-S6, the in-firm read scope

**Ruling: ADD a book check on BOTH routes** (the new fee-quarter route and the existing relationship and platinum-summary route). Parity is not kept.
- **Why:** a fee is the most sensitive per-client figure on the page. Today any in-firm viewer can read any household's object. An advisor sees only the
  households in their own book; a firm administrator role keeps the firm view.
- The check is keyed on the viewer's verified identity and the book membership the estate already holds. No body field is trusted.
- **This narrows a served route,** so it moves served output and needs a never-widen pair. The pair names both branches: an advisor in-book is admitted,
  and an advisor out-of-book is refused.
- **Until it ships, parity holds on DEV only.** The PROD push of the fee panel is not proposed to Andrew before the check is live.

## Enrichment list (round 2)

1. **The book check on both routes, with its pair.** Tests: in-book admitted, out-of-book refused, firm-admin admitted, other firm refused.
2. **An SMArtX statement or fee ingest** (rates and the true-up), so the advisor and platform components can MATCH or DIFFER with a measured reason. Egress is
   open (law 4d77a9c3ea).
3. **The `rel_to_z` crosswalk** lands on a durable plane at an `address()` path, so the household key is not rebuilt per run.
4. **FWD-3's step view:** the panel already shows value, schedule, flows and exclusions per account. Round 2 grades FWD-3 on one client's real render.

-- 1.0.0_SA_CTO~DELL2
