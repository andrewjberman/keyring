# TCKT_VNEXT TO-R21-RB1 -- Trade attachment byte read-back on PROD (0.7.0_AE_CloudOps~TV2)
**archetype:** DEPLOY

Result: RUN-OK (tradejourney). ONE attempt, GO msg 11390 (AMENDMENT 4). Ledger `tckt-vnext-r21-rb1b-20261020` CLOSED, 6 of 6 legs.

- Start gate 15:31Z to 15:44Z: check-inbox; PROD head 4546cee0528c (CI run 39438860151 success, DT msg 11397 none in flight); site 200; census 44 trees, 0 other live ledgers naming the surfaces; CTO 11398, DT 11397, Y2 11400 none; IB2 silent 10 minutes (reads none per the order); offline proof re-run 15:36Z OK.
- Run 15:45:01Z to 15:48:07Z: filer row written, one token (180 s, never printed); TCK-20261020-645d7017 filed (door 200, PUT 200, ticket 201); Open 200, body keys [expires_in, filename, url]; plain GET of the url; SHA-256 uploaded == read back b0b2b41f6ccc3d552457c98840b0b47a3415781f9a36aa0d8600a5aca8a73455 (31 bytes).
- After exp: ticket saved whole then deleted by key, filer row deleted, both ConsistentRead ABSENT. Object left: key `portal/cottonwood/state/ticket_attachments/trade-form/85de6b5ed04b4ac5a14ea677949c1981/tckt-r21-trade-synthetic.csv`, version `lway93Q_YhLuvb25e3M__smeGKeFABbC` (fourth residue, CTO row 6e7c).
- Check blob 9167d289eb: R21-TRADEJOURNEY-SELFTEST-OK beside RUN-OK (tradejourney).

## Compiler Tools
- `deploy_ledger.py` open, close-leg x6, close: worked. `r21_offline_proof.py`, `r21_trade_prod.py`, `r21_tradejourney_check.py` (and `--self-test`): worked. `safe-commit.sh`: refused the complete flip until a proof-of-spec instance sat beside the order (written). Gaps: none.
