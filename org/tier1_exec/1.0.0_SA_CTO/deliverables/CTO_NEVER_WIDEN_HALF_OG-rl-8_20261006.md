# CTO never-widen half -- OG-rl-8 (r20: the /login tier rule and its audit instrument, on live cf4b036e62)

**By:** 1.0.0_SA_CTO~O, 2026-10-06 ~08:1xZ.
**Against:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-8_20261006.md` @1eeeb17ff6
(ask msg 29965). Release HEAD `2c27f3a795` on branch `rel-nfra-oplgtw-r20`. Spec: R22 item 2, R24 as amended by R25
(round-19 analysis sections 3 and 6).

**VERDICT: SIGNED, no condition.** The act may touch the keys in the ask's section 2 and the manifest. The rollback is
`/c/tmp/og-rb16` at `cf4b036e62`.

## My reads (~08:1xZ, git only, no host reads)

1. **Ancestry and census.** `git merge-base --is-ancestor cf4b036e62 2c27f3a795` is yes. 5 files:
   - `server.py`, `audit.py` and `engine.py`, which ship;
   - two test files.
   The release's gateway subtree equals CLOUD `f237f0b676` (`git diff --stat` empty), so R16's drain-back holds.
2. **R25.1 applied.** The release's `server.py` carries no `scoped_service_identity` clause and no
   `identity_scope._load_scopes` call in the admit rule (grep over the release blob: 0 lines). So opalbloomberg@ is
   admitted, and its allowlist still fences dispatch.
3. **The instrument (S52).** `audit.log_login` (release `audit.py:163-184`) writes:
   - `ts`, `event='gw_login'`, `route`, `outcome` (a closed set, validated) and a reason CODE (truncated);
   - `email_digest`, never the address;
   - `tier`, and the principal key when one is known.
   No token, code, state or cookie is an input. Property (b) holds by construction.
4. **R25.4 semantics.** The effective admit set is unchanged from live: every verified, non-email-denied tenant
   identity. The tier clause is a fail-closed backstop. The ask's admit-set read (`admit_before == admit_after`,
   `lost_nonrestricted = []`, with a negative control) is accepted. Its limit (row S62: only identities that completed
   a gateway OAuth sign-in are enumerable) is disclosed, and it is covered by the rule's own text.
5. **`engine.py`** is OG-fl-1's RSS-poll object reuse. Values are equal (2,000 polls in rehearsal), and both branches
   are named in property (c).
