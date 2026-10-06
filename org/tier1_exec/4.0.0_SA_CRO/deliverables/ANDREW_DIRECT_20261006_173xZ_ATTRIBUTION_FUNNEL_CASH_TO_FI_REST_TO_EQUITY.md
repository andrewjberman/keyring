# ANDREW-DIRECT 2026-10-06 ~17:3xZ -- Attribution funnel: Cash -> Fixed Income, every other class -> Equity

- Channel: Claude Code terminal session, seat 4.0.0_SA_CRO~X (Andrew at the terminal, overseeing the edit in-session).
- Recorded by: 4.0.0_SA_CRO~X, same turn.

## Verbatim

"What i need from you today is a very surgical edit that you will pursue with me in the session here to oversee. THe
premise is in the "Attribution" page on the opalinvest.dev portal. The issue that we are encountering is that in our
asset taxonomy there are more asset classes than just equity and fixed income, however the way we manage attribution is
by splitting into equity or fixed income. Because the opal models only invest in equities and fixed income, this has
historically always been fine. The issue becomes when we split cash out from fixed income, and "structured" out from
equity. We need something in the lambda or whatever server side processing puts together the calculations for that
where there is a funneling action. The way i would handle that is via the following rules. 1.) If a "Cash" tagged item
appears in a model, that is included in the "Fixed Income" side of the attribution. 2.) If there is any other tagged
item in the model (e.g. Alternative(s), Commodities, or Structured), these are included in the equity side of the
attribution. Please assess the yang pipeline as it refers to the attribution aspect of the portal, and see how we can
incorporate this ruling."

## Scope as given

- Surface: the portal Attribution page; the server-side attribution processing in the yang pipeline.
- Rule 1: Cash -> Fixed Income side. Rule 2: any other non-Fixed-Income class (Alternatives, Commodities, Structured,
  ...) -> Equity side.
- Mode: surgical, pursued with Andrew in-session. This record is also the explicit data-engineering directive the
  2026-10-03 relayed order requires before any data-ops change.
