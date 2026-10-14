# R16-cw2 AC1 re-run under AMENDMENT 2 -- 0.7.0_AE_CloudOps~TV2

## Objective
Record a passing AC1 for `TCKT_VNEXT.TO-RUN-R16-cw2` after the issuer fixed the check (AMENDMENT 2, GO msg 7565).

## What happened
- Ran `python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R16_CHECKS/r16_cw2_close.py` as written, rc=0. Printed line, verbatim:
  `CW2-OK two tickets completed by the identity; row absent after exp; card-1 ticket never claimed by the identity`
- Confirmed the two fix commits exist locally: 12ba66c52b (absent item parse) and 6ab1df0771 (card-1 clause as an invariant).
- Set AC1 `output_evidence`, `status` (PASS) and `status_reason` in the one proof file; first FAIL text kept as history; updated the `r16_cw2_close.py (AC1)` compiler_tools row. Instance validates VALID (rc=0).
- Flipped the order `<status>` to `complete`.
- No ticket, row, table, secret, code or ledger write; no browser; no token.

## Findings the issuer should read
None new.

## Compiler Tools
- `r16_cw2_close.py` -- AC1, rc=0, CW2-OK.
- `.tools/proof-of-spec-check.py` -- instance VALID (rc=0).
