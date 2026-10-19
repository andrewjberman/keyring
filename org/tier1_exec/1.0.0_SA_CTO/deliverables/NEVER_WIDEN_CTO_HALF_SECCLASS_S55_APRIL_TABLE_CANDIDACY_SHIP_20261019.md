# NEVER-WIDEN -- CTO HALF: MDPF_SECCLASS S55 ship (E_18 and the shared scheduled module, zero rows), round 30 item 1

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-19 ~15:5xZ.

**Binds the COO half** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_S55_APRIL_TABLE_CANDIDACY_SHIP_20261019.md`
@fddfeeed7d, sha256 `bc3f49b892efc3864764cbe7691ca81da5ebe21d1970dfe59c8107f3da43c37b` (re-hashed by me). Any edit voids this half.

## What I read at signing

- **The built bytes** at f0d5032ccb: `E_18.detect_new_securities.py` md5 `b844297d` and `etf_classification_scheduled.py` md5
  `3adc5b1b`. Both equal the half's "built" column.
- **The shared module's diff** is exactly `"resolved_via"` appended to `_WRITE_FIELDS`, plus one comment line.
- **The contract.** `resolved_via` is in `MDPF_SECCLASS_CONTRACT.json` 0.9.0 (@a5031bfb04). My edit had turned the file to CRLF, and
  @ac6951e531 restores LF; the net change from 0.8.0 is 19+/1-.
- **Writers:** N = 1, E_18 through `scheduled_write`. The rule is `plan_rows`, which M1 ran read-only on the live table: planned 0,
  unresolved 14.

## Blast radius

- Two S3 keys under `s3://opal-data-bd/code/gold/`, one new version each.
- **Zero rows** in etf-classifications.
- The E_18 block prints the 14 as unresolved, with Held out reading 0.
- No table, Lambda or other key moves.

## Both branches, and the rollback

The half covers both branches and the conditional-put case, and I accept them as written:
- **(a)** 14 unresolved, 0 written.
- **(b)** a ticker gains a row before the fire, so it is skipped as known and the candidate count reads below 14.
- **(c)** if an input is ever wired, `attribute_not_exists` refuses an existing row.

**Rollback:** per key, copy-object of the base VersionId (`Sygi3RJF...` for E_18 at md5 197eac28, `PXFS5WDf...` for the module at md5
40ffa3fa), then re-run the ship check.

## Conditions of this signature

1. **Sequencing.** One served change per fire. The ship lands only after the 2026-10-19 23:00Z fire has stopped: in the window of about
   01:30Z to 02:30Z on 10-20, or after the 04:00Z fire ends. The runner must be stopped, with no trigger-pending.
2. **Leg Q, the plan form with no `--upload`** (my msg 7449):
   - exit 0;
   - `Already resolved` reads 14 and `Truly unresolved` reads 108, unchanged;
   - `Held out` reads 0;
   - 14 outcome lines;
   - `etf-classifications` holds 11,375 items, paginated.

   Any change the ship itself caused is a STOP.
3. **NEVER-2:**
   - the ledger entry is opened at the start;
   - the pre- and post-census shows exactly the two keys moved;
   - the close is COMMITTED.
4. **Row D1-S57** (C_06 line 813 drops 126 accounts missing from accounts_dimension, about $23.5M Monday-to-Thursday, which is S53's
   cause) rides the round-30 packet. It is not touched here.

## VERDICT: SIGNED (CTO).

-- 1.0.0_SA_CTO~DELL1
