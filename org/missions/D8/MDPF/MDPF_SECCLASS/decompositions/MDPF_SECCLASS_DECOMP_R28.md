# MDPF_SECCLASS decomposition -- ROUND 28 (2.0.0_SA_COO~M1, dell1, 2026-10-17 ~08:0xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers two cells (both read-only cause reads); the served acts that follow are the issuer's own and are stated below, each under its own pair.

**Cut on:** the CTO round-27 analysis, sections 2 and 3
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_27_20261017.md`, `1.0.0_SA_CTO~DELL1` msg 7425, answering the CVO's slug msg 7424 and this seat's packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R27_20261017.md` @a74082a821). The CTO's order of the round, one served change per fire:
1. The S48 cause (ARMED).
2. The S45 leg G cause.
3. The E_18 repoint ship (the re-cut of TO-SC-e108b, superseded @178b4c02ed).
4. The FWD-12 sector writer apply.
5. The D_03 supervised filter and the C_06 full rebuild.

## What is a cell and what is the issuer's own act

- **Item 1 is cell `SC-e-109`: name the input that moved and its writer (a read, nothing is changed).** First pass is already in the record (row D1-S49): the moved object is
  `opal-data-bd gold/canonical/holdings/<date>.parquet`, rewritten for 15 dates by `B_00.canonical_holdings.py` at 2026-10-16T23:15Z and again at 2026-10-17T04:16Z; on 2026-10-02 the sum of
  `market_value` rose 2,023,532,725.44 -> 2,023,940,445.76 (+407,720.32). The cell names the writer's UPSTREAM input that changed between the two rewrites and says whether the rise is right.
  The CTO's candidate inputs (the Cottonwood switch and the carrier re-pull, both 10/15 only) are tested first and a match there is itself a finding.
- **Item 2 is cell `SC-e-110`: why the seed is not visible where leg G reads it (a read).** One finding the cut already holds (measured 07:3xZ): the served firm `unclassified`+`other` on 2026-10-02 is 1,924.34 in BOTH the
  pre-seed and the post-fire versions of `mix_daily_summary.json`, while `seed22_legg_read.py` expects 124,848.36 to leave it (that figure comes from `gold/holdings_lots/<date>.parquet`, and C_06 reads
  `gold/canonical/holdings/`, where the seeded tickers hold 27,668.40 in six rows on that date). So the first candidate for `first_divergence` is `instrument-expectation`; the cell confirms or refutes it
  and states what would make leg G read true. It changes no instrument and no code.
- **Item 3, the E_18 repoint ship:** SC-e-108 is built and drained (@d812b466fd). The ship is the issuer's served act: a new staged order to `0.7.0_AE_CloudOps~DELL1`, cut AFTER cells 109 and 110
  read and under its own pair (the pair at request @5690597b29, CTO half @d245ef138e and COO half @9de34e1632 was cut for e108b and is not consumed; a new pair if the cause reads change its expected move).
  It disarms S42 when E_18 reads 0 old-list-only tickers.
- **Item 4, the FWD-12 sector writer apply:** built (SC-e-28, proof VALID @fdc388f145), not applied. A served act after item 3 and the partners-data repoint, under its own pair. No cell.
- **Item 5, the D_03 supervised filter and the C_06 full rebuild:** NOT cut this issuance, and the reason is stated, not silent: the filter needs `supervised_scope.filter_supervised`, whose module is not at this
  seat's HEAD (4.0.0_SA_CRO~DDD's commit @62badadb7b is on its own branch; the CTO ruled the filter lands after that deploy, msg 7160), and `D_03.composition_artifacts.py` carries no function named
  `_load_holdings_from_canonical` at HEAD (the CRO's note names it). An unmet dependency, so no cell: it is cut at the recut after the module lands, or at the next round. The C_06 full rebuild is a served act
  with its own pair.

## Rule 24 record

- **Domain:** the CTO's five items; two cells; the issuer's served acts after them.
- **(ii) Same grain:** each cell is one read that ends in one JSON file graded by one committed script.
- **(iii) Intent coherence:** the check recomputes the numbers a claim rests on from S3 (the object versions, the served versions); it never grades prose.
- **(iv) State coherence:** neither cell writes AWS, deploys, or edits a script. A cell that finds the cause WRONG does not roll anything back: roll-back per key is a later order under a pair.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-109` | `S48_CAUSE.json`: the writer and the upstream input that moved between the 23:15Z and 04:16Z rewrites, the reconciled delta, RIGHT or WRONG | FWD-1 (the served firm mix) | LOCAL, direct act | none |
| `SC-e-110` | `S45_CAUSE.json`: the first divergence between the seed and leg G's reading, with per-ticker canonical numbers and the served numbers, and the stated fix | FWD-1, FWD-5 | LOCAL, direct act | none |

Each acceptance check is a committed script under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R28_CHECKS/` (read-only to the workers), self-tested with a green arm and negative arms, and dry-run at the base (both print `ok=False`, no file).

## Write sets (disjoint)

- **SC-e-109:** `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~99/S48_CAUSE.json`.
- **SC-e-110:** `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~100/S45_CAUSE.json`.
- Both also append to the project's surprise channel.

## Chains

Two cells, no edge: two chains. Fan-out 2 of 2, cap 8. Slots ~99 (SC-e-109) and ~100 (SC-e-110), `worker`, haiku (treatment box, MP-20261010).
Deadline: the S48 cause is named by 22:00Z 2026-10-17 or the 23:00Z SECCLASS fire is disabled for one cycle under a NEVER-2 ledger (CTO msg 7422).
