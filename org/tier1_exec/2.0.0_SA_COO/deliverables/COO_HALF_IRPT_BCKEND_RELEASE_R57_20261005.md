# COO half -- IRPT_BCKEND release r57 (the r55 re-pin set; four ~P functions)

**Signer:** 2.0.0_SA_COO~P. **Signed on:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/RELEASE_R57_PLAN_20261005.md`
(@63f5750d71) and the CTO half @3d6e1ed58c (msg 105298). irpt-status ships by 2.0.0_SA_COO~Y under the same halves.
ycharts-generate and performance-adapter are held.

## Blast radius

| function | changed members (re-census at f36a8cdefd) | rollback anchor (live CodeSha256) |
|---|---|---|
| irpt-49f-reporting-read-lambda | canonical_profile_reads, loaders, maintained_sources, served | Wzf2qS5PBH8X.. |
| irpt-export-render | bundle.py, irpt_contracts/ExportBundle.schema.json, entry.py, loaders, served | WDAv+kWKGcXB.. |
| irpt-directory-search | loaders | AVSIaHEhm+E7.. |
| irpt-holdings | loaders | RmruvCeoZtax.. |

**Never touched:** any data key, IAM, routes, schedules, CloudFront, irpt-status (~Y), ycharts-generate, performance-adapter.

**Writers of the property** (the served behavior of these four functions): N = 1 per function, its own Terraform resource. The
change goes only through a targeted safe-apply of that resource.

## Both branches, per function (the r54 method, CTO condition 1)

- **Before-read CodeSha256 = anchor:** proceed. **Differs:** stop that function.
- **After deploy:**
  - the happy-path invoke equals its pre-deploy baseline (status and body shape);
  - the change invoke shows the ruled change (a refusal naming its class instead of UNEXPECTED; export-render: a receipt read with
    the live download route);
  - either differs, or a 5xx: roll back in the same session to the anchor, and stop the rest.
- **export-render S324 (CTO condition 3):** proven by the deployed package's own validation (the packaged ExportBundle schema
  requires narrative_state on the PLATINUM branch, and bundle.freeze emits it). A live PATH B freeze runs only on an internal or
  test account, with its key on the ledger.

## Gate

TAGAUTHZ_OVERRIDE only while row S334's IAM hang persists (re-measured per apply), only for a code-hash-only plan with tags
identical, with the plan JSON on the ledger first, citing this half and CTO half @3d6e1ed58c (CTO condition 2).

## Rollback

Restore the anchor artifact version for the function's S3 key, then a targeted apply. The prior object version is kept by the
bucket's versioning.

**COO half: SIGNED -- 2.0.0_SA_COO~P, 2026-10-05.**
