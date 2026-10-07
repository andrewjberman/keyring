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

**Grade:** the CTO's round-31 analysis said that E-M3 met makes this project's FWD-5 share REALIZED, and E-M3 is met. The
grade itself is the CTO's, after the CVO's round-32 sweep, and is not yet written. FWD-5 as a whole then waits only on
IRPT_FNTEND's view.

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

1. **Wait for the CTO's answer to round 32.** Then issue its M items in one issuance the same tick, or record FWD-5's
   share REALIZED if it has none.
2. **dell1's release ask for `holdings_snapshot.py` (SC-e-56):** sign or refuse the COO half against its stated blast
   radius (the three firms' Holdings publications, rollback per key).
3. **The unclassified Cottonwood tickers** (BDCASHIN, FCASH, CQP plus 5, from the 10-05 build log). Andrew's word is
   recorded @fa8d7d1cf7: a "Cash" token is the cash class, and the others can be web-searched. The tickers are dell1
   `~M1`'s, relayed through `0.0.0_AB_MSTR~DELL2` (msg 667). This seat does not classify them.

## Dependencies

| Needs | From (owner) | State |
|---|---|---|
| round-32 sweep and slug | `3.0.0_SA_CVO` | packet READ 13:15Z (id 605) |
| FWD-5 share grade, round-33 items | `1.0.0_SA_CTO~DELL2` | after the slug |
| release ask for `holdings_snapshot.py` | dell1 `2.0.0_SA_COO~M1` | not yet sent |
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
