# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M2` (CLAUDE, dell2), successor of laptop `2.0.0_SA_COO~M`, which is FINAL on this project (handoff
@1640a0e86e; laptop `1.0.0_SA_CTO` msg 106037). One issuer for M: `~M2` (`1.0.0_SA_CTO~DELL2` msg 160).
- CTO: `1.0.0_SA_CTO~DELL2` writes the M round analyses.
- Reviewer: `3.0.0_SA_CVO` (dell2).
- As of 2026-10-07 ~14:2xZ. This replaces the 10-02 file of the laptop ~M.

Mode: FULL (`.tools/drive-mode.py read IRPT_BCKEND`). Loop: `/canonical-drive` 30m. Authority: the `org/ref/LIVE_ARMS.md`
DELL2 block, class CHOSEN, @3e5ce43ebb.

Claim words: `measured` = read this session on dell2; `held` = cited from a record and not re-read.

## FWD-5 -- this project's share (join correctness, the reconcile control, the denominators)

All cases below were read on the served 2026-10-05 publication.

| PROOF item | round | result | claim |
|---|---|---|---|
| before/after reconcile at 3 of 3 firms, every arm | 30 (E-M1) | account sum = served custody total to the cent (49F 1,825,384,091.11; INF 208,044,040.13; COT 545,819,721.23); served reconcile blocks read reconciled | measured (`R30_CHECKS`, compile @471e285eb1) |
| unassigned account | 31 (E-M2) | 1,876 of 1,876 pass: served as an ACCOUNT, the subtree ties, no model node beneath (49F 1,645, INF 231; COT lists 0) | measured (dell2 re-check @6458a5a9d3) |
| unmatched join | 31 | reconciles, with the residual visible: 49F 168,525,497.37 USD across 1,645 of 7,597 accounts | measured (compile @1ec3aa4eef) |
| blended model | 31 | COT, 366 instances; the named one ties | measured |
| multi-relationship membership | 32 (E-M3) | COT acc_0f1e215e521798954f80f291 is in 2 relationships (3 of 860 accounts); 58 rows collapse to 29 unique; rebuilt = served 462,857.7422 | measured (compile @d1abea06f8) |
| coverage denominated | 31 | 49F 5,952 of 7,597; INF 627 of 858; COT 475 of 860 | measured |

**Grade: REALIZED** for this project's share, by `1.0.0_SA_CTO~DELL2` in the sweep-15 part-1 analysis
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_SWEEP_15_PART_1_20261007.md` @db1e82ce18, msg 890), on the
CVO's E-M3 grade C-S300. FWD-5 as a whole waits only on IRPT_FNTEND's view. The 22% unattributed-membership residual is a coverage
question for that view and the overlay sources.

## Live thread

The Holdings tab is LIVE END TO END at three firms. This is held from the 09-27 walks and was not walked this session.
Rounds 30-32 read the served publications and walked no page.

## Rounds this seat issued

| round | cell | order | slot | drain | rows |
|---|---|---|---|---|---|
| 30 | IB-mr-301 (E-M1) | TO-IB-m30-301 | ~152 | @1758606f46 | S352 (disarmed by S362), S356 |
| 31 | IB-mr-311 (E-M2) | TO-IB-m31-311 | ~153 | @5eea584574 | S363 (disarmed by S367), S366 |
| 32 | IB-mr-321 (E-M3) | TO-IB-m32-321 | ~154 | @3daee801f3 | S368 (disarmed by S370) |

Each order was cut on a delivered FILE, pinned by commit and sha256, because dell2 could not make the read itself.

## Constraints this lane works under

- **Firm buckets from dell2:** all three READ. 49financial and inflection read since the fence join (~10:44Z); cottonwood
  reads from 15:02Z (head-object answered, manifest LastModified 2026-10-07T14:18:11Z). M reads now run on dell2 with no
  laptop relay. Measured.
- **`holdings_snapshot.py`** has one writer: dell1's SC-e-56 (`2.0.0_SA_COO~M1`), decision 106191. No dell2 seat edits it.
  Its RELEASE runs through IRPT_BCKEND: `~M2` gives the COO never-widen half and `1.0.0_SA_CTO~DELL2` the CTO half.
- **Row ids:** only dell2 mints IRPT_BCKEND ids (08:5xZ ruling). S370 exists twice, here and on origin (laptop ~C's).
  `~M2` keeps S370, and the laptop row comes back as a FILE (`0.0.0_AB_MSTR~DELL2` msg 614).
- **No bun install, no downloads.** Research browsing is allowed only when necessary (Andrew-direct ~14:0xZ; rules
  106215 and 106221). No `~M2` order runs bun or reaches the internet.

## Next-list, in order

1. **The SC-e-62/56 release** (dell1 r3 @a87e215afc). The IRPT_BCKEND COO half is
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_IRPT_BCKEND_COO_HALF_SECCLASS_E62_E56_RELEASE_20261007.md`,
   signed @a8276122e5 and re-pointed to r3 @ef800c1bd0; the CTO half is @f67ab9002b with AMENDMENT 1 @6c57a70f2f. This seat owes:
   - after `0.0.0_AB_MSTR` merges r3, the `tar -tzf` read-back of the bundle: 12 members, exactly 2 changed;
   - after the first weekday `irpt-holdings-snapshot` fire (10:15 ET), the per-firm read: new revision, reconcile, class moves
     against expected, 0 `multi_asset`; or Branch B's rollback to the recorded pins before the next fire.
   The 238 pre-check passed on r2 (producer bytes equal at r3). No manual Holdings run is covered.
2. **No new M item** this sweep (CTO msg 890). The next M round comes from the CTO's next analysis.
3. **The unclassified Cottonwood tickers** belong to dell1 `~M1` under Andrew's word @fa8d7d1cf7 (relayed, msg 667).

## Dependencies

| Needs | From (owner) | State |
|---|---|---|
| round-32 sweep and slug | `3.0.0_SA_CVO` | packet READ 13:15Z (id 605) |
| FWD-5 share grade | `1.0.0_SA_CTO~DELL2` | REALIZED (msg 890) |
| r3 merge into CLOUD | `0.0.0_AB_MSTR~DELL2` | both halves on r3; not merged at 17:02Z |
| Cottonwood read access for dell2 | NFRA_CTLPLN fence apply (TO-APPLY-4) | MET: reads at 15:02Z |

## Retired from the 10-02 list

| item | why it is retired |
|---|---|
| BD r3 re-land | MDPF_SECCLASS, now on dell1 |
| `multi_asset` readers packet | retired by Andrew's six-class word |
| the two walks | the INF split-account ledger closed 10-02; the COT seed-rows ledger closed 10-02 |

The `secclass-*`, `bd-securities-cot-new-p1-m-*` and `cot-cash-admission-m-*` ledgers in `.open_deploys/` are
MDPF_SECCLASS's and went to `~M1` with the laptop ~M's final handoff.

## Limits

- No page was walked this session.
- Every read was of the 2026-10-05 publication.
- The multi-relationship case rests on one of the three accounts; the criterion asks for one.
