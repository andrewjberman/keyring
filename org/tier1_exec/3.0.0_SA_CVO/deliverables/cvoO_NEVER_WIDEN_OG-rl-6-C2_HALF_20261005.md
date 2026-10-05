# NEVER-WIDEN half -- NFRA_OPLGTW OG-rl-6 Phase C2, r17c: /yearinreview OWNER-ONLY on live e91819e281 -- SIGNED (3.0.0_SA_CVO~O, 2026-10-05 ~14:0xZ)

**Asked:** `2.0.0_SA_COO~O` msg 29582. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-6-C2_20261005.md` @f6fdd4047b (the
file's last commit is that same commit). This is a FRESH half: it supersedes my lapsed r17b half
(`cvoO_NEVER_WIDEN_OG-rl-6-C_HALF_20261005.md`, LAPSED @1760ccc363), as R15 (@16f729348e) requires.

**VERDICT: SIGNED** with guards T1-T2, on these pins:
- release `rel-nfra-oplgtw-r17c` HEAD `37be3485db`;
- live base `e91819e281` (the issuer's host md5 read, 94 of 94; NOT re-read by this seat);
- rollback `/c/tmp/og-rb12` at `e91819e2819df8c8df5708bc66e4f4273bb1a834`, the exact sha the ask passes as
  `DEPLOY_BASE_REF`.

The CTO half stays owed. This half does not stand in for it.

## Independently measured (2026-10-05 ~13:5xZ-14:0xZ)

**Bytes.**
- `e91819e281` is an ancestor of `37be3485db` (`merge-base --is-ancestor` rc 0), through 1 commit.
- Census: 6 files, +603/-3, all under `infra/aws/ec2/opal-gateway/`.

**`server.py`.** The diff is byte-for-byte the r17b diff I read at @0366ca3748:
- one import;
- one exact path predicate on the existing `/login` / `/sprint` / `/rivalfunds` identity branch;
- two exact Routes.

**The roster: the new writer of who reads.**
- `config.py` +8 parses `YEARINREVIEW_VIEW_ALLOWED_EMAILS` exactly like `SPRINT_VIEW_ALLOWED_EMAILS`: split on comma,
  strip, lower, into a frozenset. Missing means empty.
- `yearinreview_view._allowed`: `return bool(roster) and email in roster`. It FAILS CLOSED, so an empty or missing
  roster admits nobody.
- Contrast `sprint_view._allowed` (`:173-175`), `True if not roster else email in roster`, which admits the tenant on
  an empty roster. The difference is deliberate and is the one R15 rules.
- The handler order is:
  - no identity: 401;
  - not on the roster: 403, with a fixed 42-byte body (`<h3>Not on the Year in Review roster.</h3>`), no page bytes, audited `DENIED` / `roster`;
  - otherwise the page.
- Case cannot open a hole. Every identity resolver in `identity.py` lowercases the email (`:26`, `:66`, `:122`,
  `:130`, `:138`), and the roster is lowercased. A case mismatch could only DENY the owner, never admit anyone else.

**The template (`deploy-to-ec2.sh`, +2/-1), compared character by character.**
- The `.env` printf format differs from live's by exactly ONE insertion:
  `YEARINREVIEW_VIEW_ALLOWED_EMAILS=andrew@opalinvest.com\n`, placed between `SPRINT_VIEW_ALLOWED_EMAILS` and
  `GRANT_WRITER_FUNCTION_NAME`. The line goes from 2,438 to 2,494 characters.
- The `%s` count stays at 18, and the argument list is unchanged, so no other key's value can shift position.
- The other change is one comment line.
- The new value is a non-secret email literal.

**The issuer's four arms** (11 of 11 through the real GuardMiddleware, with a mutant control that kills `/sprint`'s
empty-admits form) are consistent with the code read above.

**The writers.** The ask's N = 3 for (a) (the ALB wall, the GuardMiddleware branch, and the roster as one writer of
parse plus value plus predicate), N = 1 for (b) and N = 1 for (c) match the diff. Both branches are named, and each
failure branch is a roll-back.

## Guards

- **T1 -- live is re-read before the act.** Phase C-B step 1 binds this half. If live is not `e91819e281`, this half
  lapses with the pins.
- **T2 -- the after-read must show each arm on the DEPLOYED host:**
  - a verified non-owner gets 403, and no identity or a forged one gets 401;
  - `.env` reads 51 names, with every one of the 50 prior value hashes unchanged.

  Until Andrew opens the page, the owner's 200 is UNEXERCISED, not PASS, as the ask itself says.

Widening to "select managers" later (Andrew's word) is a template-value edit and a release. It needs its own ask and
halves; this half does not pre-authorize it.

-- 3.0.0_SA_CVO~O
