# CTO never-widen half -- MDPF_SECCLASS SC-e-32/e50, old-list reclassify V3: 5,182 DIRECT puts + the AI classifier over 2,291 old-list keys

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~19:1xZ, release mode request 9 (msg 565). **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_OLD_LIST_RECLASSIFY_20261007.md` @44c0350292,
section "ADDENDUM V3 + COO half" (COO half SIGNED WITH CONDITIONS 1-3). Set `OLD_LIST_RECLASSIFY_SET_V3_20261007.tsv` @15f9c9a411.

## VERDICT: SIGNED -- the snapshot, the DIRECT leg, the AI leg over the 2,291 old-list keys, and the per-key rollback, under the COO's conditions 1-3 plus the two below.

## Read by this seat

- **Vendor word: inside it, squarely.** These keys ARE the old table: the set is the `bd-securities` scan, 10,965 rows, live 10,965.
  - Andrew-direct 2026-10-06 00:03Z, "RUn on the full old table", covers up to 8,495 old-table rows.
  - The model is the existing writer's (kimi-k3), the payload is name and key only, and the direct match runs first.
  - 2,291 keys, at most 4,582 calls. The writer refuses an AI key set above 8,495.
- **Names:** my census of the V3 `clean_name` column (10,965 rows, case-sensitive, word-boundary) reads 0 for every form refused on
  SC-e-48 (`Adr`/`Ads`/`Etf`/`Ltd`/`Plc`/`Abb`, all-caps `INC`/`CORP`, `X&y`), and 0 non-ASCII. One residual is accepted, not
  blocking: `Sumitomo Ele-Adr`, where the source joins the form to a word with a hyphen.
- **Cash:** 316 DIRECT rows re-plan from `fixed_income/Cash` to `cash/Cash` under PRD v0.14 ruling 2.4. Both the DIRECT and AI bounds
  are the contract 0.8.0 closed list, not the live vocabulary.
- **The dry-run mismatch is real and correctly gated.** `to_model=2290 != ai_keys=2291` is row S63: a `NAME::` key that the cash-token
  ticker leg places but the write path never puts. The COO's condition 1 makes TO-SC-e65 amendment 3 a precondition.

## Conditions (in addition to the COO's 1-3)

1. **TO-SC-e65 amendment 3 has two faces, and only one is covered here.** This half covers the act's runner reading the amended
   module from the release head. The amended `etf_classification_scheduled.py` reaching `opal-data-bd`/`opal-data-cot`
   `code/gold/lib/_shared/` is a NEW deploy of a live module (e65 is at ETag 3f1e6be8). That deploy needs its own pair, and it does
   not run until the e65 ledger closes after the 23:00Z read.
2. **Sequencing with SC-e-49:** this act runs first. Its 157 keys shared with e49 land here, and e49's planner reads them PRESENT.
   The vendor-word question on e49's other keys is not ruled here (see this seat's correction, VERDICTS 2026-10-07T19:1xZ).
