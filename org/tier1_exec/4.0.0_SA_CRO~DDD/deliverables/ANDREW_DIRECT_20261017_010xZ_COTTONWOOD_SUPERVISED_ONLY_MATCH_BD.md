# ANDREW-DIRECT 2026-10-17 ~01:0xZ -- Cottonwood MDPF tracking is Supervised-only and must match the BD Dashboard

**Author:** 4.0.0_SA_CRO~DDD (Chief Research Officer)
**Channel:** the 4.0.0_SA_CRO~DDD terminal on dell1, ~01:0xZ 2026-10-17 (~21:0x ET 2026-10-16)
**Attachment:** `C:\Users\Test\Downloads\zipppp.zip`, four screenshots: BD Dashboard 10/15 All Assets (563.56M), the
Supervised filter, BD Dashboard 10/15 Supervised (530.42M), and the Opal Model Portfolios page (Cottonwood, $554.63M,
October 15th 2026 5:00p ET). The zip is not committed.

## VERBATIM

"I want you to go find something for me. look at the images contained here; C:\Users\Test\Downloads\zipppp.zip. The
issue is that Cottonwood only wants to see the assets they actually supervise, not all of them. However, for some reason
we are not displaying the same number they show when they show all assets. Where is the error here, are we one day lagged
or are they counting assets we somehow arent counting? We need to get to the bottom of that first of all, second we need
to make sure "Cottonwood" asset tracking for the dashboard only includes the Supervised assets (and matches that fucking
number you see there), figure it out go"

## Two asks, as he ordered them

1. Root-cause the gap between the Opal Cottonwood total ($554.63M) and the BD Dashboard All Assets figure ($563.56M):
   one-day lag, or assets BD counts that we do not.
2. Cottonwood asset tracking on the dashboard includes Supervised assets only, and matches the BD Dashboard Supervised
   figure ($530.42M on 10/15).

Prior ruling this re-affirms: Andrew-direct 2026-08-25 ~14:05Z, "Cottonwood specifically had that request that their
book be displayed as only that which is Supervised on their behalf" (commit a78c51158c).

Findings: `org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/COTTONWOOD_SUPERVISED_GAP_FINDINGS_20261017.md`.
