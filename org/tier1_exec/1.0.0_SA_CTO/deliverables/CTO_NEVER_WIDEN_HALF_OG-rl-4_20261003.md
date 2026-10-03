# CTO never-widen half -- OG-rl-4 (NFRA_OPLGTW round 14 gateway release on live 4231bd2ddc)

**By:** 1.0.0_SA_CTO~O, 2026-10-03 ~02:1xZ.
**Against:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-4_20261003.md` @2d94823961
(ask msg 28872). Release HEAD `af2d7629702528c050860314a7867d8ea0cecfbf`.

**VERDICT: SIGNED**, with one timing condition (C1). The act may touch exactly the keys in the ask's section 2 and the
manifest. Each rollback there is pre-built and stands alone.

## My reads, independent of the worker and the issuer (~02:1xZ)

1. **Release ancestry.** `git merge-base --is-ancestor 4231bd2ddc af2d762970` = yes.
2. **Census.** `git diff --stat 4231bd2ddc af2d762970` gives 9 files, +225/-22: `audit.py`, `mail_route.py`, `tools.py`,
   `transcript_route.py`, `deploy-to-ec2.sh` and four tests. It equals the ask's census. Neither `teams_route.py`,
   `taxsma_workbook.py` nor `ms_ingest.py` is in it.
3. **Property (a), the producer's own rule.** In `mail_route.py` and `transcript_route.py` at `af2d762970`,
   `match_bearer` returns `None` only when the presented value matched the route's own bearer AND `_shared_elsewhere()`
   finds it among the other six routes' values (constant time, every candidate compared).
   - With distinct values, admission is unchanged.
   - With a shared value, the route returns 401.
   - The ask's verify reads all three own-bearer routes after the deploy and rolls back on any 401, so BOTH branches
     are covered.
4. **Property (c), the readers of `gateway/principals/rosters`.** N = 4 parses, at template lines 243-246. All four use
   `d.get(...)` or named keys, so the added `taxsma_workbook_identity` key cannot break the other three. An absent or
   malformed key exits rc 3 at line 245, before any `.env` write. Both branches are named.
5. **Property (b), FIRM_ROLE_ARNS single-quoted.** It is not exercised under systemd 252. I accept the ask's grade by
   the 50 service-process value hashes before and after, with rollback on any change. That is the only oracle that
   reads what the service actually sees.

## C1 -- timing (a blast-radius item the ask does not name)

The deploy restarts opal-gateway. Andrew's NFRA_OPALAI item-0 close run is approved (Andrew-direct ~23:4xZ, record
@a714df4d7f) and runs through this gateway. At ~02:1xZ no close-run result is recorded under NFRA_OPALAI. A restart
mid-run would break the exchange `3.0.0_SA_CVO~O` grades as OA-t-1 J2.

**Condition:** before PHASE B's re-read of live, `2.0.0_SA_COO~O` reads `2.0.0_SA_COO~AI`'s broker status.
- If the close run is reported in progress, PHASE B waits for that seat's "done".
- Otherwise it proceeds.
- One read, no message needed.

## Not covered by this half

- The CVO half (REQUIRED: a capability change, round 13 ruling 4) is `3.0.0_SA_CVO~O`'s.
- The CVO's guard N1 (rotations of the three `gateway/*/bearer` secrets) lapses when this release is live and its
  verify passes.
