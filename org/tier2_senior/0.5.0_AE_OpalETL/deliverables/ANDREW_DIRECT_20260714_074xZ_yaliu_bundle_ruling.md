# ANDREW-DIRECT (verbatim) — 2026-07-14 ~07:4xZ, via CTO session (relay: CTO 074036Z)

**Channel:** Andrew in CTO's session; relayed to 0.5.0_AE_OpalETL by CTO msg 20260714T074036Z with
his operationalization. **Scope (as relayed):** the SmartX account-tier credential fork — plan
section 3 of `SMARTX_C5_DATA_SHAPE_PLAN_20260714.md` (@ `7414df175`). CTO recorded on his side and
CC-folds to COO; this file is 0.5.0's durable copy per the verbatim rule.

## Verbatim (as relayed by CTO)

> Yeah that is entirely unsurprising, I told them 100 times to just explore/develop/bundle the
> yaliu account auth/cookie, because it had higher privileges, and it wanted to keep trying to use
> the original one saying they were the same even though we all know they are obviously not the
> same, glad thqat is resolved.

## CTO operationalization (074036Z, binding on C5 execution)

1. **Section 3 = OPTION (a):** develop the yaliu account auth/cookie into the dormant BUNDLE shape
   (`SMARTX_CRED_BUNDLE_SECRET`); feeds 8+9 run under it. **No HAR seed** — the API feed is the
   source from day one.
2. **opal7 stays for feeds 1–7, unchanged** — the bundle is a scoped, ADDITIVE credential for the
   account tier only. The 07:29Z probe is the instrument that settled the "they're the same"
   dispute: they are measured NOT the same.
3. **Mandatory guards:** `expect_min_models`-class assert on the BUNDLE's roster (yaliu-grade grant
   measured missing 4/11 models + 7 view-only — coverage is a MEASURED quantity, re-probe at
   development time, never inherit the HAR's numbers); feed-9-vs-feed-5 reconciliation (fewer
   resolver rows than roster = PARTIAL identity table, FAIL LOUD); fleet-zero = broken endpoint.
4. **Secrets:** the cookie/auth lands in Secrets Manager under the bundle secret — never in code,
   never in bronze, never in a commit.
5. **Sequencing (mine):** fence attach + build items 1–3 stay in front; feed 9 development follows
   the moment the bundle auth works.
