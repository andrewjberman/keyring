# L4-R review -- MDPF_CANON PRD v2.21, ratified-text half (ENDPOINT + CONTRACTS)

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-14 ~21:0xZ. Delivered by 1.0.0_SA_CTO~DELL1 msgs 5870 and 5871. v2.20 (msgs 5866 and
5867) was superseded before this seat stamped it, and is read here as part of the chain.
**Graded:** `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` @3826492d9c (v2.21). Chain: v2.18 @0736ed5c23 SIGNED by this seat; v2.19
@02852d9d16 REFUSED by this seat (@897fe1d0d1); v2.20 @038b2173f3; v2.21.

## Verdict: SIGN

## What changed since v2.19, and why it answers the refusal

- **v2.20 takes this seat's option 3.** On dates where Global holds one firm (the five models before 2026-05-15; Custom from 05-15 to
  07-19), the per-model lines draw ONLY for an internal session (`firmId` = the internal firm), read from that firm's own served series.
  The Global served leaves keep FWD-3's fold and gain no single-firm value. Every other session (the demo tenant, a claim with no
  firmId) draws one "Models" band and keeps v2.18's exception (ii), its boundary sentence and its printed gap. This removes the
  dependence on "only opal staff see global" that the demo tenant contradicts.
- **v2.21 restates (b) and adds (e), on Andrew's word in the CRO spec amendment 1 @686f769e63:** Client Supervised is net of the two
  Opal SMA strategies (and, before 2025-03-27, Opal Global All Equity Total Return), from SMArtX `fact_model_aum_daily` before
  2026-05-18 and from the served carve-outs after. ETF Strategies draw from 2024-11-01. ALT Strategies = `tax_additive_aua` only, and
  Muni is a Custom member. The SMA lines draw for every session; the cited ruling reads them as held at no firm, so they carry no
  single-firm exposure.

## The four checks

| Check | Result |
|---|---|
| ENDPOINT against its pins | FWD-9's head now states the Global Trend rule, (a)-(e). FWD-3 is not weakened for any served leaf: its fold stays on every Global leaf, and the single-firm lines are a read-side, internal-session draw from the firm's own leaf. No other FWD's DONE WHEN or ACCEPT moves. |
| Every operative constraint present | Yes. Exception (ii) survives for non-internal sessions; roll-forward (c) is forward-only and claim-held; (d) applies to internal sessions only. |
| No annotation, history or seat name inside the section | The v2.19 OVERRIDES paragraph with citations and a seat path is gone; the head states the rule only and the provenance sits in the v2.20 and v2.21 addenda. The two remaining items (`(v2.18)` at the old exception, and the deliverables path at line 169) predate this bump and were in text already signed. Drop them at the next edit. |
| CONTRACTS agrees with the counterpart PRD | No CONTRACTS table row changed across v2.18 -> v2.21. |

## Recorded separately (not a ground against this text)

The CTO's v2.20 note says the demo tenant "cannot reach those values through the page or the API". The page half holds under v2.20. The
API half does not, independently of this PRD: `/api/general/mdpf/*` is rewritten to `platinum/mdpf/*` behind the JWT check alone, with
no firm scoping, so any authenticated login can fetch another firm's per-firm leaf by URL. That is filed as row **MDPF_CANON-D1-S27**
(ARMED, owner 1.0.0_SA_CTO~DELL1), read from repo source; the deployed edge bytes were not compared. The internal-session draw that
v2.20 relies on is sound only once that gap is closed.

-- 3.0.0_SA_CVO
