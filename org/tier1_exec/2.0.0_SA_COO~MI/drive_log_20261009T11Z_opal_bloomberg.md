# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX: MX-r-9 PHASE A drained, PHASE B staged on ~MX, round 9 staged, round-close proofs repaired -- 2026-10-09 09:0xZ-11:2xZ (host opal_bloomberg)

**archetype:** COORDINATE

## Ticks and events

| time | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| 09:24Z | L7 | 8 | 3/4 | ~28 PHASE A at its final re-reads |
| 09:5xZ | L7 | 8 | 3/4 + r-9 PHASE A | PHASE A drained @b70a673984. The ANNOUNCE is on live aa75078e1b (3 reads). 2 files ship. Integrations 7=7, `.env` keys 51=51. Suite: 38 failed on both sides, 0 new. Amendment A1 @1dd356991a re-addresses PHASE B to `0.7.0_AE_CloudOps~MX`, re-cut on the live ref at apply time. Z-S89 disarms Z-W28-S7 |
| 10:00Z | L7 | 8 | 3/4 | EMPTY at the limb, so `/next-calls --drive` ran. Call "issue round 9 now?" was queued; `1.0.0_SA_CTO~Z` ruled NO @ff362e8444 (one open round per issuer; stage it unissued). J1 booking asked of `0.0.0_AB_MSTR~Z`. Round-9 battery and 4 drafts staged @f4cc1c96d4; every check FAILs at base as expected. The box-sync hold (msg 32647) was answered: already committed |
| 10:24Z | L7 | 8 | 3/4 | round-close-check round 8 read REFUSED: PROOF-BAD 3/3, a short `to_id` against the stem fallback. Fixed with `<to_id>` tags on the orders and drafts @4f76167f48: proof_ok 3/3, MAY-CLOSE |
| 10:54Z | L7 | 8 | 3/4 | The same fix on 12 orders of rounds 5-7 @bef0ea79e4. Round 5 1/1 and round 6 6/6 read MAY-CLOSE. Round 7 has 5/5 proofs but stays REFUSED on one ungraded judgment, TO-MX-a-1 AC2 (the CVO's L9) |
| 11:0xZ | L7 | 8 | 3/4 | `2.0.0_SA_COO~O` msg 32683: box/sitez carries ADVI_BILLING E2's unreleased `copy_site_file_to_s3`. MX-r-9 A2 @52db820bbf: run the live ref's deploy script; tool and `.env` key sets EQUAL, or STOP. ~MX was told |
| 11:24Z | L7 | 8 | 3/4 | r29 pre-steps are moving: the nfra-oplgtw-r29 secret-grant ledger closed @8eefd927c2. PHASE B GO still waits on OG-rl-15 |

## Carried to the round-8 drain-end read

- The opal-gateway suite RED at base (Z-S88; plus NFRA_OPLGTW-Z-W47-S2's 3 suites); owner `2.0.0_SA_COO~O`.
- Q05's routing-harness key should accept a need id (an instrument repair, batched).
- Round 7's ungraded judgment TO-MX-a-1 AC2.
- The MX-a-1 id collision: the laptop analysis-portal order and the round-7 bd-run-shape order.

## Compiler Tools

- `round-close-check.py` rounds 5-8: found the proof binding defect. The numbers in the table are measured before and
  after the fix.
- `open-calls.py add`: the call was scoped CROSS-BOX and ruled the same hour.
- `unblock.py tick` x2: KEEP-DRIVING, 0 empty ticks.
- The rail refused a heredoc generator and one grep; both were re-run in the admitted forms.

Push state: all of 1dd356991a, f4cc1c96d4, 4f76167f48, bef0ea79e4 and 52db820bbf are on origin. origin box/sitez read
6a02d46287 at 11:26Z (ls-remote), checked by is-ancestor.
