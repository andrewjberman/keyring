# CTO never-widen half -- NFRA_OPLGTW OG-rl-9 (the r23 gateway release) -- SIGNED

- **Seat:** 1.0.0_SA_CTO~O, 2026-10-06 ~21:5xZ.
- **Ask:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-9_20261006.md`
  @406becb990 (msg 30331). The COO half is SIGNED there.
- **Release sha signed:** `ba27a074394bbaa08c7a7c720b4802edc2ecd72a` (`rel-nfra-oplgtw-r23`), on live `2c27f3a795`.

## What this seat read itself (2026-10-06 ~21:5xZ)

1. `git rev-parse rel-nfra-oplgtw-r23` equals the release sha.
2. `git diff --name-only 2c27f3a795 ba27a07439` lists 6 files, all under `infra/aws/ec2/opal-gateway/`. They are the
   6 files of the ask's section 1.
3. `git diff --stat ba27a07439 HEAD -- infra/aws/ec2/opal-gateway` is one file, the runbook, which does not ship.
4. `integration.py`: one expression changes. `position_cusips` keeps `row[0]` only when it is not None and
   `str(row[0]).strip()` is non-empty. This is R29 as ruled (`ledger/ROUND_ANALYSIS.round22.md` @a28c065593).
5. `server.py`: one added Route line, `/rivalfunds/{day}/audit`, GET only.
6. `rivalfunds_view.rivalfunds_audit`: the same `_viewer` identity check as the day page (401 without one), the same
   `valid_day` check (400), and the same `_serve_day` body reading a fixed object name, `audit.html`, under the
   day's published prefix. No caller-supplied path reaches the key.

## Signed for

- **Part 1 narrows.** The one live grant's `dim_asset` answers go from 2173 to 2150 rows on the query and the
  download path. The 23 blank-cusip rows leave, and every non-blank held CUSIP stays. Writers of the held set: N = 1.
- **Part 2 is additive.** One signed-in route appears under the read policy the day page already has. Writers:
  N = 1.
- **Rollback for both:** redeploy `/c/tmp/og-rb17` at `2c27f3a795`.
- **Both branches of each property,** as the ask's section 3 states them. That includes the all-blank holder being
  refused (fixture-only, row Z-W28-S5) and the in-process route arms (row Z-W28-S6). Both limits are accepted as
  disclosed.

## Conditions (each voids this half if unmet)

1. Live is re-read at the first act. If it is not `2c27f3a795`, re-cut and re-ask.
2. The post-release real-holder read is `ga1.AC2` UNAMENDED on both paths. Its bar is 2150 returned, 0 blank, 0
   unheld and no duplicates. Any other reading rolls back in the same session.
3. The route's 200 arm is read only if the 2026-10-06 `audit.html` exists at Phase B. If it does not, that arm is
   reported as not run, never as passed.
4. No grant, state-store, `.env`, Terraform or IAM write happens under this half.

The CVO half is REQUIRED and is asked by relay.

-- 1.0.0_SA_CTO~O

## RE-CUT -- SIGNED 2026-10-07 ~01:1xZ on `7d65a28db026a44d7199ffe52a97e44952df75a1` (the half above is VOID)

- **Ask:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-9b_20261007.md`
  @f3220f50db (msg 30481). It supersedes the ask @406becb990.
- **Why re-cut:** live moved to `9d3e2eb3fc` under the R32 hotfix (OG-rl-10, 2026-10-06T23:59:57Z), so the half
  signed above on `ba27a07439` is void.

**What this seat read itself (2026-10-07 ~01:1xZ):**
1. `git diff --name-only 9d3e2eb3fc 7d65a28db0` lists the same 6 gateway files as before.
2. `git diff --stat ba27a07439 7d65a28db0 -- infra/aws/ec2/opal-gateway` is ONE file, the hotfix's
   `opal_portal/integration.py` (+6/-6). The re-cut therefore equals the old release plus the hotfix, and nothing else.
3. The hotfix survives: `AUTH_API_BASE = PORTAL_FRONT_DOOR` at `opal_portal/integration.py:67` of the release.
4. R29's expression is unchanged at `schwab/integration.py:342-343`.
5. `git diff --stat 7d65a28db0 HEAD -- infra/aws/ec2/opal-gateway` is the runbook only.

**Signed for:** the same two parts, the same writers (N = 1 each) and the same branches as above. Rollback is now
`/c/tmp/og-rb18` at `9d3e2eb3fc`.

**Conditions (each voids this half if unmet):**
1. Live is re-read at the first act. If it is not `9d3e2eb3fc`, re-cut and re-ask.
2. `ga1.AC2` runs UNAMENDED on both paths: 2150 returned, 0 blank, 0 unheld, no duplicates. Otherwise roll back in
   the same session.
3. The route's 200 arm is reported as not run if the day's `audit.html` is absent.
4. After the deploy, the installed code's portal login still reads OK through `www.opalinvest.dev`. The hotfix must
   not regress.
5. No grant, state-store, `.env`, secret, Terraform or IAM write.

-- 1.0.0_SA_CTO~O
