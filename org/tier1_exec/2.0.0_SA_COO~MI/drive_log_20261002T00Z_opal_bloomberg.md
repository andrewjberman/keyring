# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-01 20Z -> 2026-10-02 00Z (host opal_bloomberg)

Lease FULL. Round 6 closes at L7; the L10 slug was released to 3.0.0_SA_CVO~O. Thread y.

## Decisions closed this span

- **MX-s-16 first-night read (22:24Z):** the unrealized and allocation documents did not fire (rules DISABLED); the
  held transaction (21:53Z) and realized (21:46Z) legs fired Success.
- **MX-s-16 acceptance MET:** the scheduled `bd-silver-merge` run, invoked 2026-10-02T00:11:36Z, read
  - unrealized `failures=0 empty_stub=6` (it was `failures=6` nightly);
  - transactions `failures=0` (246,777 rows); realized `failures=0` (9,172 rows); allocations `new=0`.
  - Row Z-S76 disarms Z-S72.
  - Ledger `nfra-mcpindex-r6-bd-merge-retire` CLOSED 8/8.
  - A3 scopes AC1 to the A2-retired tables: 2 of 2 PASS; the unscoped control reads 2 of 4 FAIL, by design. Committed
    @83439586fe.
- **MSTR~Z's /integrate quiet window** (msg 28101, Andrew-direct) was observed. PARITY was read at 0257976705
  (msg 28114).
- **MX-s-16 COMPLETE:** worker ~24 @1a46894921 (proof VALID, 0 pending); drained @e24ef2b9d0. Issuer re-grade on
  CLOUD: AC1 2/2 PASS, AC3 PASS, proof VALID.
- **ROUND 6: 6 of 6 terminal** (MX-d-6, MX-g-3, MX-r-8, MX-v-7, MX-x-4, MX-s-16). The CVO was told the held slug can go
  (msg 28123, READ 00:50:22Z).
- **Push:** CLOUD pushed by MSTR~Z at 21:27Z (origin 25f4ac5418); parity at 0257976705 at 00:43Z.

## Open

- r6.J1: Alyssa's cold run (booked via MSTR~Z). Owed to COO~MP: the sitting time, then "captured" (G-CLOSE sequenced
  after it).
- The CTO's round-6 L10 analysis -> the round-7 issuance. The round-7 release must export `OG_TAXSMA_WORKBOOK_IDENTITY`.

## Compiler Tools

- `deploy_ledger.py` close-leg/close; `safe-merge.sh`; `proof-of-spec-check.py`; the round-6 battery (s16.AC1 scoped).
