# Andrew-direct 2026-10-16 ~15:5xZ: a 2.5M-cell daily Bloomberg budget by surface, and the Bloomberg terminal agent may download

**Recorded by:** `2.0.0_SA_COO~Q1`, same turn. **Channel:** the dell1 terminal session. **Routed to:** `1.0.0_SA_CTO~Z` and `1.0.0_SA_CTO~DELL1` for how to implement (Andrew's word).

## VERBATIM

> yes this is much better policy as youve described here + we need to make sure BBG agent policy is synched up with this, also definitely let it download it has to be able to download.

> let's get this policy implemented and let sitez know so they can make any edits needed on their side, route that to CTO for how they want to handle it

His earlier word that framed the ask (same session): the floor is about 2.9M cells a day; cap the plan at a 2.5M ceiling; "identify budgets for the various surfaces + ad hoc calls that actually add up to that, so we arent not spending any of our daily budget."

## What he approved: the policy as described (the numbers are the COO's proposal; his word approves the shape)

| Surface | Budget a day (cells) | Basis |
|---|---|---|
| A Production daily (A1 to A5) | 350,000 | A3 at its 150,000-row ceiling x 2 fields is about 300,000 (inferred); A1 is not metered; A2, A4, A5 are about 3,100, 1,000 and 190 (held). First claim, protected. |
| B Client history | 1,500,000 | The sink. The Cottonwood backlog is 1,857,629 needed-date cells (3,581 securities, less the Yahoo-held), so it finishes in about 1.3 days at this level, after the first-tranche resolve rate clears 50 percent (CTO ruling 20261016). |
| C Rival funds history | 400,000 | The 213,149-cell backlog clears in about a day, then the producer's 20,000-per-run cap governs and the rest releases. |
| D Research | 100,000 | Current demand is about 2,000. |
| E Ad hoc, including the Bloomberg terminal agent | 150,000 | Per-request cap 5,000 (was 585). |
| **Total** | **2,500,000** | The remaining 420,000 to the 2,920,000 block (measured 2026-10-05) is the margin. |

**Release rule:** whatever A, C, D and E leave unused in a day flows to B the same day, so none of the budget sits idle.

**The terminal agent:** `0.0.3_BG_BBGTerminal` may download. The view-never-download tie-breaker and "Unclassifiable = download-side until Andrew says otherwise" in `refs/BLOOMBERG_GUARDRAILS.md` no longer bind a request that fits surface E (at most 5,000 cells a request, 150,000 a day). The agent's own record of the 13-CUSIP case is `org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/ANDREW_DIRECT_20261016_1512Z_JUST_PULL_IT_FROM_BBG.md`. Its `prompt.md` line "capped at 2 securities" is stale (13 went through) and must say the E cap.

## Claims

- 2,920,000: **measured** (the 2026-10-05 BQL block), a BQL figure.
- The weight of a history or reference cell against a BQL cell: **UNMEASURED**. The budget assumes one cell is one cell.
- A3 rows to cells (x2): **inferred**.
- The drawer enforces 5,858 history cells a day today (**measured**, a floor from our own largest day), and the CTO's ramp ruling (`MDPF_DEMQUE/ledger/CTO_RULING_HISTORY_CEILING_RAMP_20261015.md`) ends at 29,290. The budget above is a target; reaching it needs a ruling on how the ramp meets it, with the pushback read on each step.
- Yahoo is a separate vendor (600 requests a day) and is outside this budget.

## What implementing it touches, by owner (none done yet; the COO does not cut mid-round or edit a served ceiling)

1. **Site Z (drawer and allowance):** `data/mdpf/scripts/demque/bbg_allowance.json` (daily ceiling and per-surface budgets, claims as above), the E per-request cap in the intake rule, the drawer's room per fire, the history ramp, trading-day draws (round-10 cells DQ-t-69 and DQ-t-70). Owner: `1.0.0_SA_CTO~Z` rules; the COO cuts the dell1 half after the ruling.
2. **Terminal agent policy:** `refs/BLOOMBERG_GUARDRAILS.md` (Andrew's rule; the agent cannot write `refs/`), `prompt.md` (the stale cap), and its Teams duty text. Owner: `0.0.0_AB_MSTR~Z` as integrator, `1.0.0_SA_CTO~Z` for the content.
3. **Metering gaps the budget exposes:** A1 and A3 have no daily meter; the S3 demand ledger carries no completeness signal for production legs A1, A4 and A5 (named gap, round-9 findings draft).

Push state: LOCAL on `box/dell1` until the integrator's next pass.
