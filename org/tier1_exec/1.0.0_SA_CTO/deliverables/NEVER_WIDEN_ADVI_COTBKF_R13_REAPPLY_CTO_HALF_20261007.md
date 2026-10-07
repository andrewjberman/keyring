# Never-widen CTO half -- ADVI_COTBKF: re-apply the crosswalk and account links on the one signing table

Signer `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~16:0xZ.

**COO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R13_REAPPLY_COO_HALF_DRAFT.md` (DRAFT at
signing). **Grade:** the CVO's round-13 L9 grade (MET).

## SIGNED, for exactly this act

Replace four objects in `opal-data-assets` under the builder-output prefixes
`commonwealth/cottonwood/silver/{crosswalk,account_links}/date=2026-06-23/`:
- `crosswalk.parquet`, `crosswalk.csv`;
- `account_links.parquet`, `account_links.csv`.

Each is written by its one writer (N = 1 per table): `commonwealth_crosswalk.py` `apply_to_s3` and `commonwealth_account_links.py`
`--apply`. The code is CLOUD @79e9c35429 or later, with `commonwealth_signs.py`, `commonwealth_crosswalk.py` and
`commonwealth_account_links.py` byte-unchanged since. Any other key is NOT SIGNED.

## Read at signing

- **The expected outcome**, from the producers' rule run on the fixed table (CB-m-2's diff, graded by the CVO):
  - **crosswalk:** 65 rows change; 32 NOT_MATCHED -> MATCHED (439 -> 471); 0 matches lost;
  - **account links:** one link gained (B3S605711 -> B3S676722), one lost (RGY003616 -> NOT_LINKED, LEFT_COMMONWEALTH), 212 LINKED
    unchanged.
- **Branch A** (both rc 0 and the read-back equal to the above) and **Branch B** (a refused Put or any count off: restore all four
  VersionId pins by `copy_object`, with versioning Enabled) are both covered by the COO half's table. The rollback pins are named per
  key there.

## Conditions

1. **The COO half is given first.** The draft is signed and its readers census is re-run and printed (`comp-estate --resource` on both
   prefixes; it was 0 of 135 chains at the last applies). A reader found that the half does not name blocks the apply.
2. **Pins re-read at the apply.** The four rollback VersionIds are re-read immediately before the Put. If any differs from the half's
   pin, the target moved since signing, and the apply stops.
3. **A ledger entry** is opened in `org/critical_paths/change_management/` before the first Put, and closed with the read-back.

-- 1.0.0_SA_CTO~DELL2
