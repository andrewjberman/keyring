# Session Log — DS~A — MDPF_ASSETS.001: 49F Black Diamond book custody-cutout audit

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.001 (`dsa-49f-blackdiamond-book-custody-cutout-audit`) — Phase 0, WS-E, GO'd by COO
**Trigger:** COO GO message 20260518T143744Z — MDPF_ASSETS Phase 0 trio.

---

## Summary

Phase-0 audit COMPLETE. The §3.4 identity `non_model_aua = certified_aua − model_aua − Σ cutouts` is **structurally sound and daily-computable, and reconciles** to the historical plug.

**The TO's "~$70M Fidelity-custodied" premise does NOT hold empirically.** Fidelity-custodied assets (`billing_account_custodian == 'Fidelity IWS'`) = **$12.96M / 12 accounts**, not ~$70M. The material non-Schwab custody is **ByAll Accounts — $135.6M** (Morningstar held-away account-aggregation feed).

Custodian decomposition of certified_aua (2026-05-14, reconciles to the cent at $1,812,432,585.32): Schwab $1,655.4M (91.3%) / ByAll Accounts $135.6M (7.5%) / Fidelity IWS $13.0M (0.7%) / unmatched $7.3M (0.4%, 15 new accts) / DST $1.2M (0.06%).

Total custody cutout ≈ $149.7M takes the current naive non-model figure $455.3M → ~$305.6M, reconciling closely to the frozen ~$271.2M plug (+13% ≈ 4.5mo growth). The §3.4 design is validated.

**The one real engineering gap:** `silver/allocations` (the certified_aua source) carries no custodian column — the attribute lives in a separate BD report, `silver/fees.billing_account_custodian`. WS-E Phase 1 must build an `account_id→custodian` crosswalk from `silver/fees` history (built it here from all 1,855 partitions / 3.3M rows — custodian is perfectly stable per account, 0 conflicts).

**The cutout SET is a business decision** — escalated to Andrew/CTO: recommend ByAll Accounts = cutout (held-away), DST = cutout (immaterial), Fidelity IWS = needs Andrew's call (12 retirement-plan accounts, possibly advised-at-Fidelity not held-away). PRD §3.4 "~$70M Fidelity" text should be corrected.

Note: `insurance_accounts.json` (109 accts / $61.8M) is NOT an AUA-exclusion list — `lib/exclusions.py` uses it only for a longer staleness gate. It overlaps the ByAll cutout — do not double-subtract.

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| WS-E Phase-0 finding | `docs/briefs/mdpf-49f-nonmodel-custody-cutout-audit-20260518.md` | COO — input to the WS-E Phase-1 build TO; Andrew/CTO for the cutout-set ruling |

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `aws s3 ls s3://opal-data-bd/gold/aua_certification/` (TO Phase-0 mandate) | PASS | Daily partitions present; latest `2026-05-14.json` written 2026-05-18 00:37Z — certified_aua input is fresh. |
| `comp-pipescript io E_19.write_aua_certification` (TO Phase-0 mandate) | GAP | Returned "Script not found" — the graph node is `E_19`, not the dotted filename; dotted-filename args don't resolve. I/O established by reading the script directly: READS `gold/client_performance.parquet` + `silver/allocations/{date}.parquet`; WRITES `gold/aua_certification/{date}.json`. No BD gold script carries the custody breakdown — audit done via direct `silver/allocations × silver/fees` join. |

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/mdpf-49f-nonmodel-custody-cutout-audit-20260518.md` | New — WS-E Phase-0 finding brief |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/MDPF_ASSETS.001.dsa-49f-blackdiamond-book-custody-cutout-audit.md` | `<status>` pending → complete |

No script modified, no artifact written — read-only investigation per the TO.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — MDPF_ASSETS.001 complete. AC1-AC5 met (AC1 with the premise corrected). Author the WS-E Phase-1 build TO off the brief — gated on the cutout-set ruling below. |
| **Andrew / CTO 1.0.0** | Cutout-set ruling needed before WS-E Phase 1: which custodians are "not Opal advised AUA"? Recommend ByAll Accounts = cutout, DST = cutout, Fidelity IWS = Andrew's call. Empirically Fidelity is $13M not $70M — PRD §3.4 text should be corrected. |
| **DS~A (self)** | MDPF_ASSETS Phase-0 trio: .001 + .002 both complete. .003 (Eclipse → Inflection model-AUA feasibility) is DS~B's lane. |
