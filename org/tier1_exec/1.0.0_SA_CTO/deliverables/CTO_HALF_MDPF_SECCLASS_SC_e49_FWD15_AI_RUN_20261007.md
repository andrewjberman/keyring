# CTO never-widen half -- MDPF_SECCLASS SC-e-49, FWD-15's missing lists: 301 DIRECT puts + the AI classifier over 1,165 keys

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~18:1xZ, release mode request 8 (msg 507). **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD15_AI_20261007.md` @963bd381e9
(COO half SIGNED WITH CONDITIONS 1-3).

## VERDICT: SIGNED -- the snapshot, both legs and the per-key rollback, under the COO's conditions plus the four below. The run does not start before condition 3 is met.

## Read by this seat

- **Vendor word: this run IS within Andrew's word, stated here as the COO's condition 2 requires.**
  - Use: Andrew-direct 2026-10-05 ~20:5xZ (PRD C-VENDOR): the AI classifier in this path, with no human review.
  - Volume: Andrew-direct 2026-10-06 00:03Z ("RUn on the full old table", record
    `ANDREW_DIRECT_20261006_0003Z_AI_CLASSIFIER_RUNS_ON_THE_FULL_OLD_TABLE.md`): up to 8,495 rows, the model the existing writer
    calls, name and ticker only, after the direct-match step.
  - This run fits each term. The model is kimi-k3 (`etf_classification_model.MODEL`, the existing writer's). The payload is
    name and key only. The direct-match leg runs first. Keys sent across BOTH AI acts: the old-list act's 2,306 plus this act's
    1,165, less the 150 shared, is at most 3,321 distinct keys. That is under 8,495.
  - Round-8 ruling 2.3 already applied the word; this half confirms it at the act's own numbers. No new word is owed.
- **The mechanism reads true.** Every put is `attribute_not_exists(ticker)`, so no existing row moves. `bd-securities` is read
  only. The second writer of an overlapping key is refused. The rollback deletes only keys absent from the snapshot that carry
  this act's two `updated_by` values: a literal key list the actor controls.
- **The COO's condition 1 is right and binding.** Contract 0.7.0 has no `fixed_income/Cash`, and the runner's bound (the live
  table's sub-classes) still admits it through 17 legacy rows. So the contract's list is the bound, checked per chunk.
- **The names are the open defect.** Each new row writes `name` through `clean_name()`, the function this seat refused at 18:0xZ
  for SC-e-48 (`CTO_HALF_MDPF_SECCLASS_SC_e48_CLEAN_NAMES_V2_20261007.md`: `Abb LTD Sponsored Adr`, split `LTD`/`Ltd`). AI rows
  keep their name (C-WRITER, analysis 2.2), so a later clean-name pass would not repair them.

## Conditions (in addition to the COO's 1-3)

1. **Vendor ceiling, counted.** The act prints, per chunk, the distinct keys sent and the calls made, including retries. The two AI
   acts together send at most 8,495 distinct keys. Any other model, or any field beyond name and key on the wire, stops the AI leg.
2. **Contract bound** (COO 1, made mechanical): the DIRECT re-plan reads 0 `fixed_income/Cash`. After each chunk, the count of
   landed rows whose class/sub-class pair is outside the contract's `values_by_class` reads 0, or the act stops and rolls back
   that chunk.
3. **Names: the act runs at a release head carrying the `clean_name()` fix that re-opens SC-e-48** (that half's items 1-3, with
   its pin test). The DIRECT leg may run before the fix only if it writes no `name`, and today it does. So both legs wait for the
   fix.
4. **Rollback exercise** stays the issuer's act on this signature. It deletes only this act's new keys, by the stated condition. It
   is not run without the issuer naming the trigger in the ledger entry.

Carried, not blocking (rows already open): W26-S5 (142 CUSIP-keyed AI rows land with no `identifier_namespace`); 99 UNPLACED-KEY
entries (cottonwood USD 76.84M) leave FWD-15 short of zero after this act.
