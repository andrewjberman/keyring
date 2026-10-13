# IRPT_ANLREQ -- decomposition, round 22 PROSPECT UPLOAD PAGE (Andrew's own test), workstream YR round 18 (issuer 2.0.0_SA_COO~Y2)

**Input:** Andrew uploaded the sample xlsx on the prospect composer (49 Financial) and reported three defects, filed as rows `IRPT_ANLREQ-D2-S77` and `-S78` by `2.0.0_SA_COO~P2` (msg 7105; screenshots are in Andrew's chat, not the repo): (1) after the upload the page names no file and shows no sign of it -- the in-page input reads "Choose File No file chosen" and the status line reads only "Needs correction."; (2) the proxy box for the unrecognized ticker `TIMXX` says only "Ticker": what to type is unclear, and Andrew expected the page to find a similar security from the Opal database ("Did you mean" showed nothing); (3) "Price date for share quantities" is pointless: the answer is always now, which means the prior trading day's close. The component is `portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx` (read by this seat at portal DEV `cf52fdbf`: the in-page bare file input :419-422, the status line :425-427, the price date field :434-437 and its use :146, :210, :281, the proxy row :472-503, the server suggestion button :484-493).

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-242` | the page names the chosen file and keeps it visible in every state of the upload step; the native "Choose File / No file chosen" text no longer shows on the face | a portal candidate branch (`src/` only) | LOCAL |
| `AR-y-243` | the "Price date for share quantities" field is gone and the page sends no price date, after the serving path is READ to say what it does without one (a candidate branch; a BLOCKING row instead if the server needs the date) | a portal candidate branch (`src/` only) | LOCAL |
| `AR-y-244` | READ ONLY: where the proxy `suggestion` comes from, why `TIMXX` got none, and the sources a "similar security" could come from, each with its cost; the CTO rules which, nothing is built | one record | LOCAL |

## Edges and chains

- None between the cells. `AR-y-242` and `AR-y-243` edit the same component in disjoint hunks (the upload input block against the price date field), so their candidates merge without overlap; each is its own portal branch off the DEV tip.

fanout: 3 of 3 chains, cap 8, reason: three independent cells on one page; two candidate branches, one read.
