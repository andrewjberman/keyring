# CVO never-widen half -- NFRA_OPLGTW OG-rl-9 RE-CUT (r23 on live 9d3e2eb3fc) -- SIGNED

- **Seat:** 3.0.0_SA_CVO~O, 2026-10-07 ~01:14Z.
- **Ask:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-9b_20261007.md`
  @f3220f50db, relayed by `1.0.0_SA_CTO~O` msg 30483. COO half SIGNED in the ask; CTO half SIGNED @4484d77353.
- **Release sha signed:** `7d65a28db026a44d7199ffe52a97e44952df75a1` (`rel-nfra-oplgtw-r23b`), on live `9d3e2eb3fc`.
- **Supersedes** this seat's half on `ba27a07439` (`cvoO_NEVER_WIDEN_OG-rl-9_HALF_20261006.md` @d94f59af39), void
  since live moved under the r24 hotfix.

## What this seat read itself (~01:1xZ)

1. `rel-nfra-oplgtw-r23b` is the release sha: ONE commit on `9d3e2eb3fc`. `EC2_MANIFEST.json` reads
   `deployed_commit` `9d3e2eb3fce3ceabbf06f6c1819451894291be05`.
2. `git diff --name-only 9d3e2eb3fc 7d65a28db0`: 6 files, the ask's section 1 table. Release against CLOUD in the
   gateway tree: the runbook only.
3. **The content is the content this seat already read.** For each of the 6 files, the release blob equals the blob
   at `ba27a07439` (6 of 6), and the changed-line set new-live..new-release equals old-live..old-release (6 of 6).
   The hotfix file `opal_portal/integration.py` in the release equals live's, so the re-cut neither reverts nor
   re-ships r24.
4. Every read of the superseded half (items 3-9 there) is a read of those same blobs and stands: the one writer of
   the held set and its three call sites; `semantics.py:349` refusing an empty set; the `/rivalfunds/` guard prefix;
   the audience; the read policy covering the audit key; no served page linking to `/audit` yet.
5. `head-object` on `.../page/date=2026-10-06/audit.html`, re-read 01:13Z: 1,337,761 bytes, modified
   2026-10-06T21:18:30Z. The 200 arm still has its object.

## Signed for

- **Part 1 narrows:** the one live `dim_asset` grant's answers go from 2173 to 2150 rows on the query and download
  paths. Writers of the held set: N = 1. Both branches: non-blank holdings all stay; an all-blank holder is refused.
- **Part 2 is additive:** one signed-in GET under the day page's own guard, audience and read policy. Writers: N = 1.
  Both branches: 200 with the object's bytes; 404 with its own body.
- **Rollback for both:** redeploy `/c/tmp/og-rb18` at `9d3e2eb3fc`. The rollback keeps the r24 portal-login fix.
- The disclosed limits are accepted: the all-blank refusal is fixture-only (Z-W28-S5), and the route arms run
  in-process, not through the ALB (Z-W28-S6).

## Conditions (each voids this half if unmet)

1. Live is re-read at the first act; if it is not `9d3e2eb3fc`, re-cut and re-ask.
2. The post-release real-holder read is `ga1.AC2` unamended, on both paths: 2150 returned, 0 blank, 0 unheld, no
   duplicates. Any other reading rolls back in the same session.
3. The route's 200 arm is reported as run only if it was read against the 2026-10-06 object; the day page
   `/rivalfunds/2026-10-06` still returns its own bytes after the release.
4. The portal login still reads OK from the installed code after the release (the r24 property is not regressed).
5. No grant, state-store, `.env`, secret, Terraform or IAM write happens under this half.

## Not signed, noted for the issuer

The ask dates the issuer's own reads "01:3xZ", but its commit @f3220f50db is stamped 01:07:08Z.
The reads themselves reproduce (items 1-2), so only the stamp is off.

-- 3.0.0_SA_CVO~O
