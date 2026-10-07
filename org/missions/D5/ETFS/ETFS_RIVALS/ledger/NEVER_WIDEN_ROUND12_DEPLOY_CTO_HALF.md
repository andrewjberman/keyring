# NEVER-WIDEN -- CTO HALF: ETFS_RIVALS round 12 -- five rivalfunds Lambdas at CLOUD 50a2248fe9, one 10-06 republish

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~17:3xZ. **Pairs with:** the COO half
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/NEVER_WIDEN_HALF_COO_ROUND12_DEPLOY.md` @d6cbfb634b
(msg 30150). **Route:** round-10 analysis ADDENDUM 4 @56de423b4d, steps 1 and 2.

## VERDICT: SIGNED

## The base, re-read live at signing

- **The pin:** 50a2248fe9 is a commit, and `merge-base --is-ancestor 50a2248fe9 CLOUD` passes.
- **The plan:** `C:/tmp/rv_plan12.txt` reads `0 to add, 5 to change, 0 to destroy`, and the only changed attribute shown is
  `source_code_hash`. The five "before" hashes equal the live CodeSha256 of all five functions:
  - `etfs-rivalfunds-daily-lambda` CGLr1BNO...
  - `etfs-rivalfunds-fetch-holdings-lambda` nhBoabXY...
  - `rivalfunds-build-canonical-shape-lambda` wLYfa47Z...
  - `rivalfunds-build-silver-lambda` CTEET1+c...
  - `rivalfunds-publish-page-lambda` RBRmqCj9...

  All five were last modified 2026-10-05 21:58Z. So the plan is against the live state.
- **The served page:** `s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-06/index.html` is 1,813,001 B,
  LastModified 13:07:38Z, equal to the COO half's control. `.../audit.html` returns 404 (absent), as the half states.

## Writers of what moves

- **The page keys:** N = 1 code writer, the publish-page stage. The scheduled chain and this act's one manual republish both
  enter it.
- **The republish's `"date":"2026-10-06"`** names a day already published today. It creates no date the scheduled path could not
  reach; that path re-reaches this day only on a same-day re-run.
- **Both A1 branches are covered** (the producer's rule in `produce_a1` with `refresh_a1: false`):
  - SKIP is measured.
  - REBUILD is unmeasured, and it carries ok-1's re-keying, which ruling (A) @982e914b1d read as a no-op on live data (Z-S43).
  - Whichever branch fires, the grade below applies to the served page.

## Conditions

1. Apply that saved plan only. Any drift that `safe-apply` reports against it is a STOP, not a re-plan.
2. **Bytes moved:** after the apply, all five live CodeSha256 equal the plan's "after" hashes.
3. **Grade on the SERVED page after the republish**, not on the local real run. Print each number:
   - `holding_dialogs: on` in the manifest;
   - headroom of at least 20% under `DIALOG_SOFT_CAP`;
   - every `data-sec` button's `popovertarget` resolves in the same document, with 0 dead;
   - no audit block and no link to `audit.html` on the main page (ADDENDUM 4 step 1);
   - 13 of 13 funds updated.

   A differing read means rollback by the COO half's table.
4. **NEVER-2:** the entry `etfs-rivalfunds-round12` opens before the apply and closes after condition 3 is printed.

## Z-S50 (answered here, NOT part of this act)

Andrew's word is "hyperlinked to the modal popup for **that fund's** engagement with that security". So a name shared by two
listings is resolved by the fund's own holdings:
- Where the fund holds exactly one of the listings, the mention links to that one. Andrew's "any mention" supersedes the
  RIV-ln-1 plain-span rule for this case.
- Where the fund holds both listings, or neither, the mention stays plain, because a guessed link is a wrong link. The page
  counts it.

This is a round-13 enrichment cell. It does not gate this deploy.

`1.0.0_SA_CTO~Z`, 2026-10-06 ~17:3xZ.
