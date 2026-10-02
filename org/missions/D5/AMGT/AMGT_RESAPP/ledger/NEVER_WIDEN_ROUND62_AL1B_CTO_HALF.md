# AMGT_RESAPP round 62 -- `AMGT-al-1` act (B) never-widen pair, CTO half (the timeline day read deadline, track B)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~11:1xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round62/NEVER_WIDEN_HALF_COO_AL1B.md`
@a12291728f, drained @a2ff06d1a1 (msg 28415). Ruling 5a @e041af6102. **Freeze 12:30Z.**

## What I read myself

1. **The live base**, read 11:1xZ: CodeSha256 `E+FAZF0f63S5LxRWs4l3mCfOZgKc3erezTkjxCoVcBY=`, MemorySize 10240. Both equal the COO
   half's base.
2. **The pin:** `a2ff06d1a1` is an ancestor of HEAD. The source diff to `scoped_amgt.py` from the track-A cut @59d350c2a4 is one
   file, +48/-4, which matches CONTENT-DIFF CHANGED 1.
3. **The reader on PROD tolerates the new branch.** At portal PROD `b3a1d8a6`, `TimelinePanel.tsx:99` types `headline: string | null`,
   and `:354` renders `row.headline ?? '[no headline]'`. A null headline does not break the day view; it shows a bracketed
   placeholder. `headline_reason` is unread by the PROD page, so it is ignored.

## Blast radius and rollback

- **The act:** one artifact version and one code-only `safe-apply`; `memory_size` stays 10240.
- **Rollback:** a code-only `safe-apply` with VersionId `YSqlUTOWHwV6H7LePjd1pr9DKomiDo5U`, which restores `E+FAZF0f...`.
- **The served change is on the deadline path ONLY:** a day whose silver read passes 18 s serves mentions with `headline: null` and
  `headline_reason`, as a 200, instead of a sandbox timeout. Every other body is byte-equal.

## Both branches (read from the code's rule)

- **The read finishes inside 18 s:** the body is byte-equal to today's. The controls BA 2026-09-30 and 2026-10-01 read
  `6c25fff80da9be93` and `69ecb7a884a83585` on the warm second call.
- **The read passes 18 s:** a 200 at about 18 s with null headlines. The read completes on its worker and fills the process cache,
  so the next call on that sandbox carries headlines.
- **Failure:** a non-200 on any of the 3 cold BA runs, or a moved control byte -> ROLLBACK.

## Conditions

1. Re-read CodeSha256 before the build (`E+FAZF0f...`); a mismatch is a STOP. The `--build-only` content-diff must be exactly
   CHANGED 1 (`scoped_amgt.py`).
2. The grade is `timeline_b.py`: 3 concurrent cold BA day invokes answer 200, and both control hashes are equal. The planted slow-read
   test passes (3 passed). HTTP 200 alone is never the grade.
3. **Freeze:** deployed AND graded by 12:30Z. Otherwise do not deploy before Andrew's read.
4. NEVER-2: a ledger entry is opened and closed.
5. **Carried, post-demo, for DSGN:** the day view prints `headline_reason` in place of `[no headline]`.

**CTO HALF: SIGNED** for one upload and one code-only `safe-apply` at `a2ff06d1a1` (or a descendant with the same one-file package
diff), on conditions 1-4.
