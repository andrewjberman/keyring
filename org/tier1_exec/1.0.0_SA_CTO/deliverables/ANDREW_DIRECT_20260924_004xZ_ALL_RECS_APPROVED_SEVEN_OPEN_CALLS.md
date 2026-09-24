# Andrew-direct 2026-09-24 ~00:4xZ at the 1.0.0_SA_CTO terminal: "all recs approved" (seven /open-calls cards)

Received directly by 1.0.0_SA_CTO (Claude) at its terminal, 2026-09-24 ~00:4xZ, answering the
/open-calls card set this seat printed at ~00:40Z (7 calls). Recorded at 2026-09-24T00:45Z.

Andrew's words, VERBATIM:

> all recs approved

## The seven cards, as answered

The word approves the REC on every card. Each card's call and REC are repeated here exactly as
printed, so the ruling each approval creates is unambiguous.

CALL 1 -- Attest that all 49 Financial report amounts are USD? (yes/no)
REC -- yes. The custodian is Schwab US and every landed source is dollar-denominated.
RULING -- YES. 49 Financial report amounts are USD on Andrew's explicit firm-level word. Same scope
and limits as the Cottonwood attestation (ANDREW_COT_USD_20260923.md): report amounts only; not a
vendor-returned field; no FX; missing values stay missing.

CALL 2 -- Attest that all Inflection report amounts are USD? (yes/no)
REC -- yes. The vendor's retained Scope responses already say USD.
RULING -- YES. Inflection report amounts are USD on Andrew's explicit firm-level word, corroborated
by the retained Orion Scope bodies (currencyCode USD, 25 of 25) and the tenant multi-currency setting
(off). Same scope and limits as above.

CALL 3 -- Per-use word for ONE live Cottonwood performance calculation (Anna, 2026-09-01 to
2026-09-22) through the installed adapter? (yes/no)
REC -- yes, bounded to that one account and window.
RULING -- YES, ONE USE: account acc_d486fc9455d6b2aa18e13af1 (Anna, Cottonwood), window
2026-09-01..2026-09-22, through the installed irpt-performance-adapter under a server-installed
one-use plan (authorization.py); X10 enforcement accepted before the call fires. Any other account,
window or second attempt needs a new word.

CALL 4 -- Keep the AutoShutdown=disabled tag on the YCharts host i-0167fd745ad906a66? (keep/veto)
REC -- keep.
RULING -- KEEP. The tag is the conscious per-instance opt-out of the earlier "ZERO such tags"
directive for this one always-on host. The host still starts only with the resident cutover plan.

CALL 5 -- Per-use word for one live Orion Reporting/Scope calculation for a real Inflection client?
REC -- yes, one client, one window, when P presents the exact request.
RULING -- YES, ONE USE, bound at execution time to the exact client, window and request P presents
in its install receipt; no second call without a new word.

CALL 6 -- 49F SmartX account-level performance for a real client: (a) one bounded live call under
yaliu-bundle when P presents it, or (b) hold?
REC -- (a).
RULING -- (a), ONE USE, bound at execution time to the exact account, window and request P presents;
the provider's period-to-date result labelled as such, the selected-set limit disclosed.

CALL 7 -- Push local CLOUD to origin now? (yes/no)
REC -- yes.
RULING -- YES. 0.0.0_AB_MSTR pushes workspace CLOUD to origin on this word.

## Routing (same turn)

- P: writes the 49F and INF ANDREW_ATTESTATION records into CurrencyAuthorities.json citing this
  record; prepares the one-use plan for CALL 3 for CTO review before the env change lands.
- M: on P's two records, requests the 49F and INF exact-write GOs with the measured write plan.
- MSTR: pushes CLOUD (CALL 7).
- CRO: FYI on CALL 6 (its capture plan's choice 2 is now also approved for one live product use).

Scope surfaced, not adjudicated: each approval is exactly the card's REC; nothing wider is inferred.
