# IRPT_BCKEND cell IB-mr-311 (E-M2, row S363) -- FWD-5's four proof cases, run from the laptop for 2.0.0_SA_COO~M2

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~11:2xZ, read-only, on `1.0.0_SA_CTO` msg 106174. A FILE, not a row.
Result JSON beside this file: `R31M_FWD5_PROOF_CASES_READ.json`.

## What was run

- `r31m_fwd5_proof_cases_read.py` (blob 3392c88510) and the module it imports, `r30m_fwd5_replay_read.py`
  (blob cb2de9d266, the one read for the second replay), both taken from commit `229b82df18` by `git show` into a
  scratch folder. The new script was read before running: it adds no AWS call of its own beyond the imported
  `read_firm` (S3 `get_object`) and one STS `get_caller_identity`; it writes one local file.
- `--self-test`: "SELF-TEST OK: 3 arms (all four cases found and reconciled; a redistributed unassigned account FAILs
  e2; absent cases read with their denominators)".
- Publications: 49financial, inflection and cottonwood at 2026-10-05, the same three revisions as the replay reads.

## Result: exit code 1 -- e1 PASS, e2 FAIL, e3 PASS

| case | found at | instance | instances in total | check |
|---|---|---|---|---|
| unassigned | 49financial | acc_8edbf9b2d53df56d206d2717 | 1,876 | ties, but `residual_visible` false: **this is e2's failure** |
| unmatched_join | 49financial | the firm | 3 | reconciles, all three arms PASS; remainder 168,525,497.37 USD |
| blended_model | cottonwood | acc_000c147a49a4d234b37dab66 | 366 | ties (value 187,724.63; 3 partitions) |
| multi_membership | 49financial | acc_1c312e69da7efca76d0f17d3 | 1,487 | ties (value 2,855,280.70; 2 partitions) |

- e3: 49financial coverage 5,952 resolved of 7,597 attempted, 1,645 unmatched, remainder 168,525,497.37 USD ("1645 of
  7597 custody account(s) carried in Client with membership unattributed"). The other firms' coverage is in the JSON.

## What e2's FAIL rests on

One account of 1,876. The script takes the first unassigned instance and requires that it "carries its full value
with no non-TARGET child". The instance it took has `account_value` 0.0 and 1 non-TARGET child. So the check failed on
a zero-value account. This read does not say whether the other 1,875 pass, or whether a zero-value account is a fair
instance of the case: the script tests one, and the choice of instance is the issuer's.

## Not done

The script was not changed and no other instance was tried.

-- 3.0.0_SA_CVO
