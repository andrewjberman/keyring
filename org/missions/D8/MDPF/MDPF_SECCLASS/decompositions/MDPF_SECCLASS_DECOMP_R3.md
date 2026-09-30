# MDPF_SECCLASS decomposition -- ROUND 3 (2026-09-30, issuer 2.0.0_SA_COO~M, on CTO RULINGS 103137 and 103140)

Round 3 holds one cell, E9, which the CTO added while round 2 was in flight. GATE (x) admits one issuance per round,
so E9 cannot join round 2. Standing rulings are as in round 2: Andrew-direct 2026-09-30 ~02:2xZ and the CTO C-WRITER
ruling. Rule 24: the domain is {E9}; one cell with no remainder, same grain as round 2, one intent (bond coverage),
and it moves no served value (dry run + half only).

## The cell

1.0.0_SA_CTO RULING 103137 held the IRPT Holdings canonical release, because 449/826/565 securities would become
unclassified, mostly CUSIP-only bonds. It added E9 to round 2. RULING 103140 fixed the key: `ticker = "CUSIP:<9>"`
plus `identifier_namespace = "CUSIP"`. Before any CUSIP write there must be a census of every scanning reader, and the
write is a conditional put on absence under its own halves.

| cell | item | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `SC-e-9` | E9: the scheduled planner writes CUSIP-keyed rows for held bonds on the prefixed key; census of every scanning reader with its guard; dry-run over the three IRPT firms + half | FWD-2, FWD-7 | NOT-EVALUATED | laptop | WORLD | A, ~4 (after round-2 SC-e-3) |

**Write set.** `_shared/etf_classification_scheduled.py` and its new test. No other round-2 cell writes them.

**Contract.** The contract field `identifier_namespace` in {TICKER, CUSIP} (an absent value reads TICKER) rides
SC-e-1 (amendment 1 of that order).

**Follow-on, not here.** The IRPT Holdings classifier looks a bond node up by `CUSIP:<cusip>`. That is an IRPT_BCKEND
cell, cut after E9's half signs.
