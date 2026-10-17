# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-17 00Z (host opal_bloomberg)

## Substantive ticks since the 21Z log

- OG-en-17 merged (4ebc1e781b); its four worker rows (Z-W129-S1..S4) dispositioned (Z-S331..S334, committed 6afee9e55b): S1 issuer spec error accepted (396-day window is the max), S2 newest-first disclosed in the ask, S3 next_cursor null at end of data, S4 test_og_ch1 red carried.
- OG-ap-32 Phase A (0.7.0_AE_CloudOps~NFRA1, msg 35302): re-cut release 11031f278d, ask sha256 82e211ff...4be3, ap32.AC1 PASS. Measured on the host: a 60-partition page holds all rows at once (+470 to +550 MB, one page 55-59 percent, two overlapping pages 85-100 percent, no swap); first transactions page predicted ~43 s against the 30 s arm.
- Ruling: the defect is the issuer's (OG-en-17 cell text). Halves stopped; release 11031f278d and that ask superseded. HOLD sent to ~NFRA1.
- Cut OG-en-18 (commit 887e203b8c, ENRICH-R40-R, worker ~130, WORLD floor): per-partition account filter inside the pool task, PAGE_PARTITIONS 30, process-wide window gate with `window_read_busy`. Addendum R3-T.104; OG-ap-32 Amendment A1 (take list, widening text, e1 arm: partitions_read 30, ~12/~14 pages). Checks dry-run at base: en18.AC3 and AC1 FAIL as expected. fanout: 1 of 1 chains, cap 8.
- Worker ~130 spawned (haiku, high) in C:/tmp/wk-oplgtw-130 at 887e203b8c.

## Next

Merge OG-en-18 (safe-merge wk-NFRA_OPLGTW-130), re-run the window tests both orders in the main tree, new Phase A GO to ~NFRA1 with the new trunk_sha, then halves, Phase B, ap32.AC2, MI and MP told the live commit, CVO relay of bodies for AC3.

Carried: Andrew's browser run for OG-ap-30 (Z-S312 ARMED), Z-S313, Z-S322/S325, Z-S177, Z-S328, ten CVO-graduated armed rows awaiting DISARM, round-39/40 L10 slug after every order is terminal.

Push state: LOCAL (no push this hour; box/sitez ahead of origin).
