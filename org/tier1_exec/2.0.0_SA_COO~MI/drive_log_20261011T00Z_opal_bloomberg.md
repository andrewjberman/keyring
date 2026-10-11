# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX: round 9 drains o-2, x-6, o-1, c-7; both FWD-19 readers GAP; r-10 PHASE A running -- 2026-10-11 00:0xZ-01:0xZ (host opal_bloomberg)

**archetype:** COORDINATE

## Ticks and events

| time | act |
|---|---|
| 00:2xZ | MX-o-2 drained @92dc842a98 (~31): billing census GAP. 6 candidates; owner ADVI_BILLING; no paid status exists in any object; no reader. o2.AC1-3 PASS re-run in the worker tree; instance VALID. Tree and branches removed |
| 00:5xZ | MX-x-6 drained @ea11910486 (~32): the emitter refuses a census dir outside its checkout (the worker's revert control fails only the refusal test). Suite baselines: full 41 failing IDs, sparse 99. x6.AC1/AC2 PASS re-run; VALID. Tree removed |
| 00:5xZ | MX-o-1 drained @bac72d2e3a (~30): trade-rec census GAP. 8 candidates; owner unowned; the nearest is Orion, with 1 status from 1 system and null order IDs on 1,520,347 rows. o1.AC1-3 PASS re-run; VALID. Tree kept for c-7 |
| 00:58Z | Z-S98 @88719444bc rules W30-S1 and W31-S1 (confirmed: served = serves the shape) and W32-S1 (disarmed: baselines 41/99; sparse runs need --continue-on-collection-errors). Z-S97 was already taken by 0.0.0_AB_MSTR~Z |
| 01:0xZ | ~30 continued on MX-c-7. Schwab and grant failing IDs sent to `2.0.0_SA_COO~O` |
| 01:1xZ | MX-c-7 drained @fbeb5b628b: E-30..E-35 all GAP. E2: FWD-18 3 of 14; C3 carried 3 of 3; folds 0 (replaced by one general exact-example rule); E-13 guidance carries 5 of 5 model codes; routes 10 of 10. c7.AC1-3 PASS re-run; VALID. FIRST suite-delta drain: full suite 41 failed / 711 passed, so new 0, fixed 0, baseline 41 |
| 01:1xZ | ~30 continued on MX-r-10 PHASE A. The ANNOUNCE states no ENABLED_INTEGRATIONS change, 2 files shipped, the live ref read from the host by md5, and the ruling-2c procedure |
| 00:50Z | `2.0.0_SA_COO~O` 33107: MX-r-10's slot is after ledger `nfra-oplgtw-gateway-release-e2` closes (OG-rl-16 / OG-ap-6, B2 in the 11:00Z window). PHASE A's pins re-cut on the post-rl-16 ref at the slot |

## State

- FWD-19 is NOT done this round: both readers are GAP. FWD-18 and the E-13 guidance ride MX-r-10's release.
- J1 is HELD at Andrew (Alyssa). MX-s-19 runs s19.PRE on 2026-10-13 after 03:00Z.

## Compiler Tools

- `safe-merge.sh` x4, fast lane, each with a tree check and an index check.
- `proof-of-spec-check.py` on each instance. My first call passed the order file instead of the instance JSON and read
  READ-ERROR; the re-run on the instance read VALID.
- `tests/suite_delta.py --report ... --shape full`: its first real use, at the c-7 drain.
- `wk-provision.sh remove` x2.
