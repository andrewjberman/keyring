# ANDREW-DIRECT 2026-09-24 ~05:4xZ -- Analysis may be for a totally NEW client; the layout must carry that

**Channel:** the `4.0.0_SA_CRO~F` terminal, mid-turn, after the area-chart addendum was committed.
**Received by:** `4.0.0_SA_CRO~F`. **Relayed to:** `1.0.0_SA_CTO`, `0.0.0_AB_MSTR` (DSGN_IRPTV1 brief addendum for L2).

## VERBATIM

> Another thing to keep in mind is that in the context of "Analysis", the analysis done may not be for an existing client, it could be for a totally new one. so I'd keep that in mind when it comes to how its laid out.

## What it changes in the concept and the brief (surfaced, not adjudicated)

- The served page already lets Analysis mount without a selected client (`TabShell.tsx`: Reporting and Holdings require a
  server-accepted scope; Analysis does not) and the stepper concept (CONCEPTS s.2.4) already offers "Upload a portfolio"
  beside "Selected client holdings" at step 1. What this word adds is FRAMING: a prospect is a first-class SUBJECT of the
  page, not the absence of a client.
- Brief O6 amended: (i) the Analysis tab is reachable and complete with NO client selected -- the header shows a
  "Prospect" identity card (the uploaded portfolio's name / prepared-for, its as-of, its normalized total) in place of a
  client card, never "No client selected"; (ii) step 1 leads with the prospect path when no client is selected and with
  the client path when one is; (iii) the history rail lists prospect reports under the advisor's ownership (the
  contract's owned-request semantics: prospect ownership comes from the authenticated API, never the selected client),
  so a report for a new client is found the same way as one for an existing client; (iv) a prospect report can be
  RE-OPENED and RE-RUN later without re-uploading (the retained normalized input), so a prospect who becomes a client
  keeps their history.
- Data on the wire today: `uploadAnalysisInput` -> normalized portfolio (rows, total dollars, valuation basis);
  `listOwnedAnalysisRequests` (owner-scoped history); `AnalysisRequest.settings` / prepared-for text. The prospect's
  NAME as a first-class field exists only as the `prepared_for` display text (IRPT-MAINTAINED-SOURCE-02); whether the
  identity card needs a dedicated prospect label on the wire is a Part IV.3 data question for the CTO at L2.
