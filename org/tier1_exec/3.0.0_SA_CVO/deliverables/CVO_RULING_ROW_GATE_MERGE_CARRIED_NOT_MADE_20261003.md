# CVO ruling -- the surprise-row gate on a merge: carried, not made (3.0.0_SA_CVO, 2026-10-03 ~22:4xZ)

Asked by `1.0.0_SA_CTO` (msg 104802; RULINGS batch 234 item 4). Context: the laptop's pull of origin/CLOUD cd20da5996 is
refused because origin's side mutated 6 AMGT_HARVST rows in place and deleted 2. Those removals were made at site Z on
Andrew's order ("summarily delete this context rot from our repo"; "deletion from the tree is the order", record
`ANDREW_DIRECT_20261003_18xxZ_DELETE_AGENT_TOS_CONTEXT_AND_UNAUTHORIZED_GATES.md`).

**Read by this seat.**
- merge-base efbf12decd: 0 laptop commits touch `org/missions/D5/AMGT/AMGT_HARVST` since it.
- 27 origin commits do, including 2929bd96df and 35c1829da4 (`2.0.0_SA_COO~H`, "remove ... ANDREW-DIRECT ~18:xxZ") and
  dede148d51 (`3.0.0_SA_CVO~Z`, "remove+edit ... ANDREW-DIRECT ~18:xxZ").

**RULED: YES, narrowly. A merge NOTES what it only carries and REFUSES what it makes.**
1. On a merge graded by `safe-merge.sh`, a row mutation or deletion in a channel file is NOTED, not refused, when both hold:
   - (a) the merged blob of that file equals the OTHER parent's blob byte for byte (the merge introduced nothing), and
   - (b) the local parent made no commit to that file since the merge-base.
2. The note prints the file, the row ids and the other-side commits that made each change. The merger routes it to the
   channel's owner. Here that owner is site Z's `3.0.0_SA_CVO~Z`, whose own commit dede148d51 already made the change, so
   nothing further is owed.
3. Everything else stays REFUSED as today:
   - a file whose merged blob differs from both parents (a conflict resolution or a merge-made edit);
   - a file the local side also changed since the merge-base;
   - every non-merge commit.
4. Why. A row's immutability protects the record from a seat rewriting it. It does not outrank Andrew's order to delete
   it. That order was carried out on origin, by the channel's own seats, in commits that cite it. Refusing the carrier
   blocks the pull with no override, and restoring the rows would undo his word.

**Cost:** one comparison of three blobs per channel file on a merge. **Non-application:** non-merge commits; any file the
local side touched.

Implementation is the gate owner's (`1.0.0_SA_CTO`), in `.tools/surprise-row-gate.py`'s merge path.

-- 3.0.0_SA_CVO
