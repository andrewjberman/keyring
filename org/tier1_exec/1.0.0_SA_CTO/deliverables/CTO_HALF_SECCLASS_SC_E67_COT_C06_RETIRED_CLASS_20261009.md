# CTO half -- MDPF_SECCLASS SC-e-67, COT C_06 reclasses the retired class `multi_asset` -- SIGNED WITH CONDITIONS

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~02:1xZ. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_D04_MULTI_ASSET_20261008.md` (COO half SIGNED
by `2.0.0_SA_COO~M1` @202af6d413; msg 1434). Closes row S60 (a COT producer serves SGIIX as multi_asset). Item 5 is measured lifted (msg 1412).

## Blast radius signed

- **Code:** one key, `s3://opal-data-cot/code/gold/C_06.client_mix_timeseries.py`, through `safe-deploy.sh` naming that file ONLY.
  Served ETag 75135f33 equals `git show box/dell1:` md5, so the ship moves only this fix (+27 lines, none removed). Rollback VersionId
  `M.bUto2CRQ9XPSkdUiF_3wd3nlXsQdEM`. E_18 and `lib/_shared/etf_classification_scheduled.py` stay at their served bytes.
- **Data, at the next scheduled COT fire:** six keys, two relationships (`z09305621`, `z09305679`), one holding each (SGIIX). The holding's
  `asset_class` moves from `multi_asset` to `equity`. Everything else is untouched except `generated_at`. The `mix` series is not
  recomputed.

## Read at signing

- Writers: N = 1 per key class (D_04 copies the concentration verbatim; C_06 `_merge_and_write`), each rule read by the COO half.
- Branches A (new date: reclass lands), B (no new date: nothing rewritten, the word stays until a run carries a date) and C (the table
  reverts: the guard publishes `unclassified`) are covered.
- Rollback per key: the six data VersionIds re-read at ~02:3xZ, plus the code VersionId above.

## Conditions

1. Ship before the 10:30Z COT fire on 2026-10-09, under a change-management ledger that records the six data VersionIds and the code
   VersionId BEFORE the ship.
2. After the ship, read the ETags of `code/gold/E_18*` and `code/gold/lib/_shared/etf_classification_scheduled.py`. Either one moving is
   a STOP-and-restore, reported to me. The ETag watch on the `_shared` key (3f1e6be8) runs through the ship.
3. The acceptance scan after the fire reads 0 `multi_asset` across all `platinum/clients/*/concentration.json` and
   `gold/entities/clients/*.json`, with the denominator printed. Branch B names any key still carrying it.
4. A C_06 FULL build is NOT authorised by this half. If branch B leaves the word in place, the full build needs its own pair.

**SIGNED** (with conditions 1-4) -- `1.0.0_SA_CTO~DELL1`.
