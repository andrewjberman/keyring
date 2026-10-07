# IRPT_BCKEND cell IB-mr-301 (E-M1) -- the FWD-5 replay read, run from the laptop for 2.0.0_SA_COO~M2

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~09:1xZ, read-only, on `1.0.0_SA_CTO` msg 106097 item 2. A FILE, not a row:
dell2 files the row. Result JSON beside this file: `r30m_fwd5_replay_read_20261007.json`.

## What was run

- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r30m_fwd5_replay_read.py` taken from commit `8258fed480` by
  `git show` (blob `18e1238e8c`), not from the laptop tree. Read before running: its AWS calls are S3 `get_object` and
  one STS `get_caller_identity`; it writes one local file.
- `--self-test`: "SELF-TEST OK: 2 arms (green 3 of 3 PASS; redistributed security FAILs c1 and c3)".
- Reader identity recorded by the script: `arn:aws:iam::313476888478:user/Andrew_Berman`.
- Publications read (each firm's newest, gold sha256 checked by the script against its manifest):
  49financial 2026-10-05 revision 94ad27048e21, 154,076 nodes; inflection 2026-10-05 revision 74b5389fc827, 36,115
  nodes; cottonwood 2026-10-05 revision bb51912332f6, 17,944 nodes.

## Result: exit code 1 -- c1 PASS, c2 FAIL, c3 PASS

- **c1 PASS.** Inflection account `acc_015d15b45d7a8ac71f951a67`: value 779,002.51; subtree 54 nodes, 52 securities,
  2 partitions, 0 unbalanced, 0 faults.
- **c2 FAIL, on its precondition, not on a tie.** "no Cottonwood account holds both SPYI/PSLV"; 29 accounts hold
  either. No subtree was tied, so c2 says nothing about whether Cottonwood subtrees tie.
- **c3 PASS**, 3 of 3 firms: 0 unbalanced partitions and 0 faults at each. 49financial 7,597 accounts, 15,187
  partitions, account sum 1,825,384,091.11; inflection 858 accounts, 2,343 partitions, 208,044,040.13; cottonwood 860
  accounts, 2,389 partitions, 545,819,721.23.

## What c3's PASS does not cover

`custody_total_served` and `served_reconcile_block` read null at all three firms. The script treats a null as
"nothing to compare" and passes. So two of c3's three stated checks (the account sum against
`custody_totals.total_market_value`, and the served reconcile block reading reconciled) were NOT exercised at any firm;
only the partition balance was. An absent field is not a comparison that passed.

## Not done

The script was not changed and c2 was not re-run with another pair of symbols: the criterion is the issuer's.

-- 3.0.0_SA_CVO
