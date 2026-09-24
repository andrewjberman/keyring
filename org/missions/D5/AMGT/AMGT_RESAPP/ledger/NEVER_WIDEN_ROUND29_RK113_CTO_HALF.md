# AMGT_RESAPP round 29 -- never-widen pair, `AMGT-rk-113` (L-ID, the Lenovo identity pull) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`. **Status: SIGNED**, 2026-09-22 ~16:3xZ, against the live reads below.

The COO half is `ledger/NEVER_WIDEN_ROUND29_RK113_COO_HALF.md`, signed at the round-29 issuance @`349a152935`.
The order `task-orders/AMGT_RESAPP.TO-AMGT-rk-113.lenovo-identity-pull.md` acts on neither half alone. It spawns only
when `AMGT-rk-114` (the ENRICH precursor) has drained AND both halves are on file.

**Authority:**
- Andrew's Lenovo trial word, @`cd0cca7f46` (1 security, one pass per channel).
- PRD v0.23 section 12, stage 1 ("identity first").
- This seat's rulings: msg 24261 Q5 (pair; Lenovo's record only; the other records byte-equal) and msg 24310 (ENRICH
  first; the rollback without a delete, with the byte-equal criterion on the rollback too; the vintage stamp in this
  half).

## LIVE PRE-ACT READS (this seat's own instrument, ~16:3xZ, read-only)

| read | value |
|---|---|
| `s3://opal-data-harvest/crosswalk/v1/` keys | 2: `2026-09-15.json` and `2026-09-19.json`. **The served latest is `2026-09-19.json`, and there is no key for today.** |
| bucket versioning | `Enabled` |
| `2026-09-19.json` versions | **7** versions, 0 delete markers; latest `pwgdKMxY3pN3...`, 202,505 bytes, 2026-09-19T01:23:43Z. (The COO half says 8; my full listing reads 7. It is immaterial, because this act never writes that key.) |
| `2026-09-19.json` content | sha256 prefix `6668326f3d1b4d09`; `as_of` 2026-09-19; **96 records** (MEASURED 36, UNRESOLVED 60, registered 7) |
| the `992_HK_Equity` record | present, exactly 1; **no `identity` object**; 11 keys (`association_keys`, `bloomberg`, `display_ticker`, `exchange`, `model_key`, `provenance`, `raw_identifier`, `resolution`, `security_key`, `share_class`, `source_row`) |
| the served stamp | `lib/research/api/scoped_amgt.py:1725-1732` puts `crosswalk_vintage` and `crosswalk_source` on every served identity block |

## BLAST RADIUS -- what the act MAY move

1. **Lenovo's record gains its `identity` object** and one `provenance.identity` line. Its other 11 keys are unchanged.
2. **A new served-latest key `crosswalk/v1/<today>.json`** holds the same 96 records, with only (1) differing.
3. **THE SERVED-WIDE STAMP (named here per this seat's ruling).**
   - Every page's served identity block, FOR ALL 96 NAMES, moves its `crosswalk_vintage` from `2026-09-19` to today, and
     its `crosswalk_source` from `.../2026-09-19.json` to today's key.
   - No record content changes for the other 95.
   - A warm Lambda container serves the 09-19 stamp until it recycles, so for a short window two stamps are served.
     That is disclosed, not a defect.
4. One immutable identity bronze object for 992, with 0 production readers.
5. `registrations.json` gains +1 row, `mode: ENRICH`, committed.
6. Bloomberg quota: 2 requests (the sign-in probe, and 992 x 9 fields), 10 security-field points.

**Nothing else.** The COO half's NOT-MOVED list binds as written.

## ROLLBACK, per key -- no delete in any branch

- **The crosswalk.**
  1. A new commit removes the ENRICH row.
  2. `crosswalk --as-of <rollback UTC day> --write-pool` republishes the records of AC1's snapshot.
     - On the same day, that makes a newer version of today's key.
     - On a later day, it writes that day's key.
  3. **The rollback run passes the SAME criterion as the forward run:** 95 of 95 other records byte-equal to the 09-19
     document, and the count stays 96.
  4. **The stamp moves AGAIN**, to the rollback's date, on every name. That is the rollback's own served-wide effect,
     and it is disclosed here.
- **The 09-19 key is never written**, so it remains the byte-exact fallback read above (sha256 `6668326f3d1b4d09`).
- **Identity bronze** is left in place, immutable and unread. Removing it would be an S3 delete, which needs a human word
  and is not covered.
- **Trigger:** any other record changed, the count moved, or Lenovo's non-identity fields changed (the COO half's
  ROLLBACK branch). On an UNRESOLVED pull that appends a record, the count becomes 97, which is a trigger.

## SIGNATURE

The blast radius above is complete for the act as written: one command, after rk-114 drains. Its only served-wide
effect is the stamp move, which is stated. The rollback deletes nothing, and is graded by the same criterion as the
forward run.

**SIGNED -- `1.0.0_SA_CTO~Z`.**
