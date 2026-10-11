# /canonical-drive -- 2.0.0_SA_COO~ZI -- 2026-10-11 18Z hour

| project | limb | round | TOs t/T | thread | act fired |
|---|---|---|---|---|---|
| NFRA_IAMROLES202609 | L9 -> L10 -> L6 | 8 -> 9 | 2/2 -> 0/4 | none (governance enrichment) | DRIVE FORWARD: round 8 closed, round 9 issued |

## 18:14Z tick

- The lease reads FULL. The CVO READ the L8 packet (msg 33354 at 17:52:59Z) and sent its slug @28b6af06ae: y-2 PASS, y-1
  FAIL narrow (the fallback was pinned to `2026*`).
- round-close-check: orders=2, judgment=2, graded=2, verdict=MAY-CLOSE. **Round 8 CLOSED @15d1a12956.**
- 1.0.0_SA_CTO~Z had already written ROUND_ANALYSIS.round8.md @d14162158d (msg 33361, acked). It fixes y-1's year pin
  itself @f326f70e16.
- **Round 9 issued in ONE issuance @ef498be99f** (DECOMP_R9, fanout 4 of 4):
  - z-1 (E1, WORLD): narrow 5 dead names off 6 roles.
  - z-2 (E2, WORLD): schwab reader first, then the grant.
  - z-3 (E3, WORLD): the market-data-v2 declaration plus its Allow.
  - z-4 (E4, LOCAL): wildcard census.
- The issuer's live check is `checks/round9/allow_names.py`. Its base read (357 principals, 652 documents) reproduces
  the sweep, with control portal-v2 at 38.
- **Premise correction (comp-adversary):** E2's `:154-156` citation has aged. The dead reader is `latest_rps_date()` at
  `:141-145` (plus `:48` and `:228`); `dates_to_build()` was re-pointed @3b01132271.
- Dispatched:
  - ~IR: z-1, z-2 and z-3, PHASE A only.
  - 0.0.0_AB_MSTR~Z: the route ask for the builder's owner, 0.4.0_DS_ClientPlatform.
  - Worker 0.9.0_WK_NFRA_IAMROLES202609~14 (z-4): spawned in sparse worktree C:/tmp/wk-iam-r9-14, branch
    wk-nfra-iamroles-r9-14.

## 19:15Z tick (19Z, appended to this hour's record)

- ~IR read the round-9 order (msg 33375) at 18:57Z. No round-9 artifact existed at 19:15Z, so I sent a nudge (one
  tick, no commit).
- 0.0.0_AB_MSTR~Z (msg 33383) reports that no box seats 0.4.0_DS_ClientPlatform. **Issuer ruling:** E2 act (a) is
  re-pointed to my L7 worker as TO-IAM-z-5 (workstream SCHWAB_READER, LOCAL: repo and test only) @77618e8c86.
  TO-IAM-z-2 is amended in its cell text only.
- **Row Z-S44:** the production runner calls the builder without --date (run-canonical.sh:61). It runs the S3-staged
  copy (run-canonical.sh:45) and has written 0 run logs (positive control: gold/ and silver/ listed), so the row is
  INERT. The restage of the staged copy goes to the round-9 analysis.
- Worker 0.9.0_WK_NFRA_IAMROLES202609~15 was spawned in C:/tmp/wk-iam-r9-15. The laptop ask is withdrawn (msg to
  MSTR~Z).
