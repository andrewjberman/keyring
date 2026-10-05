# AMGT_HARVST round 45 -- HVST-ar-1 served silver re-derivation, never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-04 ~23:1xZ. **COO half:**
`deliverables/2.0.0_SA_COO_H/round45/NEVER_WIDEN_HALF_COO_SILVER_REDERIVE.md` @b5d31484b7 (msg 29305). **Authority:** round-44
analysis @ed9efe80ea ruling 1 (FWD-2).

## What I read

- **The act is bound to a plan digest** (`9d7b7d57c651...`). `--write` re-runs the identical plan and refuses any other digest, then
  requires every planned row to be the row its `article_key` serves after the write.
- **The rule is the producer's own** (the act's docstring):
  - served rows are chosen by `store.supersedes`, the one rule every silver reader shares;
  - an original is rebuilt only when it is its article's served row and its `record_hash` differs;
  - an article with no served row gains one;
  - another fetch of a served article is never planned.
- **Dry run 2:** 1,978 rebuilt plus 17 new = 1,995 rows in 13 new parts, with **CHANGED 0** and **GONE 0**. Dry run 1 FAILED the gate
  on mixed column types and wrote nothing; that failure is why the type-compatible bins exist.
- **Writers of silver `article`, N = 3:** the HarvestUploader on a collection run, LegacyUploader (not run), and this act.
  - Every put is `IfNoneMatch="*"`, so nothing is overwritten.
  - Gold is untouched; its next rebuild takes its own pair.

## Conditions

1. **One writer at a time.** No collection run (writer 1) starts until this act's write record is complete and verified. Andrew's
   one-run-per-publisher word (@441338fdf7) already follows this round.
2. **Rollback is append-only, never a delete.** If the served-plane verify fails, restore by appending a newer part per affected
   bin that re-serves the prior rows under `store.supersedes`; nothing is deleted. That is the round-43 pattern. Deleting the 13
   new keys, as the COO half names, is an S3 delete, so it takes Andrew's word at the time (CLAUDE.md Agent Autonomy).
3. The verify reads the SERVED plane, not the write's own return. The 17 new articles and a sample of rebuilt rows per publisher
   serve their new typed fields through the silver reader, and the CHANGED/GONE counts re-read 0 after the write.
4. One NEVER-2 entry, opened before `--write`.

**CTO HALF: SIGNED** for plan digest `9d7b7d57c651...` under conditions 1-4.
