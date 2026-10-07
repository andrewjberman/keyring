# CVO never-widen half -- NFRA_OPLGTW OG-rl-9 (the r23 gateway release) -- SIGNED

- **Seat:** 3.0.0_SA_CVO~O, 2026-10-06 ~21:55Z.
- **Ask:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-9_20261006.md`
  @406becb990, relayed by `1.0.0_SA_CTO~O` msg 30333. COO half SIGNED in the ask; CTO half SIGNED
  @cd1344d1b0.
- **Release sha signed:** `ba27a074394bbaa08c7a7c720b4802edc2ecd72a` (`rel-nfra-oplgtw-r23`), on live `2c27f3a795`.

## What this seat read itself (~21:5xZ)

1. `git rev-parse rel-nfra-oplgtw-r23` equals the release sha. Live `2c27f3a795` is its ancestor, two commits below.
   `EC2_MANIFEST.json` reads `deployed_commit` `2c27f3a795...`.
2. `git diff --name-only 2c27f3a795 ba27a07439`: 6 files, the ask's section 1 table. Release against CLOUD in the
   gateway tree: the runbook only.
3. **Part 1, the held set.** `integration.py:342` keeps `row[0]` only when it is not None and `str(row[0]).strip()`
   is non-empty. `_asset_holdings` is the one writer; its three call sites (`:658` query, `:842` download pre-check,
   `:941` download/export) pass the set to `sem.qualify_asset_plan`; a grep of the file finds no fourth. `semantics.py:349` refuses an empty set with
   `asset_read_denied_unqualified`, so the all-blank holder is refused and never falls back to every cusip.
4. **Part 1, the before state.** This seat re-ran `ga1.AC2` at round 22's L8: 2173 returned = 2150 held + 23 blank;
   0 non-blank unheld (`ADJUDICATION_v14.Z.md` C-S38). The narrowing removes the blank key only.
5. **Part 2, who can reach the route.** `server.py:203` guards by `is_rivalfunds_path`, a `/rivalfunds/` prefix test,
   so the new path takes the day page's branch: ALB-OIDC identity plus the blocklist, fail-closed. The handler
   repeats the `_viewer` check (401) and `valid_day` (400). The key is `<prefix>date=<day>/audit.html`, a fixed
   name; no caller text reaches it beyond a validated date. ROUTE_CLASS declares it `access-layer`, as the day page.
6. **Part 2, the audience.** The module's viewers are any signed-in account. That audience for the audit page is
   Andrew's ("We should have it", record @56de423b4d, cited by ETFS_RIVALS round-11 ADDENDUM 1 @2f44b42430).
7. **Part 2, IAM.** `infra/aws/terraform/opal-gateway/rivalfunds-iam.policy.json` allows `s3:GetObject` on
   `opal-data-etfs/rivalfunds/etfs/platinum/page/*`, which covers the audit key. No IAM change is needed.
8. **Part 2, the object.** `head-object` on `.../page/date=2026-10-06/audit.html`: 1,337,761 bytes, modified
   2026-10-06T21:18:30Z. The 200 arm has its object.
9. **Who routes users to the route.** No served page links to `/audit` today: ETFS_RIVALS lk-1 (the page link) lands
   only after the route serves a signed-in 200. Before the release the URL is a 404, so no user loses a working link
   in either direction.

## Signed for

- **Part 1 narrows:** the one live `dim_asset` grant's answers go from 2173 to 2150 rows on the query and download
  paths. Writers of the held set: N = 1. Both branches: non-blank holdings all stay; an all-blank holder is refused.
- **Part 2 is additive:** one signed-in GET under the day page's own guard, audience and read policy. Writers: N = 1.
  Both branches: 200 with the object's bytes; 404 with its own body.
- **Rollback for both:** redeploy `/c/tmp/og-rb17` at `2c27f3a795`.
- The two disclosed limits are accepted: the all-blank refusal is fixture-only (Z-W28-S5; this seat read the refusing
  line itself, item 3), and the route arms run in-process, not through the ALB (Z-W28-S6).

## Conditions (each voids this half if unmet)

1. Live is re-read at the first act; if it is not `2c27f3a795`, re-cut and re-ask.
2. The post-release real-holder read is `ga1.AC2` unamended, on both paths: 2150 returned, 0 blank, 0 unheld, no
   duplicates. Any other reading rolls back in the same session.
3. The route's 200 arm is reported as run only if it was read against the 2026-10-06 object; the day page
   `/rivalfunds/2026-10-06` still returns its own bytes after the release.
4. No grant, state-store, `.env`, Terraform or IAM write happens under this half.

## Not signed, noted for the owner

`audit.html` is 1,337,761 bytes against the viewer's 2,097,152-byte read cap (64 %). Past the cap the route returns
502, not the page. This is ETFS_RIVALS's to watch, not a release blocker.

-- 3.0.0_SA_CVO~O
