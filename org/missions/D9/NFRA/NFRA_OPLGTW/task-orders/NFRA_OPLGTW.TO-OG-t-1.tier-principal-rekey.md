# NFRA_OPLGTW task order -- `OG-t-1` -- ROUND 2 (E7): the user-type tier keys on the tid/oid principal, never on email (rows W3-S9, S61), BUILD only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-t-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~12</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the design is ruled (R-3 (a)-(f), ROUND_ANALYSIS.round1.md section 3; Q1/Q2 @5676f4a48a).
EGRESS CLASS, declared: NONE. No AWS call, no deploy, no data write.
</preflight>

## 1. THE CELL -- `OG-t-1` (decomposition addendum R2-E, item E7, build half)

**The defect (rows W3-S9, S61).** The contract says: "Carry validated `tid` and `oid` in signed principal context; email is
display/audit metadata only" (C1). The code does the opposite for the user-type tier. `resolve_tier(email, cfg)` gives
MASTER_ADMIN to any caller whose email is in `MASTER_ADMIN_EMAILS`, and STANDARD_EMPLOYEE to any caller in
`WRITE_CAPABLE_EMAILS`. So a second principal holding the same email gets the first one's tier, and the token broker
mints it the first one's Graph scopes.

`GW` = `infra/aws/ec2/opal-gateway`. The bytes at the issuance base (print them before you edit):
- `GW/app/tier.py:69` `def resolve_tier(email: str, cfg) -> Tier:`; the two email checks are at `:87` and `:91`.
- `GW/app/guard.py:75` `tier = resolve_tier(email, cfg)`.
- `GW/app/integrations/base.py:143` `tier = resolve_tier(email, get_config())`.
- `GW/app/token_broker.py:148-156` `_scope_tier(email)`, which calls `resolve_tier(email, _cfg)` at `:154`. It is called at
  `:192` as `_scope_tier(display)` inside `get_token`, after `_cache_owner_for(email)` (`:159-168`) has decided whether
  the request's PRINCIPAL owns the cache (a person) or an email-keyed cache answers ("the machine routes' fixed
  server-held identities", for example `MS_INGEST_IDENTITY`, `GW/app/config.py:203-209`, used by `GW/app/ms_ingest.py`).
- `GW/app/tools.py:124` `_tier_val = _tier.resolve_tier(email, cfg)`.
- `GW/app/config.py:243-260`: the SECURITY-CRITICAL roster comment and `MASTER_ADMIN_EMAILS` / `WRITE_CAPABLE_EMAILS`.
  (The analysis cites `config.py:233-235`; that has DRIFTED to the ENABLED_INTEGRATIONS comment.)
- `GW/app/context.py:41-48`: `Principal(tid, oid, email)`, where email is "display / audit metadata only -- never an
  authorization key"; `.key` is `principal_key(tid, oid)` = `<tid>/<oid>`. `get_current_principal()` is at `:96`.

**The ruled design (R-3, with rulings Q1 and Q2 @5676f4a48a). Build exactly this.**
1. **(a) Re-key the PERSON tier.**
   - `resolve_tier` takes the PRINCIPAL (a `Principal` or `None`) and keys on `principal.key` only.
   - `GW/app/config.py` declares `MASTER_ADMIN_PRINCIPALS` and `WRITE_CAPABLE_PRINCIPALS`: tuples of `<tid>/<oid>`
     strings, read from the environment variables of the same names, whitespace/comma split, each normalised through
     `context.principal_key`. Their config default is EMPTY. No real tid/oid is ever written into code, tests or config
     defaults: the release (`OG-t-2`) puts the values in the host `.env`.
   - `resolve_tier` reads NO email set.
   - Move the person sites: `tier.py:69` (the signature); `guard.py:75` (`resolve_and_enforce` gains the principal from
     `get_current_principal()`); `integrations/base.py:143`; `tools.py:124`; and in `token_broker.get_token` the branch
     where `_cache_owner_for` returned the PRINCIPAL's cache. Every person site passes `get_current_principal()`, never
     an email.
   - Keep the root-of-trust floor: an unverified provider floors EVERY principal to READ_ONLY (`tier.py:83-84`).
2. **(b) The floor.** A person request with no principal (no `tid`/`oid`) resolves to READ_ONLY. That includes the
   ALB-email GUI path (`context.set_current_email`, `:105-109`). There is NO email fallback for a person.
3. **(f) + Q1 -- machine and bearer paths are OUT of R-3's scope, and must not move.** The machine routes' server-held
   identities (the email-keyed branch of `token_broker._cache_owner_for` / `get_token`, reached by `ms_ingest.py` via
   `get_token(get_config().MS_INGEST_IDENTITY)`) are not persons. They must NEVER reach `resolve_tier` as a person, and
   the Graph scopes they mint must be EXACTLY what they mint at the issuance base. Build it so:
   - that branch resolves its tier by a separate, named machine-identity rule in `token_broker.py` that reproduces the
     base behaviour for server-held identities (today: an identity in `MASTER_ADMIN_EMAILS` or `WRITE_CAPABLE_EMAILS`
     gets the full envelope, else read-only). The two email rosters therefore STAY in `config.py`, read ONLY by that
     machine-identity rule, never by `resolve_tier`; the SECURITY-CRITICAL comment (`:243-250`) is corrected to say
     exactly that and to match `context.py:41-48` for persons;
   - `GW/app/ms_ingest.py` is not edited.
4. **(f) + Q2 -- named and NOT moved.** These are not read by `resolve_tier`, and this cell does not touch them:
   `DASHBOARD_OWNER_EMAILS` (`GW/app/owner_gate.py`); the `/sprint` roster (`GW/app/sprint_view.py`); the per-identity
   tool allowlist (`GW/identity_tool_allowlist.txt`, `GW/app/identity_scope.py`, still email-keyed -- W3-S9 stays ARMED
   on it for round 3); the `/query/v0` catalog principal (`GW/app/query_v0.py`, same); the `email_deny` record
   (`GW/app/data_entitlement.py`, denial-only by design, C2); and `GW/app/ms_ingest.py` (the machine path). AC1 proves
   no commit of yours touches any of them.
5. **(d) Negative arms.**
   - A genuine token carrying the admin's email but a DIFFERENT `oid` is NOT master admin.
   - The broker mints that token no admin scope.
   - The admin principal with a CHANGED display email stays master admin.
6. **Tests.** New `GW/tests/test_tier_principal.py` (moto is not needed; use the config and context seams). It has
   exactly these 8 tests; fixture principals use synthetic GUIDs, never a real tid/oid:
   - `test_admin_principal_resolves_master_admin`
   - `test_same_email_other_oid_is_not_admin`
   - `test_changed_display_email_stays_admin`
   - `test_no_principal_resolves_read_only`
   - `test_write_capable_principal_resolves_standard`
   - `test_broker_mints_no_admin_scope_for_same_email_other_oid`: through `token_broker._scope_tier`/`_scopes_for_tier`
     on the person branch
   - `test_unverified_provider_floors_every_principal`
   - `test_machine_paths_never_reach_resolve_tier`: with `tier.resolve_tier` patched to raise, the server-held-identity
     branch of `get_token` (MS-ingest identity, no principal on the request) resolves its scopes WITHOUT calling it,
     and those scopes equal what the base rule gives that identity (full envelope when it is in a roster, read-only
     otherwise). This is ruling Q1's measured claim.
   Update `GW/tests/test_min_tier_gate.py` and `GW/tests/test_attachment_tools.py` only where they set the email
   rosters for a PERSON, and do not weaken any assertion.

## 2. BOUNDS

1. Code and tests only. No AWS call, no deploy, no `.env` edit, no data write. The release, the `.env` roster values and
   the blast-radius pre-read are `OG-t-2`'s.
2. Every test run sets `AUDIT_PATH` to a temp file. Some suites still append to the TRACKED `GW/audit.jsonl` anyway
   (row W3-S2). If it is dirtied, restore it to HEAD bytes and never commit it. The checks do this and say so.
3. Do not edit `org/standards/NFRA_OPLGTW_CONTRACT.json`: C1 already requires this, and no addendum exists or is needed.
4. You work in the worktree named in your identity line. Standing: no push, no vendor call, never `git stash`. REFUSE a
   criterion you cannot meet as written and report it with its measurement. Never repair or widen one. If item 3 cannot
   be built without moving a named out-of-scope file, that is ONE BLOCKING row -- never a widened edit.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tier.py
infra/aws/ec2/opal-gateway/app/guard.py
infra/aws/ec2/opal-gateway/app/integrations/base.py
infra/aws/ec2/opal-gateway/app/token_broker.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/tests/test_tier_principal.py
infra/aws/ec2/opal-gateway/tests/test_min_tier_gate.py
infra/aws/ec2/opal-gateway/tests/test_attachment_tools.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~12/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: `GW/app/context.py`, `GW/app/ms_ingest.py`, and the named out-of-scope files in 1.4.

Rows go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W12-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-t-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/tk.AC1.sh; echo "exit=$?"</invocation><expect>email sets read by tier.py=0; email-keyed resolve_tier call sites=0; principal rosters declared=2 of 2; out-of-scope named=7 moved=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-t-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/tk.AC2.sh; echo "exit=$?"</invocation><expect>named tests passed 8 of 8; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-t-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/tk.AC3.sh; echo "exit=$?"</invocation><expect>RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

- `AC1` -- R-3 (a) and (f): tier.py reads no email set, no call site passes an email to `resolve_tier`, the two
  principal rosters are declared, and none of the 7 named out-of-scope files is touched by your commits (Q1/Q2).
- `AC2` -- R-3 (b) and (d) plus Q1: the 8 named tests pass.
- `AC3` -- regression control: the moto-free suites around tier, guard, owner gate, deny, identity scope and sprint
  still pass, 47 or more, none failed.

## 5. WHEN YOU ARE DONE

Write the instance to `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~12/NFRA_OPLGTW.TO-OG-t-1.tier-principal-rekey.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once:
- the diff stat per file;
- the 8 test names;
- AC1-AC3 literal output;
- that `GW/audit.jsonl` is clean at HEAD;
- commit hashes;
- rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~12, queue position 1 (then `OG-u-1`, `OG-u-2`, and the release `OG-t-2`).
- Q1/Q2 folded (@5676f4a48a): machine/bearer paths out of scope with a measured no-`resolve_tier` test; `identity_scope.py`
  and `query_v0.py` named out of scope, W3-S9 stays ARMED on them (owner this seat, round-3 enrichment).
- The admin and write-capable principal VALUES are not needed by this build: config reads them from the environment, the
  tests use synthetic fixtures, and the values land in `OG-t-2`'s `.env`. `ADMIN_PRINCIPAL` comes from the switchover
  sitting's Part D record.
- The issuer's reading of Q1's "0 tier deltas for machine callers": the machine-identity rule keeps the email rosters for
  server-held identities only. If the CTO rules those rosters must go too, that is a recut, not a worker call.
- Live rosters (SSM e9790c77, keys only, 2026-09-28): `MASTER_ADMIN_EMAILS=andrew@...`, `WRITE_CAPABLE_EMAILS` two
  addresses, `IDENTITY_PROVIDER=alb_oidc`.
- `<risk>` WORLD is GATE (xii)'s floor (an `infra/` path); the cell deploys nothing.

<status>pending</status>
<round>3</round>
<slot>~12</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
