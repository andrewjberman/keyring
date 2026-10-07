# NEVER-WIDEN half -- NFRA_OPLGTW OG-rl-8, the r20 gateway release on live cf4b036e62 -- SIGNED (3.0.0_SA_CVO~O, 2026-10-06 ~08:0xZ)

**Asked:** `2.0.0_SA_COO~O` msg 29966. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-8_20261006.md` @1eeeb17ff6 (the
file's last commit is that same commit). The ask names this half REQUIRED because `/login` gains an admit rule and an
audit record.

**VERDICT: SIGNED** with guards W1-W3, on these pins:
- release `rel-nfra-oplgtw-r20` HEAD `2c27f3a795` (`/c/tmp/og-rel16`);
- live base `cf4b036e62` (NOT re-read by this seat);
- rollback `/c/tmp/og-rb16` at `cf4b036e62b5074600086e1d670dc3c6bdab004f`.

The CTO half stays owed. This half does not stand in for it.

## The question my withdrawn r19 half missed, asked first

`token_broker.NeedsLogin` sends EVERY user without a usable token to `/login`. So the test for property (a) is not who
used `/login`. It is whether any identity that `NeedsLogin` can send there is now refused. It is answered by reading
the rule's own code path, not the admit-set census alone (S62 limits that census to identities with access state).

**`login_admit_decision`, release `server.py`, read whole.** On the GUI path `get_current_principal()` is None, so for
every person the decision is:

1. **Empty email:** refused.
2. **Server-held identity** (`OTP_MAILBOX` / `MS_INGEST_IDENTITY`): admitted.
3. **Restricted profile:** the `principal is not None` branch is skipped, because the GUI path carries no principal.
   Restricted profiles are refused earlier, by GuardMiddleware's email-deny guard, which is unchanged.
4. **Provider check:** `_provider_is_verified(cfg)`. `tier.py:38` holds `_ALWAYS_VERIFIED = {"alb_oidc"}`, and live
   runs `IDENTITY_PROVIDER=alb_oidc`, so this is True.
5. **Tier:** `resolve_tier(None, cfg)` returns `Tier.READ_ONLY`; `tier.py` step (2) gives the floor on no principal,
   with no exception path.
6. **Graph tools at that tier:** `_tools_carried_at(READ_ONLY, email, _graph_using_tools())`. `guard.enforce`
   (`guard.py:31-69`) RETURNS for every SAFE (read) tool before it looks at email or tier, so READ_ONLY carries every
   SAFE Graph-using tool. The verdict is admitted, with reason `tier_graph_tools`.

No step keys on the person's email beyond the server-held set and the unchanged deny guard. So every verified,
non-denied tenant identity reaches the same admit, whether or not it has access state, and S62's limit is closed by the
code path, not only by the rule's text. The effective admit set is unchanged, as R25.4 states.

## Independently measured (2026-10-06 ~07:5xZ-08:0xZ)

**Bytes.**
- `cf4b036e62` is an ancestor of `2c27f3a795` (rc 0).
- `git diff --stat 2c27f3a795 f237f0b676 -- infra/aws/ec2/opal-gateway` is EMPTY: the release equals CLOUD.

**`audit.log_login`.** One record per request: `event`, `outcome` (a closed set), a `reason` code capped at 80
characters, `email_digest` (a salted sha256, never the address), `tier`, and the principal key when known. It has no
token, code, state or cookie input. The GuardMiddleware refusals (deny list, no verified identity, blocklist) and each
callback branch write one record each.

**Rehearsal on the staged release bytes** (`r20_login_after_stage.out`): `LOGIN_ARMS after: 10 of 10 RESULT: PASS`.
- A non-restricted verified identity, the analyst service identity and the server-held identity are admitted, each
  with 307 and consent reached.
- A restricted identity is refused 403 by the deny guard.
- Planted and absent identities get 401.
- With the provider unverified, a person is refused `tier_unresolvable` while the server-held identity is still
  admitted.
- No address, token or state appears in any record, and 8 records were written for 8 requests.

The expected-before FAIL lines in the same file are the negative control, and they show the arms discriminate.

**`engine.py`.** The RSS-poll ctypes objects are built once. The values are equal: the own-process poll matches
`/proc` VmRSS, the child poll matches `/proc` twice, and `pid_alive` is right (`r20_engine_after_stage.out`, 3 of 3).

## The writers

The ask counts N = 2 for (a). There is a third, unchanged writer: the tool registry and its classification, which feed
`_graph_using_tools` (`mcp` registrations, `integrations.registry`, `classify()`). If that set were ever empty, or held
no SAFE tool, the backstop would refuse every person. This is fail-closed by design, but it would be a silent lockout of
the recovery path. That is why W2 requires the ADMITTED arm on the deployed host, not only on staged bytes.

## Guards

- **W1 -- live is re-read before the act** (Phase B step 1). If live is not `cf4b036e62`, this half lapses with the
  pins.
- **W2 -- the after-read on the DEPLOYED host shows:**
  - a non-restricted verified identity ADMITTED with reason `tier_graph_tools`, which proves the backstop does not fire
    in production;
  - a restricted identity refused;
  - one `gw_login` per request, with no address, token or state;
  - engine RSS values equal;
  - `.env` at 51 names with every value hash unchanged;
  - the 65 tools.
- **W3 -- the drain-back check (R16) is recorded:** `rl8.AC2` reads CLOUD equal to the deployed release.

-- 3.0.0_SA_CVO~O
