# Backend Authorization Enforcement — Partner Advisor Scoping (Inflection-first)

**Author:** 0.4.0_DE_ClientPlatform · **Date:** 2026-06-29 · **Trigger:** Andrew-direct (Inflection noel@/patrick@ identity issue → "scope the backend work")
**Status:** SCOPE / PLAN (analysis only — route to COO to formalize as TO; backend build is AE/DT lane)

---

## 0. Correction to the record (grounding)

My first read told Andrew the admin/user split was "frontend-enforced only; the authorizer
doesn't propagate firmRole." **That was wrong.** Source-confirmed reality:

- `portal_authorizer/index.mjs:97,101` DOES propagate `role` (=firmRole, admin|user) **and**
  `advisorId` into the request context (signed RS256 JWT, verified at the edge/authorizer).
- The partner data Lambda `opal-partners-data` (v2.10) **already enforces real backend scoping**:
  - **Firm-level:** `is_authorized(firm_id, allowedFirmIds)` — a user cannot read another FIRM's data (JWT-gated).
  - **Client-PII:** `_pseudonymize_s3_response` / `_filter_partner_analytics` hash client names for non-own-book views (own book = `segment.key == advisorId`).
  - **Role-strip:** `_apply_implementor_strip_to_response` strips clients[]/tax/cost-basis for `advisorRole == 'implementor'` (aggregate-only).

So backend enforcement EXISTS. The work is to **close specific gaps + remove a 49F-only concept
that is noise for Inflection**, not to build authz from scratch.

---

## 1. Confirmed gaps (source-grounded)

### G1 — Own-book IDOR on the advisor-book / drilldown routes (highest priority)
Router (`lambda_function.py:1791-1801`):
```python
elif '/advisors/' in path and '/book' in path:
    path_advisor_id = extract_path_param(path, 'advisors')   # attacker-controlled
    book_resp = _pseudonymize_s3_response(
        handle_advisor_book(bucket, path_advisor_id), user_role, firm_id, advisor_id)
    if not admin_bypass and advisor_role == 'implementor':
        book_resp = _apply_implementor_strip_to_response(book_resp)
    return book_resp
```
`path_advisor_id` (the requested advisor) is **never checked against** `advisor_id` (the caller's own
JWT advisorId) for non-admins. A non-admin `user` with a valid token can request
`/advisors/{any_advisor_in_their_firm}/book` and receive that advisor's **aggregate book**
(total_aua, accounts_count, fee headline, role_breakdown) — only client *names* are hashed, and for
Inflection (all `advisorRole=architect`, level 3) the implementor strip never fires, so they get the
full aggregate. Reachable by direct API call (the authorizer returns `isAuthorized:true` for any
valid token regardless of role; the FE merely hides the Books tab from non-admins).
**Fix:** for non-admin callers, require `path_advisor_id == advisor_id` (own book only) → else 401/403
(401 per the existing CF-error-swallow note at :1674). Same gate on the platinum summary route (:1846).

### G2 — Authorizer claim parity (firmRole / advisorRole present on one entry path, absent on the other)
The data Lambda reads `auth_context.get('firmRole')` and `auth_context.get('advisorRole')`
(:1651-1654), but the **API Gateway authorizer** (`portal_authorizer/index.mjs`) only sets
`role`, `firmId`, `advisorId` — NOT `firmRole`/`advisorRole`. Those are only populated on the
**CloudFront / auth-validator-edge** path ("backwards compatibility during authorizer migration",
:1658). So enforcement that keys on `firmRole`/`advisorRole` silently degrades to `'null'` depending
on which entry path served the request. **Fix:** make the two authorizers emit an identical claim set
(or collapse to one), so backend gates are deterministic regardless of entry path.

### G3 — `advisorRole` ("architect"/"implementor"/...) is a 49 Financial concept, irrelevant to Inflection (Andrew-direct 2026-06-29)
`_ADVISOR_ROLE_LEVEL = {'implementor':1,'local_ops':2,'consultant':2,'architect':3}` is a 49F
role-tier model. Every Inflection row is set to `advisorRole=architect` (spurious — it just means
"no strip"). Andrew: there is **no advisor-role concept for Inflection**. **Fix:** the role-strip
ladder must be **firm-scoped** (49F-only), and Inflection rows should not carry a meaningless
`advisorRole`. Provisioning (AE's new scripts) should not write `advisorRole` for Inflection.

---

## 2. The intended boundary (to ratify before build)

| Caller class | Firm data | Own book | Other advisors' books (same firm) | Other firms |
|---|---|---|---|---|
| internal / opal-capital / Dev | all | n/a | yes | yes |
| firm **admin** (e.g. peter@) | full firm-wide | n/a | yes (leaderboard + drill) | no |
| firm **user** w/ advisorKey (e.g. patrick@) | Distribution (full) | yes | **NO** (G1 closes this) | no |
| firm **user** w/o advisorKey — viewer (e.g. noel@) | Distribution (full) | none (no Profile tab) | no | no |

Open ratification Qs for COO/Andrew:
- (a) Should a firm **user** see firm-wide **aggregate** Distribution (current: yes, full fidelity) — confirm that's intended vs. own-book-only?
- (b) Is the client-name hashing (vs. hard 403) the right boundary for the residual non-own-book aggregate, or should non-admins get a hard deny on any non-own advisor route?

## 3. Proposed phases (AE/DT build; DE = FE rule + interface concur; CVO = verify)
- **P0 (validate):** live PoC — with patrick's (user) token, curl `/advisors/{peter_lee}/book` and confirm the aggregate returns (proves G1 exploitable) before building. ~30 min.
- **P1 (G1):** add own-book ownership gate for non-admins on book + platinum-summary + drilldown routes. Highest value, smallest change.
- **P2 (G2):** authorizer claim parity (firmRole/advisorRole on both paths, or single authorizer). Add `advisorId` to the shared `opal_auth.UserClaims` dataclass (currently omitted) so Python data lambdas can scope uniformly.
- **P3 (G3):** firm-scope the advisorRole strip ladder to 49F; stop writing `advisorRole` for Inflection in provisioning.
- **P4 (FE, my lane — DONE for the reported case):** Profile tab gated on resolved `advisorId` (no advisorKey → no /Profile tab). Shipped Inflection (portal `adda3e0e`); generalize the same rule to 49F/demo/cottonwood non-admin pages on concur.

## 4. Compiler tools
`comp-which` (routing — mis-matched, fell back to source read), Grep/Read over the authorizer +
opal-partners-data Lambda + shared opal_auth; live `aws dynamodb scan` on opal-partner-inflection
(operational, off-rail). No comp-iam/comp-routes run — this is app-layer authz inside one Lambda's
router, not IAM/CF surface; flagged for the build phase (comp-iam service opal-partners-data before
any iam change).
