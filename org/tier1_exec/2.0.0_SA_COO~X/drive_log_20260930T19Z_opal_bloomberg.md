# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 19Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 18:58Z-19:0xZ | L8 | 25 | aa-4, as below |
| 19:1xZ | L8 | 25 | aa-4 leg d: 0 writes. `dossier.py:927` / `:966` reads the RAW key (the kept 09-25 copies); row `Z-S71` filed ARMED |
| 19:14Z | L8 | 25 | aa-4 leg v, as below; deviations file `b00b96102f` asked of the CTO (27338) |
| 19:26Z | L8 | 25 | CTO YES on both (27343, AMENDMENT 2 `323ccd85be`); aa-4 ledger CLOSED; packet `5fe52a896a` to `3.0.0_SA_CVO~Z` (27347) |
| 19:49Z | L9 | 25 | packet OFFER-EXHAUSTED; the CVO seat LIVE (PID 9420) with a stale Working-on line |

**aa-4, 18:58Z-19:0xZ:** the CTO's YES on the closure reading (27330); the act-start diff re-read in its own call (2 out-of-closure
paths); the expected blocks captured; the derive (`190146Z` / `190147Z`); leg c CLOSED (both blocks equal their dry runs, counts equal
to the pair, 18 signs match their values).

**aa-4, leg v at 19:14Z:** `/thesis` at the identity form serves the new blocks (BP `PROF_MARGIN` UNRESOLVED, BP case ABSENT, NG case
1,298.21). The BP payload carries 778.57 in the ABSENT case's inputs.

## Compiler Tools

- `aa4_verify.py capture|compare`, `d25.py` (`D25_KEYS`), `capture_lib._invoke` (identity form), and `dossier.current_inputs`.
- Gaps:
  - `/thesis` resolves the identity form, not the encoded form (the first read hit an UNRESOLVED identity);
  - a commit retry loop hid a gate BLOCK (fixed in `commit_retry.sh`).
