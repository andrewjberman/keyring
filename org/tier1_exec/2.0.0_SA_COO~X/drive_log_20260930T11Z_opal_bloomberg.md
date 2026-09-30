# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 11Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 11:14Z | L7 | 24 | workers spawned: z-1 (`~1`, worker), z-2 (`~2`, worker-light), z-4 (`~4`, worker); z-3 is this seat's read of the 13:00Z fire |
| 11:22Z | L7 | 24 | the z-4 worktree base `9c9fa60bc8` contains the issuance (`is-ancestor` rc 0); the round-23 packet (27095) was READ at 10:42Z |
| 11:3xZ-11:48Z | L7->L8 | 24 | z-2 re-graded (AC1 `z2 sources_searched 13 anchor none ... census_file True`, raw bytes read; AC2 5 passed; posc VALID) and merged `92f1403d25` |
| 11:45Z | L7 | 24 | row `Z-S69` `74c8602a0c`: TSM `CUR_MKT_CAP`, a USD listing-currency value, is served labelled TWD. The rule reaches 79 header figures on 27 mixed-currency securities, and 1 is measured wrong. INERT |
| 11:52Z-11:55Z | L7->L8 | 24 | z-1 re-graded (AC1 exact, `projected_after 49`; AC2 38 passed; the F4/F5 same-currency guard read in code) and merged `d342614233`; the channel conflict was resolved with both sides kept |
| 11:53Z | L7 | 24 | rows `Z-W1-S19` and `Z-W1-S20` ruled `717cbb0a14` |

## Compiler Tools

- `z1_AC*.sh`, `z2_AC*.sh`, `proof-of-spec-check.py`, `safe-merge.sh --continue`; the issuer's census of header currency labels over the newest block of 100 keys.
- Gaps: the first census predicate matched on None == None for 4 securities with no stated reporting currency; the row counts only the stated class.
