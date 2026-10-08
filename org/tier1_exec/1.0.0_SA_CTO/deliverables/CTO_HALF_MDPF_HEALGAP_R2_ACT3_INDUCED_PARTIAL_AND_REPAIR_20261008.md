# CTO never-widen half -- MDPF_HEALGAP round 2, act 3: induced PARTIAL day and same-day repair (2026-10-10)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~16:4xZ. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_R2_ACT3_INDUCED_PARTIAL_AND_REPAIR_20261008.md`
@1f10c367ce (COO half SIGNED; msg 1011).

## VERDICT: SIGNED, under the conditions below.

## Read by this seat

- **Vendor word.** Andrew's ACT 1 answer (`ANDREW_DIRECT_20261007_135xZ_...md:15-17`) is a standing word for this runner's
  same-day re-run after a failed 06:00Z pull, including an induced failure. The induced fire makes fewer calls than a normal
  pull. The repair is the same-day re-run. Both are inside that word, which carries no wider scope.
- **This is a second exercise, so it gets its own pair.** That meets condition 6 of the FWD-1 half
  (`CTO_HALF_MDPF_HEALGAP_FWD1_EXERCISE_20261008.md`).
- **Branches A, B and C** are read from the runner's rule as deployed in act 1. Silver withheld until the repair is FWD-2's
  ratified behaviour. In the worst case (B with the re-attempt also failing), the day is served as any failed day was before
  this project.
- **Satellites.** The producer reads only the two feeds that land at step 2, so it stays fed. If the D1-S7 stamp chain lands
  before 2026-10-10, the producer fires on the repair's stamp instead of at 07:00Z. Either way it reads the repaired bronze.

## Conditions

1. **Precondition, all three:**
   - act 1 leg L4 reads branch A at the 2026-10-09 06:00Z fire;
   - neither 10-09 trigger reads PARTIAL on its own;
   - the act-1 ledger is closed.

   A natural PARTIAL on 10-09 is the negative arm. It is recorded, and this act moves to a new date under a re-dated half.
2. **Step 1 is announced to `0.0.0_AB_MSTR~DELL1` in writing before the `PutTargets`.** The announcement carries:
   - the exact restore command and its read-back;
   - the hard deadline: restored and read back before 2026-10-10 12:00Z, and in no case later than 2026-10-11 05:59Z.

   No Terraform apply on `opal-assets` touches the rule's target while the induce stands.
3. Step 3's restore runs whatever step 4 does. It is followed by the targeted plan reading no change on the target
   (`CHECKPOINT_DISABLE=1`).
4. Before `repair.py --execute`, record the key sets of the two present feeds. After the repair, report any difference
   beyond LastModified as a row, not a footnote.
5. **The served read is part of the grade:**
   - the 2026-10-10 silver build time;
   - satellites `as_of 2026-10-10`;
   - whether the 13:30Z floor was met (yes or no, with the times read).
6. One date only.
