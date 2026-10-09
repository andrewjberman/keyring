# ADVI_COTBKF round 43 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~14:5xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_43_DRAIN_END_20261009.md @7f2f3d7323 (msg 3499)`. Row D2-S66.

| criterion | verdict | evidence |
|---|---|---|
| CB43aq1-AC2: one entry added, no firm token, values admitted; the producer's compute path proven not to pick it up; IRPT_DASHBD's tests green | MET | `sources.json` gains one key, `_commonwealth_delivery`: registry_key z09, positions-times-as-traded-close valuation, net of fees, as-traded basis, and no firm token. The rule commit precedes the output. `account_return_daily.py:291` `declared_sources()` returns only non-underscore object keys; this seat read `sources.json` and the one declared source is `schwab_08335338`. `:300` `source_entry()` refuses anything else. The issuer's test runs: producer 102 passed, handler 86 passed |

**Open (W70-S1, for the CTO):** every manifest says `method_version: 2` (custodian equity) beside Cottonwood's positions-based fields. Rule it
before the mint.
