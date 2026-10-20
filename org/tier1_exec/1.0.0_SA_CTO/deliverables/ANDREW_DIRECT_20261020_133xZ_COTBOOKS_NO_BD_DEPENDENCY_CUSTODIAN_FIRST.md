# ANDREW-DIRECT 2026-10-20 ~13:1xZ to 13:3xZ at the 1.0.0_SA_CTO~DELL1 terminal: ADVI_COTBOOKS is re-framed as the first case study for representing a firm without Black Diamond

**Recorded by:** 1.0.0_SA_CTO~DELL1.
**Context:** I showed the six DONE WHEN lines of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_ADVI_COTBOOKS_20261017.md` (open call 0cf5).

## His words, VERBATIM (typos his)

> This works but keep in mind that it's not going to add up to Black Diamond because they have Schwab and "Strata" (another
> custodian) clients too. The purpose of this work should really be about assessing how to analyze and stitch the commonwealth
> books to the fidelity backfill and shape. Our ultimate goal is figuring out how to replace Black Diamond, which means that we
> cannot rely on Black Diamond for any critical function. Let's discuss how we can thread this here, because we want Cottonwood
> to be our first true case study where we figure out how to represent all their stuff without having any BD dependency.

I proposed a custodian-first thread and asked four questions. His answers:

> 1.) We have master account numbers associated with the various advisors at Cottonwood on Schwab, but we don't have access
> yet, i am going to get those from Mike Little at Alongside today. Regarding Fidelity, there are "G Numbers" whereby we are
> going to have to backfill off the G Numbers and create daily pulls per each G Number, various of which is the primary and
> advisor specific Cottonwood G Numbers, pictured here [screenshot] 2.) We need to clarify that. 3.) Yes we can compare to BD.
> 4.) Yes definitely.

The four questions were:
1. Is the custodian's advisor code the right advisor key?
2. How does Cottonwood see its Strata accounts today?
3. May we compare against Black Diamond as a check?
4. Should the CRO re-brief on the custodian data before the endpoint is re-cut?

## The Cottonwood G numbers in his screenshot

Seven Cottonwood rows. The numbers are masked here, because NFRA_FIDUPL keeps account and G numbers out of committed files. The
full numbers are in the screenshot, copied off git to `tmp/cotbooks/ANDREW_20261020_wealthscape_g_numbers.png` (gitignored,
dell1).

| G number (masked) | label |
|---|---|
| G460...202 | COTTONWOOD CAPITAL ADVISORS - PRIMARY |
| G460...203 | COTTONWOOD CAPTIAL ADVISORS - SHIPLEY |
| G460...204 | COTTONWOOD CAPTIAL ADVISORS - RUBOTTOM |
| G460...205 | COTTONWOOD CAPITAL ADVISORS - BASS |
| G460...211 | COTTONWOOD CAPITAL ADVISORS - SECONDARY |
| G475...184 | COTTONWOOD CAPITAL ADVISORS |
| G482...519 | COTTONWOOD CAPITAL ADVISORS - ADVISOR PAYS |

The same list also shows three VM WEALTH PARTNERS G numbers. They are another firm, and his word does not name them.

## What this sets

- **Goal.** Represent Cottonwood's whole book with no Black Diamond dependency in any critical function. Cottonwood is the first
  case study toward replacing Black Diamond.
- **Black Diamond.** It may be COMPARED against, as a check. It is never a source.
- **Fidelity.** Backfill and daily pulls per G number, covering the seven Cottonwood G numbers above. This feeds NFRA_FIDUPL
  FWD-9 (the per-firm split on the G number) and C-BACKFILL.
- **Schwab.** Advisor master account numbers exist. Access is pending: Andrew is getting them from Mike Little at Alongside today.
- **Strata.** Its feed is to be clarified. Until then it is a named coverage gap, never a guess.
- **L1.** The CRO re-briefs ADVI_COTBOOKS custodian-first. The 2026-10-17 endpoint is superseded once the re-brief lands and the
  endpoint is re-cut; the re-cut goes back to Andrew for his DONE WHEN confirmation.
