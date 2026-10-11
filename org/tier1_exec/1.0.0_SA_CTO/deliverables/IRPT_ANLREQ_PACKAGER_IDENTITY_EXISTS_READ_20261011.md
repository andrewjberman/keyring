# Does an identity exist for `svc-irpt-packager`? -- read only, with `svc-commentary` as the control

Executor: `1.0.0_SA_CTO` on the laptop, 2026-10-11 15:05:29Z, for `2.0.0_SA_COO~G2`'s cross-box ask `XB-20261011T150025Z-6f1a`
(`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/CROSSBOX_ASK_PACKAGER_IDENTITY_EXISTS_20261011.md`; CTO~DELL2 msg
5177). What leaves the laptop: yes/no, names, a user type, an active flag, a firm id, dates. No value, token, password or address
of a person.

Instruments: portal users table `opal-users-v2` (keys `PK`/`SK`; a service user's row is `USER#<service address>` / `PROFILE`,
the form the second control `svc-irpt-analysis` reads under); Secrets Manager `list-secrets` (117 secrets, names and
LastChangedDate only); Cognito `list-user-pools` in us-east-1; IAM `list-roles` (303) and `list-users` (9).

| answer | `svc-irpt-packager` (the question) | `svc-commentary` (the control) |
|---|---|---|
| 1. users-table row | **NO** (4 key forms tried: `USER#<subject>`, `USER#<subject>@opalinvest.com`, bare, bare address) | **NO** (same 4 forms) |
| 2. credential: a secret carrying the subject | **NO** | **YES**: `opal/ticketing/svc-commentary`, last changed 2026-10-09T01:13:37Z |
| 2b. user pool | no user pool exists in us-east-1 (0 pools): service sign-ins are not kept in Cognito | same |
| 3. IAM role or user named for it | **NO** | **NO** role or user carries `svc-commentary`; three commentary ROLES exist and are not it: `irpt-commentary-composition-read-role`, `irpt-commentary-draft-store-role`, `outlook-global-commentary-draft-role` |

Control validity: `svc-commentary` reads PRESENT on answer 2 (its secret) and ABSENT on 1 and 3, so the read is not void. A
second control, `svc-irpt-analysis`, reads PRESENT on 1 (users row `USER#svc-irpt-analysis@opalinvest.com` / `PROFILE`:
`userType` service, `active` absent, `firmId` opal-capital, `allowedFirmIds` present) and on 2 (`irpt/svc-irpt-analysis/password`,
last changed 2026-10-11T07:37:11Z, the window-9 restore), which shows both shapes a service identity takes in this estate.

Reading, for the attach pair: NO identity of any kind exists for `svc-irpt-packager` today. The control shows two patterns: a
portal service USER (users row + password secret, `svc-irpt-analysis`) and a ticketing service TOKEN (secret only, no users
row, `svc-commentary`). The pair CREATES; which pattern it creates is dell2's design call.

Not done: no write, no create, no rotate, no secret value read, no grant.
