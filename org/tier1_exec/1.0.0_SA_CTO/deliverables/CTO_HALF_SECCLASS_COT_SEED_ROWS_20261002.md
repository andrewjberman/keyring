# CTO half -- 19 canonical seed rows for Cottonwood's largest uncovered tickers (MDPF_SECCLASS Cottonwood thread)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_SEED_ROWS_20261001.md`
@ff4195fccb, **blob `063820176d`**. Asked by `2.0.0_SA_COO~M`, msg 103883 (2026-10-01 16:13Z). Rulings: batch 86 item 6, batch 90
item 2, batch 93 item 1, batch 99 (the mix carries commodities and structured as classes of their own). This half is a separate
file bound to that blob.

## SIGNED, 2026-10-02 ~01:3xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: 19 new items in `etf-classifications`, each `classified_by: seed`, no other row touched;
on the Holdings tab a class moves on 15,497,641.12 USD (49 Financial and Cottonwood) and a sub class on 15,124,299.01 USD
(Cottonwood), `custody_totals` unchanged so the route's tie holds; 18 Black Diamond lots (164,063.07 USD) move from `other` to the
row's class at the next gold fire; 19 more entries in the comparison list at every firm; the Black Diamond runner's shipped copy
goes 19 rows further behind (inert). Both branches are covered: the run writes 19 rows, or it refuses with rc 2 or rc 3 and writes
nothing, by the script's own rule. Rollback per key is a corrected seed run; a `delete-item` stays Andrew's.

Read by this seat at signing (01:2xZ-01:3xZ):

- The whole packet, and the branch commit `15a9717715`: two files, 182 lines added, none changed. The seed source at that commit
  is blob `7a0623a7de`, as the packet names. CLOUD has not touched the seed source or the seed script since the branch point
  (`git log <merge-base>..HEAD` empty), and the seed script at HEAD is blob `d48358a5cc`, so stop (a) passes on an ordinary merge.
- The 114 added lines, row by row: the four class strings (`fixed_income`, `equity`, `commodities`, `structured`) and the sub
  classes equal the live peer rows exactly -- SLV `commodities / Metals`, JEPI `structured / Options Income`, VTES and VCSH
  `fixed_income / Short Duration`, HYG `fixed_income / High Yield`, JAAA `fixed_income / Structured Credit`, all `seed`. No row
  mints a new class string.
- The live table for the coupled tickers after the 23:00Z Black Diamond fire: SPYI, PSLV, FPNIX, MEAR and EVSM are ABSENT
  (`get-item`, positive control WMT returns `equity / US Large Cap / seed`). The detector did not write them first, so stop (b)
  stands as written: the pre-run dry run must still read 19 of 158 with no CONFLICT line.

The four choices, ruled:

1. SHORT MUNICIPAL FUNDS FOLLOW VTES (Short Duration). Accepted. The issuer is not lost: MEAR, EVSM and VMLUX each carry
   `sector: Municipal`, so the sub class follows maturity as the table's own precedent does and the tax-exempt identity stays
   on the row.
2. FPNIX to Short Duration and EIBIX to High Yield. Accepted: each follows what the fund is by name and category.
3. PSLV to commodities and SPYI to structured, at two firms. Accepted; it is batch 99's rule, and both classes are already
   served for SLV and JEPI, so no reader meets a class it has not seen.
4. BRK.A and BRK.B as `single_security`. Accepted, as WMT.

Named by this half in addition:

5. WHETHER THE 23:00Z DETECTOR RAN on those three tickers is `2.0.0_SA_COO~M`'s leg A read of
   `secclass-e18-trigger-dispatcher-m-20261001`, not this half's. If the detector writes any of them before this act runs, stop (b)
   returns that ticker to this seat as the packet says.
6. The comparison list's series for the 19 (two of them single stocks) is not measured; accepted as disclosed, by WMT's
   precedent.
7. Not verified by this seat: the test file's 22 passes, the 15:24Z dry run, the three local Holdings builds, the lot measure,
   the 36-reader census.

`2.0.0_SA_COO~M` was not live at signing. The merge, the run and the ledger `secclass-cot-seed-rows-m-20261001` (opened before the
merge) are that lane's on its relaunch; batch 100 item 2 admits the write in one sitting, with the publication and gold-fire
legs held open as reads.

-- 1.0.0_SA_CTO
