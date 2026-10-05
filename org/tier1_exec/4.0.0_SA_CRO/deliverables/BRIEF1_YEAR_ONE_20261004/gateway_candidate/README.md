# /yearinreview -- gateway release kit (Brief #1)

Order: Andrew-direct 2026-10-04, verbatim "id publish it at mcp.opalinvest.dev/yearinreview". Record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261004_194xZ_BRIEF1_WHERE_WEVE_BEEN_ONE_YEAR_SCALE_ONE_PAGER.md`.
Author: 4.0.0_SA_CRO~2026. Release owner: the opal-gateway release lane (NFRA_OPLGTW OG-rl procedure).

## Why this is a kit, not a release from the laptop

The live gateway runs `af2d762970` (EC2_MANIFEST, deployed 2026-10-03T16:55:49Z, OG-rl-4). That commit is not on
this laptop or on origin (read 2026-10-04: `git cat-file` after `git fetch origin` -> not a valid object), and the
mcportal checkout the deploy script needs is not initialized here. A release cut from this tree would drop r14's
changes. So the change ships as files plus an anchored hookup, to be applied on top of the live base by the lane that
holds it.

## What it adds (no S3, no IAM, no new storage address, no ALB change)

| File | Purpose |
|---|---|
| `app/yearinreview_view.py` | GET /yearinreview serves one bundled page; /yearinreview/ redirects; same identity wall and frame policy as /sprint |
| `app/static/yearinreview/index.html` | The page, byte-equal to `../YEAR_ONE_ONE_PAGER.html` (sha256 prefix a31571e8012026a8), ASCII-only |
| `tests/test_yearinreview_view.py` | 5 ACs, both arms: path predicate, bundled page present and capped, 401 without identity, 200 with identity and frame policy, trailing-slash redirect |
| `apply_hookup.py` | Three anchored edits to `app/server.py`: the import, the GuardMiddleware identity branch (same as /sprint and /rivalfunds), two Routes after /rivalfunds/{day}; refuses if an anchor count is not exactly 1 or if already applied |
| `server_hookup.patch` | The same three edits as a unified diff against CLOUD's `app/server.py`, for review |

## Apply and release (on the device holding the live base)

1. Release worktree at the live base (`af2d762970`), as in OG-rl-4.
2. Copy `app/yearinreview_view.py`, `app/static/yearinreview/index.html` and `tests/test_yearinreview_view.py` into
   `infra/aws/ec2/opal-gateway/` at the same relative paths.
3. `python apply_hookup.py infra/aws/ec2/opal-gateway/app/server.py`
4. `python -m pytest -q infra/aws/ec2/opal-gateway/tests/test_yearinreview_view.py` -> 5 passed.
5. Release through `safe-ec2-deploy.sh opal-gateway ...` with the deploy-ledger entry, rollback tree and verify, as in
   OG-rl-4.
6. Live check: unauthenticated `GET https://mcp.opalinvest.dev/yearinreview` -> 302 to login.microsoftonline.com;
   signed in -> 200, title "Opal Year One Review".

## Evidence on this laptop (2026-10-04)

- Kit applied to a scratch copy and to a detached worktree of CLOUD HEAD: `app/server.py` compiles and imports, with
  routes `/yearinreview` and `/yearinreview/` registered.
- Full gateway suite on the CLOUD worktree with `--continue-on-collection-errors`: baseline 3 failed, 419 passed,
  15 errors; with the kit 3 failed, 424 passed, 15 errors (the 5 new tests; the 3 failures and 15 collection errors
  are pre-existing and unchanged).
- To refresh the page later: rebuild with `../build_year_one.py`, copy `YEAR_ONE_ONE_PAGER.html` over
  `app/static/yearinreview/index.html`, release.
