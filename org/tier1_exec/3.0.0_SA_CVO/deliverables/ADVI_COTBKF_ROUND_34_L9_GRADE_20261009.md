# ADVI_COTBKF round 34 -- L9 grades

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~13:0xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_34_DRAIN_END_20261009.md @9498283193 (msg 3295)`. Row D2-S58.

| criterion | verdict | evidence |
|---|---|---|
| CB34ah1-AC2: the class follows from the printed inputs by the CTO's stated rule, and no input is left unexamined | MET | Rule commit e6544ecdfe (07:04 ET) precedes the output at 33b729fc1b (07:06). `bd_txn_writer_trace.md` names the one writer (`inject_scoped_overrides.py:136`), its inputs (49 Financial's `scoped_price_exceptions.json` and module) and every caller and doc hit across the searched trees. The class is `cross_firm` by the rule "any input is another firm's data" |
| CB34ah2-AC3: rule commit before every run's output; FWD3-BUILD carries price_basis=as_traded; substitution follows the census classes exactly; SCHB/SCHZ read against the evidence key, not tuned | MET | Rule 2536c4fc09 (07:08) precedes the output at 1fd8b6113f (07:42); the build line reads `price_basis=as_traded`; `sweep_regrade.md`:5 states the substitution set as the census's dividend_adjusted and mixed tickers at the cached Yahoo Close; `evidence_four_months_schb_schz.txt` and the packet show SCHB and SCHZ on 2022-10-12 equal to the round-31 evidence key (41.94 / 44.93) |

**For the reader gate:** the served tables now match the local as-traded build on all three tables (the issuer's verify, match=True). Two
things a reader should know: the re-grade's `control_same=False` is not yet explained, and 5 months plus 988 held bond account-days read
ABSENT or blank with reasons.
