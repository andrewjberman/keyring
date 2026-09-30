# Never-widen sign-off packet -- the resident st3 -> st4: window 21's two Analysis blockers (S194, S193)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-29 ~08:2xZ.
**Asked by:** ~Y 102630 / 102647 (`org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R21_Y.md`).
**Ledger:** `irpt-resident-st4-yr201-yr211-20260929` (U1 closed, D1 open).

This packet is st3's (`NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_SAVED_TYPE_ST3_20260929.md`, blob 17661cbe, both halves; D1
closed @a45157fe5a) with the deltas below. Every unnamed section reads as st3's, including:
- the install script's own limbs (10 member shas, the factory pre-check, stop only on an empty queue, automatic
  rollback to the prior root);
- the generate Lambda staying unmoved: ~Y measured that generate_installed.py and entry.py do not reference recipe,
  and yr-201 only ADDS `report_security_ids`.

## 1. What ships

| change | commit | files |
|---|---|---|
| IB-yr-201 (row S194, window 21 Y1): a Comparison sends its models in `security_ids`, and a PDF that prints no comparison is refused before publication | f287444013 | recipe.py, resident_worker.py |
| IB-yr-211 (row S193, window 21 Y2/Y4/Y6): an upload whose resolve answers RETRY is logged and re-offered in 60 s | 14c961af32 (carries yr-201) | recipe.py, resident_worker.py |

`git diff ec8f69f718 14c961af32` on the two files: 59 insertions, 2 deletions. ~Y's drain checks: ycharts/generate 290
passed / 30 skipped; the round checks 3/3 and 2/2 pass; ruff and py_compile clean.

## 2. The one move -- `fe64236bbb-st3` -> `fe64236bbb-st4`

- SUMS vs st3: 225/225. Only recipe.py (4fde9ac9 -> b2fbd720), resident_worker.py (95f79dad -> 0b67be2a) and
  resident_bindings.json differ. Tar 266 members, equal to st3's.
- Tar `7d10152c..` at `ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st4.tar.gz`, S3 version
  `jK0FFkzC_Oc8m3mZMiatYrPCpuyOc9ZE`, read back by version: sha equal.
- `resident_host_install_st4_20260929.sh` (sha 7423a589) is st3's script with NEW/OLD/KEY/tar/recipe/worker shas and
  the receipt's ledger changed only. It rolls back to st3.

## 3. Blast radius -- both branches

Writers of an Analysis job's outcome: 1, `ResidentGenerationWorker`, whose rule is read at `resident_worker.py`
@14c961af32 (~Y's decomposition names the lines).

- **Comparison / Multi-Comp (yr-201, moves):**
  - today a Comparison is generated without its models in `security_ids`, and the PDF can print no comparison;
    window 21's Y1 was READY on such a PDF (S194);
  - after, the models are sent, and a PDF printing no comparison stops before publication with a named refusal;
    no uncertified report is published.
- **An upload that resolves RETRY (yr-211, moves):**
  - today it sits RESOLVING until the walker's 600 s wait lapses, so no body is sent (window 21: Y2, Y4, Y6);
  - after, the RETRY is logged and re-offered in 60 s. The re-offers are bounded by ~Y's own rule in the
    decomposition, and the bound is read at the gates.
- **Unchanged:** Overview, saved-type refusal (st3), certification, publication, and every non-Analysis path. No
  Lambda, IAM, queue or schema moves.
- **Reachable:** Analysis submissions, which today means the walk windows.

## 4. Apply protocol

1. ~Y runs its gates on the BUILT st4 (S3 version jK0FFkzC) and the result is recorded in the ledger before the SSM
   run (the CRO's st3 condition, carried).
2. Both halves at HEAD naming this file's blob.
3. LIVE before-read: running root `fe64236bbb-st3`, queue 0/0 (script line 1).
4. SSM run of the install script; running root and member shas read back; polls; 0 Tracebacks.
5. The live proof of both fixes rides the next Analysis window (the K8 re-run window ~D asked for).

**Rollback per key:** the resident root `fe64236bbb-st3` stays on the host; the cutover receipt is copied to
`cutover_receipt.fe64236bbb-st3.json` before the write.
