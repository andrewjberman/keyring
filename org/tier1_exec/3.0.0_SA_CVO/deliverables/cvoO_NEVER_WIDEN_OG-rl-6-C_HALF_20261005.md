# NEVER-WIDEN half -- NFRA_OPLGTW OG-rl-6 Phase C, the r17b gateway release (/yearinreview) on live e91819e281 -- SIGNED (3.0.0_SA_CVO~O, 2026-10-05 ~03:3xZ)

**Asked:** `2.0.0_SA_COO~O` msg 29457. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-6-C_20261005.md` @f93545276f (the
file's last commit is that same commit). The ask names this half REQUIRED because a new page route is served.

**STATUS 2026-10-05 ~13:0xZ: LAPSED under guard S2.** Andrew ruled the audience OWNER-ONLY ("Visible to me only";
record org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261005_125xZ_THREE_CALLS_NO_STANDBY_YEARINREVIEW_OWNER_ONLY_DSGN_R37_R38_DEV.md
@121b7b016e, relayed by 0.0.0_AB_MSTR~Z msg 29558). The kit changes before the deploy, so release `14e0af86fa` is not the
release that ships. Nothing may deploy on this half; the re-cut bytes need a new ask and a new half.

**VERDICT: SIGNED** with guards S1-S2, on these pins:
- release `rel-nfra-oplgtw-r17b` HEAD `14e0af86fa`;
- live base `e91819e281` (the issuer's host md5 read, 94 of 94; NOT re-read by this seat);
- rollback `/c/tmp/og-rb12` at `e91819e2819df8c8df5708bc66e4f4273bb1a834`, the exact sha the ask passes as
  `DEPLOY_BASE_REF`.

The CTO half stays owed. This half does not answer section 0, the audience question, which is Andrew's.

## Independently measured (2026-10-05 ~03:3xZ)

**Bytes.**
- `e91819e281` is an ancestor of `14e0af86fa` (`merge-base --is-ancestor` rc 0), through 1 commit.
- Census: 4 files, +509/-2, all under `infra/aws/ec2/opal-gateway/`. `tests/` does not ship.

**The `server.py` diff, read whole (+5/-2):**
- one import (`yearinreview_view`);
- one added `or yearinreview_view.is_yearinreview_path(path)` on the GuardMiddleware branch that already holds
  `/login`, `/sprint*` and `/rivalfunds*`: an ALB-OIDC-verified identity plus the blocklist, failing closed on a
  missing header;
- two exact Routes, `/yearinreview` and `/yearinreview/`.

No other route, branch or middleware line moves.

**The predicate cannot widen another path.**
- `is_yearinreview_path` is `path == "/yearinreview" or path.startswith("/yearinreview/")`; `/yearinreviewx` is not
  matched.
- A path the predicate admits only enters the identity branch. It reaches no handler except the two new Routes, and
  anything else is a 404 after identity.

**The view (`yearinreview_view.py`, 83 lines).**
- The handler re-checks identity and returns 401 when the email is empty.
- It serves one bundled file, read once and capped at 2 MB.
- It audits each view (`log_call`, email plus verdict).
- It sends the same headers as `/sprint`: `no-store`, `frame-ancestors` limited to self and the Teams/M365 hosts,
  `nosniff`, `no-referrer`.
- There is no S3 read, no grant read, no store write and no new IAM grant.

**The page (`static/yearinreview/index.html`).** 48,022 bytes, 0 non-ASCII. A scan for `fetch(`, external URLs,
script `src`, `api/`, `token` and `secret` returns no hit, so the page makes no call of its own.

**The writers.** The ask's N = 2 for (a) is the ALB wall plus the GuardMiddleware branch, and it matches the diff:
`yearinreview_view.yearinreview_page`'s own identity check is a second refusal on the same identity, not a new writer
of who reads. N = 1 for (b) and (c) matches. Both branches are named, and each failure branch is a roll-back.

## Guards

- **S1 -- live is re-read before the act.** Phase C-B step 1 binds this half. If live is not `e91819e281`, this half
  lapses with the pins.
- **S2 -- this half covers the bytes at `14e0af86fa`, which are the TENANT-WIDE branch of section 0.**
  - If Andrew rules tenant-wide, this half stands.
  - If Andrew rules owner-only, the kit changes before release, the release sha moves, and this half lapses with the
    pins: the new bytes need a new half.
  - Under no answer does this half certify an owner-only filter that does not exist at these bytes.

-- 3.0.0_SA_CVO~O
