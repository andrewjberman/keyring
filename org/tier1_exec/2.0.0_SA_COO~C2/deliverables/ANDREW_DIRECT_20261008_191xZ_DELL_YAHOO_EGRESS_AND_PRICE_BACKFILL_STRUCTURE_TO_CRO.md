# ANDREW-DIRECT 2026-10-08 ~19:1xZ -- Yahoo egress on the Dell boxes; the price-backfill structure goes to the CRO

Channel: dell2 terminal of `2.0.0_SA_COO~C2`, in-session, after the seat reported that the 10-07 Yahoo word was scoped to DELL1 and
MDPF_SECHIST only (relay @19895b0d77 on dell1, MSTR~DELL1 bus cab25644).

VERBATIM:

> DELL boxes can call yahoo all they want, i thought i already gave egress to that? In any case, yahoo is a free resource so you
> should be able to do that freely. The greater issue is resolutin of the ticker with yahoo, specifically the methodology of how that
> can be locked in. Beyond that, there needs to be a process of securities that cannot be mapped to yahoo successfully, also how we
> handle corporate actions needs to be threaded into that, particualrly retroactively. Also yfinance is a free api so you have to be
> gentle with it and figure out a schedule that actually facilitates being able to get that reliably day over day, i expect it to be a
> very long multi-day even multi-week batching process, I recommend talking to CRO about that and figuring out a structure that covers
> resolution, unresolved indexing on time period(s), api call structure/request amount, and so on. The way I see that working is
> ultimately that we keep a "ranking" on the importance of being able to pull that backfill. For example, if there is a mutual fund
> that we cannot resolve, and that ticker is something that only existed on a cottonwood client that no longer exists by name or
> account match in the black diamond set, then that is not a priority to get.

## What it says (relayed, not widened or narrowed)

1. **Egress:** the Dell boxes may call Yahoo (yfinance). The 10-07 relay's "DELL1 and MDPF_SECHIST only" scope is superseded by this
   word for the Dell boxes; Bloomberg is untouched by it.
2. **The structure to research (the CRO's, on Andrew's recommendation):**
   - how a security's Yahoo ticker is resolved and locked in;
   - a process for securities that cannot be mapped to Yahoo;
   - corporate actions threaded in, retroactively;
   - a gentle, reliable day-over-day call schedule (multi-day to multi-week batching), the request size and amount;
   - indexing of what is unresolved, by time period;
   - a RANKING of backfill importance. Andrew's example: an unresolvable mutual fund held only by a Cottonwood client that no longer
     exists by name or account match in the Black Diamond set is not a priority.

## Not decided here

Who builds the backfill. The Cottonwood price need is today carried by MDPF_SECHIST's price-need file; this record does not move that
ownership.
