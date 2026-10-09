# IRPT_ANLREQ workstream TICKET (~V2), round 2 -- L8 PACKET

**Compiled by** `2.0.0_SA_COO~V2`, 2026-10-09 ~08:1xZ. **For** `3.0.0_SA_CVO` at L9, as a FILE. This is not the L10 slug.

**Authority:** `decompositions/IRPT_ANLREQ_DECOMP_R2.md` @cff0872f0f (AMENDMENT 1 @77d85c7fd7, the one I7 sample); the CTO's round-1
analysis (msg 2770) rulings 2-5.

`round-close-check.py --project IRPT_ANLREQ --round 2` (all lanes): `orders=5 judgment=0 ungraded=0 verdict=MAY-CLOSE`.

## 1. Terminal order

| order | cell | risk | instance (`deliverables/`) | issuer re-run on the merged state | landed |
|---|---|---|---|---|---|
| TO-AR-v21 (+ AMENDMENT 1 @65f2c52985) | AR-v-21: Branded PDF reader; I5' custody sentence; I7 refs on the package route and the page | WORLD | `0.9.0_WK_IRPT_ANLREQ~21/IRPT_ANLREQ.TO-AR-v21.package-pdf-reader-i5p-i7.proof_of_spec.json` (VALID) | on box/dell2 53cbcad426: `V21-PACKAGE-OK passed=5`, `REGRESS-OK passed=147 failed=0`; on the synced worker branch: `V21-PAGE-OK pass=4`, `PORTAL-TSC-OK rc=0`, `V12-PACKAGER-OK passed=6` | workspace drain @53cbcad426; portal DEV `d06ae384` (CTO msg 2826; landed by MSTR~DELL2, ls-remote read by the issuer) |

The contract test reads `deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json` at test time and round-trips it both ways. The portal test carries
the same canonical string as a literal, because the portal cannot read the workspace.

## 2. Rows filed this round

- **D2-S4 and D2-S5** (@651316fe8d): the dispositions of W11-S1 (ARMED, disarmed) and W11-S2, as the analysis asked. Both are
  DISMISSED_WITH_REASON on grounded evidence; the CVO's L9 is the adjudicating read.
- **D2-S6** (@dc8c27e96d), **BLOCKING**: there is no server reader for Commentary or Original file, so "four files opened" cannot pass from
  this cell. `~Y2` asked the CTO for an addendum (msg 2811): AR-y-22, an original-file reader, with the commentary read inside the PDF.

## 3. What is owed, and when

- **No judgment criterion on AR-v-21.**
- **The ticket_center half is not live.** It ships in an `opal-ticket-api` release AFTER V12 (pinned to 86454002bf, pending at
  `0.7.0_AE_CloudOps~DELL2`), under its own never-widen pair. `~O2`'s OW-l-1 (trade_request) is also at HEAD and also waits on a ticket
  release.
- **Client-facing.** The Ticket Center is client-facing (CTO msg 2826), so the portal half is DEV only; PROD waits on Andrew.
- FWD-1's grading run (the CVO reads one live journey) follows the four releases named in DECOMP_R2.
