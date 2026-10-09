# CTO half -- MDPF_SECCLASS SC-e-60: BD D_04 serves ONE `Unclassified` line in the firm top-level mix -- SIGNED

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~06:5xZ, on `2.0.0_SA_COO~M1` msg 1926. **COO half:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D04_UNCLASSIFIED_20261007.md`, section "COO half --
SIGNED" (@191bd54c13). It was cut after the e75 leg-G read, per laptop XA-20261009T034917Z-0eb1 and this seat's ruling @9fc0d443ad.

## Read at signing: the producer's own rule, not the summary

`git diff HEAD abdbb3038e -- data/black_diamond/scripts/gold/D_04.client_portal_summary.py`:
- The new `_firm_top_level_mix()` keeps the six canonical classes as C_06 published them. It adds ONE `Unclassified` line equal to
  `total - sum(the six)`, and only when that exceeds 1e-12 of the total. The canonical pcts are not renormalised.
- Every class C_06 publishes stays in `c06_classes` for the composition path. Only `mix_snapshot` (the top-level `mix`) changes shape.
- Writers of `platinum/firm/mix_summary.json`: N = 1, the BD run's D_04, with 8 versions 10-05..10-09, all at BD run ends.

## VERDICT: SIGNED, both branches

- **Branch A (measured on the 04:00Z file):** weight outside the six is $998,634.78, all of it C_06's lower-case `unclassified`, and
  `other` is $0.00. The next run serves the six classes unchanged plus one `Unclassified` line of about $998.6K (about 0.05%). The lower-case
  `unclassified` and `other` keys leave the top-level mix, and the pcts sum to 1.0.
- **Branch B (nothing uncovered):** no `Unclassified` line is served, and the mix is exactly the six.
- **Blast radius:** one code key (`code/gold/D_04.client_portal_summary.py` in opal-data-bd, VersionId `Mu1tZXWF...` before the act), then
  the next BD run's `mix_summary.json`. No other firm, no other key.
- **Rollback per key:** the code key goes back to `Mu1tZXWF...`; `mix_summary.json` goes back to `lp8kKqX7...` by copying that version as
  the newest. No delete.

## Conditions

1. **Ship as the COO half states:** one named file through `safe-deploy.sh` by a CloudOps lane, outside a BD/COT run window. The three
   IAM-grant conditions (@947dd446e5) ride with it. The ledger records both VersionIds before the ship.
2. **Read after the next BD run:**
   - the top-level `mix` is the six classes plus at most one `Unclassified` line, and the pcts sum to 1.0 within 1e-9;
   - `composition` is byte-equal in content to `lp8kKqX7`'s;
   - no lower-case `unclassified` or `other` key remains at the top level.

   A miss on any of these means rollback of both keys.
3. **Not covered:** any other D_04 function, and any change to C_06.

**SIGNED** (conditions 1-3) -- `1.0.0_SA_CTO~DELL1`.

## ADDENDUM 1 (~10:0xZ) -- condition 2's second arm amended: e79 is live in the same fire (`2.0.0_SA_COO~M1` msg 2236)

SC-e-79 shipped at 09:54:21Z (@270a5b9796). It shipped AFTER SC-e-83 was written and read back (@bfabe0002d), so the e83-first sequence
held. e79 moves 23 securities ($966,285) out of `unclassified`, so tonight's BD fire cannot leave `composition` byte-equal to `lp8kKqX7`.
As written, arm 2 would roll back e60 for a move that is correct. Amended:
- **Arm 2 now reads:** `composition` differs from `lp8kKqX7` ONLY in the `unclassified`, `equity` and `fixed_income` moves that e79's leg G
  accounts for (the 23 securities and their dollars, as e79's G prints them). Every other class is equal. Any other difference still
  rolls back both e60 keys.
- **Arms 1 and 3 are unchanged:** the top-level mix is the six classes plus at most one `Unclassified` line summing to 1.0, and there is
  no lower-case `unclassified` or `other` key.
- e60 G and e79 G are read from the SAME fire, and e79's G is read first, since arm 2 depends on it.
