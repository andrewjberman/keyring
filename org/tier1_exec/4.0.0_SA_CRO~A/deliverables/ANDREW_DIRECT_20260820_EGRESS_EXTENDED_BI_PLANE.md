# ANDREW-DIRECT 2026-08-20 ~0210Z (CRO~A terminal, live) -- egress extended to the BI plane

## VERBATIM

> "you have egress there too, go ahead"

**Channel:** CRO~A terminal, in direct response to my report that the BI plane is
`bd3.bdreporting.com/advisor/api/v1/` and my statement that I would NOT call it without his word.
**Recorded:** same turn, BEFORE the first call.

## SCOPE -- RECORDED, NOT ADJUDICATED

**"there"** = the surface I had just named and described in the message he answered: the **BD
Business-Intelligence / advisor plane on `bd3.bdreporting.com`** -- `/advisor/api/v1/*`, plus the
sibling read paths surfaced in his own HAR (`/request/api/*`, `/ClientView/api/*`, and the
`firm-api` / `alerts` / `broadcast-api` hosts observed there).

**"go ahead"** = proceed now; no further return trip for this surface.

## WHAT CARRIES OVER UNCHANGED (not new limits -- previously ruled, still binding)

- **READ-SIDE ONLY.** He DROPPED a vendor-config write (dim 436) two rulings ago; an egress grant
  does not become a write grant by being extended to a new plane. No PUT/POST that mutates
  vendor-side state, no template creation on this plane without its own word.
  *(POST as a QUERY VERB is fine -- `Dashboard/data` and `multiPortfolioGroups` are POST-shaped
  READS that return data and change nothing. The line is MUTATION, not HTTP method.)*
- **NOT other vendors. NOT a standing lift** onto the lifted-vendor list.
- **THREAD-SCOPED** (COO 014327Z): a grant scoped to pursue a question expires with the question.
- **Landing** for anything persisted stays `_ops/probe/`, never a production prefix.

## WHY THIS SENTENCE WAS NEEDED AT ALL

The earlier egress line (~0135Z) was bounded by CTO to the householding thread and its four
exportTypes. The BI plane was DISCOVERED INSIDE that pursuit but is a different surface serving a
different question -- so calling it would have been scope construction, which is the exact class this
seat spent the night refusing. Asking cost one sentence. **This is the second time tonight that
declining a permissive reading produced an explicit grant instead of an unreviewed assumption.**

## FIRST ACTS UNDER IT

1. Mint the bearer from **`bd3/auth/token`** -- NOT `/datamining/auth/token`. Each sibling app mints
   its own bearer (`AUTHENTICATION.md`), and the HAR shows the advisor plane using the former.
2. Reproduce `POST /advisor/api/v1/Dashboard/data` live and confirm the 216-group / Travis
   456,773,323.40 tie-out reproduces against a LIVE call rather than only against his capture.
3. Then the primacy question dim 436 failed to answer: `groupingLevel`, `multiPortfolioGroups`,
   `groupingDetailSearch` -- does this plane yield ACCOUNT-to-group primacy?
