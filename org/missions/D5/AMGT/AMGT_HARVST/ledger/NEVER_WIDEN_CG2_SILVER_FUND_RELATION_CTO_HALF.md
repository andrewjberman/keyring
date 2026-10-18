# NEVER-WIDEN -- CTO HALF: `HVST-cg-2`, the silver `research-report` rewrite that adds `fund_relation` (round 92)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~00:0xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round92/NEVER_WIDEN_HALF_COO_CG2_SILVER_FUND_RELATION.md` as committed at
8fd59f9bff, sha256 `11cf6bd0e637fd440b89881ecd9357c0a10d9c942644f57a3193a7fd287b9158`. Any edit to that file voids this half.

## Basis

- **The census at cg-5 @a9aecdd593,** re-run by W1:
  - holding 121, candidate 14, initiate 2, interest 2, template 1, unclassified 0, none 213; 353 rows; MOVED_ROWS = 4.
  - These are the counts I said to expect after my rulings: "size reduction in" is a holding, RECOMMEDATION is an exact alias, and
    "adding" is guarded, matching 2 rows, both CPA, both held.
  - The six-name proof line holds.
- **N = 2 writers** of the moved column: `typed.py::main` (`store.silver_append`), and this rewrite.

## Blast radius

- **Writes:** three NEW parquet parts in `opal-data-harvest` under `amgt/harvest/silver/research-report/`, dated 2026-09-23, 09-24 and 09-25,
  with 84, 121 and 148 rows: 353 in all. Nothing is overwritten or deleted.
- **Served move: NONE until cg-3.** REPORT_FIELDS does not yet carry `fund_relation`, and `fund_form.gather_items` still reads `fund`. The
  new parts win `silver_latest` per key, so every record_hash changes, and every value other than `fund_relation` is equal.
- **Untouched:** gold, the gateway code, fund_form, other tables, IAM and Terraform.

## Both branches

As the COO half states them:
- Branch A: each part read back equals its plan, in count, column and key set, with all other columns equal.
- Branch B: any difference is a STOP. A repair is a still newer part, never an overwrite.

## Rollback

The act is ADD-ONLY. Removing the three new keys restores the prior state exactly; that is an S3 delete, Andrew's act, and not pre-approved
here. `cg2_written.out` is the key list.

## Conditions of this signature

1. **C-1 to C-9 of the COO half bind as written,** including:
   - C-6: after the last write, all 353 reports resolve to the new parts and the counts equal the census;
   - C-7: UNH and CPA read unchanged through the gateway;
   - C-9: site Z is told first, and a site Z write to the table in flight is a STOP.
2. **The S44 rule:** each part is written foreground, with the manifest checked after each write.
3. **cg-3 (the gateway release) waits for this act's ledger close.** That way the gateway never serves `fund_relation` empty.

## VERDICT: SIGNED (CTO).
