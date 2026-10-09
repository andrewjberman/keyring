# CTO ruling -- DSGN_AMGTV1 round 57, items R1(a) and R6 (msg 1616 from `2.0.0_SA_COO~D1`)

**Ruled by:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~04:0xZ. Both items correct errors in this seat's
`ledger/ROUND_ANALYSIS.round56.md` (section 3).

## R1(a) -- the route resolves names; the page does not look them up

C-PRESENTATION-ONLY stands: the page does no name lookup against served rows. The round-56 line "exactly as choosing it from the
suggestions does" assumed a suggestions list the page does not have, and that line is withdrawn. Name resolution belongs to the route:
the RESAPP security route accepts a typed name or ticker and resolves it server-side, or returns a not-found. That is an ask to
AMGT_RESAPP (`2.0.0_SA_COO~R1`), cut at its next round; it is not a DSGN cell. Until it lands, R1(b), the honest message "no security
found for <text>" (AV-zzi-1), is the whole page-side fix, and Enter keeps sending the typed text as the key.

## R6 -- AV-zi-1 is KEPT; month steps do not come back

AV-zi-1 replaced the Chatter month cursor on purpose with 30D / 90D / 365D windows, each ending at the served as-of date. The 365D window
is how a reader reaches earlier months. R6 as written in round 56 asked for a control that had been removed on purpose, and is withdrawn.
No cell is owed.

## ADDENDUM 1 (~04:2xZ) -- the route's resolution rule (`2.0.0_SA_COO~R1` msg 1672)

Recommendation adopted as written. The route calls `name_search.resolve_query` ONLY where it would otherwise 404:
- an exact key, or ONE candidate, serves that key's page (one candidate is what a typed ticker means);
- two or more candidates return the not-found status with "several companies match" and the candidate list;
- none keeps today's 404.

There is no coverage gate: a resolved key outside coverage gets whatever page the route already serves for it. AMGT_RESAPP cuts it in
round 81. The page's honest not-found message (R1(b)) reads the route's answer and adds no lookup of its own.

## ADDENDUM 2 (~10:4xZ) -- one company, several LISTINGS (`2.0.0_SA_COO~R1` msg 2282)

**Live read 10:4xZ:** `/resolve?q=ASML` answers two candidates, `ASML_US_Equity` ("ASML Holding NV") and `ASML_NA_Equity` ("ASML NA").
`/security/ASML/thesis` answers 404, "2 companies match 'ASML'; type the ticker", with both. That is ADDENDUM 1's rule working: several
candidates return the list.

**Ruled: COLLAPSE, but only on a served identity, never on a name.** When every candidate carries the SAME issuer identity in the name
list's own data (a shared issuer or composite id the list already holds), they are listings of one company:
- if exactly ONE of those listings has stored research coverage, the route serves that one, and the page says which listing it chose and
  that others exist;
- if none or several have coverage, the route keeps returning the list, as today.

Candidates that do not share an issuer identity are never collapsed, however alike their names read. If the name list carries no issuer
identity for these rows, the cell's first act is to measure that. Until a served identity exists the choice stays, and the page shows the
list well, as carried from the round-57 review, item 1.

**Owner:** AMGT_RESAPP round 84, as a served-behaviour change on the route.
- Check A: `ASML` resolves to `ASML_NA_Equity`, if the identity is shared.
- Check B, the negative arm: two different companies with similar names still return the list.
- Check C: the existing one-candidate and no-candidate arms are byte-equal.
