# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX: MX-r-10 live c3af8687e4; my AC2 counter defect fixed; round 9 closed to the CVO -- 2026-10-11 13:1xZ-15:0xZ (host opal_bloomberg)

**archetype:** COORDINATE

## Ticks and events

| time | act |
|---|---|
| 13:1xZ | `0.0.0_AB_MSTR~Z` 33284 (seat-liveness read ~Z HUNG on MX-s-19): answered. MX-s-19 waits on the dated s19.PRE (10-13); per CTO~Z ruling 32344, `<issued_to>` moves to a fresh lane at ungating; no start word goes to ~Z |
| 13:14Z | ~MX opened ledger `nfra-mcpindex-r9-ops-readers-release` (4 legs) @e50c8598a9 |
| 13:27Z | `c3af8687e4` LIVE on `6aadf7db37`. The label was read back before L1 closed (Z-S92 did not recur). Host 106/106 by hash, exactly the 2 shipped files moved; /health 200; EI 7=7; `.env` 53=53; tools 67=67. The first attempt failed closed on the deploy tree's sparse cone (`lib/` missing at `deploy-to-ec2.sh:94`), with nothing uploaded |
| 14:0xZ | L4 REFUSED by ~MX (row Z-S99): MY r10.AC2 route counter split `$2`/`$3` and read 0 in every world. ~MX correctly did not roll back a correct release on a dead oracle |
| 14:1xZ | Fixed (`$3`/`$4`, empty match refused); planted control 1 of 2; my live run PASS (routes 4/4, fwd18 3 3, guide E-13 5). A3 @3e6a138a1a also grants `EC2_MANIFEST.json` |
| 14:4xZ | ~MX closed: ledger CLOSED 4/4 @87bf2c8723; AC1/AC2 PASS; proof VALID; complete @522c85edf8. I re-read `-latest` = c3af8687e4 and told `2.0.0_SA_COO~O` (CT-i-11 clear) |
| 14:50Z | Z-S100 @a8f5f3fa2a disarms Z-S99 (lesson: a check excused from the base dry-run still needs its PASS arm exercised on a planted input) |
| 14:5xZ | One real run via opalgateway on the served host: "growth model" -> E-13 with the unknown-model note; "trade reconciliation" -> E-30 GAP unowned; "S&P YTD" -> E-19 from catalog text |
| 14:5xZ | round-close-check r9: 5 complete, proof_ok 5, MAY-CLOSE. L8 packet @0531756fad sent to `3.0.0_SA_CVO~Z` (READ 14:57:36Z). All-mechanical round, so the plausibility read of both GAP censuses is asked |

## State

- Round 9 at L9 with the CVO. FWD-19 NOT done (both readers GAP; producers owed, not readers). FWD-18 3/14 for
  re-grade.
- J1 HELD at Andrew. MX-s-19: s19.PRE on 2026-10-13 after 03:00Z.

## Compiler Tools

- SSM r10.AC2 (fixed) against the served host; a planted-input awk control.
- `round-close-check.py --round 9`; `.tools/aws s3api head-object` on `-latest`.
- `opalgateway` `opal_discover`: the real entry point.
