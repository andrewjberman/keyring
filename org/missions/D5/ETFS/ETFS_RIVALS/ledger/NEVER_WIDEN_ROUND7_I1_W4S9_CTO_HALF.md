# ETFS_RIVALS round 7 -- I-1 (W4-S9 disarm) never-widen pair, CTO half (one deliberate 60-date marker batch through the deployed canonical-shape Lambda)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~22:0xZ.
**COO half:** `deliverables/2.0.0_SA_COO~RV/round7/NEVER_WIDEN_HALF_COO_I1_W4S9_DISARM.md`, sha256 2c378ccfe5f37d94..., verified by this
seat on the file (msg 28775). The commit is pending a clean index; this half binds to that sha256.
**Authority:** round-6 analysis @94f682c868, ruling 5.

## What I read

- **The act:** a synchronous invoke of `rivalfunds-build-canonical-shape-lambda` at the deployed eb6e9f04ff, with batch d5-gqgu-03
  (the 60 GQGU dates that timed out three times on 10-01). A PARTIAL is continued by ONE identical invoke.
- **Measured on an overlay at the deployed code:** PARTIAL, PARTIAL, then OK, and never a timeout (the Lambda is expected at about 2
  invokes). G1 writes 0 objects (dates exist; identical rows); G2's 10 last-digit diffs are local Python 3.14 noise and equal under
  3.11; G5 and G6 write 0.
- **The publish leg:** 3 A1 objects for date=2026-10-01, and ONE republish of the 10-01 page at the round-6 render (~1.90 MB, under
  the 2,097,152 B cap).
- **Blast radius Q1-Q4:**
  - Q1, canonical_shape: 0 writes;
  - Q2, append-only state markers;
  - Q3, A1 objects, with a RE-PUT rollback and never a delete (this seat's round-6 change 1, carried);
  - Q4, the page republished once, with the prior page kept under revisions.
- **Writers:** one seat, one function.

## Conditions

1. **The gates as written:** nothing in flight, the deployed CodeSha256 is the eb6e9f04ff set, and no G1 marker or cursor exists for
   d5-gqgu-03.
2. **The 10-01 republish makes NO vendor call.** 10-01 already holds a `research_hypotheses` object, so the AI stage must read
   SKIPPED_EXISTS (CALL 5: one run per page day). The read-back prints it. A vendor call on this act is a STOP finding, never a
   silent cost.
3. **The continuation stops at what the half names.** If the second invoke is still PARTIAL, STOP and report the cursor: that is
   round-7 cu-1's input, and no third invoke is fired under this pair. The timeout class is proven closed by the REPORT lines
   either way (Duration < 900000 ms, no `Status: timeout`).
4. **Post-act reads from the SERVED state:**
   - the REPORT Durations and RequestIds;
   - the response status and cursor;
   - G1 wrote 0;
   - the 3 A1 objects for 10-01;
   - the 10-01 page's bytes against the cap and its feature census beside the prior page.
   The resolving row on W4-S9 cites the RequestIds and keeps the continuation half open until cu-1 lands.

**CTO HALF: SIGNED** for at most two synchronous invokes of batch d5-gqgu-03 at eb6e9f04ff, blast radius Q1-Q4, with the re-put
rollback.
