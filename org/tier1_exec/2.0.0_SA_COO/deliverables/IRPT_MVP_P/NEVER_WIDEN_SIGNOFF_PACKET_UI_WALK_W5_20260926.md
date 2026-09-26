# Never-widen sign-off packet -- WINDOW 5: the bounded admin + internal + Dev principal for ~D's C25 walk (read-only)

**For:** `1.0.0_SA_CTO` (half 1) and `4.0.0_SA_CRO` (half 2). **Prepared by / operator of create and delete:**
`2.0.0_SA_COO~P`, 2026-09-26 ~21:4xZ. **Asked by:** `2.0.0_SA_COO~D` 101495. **Walker:** `2.0.0_SA_COO~D` only.
**Ledger (opened before any write):** `irpt-ui-walk-principal-w5-20260926`.

This packet is the window-4 shape with a SMALLER write set: no upload, no submission, no export. Where it says "as
v10", the text is `NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_ADMIN_DEV_PRINCIPAL_20260926.md` blob 32c85e40, at the lines
cited.

## 1. What the window is for

~D's C25 acceptance walk: IVE33-AC3, IVE34-AC3 and IVE36. It runs on a LOCAL portal build, DEV fdccc6e6 plus IV-e-36,
served at `localhost:5174` against the live IR API. The HAR is scrubbed in-stream as in windows 2-4, and it also
answers what `2.0.0_SA_COO~M` is waiting on.

Named observations (reads already inside the admitted classes, NOT extra acts):
- Performance in the page now runs on adapter `Ll6t4VPa` (S147 fix M) and `8a6zq+` (P-REOPEN-01). A first open of a
  new account/window should render under the 30 s gateway cap (served: 6.2-6.9 s), and a reopen by this second
  principal should render. The window-4 K7 account (JASON JONES ****9978, YTD) is the natural re-read.

## 2. Keys

| key | what | rollback / retention |
|---|---|---|
| K1 | ONE `opal-users-v2` PROFILE item, `USER#usr_irptuiwalk_<epoch>` / `PROFILE`: `role admin`, `firmId opal-capital`, `userType Dev`, `status active`, no MFA / phone / advisor / FIRM# fields -- exactly as v10 `:101-131` | `DeleteItem`, verified by a failing consistent `GetItem` |
| K1-CRED | SSM SecureString `/irpt/ui-walk-principal/<epoch>/password` (`alias/aws/ssm`), read by ~D BY NAME into browser memory only | `delete-parameter`, verified by `ParameterNotFound` |
| K2 | the session: access 15 min, refresh re-reads K1, so it dies with K1; walk <= 60 min from the login -- as v10 `:214-218` | dies with K1 |
| K3 | the page's own SELECTION# rows in `irpt-requests` (content-addressed, identity-free) -- as v10 `:132-142` | RETAINED; before/after census with each new id traced to a HAR `/selections` POST |
| K9 | retained Performance reports the page's GETs compute (REPORT#/ARTIFACT#/RETENTION# + blobs, the human-read path) | RETAINED, as every human read's; the new REPORT# ids listed from the HAR's responses |

Nothing else is written: no upload (K4), no submission (K5), no export (K8), no render grant.

## 3. The blast radius

This is a superadmin session for its life, exactly as v10 `:220-243`: the authorizer's Dev bypass over all firms, the
edge admin bypass, opal-partners-data at every level, IRPT OPAL_GLOBAL, and the auth-handler's admin write surface
(create/list/delete/reset ANY user). **The mechanical bound is the interval, not the grant.** The bound on what is done
is ~D's script plus the HAR as the whole call list.

**New to this window:** the page is a LOCAL build, not the served portal. The superadmin token lives in a local
browser for the walk. The local bundle is DEV fdccc6e6 plus IV-e-36, and ~D names its build hash in the walk log. The
HAR, not the bundle, is the audit.

**THE LIMIT:** "page use only: reads plus the page's own selection writes; no admin, export, upload, submission, grant
or vendor call."

## 4. The audit, graded by route (denominator printed)

| class | admitted |
|---|---|
| any method | `/auth/login`, `/auth/refresh` |
| POST | `/api/scoped/investor-reporting/directory/resolve` (page load); `/api/scoped/investor-reporting/selections` (each selection -> K3) |
| GET / HEAD / OPTIONS | any page read: directory, holdings, performance (one account at a time), the Export PREVIEW's reads |

Any request outside these classes is branch (d). This includes, explicitly:
- any request of any method to `/auth/admin/`;
- ANY `/export` POST;
- any `/analysis` or `/analysis/inputs` POST;
- any other POST/PUT/PATCH/DELETE.

The census prints the count per class, the count outside (must be 0), and the denominator.

## 5. Branches (as v10 `:271-279`)

- **(a) Walk completes:** delete K1, then K1-CRED, then audit.
- **(b) Walk fails or is abandoned:** the same deletes, the same turn.
- **(c) A delete refuses:** set K1 `status disabled` the same turn, then escalate to the CTO and Andrew.
- **(d) The HAR shows any request outside section 4:** a BLOCKING row; a same-turn user census against the pre-walk
  baseline; escalate to Andrew.

## 6. The sequence (as v10 `:281-312`, minus K4/K5/K8)

1. C: >= 5 GB free. Open the ledger; commit its OPEN sentinel.
2. Pre-read:
   - 0 users with the e-mail;
   - `ParameterNotFound`;
   - the `opal-users-v2` user census (count + status digest);
   - the SELECTION# census;
   - the REPORT# count for 49F / cottonwood / inflection.
3. Put K1-CRED, then K1 (`attribute_not_exists(PK)`); read back; digest with `passwordHash` excluded.
4. Hand over to ~D: the e-mail, the parameter NAME, section 4, and the 60-min deadline.
5. ~D walks at `localhost:5174`, grading IVE33-AC3, IVE34-AC3 and IVE36, with the HAR scrubbed in-stream.
6. Delete:
   - K1, verified by a failing consistent read;
   - one login attempt through `https://opalinvest.dev/auth/login` refused `Invalid email or password`, 1 of 1;
   - K1-CRED, verified by `ParameterNotFound`;
   - ~D reloads once and lands on `/login`.
7. Audit:
   - the route-graded census;
   - SELECTION# and REPORT# re-reads with the new ids traced to the HAR;
   - the user census equal to the baseline;
   - no IRPT or auth request after the last token's `exp`;
   - the interval recorded; close and commit the ledger.

## 7. What the halves sign against

This file's committed blob; the key list K1 + K1-CRED + K2 + K3 (retained) + K9 (retained) for window 5's NEW
principal; the stated superadmin radius including the local-build note; and the sequence's rollback and audit.
