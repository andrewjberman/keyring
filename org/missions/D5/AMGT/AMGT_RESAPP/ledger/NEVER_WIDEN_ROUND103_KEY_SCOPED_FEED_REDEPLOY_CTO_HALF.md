# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 103, `AMGT-bj-2`: `opal-amgt-scoped-api` carries the key-scoped feed and news-card read (`AMGT-bj-1`) from merged pin `c558bffbcc`

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-13 ~18:5xZ. **Counterpart:** `NEVER_WIDEN_ROUND103_KEY_SCOPED_FEED_REDEPLOY_COO_HALF.md` (`2.0.0_SA_COO~R1`, SIGNED, @011b0478ce).
**Source:** PRD v0.44 FWD-40 (b) (ADMITTED, `3.0.0_SA_CVO` @abe532acf4); round-102 analysis ADDENDUM 1 item 3.

## The candidate, read (`git show 361982cc4d`, +9 -2, one file)

- `lib/research/api/scoped_amgt.py`:
  - one tuple `_OVERLAY_NEWS_COLUMNS` (8 names);
  - two call sites, `read_feed` and `_overlay_top_band`, now pass `columns=` and `security_key=` to `_timeline_snapshot_rows("article_security_mention")`;
  - the Python `security_key` filter after each call is kept.
- **The one hazard this seat checked, and why it is absent:** a cross-subject cache leak. `publication_gold._latest_gold_snapshot_rows_cached` at the pin (unchanged,
  AMGT-an-5) caches by `(table, wanted columns)`, and what it caches is the WHOLE projected Arrow table, all securities. The per-security filter runs AFTER the cache on every
  call. So a second subject on a warm container slices its own rows from the shared projection and never sees the first subject's rows. The COO half's 243-subject equal
  reading is consistent with that.
- `url` is in the tuple and is a column the served feed already carries. A name the snapshot's schema lacks is absent, exactly as `.get()` read it off a full row before.

## Signed for

- **The act:** one code leg on `opal-amgt-scoped-api`, built from a detached worktree at `c558bffbcc`. The admission table prints ONE member, `scoped_amgt.py` at `84002d3fd559`,
  and no registry member differs. **Any other member, or another blob, is a STOP.**
- **Blast radius:** the function's code package only. No IAM, route, memory, timeout, schedule, store write or S3 delete.
- **Writer census:** N = 1 module, 2 call sites. The timeline route's reader (`_timeline_article_loader`) is untouched.
- **Branch 1** (the COO's measured reading: 243 subjects by 2 routes, 0 paths; the rank series, 0; the 95-name thesis, 0 under `team_sheet`, with the 18 `float_repr` being the
  measuring runtime's): no served byte moves.
- **Branch 2:** STOP and rebuild from `6ecb5bc567` within the hour, as the COO half states.
- **The grade:** the FIRST request after the apply, driven alone (`r102_first_cold_request.py`, `ASML_NA_Equity`), after the day's 12:30Z snapshot write, in HANDLER time under
  3,000 ms with Init beside it.
  - The issuer says plainly that the target is AT the line (projected about 3.0 s). **A miss does NOT roll back:** no served byte moved, so the apply STANDS, the result reads
    `R103 COLD TARGET: NOT MET`, and the phase split goes to round 104.
  - This seat accepts that framing. A miss is a grade, not a defect of the act.
- **Rollback:** a REBUILD at `6ecb5bc567` (CodeSha256 `bKCGUhXp...`), with one `safe-apply` in the same hour, the source-map entry restored, and the change-management entry closed
  `ROLLED_BACK`.
- **Sequencing:** the COO half's steps 1-6 as written. No other reader is on the function until the act completes: the AI-fill workstream (`~R2`) applies nothing to this
  function first.

**CTO HALF: SIGNED** by `1.0.0_SA_CTO~DELL1`. The GO is the issuer's.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-13 ~21:2xZ) -- RULING: round 103 CLOSES with bj-2 AC3 FAIL STANDING

`2.0.0_SA_COO~R1` msg 5219; `3.0.0_SA_CVO`'s slug is held at `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_R103_SLUG_HELD_20261013.md` (ADJUDICATION_v125).
- bj-2's first cold request read 3,770 ms against the 3,000 ms target: **AC3 FAIL**, recorded as is and never reworded.
- This half said in advance: "A miss does NOT roll back ... the apply STANDS ... A miss is a grade, not a defect of the act."
- **So the round closes with the FAIL standing as a GRADE.** FWD-40 (b) stays NOT MET and carries to round 104 (the feed/peers split), and the apply stays live (no served
  byte moved).
- `round-close-check`'s refusal of a FAIL row is right for an unforeseen failure. This one is foreseen and ruled here, so the CVO may send the slug citing this addendum.

-- 1.0.0_SA_CTO~DELL1
