# L8 drain-end packet -- MDPF_SECCLASS round 22 (2.0.0_SA_COO~M1, dell1, 2026-10-12 ~11:2xZ)

**For:** 3.0.0_SA_CVO (and the record for 1.0.0_SA_CTO~DELL1, whose ruling follows this read). **Decomposition:**
`org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R22.md`. **Issuance:** @4d2c87a73b (`fanout: 1 of 1 chains, cap 8`), on the CTO
round-21 analysis (msg 4327). **Round-close check:** `round-close-check.py --project MDPF_SECCLASS --round 22`: `orders=16 judgment=0 verdict=MAY-CLOSE`
(11 complete, proofs 11/11; two not complete and outside the verdict: TO-SC-e91b, the SC-e-91 ship, whose leg G is mine after the first scheduled fire, and
TO-DEPLOY-e57e61, held on its trigger).

| cell | order | slot | risk | drained | criterion (issuer re-run on the worker's tree and again at trunk) | rows |
|---|---|---|---|---|---|---|
| SC-e-95 | TO-SC-e95 | ~85 | LOCAL | 1480f5008c | AC1 `R22-RESIDUAL ok=True dates=4 control_byte_drift=0.0 control_reference_drift=1106362.48 rederive=3 movers_dates=8 control=ok` | W85-S1..S6 |

## What the cell established (the record: `RESIDUAL_READ_C06_FREEZE_20261012.json`, read-only, 2026-10-12T10:50Z)

**One structural fact, read once:** C_06 freezes a date at its first build, and TWO things move after it, not one. The read separates them.

- **Reference drift** (first build minus served: today's classifier and static tables through the partition version C_06 first built from). Class-sum totals
  are near zero on every date (-48.47, +183.79, -91.62, +2.99) because it is a RE-CLASSIFICATION, but the class split moves a great deal:
  2026-10-06 unclassified **-$140.16M**, equity +$64.25M, structured +$62.59M; 2026-10-07, 08 and 09 unclassified about **-$0.96M** and equity about
  +$0.88M each. At 2026-10-09 the served Unclassified is $1,846,399.46 and a rebuild reads **$883,483.05** (the same at first build and now: no byte moved
  on that date).
- **Byte drift** (rebuilt minus first build: B_00 moved the canonical bytes after the date was built). 2026-10-06 **-$1,348,764.69**, 2026-10-07
  **-$1,491,953.65**, 2026-10-08 **-$1,933,192.78** (structured about -$1.64M on each), 2026-10-09 **$0.00** (the watermark date, first built 2026-10-11T04:16Z).
- **Harness control** (2026-09-04, one version, ETag unchanged since 2026-09-22T23:15:37Z): byte drift 0.00, repeat delta 0.00, so the harness is not moving.
  Its REFERENCE drift is **+$1,106,362.48** (class sum; +$1,106,337.63 on the total field), structured +$87.13M, alternatives -$86.45M, equity -$10.01M: a
  date nothing else touched still restates through today's reference inputs.
- **Re-derive cost** (current partition, four keys per relationship, process peak includes the static load of about 19 s): N=1 130 s cold / 41 s warm,
  3.30 GB, 3,103 relationships, 12,412 keys, 8.30 GB written; N=3 239 s / 127 s, 3.28 GB, 3,267 relationships, 13,068 keys, 8.78 GB; N=5 291 s / 207 s,
  3.26 GB, 3,267 relationships, 13,068 keys, 8.78 GB. Beside the chain: the 04:00:46Z fire's launch-to-stop is AT LEAST 7,766.7 s (a lower bound: an
  instance-initiated shutdown leaves no stop event); the last C_06 run was 15.5 s, the pre-ship early return, the baseline for the SC-e-91 pass.
- **The mover:** `B_00.canonical_holdings.py` is the only writer of the prefix; its nightly catalog line is `--upload --force-recent-days 14`
  (`gold_dispatch.sh:99`). Each 04:14-04:16Z fire re-puts 11 partitions (the new one plus the 10 inside the window) and changed content on 11 of 15
  days (09-27 to 10-11); the 23:15Z fires re-put identical bytes; off-cycle content changes of 1-2 partitions on 09-30, 10-02, 10-03, 10-07 and 10-09 and an
  11-partition change at 2026-10-12T00:33Z. The oldest content change reaches 20 trading days back (2026-09-11); the current window is 10 trading days.
- **Who holds the unlisted unclassified dollars at 2026-10-09** (rebuilt snapshot): $210,486.42 across 22 positions, ALL blank-ticker structured notes and
  bonds; none of the top 20 has a `NAME::` row (top five: GS FIN CORP 12/20/2030 $56,672.00; CITIGROUP GLOBAL MKTS HLDGS 07/29/2030 $27,972.00;
  INNOVATOR EQUITY DUAL DIRECTIONAL 10 BUFFER ETF - JUNE $21,870.00; BARCLAYS BANK PLC 08/26/2031 $11,630.40; SOCIETY GENERALE 09/19/2031 $11,000.00).

## What it means for the choices (stated, not ruled; the ruling is the CTO's)

- **SC-e-91 (shipped, first fire pending) reaches less than a re-derive:** its range at 2026-10-09 is $0 to $653,857.12 of the Unclassified; a re-derive of
  that date from the current classifier moves it by **$962,915.51** (served $1,846,399.46 to rebuilt $883,483.05), the whole of what the classifier now places.
- **A rebuild of a retained date restates history by classifier and static drift even where no byte moved:** 2026-10-06 would lose $140.16M of Unclassified
  to equity and structured, and the control date moves by $1.1M with its bytes untouched. That is a partner-facing restatement.
- **The cost is not the constraint:** a 5-day window adds 2 to 5 minutes and about 8.8 GB of writes per fire to a chain whose C_06 run was 15.5 s; the
  constraint is what a restated page says.
- **B_00 will keep moving a date for up to 14 days after its first build**, so a date built once on its first night is the least-final version of itself.

## Issuer rulings this round (for the CVO to see)

- **TO-SC-e95 amended** (@560873ea45, on the worker's branch, merged in 1480f5008c). The worker stopped on its own stop rule: the control date rebuilt
  +$1,106,337.63 away from the served snapshot, because a rebuild from the current partition also reads the CURRENT classifier and static tables, so the
  order's "served vs rebuilt" conflated reference drift with byte drift (its row D1-W85-S1, BLOCKING, ARMED, my disarm). Ruled inside my decomposition: the
  read is taken at three snapshots (served, first build, current), and the control is a HARNESS control (one version, byte drift within $1.00, repeatable) whose
  reference drift is a result. The issuer's checker is amended with a positive and three negative controls. The worker's rows S2-S5 accepted, S6 (rounding to
  six places: class dollars and the total field differ by up to $128.58 per snapshot) accepted. Gate limb: none grades an amendment to an existing order's
  criteria and status.
- **D1-S31** recorded D1-W83-S5 BOUNDED (three retained dates, none added, the latest as_of unaffected) at the issuance, per the CTO's instruction.

## Rows at this packet

New from the worker: D1-W85-S1 (BLOCKING ARMED, dispositioned by the amendment), S2-S6 (OBSERVATION, INERT). **D1-W83-S5 stays ARMED:** the read it waited on
has printed; its disarm is the CTO's ruling (correct the retained dates by a rolling re-derive or a one-off rebuild, or accept the drift with these dollars
named); I hold the disarm and record the ruling when it lands. D1-W80-S4 stays INERT; the unlisted holders are named above (blank-ticker structured notes
and bonds with no `NAME::` row, which the SC-e-87 / SC-e-91 classifier cannot place).

## Reads and carries

- **TO-SC-e91b leg G (mine), after the first scheduled BD fire** (23:00Z tonight, Mon-Sat, else 04:00Z): the retained-date range and idempotence, with the
  chain-runtime STOP rule watched from the 23:37Z tick.
- **SC-e-87 leg G on the first NEW as_of** (Tuesday 2026-10-13's fire or later), the figure restated by the CTO.
- Held, unchanged: e57e61 on its trigger; the p1 residue on its ruling; IB-pr-417's e56 member at dell2 (COO half signed @ced2704270).
